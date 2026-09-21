# Exact Weyl path escape for the frozen raw-modular map

Date: 21 September 2026.

Status: recovered project proof from the 14--15 September BGS dossiers,
re-derived in the **raw modular Weyl convention of the actual frozen
operator** and given fresh finite/exact regressions. This is a structural
Heisenberg-time theorem, not a CUE form-factor theorem and not BGS.

## Exact Hilbert--Schmidt dynamics

For odd \(N\), retain exactly

\[
(T_N(a,b)\psi)(x)=e_N\!\left(b(x+2^{-1}a)\right)\psi(x+a),
\qquad U_N=e^{i\tau N A_N}M_N,\qquad \tau=10^{-80},
\]

with the frozen finite Fourier generator in
[the fixed-map frontier](fixed_map_resolvent_frontier.md). With normalized
Hilbert--Schmidt inner product and
\(\mathcal A_N=\operatorname{Ad}_{U_N}\),

\[
\boxed{\operatorname{Tr}_{HS}\mathcal A_N^m
      =|\operatorname{Tr}U_N^m|^2.} \tag{1}
\]

For \(r=(a,b)\), \(n=(c,d)\), put \(\sigma(r,n)=ad-bc\). The **raw** Weyl
product law is

\[
T_N(r)T_N(n)
=e_N(2^{-1}\sigma(r,n))T_N(r+n)
=(-1)^{\sigma(r,n)}e^{\pi i\sigma(r,n)/N}T_N(r+n), \tag{2}
\]

so

\[
[T_N(r),T_N(n)]
=2i(-1)^{\sigma(r,n)}
 \sin\!\frac{\pi\sigma(r,n)}N\,T_N(r+n). \tag{3}
\]

The sign in (3) is exactly the gauge correction absent from the old
ordinary-midpoint wording. All estimates below use absolute values, so it
does not change their constants.

Let \(a_r\) be the nonconstant raw Weyl coefficients of \(A_N\), before
modular aliasing, and define

\[
A_1=\sum_{r\ne0}|a_r|\|r\|_1,\qquad
R_0=\max_{a_r\ne0}\|r\|_1.
\]

Exact coefficient assembly gives

\[
\boxed{
A_1={2\sqrt{101}\over25}+{1307\over200}
=7.3389900496\ldots<8,\qquad R_0=9.} \tag{4}
\]

With \(L_N=i\tau N[A_N,\cdot]\),

\[
\mathcal A_N=e^{L_N}P_{S,N},\qquad P_{S,N}T_N(n)=T_N(Sn), \tag{5}
\]

and

\[
\sum_r |(L_N)_{n+r,n}|
\le a_0\|n\|_1,\qquad a_0=2\pi\tau A_1. \tag{6}
\]

This is exact finite-dimensional dynamics, with no Egorov remainder.

## One-kick Chernoff bound

Put

\[
E_N(v,u)=\langle T_N(v),e^{L_N}T_N(u)\rangle_{HS},
\qquad q_*=a_0R_0,
\]

and let \(d_N(v,u)\) be the minimum \(\ell^1\)-norm of an integer
representative of \(v-u\bmod N\). For every \(t>1\) with \(q_*t<1\),

\[
\boxed{
|E_N(v,u)|
\le t^{-d_N(v,u)/R_0}(1-q_*t)^{-\|u\|_1/R_0}.} \tag{7}
\]

Indeed, a length-\(k\) Dyson path has total absolute weight at most

\[
{q_*^k\over k!}(x)_k,\qquad x={\|u\|_1\over R_0},
\]

while a displacement \(d\) needs at least \(\lceil d/R_0\rceil\) microhops.
Summing with
\(\sum_{k\ge0}(x)_kz^k/k!=(1-z)^{-x}\) proves (7). Moreover

\[
\boxed{e^{L_N}T_N(0)=T_N(0).} \tag{8}
\]

## Hyperbolic forcing

Let

\[
S=\begin{pmatrix}3&4\\2&3\end{pmatrix},\qquad
\lambda=3+2\sqrt2.
\]

For every cyclic real sequence
\(n_{j+1}=Sn_j+h_j\),

\[
\boxed{
\sum_j\|n_j\|_1\le{\lambda\over2}\sum_j\|h_j\|_1.} \tag{9}
\]

This is the stable/unstable Green-function estimate in the eigenbasis
\((\sqrt2,1),(-\sqrt2,1)\). For an open segment,

\[
\boxed{
\sum_{j=1}^L\|n_j\|_1
\le{\lambda\over2}
\left(\sum_{j=1}^{L-1}\|n_{j+1}-Sn_j\|_1+
\|n_1\|_1+\|n_L\|_1\right).} \tag{10}
\]

## Exact near-sector anti-refocusing

Choose

\[
Q=5\cdot10^{-78},\qquad t=Q^{-1/2}.
\]

The actual frozen coefficients give

