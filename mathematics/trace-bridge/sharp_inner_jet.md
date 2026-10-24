# Sharp right-weighted jets of rational matrix inner functions

**Stable claim ID:** BGS-TRACE-054. **Status:** self-contained project proof, independently reconstructed internally, 8 October 2026. This strengthens the supplied manuscript Section 89.2 from 13/3 to the optimal universal leading constant 4/3. External priority is not established.

## Result

Let F(z)=zG(z), where G is an m by m rational function analytic on the closed unit disk (after removal of removable singularities) and unitary on its boundary. Set z=e^{iθ}, dμ=dθ/(2π), and T=F(z)* zF'(z). The following inequality holds:

\[
\boxed{\int\operatorname{Tr}(\dot T T^{-1}\dot T)\,d\mu
\le\frac13\int\operatorname{Tr}(T^3-T)\,d\mu.}
\]

Here `F(z)=zG(z)` is any square rational inner matrix function, `T=F* zF' >= I` on the circle, and `dmu=dtheta/(2pi)`. The proof uses finite Blaschke--Potapov factorization, one matrix weighted Cauchy inequality, an exact cubic increment, and the scalar Poisson identity. The noncommutative commutator terms are retained throughout and cancel only after taking the indicated traces.

It follows that

\[
\boxed{\int\|F''T^{-1/2}\|_F^2\,d\mu
\le\frac43\int\operatorname{Tr}T^3\,d\mu
-2\int\operatorname{Tr}T^2\,d\mu
+\frac23\int\operatorname{Tr}T\,d\mu.}
\]

The universal leading coefficient `4/3` is sharp in every matrix dimension. These statements do not identify a cavity law or prove BGS. No novelty claim is made here.

## 1. Weighted Cauchy with a singular positive weight

Let `A>0`, let `P` be an orthogonal projection, and let `p>0`. For arbitrary matrices `X,Y` with `PY=Y`,

\[
\|(A+pP)^{-1/2}(X+Y)\|_F^2
\le\|A^{-1/2}X\|_F^2+\frac1p\|Y\|_F^2.
\tag{1}
\]

For completeness, take the block row

\[
C=(A+pP)^{-1/2}[A^{1/2},\sqrt p\,P].
\]

Then `CC*=I`, so `C` is contractive on the block Frobenius space. Apply it to the block column `[A^{-1/2}X; p^{-1/2}Y]`; the support condition `PY=Y` gives the left side of (1). This is a genuine matrix inequality and requires no commutativity.

## 2. One appended inner factor

Suppose a partial inner product has delay `T_old`, and append on the right

\[
B(z)=I+(b_a(z)-1)P,
\]

where `P` is a constant orthogonal projection and `b_a` is a scalar Blaschke factor. Let `p=overline(b_a) z b_a'` be its positive Poisson kernel. Boundary differentiation with respect to `theta` gives

\[
\dot B=i pBP,\qquad \dot B^*=-i pPB^*.
\]

Put

\[
A=B^*T_{\rm old}B,\qquad C=B^*\dot T_{\rm old}B.
\]

Both `A` and `C` are Hermitian, and `A>=I`. The new delay and its derivative are exactly

\[
T=A+pP,\qquad
\dot T=C+i p(AP-PA)+p'P.
\tag{2}
\]

The crucial split retains the commutator but distributes its two terms asymmetrically:

\[
X=C+i pAP,\qquad Y=p'P-i pPA.
\tag{3}
\]

Then `X+Y=dot T` and `PY=Y`. Apply (1). Its first right term expands as

\[
\operatorname{Tr}(X^*A^{-1}X)
=\operatorname{Tr}(CA^{-1}C)+p^2\operatorname{Tr}(PA).
\]

The cross terms are `i p Tr(CP-PC)=0`. Its second term expands as

