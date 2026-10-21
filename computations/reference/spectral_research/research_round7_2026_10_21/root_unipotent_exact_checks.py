#!/usr/bin/env python3
"""Exact, bounded checks of the explicit finite-field countermodel.

Run from the workspace root:
  python3 research_round7_2026_10_21/root_unipotent_exact_checks.py

This is a newly designed and authorized computation. Its tested assertion is
finite and is not an asymptotic claim. Only the standard library is used.
"""

from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import os
import platform
import resource
import subprocess
import sys
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PRIMES = (5, 7, 11)
PROOF = HERE / "root_unipotent_flat_clock.md"
SCRIPT = Path(__file__).resolve()
RESULT = HERE / "root_unipotent_exact_checks_result.json"
MANIFEST = HERE / "root_unipotent_exact_checks_manifest.json"


def file_hash(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def cyclotomic_equal(a: list[int], b: list[int]) -> bool:
    """For prime p, Phi_p=1+...+X^(p-1); both arrays have length p."""
    difference = [x - y for x, y in zip(a, b)]
    return all(x == difference[0] for x in difference)


def phase(t: int, k: int, l: int, p: int) -> int:
    return (t * l * l * pow(2, -1, p)
            + t * t * k * l * pow(2, -1, p)
            + t * t * t * k * k * pow(6, -1, p)) % p


def matmul(a: tuple, b: tuple, p: int) -> tuple:
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) % p
                       for j in range(2)) for i in range(2))


def matvec(a: tuple, x: tuple, p: int) -> tuple:
    return tuple(sum(a[i][j] * x[j] for j in range(2)) % p
                 for i in range(2))


def dot(x: tuple, y: tuple, p: int) -> int:
    return sum(a * b for a, b in zip(x, y)) % p


def transpose(a: tuple) -> tuple:
    return tuple(zip(*a))


def run_checks() -> dict:
    checks = Counter()
    per_prime = []

    def verify(condition: bool, name: str) -> None:
        if not condition:
            raise AssertionError(name)
        checks[name] += 1

    for p in PRIMES:
        verify(p > 3 and all(p % q for q in range(2, int(p ** 0.5) + 1)),
               "prime_and_denominators")
        vectors = tuple(product(range(p), repeat=2))
        half = pow(2, -1, p)
        before = checks.total()

        # Full cocycle population, including t=0 and s=0.
        for t, s, k, l in product(range(p), repeat=4):
            verify((phase(t, k, l, p) + phase(s, k, l + t * k, p)
                    - phase(t + s, k, l, p)) % p == 0,
                   "full_cocycle")

        multiplicities = [p - 1] * p
        for l in range(p):
            multiplicities[half * l * l % p] += 1
        verify(sum(multiplicities) == p * p, "spectrum_dimension")
        verify(all(p - 1 <= m <= p + 1 for m in multiplicities),
               "spectrum_multiplicity_range")

        for k in range(1, p):
            verify(sum(phase(1, k, l, p) for l in range(p)) % p == 0,
                   "weighted_cycle_phase_product")
            verify(len({(l + k) % p for l in range(p)}) == p,
                   "cycle_permutation")

        for n in range(0, 2 * p + 1):
            t = n % p
            spectral_trace = [0] * p
            for s, multiplicity in enumerate(multiplicities):
                spectral_trace[n * s % p] += multiplicity
            direct_trace = [0] * p
            for k, l in vectors:
                if (l + t * k) % p == l:
                    direct_trace[phase(t, k, l, p)] += 1
            verify(cyclotomic_equal(spectral_trace, direct_trace),
                   "trace_from_spectrum_vs_monomial_operator")
            norm = [sum(direct_trace[a] * direct_trace[(a - r) % p]
                        for a in range(p)) for r in range(p)]
            expected = [p ** 4 if t == 0 else p] + [0] * (p - 1)
            verify(cyclotomic_equal(norm, expected), "exact_trace_norm")

        for t in range(1, p):
            it = pow(t, -1, p)
            h = ((t ** 3 * pow(3, -1, p) % p, t * t * half % p),
                 (t * t * half % p, t))
            g = ((12 * it ** 3 % p, -6 * it ** 2 % p),
                 (-6 * it ** 2 % p, 4 * it % p))
            y = ((1, t), (0, 1))
            verify((h[0][0] * h[1][1] - h[0][1] * h[1][0]) % p
                   == t ** 4 * pow(12, -1, p) % p, "hessian_determinant")
            verify(matmul(h, g, p) == ((1, 0), (0, 1)), "hessian_inverse")
            d = matmul(g, y, p)
            verify(d == ((12 * it ** 3 % p, 6 * it ** 2 % p),
                         (-6 * it ** 2 % p, -2 * it % p)),
                   "mixed_endpoint_coefficient")
            skew = tuple(tuple((d[i][j] - d[j][i]) % p for j in range(2))
                         for i in range(2))
            verify((skew[0][1] * skew[1][0]) % p != 0,
                   "reverse_edge_nondegeneracy")

            centered = [0] * p
            for k, l in vectors:
                centered[phase(t, k, l, p)] += 1
            gauss_norm = [sum(centered[a] * centered[(a - r) % p]
                              for a in range(p)) for r in range(p)]
            verify(cyclotomic_equal(gauss_norm, [p * p] + [0] * (p - 1)),
                   "exact_centered_gauss_norm")

            # All linear terms. A histogram rotation checks completing the
            # square before any use of the cyclotomic quotient.
            for v in vectors:
                direct = [0] * p
                for k, l in vectors:
                    direct[(phase(t, k, l, p) + k * v[0] + l * v[1]) % p] += 1
                shift = (-half * dot(v, matvec(g, v, p), p)) % p
                expected = [centered[(r - shift) % p] for r in range(p)]
                verify(direct == expected, "all_linear_terms_square_completion")
                norm = [sum(direct[a] * direct[(a - r) % p]
                            for a in range(p)) for r in range(p)]
                verify(cyclotomic_equal(norm, [p * p] + [0] * (p - 1)),
                       "all_kernel_gauss_norms")

            ygy = matmul(matmul(transpose(y), g, p), y, p)
            ag = tuple(tuple((ygy[i][j] - g[i][j]) % p for j in range(2))
                       for i in range(2))

            def action(x: tuple, yy: tuple) -> int:
                transformed_y = matvec(y, yy, p)
                v = tuple((transformed_y[i] - x[i]) % p for i in range(2))
                return (-half * dot(v, matvec(g, v, p), p)) % p

            for x, yy in product(vectors, repeat=2):
                rhs = (half * dot(x, matvec(ag, x, p), p)
                       - half * dot(yy, matvec(ag, yy, p), p)
                       + dot(x, matvec(skew, yy, p), p)) % p
                verify((action(x, yy) - action(yy, x)) % p == rhs,
                       "all_endpoint_reverse_edge_phases")

            # Exact character orthogonality for every row difference, the
            # invariant that fixes the norm rather than a floating SVD.
            for r in vectors:
                histogram = [0] * p
                for yy in vectors:
                    histogram[dot(r, matvec(skew, yy, p), p)] += 1
                expected = ([p * p] + [0] * (p - 1) if r == (0, 0)
                            else [p] * p)
                verify(histogram == expected, "reverse_edge_orthogonality")

        per_prime.append({"p": p, "dimension": p * p,
                          "assertions_after_prime_setup": checks.total() - before})

    return {"status": "all finite assertions passed", "primes": list(PRIMES),
            "checks": dict(sorted(checks.items())),
            "total_assertions": checks.total(), "per_prime": per_prime,
            "non_claim": "No computation of the original fixed-kick spectrum; "
                         "no finite test is used as a proof of an asymptotic."}


