# Research ledger

This is the short active ledger. The complete historical ledger is preserved under `archive/legacy-workspace/HISTORY.md`.

## 2026-09-03 — repository re-audit and human restructure

- Rebuilt the active repository around `research/`, `src/`, `experiments/`, `results/`, `formal/`, `references/`, `paper/`, and one immutable `archive/`.
- Re-established that general BGS is open.
- Preserved the full pre-restructure corpus and original ZIP provenance while removing historical run-number clutter from the active working surface.
- Kept the audited R82, exact k=2 and scalar twisted-Jacobi checks as finite/reproducibility anchors.

## 2026-09-03 — historical M1 falsification

- Reproduced the historical Möbius-fiber assembly independently in Python and C++; cross terms are nonzero.
- Found the exact degenerate `d=0` semi-trivial values `A(0)=N-2`, contradicting the old universal `4 sqrt(N)` claim.
- Corrected the historical pole from `d-1` to `d+1` and identified the relevant annihilator-character order as `m=(N-1)/K`, not `K`.
- Classified the historical rational-function divisor: generic fibers have no nontrivial `m`-th-power case; `d=0` is the explicit exceptional family.

## 2026-09-03 — old ZIP archaeology

- Re-read late Runs 92–110 from the original ZIP instead of relying only on the cleaned repository.
- Recovered the useful k=4/even-k factorization, layer-scaling/Stieltjes evidence and rank-2/Sp4 experiments.
- Promoted only results that survived an independent reconstruction; everything else remains in the archaeology queue.

## 2026-09-03 — exact k=4 key geometry

- Rebuilt the pair-key map from the original `(x,y)` variables.
- Verified that the off-diagonal map is bijective onto `u,v in F_N^*\{1}`, `u!=v`, while the diagonal collapses to `(1,1)` with multiplicity `N-2`.
- Strengthened the k=4 verifier to reconstruct the full difference distribution `B(t)`.
- Three independent finite constructions agree at small designs: original-pair collapse, explicit/collapsed key table and corrected `H^2` permutation gather.
- Independent C++ reproduces the same exact invariants and direct Jacobi fourth moments.
- Exact anchors now include `N=23,53,199,461`.

## 2026-09-03 — Run 93.2 bookkeeping bug

- Archived `code/large_m/third_calibration.py` adds diagonal→off coupling once but omits the reverse off→diagonal ordered class.
- At `N=53,K=13` the missing class has exact size `6732`; omitting it changes `423879` to `417147`.
- Downstream old large-design outputs that depend on that producer are no longer admissible evidence until recomputed.

## 2026-09-03 — exact total V4 formula

- Counted off/off coupling by inclusion-exclusion over partner failures `h1=u`, `h2=v`, and `h1 v=h2 u`.
- Obtained
  `V_off=K^2(N-2)(N-3)-3K(K-1)(N-3)+2(K-1)(K-2)`.
- Adding both ordered mixed classes and the diagonal class gives the exact closed form
  `V4=(K^2+1)N^2-(6K^2+3K)N+13K^2-3K`.
- All active exact anchors satisfy this polynomial identically.

## 2026-09-03 — historical Möbius assembly identified as the wrong object

- Symbolic elimination gives `y=(1-v)/(u-v)` and `d=(u-1)(v-1)/(v-u)`.
- The eliminated Möbius equation contains `(u,v)=(1,1)` for every `d`, but the inverse pair map is undefined there. This is a saturation artifact.
- Exact finite comparison at `N=53,199` gives:
  - `d!=0`: `A_hist=A_key+1` for every twist pair;
  - `d=0`, first twist trivial: both equal `N-2`;
  - `d=0`, first twist nontrivial: `A_hist=-1`, `A_key=N-2`.
- Therefore the old M1 object cannot be repaired just by adding cross terms or improving a Weil bound.

## 2026-09-03 — twist sum collapses exactly to B(t)

- Defined the correct amplitude from the weighted key table.
- Double character orthogonality gives exactly
  `sum_tau(A_tau*A_tau)=m^2 B` and
  `sum_tau Ahat_tau^2=m^2 Bhat`.
- Python FFT and independent C++ direct-DFT/circular-convolution checks agree through `N=199` at floating-point precision.
- The old “cross-Gram cancellation among twists” problem is therefore replaced by one geometric `B(t)` variance problem.

