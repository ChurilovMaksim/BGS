# Independent audit of Theorem 89.1 and equation (89.2)

**Verdict:** The bound in (89.1) is valid. The published proof structure is terse, but its endpoint argument and its two separate repeated-occupation corrections can be made rigorous without a reverse-kernel hypothesis, diagonal-mark restriction, or stronger entry flatness. Equation (89.2) follows. These assertions are finite-degree random-phase statements; they do not identify a microscopic scalar cavity law or prove deterministic BGS.

## Exact expansion and unrestricted pairings

Write `Z = S X S*`, and test against an arbitrary complex matrix `Y` using the ordinary Frobenius inner product. A path is `a=(a_1,...,a_n)`; its amplitude is

\[
u(a)=\prod_{r=1}^{n-1}S_{a_{r+1},a_r}.
\]

The phase average retains exactly pairs of paths `a,b` having equal occupation multisets. Thus

\[
\langle Y,T_nX\rangle=
\sum_{\operatorname{occ}(a)=\operatorname{occ}(b)}
\overline{Y_{a_n b_n}}Z_{a_1 b_1}u(a)\overline{u(b)}.
\]

For a permutation `sigma` of the `n` formal times put `b_r=a_{sigma(r)}` and denote the resulting **unrestricted** sum over `a` by `Q_sigma(Y,Z)`. All initial and final marks remain arbitrary complex matrices.

Weighted Cauchy--Schwarz gives

\[
|Q_\sigma|\le
\bigg[\sum_a\prod_{r<n}P_{a_{r+1},a_r}|Y_{a_n,a_{\sigma(n)}}|^2\bigg]^{1/2}
\bigg[\sum_a\prod_{r<n}P_{a_{\sigma(r+1)},a_{\sigma(r)}}|Z_{a_1,a_{\sigma(1)}}|^2\bigg]^{1/2}.
\]

A bistochastic Markov path with counting-measure initial distribution has every one-time marginal equal to counting measure and every two-time marginal at distinct formal times equal to a positive power of `P` (or its transpose). Every entry of every positive power is at most `delta`: by induction a stochastic row makes each new entry a convex combination of entries already at most `delta`.

Consequently, the first bracket is at most `delta ||Y||_F^2` when `sigma(n) != n` and at most `||Y||_F^2` otherwise. The second bracket is at most `delta ||Z||_F^2` when `sigma(1) != 1` and at most `||Z||_F^2` otherwise. A pairing with at least one moved endpoint therefore costs at most `sqrt(delta)||Y||_F||Z||_F`; with both moved it costs at most `delta ||Y||_F||Z||_F`.

If both endpoints are fixed, the unrestricted summation over `a_n` and `a_1` is exact and reduces the length by two, with

\[
Y_{\rm new}=S^*\Pi(Y)S,\qquad Z_{\rm new}=S\Pi(Z)S^*.
\]

Both maps contract Frobenius norm. The interior permutation remains nonidentity when the original permutation was nonidentity. Repeated removal must reach a moved endpoint. Hence every nonidentity unrestricted pairing satisfies the `sqrt(delta)` bound, with no dimension factor. For the identity pairing, exact summation is `A^n`.

## Collision bounds and multiplicity correction

For any fixed distinct formal times `i,j`, insert `1_{a_i=a_j}` in a pairing. The same Cauchy split applies. A two-time endpoint mark already has a `delta` bound, and dropping the collision restriction preserves it. A one-time endpoint mark is at the terminal endpoint for `Y`, and at the initial endpoint of the reordered negative chain for `Z`.

Conditioned on an initial endpoint `e`, the collision probability for times `i<j` is

\[
\sum_c (P^{i-1})_{ce}(P^{j-i})_{cc}\le\delta.
\]

For a terminal endpoint use the reversed bistochastic chain with kernel `P^T`. Thus each bracket is at most `delta` times the squared Frobenius norm of its mark, regardless of whether that mark has one or two formal-time arguments. Every prescribed collision contributes at most `delta ||Y||_F||Z||_F`. The estimate still holds if one restricts the summation further to any subset of paths: after Cauchy the nonnegative sums are enlarged to the full collision event.

Separate the true occupation-matched sum into distinct-label and repeated-label parts. Distinct paths have a unique pairing. For the true repeated part, assign each pair one canonical matching permutation; this partitions it into at most `n!` restricted pairing sums. Use a fixed-order partition according to the first colliding pair to avoid counting a signed sum twice. This bounds the true repeated part by `n! binom(n,2) delta ||Y||_F||Z||_F`.

Independently, the repeated part of the unrestricted permutation sum has the same bound, again by partitioning paths according to their first collision. Subtracting these two **separate** repeated parts gives `n! n(n-1) delta`. Adding the `n!-1` nonidentity unrestricted pairings establishes the slightly stronger bound

