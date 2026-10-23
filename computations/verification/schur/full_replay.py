#!/usr/bin/env python3
"""Portable, source-bound exact Schur controls, with immutable expected bytes.

No-argument invocation runs both exact families under normal Python in a
throwaway directory. Use --output-dir DIR --modes normal optimized for durable
provenance and optimizer controls. Only bounded finite algebra is certified.
"""
from pathlib import Path
import argparse
import ast
import contextlib
import datetime
import hashlib
import importlib.util
import json
import os
import platform
import resource
import stat
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[3]
BINDING_PATH = 'record/schur_reduction_source_bindings.json'
BINDING_SHA256 = '553d1427d6eb2bbd41ef81136d476f69182caa7d4791185ec2f65c114fb903d7'
FAMILIES = {
    'author': {'script': 'computations/verification/schur/author_checks.py',
               'expected': 'archive/evidence/schur_reduction_20261007/raw/author/verified_checks.json',
               'cpu_seconds': 60, 'wall_seconds': 70},
    'independent': {'script': 'computations/verification/schur/independent_checks.py',
                    'expected': 'archive/evidence/schur_reduction_20261007/raw/review/checks.json',
                    'cpu_seconds': 160, 'wall_seconds': 180},
}
MEMORY_BYTES = 2 * 1024 ** 3
THREAD_ENV = {name: '1' for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS',
              'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS')}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def absolute_path(path):
    """Make a path absolute without erasing a symlink from its ancestry."""
    return Path(os.path.abspath(path))


def check_ancestry(path, allow_missing=False):
    path = absolute_path(path)
    for component in reversed((path, *path.parents)):
        try:
            info = component.lstat()
        except FileNotFoundError:
            require(allow_missing, 'missing path: ' + str(component))
            return path
        require(not stat.S_ISLNK(info.st_mode), 'symlink path/ancestor: ' + str(component))
        if component != path:
            require(stat.S_ISDIR(info.st_mode), 'non-directory ancestor: ' + str(component))
    return path


def read_regular(path):
    path = check_ancestry(path)
    before = path.lstat()
    require(stat.S_ISREG(before.st_mode), 'not a regular file: ' + str(path))
    # Do not follow a leaf switched to a symlink after the ancestry check.
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(fd, 'rb') as stream:
        current = os.fstat(stream.fileno())
        require(stat.S_ISREG(current.st_mode) and
                (before.st_dev, before.st_ino) == (current.st_dev, current.st_ino),
                'file identity changed while reading: ' + str(path))
        return stream.read()


def cache_inputs(root):
    """Authenticate immutable source/reference bytes; never stage them as results."""
    root = check_ancestry(root)
    manifest_raw = read_regular(root / BINDING_PATH)
    require(digest(manifest_raw) == BINDING_SHA256, 'source binding manifest mismatch')
    bindings = json.loads(manifest_raw)
    require(bindings['schema'] == 'bgs-schur-source-bindings-v1', 'binding schema')
    frozen = {BINDING_PATH: manifest_raw}
    for path, expected in bindings['files'].items():
        item = Path(path)
        require(not item.is_absolute() and '..' not in item.parts, 'unsafe source path')
        value = read_regular(root / item)
        require(digest(value) == expected, 'source hash mismatch: ' + path)
        frozen[path] = value
    return frozen


def changed_inputs(root, frozen, identities):
    changed = []
    for relative, raw in frozen.items():
        path = root / relative
        try:
            value = read_regular(path)
            info = path.lstat()
            identity = (info.st_dev, info.st_ino)
            if value != raw or identity != identities[relative]:
                changed.append(relative)
        except (OSError, RuntimeError):
            changed.append(relative)
    return changed


def safe_destination(path, protected, identities):
    path = check_ancestry(path, allow_missing=True)
    require(path not in protected,
            'output would overwrite authenticated source or historical evidence')
    if path.exists():
        info = path.lstat()
        require(stat.S_ISREG(info.st_mode) and info.st_nlink == 1,
                'output target is not an unaliased regular file: ' + str(path))
        require((info.st_dev, info.st_ino) not in identities,
                'output would overwrite authenticated source or historical evidence')
    return path


def write_result(path, raw, protected, identities):
    path = safe_destination(path, protected, identities)
    # Unlink a safe old result before exclusive creation, never truncate an alias.
    if path.exists():
        path.unlink()
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, 'wb') as stream:
        stream.write(raw)


@contextlib.contextmanager
def private_workspace(label):
    # The enclosing directory owns cleanup even if a child replaces its cwd
    # with a symlink. rmtree then unlinks that symlink, not its external target.
    with tempfile.TemporaryDirectory(prefix='bgs-schur-' + label + '-') as directory:
        workspace = Path(directory) / 'child'
        workspace.mkdir()
        yield workspace