## 2026-09-03 — exact Fourier mean/variance duality

- For `Sigma4(q)=sum_t B(t)e_N(qt)`, derived
  `mean_(q!=0)Sigma4=(N B(0)-V4)/(N-1)`.
- Derived the exact identity
  `Var_(q!=0)Sigma4=N Var_(t!=0)B(t)`.
- Thus `std Sigma4=O(NK)` is equivalent to `std B_off=O(K sqrt(N))`.

## 2026-09-03 — corrected scaling survives fresh falsifiers

Using the corrected key-table algorithm rather than archived producers:

- `N=199,K=11,m=18`: `mean/N^2=1.8556`, `std/(NK)=3.7996`;
- `N=461,K=23,m=20`: `1.8895`, `3.8797`;
- new trace-3 `N=521,K=13,m=40`: `1.9357`, `3.8408`.

Across a wider finite scan the data suggest `mean ~ 2N^2` and `std ~ 4NK`, but these remain conjectural asymptotics.

## 2026-09-03 — structural source of the mean

- Decomposed
  `B=O+2(N-2)C_H+(N-2)^2 delta_0`.
- Found `C_H(0)=0`.
- The diagonal self-coupling contributes `(N-2)^2` to `B(0)`.
- The off/off class `(h1,h2)=(1,1)` contributes every off key because inversion sends `d` to `-d`, giving a second exact spike `(N-2)(N-3)`.
- For `h1=h2=h!=1`, the zero-difference condition reduces to `uv=h`; one-sided `h1=1` or `h2=1` classes have no valid zero-difference solutions.
- For `h1,h2!=1` distinct, the zero-difference equation is a smooth plane cubic. This opens a Hasse-Weil route to the mean.

## 2026-09-03 — explicit mean estimate

- SymPy and Wolfram independently factor the affine singularity resultant at `t=0` as a nonzero scalar times
  `h1^5 h2^6 (h1-1)^14 (h1-h2)^4 (h2-1)^18`.
- Hence no hidden generic `t=0` singular stratum remains after `h1,h2!=1`, `h1!=h2`.
- For each generic class, projective Hasse-Weil plus a conservative finite-boundary count gives `M_h(0)=N+epsilon_h` with `|epsilon_h|<=2 sqrt(N)+28`.
- Writing `S_eta=sum_{h in H\{1}} eta(h)`, obtained
  `B0_det=2N^2+K^2N-2KN-8N-4K+14-S_eta`
  and
  `|B(0)-B0_det| <= (K-1)(K-2)(2 sqrt(N)+28)`.
- Therefore
  `mean Sigma4 = 2N^2 + O(KN+N+K^2 sqrt(N))`,
  giving the mean asymptotic in the provisional range `K=o(N^(3/4))` once the resultant calculation is converted to a publication-quality algebraic lemma.

## 2026-09-03 — generic cubic stratification and literature route

- For fixed `(h1,h2,t)`, the off/off equation is a plane cubic.
- As a quadratic in `v`, its branch-quartic discriminant exposes the strata
  `h1=h2`,
  `(h1-1)(h2-1)+t(h1-h2)=0`,
  and a quartic `Q(h1,h2,t)=0`, besides `h1=1`/`h2=1` cases.
- At `t=0`, `Q=16(h1-1)^2(h2-1)^2`, consistent with the exact smoothness resultant above.
- Fouvry-Kowalski-Michel trace-function correlation machinery has been identified as a plausible variance tool. It is **not yet applied**: conductor, monodromy, geometric-isomorphism and exceptional-stratum checks remain open.

## 2026-09-03 — code consolidation

- Moved reusable pair-key geometry into `src/python/bgs/key_geometry.py` instead of maintaining parallel experiment-specific implementations.
- Tightened subgroup construction so a purported order-`K` generator must actually return to `1` after exactly `K` steps; the earlier helper only checked that the first `K` powers were distinct. Audited production designs already had the claimed exact orders, so this changes the API guard rather than the stored results.

## Promotion rule

A historical result moves into active theory/results only after its statement, conventions and producer are reconstructed and at least one independent check is performed. Numerical scaling language is never upgraded to “theorem” without an analytic proof.
