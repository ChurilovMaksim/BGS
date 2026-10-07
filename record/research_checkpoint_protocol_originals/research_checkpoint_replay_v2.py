#!/usr/bin/env python3
"""Source-bound finite packet replay; normal/-O retain explicit assertion tests.

No analytic theorem or BGS conclusion follows from this bounded replay.
Raw reviewed bytes and expected output bytes are cached before any execution.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
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
        f = root / rel
        require(f.is_file() and not f.is_symlink() and f.resolve().is_relative_to(root.resolve()), 'missing/nonregular/escaping source: ' + rel)
        data = f.read_bytes()
        require(hashlib.sha256(data).hexdigest() == digest, 'changed source: ' + rel)
        cached[rel] = data
    return cached


def compare(expected, observed, fields):
    require(isinstance(expected, dict) and isinstance(observed, dict), 'expected root objects')
    expected = dict(expected)
    observed = dict(observed)
    for key in fields:
        require(key in {'seconds', 'runtime_seconds', 'elapsed_seconds', 'python', 'sympy', 'compiler_command'}, 'unknown provenance exemption')
        require(key in expected and key in observed, 'missing declared provenance field: ' + key)
        for value in (expected[key], observed[key]):
            if key.endswith('seconds'):
                require(type(value) in (int, float) and math.isfinite(value) and 0 <= value <= 180, 'invalid runtime')
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


def execute_task(work, task, env, mode):
    generated = None
    if task.get('generated_result'):
        generated = work / task['generated_result']
        require(generated.resolve().is_relative_to(work.resolve()), 'escaping generated result')
        generated.unlink(missing_ok=True)
    result = subprocess.run([sys.executable, *mode, '-c', BOOTSTRAP,
                             str(work / task['source']), *task['arguments']],
                            cwd=work / 'evidence/research_checkpoint_20261007/raw',
                            env=env, capture_output=True, timeout=task['timeout_seconds'],
                            preexec_fn=child_limits)
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


def child_limits():
    resource.setrlimit(resource.RLIMIT_AS, (3 * 2**30, 3 * 2**30))
    resource.setrlimit(resource.RLIMIT_CPU, (180, 180))


def run(root=ROOT):
    cached = source_bytes(root)
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
            observed_bytes = execute_task(work, task, env, mode)
            authenticate_copied_inputs(work, cached, generated_outputs)
            compare(expected[task['name']], final_json(observed_bytes), task['provenance_root_fields'])
        authenticate_copied_inputs(work, cached, generated_outputs)
        exe = work / 'check_growing'
        compiled = subprocess.run(['g++', '-std=c++17', '-O2', '-Wall', '-Wextra', '-pedantic',
                                   str(work / cpp['source']), '-o', str(exe)], env=env,
                                  capture_output=True, timeout=60)
        require(compiled.returncode == 0, 'growing-period exact control compilation failed')
        output = subprocess.run([str(exe)], env=env, capture_output=True, timeout=cpp['timeout_seconds'])
        require(output.returncode == 0, 'growing-period exact controls failed')
        observed = final_json(output.stdout)
        negative = subprocess.run([str(exe), '--inject-bad-carry'], env=env,
                                  capture_output=True, timeout=20)
        require(negative.returncode == 2 and b'literal cyclic carry identity' in negative.stderr,
                'injected carry defect did not fail')
        observed['negative_control'] = {'fault':'omit low-digit carry into high digit',
                                       'returncode':negative.returncode,
                                       'diagnostic':negative.stderr.decode().strip()}
        observed['compiler_command'] = ['g++', '-std=c++17', '-O2', '-Wall', '-Wextra', '-pedantic',
                                        str(work / cpp['source']), '-o', str(exe)]
        authenticate_copied_inputs(work, cached, generated_outputs)
        compare(cpp_expected, observed, cpp['provenance_root_fields'])
    require(source_bytes(root) == cached, 'sources changed during execution')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-sources', action='store_true')
    args = parser.parse_args()
    if args.check_sources:
        source_bytes(ROOT)
    else:
        run()


if __name__ == '__main__':
    main()
