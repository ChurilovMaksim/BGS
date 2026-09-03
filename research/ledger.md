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
