# Exact quantum histories and fixed-complexity reconnection tensors

Date: 21 September 2026.

Status: exact finite-dimensional identities recovered from the 16 September
working state and independently replayed. The flat-link corollary uses the
repaired one-step unistochastic gap. No semiclassical identification of all
partner tubes is assumed. These results do not prove the post-cyclic residual
small or establish BGS.

## 1. Exact open-history probability

Let \(\mathcal K\) have dimension \(D\), let
\(\mathcal V:\mathcal K\to\mathcal K\) be unitary, and let
\(\{\Pi_a\}\) be a finite orthogonal resolution of the identity. For a history
\(\boldsymbol a=(a_0,\ldots,a_M)\), define

\[
H_{\boldsymbol a}
=
\Pi_{a_M}\mathcal V\Pi_{a_{M-1}}\mathcal V\cdots
\Pi_{a_1}\mathcal V\Pi_{a_0}.
\]

Successive Hilbert--Schmidt Pythagoras and unitary invariance give

\[
\boxed{
\sum_{\boldsymbol a}\|H_{\boldsymbol a}\|_{\rm HS}^2=D.}
\tag{1}
\]

Thus

\[
\boxed{
\mathbb P(\boldsymbol a)=D^{-1}\|H_{\boldsymbol a}\|_{\rm HS}^2}
\tag{2}
\]

is an exact probability distribution at every history depth, with exact
prefix/descendant consistency.

For the frozen map take
\(\mathcal K_N=\operatorname{End}(\mathcal H_N)\),
\(D=N^2\), and \(\mathcal V=\operatorname{Ad}_{U_N^\ell}\).
If \(P_C\) are orthogonal position-cell projectors, then

\[
\Pi_{CD}(X)=P_DXP_C
\]

is an orthogonal resolution on Liouville space. Hence (2) gives an exact
positive coarse pair-history measure for the actual deterministic quantum
dynamics, without a semiclassical approximation.

## 2. Smooth Parseval histories

Orthogonality is not needed. Let \(\{\mathcal M_a\}\) be finite operators on
\(\mathcal K\) satisfying

\[
\sum_a\mathcal M_a^*\mathcal M_a=I.
\tag{3}
\]

Define

\[
H_{\boldsymbol a}
=
\mathcal M_{a_M}\mathcal V
\mathcal M_{a_{M-1}}\mathcal V\cdots\mathcal M_{a_0}.
\]

Then the same recursion gives exactly

\[
\boxed{
\sum_{\boldsymbol a}\|H_{\boldsymbol a}\|_{\rm HS}^2=D.}
\tag{4}
\]

For real multiplication cutoffs \(\chi_C\) on \(\mathcal H_N\) with

\[
\sum_C\chi_C^2=I,
\]

the Liouville operators

\[
\mathcal M_{CD}(X)=\chi_DX\chi_C
\]

satisfy (3) exactly. Smooth overlapping cells therefore incur no
combinatorial overlap loss in the total Hilbert--Schmidt history mass.

## 3. Two-sided Hilbert--Schmidt gluing

For arbitrary operator families \(A_i,B_i\) on a \(D\)-dimensional Hilbert
space,

\[
\boxed{
{1\over D}\sum_i|\operatorname{Tr}(A_iB_i)|
\le
\left({1\over D}\sum_i\|A_i\|_{\rm HS}^2\right)^{1/2}
\left({1\over D}\sum_i\|B_i\|_{\rm HS}^2\right)^{1/2}.}
\tag{5}
\]

Thus if disjoint first-witness prefixes satisfy total squared mass at most
\(D\), while their coherent descendant sums satisfy total squared mass at
most \(\eta_N^2D\), then the complete normalized glued contribution is at
most \(\eta_N\). There is no factor equal to the number of possible witness
locations.

This is an exact bookkeeping theorem. The missing model-specific statement
is to prove such an \(\eta_N=o(1)\) descendant contraction for the actual
first unmatched block.

## 4. Exact segment-reconnection tensor

