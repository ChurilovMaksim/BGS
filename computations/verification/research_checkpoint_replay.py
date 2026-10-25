#!/usr/bin/env python3
"""Source-bound finite packet replay; normal/-O retain explicit assertion tests.

No analytic theorem or BGS conclusion follows from this bounded replay.
Raw reviewed bytes and expected output bytes are cached before any execution.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
from functools import partial
import json
import math
import os
import resource
import re
from pathlib import Path, PurePosixPath
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
CONTRACT = 'record/research_checkpoint_replay_contract.json'
BINDINGS = 'record/research_checkpoint_source_bindings.json'
# Fail-closed historical-target allowlist (Wave 2 proposal, parent review
# required before landing). Each declared override maps a logical pin to
# exactly one audited target path whose bytes are hash-identical to the
# pin. Any key or target outside this map still fails closed below; the
# bindings entry for an override must additionally carry sha256 == pin.
HISTORICAL_TARGETS = {
    'mathematics/phase_trace_checkpoint.md': 'evidence/wave2_checked_20261007/raw/provenance/base_navigation/mathematics/phase_trace_checkpoint.md',
    'mathematics/phase_ward_identity.md': 'evidence/research_checkpoint_20261007/raw/bgs_balanced_delay_ward_review/phase_ward_identity_v2.md',
    'mathematics/actual_body_coercivity_constants.md': 'evidence/research_checkpoint_20261007/raw/bgs_global_phase_coercivity/actual_constants_addendum.md',
    'mathematics/actual_charge_radial_resolvent.md': 'mathematics/fixed-map/actual_charge_radial_resolvent.md',
    'mathematics/actual_charge_radial_shell.md': 'archive/evidence/research_checkpoint_20261007/pinned/mathematics_actual_charge_radial_shell.md',
    'mathematics/literal_fixed_word_freeness.md': 'mathematics/fixed-map/literal_fixed_word_freeness.md',
    'mathematics/literal_growing_word_window.md': 'mathematics/fixed-map/literal_growing_word_window.md',
    'mathematics/literal_kick_phase_law.md': 'mathematics/fixed-map/literal_kick_phase_law.md',
    'mathematics/literal_strong_freeness_obstruction.md': 'mathematics/fixed-map/literal_strong_freeness_obstruction.md',
    'literature/color_one_boundary_qualification_20261007.md': 'archive/evidence/research_checkpoint_20261007/pinned/literature_color_one_boundary_qualification_20261007.md',
}


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def strict_json(raw):
    def unique(pairs):
        out = {}
        for key, value in pairs:
            require(key not in out, 'duplicate JSON key: ' + key)
            out[key] = value
        return out
    def bad(value):
        raise RuntimeError('nonfinite JSON constant: ' + value)
    return json.loads(raw, object_pairs_hook=unique, parse_constant=bad)


def final_json(raw):
    text = raw.decode('utf-8') if isinstance(raw, bytes) else raw
    decoder = json.JSONDecoder(object_pairs_hook=lambda pairs: strict_json(json.dumps(dict(pairs))))
    # Historical CFT logs include bounded progress lines before the final object.
    candidates = []
    for i, char in enumerate(text):
        if char != '{':
            continue
        try:
            _, end = decoder.raw_decode(text, i)
        except (ValueError, RuntimeError):
            continue
        if not text[end:].strip():
            candidates.append(i)
    require(bool(candidates), 'missing final complete JSON object')
    return strict_json(text[min(candidates):])


def source_bytes(root):
    manifest = strict_json((root / BINDINGS).read_bytes())
    require(manifest.get('schema') == 'bgs-checkpoint-source-bindings-v1', 'unknown source bindings')
    cached = {}
    for rel, digest in manifest['files'].items():
        p = PurePosixPath(rel)
        require(not p.is_absolute() and '..' not in p.parts and str(p) == rel and '\\' not in rel, 'unsafe source path')
        # The original reviewed checkpoint is retained for this historical replay;
        # current navigation additions do not silently refresh a scientific pin.
        historical = manifest.get('historical_inputs', {})
        require(set(historical).issubset(set(HISTORICAL_TARGETS)), 'undeclared historical override')
        source_rel = historical.get(rel, {}).get('source', rel)
        if rel in historical:
            require(historical[rel]['sha256'] == digest, 'historical pin was refreshed')
            require(source_rel == HISTORICAL_TARGETS[rel], 'unexpected historical target')
        source_path = PurePosixPath(source_rel)
        require(not source_path.is_absolute() and '..' not in source_path.parts and str(source_path) == source_rel and '\\' not in source_rel, 'unsafe historical source path')
        f = root / source_rel
        require(f.is_file() and not f.is_symlink() and f.resolve().is_relative_to(root.resolve()), 'missing/nonregular/escaping source: ' + source_rel)
        data = f.read_bytes()
        require(hashlib.sha256(data).hexdigest() == digest, 'changed source: ' + rel)
        cached[rel] = data
    return cached


def compare(expected, observed, fields, elapsed_budget_seconds=180):
    require(type(elapsed_budget_seconds) is int and 1 <= elapsed_budget_seconds <= 660,
            'invalid declared elapsed budget')
    require(isinstance(expected, dict) and isinstance(observed, dict), 'expected root objects')
    expected = dict(expected)
    observed = dict(observed)
    for key in fields:
        require(key in {'seconds', 'runtime_seconds', 'elapsed_seconds', 'python', 'sympy', 'compiler_command'}, 'unknown provenance exemption')
        require(key in expected and key in observed, 'missing declared provenance field: ' + key)
        for value in (expected[key], observed[key]):
            if key.endswith('seconds'):
                require(type(value) in (int, float) and math.isfinite(value) and 0 <= value <= elapsed_budget_seconds, 'invalid runtime')
            elif key in {'python', 'sympy'}:
                require(type(value) is str and 0 < len(value) <= 256 and re.fullmatch(r'[0-9]+(?:\.[0-9]+)+(?:[a-zA-Z0-9.+-]*)', value) is not None, 'invalid environment version')
            elif key == 'compiler_command':
                require(type(value) is list and len(value) == 9 and all(type(v) is str and v for v in value) and value[:6] == ['g++', '-std=c++17', '-O2', '-Wall', '-Wextra', '-pedantic'] and value[-2] == '-o', 'invalid compiler provenance')
        del expected[key]
        del observed[key]
    differences = []
    total = 0
    def walk(a, b, path):
        nonlocal total
        if type(a) is not type(b):
            total += 1
            if len(differences) < 16:
                differences.append(path + ': type')
        elif isinstance(a, dict):
            for k in sorted(set(a) | set(b)):
                if k not in a or k not in b:
                    total += 1
                    if len(differences) < 16:
                        differences.append(path + '/' + k + ': missing/extra')
                else:
                    walk(a[k], b[k], path + '/' + k)
        elif isinstance(a, list):
            if len(a) != len(b):
                total += 1
                if len(differences) < 16:
                    differences.append(path + ': length')
            for i, (x, y) in enumerate(zip(a, b)):
                walk(x, y, path + '/' + str(i))
        elif a != b:
            total += 1
            if len(differences) < 16:
                differences.append(path + ': value')
    walk(expected, observed, '')
    require(total == 0, 'scientific mismatch: ' + repr(differences) + '; total=' + str(total))


BOOTSTRAP = r'''
import ast, sys
from pathlib import Path
class ExplicitAssertions(ast.NodeTransformer):
    def visit_Assert(self, node):
        messages = [node.msg] if node.msg is not None else []
        replacement = ast.If(test=ast.UnaryOp(op=ast.Not(), operand=node.test),
            body=[ast.Raise(exc=ast.Call(func=ast.Name(id='AssertionError', ctx=ast.Load()), args=messages, keywords=[]), cause=None)], orelse=[])
        return ast.copy_location(replacement, node)
path = Path(sys.argv[1]); sys.argv = sys.argv[1:]
source = path.read_bytes(); tree = ast.parse(source, filename=str(path))
tree = ast.fix_missing_locations(ExplicitAssertions().visit(tree))
exec(compile(tree, str(path), 'exec'), {'__name__':'__main__', '__file__':str(path)})
'''


def task_budget(task):
    """One named unchanged finite control has a larger, still bounded budget."""
    extended = task.get('name') == 'compact_independent_n4'
    if extended:
        require(task.get('source') == 'evidence/research_checkpoint_20261007/raw/bgs_astra_corrected_integral/checks/independent_checks.py'
                and task.get('arguments') == ['4', '3'], 'expanded budget requires exact N4 control')
    wall = task['timeout_seconds']
    cpu = task.get('cpu_seconds', 180)
    require(type(wall) is int and 1 <= wall <= (660 if extended else 180), 'invalid task wall budget')
    require(type(cpu) is int and 1 <= cpu <= (600 if extended else 180), 'invalid task CPU budget')
    return {'wall_seconds': wall, 'cpu_seconds': cpu, 'memory_bytes': 3 * 2**30}


def partial_generated_bytes(work, generated):
    if generated is None or not generated.is_file() or generated.is_symlink():
        return None
    if not generated.resolve().is_relative_to(work.resolve()):
        return None
    if any(p.is_symlink() for p in generated.parents if p.is_relative_to(work)):
        return None
    if generated.stat().st_size >= 2**20:
        return None
    return generated.read_bytes()


def execute_task(work, task, env, mode, captured=None):
    budget = task_budget(task)
    generated = None
    if task.get('generated_result'):
        generated = work / task['generated_result']
        require(generated.resolve().is_relative_to(work.resolve()), 'escaping generated result')
        generated.unlink(missing_ok=True)
    command = [sys.executable, *mode, '-c', BOOTSTRAP,
               str(work / task['source']), *task['arguments']]
    description = [sys.executable, *mode, '-c', 'authenticated explicit-assertion bootstrap',
                   str(work / task['source']), *task['arguments']]
    try:
        result = subprocess.run(command,
                                cwd=work / 'evidence/research_checkpoint_20261007/raw',
                                env=env, capture_output=True, timeout=budget['wall_seconds'],
                                preexec_fn=partial(child_limits, budget['cpu_seconds']))
    except subprocess.TimeoutExpired as error:
        if captured is not None:
            def raw(value):
                return value if isinstance(value, bytes) else (value or '').encode()
            captured.update(stdout=raw(error.stdout), stderr=raw(error.stderr), returncode=None,
                            command=description, timed_out=True, resource_budget=budget)
            observed = partial_generated_bytes(work, generated)
            if observed is not None:
                captured['partial_actual'] = observed
            elif captured['stdout']:
                captured['partial_actual'] = captured['stdout']
        raise
    if captured is not None:
        captured.update(stdout=result.stdout, stderr=result.stderr, returncode=result.returncode,
                        resource_budget=budget, timed_out=False,
                        command=[sys.executable, *mode, '-c', 'authenticated explicit-assertion bootstrap', str(work / task['source']), *task['arguments']])
    require(result.returncode == 0, task['name'] + ' failed: ' + result.stderr.decode(errors='replace')[-2000:])
    require(len(result.stdout) < 2**20, 'result output cap exceeded')
    if generated is not None:
        require(generated.is_file() and not generated.is_symlink(), 'missing generated packet result')
        require(generated.resolve().is_relative_to(work.resolve()) and not any(p.is_symlink() for p in generated.parents if p != work.parent and p.is_relative_to(work)), 'escaping/symlink generated result')
        require(generated.stat().st_size < 2**20, 'generated result output cap exceeded')
        return generated.read_bytes()
    return result.stdout


def authenticate_copied_inputs(work, cached, generated_outputs=()):
    for rel, data in cached.items():
        if rel in generated_outputs:
            continue
        f = work / rel
        require(f.is_file() and not f.is_symlink() and f.resolve().is_relative_to(work.resolve())
                and f.read_bytes() == data, 'copied input changed: ' + rel)


def child_limits(cpu_seconds=180):
    require(type(cpu_seconds) is int and 1 <= cpu_seconds <= 600, 'invalid child CPU budget')
    resource.setrlimit(resource.RLIMIT_AS, (3 * 2**30, 3 * 2**30))
    resource.setrlimit(resource.RLIMIT_CPU, (cpu_seconds, cpu_seconds))


def output_directory(root, output):
    if output is None:
        return None
    output = Path(output).absolute()
    require(not any(p.is_symlink() for p in (output, *output.parents)), 'symlink output ancestor')
    output = output.resolve()
    inside = output.is_relative_to(root.resolve())
    excluded_build = inside and output.relative_to(root.resolve()).parts[0] == 'build'
    require((not inside or excluded_build) and not root.resolve().is_relative_to(output),
            'durable output must be separate from maintained sources or under excluded build/')
    output.mkdir(parents=True, exist_ok=True)
    require(output.is_dir() and not any(output.iterdir()), 'durable output directory must be empty')
    return output


def save_artifact(output, name, data):
    if output is None:
        return None
    path = output / name
    path.write_bytes(data)
    return {'path':name, 'bytes':len(data), 'sha256':hashlib.sha256(data).hexdigest()}


def run(root=ROOT, output=None):
    output = output_directory(root, output)
    receipt = {'schema':'bgs-checkpoint-durable-replay-v1', 'status':'running', 'tasks':[], 'artifacts':[],
               'python':sys.version, 'optimization':sys.flags.optimize,
               'scope':'Bounded finite controls only; complete mathematical identification remains open.'}
    def retain(name, data):
        record = save_artifact(output, name, data)
        if record is not None:
            receipt['artifacts'].append(record)
    def publish():
        if output is not None:
            (output / 'replay_manifest.json').write_text(json.dumps(receipt, indent=2) + '\n')
    publish()
    try:
        cached = source_bytes(root)
        retain('source_bindings.original.json', (root / BINDINGS).read_bytes())
        retain('replay_contract.original.json', cached[CONTRACT])
        receipt['source_hashes'] = {rel:hashlib.sha256(data).hexdigest() for rel, data in cached.items()}
        contract = strict_json(cached[CONTRACT])
        expected = {t['name']: final_json(cached[t['expected']]) for t in contract['tasks']}
        cpp = contract['cpp']
        cpp_expected = final_json(cached[cpp['expected']])
        env = dict(os.environ)
        env.update(OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1',
                   NUMEXPR_NUM_THREADS='1', PYTHONDONTWRITEBYTECODE='1')
        mode = ['-O'] if sys.flags.optimize else []
        with tempfile.TemporaryDirectory(prefix='bgs-reviewed-checkpoint-') as tmp:
            work = Path(tmp)
            for rel, data in cached.items():
                f = work / rel
                f.parent.mkdir(parents=True, exist_ok=True)
                f.write_bytes(data)
            generated_outputs = {t['generated_result'] for t in contract['tasks'] if t.get('generated_result')}
            for task in contract['tasks']:
                authenticate_copied_inputs(work, cached, generated_outputs)
                capture = {}
                retain(task['name'] + '.expected.raw', cached[task['expected']])
                try:
                    observed_bytes = execute_task(work, task, env, mode, capture)
                except Exception as error:
                    for key in ('stdout', 'stderr'):
                        if key in capture:
                            retain(task['name'] + '.' + key, capture[key])
                    if 'partial_actual' in capture:
                        retain(task['name'] + '.partial.actual.raw', capture['partial_actual'])
                    receipt.update(status='failed', failure=task['name'] + ': ' + str(error),
                                   failed_task={'name': task['name'], 'timed_out': capture.get('timed_out', False),
                                                'exit_status': capture.get('returncode'),
                                                'resource_budget': capture.get('resource_budget', task_budget(task)),
                                                'partial_actual_is_not_scientific_acceptance': True})
                    publish()
                    raise
                retain(task['name'] + '.stdout', capture['stdout'])
                retain(task['name'] + '.stderr', capture['stderr'])
                retain(task['name'] + '.actual.raw', observed_bytes)
                authenticate_copied_inputs(work, cached, generated_outputs)
                observed = final_json(observed_bytes)
                compare(expected[task['name']], observed, task['provenance_root_fields'],
                        elapsed_budget_seconds=task_budget(task)['wall_seconds'])
                receipt['tasks'].append({'name':task['name'], 'status':'passed', 'command':capture['command'],
                    'exit_status':capture['returncode'], 'resource_budget':capture['resource_budget'],
                    'source_sha256':hashlib.sha256(cached[task['source']]).hexdigest(),
                    'expected_raw_sha256':hashlib.sha256(cached[task['expected']]).hexdigest(),
                    'actual_raw_sha256':hashlib.sha256(observed_bytes).hexdigest(),
                    'declared_provenance_fields':task['provenance_root_fields'],
                    'expected_provenance':{k:expected[task['name']][k] for k in task['provenance_root_fields']},
                    'observed_provenance':{k:observed[k] for k in task['provenance_root_fields']}})
                publish()
            authenticate_copied_inputs(work, cached, generated_outputs)
            exe = work / 'check_growing'
            compiled = subprocess.run(['g++', '-std=c++17', '-O2', '-Wall', '-Wextra', '-pedantic',
                                       str(work / cpp['source']), '-o', str(exe)], env=env,
                                      capture_output=True, timeout=60)
            retain('growing_period.compile.stdout', compiled.stdout)
            retain('growing_period.compile.stderr', compiled.stderr)
            require(compiled.returncode == 0, 'growing-period exact control compilation failed')
            retain('growing_period.expected.raw', cached[cpp['expected']])
            cpp_run = subprocess.run([str(exe)], env=env, capture_output=True, timeout=cpp['timeout_seconds'])
            retain('growing_period.stdout', cpp_run.stdout)
            retain('growing_period.stderr', cpp_run.stderr)
            require(cpp_run.returncode == 0, 'growing-period exact controls failed')
            observed = final_json(cpp_run.stdout)
            negative = subprocess.run([str(exe), '--inject-bad-carry'], env=env,
                                      capture_output=True, timeout=20)
            retain('growing_period.negative.stdout', negative.stdout)
            retain('growing_period.negative.stderr', negative.stderr)
            require(negative.returncode == 2 and b'literal cyclic carry identity' in negative.stderr,
                    'injected carry defect did not fail')
            observed['negative_control'] = {'fault':'omit low-digit carry into high digit',
                                           'returncode':negative.returncode,
                                           'diagnostic':negative.stderr.decode().strip()}
            observed['compiler_command'] = ['g++', '-std=c++17', '-O2', '-Wall', '-Wextra', '-pedantic',
                                            str(work / cpp['source']), '-o', str(exe)]
            authenticate_copied_inputs(work, cached, generated_outputs)
            actual = (json.dumps(observed, indent=2) + '\n').encode()
            retain('growing_period.actual.raw', actual)
            compare(cpp_expected, observed, cpp['provenance_root_fields'])
            receipt['tasks'].append({'name':'growing_period', 'status':'passed',
                'source_sha256':hashlib.sha256(cached[cpp['source']]).hexdigest(),
                'fresh_executable_sha256':hashlib.sha256(exe.read_bytes()).hexdigest(),
                'expected_raw_sha256':hashlib.sha256(cached[cpp['expected']]).hexdigest(),
                'actual_raw_sha256':hashlib.sha256(actual).hexdigest(),
                'expected_provenance':{k:cpp_expected[k] for k in cpp['provenance_root_fields']},
                'observed_provenance':{k:observed[k] for k in cpp['provenance_root_fields']},
                'negative_exit_status':negative.returncode})
        require(source_bytes(root) == cached, 'sources changed during execution')
        receipt.update(status='passed', original_sources_unchanged=True, copied_inputs_authenticated_after_each_child=True,
                       expected_bytes_cached_before_execution=True, scientific_equality=True)
        publish()
        return receipt
    except Exception as error:
        receipt.update(status='failed', failure=str(error))
        publish()
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-sources', action='store_true')
    parser.add_argument('--output-dir', type=Path, help='Fresh empty external or excluded build/ directory for durable raw expected/actual/log/provenance artifacts.')
    args = parser.parse_args()
    if args.check_sources:
        source_bytes(ROOT)
    else:
        run(output=args.output_dir)


if __name__ == '__main__':
    main()
