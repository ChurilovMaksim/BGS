#!/usr/bin/env python3
"""Bounded portable author/reviewer/synthesis replay, silent unless a check fails.

Run from any directory with python3 -B PATH --output-dir DIR. Default results
must be explicitly placed under the supplied repository root for a portable
manifest. This archival generator is not the no-argument workspace verifier. Scientific comparisons
omit only author elapsed_seconds and reviewer runtime_seconds. No source hash,
Python version, arithmetic record, mathematical value or case is omitted.
"""
from pathlib import Path
import argparse
import ast
import datetime
import hashlib
import json
import os
import platform
import resource
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
PORTS = ROOT / 'computations/verification/fractional_hamming'
RAW = ROOT / 'evidence/fractional_hamming_20261007/raw'


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized(data, family):
    result = dict(data)
    for key in {'author': ['elapsed_seconds'],
                'independent': ['runtime_seconds'], 'synthesis': []}[family]:
        result.pop(key, None)
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args(argv)
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env.update(PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1',
               OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
    cpu = min(os.sched_getaffinity(0))

    def limits():
        os.sched_setaffinity(0, {cpu})
        resource.setrlimit(resource.RLIMIT_AS, (3 * 1024 ** 3, 3 * 1024 ** 3))
        resource.setrlimit(resource.RLIMIT_CPU, (320, 320))

    def execute(command, timeout=360):
        start = time.monotonic()
        run = subprocess.run(command, cwd=output, env=env, preexec_fn=limits,
                             timeout=timeout, capture_output=True, text=True)
        return run, {'command': command, 'runtime_seconds': time.monotonic() - start,
                     'exit_status': run.returncode,
                     'stdout': run.stdout, 'stderr': run.stderr}

    files = sorted(p for p in RAW.rglob('*') if p.is_file())
    files += [PORTS / (name + '_checks.py') for name in ['author', 'independent', 'synthesis']] + [Path(__file__).resolve()]
    before = {str(p.relative_to(ROOT)): sha(p) for p in files}
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    overall_start = time.monotonic()
    expected_paths = {'author': RAW / 'author/results.json',
                      'independent': RAW / 'review/results/verified/all_results.json',
                      'synthesis': RAW / 'review/synthesis_results.json'}
    records = []
    controls = []
    output_files = []
    failure = None
    try:
        for family in ['author', 'independent', 'synthesis']:
            port = PORTS / (family + '_checks.py')
            tree = ast.parse(port.read_text())
            require(not any(isinstance(n, ast.Assert) for n in ast.walk(tree)),
                    'Port retains an optimization-sensitive assert: ' + family)
            expected = normalized(json.loads(expected_paths[family].read_text()), family)
            normal_bytes = None
            for optimized in [False, True]:
                mode = 'optimized' if optimized else 'normal'
                prefix = [sys.executable, '-B'] + (['-O'] if optimized else [])
                import_code = (
                    'import importlib.util, pathlib; '
                    'p=pathlib.Path(' + repr(str(port)) + '); '
                    's=importlib.util.spec_from_file_location("adapter",p); '
                    'm=importlib.util.module_from_spec(s); s.loader.exec_module(m)')
                earlier = sorted(str(p) for p in output.rglob('*'))
                imported, info = execute(prefix + ['-c', import_code], timeout=20)
                require(imported.returncode == 0 and not imported.stdout and not imported.stderr,
                        'Import is not silent or failed: ' + family)
                require(earlier == sorted(str(p) for p in output.rglob('*')),
                        'Import wrote output files: ' + family)
                controls.append({'family': family, 'mode': mode, 'check': 'silent import', **info})
                noop, info = execute(prefix + [str(port)], timeout=20)
                require(noop.returncode == 0 and not noop.stdout and not noop.stderr,
                        'No-argument main is not silent: ' + family)
                controls.append({'family': family, 'mode': mode, 'check': 'silent no-argument main', **info})
                # Exercise an actual converted mathematical check, not merely the CLI.
                if family == 'author':
                    negative_code = import_code + '; m.direct_trace([(0,)], [])'
                elif family == 'independent':
                    negative_code = import_code + '; m.zero(m.s.ones(1,1))'
                else:
                    negative_code = (
                        'import ast, pathlib; '
                        't=ast.parse(pathlib.Path(' + repr(str(port)) + ').read_text()); '
                        'n=next(n for n in ast.walk(t) if isinstance(n,ast.If) and '
                        'any(isinstance(x,ast.Name) and x.id=="ham" for x in ast.walk(n.test)) and '
                        'any(isinstance(x,ast.Raise) for x in n.body)); '
                        'n.test=ast.Constant(value=True); ast.fix_missing_locations(t); '
                        'g={"__name__":"negative_control"}; '
                        'exec(compile(t,"negative_control","exec"),g); g["run_checks"]()')
                negative, info = execute(prefix + ['-c', negative_code], timeout=20)
                require(negative.returncode != 0 and 'AssertionError' in negative.stderr,
                        'Mathematical failure control disappeared: ' + family)
                controls.append({'family': family, 'mode': mode,
                                 'check': 'actual explicit mathematical failure remains active', **info})
                result_path = output / (family + '_' + mode + '.json')
                run, info = execute(prefix + [str(port), '--output', str(result_path)])
                require(run.returncode == 0, family + ' replay failed: ' + run.stderr)
                require(not run.stdout and not run.stderr, 'Replay main is not silent: ' + family)
                actual = json.loads(result_path.read_text())
                require(actual == expected, family + ' differs from frozen scientific output')
                if family == 'independent':
                    for name in ['full_end', 'top_gram', 'torus', 'network', 'offcharge_bound']:
                        for version in ['results/verified', 'results']:
                            reference = json.loads((RAW / 'review' / version / (name + '.json')).read_text())
                            require(actual[name] == reference, 'Subresult differs from ' + version + '/' + name)
                if family == 'synthesis':
                    require(len(actual['mask_cases']) == 108, 'Missing synthesis radius pair')
                    require(len(actual['pair_families']) == 8, 'Missing synthesis coordinate family')
                if normal_bytes is None:
                    normal_bytes = result_path.read_bytes()
                else:
                    require(normal_bytes == result_path.read_bytes(), family + ' normal/-O bytes differ')
                records.append({'family': family, 'mode': mode,
                                'scientific_output_matches_frozen': True,
                                'scientific_sha256': sha(result_path), **info})
                output_files.append(result_path)
    except Exception as error:
        failure = repr(error)
    after = {str(p.relative_to(ROOT)): sha(p) for p in files}
    stable = before == after
    if not stable:
        failure = (failure or '') + ' Input bytes changed during replay.'
    report = {'status': 'passed' if failure is None else 'failed',
              'failure': failure, 'runs': records, 'portability_controls': controls,
              'input_bytes_unchanged': stable,
              'normal_optimized_scientific_bytes_identical': failure is None,
              'omitted_fields': {'author': ['elapsed_seconds'],
                                 'independent': ['runtime_seconds'], 'synthesis': []},
              'bounds': {'author_position_tuples_N2_m5_r2': 256,
                         'author_N3_m5_r2_selected_tuples': 6,
                         'full_End_N_m': [[2, 1], [2, 2], [2, 3], [3, 2]],
                         'top_Gram_N_m_r': [2, 4, 2],
                         'torus_N_m': [[2, 3], [3, 2]],
                         'network_stages': [1, 2, 3],
                         'offcharge_N2_m': [1, 2, 3, 4, 5, 6],
                         'synthesis_N': [2, 3], 'synthesis_m': [1, 2, 3, 4],
                         'synthesis_radius_pairs': 108},
              'non_claims': ['Bounded replay is not a universal proof.',
                             'Inherited actual-map analysis and Haar tail are not re-audited.',
                             'No bound on the final residual, plateau, factorial hierarchy or BGS.']}
    report_path = output / 'comparison.json'
    report_path.write_text(json.dumps(report, indent=2) + '\n')
    output_files.append(report_path)
    import sympy
    manifest = {
        'schema_version': 2, 'claim_id': 'BGS-FRACTIONAL-HAMMING-PORTABLE-REPLAY',
        'repository': {'commit': 'none: partial staging overlay; source hashes are authoritative', 'dirty': True},
        'command': [sys.executable, '-B', str(Path(__file__).resolve()), '--output-dir', str(output)],
        'environment': {'software': [{'name': 'Python', 'version': sys.version},
                                     {'name': 'SymPy', 'version': sympy.__version__}],
                        'hardware': platform.platform()},
        'mathematics': {'assertion_tested': 'All author, independent-review and synthesis scientific outputs match frozen originals in normal and optimized Python; explicit negative controls remain active.',
                        'coefficient_domain': 'Exact QQ, QQ(i), integer Laurent coefficients and integers; no tolerance or sampling',
                        'conventions': 'Frozen arithmetic, basis, cyclic orientations, support and whole-fiber masks retained; unnormalized HS.',
                        'inputs': sorted(before), 'bounds': report['bounds'],
                        'non_claims': report['non_claims']},
        'randomness': {'used': False, 'generator': 'none', 'seed': None},
        'run': {'started_at': started, 'runtime_seconds': time.monotonic() - overall_start,
                'exit_status': 0 if failure is None else 1,
                'status': 'completed' if failure is None else 'failed',
                'resource_limits': {'memory_bytes': 3 * 1024 ** 3, 'cpu_seconds': 320,
                                    'max_cores': 1, 'max_threads': 1},
                'wall_timeout_seconds': 360, 'limits_apply_to': 'each subprocess',
                'cpu_affinity': cpu},
        'input_artifacts': [{'path': p, 'sha256': h, 'sha256_after': after[p]} for p, h in before.items()],
        'execution_artifacts': sorted(before),
        'declared_results': [str(p.relative_to(ROOT)) for p in output_files],
        'outputs': [{'path': str(p.relative_to(ROOT)), 'sha256': sha(p), 'kind': 'result'} for p in output_files],
        'checks': [{'check': 'normal/-O frozen-output agreement and active failure controls', 'passed': failure is None}],
        'result': 'implementation and finite assertion verified in the stated range' if failure is None else 'failed; inspect comparison.json',
        'residual_risks': ['No analytic recertification; exact symbolic computation is not proof-assistant verification.']}
    (output / 'execution_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    if failure is not None:
        raise RuntimeError(failure)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