\[
q_*=4.1501011004\ldots\cdot10^{-78}<Q.
\]

Restrict a cyclic path to \(\|n_j\|_\infty\le N/32\). Then
\(h_j=n_{j+1}-Sn_j\) is the minimal modular lift. Combining (7), (9), and
\(\|Sn\|_1\le7\|n\|_1\) gives

\[
\prod_j|E_N(n_{j+1},Sn_j)|
\le e^{-\gamma\sum_j\|n_j\|_1}, \tag{11}
\]

where

\[
\gamma={1\over R_0}
\left({2\log t\over\lambda}+7\log(1-q_*t)\right)
=3.39318149\ldots>3.39. \tag{12}
\]

Thus

\[
Z_\gamma=
\sum_{n\in\mathbb Z^2\setminus\{0\}}e^{-\gamma\|n\|_1}
=\left({1+e^{-\gamma}\over1-e^{-\gamma}}\right)^2-1
=0.14391550\ldots<0.145. \tag{13}
\]

If one state on a cyclic path is zero, (8) forces the whole path to be the
identity path. Hence, if \(\mathcal T^{\rm near}_{N,m}\) is the exact
contribution of paths satisfying \(\|n_j\|_\infty\le N/32\),

\[
\boxed{
|\mathcal T^{\rm near}_{N,m}-1|
\le Z_\gamma^m<0.145^m} \tag{14}
\]

for every odd \(N\) and every \(m\ge1\).

## Long near runs and multiscale escape

For \(1\le R<N/32\), a nonzero near run
\(0<\|n_j\|_\infty\le R\), \(j=1,\ldots,L\), obeys

\[
\boxed{
\|\text{near-run kernel}\|_{\max}
\le e^{4AR}Z_\gamma^L,\qquad
A={\log t\over R_0}<9.89.} \tag{15}
\]

For \(L\ge25R\), the right side is at most \(e^{-8R}\). The
Hilbert--Schmidt dynamics has dimension \(D=N^2\), and all complementary
factors are unitary. A specified run therefore contributes at most
\(D^2e^{-8R}=N^4e^{-8R}\) to the trace. Union over start and run length
gives, for \(m\le\tau_1N\),

\[
\boxed{
|\mathcal T^{\rm long-run}_{N,m}|
\le\tau_1^2N^6e^{-8R}.} \tag{16}
\]

Take \(R=N^\epsilon\), \(0<\epsilon<1\), and
\(m\in[\tau_0N,\tau_1N]\). Removing the all-near nonidentity part and all
long near runs costs at most

\[
0.145^{\tau_0N}+\tau_1^2N^6e^{-8N^\epsilon}=o(1). \tag{17}
\]

Every remaining nonidentity path is separated by bulk states
\(\|n_j\|_\infty>N^\epsilon\) into near runs of length
\(<25N^\epsilon\). If there are \(K\) bulk visits,

\[
m\le K(25N^\epsilon+1),
\]

hence for large \(N\),

\[
\boxed{
K\ge{\tau_0\over26}N^{1-\epsilon}.} \tag{18}
\]

This is the recovered **Heisenberg-scale multiscale escape theorem** for the
actual raw frozen operator.

## All-characteristic encounter rank

Let \(A_m\) be the adjacency matrix of the cycle and \(P\) a permutation
matrix. Set

\[
B_P=P^TA_mP-A_m
\]

and let \(s(P)\) be the number of nonzero rows. The support graph of \(B_P\)
has maximum degree four; each nonzero row has degree two or four, so it has
at least \(s(P)\) edges.

A greedy induced matching discards at most 25 edges per chosen edge:
one selected edge, at most six other incident edges, and at most nine
second-neighborhood edges through each endpoint. Thus there is an induced
matching of size at least \(s(P)/25\). The corresponding minor of \(B_P\)
is diagonal with entries \(\pm1\), so it survives every characteristic.
Therefore

\[
\boxed{\operatorname{rank}_{\mathbb F}B_P\ge{s(P)\over25}}
\tag{19}
\]

for every field \(\mathbb F\).

Fresh regression is in
[bgs_heisenberg_path_audit.py](../computations/verification/bgs_heisenberg_path_audit.py).

## Boundary

This theorem deliberately stops before the missing cancellation theorem.
For \(m<N\), the CUE form-factor target is of order \(m\), while the adjoint
dynamics has an \(N\)-dimensional fixed commutant when the spectrum is
simple. The bulk sector must therefore produce a macroscopic **signed**
cancellation; it cannot simply be discarded by absolute values.

In particular, (14)--(19) do not prove that a historical object called the
“CUE contraction sector” contributes \(\min(m,N)\). The 15 September audit
found that this deterministic main term had been asserted, not derived, in
v7--v9. What is proved here is narrower but genuine: nontrivial
Heisenberg paths cannot remain almost entirely in small Weyl modes, and
extensive encounter support forces extensive modular rank.
