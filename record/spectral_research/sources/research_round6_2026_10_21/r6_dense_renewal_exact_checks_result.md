> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round6_2026_10_21/r6_dense_renewal_exact_checks_result.md`. Embedded SHA256: `10f7187346a1995e392de72fd48f213cc17481194d6bb324140aed1dfa77ae33`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/histories.md).

# Exact renewal and bounded-run verification

21 October 2026. All arithmetic was exact. Formal coordinate phase variables were retained in the rooted counting comparison, so no finite phase grid was substituted for Fourier extraction.

The complete mathematical proofs are in r6_dense_renewal_long_return_obstruction.md. These tests check finite algebra and indexing only; they do not prove any spectral asymptotic.

~~~json
{
  "status": "ALL EXACT CHECKS PASSED",
  "arithmetic": "integers, fractions, formal Laurent polynomials, exact cyclotomic rings",
  "block_cases": [
    {
      "N": 2,
      "signs": [
        1,
        1
      ],
      "renewal_orders": 8,
      "finite_energy_tail_checks": 7,
      "isometric_rank_checks": [
        {
          "m": 1,
          "unit_singular_values": 1,
          "guaranteed": 1
        }
      ],
      "companion_determinants": [
        {
          "L": 1,
          "large_dim": 4,
          "small_dim": 4,
          "nonzero_determinant_degree": 3
        },
        {
          "L": 2,
          "large_dim": 6,
          "small_dim": 6,
          "nonzero_determinant_degree": 4
        },
        {
          "L": 3,
          "large_dim": 8,
          "small_dim": 8,
          "nonzero_determinant_degree": 5
        }
      ]
    },
    {
      "N": 2,
      "signs": [
        1,
        -1
      ],
      "renewal_orders": 8,
      "finite_energy_tail_checks": 7,
      "isometric_rank_checks": [
        {
          "m": 1,
          "unit_singular_values": 1,
          "guaranteed": 1
        }
      ],
      "companion_determinants": [
        {
          "L": 1,
          "large_dim": 4,
          "small_dim": 4,
          "nonzero_determinant_degree": 3
        },
        {
          "L": 2,
          "large_dim": 6,
          "small_dim": 6,
          "nonzero_determinant_degree": 4
        },
        {
          "L": 3,
          "large_dim": 8,
          "small_dim": 8,
          "nonzero_determinant_degree": 5
        }
      ]
    },
    {
      "N": 3,
      "signs": [
        1,
        1,
        1
      ],
      "renewal_orders": 8,
      "finite_energy_tail_checks": 7,
      "isometric_rank_checks": [
        {
          "m": 1,
          "unit_singular_values": 4,
          "guaranteed": 4
        },
        {
          "m": 2,
          "unit_singular_values": 4,
          "guaranteed": 2
        }
      ],
      "companion_determinants": [
        {
          "L": 1,
          "large_dim": 9,
          "small_dim": 6,
          "nonzero_determinant_degree": 5
        },
        {
          "L": 2,
          "large_dim": 15,
          "small_dim": 9,
          "nonzero_determinant_degree": 7
        },
        {
          "L": 3,
          "large_dim": 21,
          "small_dim": 12,
          "nonzero_determinant_degree": 9
        }
      ]
    },
    {
      "N": 3,
      "signs": [
        1,
        -1,
        1
      ],
      "renewal_orders": 8,
      "finite_energy_tail_checks": 7,
      "isometric_rank_checks": [
        {
          "m": 1,
          "unit_singular_values": 4,
          "guaranteed": 4
        },
        {
          "m": 2,
          "unit_singular_values": 3,
          "guaranteed": 2
        }
      ],
      "companion_determinants": [
        {
          "L": 1,
          "large_dim": 9,
          "small_dim": 6,
          "nonzero_determinant_degree": 5
        },
        {
          "L": 2,
          "large_dim": 15,
          "small_dim": 9,
          "nonzero_determinant_degree": 7
        },
        {
          "L": 3,
          "large_dim": 21,
          "small_dim": 12,
          "nonzero_determinant_degree": 9
        }
      ]
    }
  ],
  "rooted_run_cases": [
    {
      "N": 2,
      "L": 1,
      "max_n": 7,
      "rooted_pairs_checked": 5374,
      "integer_numerator_denominator": 5,
      "cases": [
        {
          "n": 1,
          "rooted_pairs": 2,
          "balanced_by_mismatch_count": {
            "0": 2
          }
        },
        {
          "n": 2,
          "rooted_pairs": 12,
          "balanced_by_mismatch_count": {
            "0": 4
          }
        },
        {
          "n": 3,
          "rooted_pairs": 32,
          "balanced_by_mismatch_count": {
            "0": 8
          }
        },
        {
          "n": 4,
          "rooted_pairs": 112,
          "balanced_by_mismatch_count": {
            "0": 16,
            "2": 16
          }
        },
        {
          "n": 5,
          "rooted_pairs": 352,
          "balanced_by_mismatch_count": {
            "0": 32,
            "2": 80
          }
        },
        {
          "n": 6,
          "rooted_pairs": 1152,
          "balanced_by_mismatch_count": {
            "0": 64,
            "2": 288
          }
        },
        {
          "n": 7,
          "rooted_pairs": 3712,
          "balanced_by_mismatch_count": {
            "0": 128,
            "2": 896
          }
        }
      ]
    },
    {
      "N": 2,
      "L": 2,
      "max_n": 7,
      "rooted_pairs_checked": 12502,
      "integer_numerator_denominator": 5,
      "cases": [
        {
          "n": 1,
          "rooted_pairs": 2,
          "balanced_by_mismatch_count": {
            "0": 2
          }
        },
        {
          "n": 2,
          "rooted_pairs": 12,
          "balanced_by_mismatch_count": {
            "0": 4
          }
        },
        {
          "n": 3,
          "rooted_pairs": 56,
          "balanced_by_mismatch_count": {
            "0": 8,
            "2": 12
          }
        },
        {
          "n": 4,
          "rooted_pairs": 176,
          "balanced_by_mismatch_count": {
            "0": 16,
            "2": 48
          }
        },
        {
          "n": 5,
          "rooted_pairs": 672,
          "balanced_by_mismatch_count": {
            "0": 32,
            "2": 160
          }
        },
        {
          "n": 6,
          "rooted_pairs": 2496,
          "balanced_by_mismatch_count": {
            "0": 64,
            "2": 480,
            "4": 72
          }
        },
        {
          "n": 7,
          "rooted_pairs": 9088,
          "balanced_by_mismatch_count": {
            "0": 128,
            "2": 1344,
            "4": 672
          }
        }
      ]
    },
    {
      "N": 2,
      "L": 3,
      "max_n": 7,
      "rooted_pairs_checked": 17078,
      "integer_numerator_denominator": 5,
      "cases": [
        {
          "n": 1,
          "rooted_pairs": 2,
          "balanced_by_mismatch_count": {
            "0": 2
          }
        },
        {
          "n": 2,
          "rooted_pairs": 12,
          "balanced_by_mismatch_count": {
            "0": 4
          }
        },
        {
          "n": 3,
          "rooted_pairs": 56,
          "balanced_by_mismatch_count": {
            "0": 8,
            "2": 12
          }
        },
        {
          "n": 4,
          "rooted_pairs": 240,
          "balanced_by_mismatch_count": {
            "0": 16,
            "2": 48
          }
        },
        {
          "n": 5,
          "rooted_pairs": 832,
          "balanced_by_mismatch_count": {
            "0": 32,
            "2": 160
          }
        },
        {
          "n": 6,
          "rooted_pairs": 3264,
          "balanced_by_mismatch_count": {
            "0": 64,
            "2": 480,
            "4": 216
          }
        },
        {
          "n": 7,
          "rooted_pairs": 12672,
          "balanced_by_mismatch_count": {
            "0": 128,
            "2": 1344,
            "4": 1344
          }
        }
      ]
    },
    {
      "N": 3,
      "L": 2,
      "max_n": 4,
      "rooted_pairs_checked": 3234,
      "integer_numerator_denominator": 9,
      "cases": [
        {
          "n": 1,
          "rooted_pairs": 3,
          "balanced_by_mismatch_count": {
            "0": 3
          }
        },
        {
          "n": 2,
          "rooted_pairs": 45,
          "balanced_by_mismatch_count": {
            "0": 9
          }
        },
        {
          "n": 3,
          "rooted_pairs": 513,
          "balanced_by_mismatch_count": {
            "0": 27,
            "2": 54
          }
        },
        {
          "n": 4,
          "rooted_pairs": 2673,
          "balanced_by_mismatch_count": {
            "0": 81,
            "2": 324
          }
        }
      ]
    }
  ],
  "rooted_pairs_checked_total": 38188,
  "prime_delay_cases": [
    {
      "p": 3,
      "cyclotomic_gauss_modulus_checks": 18,
      "exact_power_orders": 6,
      "renewal_orders": 9,
      "return_support": [
        1,
        3
      ],
      "total_energy": "3",
      "weighted_energy": "7",
      "dark_dimension": 2,
      "compressed_power_HS2": [
        6,
        4,
        2,
        2,
        2,
        2,
        2
      ]
    },
    {
      "p": 5,
      "cyclotomic_gauss_modulus_checks": 50,
      "exact_power_orders": 10,
      "renewal_orders": 15,
      "return_support": [
        1,
        5
      ],
      "total_energy": "5",
      "weighted_energy": "21",
      "dark_dimension": 4,
      "compressed_power_HS2": [
        20,
        16,
        12,
        8,
        4,
        4,
        4,
        4,
        4,
        4,
        4
      ]
    },
    {
      "p": 7,
      "cyclotomic_gauss_modulus_checks": 98,
      "exact_power_orders": 14,
      "renewal_orders": 21,
      "return_support": [
        1,
        7
      ],
      "total_energy": "7",
      "weighted_energy": "43",
      "dark_dimension": 6,
      "compressed_power_HS2": [
        42,
        36,
        30,
        24,
        18,
        12,
        6,
        6,
        6,
        6,
        6,
        6,
        6,
        6,
        6
      ]
    },
    {
      "p": 11,
      "cyclotomic_gauss_modulus_checks": 242,
      "exact_power_orders": 22,
      "renewal_orders": 33,
      "return_support": [
        1,
        11
      ],
      "total_energy": "11",
      "weighted_energy": "111",
      "dark_dimension": 10,
      "compressed_power_HS2": [
        110,
        100,
        90,
        80,
        70,
        60,
        50,
        40,
        30,
        20,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10
      ]
    },
    {
      "p": 13,
      "cyclotomic_gauss_modulus_checks": 338,
      "exact_power_orders": 26,
      "renewal_orders": 39,
      "return_support": [
        1,
        13
      ],
      "total_energy": "13",
      "weighted_energy": "157",
      "dark_dimension": 12,
      "compressed_power_HS2": [
        156,
        144,
        132,
        120,
        108,
        96,
        84,
        72,
        60,
        48,
        36,
        24,
        12,
        12,
        12,
        12,
        12,
        12,
        12,
        12,
        12,
        12,
        12,
        12,
        12,
        12,
        12
      ]
    }
  ],
  "gauss_modulus_checks_total": 746,
  "scope": "finite identities only; no assertion of H_diag or a spectral limit"
}
~~~