def main() -> None:
    started = datetime.now(timezone.utc).isoformat()
    start_time = time.perf_counter()
    inputs = {str(p.relative_to(ROOT)): file_hash(p) for p in (SCRIPT, PROOF)}
    result = run_checks()
    elapsed = time.perf_counter() - start_time
    RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    after = {str(p.relative_to(ROOT)): file_hash(p) for p in (SCRIPT, PROOF)}
    if after != inputs:
        raise RuntimeError("Input artifacts changed during the exact run.")
    git_result = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                                text=True, capture_output=True, check=False)
    if git_result.returncode == 0:
        dirty = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT,
                               text=True, capture_output=True, check=False)
        repository = {"commit": git_result.stdout.strip(),
                      "dirty": bool(dirty.stdout.strip())}
    else:
        repository = {"commit": "unavailable: workspace has no readable Git revision",
                      "dirty": True}
    manifest = {
        "schema_version": 2,
        "claim_id": "r7-explicit-finite-field-countermodel-exact-checks",
        "repository": repository,
        "command": [sys.executable, str(SCRIPT.relative_to(ROOT))],
        "environment": {
            "software": [{"name": "Python", "version": platform.python_version()},
                         {"name": "arithmetic", "version": "standard-library integers"}],
            "hardware": platform.platform() + "; machine=" + platform.machine()
                        + "; observed CPU count=" + str(os.cpu_count())},
        "mathematics": {
            "assertion_tested": "For p in {5,7,11}: all cocycle tuples, all "
                "nonzero times, every finite-field linear term and endpoint "
                "pair; exact Gauss norms, reverse-edge phases/orthogonality, "
                "and traces for 0<=n<=2p agree with the written formulas.",
            "coefficient_domain": "F_p and Z[X]/(1+X+...+X^(p-1)), p prime",
            "conventions": "Finite-field fractions are modular inverses; "
                "Fourier F has positive exponent; C=F* V F; d=p^2.",
            "inputs": [str(PROOF.relative_to(ROOT)), str(SCRIPT.relative_to(ROOT))],
            "bounds": {"primes": list(PRIMES), "max_dimension": max(PRIMES) ** 2,
                       "times": "all 0<=t<p; trace powers 0<=n<=2p",
                       "tuple_coverage": "exhaustive in each explicitly stated finite domain"},
            "non_claims": [result["non_claim"], "No claim of historical novelty"]},
        "randomness": {"used": False, "generator": "none", "seed": None},
        "run": {"started_at": started, "runtime_seconds": elapsed,
                "exit_status": 0, "status": "completed",
                "resource_limits": {"memory_bytes": None, "cpu_seconds": None,
                                    "max_cores": 1, "max_threads": 1}},
        "outputs": [{"path": str(RESULT.relative_to(ROOT)), "sha256": file_hash(RESULT),
                     "kind": "result"}],
        "checks": list(result["checks"]),
        "result": result["status"],
        "residual_risks": ["Finite verification is bounded to the listed primes.",
                           "The all-prime and asymptotic claims require the separate proof."],
        "input_artifacts": [{"path": name, "sha256": value,
                             "sha256_after": after[name]} for name, value in inputs.items()],
        "declared_results": [str(RESULT.relative_to(ROOT))],
        "observed_max_rss_platform_units": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"result": result["status"], "assertions": result["total_assertions"],
                      "runtime_seconds": elapsed, "manifest": str(MANIFEST.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
