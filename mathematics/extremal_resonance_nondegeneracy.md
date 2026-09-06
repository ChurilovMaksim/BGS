# An isolated extremal Fourier mode forces positive resonance

**Status: general mathematical proof, with independent exact-arithmetic checks.**

For every hyperbolic matrix A in SL(2,Z), every nonconstant real trigonometric
polynomial has positive second-order cohomological variance. There is no
restriction on its bandwidth, coefficient signs, Fourier phases, or the sign
of tr(A). This supersedes the radius-eight restriction in
`resonance_nondegeneracy_and_hessian.md`; the older finite certificate remains
an independent check, not a hypothesis of the theorem.

The proof is a support-geometric argument, not extrapolation from finite
certificates. It proves a nondegeneracy theorem needed by this programme, not
BGS universality. External priority for this specialized theorem has not been
established. The general Fourier-orbit description of dynamical variance is
prior theory, including Cohen--Conze, arXiv:1304.4556.

## 1. Definitions and statement

Put S=A^T, C_A g=g composed with S, and e_v(x)=exp(2*pi*i*v.x) on T^2.
The Poisson bracket is {f,h}=f_x1 h_x2-f_x2 h_x1. Define
\[
 h_g=\frac{\{g,C_Ag\}}{4\pi},\qquad
 \Gamma_A(g)=\sum_{\mathcal O}
    \left|\sum_{k\in\mathcal O}\widehat h_g(k)\right|^2,       \tag{1}
\]
where O ranges over oriented A-orbits in Z^2 minus {0}. For a polynomial the
sums are finite. Its bracket has zero mean, since every summand contributing
at k=0 has det(u,Av)=det(u,-u)=0. Fourier differentiation gives
\[
 \widehat h_g(k)=-\pi\sum_{u+Av=k}
                  \det(u,Av)\widehat g(u)\widehat g(v).       \tag{2}
\]

**Theorem 1 (unrestricted finite Fourier nondegeneracy).** Let A in SL(2,Z)
satisfy |tr A|>2. Let g be any nonconstant real trigonometric polynomial.
Then Gamma_A(g)>0. More precisely, its nonzero Fourier support V contains
u,v such that, for k=u+Av,

1. k has exactly one ordered decomposition in V+AV;
2. det(u,Av) is nonzero;
3. A^j k is outside V+AV for every nonzero integer j.

Consequently
\[
 \boxed{\Gamma_A(g)\ge
 2\pi^2\det(u,Av)^2|\widehat g(u)\widehat g(v)|^2>0.}       \tag{3}
\]
Constants in g have no effect. Central symmetry of V is sufficient for the
three support assertions, even without any relation between the coefficients.
Reality gives the factor two in (3).

## 2. Hyperbolic coordinates

Write s=sign(tr A), B=sA, t=|tr A|>=3 and
\[
 \lambda=\frac{t+\sqrt{t^2-4}}2>1,\qquad
 \lambda+\lambda^{-1}=t.
\]
Choose independent real eigen-covectors xi,eta of B with
\[
 \xi(Bz)=\lambda\xi(z),\qquad
 \eta(Bz)=\lambda^{-1}\eta(z).
\]
There is no nonzero integer vector on either eigenline: t^2-4 lies strictly
between (t-1)^2 and t^2 for integer t>=3, hence the eigenvalues are irrational.
An integral matrix with an integral eigenvector would have a rational
eigenvalue. In particular the maxima below are positive.

Since V=-V, also AV=BV. Set
\[
 X=\max_{z\in V}|\xi(z)|>0,\qquad
 Y=\max_{z\in V}|\eta(z)|>0.
\]
All z in V+AV belong to the eigen-coordinate rectangle
\[
 |\xi(z)|\le(1+\lambda)X,\qquad
 |\eta(z)|\le(1+\lambda^{-1})Y.                            \tag{4}
\]

## 3. Constructing an exposed frequency

Choose v_X,u_Y in V with xi(v_X)=X and eta(u_Y)=Y. Put
\[
 a=\xi(u_Y)/X,\qquad b=\eta(v_X)/Y.
\]
Choose sigma in {+1,-1} with sigma(a+b)>=0 and define
\[
 L(z)=\xi(z)/X+\lambda\sigma\eta(z)/Y.                     \tag{5}
\]
The trial points sigma*u_Y in V and B*v_X in BV show that
\[
 \max_{u\in V}L(u)+\max_{w\in V}L(Bw)
 \ge (\lambda+\sigma a)+(\lambda+\sigma b)
 =2\lambda+|a+b|\ge2\lambda>t+2.                          \tag{6}
\]
The last inequality is strict because
2*lambda-(t+2)=sqrt(t^2-4)-2>0 for t>=3. This strict gap is the reason the
argument works even for the smallest possible hyperbolic trace, three.

Select u as the lexicographic maximizer of (L(z),xi(z)) over V, and w as the
maximizer of (L(Bz),xi(Bz)) over V. The two linear forms L and xi are
independent, so these lexicographic maximizers are unique. Put v=s*w and
k=u+Av=u+Bw. Then
\[
                              L(k)>t+2.                  \tag{7}
\]

**Unique decomposition.** Suppose k=u'+Av' with u',v' in V. In the
translation-invariant lexicographic order, the coordinate pairs of u' and Av'
are bounded above by the separately selected maxima. Their sums equal those
maxima's sum. Therefore each pair equals its maximum; independence of the two
linear forms implies u'=u and Av'=Av, hence v'=v. This is an exact assertion
about ordered pairs, not merely a vertex of the convex hull with multiplicity
left unchecked.

## 4. The entire orbit is excluded

