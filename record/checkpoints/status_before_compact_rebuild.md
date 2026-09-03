# Scientific status

Updated: 2026-09-03.

## Bottom line

General BGS/local eigenphase statistics for this project are **not proved**. The historical `M4D_PROOF` / Mobius-fiber argument is not an active theorem input.

The current proof program has, however, become much sharper. The exact fourth-moment object is the pair-key distribution `B(t)`. Its finite combinatorics, Fourier reduction, mean/variance duality, the mixed `k=2` energy, and most of the generic off/off elliptic-family geometry are now explicit. A restricted M1 proof chain for odd prime `K` outside an explicit cyclotomic exception set and in the first regime `K=o(N^(1/4))` has been assembled. It remains a **theorem draft pending line-by-line proof audit/formalization**, especially for computer-assisted algebraic factorizations and the precise sheaf-theoretic citations/hypotheses.

## Exact finite statements

Let `N` be an odd split prime, `H <= F_N^*` have order `K`, and `m=(N-1)/K`. For the weighted pair-key table, the exact coupled distribution `B(t)` satisfies

`V4=sum_t B(t)=(K^2+1)N^2-(6K^2+3K)N+13K^2-3K`.

For the correct key amplitudes,

`sum_(chi,psi in H^perp) (A_(chi,psi)*A_(chi,psi))(t)=m^2 B(t)`

and

`sum_(chi,psi in H^perp)|J(chi,psi;q)|^4=m^2 Sigma4(q)`,

where `Sigma4(q)=sum_t B(t)e_N(qt)`.

The exact Fourier identities are

`mean_(q!=0) Sigma4=(N B(0)-V4)/(N-1)`

and

`Var_(q!=0) Sigma4=N Var_(t!=0)B(t)`.

Independent Python/C++ exact anchors are:

| N | K | V4 | B(0) | sum B(t)^2 |
|---:|---:|---:|---:|---:|
| 23 | 11 | 48,621 | 2,609 | 103,156,981 |
| 53 | 13 | 423,879 | 12,063 | 3,410,502,105 |
| 199 | 11 | 4,681,821 | 96,641 | 115,589,503,389 |
| 461 | 23 | 111,147,915 | 641,799 | 26,960,554,630,421 |

## Mixed k=2 component: exact control outside explicit exceptions

The structural decomposition is

`B(t)=O(t)+2(N-2)C_H(t)+(N-2)^2 1_(t=0)`.

With `c(h)=(h+1)/(h-1)`,

`d(u,v)=2/(c(u)-c(v))`.

Thus `C_H` is the nonzero additive-difference representation function of the Cayley image `A=c(H\{1})`, after a bijective relabeling of the difference.

For odd prime `K`, an exact 720-system cyclotomic audit leaves only identity and inversion-swap collisions in characteristic zero. Non-forced finite-field collisions occur exactly at rational primes dividing explicit cyclotomic resultants. The default verified sets are

`E_11={23,67,89}`,

`E_13={53,79,131,157,313}`.

For prime `N == 1 (mod K)` with `N notin E_K`,

`sum_t C_H(t)^2=(K-1)(2K-5)`

and therefore the mixed layer has standard deviation `O(K sqrt(N))`, exactly the global M1 scale.

## Mean of Sigma4

Two deterministic `N^2`-scale spikes occur at `t=0`: the weighted diagonal key and the off/off inversion class `(h1,h2)=(1,1)`. Generic zero-difference classes complete to smooth genus-one curves. The current Hasse-Weil calculation gives

`mean Sigma4 = 2N^2 + O(KN + N + K^2 sqrt(N))`.

Hence the mean asymptotic is available in the provisional range `K=o(N^(3/4))`, subject to publication-quality certification of the displayed resultant/boundary calculation.

## Generic off/off elliptic family

In Cayley coordinates `a=c(u)`, `b=c(v)`, `alpha=c(h1)`, `beta=c(h2)`, put

