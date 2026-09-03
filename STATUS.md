# Scientific status

Updated: 2026-09-03.

## Established finite statements and reproducibility anchors

- Twisted-Jacobi fourth-moment baseline reproduces the preserved R82 data at `N=199` and `N=3571` to the previously audited floating-point tolerance.
- The exact `k=2` character-orthogonality reduction is reproduced at `N=53` and `N=199`; the off-diagonal constraint counts are `132=(13-1)(13-2)` and `90=(11-1)(11-2)`.
- The vectorized twisted-Jacobi matrix formula agrees with independent direct scalar character sums at `N=461` and `N=19489` within the stored tolerance.
- The exact `k=4` pair-key distribution `B(t)` is independently reconstructed in Python and C++. Current exact anchors are:
  - `N=23,K=11`: `|V4|=48,621`, `B(0)=2,609`, `sum B(t)^2=103,156,981`;
  - `N=53,K=13`: `423,879`, `12,063`, `3,410,502,105`;
  - `N=199,K=11`: `4,681,821`, `96,641`, `115,589,503,389`;
  - `N=461,K=23`: `111,147,915`, `641,799`, `26,960,554,630,421`.
- For `N<=53`, original-pair collapse, explicit keys and the corrected `H^2` algorithm agree on the exact geometry. The twist-sum identity is independently checked through `N=199` in Python and direct-DFT C++.
- The total k=4 variety count now has an exact closed form:
  `V4=(K^2+1)N^2-(6K^2+3K)N+13K^2-3K`.
- More generally, the even-moment factorization follows algebraically from expanding `J^s conjugate(J)^s` and applying character orthogonality twice. This is an exact reduction, not an asymptotic estimate.

## New exact reformulation of M1

The active fourth-moment object is the pair-key distribution `B(t)`, not the historical Möbius graph.

For the correct key amplitudes `A_(chi,psi)`, double character orthogonality gives exactly

`sum_(chi,psi) (A_(chi,psi)*A_(chi,psi))(t)=m^2 B(t)`

and in Fourier space

`sum_(chi,psi) A_hat_(chi,psi)(xi)^2=m^2 B_hat(xi)`.

The fourth-moment fluctuation is

`Sigma4(q)=sum_t B(t)e_N(qt)`

with exact identities

`mean_(q!=0) Sigma4=(N B(0)-V4)/(N-1)`

and

`Var_(q!=0) Sigma4=N Var_(t!=0)B(t)`.

Therefore the load-bearing variance target is now the clean geometric estimate

`Var_(t!=0)B(t)=O(K^2 N)`.

## Fresh corrected numerical evidence

Using the corrected key-table producer, not archived Run-93 outputs, larger-`m` designs are consistent with

`mean Sigma4 ~ 2N^2`,
`std Sigma4 ~ 4NK`,
`relative std ~ 2K/N`.

Examples include `N=199,K=11,m=18`, `N=461,K=23,m=20`, and the new trace-3 design `N=521,K=13,m=40`. This is evidence for the theorem target, not a proof.

## Main analytic frontier

Write

`B(t)=O(t)+2(N-2)C_H(t)+(N-2)^2 1_{t=0}`.

The mean has two deterministic `N^2`-scale spikes: the diagonal key self-coupling and the `(h1,h2)=(1,1)` inversion class in `O(0)`. For generic `h1,h2!=1`, `h1!=h2`, the zero-difference off/off equation completes to a smooth plane cubic. Independent SymPy and Wolfram resultants give no additional generic `t=0` singular stratum. A Hasse-Weil argument therefore yields

`mean Sigma4 = 2N^2 + O(KN + N + K^2 sqrt(N))`,

once the displayed resultant factorization is converted into a publication-quality algebraic lemma. In particular the mean asymptotic holds in the provisional range `K=o(N^(3/4))`.

The variance is harder. The off/off layer is a family of cubic/elliptic point-count fluctuations. Candidate Deligne/Katz/Fouvry-Kowalski-Michel trace-function correlation machinery has been identified, but its conductor, monodromy, geometric-isomorphism and exceptional-parameter hypotheses have **not** yet been verified for this family.

## Explicitly retracted / not active

- “General BGS proved.” — false.
- Historical `M4D_PROOF` / Möbius-fiber theorem — retracted as a theorem input.
- The historical Möbius assembly itself is the wrong finite object: it contains a phantom `(1,1)` point for every `d!=0` and mishandles the multiplicity-`N-2` diagonal at `d=0`.
- R86/R87 trace-fluctuation shortcut — invalid as stated because it uses a commutative binomial expansion for noncommuting matrices and an unproved factorization.
- Historical `N=95419` ratio-vs-spacing KS result — invalid comparison of different statistics.
- Old word-trace “certificate” — unresolved word case, not a proof.
- Archived Run 93.2 third-calibration outputs — producer omits the reverse ordered off→diagonal coupling and must be recomputed before use.
- Old Sp4/rank-2 theorem labels — archaeology until representation/projector conventions are rebuilt independently.

No file under `archive/` changes the status above.
