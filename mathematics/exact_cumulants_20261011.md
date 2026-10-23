# Exact fourth cumulants and a sharper all-time comparison

**Stable claim:** BGS-TRACE-069. **State:** PROVED.
**Boundary:** Growing n/N->1, d=o(N), logarithmic critical variance, every fixed cumulant and mixed moment, conditional Gaussian law. Second/fourth cumulants are prior HSW formulas; no independent-block interpretation or external novelty certificate.
**Integration and review:** [11 October disposition](../archive/record/chat_integration_20261011.md).
**Original input:** [dated source](../archive/evidence/executions/20261011/chat-research/original/jack_phase_2026_10_11/exact_cumulants.md).


Conventions are those of `phase_contraction_20261011.md`: N is the number of distinct
eigenvalues, with half the matrix trace in CSE. Define

\[
H_r(m)=\sum_{j=0}^{m-1}(j+\tfrac12)^{-r},\qquad H_r(0)=0.
\]

The exact ensemble formulas below are already known. In particular,
Haake–Sommers–Weber, arXiv:chao-dyn/9906024 (14 June 1999), equations
(14), (21) and (22), give the CUE variance and the CSE second and connected
fourth moments. Here they are independently rederived from finite matrices
to check normalizations and supply explicit conditional phase estimates.
Their rederivation is not a claim of scientific novelty.

## CSE: grouping the finite trace-log

Use the weighted shifts B_s and the Pfaffian generating function established
in `heisenberg_form_factor_20261011.md`. Put

\[
\begin{aligned}
T_1&=\operatorname{Tr} B_nB_{-n},&
T_2&=\operatorname{Tr} B_{2n}B_{-2n},\\
T_3&=\operatorname{Tr} B_n^2B_{-2n},&
T_{4b}&=\operatorname{Tr} B_n^2B_{-n}^2,\\
T_{4a}&=\operatorname{Tr}(B_nB_{-n})^2.
\end{aligned}
\]

Reflection identifies the companion term to T_3. Sorting compositions in
the coefficient of u²v² by their length, including the factor 2!2!, gives:

| Length | Contribution |
|---|---|
| 1 | N |
| 2 | −2N−2T₁−T₂/2 |
| 3 | 4T₁+2T₃ |
| 4 | −T₄a−2T₄b |

Consequently

\[
\kappa_{2,2}=-N+2T_1-\tfrac12T_2+2T_3-2T_{4b}-T_{4a}.
\tag{1}
\]

For R₁={k∈H_N:k−n∈H_N} and R₂={k∈H_N:k−2n∈H_N}, the
five summands before summing over k are respectively

\[
\begin{aligned}
T_1:&\quad 1+\frac{n^2}{4k(k-n)},\\
T_2:&\quad 1+\frac{n^2}{k(k-2n)},\\
T_3:&\quad 1+\frac{3n^2}{4k(k-2n)},\\
T_{4b}:&\quad 1+\frac{9n^2}{16k(k-2n)}
                  -\frac{n^2}{16(k-n)^2},\\
T_{4a}:&\quad 1+\frac{3n^2}{8k(k-n)}
                  +\frac{n^2}{16}\left(\frac1{k^2}+\frac1{(k-n)^2}\right).
\end{aligned}
\tag{2}
\]

The first and last sums use R₁; the other three use R₂. The intermediate
point k−n is automatically in H_N when k and k−2n are in H_N.
Thus no endpoint restriction is lost.

For n<N abbreviate

\[
a=H_1(N)-H_1(N-n),\quad b=H_1(N)-H_1(|N-2n|),
\quad f=H_2(N),\quad g=H_2(N-n).
\]

Partial fractions in (2) and reflection of each active interval give

\[
\begin{aligned}
T_1&=2N-n-na/2,\\
T_2&=2N-2n-nb,\\
T_3&=2N-2n-3nb/4,\\
T_{4b}&=2N-2n-9nb/16-n^2g/8,\\
T_{4a}&=2N-n-3na/4+n^2(f+g)/8.
\end{aligned}
\]

