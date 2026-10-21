> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/arithmetic_oldspace_escape.md`. Embedded SHA256: `596d44605310cc898fa75e23df4aa811189a1764fed21ce8b9f5d07ae734813a`.
> [Thematic guide](../../topics/arithmetic.md).

# Canonical old subspaces: exact escape and an actual fixed-tau asymptotic

Research continuation, 20 October 2026. All results below concern the exact
matrices in the question. The parameter is the fixed number tau=10^(-80).
The asymptotic in Theorem 3 does not replace it by an N-dependent parameter.
These results exclude specific arithmetic mechanisms; they do not prove
H_diag or Sine_2 statistics.

## 1. Statements

Write N=d^2 m, where d>=3 and m>=1 are odd. Define an isometry
J=J_(d,m):C^m -> C^N by

$$
(J\phi)(x)=
\begin{cases}
d^{-1/2}\phi(y\bmod m),&x=dy\pmod N,\\
0,&d\nmid x.
\end{cases}
\tag{1.1}
$$

There are exactly d copies of every coordinate of phi. Put
H_old=Ran(J), P=JJ*, Q=I-P. Thus rank(P)=m=N/d^2.

**Theorem 1: exact escape.** For every such d,m and every nonzero algebraic
complex number z,

$$
M_NJ=JM_m,\qquad
U_N(z)H_{\rm old}\cap H_{\rm old}=\{0\}.
\tag{1.2}
$$

Here M_1=(1). In particular, no eigenvector of the actual U_N(tau) lies in
any of these canonical old subspaces.

**Theorem 2: uniform infinitesimal escape.** For the same d,m,

$$
\boxed{\|QA_NJ\phi\|\ge \frac{\sqrt3}{200}\|\phi\|.}
\tag{1.3}
$$

This is uniform even when d and m vary. It also implies that no vector in
H_old can be a quasimode for A_N with residual less than sqrt(3)/200.

**Theorem 3: asymptotic mean escape at the full fixed parameter.** For each
fixed odd d>=3, along every odd m -> infinity with N=d^2m,

$$
\boxed{\frac1N\operatorname{Tr}(P U_N(\tau)^*P U_N(\tau))
                  \longrightarrow\frac1{d^4}.}
\tag{1.4}
$$

Equivalently,

$$
\frac1m\|PU_N(\tau)P\|_{\rm HS}^2\to\frac1{d^2},
\qquad
\frac1m\|QU_N(\tau)P\|_{\rm HS}^2\to1-\frac1{d^2}.
\tag{1.5}
$$

For the tower of powers of 7, choose d=7: the average retained norm-squared
of the canonical subspace of dimension N/49 tends to 1/49, and the average
escaped norm-squared tends to 48/49. The theorem concerns an average over
an orthonormal basis of that deterministic subspace, not extra randomness
in the matrix or parameter. It does not give a uniform minimum escape
angle over all vectors.

## 2. Exact kernel and the off-diagonal coefficient

Let h=(N+1)/2, the integer representative of the inverse of 2 modulo N.
The prescribed quantization gives the exact Jacobi entries

$$
(A_N)_{xx}=V(x/N),\qquad
(A_N)_{x,x+1}=w_x=
\frac{e^{-i\alpha_0}}{200}r((x+h)/N),
\tag{2.1}
$$

with the opposite entries conjugate, where

$$
V(q)=\cos(14\pi q)+\frac{r(q)}{10}
       +\frac{r(q)\sin(2\pi q)}{100}-\frac1{10}.
\tag{2.2}
$$

To obtain (2.1), separate the l=0,1,-1 Fourier terms in the question.
For l=1 the p-Fourier coefficient of cos(2pi p-alpha_0) is
e^(-i alpha_0)/2, and T_N(1,k) evaluates its q-polynomial at (x+h)/N.
The other coefficient follows by Hermitian conjugation.

For integer y and odd N,

$$
r(y/N)=0\quad\Longleftrightarrow\quad N\mid7y.
\tag{2.3}
$$

Indeed, the first factor vanishes exactly at these points, and the second
would require 2y=(2j+1)N, impossible when N is odd.

To prove M_NJ=JM_m with its precise scalar, write the input index as
y=d(v+jm), with 0<=v<m and 0<=j<d. In the exponent of M_N, changing j
changes the quadratic expression by

$$
-2xdjm+3d^2(2vjm+j^2m^2).
$$

The second summand is divisible by N. Summing the first produces
sum_(j=0)^(d-1) e_d(2*bar8*x*j), which is zero unless d divides x,
because 2*bar8 is a unit modulo d. When x=du this sum is d and the
remaining phase is exactly

$$
e_m[-\overline8_m(3u^2-2uv+3v^2)].
$$

The reduction of bar8_N modulo m is bar8_m, and
d/(sqrt(N)*sqrt(d))=1/(sqrt(d)*sqrt(m)). The positive real normalizations
therefore give M_NJ=JM_m without an additional scalar. For m=1 the same
sum gives the one-dimensional identity.

## 3. Exact escape by an explicit minor

Choose the m rows x_u=du-1 modulo N, 0<=u<m, and let R be their restriction
map. They lie outside dZ, so RJ=0. Only the neighbor x_u+1=du of each
chosen row lies in dZ, since d>=3. This remains true for u=0 at the cyclic
seam. Thus

$$
RA_NJ=\operatorname{diag}_{0\le u<m}
                  (d^{-1/2}w_{du-1}).
\tag{3.1}
$$

For y=du-1+h, one has 2y=-1 modulo d, hence gcd(y,d)=1. If w_(du-1)
were zero, (2.3) would give d^2|7y and therefore d^2|7, impossible for
d>=3. Every entry of (3.1) is nonzero.

Consequently the analytic function

$$
F(t)=\det(R e^{tA_N}J)
=t^m d^{-m/2}\prod_{u=0}^{m-1}w_{du-1}+O(t^{m+1})
\tag{3.2}
$$

is not identically zero. All matrices in (3.2) are algebraic, and A_N is
Hermitian. The exponential-polynomial transfer proved in Section 2 of
`arithmetic_second_order_proof.md` applies to this determinant: after
collecting equal algebraic frequencies, Lindemann-Weierstrass gives F(t)
nonzero at every nonzero algebraic t. Its cited published theorem is
Popescu, Theorem 3.2, DOI 10.1007/978-3-031-51959-8_16.

At t=iNz, the identity M_NJ=JM_m now makes

$$
RU_N(z)J=R e^{iNzA_N}J M_m
$$

invertible. Since R vanishes on H_old, no nonzero vector in U_N(z)H_old
can belong to H_old. This proves Theorem 1. The argument proves exact
nonintersection; Lindemann-Weierstrass supplies no lower bound on this
minor or on a principal angle.

## 4. A uniform quantitative bound for the generator

The supports of A_NJ e_u for different u are disjoint: the centers are
distinct multiples of d, their mutual cyclic distance is at least d>=3,
and their support neighborhoods have radius 1. Subtracting their
projections into H_old preserves this orthogonality. Put

$$
q=u/(dm),\qquad q_j=q+j/d,\quad 0\le j<d,\qquad
\epsilon=1/(2N).
$$

The diagonal Gram entry of (QA_NJ)*(QA_NJ) corresponding to u is exactly

$$
\mathcal E_d(q,\epsilon)=
\frac1d\sum_j|V(q_j)-\overline V|^2
 +\frac1{40000d}\sum_j
  \left[r(q_j+\tfrac12-\epsilon)^2+
        r(q_j+\tfrac12+\epsilon)^2\right],
\tag{4.1}
$$

where bar(V)=d^(-1)sum V(q_j). Formula (4.1) includes both the variation
of the diagonal entries between the duplicated copies and the two
off-diagonal escape coordinates. The factors 1/2 in the arguments are
forced by the modular inverse h, and cannot be dropped.

If d is odd and d!=7, the mean of cos(14pi q_j) is zero and its mean
square is 1/2, by finite geometric sums. Also

$$
V(q)=\frac9{10}\cos(14\pi q)+W(q),\qquad
|W(q)|\le\frac6{25}.
$$

Here W=(1/10)(1-cos(14pi q))cos(2pi q)+(1/100)r(q)sin(2pi q), and
0<=r<=4. Orthogonal projection off the constants is a contraction in the
discrete L2 norm. Hence the square root of the first term of (4.1) is at
least 9/(10sqrt(2))-6/25, which is greater than 9/25.

For d=7 put t=14pi q, C=cos(t), and delta=7pi/N. Finite Fourier
orthogonality at the frequencies 1 and 2 gives exactly

$$
\mathcal E_7(q,\epsilon)=
\frac{81}{16000}(1-C)^2
 +\frac3{80000}
  \left[(1+\cos(t-\delta))^2+(1+\cos(t+\delta))^2\right].
\tag{4.2}
$$

For example, the diagonal variation is (1-C) times
(1/10)cos(2pi q_j)+(1/100)sin(2pi q_j)+(1/200)sin(4pi q_j), whose squared
discrete norm is (81/16000)(1-C)^2. For each off-diagonal term, the
remaining average of (1+cos)^2 is 3/2.

Since N>=49, delta<=pi/7 and cos(delta)>0. Convexity of the square bounds
the bracket in (4.2) below by 2(1+C cos(delta))^2. If C>=0 this gives
at least 3/40000; if C<0 the first term alone gives at least 81/16000.
Thus every Gram entry in every case is at least 3/40000, proving (1.3).

For comparison with finite times, a direct row-sum or Fourier bound gives
||A_N||<=59/50. Unitary Taylor's formula therefore yields, for real s,

$$
\sigma_{\min}(Qe^{isA_N}J)
 \ge c|s|-\tfrac12(59/50)^2s^2,\qquad c=\sqrt3/200.
\tag{4.3}
$$

In particular, it is at least c|s|/2 if |s|<=c/(59/50)^2. With s=N*tau
this only covers N up to about 6.2 times 10^77. That large finite range
is not an asymptotic theorem at fixed tau. Theorem 3 instead uses the
fixed classical time of the prescribed exponential and is proved next.

## 5. Ordinary Weyl operators and a self-contained Egorov estimate

For integer Fourier labels v=(k,l), define

$$
(W_N(k,l)\psi)(x)=
 \exp(2\pi ikx/N+\pi ikl/N)\psi(x+l),
\qquad
\operatorname{Op}_N(b)=\sum_{k,l}\widehat b(k,l)W_N(k,l).
\tag{5.1}
$$

The Fourier sum converges in operator norm for a smooth torus symbol b.
Because N is odd, the prescribed modular Weyl operator obeys

$$
T_N(l,k)=(-1)^{kl}W_N(k,l).
$$

Consequently A_N=Op_N(a) exactly, for the fixed smooth real symbol

$$
\boxed{a(q,p)=V(q)+\frac1{100}r(q+\tfrac12)
                         \cos(2\pi p-\alpha_0).}
\tag{5.2}
$$

The Fourier support of a lies in |k|<=9, |l|<=1, and
sum |a_hat(k,l)|<=59/50. In particular this is not obtained by silently
replacing the modular inverse of 2 with the ordinary real fraction.

Direct multiplication in (5.1) gives, with sigma(v,w)=l*k'-k*l',

$$
W_N(v)W_N(w)=e^{\pi i\sigma(v,w)/N}W_N(v+w).
\tag{5.3}
$$

Three elementary consequences, for fixed smooth symbols b,c, are

$$
\|\operatorname{Op}_N(b)\operatorname{Op}_N(c)
                         -\operatorname{Op}_N(bc)\|=O(N^{-1}),
\tag{5.4}
$$

$$
\frac1N\|\operatorname{Op}_N(b)\|_{\rm HS}^2
                         \longrightarrow\int_{\mathbb T^2}|b|^2,
\tag{5.5}
$$

$$
iN[A_N,\operatorname{Op}_N(b)]
                         =\operatorname{Op}_N(Xb)+O_b(N^{-2}),
\quad
X=\frac1{2\pi}(a_p\partial_q-a_q\partial_p).
\tag{5.6}
$$

For (5.4), use |e^(iu)-1|<=|u| termwise in the absolutely convergent
Fourier sum, weighted by |v||w|. For (5.5), the normalized trace of W_N(v)
vanishes unless both labels are divisible by N. For trigonometric
polynomials this gives exact Fourier orthogonality for sufficiently
large N. Approximation by their Fourier truncations in the absolutely
summable norm gives (5.5) for smooth symbols. For (5.6), subtract the
linear term from 2i sin(pi*sigma/N) in the commutator and use
|sin u-u|<=|u|^3/6. The Fourier sums weighted by third powers converge.
The Poisson bracket is b_q*c_p-b_p*c_q, so the sign in (5.6) is fixed by
iN*[Op(a),Op(b)]=-(1/(2pi))*Op({a,b})+O(N^-2)=Op(Xb)+O(N^-2).

Let Phi_s be the classical flow of X and E_N(s)=exp(isNA_N). From (5.6)
and Duhamel's formula one obtains, for every fixed smooth b and fixed s,

$$
E_N(s)\operatorname{Op}_N(b)E_N(s)^*
  =\operatorname{Op}_N(b\circ\Phi_s)+O_{b,s}(N^{-2}).
\tag{5.7}
$$

Indeed, differentiate the conjugated comparison with the transported
symbol. Its defect is (5.6) at b composed with Phi_t. The relevant
weighted Fourier seminorms are bounded on a compact time interval,
because the smooth flow preserves smoothness. Integrating the defect
proves (5.7); the conjugating matrices are unitary. This proof establishes
precisely the fixed-time operator-norm estimate used here and makes no
long-time decorrelation assertion.

For g=(alpha,beta) in (Z/dZ)^2 put
T_g=T_N(dm*alpha,dm*beta) and let t_g be translation by
(alpha/d,-beta/d) on the torus. Conjugating (5.1) gives the exact identity

$$
T_g\operatorname{Op}_N(b)T_g^*
                       =\operatorname{Op}_N(b\circ t_g).
\tag{5.8}
$$

## 6. The normalized trace lemma

**Lemma.** Let F_N be unitary matrices and kappa a fixed smooth torus map.
Suppose, for every fixed smooth b,

$$
F_N\operatorname{Op}_N(b)F_N^*
               =\operatorname{Op}_N(b\circ\kappa)+o(1)
\tag{6.1}
$$

in operator norm. If the fixed-point set of kappa has Lebesgue measure
zero, then Tr(F_N)/N -> 0.

**Proof.** Consider the functionals
L_N(b)=N^(-1)Tr(Op_N(b)F_N). Hilbert-Schmidt Cauchy-Schwarz and (5.5)
give limsup |L_N(b)|<=||b||_L2. From any subsequence, extract a further
subsequence on which L_N converges on a countable dense set of
trigonometric polynomials. Its limit extends to a bounded functional on
L2 with norm at most 1, so is integration against a function mu in L2.
The same convergence holds for every fixed smooth symbol, by approximation
and the Hilbert-Schmidt bound.

Using (5.4), (6.1) and cyclicity of the trace, one gets for any smooth b,c

$$
L_N(c(b\circ\kappa))
 =N^{-1}\operatorname{Tr}(\operatorname{Op}_N(c)F_N
                                      \operatorname{Op}_N(b))+o(1)
 =L_N(cb)+o(1).
$$

Thus mu*(b composed with kappa-b)=0 almost everywhere for every b.
It suffices to use the two coordinate characters exp(2pi iq) and
exp(2pi ip): outside Fix(kappa), one of these two factors is nonzero.
Hence mu is supported on Fix(kappa), and the measure-zero assumption
forces mu=0. Every possible subsequential limit of L_N(1) is zero,
which proves the assertion. No stationary-phase theorem is used.

If kappa is a nonidentity real analytic torus diffeomorphism isotopic to
the identity, its fixed set has measure zero. To see this, lift it as
z -> z+u(z), with u periodic real analytic. Fixed points are the zeros
of u(z)-n for integers n in a bounded range. A nonzero real analytic
function has a measure-zero zero set: locally, restrict to lines in a
direction with a nonzero lowest Taylor derivative, use the discreteness
of one-dimensional analytic zeros, and apply Fubini; a countable cover
finishes the argument. If both components of u-n vanished identically,
the torus map would be the identity. Applying the scalar assertion to a
nonzero component proves the claim about fixed points.

## 7. No translation relation survives at the prescribed time

For g,h in (Z/dZ)^2 define

$$
F_N(g,h)=T_g E_N(\tau)^*T_h E_N(\tau).
$$

Equations (5.7)-(5.8), in their actual order, give (6.1) for

$$
\kappa_{g,h}=\Phi_\tau\circ t_h\circ\Phi_{-\tau}\circ t_g.
\tag{7.1}
$$

We prove kappa_(g,h) is nonidentity unless g=h=0. First suppose it is
the identity. Use real representatives gamma,eta of the translation
vectors of t_g,t_h, and the equivariant lift F of Phi_tau. The identity
implies

$$
F(z+\eta)=F(z)-\gamma+n
$$

for a constant n in Z^2. Iterating d times and using d*eta in Z^2 gives
d*eta=-d*gamma+d*n. Thus gamma+eta is integral, and Phi_tau commutes
with t_h.

It remains to show that a translation commuting with this time map must
preserve X itself. We prove this with a bound relative to the difference
of vector fields, so arbitrarily small translations cause no difficulty.
Let Y be any translate of X and D=X-Y. From the Fourier support and
absolute coefficient bound following (5.2), one has the generous bounds

$$
\|X\|_\infty,\|Y\|_\infty\le20,
\qquad\|\nabla X\|_\infty,\|\nabla Y\|_\infty\le2000.
\tag{7.2}
$$

The symbol has at most 57 Fourier labels, each of Euclidean length below
10. For the vector polynomial D, each Fourier coefficient has norm at
most ||D||_infty by its integral formula. Therefore

$$
\|\nabla D\|_\infty\le4000\|D\|_\infty.
\tag{7.3}
$$

Let F_X^s and F_Y^s be their equivariant lifted flows. Gronwall applied
to their difference gives
||F_X^s-F_Y^s||_infty<=s*exp(2000s)*||D||_infty for s>=0. In the integral
equation for this difference, subtract sD(z), use (7.2)-(7.3), and obtain

$$
\|F_X^s-F_Y^s-sD\|_\infty
\le\tfrac12 s^2(80000+2000e^{2000s})\|D\|_\infty
\le10^5s^2\|D\|_\infty
\tag{7.4}
$$

for 0<=s<=10^(-6). If the time-tau maps are equal on the torus, their
lifts are equal as well: each lift has displacement at most 20*tau, so
their difference cannot be a nonzero integer. Equation (7.4), with
10^5*tau<1, then forces D=0.

A translation t_h commuting with Phi_tau conjugates the X-flow to the
flow of a translated vector field, with the same time-tau map. Hence it
preserves X. The two Fourier coefficients

$$
\widehat a(1,0)=\frac1{20}-\frac{i}{200}\ne0,
\qquad
\widehat a(0,1)=\frac{e^{-i\alpha_0}}{200}\ne0
\tag{7.5}
$$

show that a translation preserving X has both coordinates integral.
Thus h=0, and then g=0. The coefficients in (7.5) are obtained directly
from (5.2); the Hamiltonian vector field does not kill either nonzero
Fourier label.

The vector field is real analytic because a is a trigonometric
polynomial. Its local flow is real analytic: Picard iteration on a
common small complex neighborhood converges uniformly to a holomorphic
flow, and restriction to the real torus gives the assertion. Therefore
every map (7.1) is real analytic. Section 6 applies and proves

$$
\frac1N\operatorname{Tr}F_N(g,h)\longrightarrow0
\quad\text{for every }(g,h)\ne(0,0).
\tag{7.6}
$$

## 8. Completing the overlap asymptotic

The translation operators T_g form an exact representation of the finite
abelian group (Z/dZ)^2. Their Weyl cocycle is trivial because
(dm)^2=N*m. Their average is exactly the old projector:

$$
P=\frac1{d^2}\sum_g T_g.
\tag{8.1}
$$

For an elementary verification, T_(alpha,beta) acts as
e_d(beta*x) times the shift by dm*alpha. Averaging beta forces d|x;
averaging alpha averages the d copies in (1.1), which is JJ*.

Since M_N commutes with P by its intertwining property and unitarity,

$$
\begin{aligned}
\frac1N\operatorname{Tr}(P U_N^*P U_N)
&=\frac1N\operatorname{Tr}(P E_N(\tau)^*P E_N(\tau))\\
&=\frac1{d^4}\sum_{g,h}\frac1N\operatorname{Tr}F_N(g,h).
\end{aligned}
$$

For fixed d this is a fixed finite sum. The (0,0) term is 1, and every
other term tends to zero by (7.6). This proves (1.4), and the elementary
Hilbert-Schmidt identities give (1.5).

As one consequence, if 0<=epsilon<1/2, the number R_N(epsilon) of vectors
in any orthonormal eigenbasis of U_N whose old mass is at least
1-epsilon satisfies

$$
R_N(\epsilon)
\le\frac{m/d^2+o(m)}
{(\sqrt{1-\epsilon}-\sqrt\epsilon)^2}.
\tag{8.2}
$$

Indeed, for such an eigenvector psi, with v=Ppsi,
||PUP psi||>=sqrt(1-epsilon)-sqrt(epsilon). The projected vectors v
form a Bessel family because the eigenvectors are orthonormal. Summing
||PUP v||^2 over that family is at most ||PUP||_HS^2; also PUP v=PUP psi.
Now use (1.5). This is an upper bound on almost-old eigenvectors, not an
assertion that every eigenvector is uniformly separated from H_old.

## 9. Scope and dependencies

Theorem 3 is unconditional for the prescribed family and fixed tau.
It uses neither classical mixing nor a random surrogate. Its only
asymptotic ingredients, (5.4)-(5.7) and the normalized trace lemma, were
proved above from the finite Weyl identities, elementary Fourier bounds,
unitary Duhamel estimates and Hilbert-space compactness. No assumption
about spectral statistics has entered.

Theorem 1 uses the published Lindemann-Weierstrass theorem as cited in
Section 3. Theorem 2 is a direct finite-dimensional estimate. The theorem
about trace overlap does not depend on Lindemann-Weierstrass.

The fixed d qualification in Theorem 3 is essential to the proof: the
group sum must contain a fixed number of terms, and no uniform bound in
d has been shown for its vanishing terms. Nor is an effective rate in
N established in this report. Most importantly, an old-space overlap
controls only a particular bounded observable of one step of U_N. It
does not control the weighted products of traces of U_N^n for n of
order N that are required by H_diag.

This report uses the original family definition and the read-only
Jacobi verification in `../research_continuation_2026_10_20/verify_spectral_simplicity.py`,
SHA-256 `add99347a674298335226dccb58b87c35a7343a33c97053bd2310f69c07bd6cf`.
All new mathematical arguments are written in full above. The separate
finite certificate report `arithmetic_second_order_proof.md` records
its own exact inputs and numerical field certificates.
