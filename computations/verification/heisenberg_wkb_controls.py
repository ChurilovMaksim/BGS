#!/usr/bin/env python3
"""Run bounded exact WKB fixtures; no analytic or global cancellation certificate."""
from pathlib import Path
import subprocess
import sys

SCRIPTS = ('check_independent', 'check_raw_gauss', 'cluster_checks',
           'exact_controls', 'exact_branch_modes')

def main():
    directory = Path(__file__).resolve().parent / 'heisenberg_wkb'
    for name in SCRIPTS:
        command = [sys.executable]
        if sys.flags.optimize:
            command.append('-' + 'O' * sys.flags.optimize)
        subprocess.run(command + [str(directory / (name + '.py'))], check=True)
    print('heisenberg-wkb-controls: bounded exact fixtures passed; analytic claims unformalized')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
