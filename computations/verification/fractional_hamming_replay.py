#!/usr/bin/env python3
"""Bounded exact Hamming replay; version provenance is separate from science.

The default runs author and synthesis. Eight unchanged split workspace entries
run independent cases. --output-dir retains fresh raw inputs/results, logs and
strict scientific comparisons on both success and failure. Without that option,
external temporary outputs are cleaned. No reviewed expected bytes are changed.
"""
from pathlib import Path
import argparse
import contextlib
import hashlib
import json
import os
import resource
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[2]
PORTS = ROOT / 'computations/verification/fractional_hamming'
RAW = ROOT / 'evidence/fractional_hamming_20261007/raw'


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def comparison_api():
    # Execute the actual maintained bytes, not a possibly stale cached pyc.
    path = PORTS / 'comparison.py'
    namespace = {'__name__': 'bgs_fractional_hamming_comparison', '__file__': str(path)}
    exec(compile(path.read_bytes(), str(path), 'exec'), namespace)
    return namespace


def main(case=None, output_dir=None):
    api = comparison_api()
    require(case is None or case in api['CASES'], 'Unknown independent Hamming case')
    mapping = json.loads((ROOT / 'record/fractional_hamming_adapter_mapping.json').read_text())
    paths = [Path(__file__).resolve(), PORTS / 'comparison.py',
             ROOT / 'record/fractional_hamming_adapter_mapping.json']
    for row in mapping['ports']:
        original = ROOT / row['frozen_source']
        port = ROOT / row['port']
        require(sha(original) == row['source_sha256'], 'Frozen adapter source mismatch')
        require(sha(port) == row['port_sha256'], 'Maintained adapter source mismatch')
        paths.extend([original, port])
    expected_paths = {
        'author': RAW / 'author/results.json',
        'independent': RAW / 'review/results/verified/all_results.json',
        'synthesis': RAW / 'review/synthesis_results.json',
    }
    paths.extend(expected_paths.values())
    paths.append(PORTS / 'case_runner.py')
    for version in ['results', 'results/verified']:
        for name in ['full_end', 'top_gram', 'torus', 'network', 'offcharge_bound']:
            paths.append(RAW / 'review' / version / (name + '.json'))
    before = {p: sha(p) for p in paths}
    # Cache immutable expected bytes before any producer is started.
    cached_expected = {family: path.read_bytes() for family, path in expected_paths.items()}
    cached_subresults = {p: p.read_bytes() for p in paths if p.parent.name in ('results', 'verified')}
    env = os.environ.copy()
    env.update(PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1',
               OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')

    def limits():
        resource.setrlimit(resource.RLIMIT_AS, (3 * 1024 ** 3, 3 * 1024 ** 3))
        resource.setrlimit(resource.RLIMIT_CPU, (320, 320))

    prefix = [sys.executable, '-B'] + (['-O'] if sys.flags.optimize else [])
    deadline = time.monotonic() + 350
    if output_dir is None:
        context = tempfile.TemporaryDirectory(prefix='bgs_fractional_hamming_', dir='/tmp')
    else:
        destination = Path(output_dir).resolve()
        require(ROOT not in destination.parents and destination != ROOT,
                'Durable output must be external to maintained repository')
        require(not destination.exists(), 'Durable output directory must be fresh and absent')
        destination.mkdir(parents=True)
        context = contextlib.nullcontext(str(destination))
    with context as directory:
        work = Path(directory)
        require(ROOT not in work.parents and work != ROOT, 'Temporary output must be external')
        records = []
        failure = None
        try:
            for family in (['author', 'synthesis'] if case is None else ['independent']):
                output = work / (family + '.json')
                require(not output.exists() and not output.is_symlink(), 'Producer output was not fresh')
                (work / (family + '.expected.raw')).write_bytes(cached_expected[family])
                remaining = deadline - time.monotonic()
                require(remaining > 0, 'Overall 350-second replay budget exhausted')
                command = prefix + [str(PORTS / (family + '_checks.py')), '--output', str(output)]
                if case is not None:
                    command = prefix + [str(PORTS / 'case_runner.py'), '--case', case, '--output', str(output)]
                try:
                    run = subprocess.run(command, cwd=work, env=env, preexec_fn=limits,
                        timeout=min(340, remaining), capture_output=True, text=True)
                except subprocess.TimeoutExpired as error:
                    for name, value in [('stdout', error.stdout), ('stderr', error.stderr)]:
                        data = value if isinstance(value, bytes) else (value or '').encode()
                        (work / (family + '.' + name)).write_bytes(data)
                    if output.is_file() and not output.is_symlink() and output.resolve() == output:
                        (work / (family + '.actual.raw')).write_bytes(output.read_bytes())
                    records.append({'family': family, 'case': case, 'command': command,
                                    'exit_code': None, 'timed_out': True, 'comparison': None})
                    raise
                (work / (family + '.stdout')).write_text(run.stdout)
                (work / (family + '.stderr')).write_text(run.stderr)
                row = {'family': family, 'case': case, 'command': command,
                       'exit_code': run.returncode, 'comparison': None}
                records.append(row)
                if output.is_file() and not output.is_symlink() and output.resolve() == output:
                    raw_actual = output.read_bytes()
                    (work / (family + '.actual.raw')).write_bytes(raw_actual)
                else:
                    raw_actual = None
                require(run.returncode == 0 and not run.stdout and not run.stderr,
                        family + ' exact replay failed or was not silent: ' + run.stderr)
                require(raw_actual is not None, family + ' result missing or nonregular')
                require(before == {p: sha(p) for p in paths}, 'Input bytes changed during replay')
                try:
                    expected, actual, comparison = api['compare'](cached_expected[family], raw_actual, family, case)
                except ValueError as error:
                    row['comparison_error'] = str(error)
                    require(False, family + ' differs from frozen scientific output: ' + str(error))
                row['comparison'] = comparison
                (work / (family + '.expected.scientific.json')).write_bytes(api['scientific_bytes'](expected))
                (work / (family + '.actual.scientific.json')).write_bytes(api['scientific_bytes'](actual))
                (work / (family + '.comparison.json')).write_text(json.dumps(comparison, indent=2) + '\n')
                require(comparison['scientific_comparison']['equal'],
                        family + ' differs from frozen scientific output: '
                        + json.dumps(comparison['scientific_comparison']['mismatches']))
                if family == 'independent':
                    all_expected, _ = api['separate'](api['parse_json'](cached_expected['independent']), 'independent')
                    for version in ['results', 'results/verified']:
                        for name in ['full_end', 'top_gram', 'torus', 'network', 'offcharge_bound']:
                            frozen = RAW / 'review' / version / (name + '.json')
                            require(api['differences'](all_expected[name], api['parse_json'](cached_subresults[frozen]))['equal'],
                                    'Initial or authoritative independent subresult differs')
                if family == 'synthesis':
                    require(len(actual['mask_cases']) == 108 and len(actual['pair_families']) == 8,
                            'Synthesis coverage changed')
        except BaseException as error:
            failure = repr(error)
            raise
        finally:
            stable = before == {p: sha(p) for p in paths}
            artifacts = {p.name: sha(p) for p in work.iterdir() if p.is_file() and not p.is_symlink()}
            receipt = {'status': 'passed' if failure is None and stable else 'failed',
                       'failure': failure, 'case': case, 'runs': records,
                       'source_sha256': {str(p.relative_to(ROOT)): h for p, h in before.items()},
                       'source_unchanged': stable, 'artifacts_sha256': artifacts,
                       'durable_output_requested': output_dir is not None,
                       'scope': 'Bounded exact finite checks. Only named top-level version/timing provenance is separated; no nested scientific field or asymptotic claim is omitted.'}
            (work / 'execution_receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
            require(stable, 'Input bytes changed during replay')
    return 0


def cli(case=None, argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path)
    args = parser.parse_args(argv)
    return main(case, output_dir=args.output_dir)


if __name__ == '__main__':
    raise SystemExit(cli())
