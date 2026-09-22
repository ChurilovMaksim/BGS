# Fixed-map frontier attempt: clustered spectra, Abel energy, and a time-window falsifier

Date: 22 September 2026. Base: `ChurilovMaksim/BGS@39d4e01ae6a6b3eb472ab30266b708ca71a70a16`.

Status: self-contained elementary finite-spectrum theorem and counterexample; self-reviewed and numerically checked. Not a positive BGS theorem, not a realization by the frozen map, and no external novelty claim.

## Target contract and actual outcome

The unchanged positive target is the pair limit for the prescribed frozen family `U_N=exp(i 10^-80 N A_N) M_N`, namely `L_N(s) -> (1-exp(-2s))/(4s^2)` at every `s>0`, followed by all-order correlations. No estimate proving the model-specific mixed-loop hypotheses has been obtained here. The result below distinguishes an Abel transform (which includes short times) from a window bounded away from zero in Heisenberg units. It strengthens a quantitative consequence for the already different compensated family, and prevents an incorrect extension of its Heisenberg-window theorem.

Inputs read: `mathematics/fixed_map_resolvent_frontier.md`, `three_orientation_resolvent_barrier.md`, `fixed_map_moment_control_and_transfer.md`, `compensated_heisenberg_trace_control.md`, `smooth_recurrence_and_compensation.md`, and `supplement/fixed_map/weighted-secular/determinant_boundary.md`. Text search across `mathematics` and `supplement` for Abel, Poisson kernel, clustered transforms and vanishing Heisenberg windows found related reductions and clustering bounds, but not the explicit counterexample below. This is bounded corpus deduplication, not a priority search.

## 1. Exact Abel lower bound from a union of short arcs

Let `D>=2` eigenphases `x_j` lie on `R/Z`, and suppose they are contained in a union of `K` arcs of radius `eta`, with `0<=eta<1/2`. Overlaps and unequal occupancies are allowed. Put

\[
L_D(s)=D^{-2}\sum_{m\ge1}e^{-2sm/D}\left|\sum_j e^{2\pi i m x_j}\right|^2,
\quad J=\max(1,\lceil2D\eta\rceil),\quad s>0.
\]

Then

\[
\boxed{L_D(s)\ge
\frac{1}{2KJ}\frac{\sinh(2s/D)}{\cosh(2s/D)-\cos(2\pi/D)}-\frac12.}
\tag{A}
\]

**Proof.** Assign each point to one containing arc, then divide each arc into at most `J` intervals of length at most `1/D`. If their occupancies are `b_t`, Cauchy--Schwarz gives `sum_t b_t^2 >= D^2/(KJ)`. For `q=exp(-2s/D)`, the absolutely convergent Poisson expansion is

\[
P_q(2\pi x)=1+2\sum_{m\ge1}q^m\cos(2\pi m x)
=\frac{\sinh(2s/D)}{\cosh(2s/D)-\cos(2\pi x)}.
\]

Consequently `2L_D+1=D^-2 sum_{j,k} P_q(2pi(x_j-x_k))`. This kernel is positive. A same-cell ordered pair has circular distance at most `1/D<=1/2`, and thus kernel at least the fraction in (A). Discard all other positive terms and apply the occupancy inequality. Equal labels are included; their inclusion is exactly compatible with the `-1/2` normalization. This proves (A).

For fixed `s`, the fraction in (A) is

\[
\frac{sD}{s^2+\pi^2}(1+O_s(D^{-2})).
\]

Since `J<=1+2D eta`, we obtain the consequence

\[
K/D\to0,\quad K\eta\to0
\quad\Longrightarrow\quad L_D(s)\to+\infty
\quad\text{for every fixed }s>0.
\tag{B}
\]

Indeed `KJ/D <= K/D+2K eta ->0`. No multiplicity hypothesis or random phases enter.

### Application to the compensated family

The cited compensated norm estimate gives spectral containment with `eta=delta_N/4`, where

\[
\delta_N=C_g|\epsilon|^3/N^2+D_g\epsilon^2/N^3.
\]

On the inversion-odd sector, `D=(N-1)/2` and `K=O(log N)`. Therefore (B) proves divergence of its Abel pair transform in the entire existing pinning range

\[
\epsilon=o(N^{2/3}K^{-1/3}).
\]

This is an explicit transform consequence of the existing clustering theorem, not a new dynamical estimate. The phase-normalized full-space version also follows from the same spectral containment with `D=N`. It extends neither the positive-time window estimate (H9) nor the fixed-strength BGS target.

