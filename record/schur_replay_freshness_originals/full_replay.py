#!/usr/bin/env python3
"""Portable, source-bound exact Schur controls, with immutable expected bytes.

No-argument invocation runs both exact families under normal Python in a
throwaway directory. Use --output-dir DIR --modes normal optimized for durable
provenance and optimizer controls. Only bounded finite algebra is certified.
"""
from pathlib import Path
import argparse
import ast
import datetime
import hashlib
import importlib.util
import json
import os
import platform
import resource
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[3]
BINDING_PATH = 'record/schur_reduction_source_bindings.json'
BINDING_SHA256 = '334f0ec42d59b37668ea2e4fe2cb93fdb0525927ff7b725e0652fe0b5ce2ea14'
FAMILIES = {
    'author': {'script': 'computations/verification/schur/author_checks.py',
               'expected': 'evidence/schur_reduction_20261007/raw/author/verified_checks.json',
               'cpu_seconds': 60, 'wall_seconds': 70},
    'independent': {'script': 'computations/verification/schur/independent_checks.py',
                    'expected': 'evidence/schur_reduction_20261007/raw/review/checks.json',
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


def cache_inputs(root):
    """Read and authenticate all input bytes before any checker is executed."""
    manifest_raw = (root / BINDING_PATH).read_bytes()
    require(digest(manifest_raw) == BINDING_SHA256, 'source binding manifest mismatch')
    bindings = json.loads(manifest_raw)
    require(bindings['schema'] == 'bgs-schur-source-bindings-v1', 'binding schema')
    frozen = {BINDING_PATH: manifest_raw}
    for path, expected in bindings['files'].items():
        item = Path(path)
        require(not item.is_absolute() and '..' not in item.parts, 'unsafe source path')
        value = (root / item).read_bytes()
        require(digest(value) == expected, 'source hash mismatch: ' + path)
        frozen[path] = value
    return frozen


def load_comparison(root):
    spec = importlib.util.spec_from_file_location('bgs_schur_comparison',
        root / 'computations/verification/schur/comparison.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
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
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    begin = time.monotonic()
    frozen = cache_inputs(root)
    # These executing sources are pinned by the entry-point/outer delivery seal.
    # Cache their actual bytes too, so before/after provenance covers the runner.
    for path in ('computations/verification/schur/full_replay.py',
                 'computations/verification/balanced_pair_schur.py'):
        frozen[path] = (root / path).read_bytes()
    # Expected raw bytes are cached now, before imports or child execution.
    expected = {family: bytes(frozen[entry['expected']])
                for family, entry in FAMILIES.items()}
    comparison = load_comparison(root)
    for family in FAMILIES:
        comparison.separate(comparison.parse_json(expected[family]), family)
    planned = [output / name for name in ('comparison.json', 'execution_manifest.json')]
    planned += [output / (family + '_' + mode + suffix)
                for family in FAMILIES for mode in modes
                for suffix in ('.json', '_scientific.json')]
    protected = {(root / path).resolve() for path in frozen}
    require(not any(path.resolve() in protected for path in planned),
            'output would overwrite authenticated source or historical evidence')
    output.mkdir(parents=True, exist_ok=True)
    records = []
    tests = []
    failure = None
    report = {'status': 'running', 'runs': records, 'controls': tests,
              'mathematical_scope': 'exact finite controls only; actual radial limit, '
                 'off-charge, higher factorial, TRACE-005 and BGS remain OPEN'}
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
                    import_code = ('import importlib.util; p=' + repr(str(script))
                        + '; s=importlib.util.spec_from_file_location("port",p); '
                        'm=importlib.util.module_from_spec(s); s.loader.exec_module(m)')
                    for label, command in [('silent import', prefix + ['-c', import_code]),
                                            ('silent no-argument port', prefix + [str(script)])]:
                        prior = sorted(str(p.relative_to(output)) for p in output.rglob('*'))
                        result = execute(command, output, family, 20)
                        require(result['exit_status'] == 0 and not result['stdout']
                                and not result['stderr'], family + ' ' + label + ' failed')
                        require(prior == sorted(str(p.relative_to(output)) for p in output.rglob('*')),
                                label + ' wrote files')
                        tests.append({'family': family, 'mode': mode, 'check': label, **result})
                    # Force the first actual mathematical failure condition true.
                    # This targets its explicit failure branch, not the CLI parser.
                    negative = ('import ast,pathlib; t=ast.parse(pathlib.Path('
                        + repr(str(script)) + ').read_text()); '
                        'f=next(n for n in t.body if isinstance(n,ast.FunctionDef) and n.name=="run_checks"); '
                        'n=next(n for n in ast.walk(f) if isinstance(n,ast.If) and any(isinstance(x,ast.Raise) for x in n.body)); '
                        'n.test=ast.Constant(value=True); ast.fix_missing_locations(t); '
                        'g={"__name__":"negative_control"}; exec(compile(t,"negative_control","exec"),g); g["run_checks"]()')
                    result = execute(prefix + ['-c', negative], output, family, 20)
                    require(result['exit_status'] != 0 and
                            ('AssertionError' in result['stderr'] or 'RuntimeError' in result['stderr']),
                            'mathematical failure branch vanished: ' + family)
                    tests.append({'family': family, 'mode': mode,
                                  'check': 'active explicit mathematical failure', **result})
                path = output / (family + '_' + mode + '.json')
                result = execute(prefix + [str(script), '--output', str(path)], output, family)
                require(result['exit_status'] == 0 and not result['stdout'] and not result['stderr'],
                        'exact replay failed: ' + family + ': ' + result['stderr'][-1600:])
                scientific, provenance = comparison.compare(expected[family], path.read_bytes(), family)
                if previous is not None:
                    require(previous == scientific, family + ' normal/-O scientific bytes differ')
                previous = scientific
                scientific_path = output / (family + '_' + mode + '_scientific.json')
                scientific_path.write_bytes(scientific)
                records.append({'family': family, 'mode': mode,
                                'resource_caps': {**entry, 'memory_bytes': MEMORY_BYTES,
                                    'cpu_affinity': 'inherited, not pinned',
                                    'library_thread_environment': THREAD_ENV},
                                **result, **provenance})
    except Exception as error:
        failure = str(error)
    changed = [path for path, raw in frozen.items()
               if not (root / path).is_file() or (root / path).read_bytes() != raw]
    if changed:
        failure = (failure or '') + ' input bytes changed: ' + ', '.join(changed[:12])
    report.update(status='passed' if failure is None else 'failed', failure=failure,
                  inputs_unchanged=not changed,
                  separated_paths=['/runtime_seconds', '/python', '/sympy'],
                  expected_bytes_cached_before_execution=True,
                  comparison_is_recursive_key_filter=False)
    (output / 'comparison.json').write_text(json.dumps(report, indent=2) + '\n')
    import sympy
    artifacts = sorted(p for p in output.iterdir() if p.is_file()
                       and p.name != 'execution_manifest.json')
    artifact_root = Path(os.path.commonpath([root.resolve(), output.resolve()]))
    source_paths = [str((root / path).resolve().relative_to(artifact_root)) for path in sorted(frozen)]
    source_pairs = list(zip(sorted(frozen), source_paths))
    output_paths = {p: str(p.resolve().relative_to(artifact_root)) for p in artifacts}
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
                            'sha256_after': digest((root / path).read_bytes()) if (root / path).is_file() else 'missing'}
                           for path, relative in source_pairs],
        'execution_artifacts': source_paths,
        'declared_results': [output_paths[p] for p in artifacts],
        'outputs': [{'path': output_paths[p], 'sha256': digest(p.read_bytes()), 'kind': 'result'} for p in artifacts],
        'checks': [{'check': 'source-bound exact finite replay', 'passed': failure is None}],
        'result': 'implementation and finite assertion verified in the stated range' if failure is None else 'failed',
        'residual_risks': ['Symbolic-library trust; finite controls are not universal analytic proof.',
                           'No external-referee, priority, or Lean certification.'],
    }
    (output / 'execution_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
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
    return run_replay(args.output_dir.resolve(), args.modes, not args.skip_controls)


if __name__ == '__main__':
    raise SystemExit(main())