\[
\|T_n-A^n\|\le(n!-1)\sqrt\delta+n!n(n-1)\delta,
\]

which implies the stated (89.1). Degree one is exact.

At degree two an exact refinement is available:

\[
(T_2-A^2)X\big|_{ij}=\begin{cases}
S_{ij}\overline{S_{ji}}(SXS^*)_{ji},&i\ne j,\\0,&i=j.
\end{cases}
\]

Therefore its induced Frobenius norm is exactly `max_{i != j}|S_ij S_ji| <= delta`.

## Positive Fejer majorant

For fixed `V`, define

\[
F_L(V)=\frac1L\sum_{|n|<L}(1-|n|/L)\operatorname{Ad}(V)^n.
\]

This is a positive self-adjoint operator on Frobenius space: on an eigenmatrix its multiplier is `|sum_{r=0}^{L-1} exp(i r theta)|^2/L^2 >= 0`, equal to one for `theta=0`. Hence the full eigenspace pinching satisfies `0 <= E_V <= F_L(V)` even with eigenvalue degeneracy. All these maps preserve traceless matrices.

On traceless matrices, `||A^n|| <= rho^(n-1)` for `n >= 1`, because `A` is contractive and its image is diagonal, after which each iteration is `P-J`. Negative powers of `Ad(V)` are adjoints, so phase averaging gives `T_{-n}=T_n*`. Summing positive and negative Fejer terms and using (89.1) yields exactly (89.2), with the omitted Fejer weights only enlarging the error term.

For each fixed `L`, the error tends to zero with `delta`. Then `L` tends to infinity. This proves vanishing norm of `E_D E_{DS}` on traceless matrices. It does **not** prove vanishing of `E_D ||E_{DS}||`: each sample pinching normally has norm one on a nonzero traceless commutant. In particular, a phase-independent traceless mark `B` satisfies

\[
\mathbb E_D\|E_{DS}B\|_F^2\le\|\mathbb E_D E_{DS}\|\,\|B\|_F^2.
\]

## Real-flow and microscopic-source scope

For `V(x)=S exp(i x H/m)`, positivity of `H` is not needed for the following norm estimate, but is part of the source theorem's hypotheses:

\[
\|V(x)-S\|_{\rm op}\le\|V(x)-S\|_F
\le |x|\sqrt{\operatorname{Tr}H^2}/m\le R\sqrt{C_H/m}.
\]

Thus `max |V(x)_ij|^2 <= 2 delta + 2 R^2 C_H/m`, uniformly for bounded real `x`. The intensity gap also persists: `P(V)-P(S)=Pi[Ad(V)-Ad(S)]Pi` on diagonal Frobenius space has norm at most `2 ||V-S||_op`, so its gap is `rho+o(1)`. The averaged-pinching conclusion therefore extends uniformly along each bounded real flow (first choose `L`, then the dimension).

This verifies the new input needed to relax the entry hypothesis of an already independently established finite-twirl/continuation/differentiation source-comparison theorem. It is **not**, alone, a proof of that source theorem: the microscopic resolvent has radius approaching one and demands its separate absorbed covariance and analytic-continuation controls. This audit has not re-audited those controls. Conditional on the reviewed source theorem described in Section 88.1, the weakened max-entry hypothesis is supported. The resulting comparison still compares the physical model to its own scalar cavity ensemble; there is no Haar/CUE identification, absorption removal, Heisenberg-time estimate, deterministic phase theorem, or BGS implication.

## Explicit delta-only rate

Set `X=log(1/delta)` and, for sufficiently large `X`, take `L=floor[X/(8 log X)] >= 2`. For `n<L`,

\[
\log(n!)\le n\log n\le L\log X\le X/8.
\]

The sum in (89.2) is therefore at most

\[
2e^{-3X/8}+2L^2e^{-7X/8}.
\]

Together with its first term this gives the rigorous rate

\[
\|\mathbb E_D E_{DS}\|_{\mathrm{traceless}\to\mathrm{traceless}}
=O_\rho\!\left(\frac{\log X}{X}\right)
=O_\rho\!\left(\frac{\log\log(1/\delta)}{\log(1/\delta)}\right).
\]

There is no unidentified asymptotic input here. Since unitarity forces `delta >= 1/m`, the bounded real flow satisfies `delta_x <= (2+2R^2 C_H)delta`. Its gap remains bounded away from one, so the same rate holds uniformly in `|x|<=R`, with constants depending on `rho,R,C_H`. An explicit rate for the full absorbed microscopic source comparison would still require quantitative versions of its separate finite-twirl/continuation/differentiation estimates.

Operator norm does not automatically control the superoperator trace at microscopic scale: on full matrix space the crude trace bound has dimension factor `m^2`, while `Tr_super T_n=E|Tr(DS)^n|^2`. The pinching estimate and its rate therefore do not supply the missing spectral form factor or microscopic scalar-cavity identification.
