#!/usr/bin/env python3
"""High-precision checks of the exact all-odd 24-image M_N^2 kernel.

This verifies finite identities only.  It does not test a spectral limit.
The matrix M is built from the original modular-inverse definition and
squared by mpmath matrix multiplication, independently of the image formula.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import mpmath as mp


def run_one(n: int, dps: int) -> dict:
    if n < 3 or n % 2 == 0:
        raise ValueError("N must be odd and at least three")
    mp.mp.dps = dps
    cache: dict[int, list] = {}

    def root(q: int, exponent: int):
        if q not in cache:
            cache[q] = [
                mp.exp(2 * mp.pi * mp.j * mp.mpf(k) / q) for k in range(q)
            ]
        return cache[q][exponent % q]

    def gauss(q: int, coeff: int):
        return mp.fsum(root(q, coeff * z * z) for z in range(q))

    inv8 = pow(8, -1, n)
    inv4 = pow(4, -1, n)
    half = pow(2, -1, n)
    sqrt_n = mp.sqrt(n)
    original = mp.matrix(n, n)
    # Fill explicitly so the tested original entries have an obvious source.
    for x in range(n):
        for y in range(n):
            original[x, y] = root(
                n, -inv8 * (3 * x * x - 2 * x * y + 3 * y * y)
            ) / sqrt_n
    squared = original * original

    def qform(x: int, y: int) -> int:
        return 17 * x * x - 2 * x * y + 17 * y * y

    def image_entry(x: int, y: int):
        return mp.fsum(
            root(48 * n, -qform(x, y + m * n)) for m in range(24)
        ) / mp.sqrt(24 * n)

    image = mp.matrix(n, n)
    for x in range(n):
        for y in range(n):
            image[x, y] = image_entry(x, y)

    g = math.gcd(n, 24)
    original_gauss = gauss(n, -3 * inv4)
    image_gauss = mp.fsum(root(48, -17 * n * m * m) for m in range(24))
    rho = mp.sqrt(mp.mpf(n) / 24) * image_gauss / original_gauss

    errors = {
        "rho_unit": abs(abs(rho) - 1),
        "gauss_norm": abs(abs(original_gauss) ** 2 - n * g),
        "image_gauss_norm": abs(abs(image_gauss) ** 2 - 24 * g),
        "matrix_identification": mp.mpf(0),
        "support_modulus": mp.mpf(0),
        "row_norm": mp.mpf(0),
        "weyl_shift": mp.mpf(0),
        "weyl_modulation": mp.mpf(0),
        "period_x": mp.mpf(0),
        "period_y": mp.mpf(0),
        "direct_gauss": mp.mpf(0),
        "coefficient_modulus": mp.mpf(0),
        "coefficient_phase": mp.mpf(0),
    }

    if n % 3:
        nu48 = (-pow(n, -1, 48)) % 48
        gamma = original_gauss / sqrt_n

        def direct_entry(x: int, y: int):
            f = -qform(x, y)
            return gamma * root(48 * n, f) * root(48, nu48 * f) / sqrt_n
    else:
        ell = n // 3
        nu8 = (-pow(n, -1, 8)) % 8
        nu16 = (-pow(ell, -1, 16)) % 16
        inv4_ell = pow(4, -1, ell) if ell > 1 else 0
        gamma = gauss(ell, -inv4_ell) / mp.sqrt(ell)
        assert (nu16 - 3 * nu8) % 8 == 0

        def direct_entry(x: int, y: int):
            if (x + y) % 3:
                return mp.mpf(0)
            s = (x + y) // 3
            correction = -6 * nu8 * (x * x + y * y) + nu16 * s * s
            return (
                mp.sqrt(3) * gamma / sqrt_n
                * root(48 * n, -qform(x, y)) * root(16, correction)
            )

    for x in range(n):
        errors["row_norm"] = max(
            errors["row_norm"],
            abs(mp.fsum(abs(image[x, y]) ** 2 for y in range(n)) - 1),
        )
        for y in range(n):
            errors["matrix_identification"] = max(
                errors["matrix_identification"],
                sqrt_n * abs(image[x, y] - rho * squared[x, y]),
            )
            expected_modulus = mp.mpf(g) / n if (x - 17 * y) % g == 0 else 0
            errors["support_modulus"] = max(
                errors["support_modulus"], abs(abs(image[x, y]) ** 2 - expected_modulus)
            )
            errors["weyl_shift"] = max(
                errors["weyl_shift"],
                abs(
                    image[x, (y - 1) % n]
                    - root(n, 12 * (x + half * 17)) * image[(x + 17) % n, y]
                ),
            )
            errors["weyl_modulation"] = max(
                errors["weyl_modulation"],
                abs(
                    root(n, y) * image[x, y]
                    - root(n, 17 * (x + half * 24)) * image[(x + 24) % n, y]
                ),
            )
            errors["direct_gauss"] = max(
                errors["direct_gauss"], sqrt_n * abs(squared[x, y] - direct_entry(x, y))
            )

    # Unsampled integer representatives and both deck shifts.
    for x, y in ((-2, -1), (0, 0), (1, n - 1), (n + 2, 2 * n + 1)):
        base = image_entry(x, y)
        errors["period_x"] = max(
            errors["period_x"], abs(image_entry(x + n, y) - base)
        )
        errors["period_y"] = max(
            errors["period_y"], abs(image_entry(x, y + n) - base)
        )

    # DFT the correction from the directly multiplied original matrix square.
    # This independently tests branch phases, including N<24 and 3|N.
    y_samples = sorted(set((0, 1, n // 2, n - 1)))
    for y in y_samples:
        correction = [
            sqrt_n * squared[x % n, y] * root(48 * n, qform(x, y))
            for x in range(24)
        ]
        for m in range(24):
            coeff = mp.fsum(correction[x] * root(24, -m * x) for x in range(24)) / 24
            predicted = (
                root(48, -34 * m * y - 17 * n * m * m)
                / (mp.sqrt(24) * rho)
            )
            errors["coefficient_modulus"] = max(
                errors["coefficient_modulus"], abs(abs(coeff) - 1 / mp.sqrt(24))
            )
            errors["coefficient_phase"] = max(
                errors["coefficient_phase"], abs(coeff - predicted)
            )

    threshold = mp.power(10, -(dps - 20))
    maximum = max(errors.values())
    if maximum >= threshold:
        raise AssertionError(
            f"N={n}: maximum error {mp.nstr(maximum, 12)} exceeds {mp.nstr(threshold, 12)}"
        )
    return {
        "N": n,
        "gcd_N_24": g,
        "precision_decimal_digits": dps,
        "full_matrix_entries_checked": n * n,
        "DFT_coefficients_checked": 24 * len(y_samples),
        "maximum_error": mp.nstr(maximum, 14),
        "errors": {key: mp.nstr(value, 14) for key, value in errors.items()},
        "rho_real": mp.nstr(mp.re(rho), 25),
        "rho_imag": mp.nstr(mp.im(rho), 25),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument(
        "--dimensions", default="3,5,7,9,11,15,21,25,27,33,45",
        help="Comma-separated odd dimensions; default includes both 3-adic cases and L=1."
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    results = []
    for n in map(int, args.dimensions.split(",")):
        result = run_one(n, args.dps)
        results.append(result)
        print(
            f"N={n:3d}, gcd={result['gcd_N_24']}, "
            f"max_error={result['maximum_error']}",
            flush=True,
        )
    report = {
        "scope": "Finite high-precision identity verification; no spectral-limit evidence.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "results": results,
        "total_original_matrix_entries_checked": sum(
            result["full_matrix_entries_checked"] for result in results
        ),
        "total_DFT_coefficients_checked": sum(
            result["DFT_coefficients_checked"] for result in results
        ),
    }
    if args.output is not None:
        args.output.write_text(json.dumps(report, indent=2) + "\n")
        print(f"Report: {args.output}", flush=True)


if __name__ == "__main__":
    main()