`T_alpha(a)=(alpha*a-1)/(a-alpha)`.

The generic fiber is the plane cubic

`2/(a-b)+2/(T_alpha(a)-T_beta(b))=t`.

For `p=alpha+beta`, `d=alpha-beta`, its binary-quartic model has a squarefree residual discriminant outside the two `O(K)` parameter strata `d=0` (`h1=h2`) and `p=0` (`h1h2=1`). The generic `j`-map has degree 12 and pole type `(4,4,1,1,1,1)`, so the family is non-isotrivial.

The exact same-base symmetry is only

`(h1,h2) -> (h2^-1,h1^-1)`.

The degree-12/cusp-width argument on `X_0(n)` rules out nontrivial generic cyclic isogenies; the inseparable case is excluded by the degree of `j`. Zarhin's geometric Tate theorem then converts local-system isomorphism into isogeny, so generic rank-two local systems are non-isomorphic outside the exact involution orbit.

At the order-four bad fiber

`t=d(h1,h2)`

the cubic factors into two lines. Its `N`-scale spike is therefore counted by the already controlled `C_H(t)` energy. The other four generic bad fibers are nodal/rational.

For the exact affine key count one has the bookkeeping form

`O_lambda(t)=N-a_lambda(t)+N 1_(t=d(h1,h2))+e_lambda(t)`,

where the open-domain boundary has total degree 10, hence at most 30 geometric intersections with an irreducible cubic. Consequently `e_lambda=O(1)` on good fibers and only sparse `O(sqrt(N))` corrections remain at the non-reducible bad fibers.

## Restricted M1 theorem draft

Combining Deligne purity, Igusa monodromy for non-isotrivial elliptic curves, fixed-degree complexity bounds, the no-isogeny classification above, and quantitative sheaf quasi-orthogonality gives the draft generic estimate

`Var O(t) << K^2 N + K^4 sqrt(N) + K^4`.

The reducible bad-fiber spikes contribute `O(K^2N)` by the Cayley energy; the special `O(K)` parameter strata are no larger than target scale. Cauchy-Schwarz controls covariance with the mixed layer.

Therefore the assembled proof chain gives, in the first restricted regime,

`K=o(N^(1/4))  =>  Var_(t!=0) B(t)=O(K^2N)`,

and hence

`std Sigma4=O(NK)`, `std(Sigma4)/mean(Sigma4)=O(K/N)`.

**Status:** proof chain assembled; not yet promoted to a final published theorem. Remaining work is proof audit/formalization, not discovery of a missing cancellation mechanism.

## Reproducibility and language migration

The active codebase is consolidated around Python for symbolic/exact orchestration and data analysis, and C++20 for heavy finite-field/exhaustive kernels. Fortran is deliberately not added without a measured numerical need. Every historical Julia path is accounted for in `research/engineering/language_migration.md`; the original Julia sources remain only in the immutable archive/Git history rather than being copied into another legacy tree.

The canonical manuscript is `paper/main.tex` with built `paper/main.pdf`. There are no competing active section-level TeX manuscripts.

## Explicitly retracted / quarantined

- "General BGS proved." - false.
- Historical `M4D_PROOF` / Mobius-fiber theorem - retracted as theorem input.
- Historical Mobius assembly - wrong finite object (phantom `(1,1)` and wrong diagonal multiplicity).
- Run 93.2 third-calibration output - old producer omitted one ordered diagonal/off coupling class.
- R86/R87 noncommutative trace shortcut - invalid as stated.
- Historical `N=95419` ratio-vs-spacing KS test - compared different statistics.
- Old word-trace "certificate" - unresolved word case.
- Hecke-centering Julia series - failed line; later red-team shows basis-selection and centering/noise defects.
- Historical `cdense_transfer.jl` Perron bracket - falsified by the zero-cost self-loop.
- Historical `sol6_closed_form.jl` title/closed form - falsified by its own preserved finite rows and the new exact enumerator.

Nothing under `archive/` overrides this status.