\[
\frac1p\operatorname{Tr}(Y^*Y)
=\frac{p'^2}{p}\operatorname{Tr}P+p\operatorname{Tr}(PA^2).
\]

The cross terms are `i p' Tr(AP-PA)=0`. Thus the precise pointwise induction inequality is

\[
\boxed{\operatorname{Tr}(\dot T T^{-1}\dot T)
\le\operatorname{Tr}(CA^{-1}C)
+p^2\operatorname{Tr}(PA)+p\operatorname{Tr}(PA^2)
+\frac{p'^2}{p}\operatorname{Tr}P.}
\tag{4}
\]

Unitary invariance gives

\[
\operatorname{Tr}(CA^{-1}C)
=\operatorname{Tr}(\dot T_{\rm old}T_{\rm old}^{-1}\dot T_{\rm old}).
\tag{5}
\]

## 3. Exact cubic increment and circle integration

Using `P^2=P` and cyclicity of the trace, without commuting `A` and `P`,

\[
\operatorname{Tr}[(A+pP)^3-A^3]
=3p\operatorname{Tr}(PA^2)+3p^2\operatorname{Tr}(PA)+p^3\operatorname{Tr}P.
\tag{6}
\]

Also `Tr(T-A)=p Tr P`. Hence

\[
\frac13\operatorname{Tr}[(T^3-T)-(A^3-A)]
=p\operatorname{Tr}(PA^2)+p^2\operatorname{Tr}(PA)
+\frac{p^3-p}{3}\operatorname{Tr}P.
\tag{7}
\]

The exact scalar Poisson identity is

\[
\int\frac{p'^2}{p}\,d\mu
=\frac13\left(\int p^3\,d\mu-1\right)
=\frac13\int(p^3-p)\,d\mu,
\tag{8}
\]

since `int p=1`. Equations (4)--(8) prove that the quantity

\[
\Phi(T)=\int\operatorname{Tr}(\dot T T^{-1}\dot T)\,d\mu
-\frac13\int\operatorname{Tr}(T^3-T)\,d\mu
\]

cannot increase when an inner factor is appended.

Every square rational inner `G` has a finite Blaschke--Potapov product, up to constant unitary factors. Begin with `F_0(z)=zU`, which has `T_0=I`, `dot T_0=0`, and `Phi(T_0)=0`. Append its finitely many factors. Constant unitary factors only conjugate the delay and preserve all traces. This establishes `Phi(T)<=0` for `F=zG`.

There is no unresolved matrix inequality in this argument. The finite factorization and (8) are the standard exact inputs; the cascade estimate above supplies the missing noncommutative step.

## 4. Right-weighted jet and sharpness

The exact boundary identity is

\[
F^*z^2F''=T^2-T-i\dot T.
\]

For the required right weight,

\[
\|F''T^{-1/2}\|_F^2
=\operatorname{Tr}(T^3-2T^2+T)
+\operatorname{Tr}(\dot T T^{-1}\dot T).
\]

The cross trace vanishes because `T^{-1}` commutes with `T^2-T`, followed by cyclicity; no commutation with `dot T` is assumed. The integrated derivative inequality therefore gives the displayed `4/3` refinement.

For fixed matrix dimension `m`, take

\[
F_r(z)=\operatorname{diag}(z b_r(z),z,\ldots,z),\qquad r\uparrow1.
\]

The first component is the scalar sharp family. The other components contribute zero to the second jet and only `m-1` to `int Tr T^3`. Thus the ratio of the integrated right-weighted second jet to `int Tr T^3` tends to `4/3`. The leading constant is universally sharp for the full matrix class as well.

## 2. Optimality of 4/3

Take F_r(z)=z b_r(z), 0<r<1, T=1+p_r. The exact Poisson moments are

$$M_2=\int p_r^2d\mu=\frac{1+r^2}{1-r^2},\qquad
M_3=\int p_r^3d\mu=\frac{1+4r^2+r^4}{(1-r^2)^2}.$$

The loss incurred by the extra 1 in T obeys

$$0\le\int\frac{(p_r')^2}{p_r}d\mu-
\int\frac{(p_r')^2}{1+p_r}d\mu
\le\int\left(\frac{p_r'}{p_r}\right)^2d\mu
=\frac{2r^2}{1-r^2}=M_2-1.$$

The last identity follows either by integration or the Fourier series of log p_r. Thus, writing J_r=integral |F_r''|²/T,

$$\frac43M_3+\frac23\le J_r\le\frac43M_3+M_2-\frac13,\qquad
\int T^3d\mu=M_3+3M_2+4.$$

Since M_2/M_3→0 as r↑1, their ratio tends to 4/3. No smaller leading constant works universally.


## 5. Limited numerical orientation check

As a check on (2)--(4), 1800 independently generated tuples with dimensions 1 through 6, `A=I+G*G`, arbitrary Hermitian `C`, random rank-one `P`, positive `p`, and real `p'` all satisfied (4); the smallest computed right-minus-left gap was approximately `0.41195`. This check is not the proof. The proof is the block-row contraction and exact trace expansions above.

## 6. Smooth localization: the exact correction also closes

Let `omega>=0` be a real `C^2` periodic scalar function. The exact pointwise Poisson identity is stronger than its unweighted integral:

\[
\frac{p'^2}{p}=\frac{p^3-p}{3}+\frac23p''.
\tag{9}
\]

One direct verification sets `alpha=(1+r^2)/(1-r^2)` and uses

\[
\frac{p'^2}{p}=-p^3+2\alpha p^2-p,
\qquad p''=-2p^3+3\alpha p^2-p.
\]

The same identities include `r=0`, where `p=1`. Integrating (9) against `omega` and integrating by parts twice gives

\[
\int\omega\frac{p'^2}{p}\,d\mu
=\frac13\int\omega(p^3-p)\,d\mu
+\frac23\int\omega''p\,d\mu.
\tag{10}
\]

Multiply the pointwise cascade inequality (4) by `omega`. Nonnegativity of `omega` preserves its direction. Combine (7) and (10). Since pointwise `Tr A=Tr T_old` and `Tr(T-A)=p Tr P`, the quantity

\[
\Phi_\omega(T)=\int\omega\operatorname{Tr}(\dot T T^{-1}\dot T)\,d\mu
-\frac13\int\omega\operatorname{Tr}(T^3-T)\,d\mu
-\frac23\int\omega''\operatorname{Tr}T\,d\mu
\]

cannot increase through the cascade. At the base `T=I`, it is zero because `int omega''=0`. Thus

\[
\boxed{\int\omega\operatorname{Tr}(\dot T T^{-1}\dot T)\,d\mu
\le\frac13\int\omega\operatorname{Tr}(T^3-T)\,d\mu
+\frac23\int\omega''\operatorname{Tr}T\,d\mu.}
\]

The exact right-weighted jet identity yields

\[
\boxed{\int\omega\|F''T^{-1/2}\|_F^2\,d\mu
\le\frac43\int\omega\operatorname{Tr}T^3\,d\mu
-2\int\omega\operatorname{Tr}T^2\,d\mu
+\frac23\int\omega\operatorname{Tr}T\,d\mu
+\frac23\int\omega''\operatorname{Tr}T\,d\mu.}
\]

The `omega''` correction is exact for the cascade argument. Dropping it for an arbitrary nonconstant weight is not justified. Neither a nonsmooth stopping indicator nor an arbitrary event can be inserted into the unweighted theorem without controlling this correction through an admissible smooth localization.

## 7. Separate adversarial checklist

1. **Factorization scope.** The input must be square, finite-degree rational inner and analytic in the disk. Finite Blaschke--Potapov factorization applies. This argument does not automatically cover arbitrary nonrational inner functions or poles/atoms on the boundary.
2. **Factor multiplication side.** Factors are appended on the right. Accordingly `A=B*T_old B` and the commutator is `+i p(AP-PA)`. The proof is sensitive to these orientations; reversing just one would invalidate the cancellation.
3. **Right weight.** The jet is the complex derivative `F''`, multiplied on the right by `T^{-1/2}`. The exact norm expansion uses `F* z^2F''`; it does not replace this right weight by a left weight involving the same `T`.
4. **Constant unitary base.** Start with `F_0=zU`, giving `T_0=I` exactly. Additional constant unitary factors act by unitary conjugation and preserve every trace and energy used in the induction.
5. **Invertibility.** Every old delay is at least `I`, and conjugation preserves this. Thus `A^{-1}` exists. The new weight `pP` may be singular, but the block-row proof requires only `PY=Y`, which is satisfied exactly by `Y=p'P-i pPA`.
6. **Projection rank and degeneracy.** Rank-one factors suffice, but the proof holds for arbitrary orthogonal projection rank. It uses only `P=P*=P^2`; no choice of eigenbasis or simple spectrum is needed. The rank enters only as `Tr P`.
7. **Noncommutativity.** Neither `A` nor `C` needs to commute with `P`. Cross terms vanish after taking the trace, and the cubic increment follows by cyclicity. They were not silently discarded as matrices.
8. **Integration.** Scalar Poisson identity (9) is pointwise and its circle integration is exact. For localization, `omega>=0` and periodic `C^2` are used explicitly, with the full `omega''` term retained.
9. **Sharpness scope.** Scalar embedding proves optimality of the universal leading `4/3` constant in the matrix class. It does not claim that every noncommuting family saturates the inequality, or that every lower-order coefficient is independently optimal.
10. **Research implication.** This closes the proposed sharper matrix jet inequality. It strengthens the analytic delay/jet estimate; it does not settle the microscopic scalar cavity law, deterministic quantum-chaos universality, or the full BGS conjecture.

## 8. Self-contained finite factorization

The finite-factorization input can be reconstructed by successive right division. The scalar determinant of a square rational inner `G` is a finite scalar Blaschke product. If it has a zero `a` in the disk, choose a unit vector `v` in `ker G(a)`, set `P=vv*`, and use `B=I+(b_a-1)P`. Then `H=G B^{-1}` is analytic at `a`, because `G(z)v` vanishes there and cancels the factor `(z-a)^{-1}` in `b_a^{-1}`. It is rational inner on the circle and `det H=det G/b_a`, lowering determinant degree by one. Repetition produces a constant residual and a finite product of right factors. Multiple kernel dimensions and multiple zeros are handled by repeated single-vector division.

For completeness, a zero-free scalar rational inner determinant is a unimodular constant. In that case both `G` and `G^{-1}` are analytic in the disk and have unitary boundary values, so both are contractions there by the maximum principle. Their singular values must consequently all equal one in the disk. A holomorphic matrix function with unitary values on the open disk is constant. Thus the terminal residual is indeed a constant unitary. Rational-inner boundary singularities are removable; no actual boundary poles are admitted in this finite inner class.

## Verification and application boundary

[Source and overlap review](../../literature/phase_channel_jet_sources_20261008.md), [maintained numerical verifier](../../computations/verification/phase_channel_jet.py), and [independent audit](../../archive/evidence/executions/20261008/phase-channel-jet/matrix_review.md) record their exact scopes. Lean certifies coefficient elimination only; all analytic arguments above remain informal proofs. No arbitrary left weight, nonrational limiting class, free event localization, source-covariance estimate or CUE law follows without additional hypotheses. The localization correction is controlled by (2/3) integral (ω'')_+ Tr T if a positive upper bound is desired.
