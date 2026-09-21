# Absolute envelope for unitary encounter coefficients

Date: 21 September 2026.

Status: exact combinatorial theorem for the standard unitary encounter
coefficients of Müller--Heusler--Braun--Haake--Altland, plus their published
order-by-order unitary cancellation. It concerns the universal formal
encounter main terms. It does not prove that the frozen quantum map admits a
uniform all-order encounter localization or domination.

For an encounter vector

\[
\mathbf v=(v_2,v_3,\ldots),
\qquad
L=\sum_{\ell\ge2}\ell v_\ell,\qquad
V=\sum_{\ell\ge2}v_\ell,
\]

put

\[
\nu(\mathbf v)=L-V+1=n.
\]

The standard unitary coefficient is

\[
\widetilde N(\mathbf v)
=
N(\mathbf v)
{(-1)^V\prod_{\ell\ge2}\ell^{v_\ell}\over L}.
\tag{1}
\]

This is equation (30) in
[Müller et al., arXiv:nlin/0503052](https://arxiv.org/abs/nlin/0503052).
Their unitary recursion yields, for every \(n\ge2\),

\[
\boxed{
\sum_{\nu(\mathbf v)=n}\widetilde N(\mathbf v)=0.}
\tag{2}
\]

## Absolute coefficient theorem

The set counted by \(N(\mathbf v)\) is a subset of all permutations of
\(\{1,\ldots,L\}\) with exactly \(v_\ell\) cycles of length \(\ell\).
Therefore

\[
N(\mathbf v)
\le {L!\over\prod_{\ell\ge2}\ell^{v_\ell}v_\ell!},
\]

and hence

\[
\boxed{
|\widetilde N(\mathbf v)|
\le{(L-1)!\over\prod_{\ell\ge2}v_\ell!}.}
\tag{3}
\]

Define

\[
A_n^{\rm abs}
=
{1\over(n-2)!}
\sum_{\nu(\mathbf v)=n}|\widetilde N(\mathbf v)|.
\tag{4}
\]

Set \(k=n-1=L-V\). For fixed \(V\), writing \(r=\ell-1\),

\[
\sum_{\substack{\sum_r rv_{r+1}=k\\
                 \sum_r v_{r+1}=V}}
{1\over\prod_r v_{r+1}!}
=
{1\over V!}\binom{k-1}{V-1}.
\tag{5}
\]

Because \(L=k+V\), equations (3)--(5) give

\[
A_n^{\rm abs}
\le
\sum_{V=1}^k
\binom{k+V-1}{V}
\binom{k-1}{V-1}.
\]

Using \(V\le k\), then Vandermonde,

\[
\boxed{
A_n^{\rm abs}
\le
\binom{3k-2}{k}
\le
\left({27\over4}\right)^k.}
\tag{6}
\]

The last inequality follows from

\[
1\ge
\binom{3k}{k}
(1/3)^k(2/3)^{2k}.
\]

Thus the universal unitary encounter coefficients have a positive absolute
radius of convergence.

## Consequence for a small time window

Let \(0<\sigma<4/27\), \(w\in C_c^\infty((0,\sigma))\), and
\(q=27\sigma/4<1\). Then the absolute main-term tail satisfies

\[
\sum_{n>R}
A_n^{\rm abs}
\left|\int_0^\sigma w(\tau)\tau^n\,d\tau\right|
\le
\boxed{
\|w\|_\infty
{\sigma^2 q^R\over1-q}.}
\tag{7}
\]

Consequently the universal main encounter series is absolutely convergent
on every compact subinterval of \(0<\tau<4/27\). Combining this with the
published cancellation (2), the **pure universal main-term** correction is
zero after all orders are summed; there is no interchange-of-orders
ambiguity at this combinatorial level.

A convenient safe window is \(\sigma=1/10\), for which \(q=27/40\).

## What remains open

Equation (7) does not dominate the actual frozen-map quantum contribution.
To use it, one still needs a uniform quantum envelope of the form

\[
\mathfrak E_{N,n}(w)
\le
C_w C_0^{n-1}
A_n^{\rm abs}\sigma^{n+1}
\]

for the complete-matching sector, together with a non-overcounting
microlocal identification of genuine partner tubes. The exact
fixed-complexity reconnection tensor provides the correct long-link power,
but does not by itself supply this all-order envelope.

The genuinely unmatched/post-cyclic sector is separate.

Finite regression of (5)--(6) is in
[unitary_encounter_envelope_audit.py](../computations/verification/unitary_encounter_envelope_audit.py).
