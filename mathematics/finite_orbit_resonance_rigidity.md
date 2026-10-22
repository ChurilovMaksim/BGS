# Smooth resonance rigidity on finitely many hyperbolic Fourier orbits

Stable claim ID: `BGS-RES-004`.

Date: 22 September 2026. Repository: `ChurilovMaksim/BGS`.

Base revision: `39d4e01ae6a6b3eb472ab30266b708ca71a70a16` (`main`).

**Status:** project proof with adversarial checking by the author and separate
finite exact regressions. Not independently refereed, not Lean-certified,
and no external priority or BGS solution is claimed. The finite-Fourier
independence theorem and common real all-pass invariance are existing
repository inputs. The extension here treats any finite union of infinite
signed frequency orbits, with arbitrary phases, using smoothness alone.

## 1. Contract

Let \(A\in\mathrm{SL}(2,\mathbb Z)\) be hyperbolic, and let \(Cf(x)=f(A^{\mathsf T}x)\) on the
two-dimensional torus with normalized Lebesgue measure. Write

\[
 e_k(x)=e^{2\pi i k\cdot x},\quad
 h_r(g)=\frac{\{g,C^r g\}}{4\pi},\qquad
 \{f,h\}=f_{x_1}h_{x_2}-f_{x_2}h_{x_1}.
\]

Oriented orbits are \(A^{\mathbb Z}k\); signed orbits also identify \(k\) and \(-k\). These notions
must not be interchanged in the variance. For a smooth mean-zero \(f\), put

\[
 \mathcal V_A(f)=\sum_{\mathcal O}
  \left|\sum_{k\in\mathcal O}\widehat f(k)\right|^2.
\tag{FO.1}
\]

**Theorem 1.** Let \(g\) be a nonconstant real \(C^\infty\) function whose nonzero
Fourier support is contained in finitely many signed \(A\)-orbits. Then, for
every \(R\ge1\) and every nonzero real vector \((a_1,\ldots,a_R)\),

\[
 \boxed{\mathcal V_A\!\left(\sum_{r=1}^R a_rh_r(g)\right)>0.}
\tag{FO.2}
\]

Consequently the classes \([h_r(g)]\), \(r\ge1\), are linearly independent modulo \(L^2\)
\(C\)-coboundaries. In particular \(\Gamma_A(g)=\mathcal V_A(h_1(g))>0\). Complex linear
independence follows by separating real and imaginary parts.

There is no restriction on the number of coefficients on each orbit, their
phases, the sign of \(\operatorname{tr}A\), or an analytic strip width. No uniform positive
lower bound over all \(g\) or all orbit families is asserted. Constants in \(g\) do
not affect the conclusion and will be subtracted.

## 2. Variance and coboundaries

For a smooth mean-zero \(f\), absolute Fourier summability gives

\[
 \sum_{q\in\mathbb Z}\sum_{k\ne0}
 |\widehat f(k)\widehat f(A^qk)|
 \le \left(\sum_{k\ne0}|\widehat f(k)|\right)^2<\infty.
\]

A hyperbolic \(A\) has no periodic nonzero integer frequency, so each ordered
pair on one orbit occurs once. Fourier orthogonality and Cesaro summation give

\[
 \mathcal V_A(f)=\lim_{n\to\infty}\frac1n
       \left\|\sum_{j=0}^{n-1}C^jf\right\|_2^2.
\tag{FO.3}
\]

If \(f=u-Cu\) with \(u\in L^2\), its equation on an orbit is \(f_j=u_j-u_{j-1}\).
Square summability makes \(u_j\) tend to zero at both ends; the absolutely
convergent sum of \(f_j\) is zero. A nonzero orbit sum therefore excludes an
\(L^2\) coboundary. Equation (FO.2) is stronger than pointwise nonvanishing.

## 3. Eventual separation of every pair channel

Choose \(v_1,\ldots,v_d\in\mathbb Z^2\setminus\{0\}\), distinct modulo signed
\(A\)-orbits, and define