## 2. Simple clustered spectra can have uniformly vanishing positive-time form factors

Take integers `K>=3`, `n>=2`, `D=Kn`, and `0<eta<1/(2K)`. Define

\[
x_{j,r}=j/K-\eta+rh,\qquad h=2\eta/(n-1),
\quad 0\le j<K,\quad0\le r<n.
\tag{C}
\]

These `D` eigenvalues are simple: the `K` arcs are disjoint and each internal step is positive. Assume along a sequence

\[
K\to\infty,\quad n\to\infty,\quad K\eta\to0,
\quad D\eta^2\to\infty.
\tag{D}
\]

Then simultaneously:

1. The empirical globally unfolded nearest-neighbour spacing law tends to `delta_0`.
2. `L_D(s)->infinity` for every fixed `s>0`.
3. For every fixed `0<a<b`,

\[
\boxed{\sup_{aD\le m\le bD}\frac{|\operatorname{Tr}U_D^m|^2}{D}\to0.}
\tag{E}
\]

**Proof of 1.** There are `K(n-1)` internal gaps, all with unfolded size `Dh=2K eta n/(n-1)->0`. Only `K` gaps remain. Their proportion is `1/n->0`.

**Proof of 2.** Apply (B), using `K/D=1/n`.

**Proof of 3.** Factor the trace exactly:

\[
p_m=e^{-2\pi i m\eta}
\left(\sum_{j=0}^{K-1}e^{2\pi i mj/K}\right)
\left(\sum_{r=0}^{n-1}e^{2\pi i mrh}\right).
\]

Thus it vanishes unless `K|m`. At a resonant time,

\[
|p_m|=K\left|\frac{\sin(\pi mnh)}{\sin(\pi mh)}\right|.
\]

For all sufficiently large members of the sequence, uniformly for `aD<=m<=bD`, one has `0<mh<=1/2`, because `bDh=2bK eta n/(n-1)->0`. Hence `sin(pi mh)>=2mh` and

\[
\frac{|p_m|^2}{D}
\le\frac{K^2}{4Dm^2h^2}
\le\frac{(n-1)^2}{16a^2Dn^2\eta^2}
\le\frac{1}{16a^2D\eta^2}\to0.
\tag{F}
\]

This also holds at nonresonant times, where the left side is zero. An explicit sequence is `n=K^5`, `D=K^6`, `eta=K^-2`.

For the explicit sequence, the Abel contribution from every `m>=aD`, with fixed `a>0`, actually tends to zero. Set `M=floor(1/(2h))`. On `aD<=m<=M`, the same sine bound gives `F_D(m)<=D/(16m^2 eta^2)`, so its contribution to `L_D` is at most `O_a(1/(D eta^2))`. For `m>M`, the bound `|p_m|<=D` gives a geometric tail at most `O_s(D) exp[-s/(Dh)]`. Because `D=K^6` and `Dh~2/K`, both bounds tend to zero. Thus the divergence of `L_D(s)` in this explicit sequence comes entirely from `m/D->0`; this assertion requires the displayed polynomial sequence, not merely the general assumptions (D).

All spectra (C) converge macroscopically to uniform measure: their displacement from a uniform `K`-root measure is bounded by `eta`, while `K->infinity`. Thus lack of macroscopic uniformity does not explain (E).

### Consequence for inference

Microscopic spacing collapse and divergent close-pair/Abel observables do not force a divergent, or even nonzero, form factor in any fixed window bounded away from zero in Heisenberg units. In this construction the diverging Abel mass is supported at times escaping toward zero after division by `D`. Thus the existing condition `D delta_N->0` in the compensated Heisenberg-window argument cannot simply be replaced by `K delta_N->0` using clustering alone. No contradiction with (H9) occurs: the construction has `D eta->infinity`.

This is a counterexample to an abstract spectral implication. It is not shown to arise from the compensated quantization or from the prescribed frozen Anosov map. It does not refute the conjectured fixed-map BGS limit.

## 3. Executed routes and limits

- Mixed-loop route: read the first mixed identities, Bessel/Herglotz bounds and three-orientation differential barrier. The residual decay remains an independent model-specific hypothesis. Raising a moment order without controlling that hypothesis would add conditional algebra, not prove the target; no such step is claimed.
- Compensated trace route: tested the tempting replacement of `D delta->0` by `K delta->0`. Construction (C) falsifies its spectral-only version, with the stronger conclusion (E).
- Positive-kernel route: proved (A)--(B) and transferred them to the existing compensated pinning theorem. This is a valid quantitative corollary, but its family has vanishing classical strength.

