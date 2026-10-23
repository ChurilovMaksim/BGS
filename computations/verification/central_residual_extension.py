"""Bounded exact replay of two distinct residual interfaces."""
from pathlib import Path
import json
import hashlib
import os
import subprocess
import sys
import tempfile


def main():
    root = Path(__file__).resolve().parents[2]
    mapping = json.loads((root / "record/central_residual_promotion_map.json").read_text())
    for row in mapping:
        target = root / row["public_path"]
        if hashlib.sha256(target.read_bytes()).hexdigest() != row["public_sha256"]:
            raise RuntimeError("Source identity mismatch: " + row["public_path"])
    reports = []
    for kind in ("hamming", "translation", "all_translation", "low_switch"):
        script = Path(__file__).resolve().parent / "central_residual" / (kind + ".py")
        expected = json.loads((root / "archive/evidence/central_residual_20261007" / (kind + "_expected.json")).read_text())
        with tempfile.TemporaryDirectory() as scratch:
            output = Path(scratch) / "output.json"
            env = dict(os.environ, OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", MKL_NUM_THREADS="1")
            command = [sys.executable] + (["-O"] if sys.flags.optimize else []) + [str(script), "--output", str(output)]
            result = subprocess.run(command, cwd=scratch, env=env, capture_output=True, text=True, timeout=200)
            if result.returncode:
                raise RuntimeError(result.stderr)
            actual = json.loads(output.read_text())
        if kind == "hamming":
            actual.pop("runtime_seconds")
            expected.pop("runtime_seconds")
        if actual != expected:
            raise RuntimeError(kind + " exact result mismatch")
        reports.append({"control": kind, "exact_output_match": True})
    print(json.dumps({"status": "PASS", "checks": reports, "scope": "Finite exact controls only; analytic bounds and distinct residual representations retain their separately reviewed hypotheses."}, indent=2))


if __name__ == "__main__":
    main()