\[
 \mathcal S=\bigcup_{i=1}^d\{\pm A^jv_i:j\in\mathbb Z\}.
\]

**Lemma 2 (large-gap separation).** There exists \(n_0\), depending on \(A\) and this
finite list, such that the following holds. If \(n>n_0\), \(i,j\) are any indices,
\(\epsilon\in\{+1,-1\}\), and

\[
 v_i+\epsilon A^n v_j
       =\zeta A^t(v_k+\delta A^m v_l),
 \quad m\ge0,\quad t\in\mathbb Z,
 \quad\delta,\zeta\in\{+1,-1\},
\tag{FO.4}
\]

then \(i=k\), \(j=l\), \(m=n\), \(t=0\), \(\zeta=1\), and \(\delta=\epsilon\). Also
\(D_{ij}(n)=\det(v_i,A^n v_j)\ne0\) for every \(n>n_0\).

Every sum of two elements of \(\mathcal S\) can be put in the right-hand form by a
common signed iterate and an interchange. Thus the statement covers all
input exponents, without a guessed finite time cutoff.

**Proof.** Put \(s=\operatorname{sign}(\operatorname{tr}A)\), \(B=sA\), and let \(\lambda>1\) be the expanding
eigenvalue of \(B\). Choose independent real eigen-covectors \(\xi,\eta\) with factors
\(\lambda\) and \(\lambda^{-1}\). Neither vanishes on a nonzero integer vector: a
rational invariant line of an integral unimodular hyperbolic matrix would
give a rational algebraic-unit eigenvalue, necessarily \(\pm1\).

The quadratic form \(Q(z)=\xi(z)\eta(z)\) obeys \(Q(Az)=Q(z)\). For fixed
nonzero integer vectors \(u,v\),

\[
 Q(u+\epsilon A^n v)=Q(u)+Q(v)+\epsilon s^n
    \{\eta(u)\xi(v)\lambda^n+\xi(u)\eta(v)\lambda^{-n}\}.
\tag{FO.5}
\]

The leading coefficient is nonzero. Its absolute value is therefore bounded
above and below by positive multiples of \(\lambda^n\) for sufficiently large \(n\).

Suppose (FO.4) has nontrivial solutions with unbounded \(n\). Pass to a subsequence
with fixed \(i,j,k,l,\epsilon,\delta,\zeta\). Applying \(Q\) to (FO.4) removes \(t\). Formula
(FO.5) forces \(m\to\infty\) and makes \(m-n\) a bounded integer. Pass
to a subsequence with \(m=n+b\), with \(b\) fixed. Applying \(\xi\) and taking absolute values
in (FO.4) gives

\[
 \lambda^t=
 \frac{|\xi(v_i+\epsilon A^n v_j)|}
 {|\xi(v_k+\delta A^{n+b}v_l)|}.
\tag{FO.6}
\]

The numerator is comparable to \(\lambda^n\) and the denominator to \(\lambda^{n+b}\).
Thus \(t\) is also a bounded integer; pass to a subsequence with \(t\) fixed. Now
(FO.4) becomes the exact vector equation

\[
 v_i-\zeta A^t v_k
   =A^n(\zeta\delta A^{b+t}v_l-\epsilon v_j).
\tag{FO.7}
\]

Both parenthesized vectors are fixed integer vectors, even when \(b+t<0\),
since \(A\) is unimodular. If the right parenthesis were nonzero,
its expanding covector would be nonzero and the right side would be
unbounded as \(n\to\infty\). Thus both sides vanish. The first equality
and the distinct signed-orbit representatives imply \(i=k\). Then
\(v_i=\zeta A^t v_i\) forces \(t=0\) and \(\zeta=1\) by hyperbolicity. The second equality
implies \(j=l\), \(b=0\), and \(\delta=\epsilon\). This is exactly the trivial solution,
contradicting the choice of nontrivial solutions. Finitely many index and
sign choices make the upper bound \(n_0\) uniform over this fixed list.

