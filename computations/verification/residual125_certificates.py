"""Exact bounded residual-125 controls; no analytic or uniform-depth formalization."""
from pathlib import Path
import hashlib
import json
import os
import resource
import subprocess
import sys
import tempfile


def limits():
    resource.setrlimit(resource.RLIMIT_AS, (2 * 1024**3, 2 * 1024**3))
    resource.setrlimit(resource.RLIMIT_CPU, (120, 120))


def main():
    root = Path(__file__).resolve().parents[2]
    mapping = json.loads((root / 'record/residual125_promotion_map.json').read_text())
    for row in mapping:
        if hashlib.sha256((root / row['public_path']).read_bytes()).hexdigest() != row['public_sha256']:
            raise RuntimeError('Source identity mismatch: ' + row['public_path'])
    rows = []
    for kind in ('raw', 'residue'):
        script = Path(__file__).parent / 'residual125' / (kind + '.py')
        with tempfile.TemporaryDirectory() as scratch:
            command = [sys.executable] + (['-O'] if sys.flags.optimize else []) + [str(script), scratch]
            result = subprocess.run(command, cwd=scratch, capture_output=True, text=True,
                                    timeout=150, preexec_fn=limits,
                                    env=dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1'))
            if result.returncode:
                raise RuntimeError(result.stderr)
            actual = json.loads((Path(scratch) / (kind + '_rebuild.json')).read_text())
        expected = json.loads((root / 'archive/evidence/residual125_20261007' / (kind + '_expected.json')).read_text())
        for value in (actual, expected):
            if not isinstance(value.get('python'), str) or not value['python']:
                raise RuntimeError('Missing or invalid Python environment metadata')
        provenance = {'original_python': expected['python'], 'replay_python': actual['python'],
                      'original_script_sha256': expected['script_sha256'],
                      'replay_script_sha256': actual['script_sha256']}
        for field in ('seconds', 'script_sha256', 'python'):
            actual.pop(field)
            expected.pop(field)
        if actual != expected:
            raise RuntimeError(kind + ' complete scientific output mismatch')
        rows.append({'control': kind, 'exact_scientific_output_agreement': True, 'provenance': provenance})
    print(json.dumps({'status': 'PASS', 'checks': rows,
                      'scope': '288 exact residue matrices and bounded raw identities; uniform depth and literal-time conclusions require the separately reviewed proofs.'}, indent=2))


if __name__ == '__main__':
    main()