Let \(V\in U(N)\), \(P(x,y)=|V_{xy}|^2\), and cut a closed path into
\(L\ge2\) oriented segments. Let \(a_i,b_i\) be the initial/final vertices
of segment \(i\), and let \(r_i\ge0\) be its number of internal one-step
edges. The original boundary reconnection is
\(c(i)=i+1\pmod L\). For a permutation \(\pi\in S_L\), form a partner by
keeping all internal segment vertices and orientations unchanged and
replacing only the boundary edges by \(b_i\to a_{\pi(i)}\).

Summing the squared internal segment amplitudes gives
\((P^{r_i})_{b_i a_i}\). Therefore the complete pair sum is exactly

\[
\boxed{
Z_{V,\pi}(\mathbf r)
=
\sum_{\mathbf a,\mathbf b}
\prod_{i=1}^L
(P^{r_i})_{b_i a_i}
V_{a_{c(i)},b_i}
\overline{V_{a_{\pi(i)},b_i}}.}
\tag{6}
\]

All long-segment phases have cancelled algebraically. No stationary phase,
shadowing theorem, or classical averaging is used in (6).

## 5. Uniform majorant and flat-link limit

Assume

\[
\max_{x,y}|V_{xy}|^2\le {C_0\over N}.
\tag{7}
\]

Because every \(P^r\) is stochastic,

\[
\boxed{|Z_{V,\pi}(\mathbf r)|\le C_0^L.}
\tag{8}
\]

Now assume also \(s_2(P)\le\rho<1\), put \(J_{xy}=1/N\), and let
\(T=\min_i r_i\). Then

\[
\|P^{r_i}-J\|_{2\to2}\le\rho^{r_i},
\qquad
\sum_{a,b}|(P^{r_i}-J)_{ba}|
\le N^{3/2}\rho^T.
\]

Expanding \(P^{r_i}=J+(P^{r_i}-J)\) in (6) yields

\[
\boxed{
|Z_{V,\pi}(\mathbf r)-Z^{(0)}_{V,\pi}|
\le
C_0^L\left[(1+N^{1/2}\rho^T)^L-1\right].}
\tag{9}
\]

For the all-flat term, row unitarity gives

\[
\sum_b V_{a,b}\overline{V_{a',b}}=\delta_{a,a'}.
\]

If \(V_\pi=\#\operatorname{cyc}(c^{-1}\pi)\), then

\[
\boxed{
Z^{(0)}_{V,\pi}=N^{V_\pi-L}.}
\tag{10}
\]

When the reconnection has encounter order
\(n=L-V_\pi+1\), this is exactly

\[
\boxed{Z^{(0)}_{V,\pi}=N^{-(n-1)}.}
\tag{11}
\]

For the spectrally conjugate frozen family, the repaired one-step theorem
gives eventual \(s_2(P)<7/8\) and fixed-time FIO gives (7). Hence for every
**fixed** \(L\), taking \(T=C\log N\) with sufficiently large fixed \(C\)
makes (9) \(O_{L,A}(N^{-A})\) for any prescribed \(A\).

This is an exact-quantum derivation of the universal long-link power for
literal segment reconnections.

## 6. Scope boundary

A genuine semiclassical partner can shadow the same classical link without
using the identical discrete position path. Equation (6) must therefore not
be silently promoted to a theorem for every partner tube. Nor does the
fixed-\(L\) result sum the high-complexity \(L\to\infty\) tail.

What is now exact is:

1. positive history normalization at arbitrary depth;
2. no witness-location entropy under an \(L^2\) descendant contraction;
3. exact long-link cancellation for literal fixed-complexity reconnections;
4. the flat universal power \(N^{-(L-V_\pi)}\) once links are logarithmically
   longer than the one-step mixing scale.

The remaining complete-match problem is the non-overcounting
microlocal/partner localization for genuine shadowing tubes and the
high-complexity tail. The genuinely unmatched sector remains a separate
signed cancellation problem.

Fresh finite regression is in
[quantum_history_reconnection_audit.py](../computations/verification/quantum_history_reconnection_audit.py).