Finally \(\det(u,A^n v)\) is a nonzero multiple of
\(s^n[\xi(u)\eta(v)\lambda^{-n}-\eta(u)\xi(v)\lambda^n]\). Its leading coefficient
is nonzero, so it cannot vanish for arbitrarily large \(n\). Increase \(n_0\) for
the finitely many pairs. This proves the lemma for either trace sign.

**Caution.** Equality of \(Q\) alone is not a criterion for orbit equivalence.
Equation (FO.7), not just comparison of quadratic invariants, is essential.

## 4. Vanishing variance forces polynomial pair products

Write, omitting empty orbit families,

\[
 g=\sum_{i=1}^d\sum_{j\in\mathbb Z}
   (c_{i,j}e_{A^jv_i}+\overline{c_{i,j}}e_{-A^jv_i}),
 \quad
 P_i(z)=\sum_{j\in\mathbb Z}c_{i,j}z^j.
\tag{FO.8}
\]

Smoothness implies every exponential moment: for every \(L>0\),
\(\sum_j|c_{i,j}|e^{L|j|}<\infty\). Indeed \(|A^jv_i|\) is bounded below by a
positive multiple of \(\lambda^{|j|}\), and smooth Fourier coefficients decay
faster than every inverse power. Thus each nonzero \(P_i\) is holomorphic on
\(\mathbb C^*=\mathbb C\setminus\{0\}\).

Introduce the two different correlations

\[
 S_{ij}(n)=\sum_t c_{i,t}c_{j,t+n},\qquad
 K_{ij}(n)=\sum_t c_{i,t}\overline{c_{j,t+n}}.
\tag{FO.9}
\]

For \(n>n_0\), Lemma 2 and direct Fourier differentiation give

\[
 \begin{split}
 J_{A^{\mathbb Z}(v_i+A^nv_j)}(h_r)
   &=-\pi D_{ij}(n)[S_{ij}(n-r)-S_{ij}(n+r)],\\
 J_{A^{\mathbb Z}(v_i-A^nv_j)}(h_r)
   &= \pi D_{ij}(n)[K_{ij}(n-r)-K_{ij}(n+r)].
 \end{split}
\tag{FO.10}
\]

For the second row, the two ordered input pairs contribute
\[
 +\pi D_{ij}(n)c_{i,t}\overline{c_{j,t+n-r}},\qquad
 -\pi D_{ij}(n)\overline{c_{j,t+n}}c_{i,t-r}.
\]
Summing over \(t\) proves the formula. The
first row is the same computation without conjugation and with the opposite
sign. Lemma 2 excludes any additional input families or gap values.
All rearrangements are justified by smooth weighted Fourier summability.

Assume, for contradiction, that the variance in (FO.2) is zero for a nonzero
real vector \(a\). Every orbit sum of the combination is zero. For \(X=S\) and
\(X=K\), and every \(i,j\), (FO.10) implies

\[
 B_{ij}^{X}(n):=\sum_{r=1}^R a_r[X_{ij}(n-r)-X_{ij}(n+r)]=0
       \quad(n>n_0).
\tag{FO.11}
\]

The symmetries \(S_{ij}(-n)=S_{ji}(n)\) and \(K_{ij}(-n)=\overline{K_{ji}(n)}\) also make
\(B_{ij}\) vanish for all sufficiently negative \(n\). Hence all these \(B\) sequences
are finitely supported.

Put \(P^*(z)=\overline{P(1/\bar z)}\) and
\(L_a(z)=\sum_{r=1}^R a_r(z^{-r}-z^r)\), a nonzero Laurent polynomial.
The generating identities are

\[
 \begin{split}
 P_i(z)P_j(1/z)&=\sum_n S_{ij}(n)z^{-n},\\
 P_i(z)P_j^*(z)&=\sum_n K_{ij}(n)z^{-n}.
 \end{split}
\tag{FO.12}
\]

