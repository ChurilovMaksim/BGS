# An isolated extremal Fourier mode forces positive resonance

**Status: general mathematical proof, with independent exact-arithmetic checks.**

For every hyperbolic matrix `A in SL(2,Z)`, every nonconstant real trigonometric polynomial has positive second-order cohomological variance. There is no restriction on bandwidth, coefficient signs, Fourier phases, or the sign of `tr(A)`. This supersedes the radius-eight restriction in `resonance_nondegeneracy_and_hessian.md`; the older finite certificate remains an independent check, not a hypothesis of the theorem.

The proof is support-geometric, not an extrapolation from finite certificates. It proves a nondegeneracy theorem needed by this programme, not BGS universality. External priority for this specialized statement has not been established. The general Fourier-orbit description of dynamical variance is prior theory, including Cohen--Conze, arXiv:1304.4556.

## 1. Definitions and statement

Put `S=A^T`, `C_A g=g composed with S`, and `e_v(x)=exp(2*pi*i*v.x)` on `T^2`. The Poisson bracket is `{f,h}=f_x1 h_x2-f_x2 h_x1`. Define

\[
 h_g=\frac{\{g,C_Ag\}}{4\pi},\qquad
 \Gamma_A(g)=\sum_{\mathcal O}
    \left|\sum_{k\in\mathcal O}\widehat h_g(k)\right|^2,       \tag{1}
\]

where `O` ranges over oriented `A`-orbits in `Z^2\{0}`. For a polynomial all sums are finite. Its bracket has zero mean, because a term contributing at `k=0` has `Av=-u` and therefore `det(u,Av)=0`. Fourier differentiation gives

\[
 \widehat h_g(k)=-\pi\sum_{u+Av=k}
                  \det(u,Av)\widehat g(u)\widehat g(v).       \tag{2}
\]

**Theorem 1 (unrestricted finite-Fourier nondegeneracy).** Let `A in SL(2,Z)` satisfy `|tr A|>2`, and let `g` be any nonconstant real trigonometric polynomial. Then `Gamma_A(g)>0`. More precisely, its nonzero Fourier support `V` contains `u,v` such that, for `k=u+Av`,

1. `k` has exactly one ordered decomposition in `V+AV`;
2. `det(u,Av) != 0`;
3. `A^j k` lies outside `V+AV` for every nonzero integer `j`.

Consequently

\[
 \boxed{\Gamma_A(g)\ge
 2\pi^2\det(u,Av)^2|\widehat g(u)\widehat g(v)|^2>0.}       \tag{3}
\]

Constants in `g` have no effect. Central symmetry of `V` is sufficient for the support assertions; reality is used for that symmetry and for the factor two in (3).

## 2. Hyperbolic coordinates

Write

\[
 s=\operatorname{sign}(\operatorname{tr}A),\qquad B=sA,
 \qquad t=|\operatorname{tr}A|\ge3,
\]
\[
 \lambda=\frac{t+\sqrt{t^2-4}}2>1,
 \qquad \lambda+\lambda^{-1}=t.
\]

Choose independent real eigen-covectors `xi,eta` of `B` with

\[
 \xi(Bz)=\lambda\xi(z),\qquad
 \eta(Bz)=\lambda^{-1}\eta(z).
\]

No nonzero integer vector lies on either eigendirection: `t^2-4` lies strictly between `(t-1)^2` and `t^2`, hence the eigenvalues are irrational, whereas an integral matrix with an integral eigenvector has a rational eigenvalue.

Since `V=-V`, also `AV=BV`. Set

\[
 X=\max_{z\in V}|\xi(z)|>0,\qquad
 Y=\max_{z\in V}|\eta(z)|>0.
\]

Every `z in V+AV` satisfies

\[
 |\xi(z)|\le(1+\lambda)X,\qquad
 |\eta(z)|\le(1+\lambda^{-1})Y.                            \tag{4}
\]

## 3. Constructing an exposed frequency

Choose `v_X,u_Y in V` with `xi(v_X)=X` and `eta(u_Y)=Y`, possible by central symmetry. Put

\[
 a=\xi(u_Y)/X,\qquad b=\eta(v_X)/Y.
\]