If A^j k were in V+AV for j>=1, (4) and absolute eigenvalue scaling would give
\[
 |\xi(k)|\le(1+\lambda^{-1})X,\qquad
 |\eta(k)|\le(1+\lambda^{-1})Y.
\]
Then L(k)<=(1+lambda^-1)+lambda*(1+lambda^-1)=t+2, contradicting (7).
If j<=-1, (4) instead gives
\[
 |\xi(k)|\le(1+\lambda)X,\qquad
 |\eta(k)|\le(\lambda^{-1}+\lambda^{-2})Y,
\]
again implying L(k)<=t+2. This excludes every nonzero integer iterate,
including when A has negative eigenvalues. No truncation or unproved
separation of long Fourier orbits is used.

## 5. The surviving coefficient cannot have zero determinant

Suppose u=r*Av=r*Bw, with r real, and put R=|r|. Let
\[
 a_0=|\xi(w)|/X,\qquad b_0=|\eta(w)|/Y.
\]
The two memberships u,w in V imply
\[
 a_0,b_0\le1,\quad R\lambda a_0\le1,\quad
 R\lambda^{-1}b_0\le1.
\]
When R>0,
\[
 |L(k)|\le(1+R)(\lambda a_0+b_0)
 \le(1+R)\{\min(\lambda,R^{-1})+\min(1,\lambda/R)\}
 \le\lambda+2+\lambda^{-1}=t+2.                            \tag{8}
\]
For completeness the last scalar inequality has three cases. For
R<=lambda^-1 its left side is (1+R)(lambda+1), maximized at lambda^-1.
For lambda^-1<=R<=lambda it is 2+R+R^-1, bounded by t+2 because
(lambda-R)(lambda*R-1)>=0. For R>=lambda it is
(1+R^-1)(lambda+1), maximized at lambda. If R=0, the bound lambda+1 suffices.
Thus (8) contradicts (7). Therefore det(u,Av) is nonzero.

## 6. Completion and consequences

Equation (2), unique decomposition and nonzero Fourier coefficients give
\[
 \widehat h_g(k)=-\pi\det(u,Av)\widehat g(u)\widehat g(v)\ne0.
\]
Since its orbit meets V+AV only at k, its orbit sum is precisely this
coefficient. The orbit of -k is different: A^j k=-k would force -1 to be an
eigenvalue of A^j, impossible for a hyperbolic A and j nonzero, while j=0
would force k=0. As h_g is real, these two orbit sums have equal modulus.
This proves (3).

**Corollary 2 (no polynomial coboundary).** The bracket h_g is not a finite
Fourier coboundary f-C_A f. Along any orbit a finite difference has zero sum,
in contradiction with the isolated nonzero orbit sum above. In fact h_g is
not an L^2 coboundary either: on the isolated orbit a nonzero single forcing
coefficient would require a nonzero constant tail in the transfer function's
Fourier coefficients, contradicting square summability.

**Corollary 3 (phase-independent coercivity for flat Fourier amplitudes).**
Let M=|V| and suppose every nonzero Fourier coefficient obeys
\[
 |\widehat g(v)|\ge\alpha\|g-\widehat g(0)\|_2/\sqrt M,
 \qquad \alpha>0.
\]
Then the integer determinant in (3) has absolute value at least one, so
\[
 \Gamma_A(g)\ge\frac{2\pi^2\alpha^4}{M^2}
                   \|g-\widehat g(0)\|_2^4.                \tag{9}
\]
For a radius-R box this is an explicit order-R^-4 lower bound at fixed
alpha, without coefficient-sign or phase assumptions. The flatness hypothesis
is essential to this inference and is not imposed by trigonometricity alone.

**Corollary 4 (every fixed box has a positive minimum).** For R>=1 let P_R be
the real mean-zero polynomials with frequencies of max-norm at most R. Then
\[
 c_R(A)=\inf_{g\in P_R\setminus\{0\}}
                     \Gamma_A(g)/\|g\|_2^4>0.              \tag{10}
\]
Indeed Gamma is a continuous quartic on this finite-dimensional space and is
positive everywhere on its compact unit sphere. The proof supplies a
support-adaptive lower bound (3), not a bandwidth-uniform lower bound.

The Fourier-tail construction in `fourier_tail_locality.md` gives, for each
fixed s>1, constants C_s,c_s>0 with
\[
             0<c_R(A)\le C_s\exp(-c_s R^{1/s}).             \tag{11}
\]
Thus positivity for every finite Fourier polynomial coexists with loss of
coercivity faster than every inverse power of the bandwidth. Neither taking
R to infinity nor replacing a fixed symbol by an N-dependent analytic
approximation yields a uniform positive lower bound.

**Scope.** The argument uses a finite Fourier maximum. It does not prove
Gamma_A(g)>0 for every nonconstant analytic function with infinite support.
Smooth counterexamples in the return-word and separated-support notes remain
valid. Nor does positivity of this classical variance alone imply microscopic
GOE/GUE statistics or a quantum comparison up to Heisenberg time.

## 7. Reproducibility and independent verification

Run from the repository root:

```sh
python computations/verification/extremal_resonance.py \
  --output evidence/certificates/extremal_resonance.json \
  --replay /tmp/extremal_replay.txt
c++ -std=c++17 -O2 computations/cpp/extremal_resonance_replay.cpp \
  -o /tmp/extremal_resonance_replay
/tmp/extremal_resonance_replay /tmp/extremal_replay.txt
```

The Python constructor uses exact arithmetic in real quadratic fields. The
C++ checker independently verifies central symmetry, hyperbolicity, the
unique ordered decomposition, nonzero determinant and forward/backward
rectangle escape using arbitrary-precision integers. Rectangle escape excludes
all nonzero iterates, not merely a finite orbit window. The accompanying
certificate records finite test coverage, not a proof by enumeration.
