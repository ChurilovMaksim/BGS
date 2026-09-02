# Active research line

This directory describes the branch of reasoning that survives the 2026-09-02 audit and is the starting point for future work.

## Surviving chain

1. **Twisted-Jacobi representation.** The rank-1 Hecke-sector matrix is computed from a finite-field twisted Jacobi sum. Current kernel: `code/math/twisted_jacobi.py`.
2. **Independent computational reproduction.** The R82 q-curves are reproduced at `N=199` and `N=3571` from preserved inputs. Current check: `code/verification/baseline_r82.py`.
3. **Exact k=2 layer.** The off-diagonal constraint set has exact cardinality `(K-1)(K-2)` and the associated energy identity is directly checked. Current check: `code/verification/h3_k2_exact_reduction.py`.
4. **Spectral target.** GOE-like spacing and matched number variance are observed numerically after desymmetrisation. These measurements motivate the desired limiting theorem.
5. **Current bottleneck.** M1 must control the full twist-summed fluctuation energy. The old proof attempt is invalid; see `M1.md`.

Everything downstream is conditional until Step 5 is repaired or bypassed by a new independent argument.
