"""Verify the complete BGS-F folder. Run with Python 3 from any directory."""

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from argparse import ArgumentParser
from hashlib import file_digest
import os
from pathlib import Path
from shutil import copytree
from tempfile import TemporaryDirectory
import subprocess
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parent

NEW_CHECKS = [
    ("alignment/check.py", "--verify"),
    ("histories/check.py", "--verify"),
    ("torsion_transport/check.py", "--verify"),
    ("relation_rank/check.py", "--verify"),
    ("relation_rank/check_rank.py",),
    ("resolution_precision/check.py", "--verify"),
    ("resolution_precision/check_matrix.py",),
]
RESEARCH_CHECKS = [
    ("effective_gaps/check_intervals.py", "--verify"),
    ("effective_gaps/check_matrix.py",),
    ("exact_splitting/check.py", "--verify"),
    ("exact_splitting/check_matrix.py",),
    ("critical_oscillation/check.py", "--verify"),
    ("critical_oscillation/check_matrix.py",),
    ("critical_block/check.py", "--verify"),
    ("critical_block/check_matrix.py",),
    ("split_law/check.py", "--verify"),
    ("split_law/check_matrix.py",),
    ("signed_decay/check.py", "--verify"),
    ("signed_decay/check_decay.py",),
    ("fourth_order/check.py", "--verify"),
    ("fourth_order/check_matrix.py",),
    ("resolvent/check.py", "--verify"),
    ("resolvent/check_matrix.py",),
    ("spectrum/check.py", "--verify"),
    ("symmetries/check.py", "--verify"),
    ("second_order/check.py", "--verify"),
    ("zero_mode/weights.py", "--verify"),
    ("zero_mode/check.py", "--verify"),
    ("translated/check.py", "--verify"),
    ("reconnection/check.py", "--verify"),
    ("contacts/recheck.py",),
    ("spacings/recheck.py",),
    ("weyl/recheck.py",),
    ("continuation/recheck.py",),
    ("research/verify.py",),
]


def verify_manifest(root):
    checked = 0
    for line in (root/"SHA256SUMS").read_text(encoding="utf-8").splitlines():
        claimed, member = line.split("  ",1)
        path = root/member
        if path.resolve().is_relative_to(root) and path.is_file():
            with path.open("rb") as stream:
                computed = file_digest(stream,"sha256").hexdigest()
            if computed==claimed:
                checked += 1
                continue
        raise RuntimeError(f"Checksum failed: {member}")
    print(f"SHA-256: {checked} files verified.", flush=True)


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--quick", action="store_true", help="Run the new checks only.")
    parser.add_argument("--rebuild-pell", action="store_true",
                        help="Also compile C++ and regenerate the Pell-209 certificate.")
    args = parser.parse_args()

    verify_manifest(ROOT)
    checks = list(NEW_CHECKS if args.quick else NEW_CHECKS+RESEARCH_CHECKS)
    environment = os.environ.copy()
    environment["OPENBLAS_NUM_THREADS"] = "1"
    started = monotonic()
    for number, command in enumerate(checks,1):
        print(f"\n[{number}/{len(checks)}] {' '.join(command)}",flush=True)
        subprocess.run([sys.executable,*command],cwd=ROOT,env=environment,check=True)
    if args.rebuild_pell:
        print("\nRebuilding Pell-209 in an isolated temporary directory.", flush=True)
        with TemporaryDirectory(prefix="bgs-pell-209-") as directory:
            source = Path(directory) / "research"
            copytree(ROOT / "research", source, ignore=lambda _, names: [n for n in names if n in {"__pycache__", "build"}])
            subprocess.run([sys.executable, "reproduce.py"], cwd=source, env=environment, check=True)
            for name in ("diag00.txt", "diag01.txt", "diag10.txt", "diag11.txt"):
                if (source / "data" / name).read_bytes() != (ROOT / "research" / "data" / name).read_bytes():
                    raise RuntimeError(f"Exact diagonal replay changed {name}")
    print(f"\nPassed {len(checks)} checks in {monotonic()-started:.1f} s.",flush=True)


if __name__=="__main__":
    main()