Choose `sigma in {+1,-1}` with `sigma(a+b)>=0` and define

\[
 L(z)=\xi(z)/X+\lambda\sigma\eta(z)/Y.                     \tag{5}
\]

The trial points `sigma*u_Y in V` and `B*v_X in BV` give

\[
 \max_{u\in V}L(u)+\max_{w\in V}L(Bw)
 \ge (\lambda+\sigma a)+(\lambda+\sigma b)
 =2\lambda+|a+b|\ge2\lambda>t+2.                          \tag{6}
\]

The last inequality is strict because `2*lambda-(t+2)=sqrt(t^2-4)-2>0` for `t>=3`.

Select `u` as the lexicographic maximizer of `(L(z),xi(z))` on `V`, and select `w` so that `Bw` is the lexicographic maximizer of `(L(z),xi(z))` on `BV`. The forms `L` and `xi` are independent, so both maximizers are unique. Put `v=s*w` and

\[
 k=u+Av=u+Bw.
\]

Then

\[
 L(k)>t+2.                                                \tag{7}
\]

**Unique decomposition.** If `k=u'+Av'` with `u',v' in V`, the lexicographic coordinate pairs of `u'` and `Av'` are bounded above by the two separately selected maxima, while their sum equals the sum of those maxima. Translation invariance of lexicographic order forces each summand to attain its maximum. Injectivity of `(L,xi)` gives `u'=u` and `Av'=Av`, hence `v'=v`.

## 4. Correct two-sided orbit escape

This is the load-bearing step. A weaker argument that tries to pull both rectangle coordinates back through the same time direction is invalid, because one eigencoordinate expands while the other contracts. The correct proof obtains a separate strict inequality for each direction directly from (7).

For every `z in V+AV`, (4) implies the signed upper bounds

\[
 \xi(z)\le(1+\lambda)X,
 \qquad \sigma\eta(z)\le(1+\lambda^{-1})Y.                \tag{8}
\]

First suppose

\[
 \xi(k)\le(1+\lambda^{-1})X.
\]

Using the second bound in (8),

\[
 L(k)\le(1+\lambda^{-1})
       +\lambda(1+\lambda^{-1})
       =\lambda+\lambda^{-1}+2=t+2,
\]

contradicting (7). Therefore

\[
 \xi(k)>(1+\lambda^{-1})X.                               \tag{9}
\]

For every `j>=1`, absolute eigenvalue scaling for `A=sB` gives

\[
 |\xi(A^jk)|=\lambda^j|\xi(k)|
 >\lambda(1+\lambda^{-1})X=(1+\lambda)X,
\]

which violates (4). Hence no positive iterate belongs to `V+AV`.

For the opposite direction, suppose

\[
 \sigma\eta(k)\le(\lambda^{-1}+\lambda^{-2})Y.
\]

Using the first bound in (8),

\[
 L(k)\le(1+\lambda)
       +\lambda(\lambda^{-1}+\lambda^{-2})
       =\lambda+\lambda^{-1}+2=t+2,
\]

again contradicting (7). Thus

\[
 |\eta(k)|\ge\sigma\eta(k)>
 (\lambda^{-1}+\lambda^{-2})Y.                           \tag{10}
\]

If `j<=-1`, then

\[
 |\eta(A^jk)|=\lambda^{-j}|\eta(k)|
 \ge\lambda|\eta(k)|
 >(1+\lambda^{-1})Y,
\]

again outside the rectangle (4). Therefore `A^j k notin V+AV` for every nonzero integer `j`, including negative-trace matrices.

## 5. The surviving coefficient cannot have zero determinant

Suppose `u=r*Av=r*Bw`, put `R=|r|`, and define

\[
 a_0=|\xi(w)|/X,\qquad b_0=|\eta(w)|/Y.
\]

Membership of `u,w` in `V` implies

\[
 a_0,b_0\le1,\qquad R\lambda a_0\le1,
 \qquad R\lambda^{-1}b_0\le1.
\]

For `R>0`,