For N≤n≤2N, R₂ is empty, and the sum of inverse squares over R₁ is
2[H₂(N)−H₂(n−N)]. Substituting both ranges into (1) proves

\[
\boxed{
\kappa_{2,2}=
\begin{cases}
\dfrac n8\bigl[2H_1(N-n)-H_1(N)-H_1(|N-2n|)\bigr]
-\dfrac{n^2}8\bigl[H_2(N)-H_2(N-n)\bigr],&1\le n<N,\\[3pt]
N-n-\dfrac n4\bigl[H_1(N)-H_1(n-N)\bigr]
-\dfrac{n^2}8\bigl[H_2(N)-H_2(n-N)\bigr],&N\le n\le2N,\\[3pt]
-N,&n\ge2N.
\end{cases}}
\tag{3}
\]

The first formula also continues correctly to n=N. The plateau starts
already at n=2N−1, where the middle formula equals −N.
In particular

\[
\kappa_{2,2}(N,N)=-\frac N4H_1(N)-\frac{N^2}8H_2(N).
\tag{4}
\]

## A uniform conditional bound without a large artificial constant

When n<N, a and f−g are nonnegative, and 0≤b≤H₁(N). Therefore
κ₂₂≤nH₁(N)/8. When n≥N, the middle formula is nonpositive, as is the
plateau. Consequently κ₂₂≤NH₁(N)/8 for every positive time.

The exact second moment is

\[
m_2=\frac n2+\frac n4[H_1(N)-H_1(|N-n|)]\quad(1\le n\le2N),
\qquad m_2=N\quad(n\ge2N).
\tag{5}
\]

Since H₁(N)≤2+log(2N−1), equation (5) implies

\[
m_2\le N\left[2+\tfrac12\log(2N-1)\right].
\]

Rotation invariance gives E p_n²=0. Hence
Var|p_n|²=m₂²+κ₂₂, and the sharp phase contraction yields

\[
\boxed{
\sup_{n\ge1}\mathbb E_Q|K_{N,Q}(n)-\overline K_{4,N}(n)|^2
\le
\frac{[2+\frac12\log(2N-1)]^2+[2+\log(2N-1)]/(8N)}{N+\frac12}.}
\tag{6}
\]

This replaces the deliberately coarse closed-walk constant in the earlier
proof. It controls every deterministic positive-time sequence. The
supremum here is outside the expectation; no maximum over all times for a
single Q is asserted. For a finite set of M_N times, a union bound gives
convergence of their maximum error in probability if
M_N log²N/N→0.

## CUE: a finite Toeplitz proof and its exact variance

Expanding the ordinary Vandermonde determinants and integrating their
columns gives

\[
Z(u,v)=\det\left(I+\sum_{a+b\ge1}
\frac{u^av^b}{a!b!}J_{(a-b)n}\right),
\]

where J_s is the unweighted shift on {0,…,N−1}. Thus its trace-log is the
same calculation with coefficient 1 instead of 1/2. Grouping its words
gives

\[
\kappa_{2,2}=-N+4T_1-T_2+4T_3-4T_{4b}-2T_{4a}.
\]

For these unweighted shifts, T₁=T₄a=(N−n)₊ and
T₂=T₃=T₄b=(N−2n)₊. Therefore

\[
m_2=\min(n,N),\qquad
\kappa_{2,2}=-N+2(N-n)_+-(N-2n)_+.
\]

Equivalently

\[
\operatorname{Var}|p_n|^2=
\begin{cases}
n^2,&n\le N/2,\\
n^2-2n+N,&N/2\le n\le N,\\
N^2-N,&n\ge N.
\end{cases}
\tag{7}
\]

The adjacent formulas agree at endpoints. Each is at most N²−N for N≥2,
so the improved all-time phase comparison is

\[
\boxed{\sup_{n\ge1}\mathbb E_Q|K_{N,Q}(n)-\overline K_{2,N}(n)|^2
\le\frac{1-1/N}{N+1}.}
\tag{8}
\]

These CUE and CSE ensemble identities are established literature results;
their use in the conditional phase theorem has a different averaging
variable from the time averaging studied in the 1999 paper.
