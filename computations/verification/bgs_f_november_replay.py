#!/usr/bin/env python3
"""Canonical workspace entry point for the November BGS-F finite replay."""

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from pathlib import Path
import runpy


if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).with_name("bgs_f_november") / "verify_all.py"),
                   run_name="__main__")