Multiplication by \(L_a\) produces the finite Laurent series \(B\) in (FO.11). Thus
each product in (FO.12) is rational and holomorphic on \(\mathbb C^*\). It is consequently
a Laurent polynomial. Both kinds of product are required: Hermitian
products alone would not force the common factor below to have real
Laurent coefficients.

## 5. A common real all-pass factor

**Lemma 3 (pair-product factorization).** Suppose nonzero functions \(P_1,\ldots,P_d\)
are holomorphic on \(\mathbb C^*\), and all \(P_i(z)P_j(1/z)\) and \(P_iP_j^*\) are Laurent
polynomials. Then

\[
 P_i(z)=R(z)Q_i(z),
\tag{FO.13}
\]

where every \(Q_i\) is a Laurent polynomial (complex coefficients allowed),
\(R\) is holomorphic and zero-free on \(\mathbb C^*\), has real Laurent coefficients, and

\[
 R(z)R(1/z)=R(z)R^*(z)=1.
\tag{FO.14}
\]

**Proof.** The ratios \(P_i/P_1\) are rational, by dividing \(P_i(z)P_1(1/z)\) by
\(P_1(z)P_1(1/z)\). Clear denominators and divide the resulting polynomial vector
by its common divisor. This gives Laurent polynomials \(q_i\) with greatest
common divisor \(1\) and a meromorphic \(F\) with \(P_i=Fq_i\). Bezout polynomials \(b_i\)
satisfy \(\sum_i b_iq_i=1\), so \(F=\sum_i b_iP_i\) is holomorphic on \(\mathbb C^*\).

The zeros of \(F\) form a finite set with finite multiplicities: they are zeros
of the nonzero Laurent polynomial \(P_1P_1^*\). Divide \(F\) by the ordinary
polynomial formed from these zeros, and multiply every \(q_i\) by that
polynomial. The resulting \(F_0\) is holomorphic and zero-free on \(\mathbb C^*\).

Using a nonzero \(q_i\), both \(F_0(z)F_0(1/z)\)
and \(F_0(z)F_0^*(z)\) are rational. They are holomorphic and zero-free on \(\mathbb C^*\),
so each is a nonzero constant times an integer power of \(z\). The first is
unchanged by \(z\mapsto1/z\) and is therefore a constant \(c\). The second is strictly
positive on the unit circle, so its integer power is zero; it is a
positive constant \(d\). Evaluation at \(z=1\) gives
\(c=F_0(1)^2\) and \(d=|F_0(1)|^2\).

Normalize \(R=F_0/F_0(1)\), absorbing \(F_0(1)\) into the polynomial factors. This
gives (FO.14). Dividing the two identities gives \(R(1/z)=R^*(z)\), or
\(R(w)=\overline{R(\bar w)}\). Hence its Laurent coefficients are real.
This proves the lemma. Notice that \(R\) need not be a monomial: smoothness
allows nontrivial entire all-pass filters.

## 6. Reduce to the existing finite-Fourier theorem

Apply Lemma 3 to (FO.12). Expand \(R(z)=\sum_j p_jz^j\). Its real Laurent
coefficients have every exponential moment, by Cauchy estimates on
arbitrarily large and small circles. Define the real trigonometric polynomial
\(q\) by placing the coefficients of \(Q_i\) along \(A^{\mathbb Z}v_i\) and their complex
conjugates along the distinct negative orbits. Then

\[
 g=T_Rq:=\sum_{j\in\mathbb Z}p_j C^j q.
\tag{FO.15}
\]

This follows coefficient by coefficient from (FO.13). The sum converges in
every smooth seminorm. The polynomial \(q\) is nonconstant since \(g\) is.

For completeness, the needed all-pass invariance is elementary here.
Define \(h_s(q)\) also for negative \(s\), and set \(h_0=0\). Symplectic invariance gives

\[
 h_r(T_Rq)=\sum_{i,j}p_i p_j C^i h_{r+j-i}(q).
\]

