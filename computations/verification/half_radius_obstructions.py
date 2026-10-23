"""Source-bound bounded auxiliary half-radius controls, not actual-map tests."""
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
    resource.setrlimit(resource.RLIMIT_CPU, (160, 160))


def main():
    root = Path(__file__).resolve().parents[2]
    for row in json.loads((root / 'record/half_radius_promotion_map.json').read_text()):
        if hashlib.sha256((root / row['public_path']).read_bytes()).hexdigest() != row['public_sha256']:
            raise RuntimeError('Source identity mismatch: ' + row['public_path'])
    with tempfile.TemporaryDirectory() as scratch:
        output = Path(scratch) / 'result.json'
        command = [sys.executable, '-B'] + (['-O'] if sys.flags.optimize else [])
        command += [str(Path(__file__).parent / 'half_radius/check.py'), '--output', str(output)]
        result = subprocess.run(command, cwd=scratch, capture_output=True, text=True,
                                timeout=180, preexec_fn=limits,
                                env=dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1'))
        if result.returncode:
            raise RuntimeError(result.stderr)
        actual = json.loads(output.read_text())
    expected = json.loads((root / 'archive/evidence/half_radius_20261007/run_final/results.json').read_text())
    actual.pop('elapsed_seconds')
    expected.pop('elapsed_seconds')
    if actual != expected:
        raise RuntimeError('Exact scientific output mismatch')
    print(json.dumps({'status': 'PASS', 'exact_scientific_output_agreement': True,
                      'scope': 'Auxiliary Fourier and symplectic models only; no actual quantizer or BGS counterexample.'}, indent=2))


if __name__ == '__main__':
    main()