def fresh_result(workspace, path):
    try:
        check_ancestry(workspace)
        check_ancestry(path)
        info = path.lstat()
        require(stat.S_ISREG(info.st_mode) and info.st_nlink == 1,
                'not an unaliased regular file')
        require(path.resolve().is_relative_to(workspace.resolve()),
                'result escapes private workspace')
        return read_regular(path)
    except (OSError, RuntimeError) as exc:
        raise RuntimeError('checker did not create a fresh regular contained result: '
                           + str(path) + ': ' + str(exc)) from exc


def load_comparison(root, source_bytes=None):
    spec = importlib.util.spec_from_file_location('bgs_schur_comparison',
        root / 'computations/verification/schur/comparison.py')
    module = importlib.util.module_from_spec(spec)
    # Source bindings authenticate these exact bytes, not a timestamp-valid pyc.
    raw = source_bytes if source_bytes is not None else read_regular(spec.origin)
    exec(compile(raw, str(spec.origin), 'exec'), module.__dict__)
    return module


def limits(cpu):
    resource.setrlimit(resource.RLIMIT_CPU, (cpu, cpu))
    resource.setrlimit(resource.RLIMIT_AS, (MEMORY_BYTES, MEMORY_BYTES))
    # Deliberately no sched_setaffinity: independent jobs need not share a core.


def execute(command, directory, family, timeout=None):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', **THREAD_ENV)
    start = time.monotonic()
    cap = FAMILIES[family]
    try:
        run = subprocess.run(command, cwd=directory, env=env,
            preexec_fn=lambda: limits(cap['cpu_seconds']),
            timeout=timeout or cap['wall_seconds'], capture_output=True, text=True)
        return {'command': command, 'runtime_seconds': time.monotonic() - start,
                'exit_status': run.returncode, 'status': 'completed',
                'stdout': run.stdout, 'stderr': run.stderr}
    except subprocess.TimeoutExpired as exc:
        return {'command': command, 'runtime_seconds': time.monotonic() - start,
                'exit_status': 124, 'status': 'timed_out',
                'stdout': str(exc.stdout or ''), 'stderr': str(exc.stderr or '')}