The Fourier \(\ell^1\) norm of \(h_s(q)\) grows at most exponentially in \(|s|\), whereas
the \(p_j\) have every exponential moment. All sums converge absolutely,
and orbit summation commutes with rearrangement. Since \(J(C^if)=J(f)\) and
\(R(z)R(1/z)=1\) implies \(\sum_i p_ip_{i+n}=\delta_{n,0}\),

\[
 \boxed{J(h_r(g))=J(h_r(q))\quad\text{for every }r.}
\tag{FO.16}
\]

This is the existing common real entire-all-pass invariance mechanism.
The existing finite-Fourier all-lag theorem, applied to the nonconstant real
polynomial \(q\), now contradicts the assumed zero variance of the nonzero
combination in (FO.2). This proves Theorem 1.

The internal finite-Fourier input is pinned at the base revision:
`manuscript/unified_sections/temporal_resonance.tex`, isolated highest-lag
frequency lemma and independence theorem. Its \(r=1\) version is also in
`mathematics/extremal_resonance_nondegeneracy.md`. The earlier all-pass
invariance theorem is in `mathematics/entire_temporal_gauge.md`.
The large-gap separation mechanism is also already used in
`mathematics/phase_regularized_resonance.md`, Section 2. Lemma 2 gives an
alternative qualitative proof; it is not a priority claim for this mechanism.
The contribution here is the smooth finite-orbit extension and the common
factor normal form, relative to these inspected inputs.

## 7. Two additional consequences and a sharp boundary of this route

**Finite invariant range.** Write \(q_A(k)=\det(k,Ak)\ne0\) for
\(k\in\mathbb Z^2\setminus\{0\}\). For each finite \(H\), the set
\(\{k:0<|q_A(k)|\le H\}\) is a finite union of signed \(A\)-orbits. Indeed \(q_A\) is a
nonzero constant multiple of \(\xi(k)\eta(k)\). Choose an iterate on each orbit
with \(1\le|\xi(k)|/|\eta(k)|<\lambda^2\). A bound on the product bounds both
coordinates and hence the Euclidean norm. Only finitely many integer
representatives remain.

The theorem applies to every smooth nonconstant \(g\) whose Fourier
support has bounded \(|q_A(k)|\). Any smooth, and in particular any analytic,
zero-variance counterexample must occupy infinitely many signed orbits and
have unbounded \(|q_A(k)|\) on its Fourier support.

**Finite-tail normal form.** The proof also shows: if for one nonzero finite
real temporal coefficient vector all sufficiently large same-sign and
opposite-sign pair-channel sums vanish, then \(g=T_Rq\), with \(q\) a real Fourier
polynomial and \(R\) a common real entire all-pass filter. Conversely this form
has finite tails in all these pair-channel sums, by (FO.12)--(FO.14). This is a
normal form for eventual pair-channel cancellation, not for zero variance.

**No uniform isolation over arbitrary families.** For any \(n\) and \(v\ne0\),

\[
 v-A^n v=2v+(-v-A^n v).
\tag{FO.17}
\]

With positive trace and \(n\) growing, the added vectors \(-v-A^nv\) have distinct
invariant values \(q_A(v)(2+\operatorname{tr}A^n)\). Thus arbitrarily late new-family
collisions can be introduced. There is no family-independent \(n_0\). A countable
union can have infinitely many such late collisions, even if its Fourier
coefficients are chosen to decay analytically. This exhibits failure of the
isolation argument, not a zero-variance analytic counterexample.

## 8. Remaining obligations

The theorem does not treat arbitrary analytic observables with infinitely
many signed Fourier orbits. No limiting passage through orbit truncations is
provided: positivity without a uniform quantitative lower bound is insufficient.
The finite-tail characterization does not assert that general smooth \(g\) has
finite tails; that was a consequence of a hypothetical zero combination.

This result is classical cohomological nondegeneracy. It proves no
Heisenberg-time joint-trace or mixed-resolvent cancellation for the frozen
quantum map. It does not imply GOE, GUE, COE, CUE, or microscopic BGS.
External priority is unestablished. Independent review should focus on
Lemma 2, both channel identities in (FO.10), and the reality step in Lemma 3.
