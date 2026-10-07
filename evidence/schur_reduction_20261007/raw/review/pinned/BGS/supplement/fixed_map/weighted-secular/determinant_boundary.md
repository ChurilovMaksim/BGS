# What the determinant route must control

20 September 2026. Base `e0ada2e2c44dfe10bebf928dc8a1d6526ae15cb7`.
Parent: `secular-route-20260920-direct-fixed-coupling-attempt`.
Self-reviewed derivations and reproducible checks; no novelty, independent
referee, formal-certification, or BGS claim. The fixed-map estimate remains
unproved. This note prevents accepting an insufficient determinant target.

## 1. Exact counterexample to a second-moment closure

For N>=2 put

\[
 V_N=\operatorname{diag}(e^{2\pi i j/(N+1)}:1\le j\le N),
 \qquad V_{N,\alpha}=e^{i\alpha}V_N.
\]

These are the (N+1)-st roots with the root 1 deleted, followed by a
common rotation. All eigenvalues are simple. Exactly

\[
 P_\alpha(z)=\det(I-zV_{N,\alpha})
       =\sum_{k=0}^N z^k e^{ik\alpha}.
\tag{1}
\]

Consequently, uniform integration over the single angle alpha gives

\[
 \frac1{2\pi}\int P_\alpha(z)\overline{P_\alpha(w)}\,d\alpha
       =\sum_{k=0}^N(z\bar w)^k.
\tag{2}
\]

This is exactly the finite CUE characteristic-polynomial second moment,
for every z,w, not just a fixed number of low coefficients. To see the
CUE identity, the coefficient of degree k is (-1)^k times the Schur
character of the column partition (1^k). Distinct Schur characters are
orthonormal in the CUE eigenangle measure. The orthogonality also follows
directly: multiply the Weyl alternant formula for each character by
the Vandermonde in the CUE density, expand the two determinants, and
integrate their integer Fourier monomials. Only equal partitions survive,
with normalization N! cancelled by the density's factor 1/N!.

But the actual power sums of (1) are

\[
 p_m=e^{im\alpha}\bigl((N+1)\mathbf1_{N+1\mid m}-1\bigr).
\tag{3}
\]

For a nonnegative nonzero smooth w supported in (-1,1), therefore,

\[
 \frac1{N^2}\sum_{m\ne0}w(m/N)
       (|p_m|^2-\min(|m|,N))
 \longrightarrow-\int_{-1}^1 |t|w(t)\,dt<0.
\tag{4}
\]

The O(N) summands equal w(m/N)(1-|m|); the claim is a Riemann sum.
The strict inequality holds for every such nonzero nonnegative smooth w.
These spectra also have uniform macroscopic density and bounded local
occupation moments of every fixed order: their unfolded gaps are N/(N+1)
except for one doubled gap. Thus neither simplicity nor those elementary
local bounds rescue the proposed implication.

**Scope.** The common rotation does not change any spectral differences.
This is an abstract counterexample to inferring pair statistics from
characteristic-polynomial covariance. It is NOT a realization by the
prescribed nonlinear Anosov map and is NOT a counterexample to its BGS
conjecture. No priority is claimed for this elementary construction.

## 2. The missing observable: a ratio of determinants

For a single unitary U, |a|,|b|<1, define the exact transform

\[
 Z_U(a,b;c,d)=\frac1{2\pi}\int_0^{2\pi}
 \frac{\det(I-ce^{i\theta}U)\det(I-de^{-i\theta}U^*)}
      {\det(I-ae^{i\theta}U)\det(I-be^{-i\theta}U^*)}\,d\theta.
\tag{5}
\]

There is no averaging over the kick, over independent eigenphases, or
over different maps in this definition. The common-angle integral is
an exact transform of the one prescribed spectrum.

Differentiate in the numerator parameters, then set c=a,d=b. The two
minus signs cancel; expand the resolvents in absolutely convergent
geometric series and integrate theta. This proves

\[
 \left.\partial_c\partial_d Z_U\right|_{c=a,d=b}
       =\sum_{m\ge1}(ab)^{m-1}|\operatorname{Tr}U^m|^2.
\tag{6}
\]

For Haar CUE one has the exact, known reference formula

\[
 \mathbb E Z_U(a,b;c,d)
  =1+\frac{(a-c)(b-d)}{1-ab}\sum_{q=0}^{N-1}(cd)^q.
\tag{7}
\]

Here is a derivation fixing the conventions. The hook expansion is

\[
 \frac{\det(I-cU)}{\det(I-aU)}
 =1+(a-c)\sum_{p\ge1}\sum_{q=0}^{N-1}
     a^{p-1}(-c)^q s_{(p,1^q)}(U).
\tag{8}
\]

It follows by multiplying the complete and elementary symmetric-function
generating series and using
h_p e_q=s_(p,1^q)+s_(p+1,1^(q-1)), with the q=0 boundary handled
by h_p=s_(p). Interior terms telescope. For fixed N and |a|<1,
the character series converges absolutely on the unitary group: each
hook character is bounded by its dimension, which grows polynomially
in p. Apply the same expansion to U* with b,d and the orthogonality
proved above. Only identical hooks remain; their sums are the geometric
series in (7). This also shows why a covariance of determinants alone
misses the denominator contributions.