def run_replay(output, modes, controls, root=ROOT):
    require(type(modes) in (list, tuple) and bool(modes)
            and all(type(mode) is str and mode in ('normal', 'optimized') for mode in modes),
            'replay modes must be a nonempty normal/optimized plan')
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    begin = time.monotonic()
    root = check_ancestry(root)
    output = absolute_path(output)
    frozen = cache_inputs(root)
    # These sources are pinned by the entry point / outer delivery seal.
    for path in ('computations/verification/schur/full_replay.py',
                 'computations/verification/balanced_pair_schur.py'):
        frozen[path] = read_regular(root / path)
    identities = {path: ((root / path).lstat().st_dev, (root / path).lstat().st_ino)
                  for path in frozen}
    # Immutable byte objects remain in the parent, outside every child workspace.
    expected = {family: bytes(frozen[entry['expected']])
                for family, entry in FAMILIES.items()}
    comparison = load_comparison(root, frozen['computations/verification/schur/comparison.py'])
    for family in FAMILIES:
        comparison.separate(comparison.parse_json(expected[family]), family)
    planned = [output / name for name in ('comparison.json', 'execution_manifest.json')]
    planned += [output / (family + '_' + mode + suffix)
                for family in FAMILIES for mode in modes
                for suffix in ('.json', '_scientific.json')]
    protected = {absolute_path(root / path) for path in frozen}
    protected_identities = set(identities.values())
    check_ancestry(output, allow_missing=True)
    for path in planned:
        safe_destination(path, protected, protected_identities)
    output.mkdir(parents=True, exist_ok=True)
    records = []
    tests = []
    generated = set()
    failure = None
    report = {'status': 'running', 'runs': records, 'controls': tests,
              'mathematical_scope': 'exact finite controls only; actual radial limit, '
                 'off-charge, higher factorial, TRACE-005 and BGS remain OPEN'}

    def execute_bound(command, workspace, family, timeout=None):
        result = execute(command, workspace, family, timeout)
        changed = changed_inputs(root, frozen, identities)
        result.update(inputs_authenticated_after_child=not changed,
                      changed_inputs=changed,
                      private_step_workspace=True,
                      original_expected_bytes_staged=False)
        return result

    def save(path, raw):
        write_result(path, raw, protected, protected_identities)
        generated.add(path)

    try:
        for family, entry in FAMILIES.items():
            script = root / entry['script']
            tree = ast.parse(frozen[entry['script']])
            require(not any(isinstance(n, ast.Assert) for n in ast.walk(tree)),
                    'optimization-sensitive assert in ' + family)
            previous = None
            for mode in modes:
                prefix = [sys.executable, '-B'] + (['-O'] if mode == 'optimized' else [])
                if controls:
                    import_code = ('import importlib.util,pathlib; p=' + repr(str(script))
                        + '; s=importlib.util.spec_from_file_location("port",p); '
                        'm=importlib.util.module_from_spec(s); '
                        'exec(compile(pathlib.Path(p).read_bytes(),p,"exec"),m.__dict__)')
                    for label, command in [('silent import', prefix + ['-c', import_code]),
                                            ('silent no-argument port', prefix + [str(script)])]:
                        with private_workspace('control') as workspace:
                            result = execute_bound(command, workspace, family, 20)
                            tests.append({'family': family, 'mode': mode, 'check': label, **result})
                            require(not result['changed_inputs'], 'input bytes changed after '
                                    + label + ': ' + ', '.join(result['changed_inputs']))
                            require(result['exit_status'] == 0 and not result['stdout']
                                    and not result['stderr'], family + ' ' + label + ' failed')
                            check_ancestry(workspace)
                            require(not list(workspace.iterdir()), label + ' wrote files')
                    # Force the first actual mathematical failure condition true.
                    negative = ('import ast,pathlib; t=ast.parse(pathlib.Path('
                        + repr(str(script)) + ').read_text()); '
                        'f=next(n for n in t.body if isinstance(n,ast.FunctionDef) and n.name=="run_checks"); '
                        'n=next(n for n in ast.walk(f) if isinstance(n,ast.If) and any(isinstance(x,ast.Raise) for x in n.body)); '
                        'n.test=ast.Constant(value=True); ast.fix_missing_locations(t); '
                        'g={"__name__":"negative_control"}; exec(compile(t,"negative_control","exec"),g); g["run_checks"]()')
                    with private_workspace('negative') as workspace:
                        result = execute_bound(prefix + ['-c', negative], workspace, family,
                                               entry['wall_seconds'])
                    tests.append({'family': family, 'mode': mode,
                                  'check': 'active explicit mathematical failure', **result})
                    require(not result['changed_inputs'], 'input bytes changed after negative control: '
                            + ', '.join(result['changed_inputs']))
                    require(result['status'] != 'timed_out',
                            'negative control timed out: ' + family
                            + ' (wall budget ' + str(entry['wall_seconds']) + 's)')
                    require(result['exit_status'] != 0 and
                            ('AssertionError' in result['stderr'] or 'RuntimeError' in result['stderr']),
                            'mathematical failure branch vanished: ' + family)
                path = output / (family + '_' + mode + '.json')
                with private_workspace('result') as workspace:
                    child_path = workspace / 'result.json'
                    require(not child_path.exists() and not child_path.is_symlink(),
                            'producer output must be absent before execution')
                    result = execute_bound(prefix + [str(script), '--output', str(child_path)],
                                           workspace, family)
                    record = {'family': family, 'mode': mode,
                              'resource_caps': {**entry, 'memory_bytes': MEMORY_BYTES,
                                  'cpu_affinity': 'inherited, not pinned',
                                  'library_thread_environment': THREAD_ENV},
                              **result, 'output_absent_before_execution': True,
                              'fresh_result_created': False, 'scientific_equality': False}
                    records.append(record)
                    problems = []
                    if result['changed_inputs']:
                        problems.append('input bytes changed after child: '
                                        + ', '.join(result['changed_inputs']))
                    if result['exit_status'] != 0 or result['stdout'] or result['stderr']:
                        problems.append('exact replay failed: ' + family + ': ' + result['stderr'][-1600:])
                    try:
                        raw = fresh_result(workspace, child_path)
                        record['fresh_result_created'] = True
                        # Preserve actual bytes even on scientific/source/exit failure.
                        save(path, raw)
                        scientific, provenance = comparison.compare(expected[family], raw, family)
                        record.update(provenance)
                        if previous is not None:
                            require(previous == scientific, family + ' normal/-O scientific bytes differ')
                        previous = scientific
                        save(output / (family + '_' + mode + '_scientific.json'), scientific)
                    except Exception as error:
                        problems.append(str(error))
                    require(not problems, '; '.join(problems))
    except Exception as error:
        failure = str(error)
    changed = changed_inputs(root, frozen, identities)
    if changed:
        failure = (failure or '') + ' input bytes changed: ' + ', '.join(changed[:12])
    report.update(status='passed' if failure is None else 'failed', failure=failure,
                  inputs_unchanged=not changed,
                  separated_paths=['/runtime_seconds', '/python', '/sympy'],
                  expected_bytes_cached_before_execution=True,
                  comparison_is_recursive_key_filter=False,
                  producer_outputs_absent_before_execution=True,
                  input_authentication_after_each_child=True,
                  shared_generated_dependencies='none: each exact family is self-contained',
                  expected_bytes_outside_child_workspaces=True)
    save(output / 'comparison.json', (json.dumps(report, indent=2) + '\n').encode())
    import sympy
    artifacts = sorted(generated)
    artifact_root = Path(os.path.commonpath([root.resolve(), output.resolve()]))
    source_paths = [str(absolute_path(root / path).relative_to(artifact_root)) for path in sorted(frozen)]
    source_pairs = list(zip(sorted(frozen), source_paths))
    output_paths = {p: str(absolute_path(p).relative_to(artifact_root)) for p in artifacts}
    manifest = {
        'schema_version': 2, 'claim_id': 'BGS-SCHUR-REDUCTION-PORTABLE-REPLAY',
        'artifact_root': str(artifact_root),
        'repository': {'commit': 'none: outside-canonical portable overlay; pinned bytes authoritative', 'dirty': True},
        'command': [sys.executable, '-B', str(Path(__file__).resolve()), '--output-dir', str(output), '--modes', *modes]
                   + ([] if controls else ['--skip-controls']),
        'environment': {'software': [{'name': 'Python', 'version': sys.version},
                                    {'name': 'SymPy', 'version': sympy.__version__}],
                        'hardware': platform.platform()},
        'mathematics': {'assertion_tested': 'Author and independently reconstructed finite exact Schur controls '
                       'match pinned scientific outputs; expected/observed environment retained separately.',
                       'coefficient_domain': 'Q(i), Q(sqrt(3)), exact rational and symbolic arithmetic',
                       'conventions': 'Ordinary traces, independent normalized left coordinate phases, '
                                      'analytic logarithm zero at origin; no changes to tested cases.',
                       'inputs': source_paths,
                       'bounds': {'author': 'N=3, powers 1..6; cycles N=2,3,5,7 through 2N+1',
                                  'independent': 'N=1,2,3,4 powers 5,5,4,4; all N=2,3 orders, two N=4 orders; '
                                      'moments through degree 12; cycles N=1,2,3,4,7 through 3N+1'},
                       'non_claims': [report['mathematical_scope'], 'No analytic recertification or formal proof.']},
        'randomness': {'used': False, 'generator': 'none', 'seed': None},
        'run': {'started_at': started, 'runtime_seconds': time.monotonic() - begin,
                'exit_status': 0 if failure is None else 1,
                'status': 'completed' if failure is None else 'failed',
                'resource_limits': {'memory_bytes': MEMORY_BYTES, 'cpu_seconds': 160,
                                    'max_cores': len(os.sched_getaffinity(0)), 'max_threads': 1},
                'limits_apply_to': 'each child: author 60 CPU/70 wall seconds; independent 160 CPU/180 wall seconds; '
                                   'library thread variables are cooperative; max_cores records inherited allowed CPUs, no affinity override',
                'wall_timeout_seconds': 180, 'per_family_caps': FAMILIES},
        'input_artifacts': [{'path': relative, 'sha256': digest(frozen[path]),
                            'sha256_after': digest(read_regular(root / path)) if path not in changed else 'changed_or_missing'}
                           for path, relative in source_pairs],
        'execution_artifacts': source_paths,
        'declared_results': [output_paths[p] for p in artifacts],
        'outputs': [{'path': output_paths[p], 'sha256': digest(p.read_bytes()), 'kind': 'result'} for p in artifacts],
        'checks': [{'check': 'source-bound exact finite replay', 'passed': failure is None}],
        'result': 'implementation and finite assertion verified in the stated range' if failure is None else 'failed',
        'residual_risks': ['Symbolic-library trust; finite controls are not universal analytic proof.',
                           'No external-referee, priority, or Lean certification.'],
    }
    save(output / 'execution_manifest.json', (json.dumps(manifest, indent=2) + '\n').encode())
    require(failure is None, failure)
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path)
    parser.add_argument('--modes', nargs='+', choices=['normal', 'optimized'], default=['normal'])
    parser.add_argument('--skip-controls', action='store_true')
    args = parser.parse_args(argv)
    if args.output_dir is None:
        with tempfile.TemporaryDirectory(prefix='bgs-schur-') as directory:
            return run_replay(Path(directory), args.modes, False)
    return run_replay(absolute_path(args.output_dir), args.modes, not args.skip_controls)


if __name__ == '__main__':
    raise SystemExit(main())