\[
 |L(k)|\le(1+R)(\lambda a_0+b_0)
 \le(1+R)\{\min(\lambda,R^{-1})+\min(1,\lambda/R)\}
 \le\lambda+2+\lambda^{-1}=t+2.                          \tag{11}
\]

The last scalar inequality has three cases. For `R<=lambda^-1` the expression is `(1+R)(lambda+1)` and is maximal at `R=lambda^-1`. For `lambda^-1<=R<=lambda` it is `2+R+R^-1`, bounded by `t+2` because `(lambda-R)(lambda*R-1)>=0`. For `R>=lambda` it is `(1+R^-1)(lambda+1)` and is maximal at `R=lambda`. The case `R=0` is impossible because `u` is a nonzero support vector, but the weaker bound `lambda+1` would also suffice. This contradicts (7), so `det(u,Av) != 0`.

## 6. Completion and consequences

Equation (2), unique decomposition and the nonzero support coefficients yield

\[
 \widehat h_g(k)=-\pi\det(u,Av)\widehat g(u)\widehat g(v)\ne0.
\]

Its oriented orbit meets `V+AV` only at `k`, so its orbit sum equals this coefficient. The orbit of `-k` is distinct: `A^j k=-k` would force `-1` to be an eigenvalue of a nonzero power of a hyperbolic matrix, while `j=0` would force `k=0`. Since `h_g` is real, the two orbit sums have equal modulus. This proves (3).

**Corollary 2 (no polynomial or L2 coboundary).** The bracket `h_g` is not `f-C_A f` with finite Fourier support. Along a bilateral orbit a finite difference has zero total sum. It is not an `L^2` coboundary either: a single nonzero forcing coefficient on the isolated orbit would force a nonzero constant tail in the transfer function's Fourier coefficients, contradicting square summability.

**Corollary 3 (flat-amplitude coercivity).** Let `M=|V|` and suppose

\[
 |\widehat g(v)|\ge\alpha\|g-\widehat g(0)\|_2/\sqrt M
\]

for every `v in V`, with `alpha>0`. Since the nonzero determinant is an integer,

\[
 \Gamma_A(g)\ge\frac{2\pi^2\alpha^4}{M^2}
                   \|g-\widehat g(0)\|_2^4.               \tag{12}
\]

**Corollary 4 (every fixed Fourier box has positive minimum).** For `R>=1`, let `P_R` be the real mean-zero polynomials with max-norm frequency at most `R`. Then

\[
 c_R(A)=\inf_{g\in P_R\setminus\{0\}}
               \Gamma_A(g)/\|g\|_2^4>0.                  \tag{13}
\]

This follows from continuity on the compact unit sphere. Together with the Fourier-tail construction in `fourier_tail_locality.md`, for every fixed `s>1` one has constants `C_s,c_s>0` such that

\[
 0<c_R(A)\le C_s\exp(-c_sR^{1/s}).                        \tag{14}
\]

Thus finite-Fourier positivity is compatible with very fast loss of coercivity as bandwidth grows.

**Scope.** The proof uses a finite Fourier maximum. It does not prove positivity for every nonconstant analytic infinite-support observable. Smooth counterexamples in the return-word and separated-support notes remain valid. Classical variance positivity alone does not imply microscopic GOE/GUE statistics or Heisenberg-time quantum trace comparison.

## 7. Reproducibility

The maintained exact checks are

```sh
python computations/verification/extremal_resonance.py \
  --output build/verification/extremal.json \
  --replay build/verification/extremal.replay
cmake -S . -B build/cmake
cmake --build build/cmake --target extremal_resonance_replay
build/cmake/extremal_resonance_replay build/verification/extremal.replay
```

`computations/maintenance/verify_workspace.py` performs both a no-argument C++ self-test and, after the Python producer finishes, a separate packet replay. The Python and C++ implementations use exact integer/quadratic-field arithmetic; their finite coverage is regression evidence, not the continuum proof.

**Audit correction, 2026-09-07.** Section 4 was rewritten after a synchronization audit found that the earlier prose incorrectly propagated both eigencoordinate bounds through the same time direction. Equations (9) and (10) are the corrected two-sided escape argument. The theorem statement and exact witness checkers were unchanged.