General ratio formulas are established literature, for example
[Conrey--Farmer--Zirnbauer](https://arxiv.org/pdf/math-ph/0511024v2).
Equations (6)--(8) are reconstructed here, not claimed as new results.

Put r=exp(-s/N), s>0, and

\[
 \mathcal Z_N(s;u,v)=Z_{U_N}(r,r;r+u/N,r+v/N),
 \qquad L_N(s)=\frac1{N^2}\sum_{m\ge1}e^{-2sm/N}
                     |\operatorname{Tr}U_N^m|^2.
\]

Then exactly L_N(s)=r^2 partial_u partial_v Zcal_N(s;0,0).
Equation (7) has the locally uniform microscopic limit

\[
 \mathcal Z_{\rm CUE}(s;u,v)
 =1+uv\,\frac{1-e^{-(2s-u-v)}}{2s(2s-u-v)},
\tag{9}
\]

where the apparent singularity is removable. In particular the required
Abel limit is

\[
 L_N(s)\longrightarrow L_{\rm CUE}(s)
       =\frac{1-e^{-2s}}{4s^2}
       =\int_0^\infty e^{-2st}\min(t,1)\,dt.
\tag{10}
\]

Local uniform convergence to (9) on any fixed complex bidisc around
(0,0) would imply (10) by Cauchy's formula. If its sup error on the
boundary torus of radius rho is delta_N, the error in (10) is at most
r^2 delta_N/rho^2+|1-r^2| L_CUE(s). This is a sufficient hypothesis,
not an estimate proved for the frozen map.

## 3. Abel convergence is sufficient, and is not a weaker endpoint

For arbitrary unitary sequences, (10) for every s>0 is equivalent to the
maintained compactly supported weighted pair comparison. In fact, for
sufficiency it is enough to establish (10) on s=s0+n/2, n=0,1,...,
for one fixed s0>0. The following proof uses positivity, not a Tauberian
assumption about unknown spectral gaps.

Define the positive measures on [0,infinity)

    mu_N = N^(-2) sum_(m>=1) |Tr U_N^m|^2 delta_(m/N).

Multiply by exp(-2s0 t) and push forward by x=exp(-t) onto [0,1].
Its n-th moment is L_N(s0+n/2). Convergence of all these moments,
including total mass at n=0, implies weak convergence of the finite
measures on [0,1], by uniform polynomial approximation. The limiting
measure is the corresponding push-forward of min(t,1) dt. For any
compactly supported continuous phi on [0,infinity), the function
x^(-2s0) phi(-log x), extended by zero near x=0, is continuous on
[0,1]. It follows that mu_N(phi) converges to its claimed integral.
The symmetry |p_(-m)|=|p_m| and the reference Riemann sums give the
full weighted comparison for every smooth compactly supported w on R.

For completeness, the converse needs a tail argument; vague convergence
alone must not be used to justify an unbounded Laplace test. Write
a_m=|Tr U_N^m|^2, including a_0=N^2. This sequence is the Fourier
transform of the positive eigenangle-difference measure. Set

    F_N(q)=sum_(|k|<N) (1-|k|/N) a_(q+k).

The Fourier transform of the triangular weights is the nonnegative
Fejer kernel. Thus 0<=F_N(q)<=F_N(0), by integration against that
positive measure and the triangle inequality. Every integer interval
of N consecutive m's is covered by weights at least 1/2 in a suitable
translate. Hence its a_m sum is at most 2 F_N(0). The compact-window
comparison, tested against a fixed nonnegative smooth majorant of
[-1,1], gives F_N(0)/N^2=O(1). The a_0 term contributes exactly 1
to this normalized bound; it must not be replaced by min(0,N).
Therefore mu_N([j,j+1)) is bounded uniformly in j,N. The tails of
exp(-2st) are now uniformly summable, proving (10).

For the deleted clock (3), exactly

\[
 L_N(s)=\frac1{N^2}\left[
 \frac{r^2}{1-r^2}+(N^2-1)
             \frac{r^{2(N+1)}}{1-r^{2(N+1)}}\right]
 \longrightarrow\frac1{e^{2s}-1}.
\tag{11}
\]

At s=1 this is approximately 0.156518, while (10) is approximately
0.216166. Thus the ratio derivative distinguishes the explicit spectrum
which has exactly the CUE determinant covariance.

## 4. What was and was not achieved

The deleted-clock control and the exact ratio/Abel reduction have been
derived and checked. They identify an insufficient target and a sufficient
one; they do not establish the sufficient estimate. Direct attempts to
bound (5) using unitarity leave resolvents of size (1-r)^(-1)=O(N),
and products of determinants can have exponential size. No o(1) control
of (9), or of its mixed derivative, follows from the evaluated principal
minor sums. No existing source checked in this continuation supplies it
for U_N=exp(i 10^(-80) N A_N)M_N.

The exact CUE calculation, the compactness/Fejer argument, and the
counterexample are internal method controls, not a claimed breakthrough.
Even closing this pair statement would leave the all-k joint estimates.