A genuine next route must supply a fixed-map mechanism controlling mixed products, not a generic concentration or simplicity argument. No such mechanism was found in this attempt.

## 4. Numerical verification and reproducible code

The proof is analytic. The following floating diagnostic checked independent direct spectral sums against the exact trace factorization in `(K,n,eta)=(3,11,.005),(5,9,.008),(7,5,.002)` for `1<=m<=2D`; maximum absolute errors were `3.19e-13`, `1.53e-13`, and `6.31e-13`. Direct Poisson energies were respectively `4.2035974096`, `2.3599694797`, `1.9243512799`, each above (A). The bound may be negative at small dimensions, which is harmless.

The explicit asymptotic sequence was checked on `[D/2,D]`:

| K | D | maximum F on resonant times | bound (F) |
|---|---:|---:|---:|
| 5 | 15625 | 0.004185313711 | 0.010000000000 |
| 7 | 117649 | 0.002101804327 | 0.005102040816 |
| 9 | 531441 | 0.001263504242 | 0.003086419753 |
| 11 | 1771561 | 0.000843016544 | 0.002066115702 |

One initial exploratory family `n=K^3, eta=K^-1.5` at `K=5,7,11` failed the finite premise `bDh<=1/2`; that run was correctly not accepted as a bound check. The displayed sequence satisfies the premise in every retained row. This records the failed check rather than discarding its reason.

```python
import numpy as np
for K in [5, 7, 9, 11]:
    n = K**5
    D = K*n
    eta = K**-2
    h = 2*eta/(n-1)
    a, b = .5, 1.
    m = K*np.arange(int(np.ceil(a*D/K)), int(np.floor(b*D/K))+1)
    F = K*K/D*(np.sin(np.pi*m*n*h)/np.sin(np.pi*m*h))**2
    bound = 1/(16*a*a*D*eta*eta)
    assert b*D*h <= .5
    assert F.max() <= bound
    print(K, D, F.max(), bound)
for K, n, eta in [(3,11,.005), (5,9,.008), (7,5,.002)]:
    D = K*n
    x = (np.arange(K)[:,None]/K-eta
         +2*eta*np.arange(n)/(n-1)).ravel()
    s = 1.
    z = 2*np.pi*(x[:,None]-x[None,:])
    P = np.sinh(2*s/D)/(2*np.sinh(s/D)**2+2*np.sin(z/2)**2)
    L = (P.sum()/D**2-1)/2
    J = max(1, int(np.ceil(2*D*eta)))
    pmin = np.sinh(2*s/D)/(2*np.sinh(s/D)**2+2*np.sin(np.pi/D)**2)
    assert L >= pmin/(2*K*J)-.5
    for m in range(1, 2*D+1):
        direct = np.exp(2j*np.pi*m*x).sum()
        exact = (0 if m%K else K*np.exp(-2j*np.pi*m*eta)
                 *np.exp(2j*np.pi*m*2*eta*np.arange(n)/(n-1)).sum())
        assert abs(direct-exact) < 1e-9
```

## 5. Literature check boundary

Checked 22 September 2026:

- Bourgade--Huang, *Loop Equations Characterize Random Matrix Statistics*, [arXiv:2607.07617v2](https://arxiv.org/abs/2607.07617v2), revised 9 September 2026. Authenticated authors/version/abstract from arXiv; the 147-page HTML fetch exceeded the tool limit. Theorem 1.9 was not independently re-extracted in this attempt, and no new conclusion here relies on it.
- Trunin--Huse, *Crystalline Spectral Form Factors*, [arXiv:2512.11054v3](https://arxiv.org/abs/2512.11054v3), revised 22 June 2026, PRL 136, 250405. Abstract-level adjacent result on strongly repulsive/crystalline spectra, not verified as the same clustered construction. No theorem is imported from it.

Queries included `quantum maps spectral statistics resolvent Heisenberg time rigorous BGS conjecture fixed map`, `unitary spectrum clustered eigenvalues Poisson kernel spectral form factor lower bound`, `clustered spectrum spectral form factor vanishing Heisenberg window Poisson kernel`, and `spectral form factor picket fence clusters Dirichlet kernel`. Search coverage was web/arXiv discovery, without a comprehensive citation graph or historical survey. Classification: (A)--(B) are elementary formal consequences of standard Poisson expansion and existing cluster bounds; (C)--(F) are an elementary explicit falsifier whose external priority is unassessed. No claim of Fields/Poincare-level progress is supported.
