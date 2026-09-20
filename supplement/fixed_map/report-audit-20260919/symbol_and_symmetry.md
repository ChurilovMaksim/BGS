# What the explicit redesigned symbol does and does not establish

19 September 2026. The symbol below belongs to the uploaded reports.
It is an auxiliary candidate, not a replacement of the already frozen
tau=10^-80 model. This is a self-review with exact algebra and finite checks.

## 1. Exact classical Fourier algebra

\[
\begin{split}
f_\star(q,p)={}&\cos2\pi(q+1/5)+\cos2\pi(2q+1/15)\\
&+\sin2\pi(q+1/5)\sin2\pi(p+1/8)
+\sin2\pi(2q-7/20)\sin4\pi p.
\end{split}
\]

Write Q=2pi(q+1/5), P=2pi p, u=sin(P+pi/4), v=sin(2P)-1/2 and
w=sqrt(3)/2. Then

\[
f_\star=\cos Q+u\sin Q+v\cos2Q+w\sin2Q.              \tag{1}
\]

Orthogonality of the first and second harmonics gives

\[
\frac1{24}\int_0^1f_\star(q,p)^4dq
=\frac{(1+u^2)^2+(v^2+w^2)^2+4(1+u^2)(v^2+w^2)}{64}.
                                                               \tag{2}
\]

For x=sin(2P), this is x^4/64+29x^2/256-9x/128+37/256, hence exactly

\[
A_4(p)=\frac{53}{256}-\frac9{128}\sin4\pi p
-\frac{33}{512}\cos8\pi p+\frac1{512}\cos16\pi p.      \tag{3}
\]

The quartic coefficients at p-frequencies +/-6 vanish; those at +/-8
are 1/1024. These claims in the reports are correct.

The *whole* cubic vertical projection does not vanish. The same elementary
calculation gives

\[
\frac16\int_0^1f_\star(q,p)^3dq
=-\frac1{16}+\frac3{32}\sin4\pi p+\frac1{32}\cos8\pi p
+\frac{\sqrt3}{8}\sin(2\pi p+\pi/4).                 \tag{4}
\]

Only particular cubic channels, including frequency +/-3, have been
eliminated. Describing that as elimination of every cubic obstruction
requires the actual definition and proof of the claimed reduction.

For odd N>1, cos(16pi j/N) never vanishes: a zero would imply
32j=N(2l+1), contradicting parity. Also the average of cos(32pi j/N)
is zero, since N does not divide 16. Therefore

\[
\frac1N\sum_{j=0}^{N-1}\left|\frac1{512}\cos(16\pi j/N)\right|^2
=\frac1{524288}.                                     \tag{5}
\]

The exception N=1 must be excluded. Formula (5) is about the classical
sampled function; it is not itself a spectral-correlation statement.

## 2. The quantum quartic coefficient is not literally (3)

In ordinary midpoint Weyl quantization, W(v)W(w)=exp(pi i det(v,w)/N)W(v+w).
For N>16, so that the fourth power has no Fourier aliases, the coefficient
at vertical frequency (0,8) in Op_N(f_star)^4/24 equals

\[
c_N=\frac{1+\cos(16\pi/N)+\cos(32\pi/N)}{3072}.        \tag{6}
\]

Here physical Fourier mode e(aq+bp) is represented by W(b,a); swapping
the two coordinates changes the phase sign but not the cosines in (6).

Indeed, to reach p-frequency 8, all four factors must have p-frequency 2.
Their q-frequencies are +/-2. Two of each are required. Their coefficient
product is 1/256, independent of the q translation used in (1).
The six orderings have total phases
exp(+/-32pi i/N), exp(+/-16pi i/N), 1, 1. Division by 24 proves (6).
The labels involved all have even coordinate product, so this particular
coefficient also agrees in the raw modular gauge. This does not assert
equality of the complete quantum symbols in those gauges.

Consequently c_N=1/1024-5pi^2/(24N^2)+O(N^-4). It is negative at N=25
and N=31, for example, although the classical coefficient is positive.
These are non-aliased dimensions. Direct matrix multiplication checks
(6) at N=17,23,25,31,33,65 with errors below 1e-13.

Thus if a reduction is meant to act on the quantum exponential, the
classical product f^4 cannot be substituted without a quantified comparison.
The convergence of (6) alone does not supply such a comparison for the
full reduced obstruction at fixed classical coupling.

## 3. Classical dynamics: what can be checked directly

For F_kappa=Phi_f_star^kappa composed with S, S=[[3,4],[2,3]], Hamiltonian
flow preserves area. With the convention X_f=(f_p,-f_q), its derivative
generator is J Hess(f), which has trace zero.

Uniform Hessian-entry bounds are
|f_qq|<=40pi^2, |f_pp|<=20pi^2, |f_qp|<=20pi^2. Its Frobenius norm is
at most 20sqrt(7)pi^2. A matrix of unit eigenvectors of S has condition
number sqrt(2), so in that basis the flow derivative B and its inverse
satisfy

\[
\|B-I\|,\ \|B^{-1}-I\|\le e^{20\sqrt{14}\pi^2|\kappa|}-1=\delta.
\]

Put lambda=3+2sqrt(2) and
delta_0=(1-lambda^-2)/(2sqrt(1+lambda^-4)). For delta<delta_0, the forward
map BD sends |y|<=|x| strictly into itself, where D=diag(lambda,lambda^-1):
the error in either coordinate is at most
delta*lambda*sqrt(1+lambda^-4)|x|. Its x expansion exceeds
(lambda+lambda^-1)/2=3. For the inverse D^-1 B^-1, the stable cone
|x|<=|y| is strictly preserved, and its y expansion is at least
lambda*(1-sqrt(2)*delta)>1 throughout this range. The two strict cone
conditions give invariant expanding and contracting lines by nested
cone intersections, hence Anosov hyperbolicity.

