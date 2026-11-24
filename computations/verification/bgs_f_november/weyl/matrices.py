"""Compatibility entry point for the archived replay command."""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")

from pathlib import Path
import runpy

if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).with_name('bgs_packet_weyl_matrices.py')), run_name="__main__")
