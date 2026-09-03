# Scientific status

Updated: 2026-09-03.

## Established finite statements and reproducibility anchors

- Twisted-Jacobi fourth-moment baseline reproduces the preserved R82 data at `N=199` and `N=3571` to the previously audited floating-point tolerance.
- The exact `k=2` character-orthogonality reduction is reproduced at multiple designs; the active verifier now also checks its Cayley/additive-energy form and exact cyclotomic exceptional primes for `K=11,13`.
- The vectorized twisted-Jacobi matrix formula agrees with independent direct scalar character sums at `N=461` and `N=19489` within the stored tolerance.
- The exact `k=4` pair-key distribution `B(t)` is independently reconstructed in Python and C++. Current exact anchors are:
  - `N=23,K=11`: `|V4|=48,621`, `B(0)=2,609`, `sum B(t)^2=103,156,981`;
  - `N=53,K=13`: `423,879`, `12,063`, `3,410,502,105`;
  - `N=199,K=11`: `4,681,821`, `96,641`, `115,589,503,389`;
  - `N=461,K=23`: `111,147,915`, `641,799`, `26,960,554,630,421`.
- For `N<=53`, original-pair collapse, explicit keys and the corrected `H^2` algorithm agree on the exact geometry. The twist-sum identity is independently checked through `N=199` in Python and direct-DFT C++.
- The total k=4 variety count has the exact closed form
  `V4=(K^2+1)N^2-(6K^2+3K)N+13K^2-3K`.
- More generally, the even-moment factorization follows by character orthogonality. This is an exact reduction, not an asymptotic estimate.

## Exact reformulation of M1

The active fourth-moment object is the pair-key distribution `B(t)`, not the historical Möbius graph.

For the correct key amplitudes `A_(chi,psi)`, double character orthogonality gives exactly

`sum_(chi,psi) (A_(chi,psi)*A_(chi,psi))(t)=m^2 B(t)`

and

`sum_(chi,psi) A_hat_(chi,psi)(xi)^2=m^2 B_hat(xi)`.

The fourth-moment fluctuation is

`Sigma4(q)=sum_t B(t)e_N(qt)`

with exact identities

`mean_(q!=0) Sigma4=(N B(0)-V4)/(N-1)`

and

`Var_(q!=0) Sigma4=N Var_(t!=0)B(t)`.

Thus the load-bearing variance target is

`Var_(t!=0)B(t)=O(K^2 N)`.

## Mixed k=2 component: now controlled outside explicit exceptions

Write

`B(t)=O(t)+2(N-2)C_H(t)+(N-2)^2 1_{t=0}`.

With the Cayley transform

`c(h)=(h+1)/(h-1)`,

one has exactly

`d(u,v)=2/(c(u)-c(v))`.

Therefore `C_H` is the nonzero additive-difference representation function of `A=c(H\{1})`, up to a bijective relabelling of the difference variable.

For odd prime `K`, an exact `6!` cyclotomic matching audit now includes both rank-two and rank-three kernels and shows that over characteristic zero the only collisions are identity and the forced central-symmetry partner. Non-forced finite-field collisions occur exactly at a finite set of rational primes dividing explicit cyclotomic resultants.

The default exact exception sets are

`E_11={23,67,89}`,

`E_13={53,79,131,157,313}`.

For prime `N == 1 (mod K)` with `N notin E_K`,

`sum_t C_H(t)^2=(K-1)(2K-5)`

and hence

`std_(t!=0)[2(N-2)C_H(t)]=O(K sqrt(N))`.

So the mixed `k=2` component has the required M1 scale in this explicit nonexceptional odd-prime-`K` regime. The remaining dominant obstruction is the pure off/off term `O(t)`.

## Mean of Sigma4

The mean has two deterministic `N^2`-scale spikes: the diagonal key self-coupling and the `(h1,h2)=(1,1)` inversion class in `O(0)`.

For generic `h1,h2!=1`, `h1!=h2`, the zero-difference off/off equation completes to a smooth plane cubic. Independent SymPy and Wolfram resultants give no extra generic `t=0` singular stratum. Hasse-Weil therefore yields

`mean Sigma4 = 2N^2 + O(KN + N + K^2 sqrt(N))`,

once the resultant factorization is converted into a publication-quality algebraic lemma. In particular the mean asymptotic holds in the provisional range `K=o(N^(3/4))`.

## Main analytic frontier: generic off/off elliptic correlations

In Cayley coordinates `a=c(u)`, `b=c(v)`, `alpha=c(h1)`, `beta=c(h2)`, the generic off/off fiber is

`2/(a-b)+2/(T_alpha(a)-T_beta(b))=t`,

where

`T_alpha(a)=(alpha*a-1)/(a-alpha)`.

The branch-quartic discriminant has an explicit factorization. Setting

`p=alpha+beta`, `d=alpha-beta`,

the residual quartic is squarefree except on the two `O(K)` parameter strata

`d=0 <=> h1=h2`,

and

`p=0 <=> h1 h2=1`.

On the generic locus the elliptic `j`-function has a genuine order-four pole at `t=2/d`, so the family is non-isotrivial. The pole location recovers `d`; the ratio of the first two Laurent coefficients at infinity recovers `p^2`. Consequently generic same-base equality of `j`-functions occurs only for

`(h1,h2)`

and the exact key involution partner

`(h2^-1,h1^-1)`.

This reduces the remaining geometric-isomorphism problem to the natural symmetry already seen in the exact finite arrays.

Modern quantitative sheaf theory gives the right abstract next step: once the rank-two elliptic trace sheaves are constructed and shown pure/geometrically irreducible, uniformly bounded complexity follows from fixed-degree geometry, and non-isomorphic sheaves admit square-root quasi-orthogonality. The repository has **not yet** promoted those sheaf hypotheses as proved.

If that final sheaf-correlation proposition is established, the generic off/off variance satisfies

`Var O(t)=O(K^2 N + K^4 sqrt(N))`,

which gives the full M1 target in the first honest regime

`K=o(N^(1/4))`.

This is a conditional theorem target, not a completed result.

## Fresh corrected numerical evidence

Using the corrected key-table producer, not archived Run-93 outputs, larger-`m` designs remain consistent with

`mean Sigma4 ~ 2N^2`,
`std Sigma4 ~ 4NK`,
`relative std ~ 2K/N`.

Examples include `N=199,K=11,m=18`, `N=461,K=23,m=20`, and the independent trace-3 design `N=521,K=13,m=40`. These are falsifiers/evidence, not a proof of the asymptotic law.

## Explicitly retracted / not active

- “General BGS proved.” — false.
- Historical `M4D_PROOF` / Möbius-fiber theorem — retracted as a theorem input.
- The historical Möbius assembly is the wrong finite object: it contains a phantom `(1,1)` point for every `d!=0` and mishandles the multiplicity-`N-2` diagonal at `d=0`.
- R86/R87 trace-fluctuation shortcut — invalid as stated because it uses a commutative binomial expansion for noncommuting matrices and an unproved factorization.
- Historical `N=95419` ratio-vs-spacing KS result — invalid comparison of different statistics.
- Old word-trace “certificate” — unresolved word case, not a proof.
- Archived Run 93.2 third-calibration outputs — producer omits the reverse ordered off→diagonal coupling and must be recomputed before use.
- Old Sp4/rank-2 theorem labels — archaeology until representation/projector conventions are rebuilt independently.

No file under `archive/` changes the status above.
