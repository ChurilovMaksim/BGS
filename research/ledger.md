# Research ledger

This is the short human ledger.  The complete historical ledger is preserved under `archive/legacy-workspace/HISTORY.md`.

## 2026-09-03 — repository re-audit and human restructure

- Re-established that general BGS is open in this workspace.
- Kept the audited R82, exact k=2 and scalar twisted-Jacobi checks as finite/reproducibility anchors.
- Reproduced the historical Möbius-fiber assembly in independent Python/C++; found nonzero cross terms.
- Found the exact degenerate fiber `d=0`, where semi-trivial twists give `A(0)=N-2`, invalidating the old universal `4 sqrt(N)` claim.
- Verified symbolically that the Möbius matrix determinant/resultant is `d^2`; corrected the old pole location to `u=d+1`.
- Re-read the old ZIP, including late Runs 92–110.  Important material not previously foregrounded includes the k=4/even-k factorization, layer-scaling data, Stieltjes experiments, and rank-2/Sp4 probes.
- Independently rechecked the k=4 factorization with clean Python and C++ at `N=23,53`.
- Observed that the archived even-k formula has a direct general derivation by character orthogonality.  Promoted the reduction to `theory.md`, while leaving the asymptotic variety estimate open.
- Quarantined late-archive “M1 killer test” rhetoric: its reported maximum omitted the semi-trivial `d=0` violations seen by the complete twist scan.

## Promotion rule

A historical result moves into the active theory/results only after its statement, conventions and producer are reconstructed and at least one independent check is performed.  Numerical scaling language is never upgraded to “theorem” without an analytic proof.

## 2026-09-03 — M1 character-order and divisor classification

- Derived `S=H^perp={chi_(Kj)}` and identified its generator as a character of order `m=(N-1)/K`; the old “perfect K-th power” wording used the wrong group order.
- Classified divisor collisions of `u^r v_d(u)^s`: generic fibers admit no nontrivial m-th-power case; `d=±1` add no nontrivial exception; `d=0` yields exactly the semi-trivial family `psi_1=1`, `psi_2` arbitrary.
- This matches the independent Python/C++ observation `A_(1,psi_2)(0)=N-2` and localizes the remaining analytic difficulty to exceptional-fiber extraction plus the full cross-Gram cancellation problem.

## 2026-09-03 — exact k=4 difference distribution and archive bug

- Strengthened the clean k=4 verifier: it now accumulates the full difference distribution `B(t)` directly from `(x,y,z,w)`, not only `Sigma_4(q)`.
- The same `B(t)` is independently rebuilt from the collapsed pair-key table, where `(1,1)` has multiplicity `N-2` and every off-diagonal key has multiplicity one.  The two distributions agree entry-by-entry.
- Independent Python/C++ runs give, at `N=53`, `|V4|=423879`, `B(0)=12063`, and `sum_t B(t)^2=3410502105`; at `N=23` they give `48621`, `2609`, and `103156981`.
- The ordered diagonal/off-diagonal coupling classes are exactly `6732` in each direction for `N=53` and `1890` in each direction for `N=23`.
- Found a factor-of-two bookkeeping error in archived `code/large_m/third_calibration.py`: the code inserts the diagonal-to-off-diagonal contribution only once although the ordered count contains both diagonal→off and off→diagonal.  The `N=53` analogue would give `417147` instead of `423879` if that bug were used.
- Large-design outputs depending on that producer are archaeology-only until recomputed from a corrected implementation.
