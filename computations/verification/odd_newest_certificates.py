"""Run the bounded source-bound odd-newest certificate in external scratch space."""
from pathlib import Path
import json
import subprocess
import sys
import tempfile


def main():
    script = Path(__file__).parent / 'odd_newest/run_checks.py'
    with tempfile.TemporaryDirectory() as scratch:
        result = subprocess.run([sys.executable, str(script), '--output-dir', scratch],
                                capture_output=True, text=True, timeout=600)
        if result.returncode:
            raise RuntimeError(result.stderr)
    print(json.dumps({'status': 'PASS', 'scope': 'Three source-bound exact controls and original/normal/optimized equality; no finite computation proves the all-depth theorem.'}, indent=2))


if __name__ == '__main__':
    main()
