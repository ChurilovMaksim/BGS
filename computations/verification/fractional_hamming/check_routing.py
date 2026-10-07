#!/usr/bin/env python3
"""Cheap wrapper-routing controls; mathematical outputs were replayed separately."""
from pathlib import Path
import argparse
import contextlib
import hashlib
import importlib.util
import io
import json
import runpy
import sys
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[3]


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_routing():
    top = ROOT / 'computations/verification/fractional_hamming_replay.py'
    files = sorted(p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts)
    before = {str(p): sha(p) for p in files}
    stream = io.StringIO()
    with contextlib.redirect_stdout(stream), contextlib.redirect_stderr(stream):
        spec = importlib.util.spec_from_file_location('current_mode_wrapper', top)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    require(not stream.getvalue(), 'Wrapper import is not silent')
    calls = []
    workdirs = []
    corrupt = False
    original_run = module.subprocess.run

    def fake_run(command, **kwargs):
        nonlocal calls, workdirs
        require(command.count('-O') == int(bool(sys.flags.optimize)), 'Wrong mode routing')
        require(command.count('-B') == 1, 'Bytecode suppression missing')
        work = Path(kwargs['cwd'])
        require(work.parent == Path('/tmp') and ROOT not in work.parents,
                'Output is not in external temporary storage')
        require(0 < kwargs['timeout'] <= 340, 'Timeout budget missing')
        require(kwargs['env']['PYTHONDONTWRITEBYTECODE'] == '1', 'Cache suppression missing')
        require(kwargs['capture_output'] and kwargs['text'], 'Silent subprocess capture missing')
        case = command[command.index('--case') + 1] if '--case' in command else None
        family = 'independent' if case is not None else Path(command[command.index('--output') - 1]).stem.replace('_checks', '')
        path = {'author': module.RAW / 'author/results.json',
                'independent': module.RAW / 'review/results/verified/all_results.json',
                'synthesis': module.RAW / 'review/synthesis_results.json'}[family]
        value = json.loads(path.read_text())
        for key in {'author': ['elapsed_seconds'], 'independent': ['runtime_seconds'],
                    'synthesis': []}[family]:
            value.pop(key, None)
        if family == 'author':
            value['python'] = 'Different Python runtime fixture'
            value['sympy'] = 'Different SymPy runtime fixture'
        if case is not None:
            value = value['full_end' if case.startswith('full_end_') else case]
            if case.startswith('full_end_'):
                n, m = map(int, case.removeprefix('full_end_').split('_'))
                value = [row for row in value if (row['N'], row['m']) == (n, m)]
        if corrupt:
            if isinstance(value, dict):
                value['unexpected_scientific_field'] = True
            else:
                value.append({'unexpected_scientific_field': True})
        output = Path(command[command.index('--output') + 1])
        require(output.parent == work, 'Output escaped external temporary directory')
        output.write_text(json.dumps(value) + '\n')
        calls.append({'family': family, 'case': case, 'command': command,
                      'external_output': True, 'timeout_seconds': kwargs['timeout']})
        workdirs.append(work)
        return SimpleNamespace(returncode=0, stdout='', stderr='')

    def invoke_split(script):
        previous = sys.argv
        try:
            sys.argv = [str(script)]
            return runpy.run_path(str(script), run_name='__main__')
        finally:
            sys.argv = previous

    try:
        module.subprocess.run = fake_run
        with contextlib.redirect_stdout(stream), contextlib.redirect_stderr(stream):
            require(module.main() == 0, 'Wrapper returned failure')
        require(not stream.getvalue(), 'No-argument wrapper is not silent')
        cases = ['full_end_2_1', 'full_end_2_2', 'full_end_2_3', 'full_end_3_2',
                 'top_gram', 'torus', 'network', 'offcharge_bound']
        require([c['family'] for c in calls] == ['author', 'synthesis'],
                'Default wrapper did not select exactly author and synthesis')
        for case in cases:
            script = ROOT / 'computations/verification' / ('fractional_hamming_' + case + '.py')
            with contextlib.redirect_stdout(stream), contextlib.redirect_stderr(stream):
                invoke_split(script)
        require(not stream.getvalue(), 'Split wrapper produced output')
        require([c['case'] for c in calls[2:]] == cases,
                'Eight split entries do not cover exactly the original independent cases')
        require(all(not p.exists() for p in workdirs), 'Temporary output survived successful return')
        successful = list(calls)
        corrupt = True
        for case in [None] + cases:
            caught = False
            try:
                if case is None:
                    module.main()
                else:
                    script = ROOT / 'computations/verification' / ('fractional_hamming_' + case + '.py')
                    invoke_split(script)
            except AssertionError as error:
                caught = 'differs from frozen scientific output' in str(error)
            require(caught, 'Scientific corruption was accepted for ' + str(case))
        require(all(not p.exists() for p in workdirs), 'Temporary output survived failed return')
    finally:
        module.subprocess.run = original_run
    require(before == {str(p): sha(p) for p in files}, 'Routing test changed repository bytes')
    require(set(before) == {str(p) for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts},
            'Routing test created a repository file')
    return {'status': 'passed', 'optimization_mode': sys.flags.optimize,
            'wrapper_sha256': sha(top), 'calls': successful,
            'silent_import_and_no_argument_main': True,
            'temporary_outputs_removed_on_success_and_failure': True,
            'scientific_corruption_rejected': True, 'all_nine_current_entries_covered': True, 'repository_unchanged': True,
            'scope': 'Routing and read-only behavior tested with subprocess fixture outputs; no repeat of expensive mathematics. Actual adapter results are separately pinned in the six-run manifest.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = test_routing()
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