This verifies the reported sufficient smallness condition

\[
|\kappa|<\frac{\log(1+\delta_0)}{20\sqrt{14}\pi^2}.
\]

For the continued fixed point issuing from zero, the derivative of its
Jacobian trace at kappa=0 is 2f_pp(0)-4f_qq(0), namely

\[
\pi^2[16\cos(2\pi/5)+64\cos(2\pi/15)+4\sqrt2\sin(2\pi/5)]
=678.941627\ldots\ne0.                               \tag{7}
\]

The change of the fixed point makes no first-order contribution from S,
whose derivative is constant. A C^1 conjugacy preserves the derivative
trace at corresponding fixed points. A toral affine map conjugate to this
map must have linear part conjugate to S on homology, and hence trace 6.
Equation (7) rules this out for sufficiently small nonzero kappa.

The external classification input was checked in Newhouse,
*On Codimension One Anosov Diffeomorphisms* (1970),
[Corollary (1.3), page 762](https://users.math.msu.edu/users/newhous7/Papers/PDF/Codimension-1-Anosov.pdf).
It identifies codimension-one Anosov maps up to topological conjugacy
by their fundamental-group action. On T^2 both invariant bundles are
one-dimensional, and the Hamiltonian flow is isotopic to the identity,
so F_kappa and S have the same fundamental-group action. They are
therefore topologically conjugate. The linear map S is mixing: its
Fourier correlations of nonconstant characters vanish eventually,
because a nonzero integer frequency has an unbounded forward orbit
under S^T. Approximation proves mixing for Lebesgue measure; its full
support then implies topological mixing. Conjugacy transfers the latter
property to F_kappa. This does not infer a quantum spectral law.

## 4. Symmetry claims need their actual scope

For the classical symbol f_star, the complete affine symmetry group is
{identity, R}, with R(q,p)=(q,1/4-p). Here an affine symmetry means an
integer unimodular linear map followed by a torus translation, preserving
the function pointwise.

To verify exhaustiveness, coefficients of modulus 1/2 occur only on
+/-(1,0),+/-(2,0); mixed coefficients have modulus 1/4. The linear
transpose must therefore preserve the primitive q direction up to sign.
Write the physical linear map [[epsilon,0],[u,delta]], with epsilon and
delta in {+1,-1}. Preservation of the mixed p-frequency-one support gives
|epsilon+u|=|epsilon-u|=1, so u=0. There are only four diagonal choices.
A q reflection would require simultaneously t_q=-2/5 mod 1 and
2t_q=-2/15 mod 1, which is impossible. With q fixed, its translation is
zero. The p-preserving choice requires zero p translation, and the
p-reflecting choice requires t_p=1/4. Direct substitution verifies R.

This classifies affine symmetries of the *symbol*, not every reversor of
the *map*, nor every symmetry of the *quantum operator*. In fact
R S R differs from S^-1 by translation (0,1/2), so even the surviving
symbol reflection is not a cat reversor with that shift.

Literally, the claim that a finite-dimensional unitary U has only scalar
commuting unitaries is false: its spectral projections generate a
commutant, which is U(1)^d for simple spectrum. Likewise, complex
conjugation in any orthonormal eigenbasis gives an antiunitary J with
J U J^-1=U^-1 and J^2=I. These spectrum-dependent constructions do not
put every chaotic model in the orthogonal symmetry class. The physically
relevant exclusion must quantify a prescribed geometric or semiclassical
class of symmetries. That missing qualification is essential.

The report does not provide a full proof excluding all allowed geometric
reversors of the quantum family. Its all-symmetries conclusion is not
accepted as stated.

## 5. Why the proposed no-go is not yet a theorem

Neither report defines the exact operator taking a symbol or quantum
propagator to the alleged reduced scalar O_N(kappa) or B_N(kappa,p).
The Phi_N, eta_3 and typical-fibre measures in other branches are likewise
not defined in the supplied summaries. Links to /session/... are internal
references, not accessible proofs in these attachments. Therefore neither
the precise remainder norm nor the implication from a nonzero coefficient
to failure of BGS can currently be checked from those summaries.

Even with a defined reduction, three separate obligations are needed:

1. Prove that the actual spectral target forces the reduced quantity to vanish.
2. Identify its coefficient with the claimed classical or quantum calculation.
3. Bound the remainder uniformly in the N and coupling regime of that target.

Only the finite classical algebra is supplied and verified here. The
missing work is not demonstrably just obligation 3.

The scale issue also precedes small divisors. The symbol has Wiener norm
4, so exp(i epsilon f) has a classical Taylor-tail estimate bounded by
exp(4|epsilon|)(4|epsilon|)^5/5!. For a Hermitian quantum A with ||A||<=4,
the operator-norm integral remainder is at most (4|epsilon|)^5/5!.
In the reported quantum propagator epsilon=kappa/hbar_N=2pi kappa N.
These bounds are not uniform O(kappa^5) at fixed classical kappa.
A different effective expansion parameter needs an actual derivation.

A simple logical warning is O_N(kappa)=kappa^4 exp(-N kappa^2)/1024:
every finite N has the same nonzero quartic coefficient, whereas the
quantity tends to zero for each fixed nonzero kappa. This is not a model
for the quantum map; it demonstrates why the order of limits cannot be
inferred from a finite Taylor coefficient.

Verified algebra, hyperbolicity and a useful candidate survive the audit.
An exclusion of this candidate from BGS does not follow.
