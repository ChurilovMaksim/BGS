# Short-time limits of the diagonal-phase form factor

**Claim ID:** `BGS-TRACE-128`.
**Status:** project proof. The occupation calculus, the dihedral main term, and the exponential-sum bounds are proved below. Python and C++ recompute the occupation sums in floating point and check the stated inequalities, including at \(N=3,5,7\). Lean decides integer comparisons only: the symmetric error constants, the time-three gap against the main term, the integer main terms at \(N=3,5,7\), and the Kloosterman quadruple count at the primes \(5\) and \(7\). It does not sum the complex form factor. No external referee.

`BGS-TRACE-127` is the exact evaluation at times one, two and three for \(DM_N\), and it is the source of the occupation expansion. The trace-closure lemma of `BGS-TRACE-126` is not used. The ensemble and the bucket calculus are those of Tanner and of Pakoński–Życzkowski–Kuś, as cited in `BGS-TRACE-127`; the new content is the cat-map main term and the inversion comparison. `BGS-TRACE-005` and `BGS-BGS-001` remain **open**.

## 1. Statements

Let \(N\ge 3\) be odd and let \(M_N\) be the cat-map quantization, with every entry of modulus \(N^{-1/2}\) and with \(M_N\) symmetric. Let \(D\) be diagonal with independent uniform phases and let \(U_N=DM_N\). Write \(P(N,m)=N(N-1)\cdots(N-m+1)\) for \(m\le N\), and \(P(N,m)=0\) for \(m>N\). Write \(\log\) for the natural logarithm.

**Theorem 1 (orthogonal short-time limit).** For \(m=1\), \(\mathbb E\lvert\operatorname{Tr} U_N\rvert^2=1\). For \(m=2\), \(\mathbb E\lvert\operatorname{Tr} U_N^2\rvert^2=(2N-1)/N\). For every integer \(m\ge 3\),
\[
\Bigl\lvert\mathbb E\lvert\operatorname{Tr} U_N^m\rvert^2
-2m\,\frac{P(N,m)}{N^m}\Bigr\rvert
\le\frac{m!\,(1+m(m-1))}{N}.
\]
In particular, for each fixed \(m\ge 3\),
\[
\lim_{\substack{N\to\infty\\N\text{ odd}}}\mathbb E\lvert\operatorname{Tr} U_N^m\rvert^2=2m.
\]
The same bound gives the limit along varying times: if \(m(N)\ge 3\), if \(m(N)!(1+m(N)(m(N)-1))=o(N)\), and if \(m(N)^2=o(N)\), then the ratio of the expectation to \(2m(N)\) tends to \(1\). Since \(m!\le m^m\), every sequence \(m\le c\log N/\log\log N\) with a fixed \(c<1\) lies in this range for all large \(N\). The estimate does not reach \(m\le N^{\alpha}\) for a fixed \(\alpha>0\).

Let \(p\) be an odd prime and let \(\pi\) be the permutation of \(\mathbb Z/p\mathbb Z\) with \(\pi(0)=0\) and \(\pi(x)=x^{-1}\) for \(x\ne 0\). Let \(W_p\) be the unitary matrix \((W_p)_{xy}=(M_p)_{\pi(x),y}\), and let \(V_p=DW_p\).

**Theorem 2 (broken reversal, prime dimensions).** The matrix \(W_p\) is flat. It is unitary because it is a row permutation of \(M_p\), whose unitarity is the cat-map quantization of the model and is not re-proved here. For \(p=3\), \(\pi\) is the identity, so \(V_3\) has the same law as \(U_3\). For every odd prime \(p\) and every integer \(m\ge 3\),
\[
\Bigl\lvert\mathbb E\lvert\operatorname{Tr} V_p^m\rvert^2
-m\,\frac{P(p,m)}{p^m}\Bigr\rvert
\le m!\,\Bigl(3^{1/4}p^{-1/4}+\frac{m(m-1)+2}{p}\Bigr).
\]
For each fixed \(m\ge 1\),
\[
\lim_{p\to\infty}\mathbb E\lvert\operatorname{Tr} V_p^m\rvert^2=m,
\]
where the cases \(m=1\) and \(m=2\) are the flat-matrix identities of `BGS-TRACE-127` and do not use \(\pi\). If \(m(p)\ge 3\), if the right-hand side of the inequality tends to \(0\), and if \(m(p)^2=o(p)\), then the ratio of the expectation to \(m(p)\) tends to \(1\). Every sequence \(m\le c\log p/\log\log p\) with a fixed \(c<1/4\) lies in this range for all large \(p\). The estimate does not reach \(m\le p^{\alpha}\) for a fixed \(\alpha>0\).

**Boundary.** Both ensembles use independent phases at the sites. Neither is the sixteen-phase kick of `BGS-TRACE-126`, and neither is the fixed propagator at \(\tau=10^{-80}\). Theorem 1 uses the antiunitary \(\Theta=DK_0\) of `BGS-TRACE-127`. The limit \(2m\) is the short-time value coming from reversal doubling. The orthogonal-class name is the heuristic for that antiunitary, and the measure is not Haar measure on the circular orthogonal ensemble. Theorem 2 breaks that reversal by the inversion permutation. Its limit \(m\) is the short-time value associated with no reversal. A second independent diagonal does not break the reversal: conjugating with \(D_2\) gives \(D_2(D_1M_ND_2)D_2^{-1}=(D_2D_1)M_N\), so the spectrum is the spectrum of Theorem 1. The error constants are large enough for the limits and are not sharp. No Heisenberg-scale statement \(m\asymp N\) is proved. `BGS-TRACE-005` and `BGS-BGS-001` remain open.

## 2. Buckets, symmetry, and a bilinear Gauss sum

The occupation expansion of `BGS-TRACE-127`, Section 2, gives
\[
\mathbb E\lvert\operatorname{Tr}(DW)^m\rvert^2
=\sum_n\Bigl\lvert\sum_{x:\,n_x=n}A(x)\Bigr\rvert^2
\]
for any matrix \(W\), with \(A(x)=\prod_{t=0}^{m-1}W_{x_t x_{t+1}}\) and with \(x_m=x_0\). If every entry of \(W\) has modulus \(N^{-1/2}\), then \(\lvert A(x)\rvert=N^{-m/2}\). Equivalently,
\[
\mathbb E\lvert\operatorname{Tr}(DW)^m\rvert^2
=\sum_{x,y:\,n_x=n_y}A(x)\overline{A(y)}.
\]

A word with a repeated site is non-injective. There are at most \(\binom{m}{2}N^{m-1}\) such words: each pair of positions may collide and the remaining positions are free, and the union bound overcounts. A fixed occupation is realized by at most \(m!\) words. The contribution \(Y\) of every pair in which the first word is non-injective therefore satisfies
\[
\lvert Y\rvert\le m!\binom{m}{2}N^{-1}=\frac{m!\,m(m-1)}{2N}.
\]
An injective word and a non-injective word have different occupations, so they never share a bucket.

**Lemma (bilinear sum).** Let \(N\) be odd and let \(Q\) be a polynomial on \((\mathbb Z/N\mathbb Z)^m\) of the form
\[
Q(x)=c\,x_i x_j+x_i L_i+x_j L_j+R,
\]
where \(i\ne j\), \(\gcd(c,N)=1\), the forms \(L_i\) and \(L_j\) do not depend on \(x_i\) or \(x_j\), and \(R\) does not depend on \(x_i\) or \(x_j\). Then
\[
\Bigl\lvert\sum_{x\in(\mathbb Z/N\mathbb Z)^m}e_N(Q(x))\Bigr\rvert\le N^{m-1}.
\]
Completing the product gives
\[
c x_i x_j+x_i L_i+x_j L_j
=c\bigl(x_i+c^{-1}L_j\bigr)\bigl(x_j+c^{-1}L_i\bigr)-c^{-1}L_i L_j.
\]
The sum over \(x_i,x_j\) of \(e_N(cuv)\) equals \(N\): the inner geometric sum over \(v\) is \(N\) when \(N\) divides \(cu\) and equals \(0\) otherwise, and \(\gcd(c,N)=1\) leaves one such \(u\). The remaining \(m-2\) variables contribute at most \(N^{m-2}\). The geometric sum is valid for every modulus, including every composite odd \(N\).

## 3. The symmetric count

For \(m\ge 3\) and \(W=M_N\), expand the injective contribution by permutations of the index set. If \(x=(x_0,\ldots,x_{m-1})\) is injective and \(\rho\in S_m\), write \((x\circ\rho)_t=x_{\rho(t)}\). Then
\[
\sum_{\substack{x,y\\\text{injective, same set}}}A(x)\overline{A(y)}
=\sum_{\rho\in S_m}\sum_{\substack{x\\\text{injective}}}A(x)\overline{A(x\circ\rho)}.
\]
Each pair of injective words on the same set arises once.

The dihedral set \(D_m\) consists of the \(m\) rotations \(\rho(t)=t+k\) and the \(m\) reversals \(\rho(t)=-t+k\). It has \(2m\) elements. These are exactly the permutations that preserve the undirected edge set of the standard \(m\)-cycle, because the automorphism group of that cycle is the dihedral group of order \(2m\). Cyclic rotation does not change the product of entries. Reversal does not change it either, because \(M_N\) is symmetric. Thus for every \(\rho\in D_m\) one has \(A(x)=A(x\circ\rho)\), and the summand equals \(N^{-m}\). There are \(P(N,m)\) injective words, so these permutations contribute
\[
D_m(N)=2m\,\frac{P(N,m)}{N^m}.
\]

Now let \(\rho\notin D_m\). The cat-map phase of a closed word is \(e_N(\alpha\sum_t Q(x_t,x_{t+1}))\) with \(\alpha=-8^{-1}\) and \(Q(u,v)=3u^2-2uv+3v^2\). For every ordering, the sum of the square terms is \(6\sum_i x_i^2\). The difference of the two orderings is therefore
\[
-2\sum_t\bigl(x_t x_{t+1}-x_{\rho(t)}x_{\rho(t+1)}\bigr).
\]
Multiplication by \(\alpha\) produces the unit \(4^{-1}\) times that integral bilinear form, because \(N\) is odd. Since \(\rho\) is not dihedral, the undirected edge sets differ, so some coefficient of a product \(x_i x_j\) with \(i\ne j\) equals \(\pm 1\). There is no square term \(x_i^2\), because a cycle of length at least \(3\) has no loop. The coefficient in the phase is \(\pm 4^{-1}\), which is a unit in \(\mathbb Z/N\mathbb Z\). The bilinear lemma bounds the sum over all of \((\mathbb Z/N\mathbb Z)^m\) by \(N^{m-1}\). The non-injective tuples number at most \(\binom{m}{2}N^{m-1}\), so the injective character sum is at most \(N^{m-1}(1+\binom{m}{2})\). Each such \(\rho\) therefore contributes at most \((1+\binom{m}{2})/N\). There are at most \(m!\) permutations, and
\[
\lvert X\rvert\le m!\,\frac{1+\binom{m}{2}}{N}.
\]
Adding the collision bound, and using \(1+\binom{m}{2}+\binom{m}{2}=1+m(m-1)\), gives Theorem 1 for \(m\ge 3\). The cases \(m=1\) and \(m=2\) are `BGS-TRACE-127`. The limit \(2m\) is the limit of \(D_m(N)\), since \(P(N,m)/N^m\to 1\) once \(m^2=o(N)\) and the error tends to \(0\) for each fixed \(m\).

The varying-time clause is the same inequality. For the logarithmic window, \(m!\le m^m\). If \(m\le c\log N/\log\log N\) with \(c<1\), then for all large \(N\) one has \(m\log m\le c\log N\), so \(m!\le N^c=o(N)\), and \(m^2=o(N)\). The factorial \(m!\) overtakes every positive power of \(N\) once \(m\) is a positive power of \(N\), so the bound does not prove a window \(m\le N^{\alpha}\).

At time three the same arithmetic is exact. `BGS-TRACE-127` gives \(\mathbb E=(6N^2-9N+4)/N^2\), while
\[
D_3(N)=6(N-1)(N-2)/N^2,
\]
so the difference is \((9N-8)/N^2\). The bound of Theorem 1 is \(42/N\). The integer comparison \(9N-8\le 42N\) for \(N\ge 1\) is the Lean witness that this case of the inequality holds; the identification of the expectation with the closed form remains in `BGS-TRACE-127`.

## 4. Kloosterman's fourth-moment bound

Let \(p\) be an odd prime and let \(e(t)=\exp(2\pi i t/p)\). For integers \(r,s\) define
\[
S(r,s)=\sum_{n=1}^{p-1}e\bigl((rn+s n^{-1})/p\bigr).
\]
**Lemma (Kloosterman).** If \(p\) divides neither \(r\) nor \(s\), then \(\lvert S(r,s)\rvert<3^{1/4}p^{3/4}\).

The proof is Kloosterman's fourth-moment count, as set out by Heath-Brown in the Nieuw Archief voor Wiskunde, fifth series, volume 1 (2000), 380–384, which was read on 29 October 2026. It is reproduced here and is an input only of the prime case \(p\ge 5\) in Theorem 2. Weil's square-root bound is not used.

For \(a\not\equiv 0\), \(S(ra,sa^{-1})=S(r,s)\): the substitution \(y=an\) sends \(ran+sa^{-1}n^{-1}\) to \(ry+sy^{-1}\). If \(p\) divides neither \(r\) nor \(s\), then as \(a\) runs through \(1,\ldots,p-1\) the pairs \((ra,sa^{-1})\) are distinct, because the first coordinate determines \(a\). Hence if \(\Sigma=\sum_{r=0}^{p-1}\sum_{s=0}^{p-1}\lvert S(r,s)\rvert^4\), the single value \(\lvert S(r,s)\rvert^4\) occurs at least \(p-1\) times on that orbit and \((p-1)\lvert S(r,s)\rvert^4\le\Sigma\). The identity \(S(ra,sa)=S(r,s)\) is false; at \(p=5\), \(r=1\), \(s=2\), \(a=2\) the two sums are not equal.

Expanding the fourth power and summing the geometric series in \(r\) and in \(s\) shows that \(\Sigma=p^2\) times the number of quadruples \((n_1,n_2,n_3,n_4)\) in \(\{1,\ldots,p-1\}^4\) with
\[
n_1+n_2\equiv n_3+n_4,\qquad n_1^{-1}+n_2^{-1}\equiv n_3^{-1}+n_4^{-1}\pmod p.
\]
The second congruence is \((n_1+n_2)/(n_1 n_2)\equiv(n_3+n_4)/(n_3 n_4)\). If the common sum is nonzero, the products agree, so \(\{n_1,n_2\}=\{n_3,n_4\}\) and there are at most \(2(p-1)^2\) such ordered quadruples. If the common sum is zero, then \(n_2\equiv-n_1\) and \(n_4\equiv-n_3\), the inverse congruence is automatic, and there are \((p-1)^2\) quadruples. The two families may overlap, so the total is at most \(3(p-1)^2\). Therefore \(\Sigma\le 3p^2(p-1)^2\) and \(\lvert S\rvert^4\le 3p^2(p-1)<3p^3\).

The count is not saturated. At \(p=5\) there are \(36\) quadruples and \(3\cdot 4^2=48\). At \(p=7\) there are \(90\) quadruples and \(3\cdot 6^2=108\). Lean decides these two censuses. The general bound remains the argument above.

## 5. Inversion breaks the reversal

On an odd prime the map \(\pi(x)=x^{-1}\) for \(x\ne 0\), with \(\pi(0)=0\), is an involution. At \(p=3\) one has \(2\cdot 2\equiv 1\), so \(\pi\) is the identity on \(\mathbb F_3\) and \(W_3=M_3\). For \(p\ge 5\) the matrix \(W_p\) is not symmetric. Let \(\delta=Q(2^{-1},1)-Q(1,2)\). Then \(Q(2^{-1},1)=3\cdot 4^{-1}-1+3=3\cdot 4^{-1}+2\) and \(Q(1,2)=3-4+12=11\), so \(\delta=3\cdot 4^{-1}-9\) and \(4\delta=-33\). The exponents of \((W_p)_{12}\) and \((W_p)_{21}\) therefore differ unless \(p\) divides \(33\). The only prime \(p\ge 5\) dividing \(33\) is \(p=11\). At that prime let \(\eta=Q(2^{-1},0)-Q(0,2)=3(4^{-1}-4)\). Then \(4\eta=-45\), and \(11\) does not divide \(45\), so the exponents of \((W_{11})_{20}\) and \((W_{11})_{02}\) differ. The verifier evaluates the pair \((1,2)\) for every listed prime other than \(11\), and the pair \((2,0)\) at \(p=11\).

For the trivial bound at \(p=3\), the occupation expansion gives \(\lvert\mathbb E\rvert\le m!\) at every time, and the main term is at most \(m\). Thus the absolute difference is at most \(m!+m\). The constant of Theorem 2 at \(p=3\) equals
\[
1+\frac{m(m-1)+2}{3}=\frac{m(m-1)+5}{3},
\]
because \(3^{1/4}\cdot 3^{-1/4}=1\). For \(m\ge 3\),
\[
3+\frac{3}{(m-1)!}\le m(m-1)+5,
\]
since the left side is at most \(3+3/2\) and the right side is at least \(8\). Multiplying by \(m!/3\) gives \(m!+m\le m!(m(m-1)+5)/3\). This is Theorem 2 at \(p=3\), for every \(m\ge 3\), and it does not use a Kloosterman sum.

Now let \(p\ge 5\) and \(m\ge 3\). For \(W_p\), a cyclic rotation still has the same product of entries. The \(m\) rotations therefore contribute the main term \(m P(p,m)/p^m\), by the same permutation expansion as in Section 3. A reversal need not.

The square terms in \(\sum_t Q(\pi(x_t),x_{t+1})\) are independent of the ordering: each index appears once as a source and once as a target. The exponent difference between the identity ordering and \(\rho\) is \(\beta\Phi_\rho\), where \(\beta=-4^{-1}\) and
\[
\Phi_\rho(x)=\sum_t\Bigl(\pi(x_{\rho(t)})x_{\rho(t+1)}-\pi(x_t)x_{t+1}\Bigr).
\]
Write \(c_{ab}\in\{-1,0,1\}\) for the coefficient of \(\pi(x_a)x_b\). The rotations are exactly the permutations whose directed edge set equals the standard edge set, so \(c_{ab}=0\) for every edge precisely on those \(m\) permutations. If \(\rho\) is not a rotation, some \(c_{ab}=\pm 1\).

Fix such a \(\rho\) and an index \(i\) with some \(c_{ib}\ne 0\). Split
\[
\Phi_\rho=\pi(x_i)L_i(x')+x_i M_i(x')+\Phi'(x'),
\]
where \(x'\) omits \(x_i\), the form \(L_i(x')=\sum_{b\ne i}c_{ib}x_b\) is linear and not identically zero, and \(M_i(x')=\sum_{a\ne i}c_{ai}\pi(x_a)\). For \(x_i\ne 0\),
\[
\Phi_\rho=x_i^{-1}L_i(x')+x_i M_i(x')+\Phi'(x').
\]
For \(x_i=0\) the first two terms vanish. Summing the additive character in \(x_i\):

- if \(L_i(x')\ne 0\) and \(M_i(x')\ne 0\), the sum over \(x_i\ne 0\) is a Kloosterman sum \(S(\beta M_i,\beta L_i)\), and \(\beta\) is a unit, so Section 4 gives absolute value \(<3^{1/4}p^{3/4}\). Adding the \(x_i=0\) term of modulus \(1\) bounds the inner sum by \(3^{1/4}p^{3/4}+1\);
- if exactly one of \(L_i(x')\) and \(M_i(x')\) is zero, the inner sum over \(x_i\ne 0\) equals \(-1\), and adding the zero term cancels it;
- if both are zero, the inner sum equals \(p\).

A nonzero linear form on \(\mathbb F_p^{m-1}\) has \(p^{m-2}\) zeros. The full character sum is therefore strictly smaller than
\[
(p^{m-1}-p^{m-2})\bigl(3^{1/4}p^{3/4}+1\bigr)+p^{m-1},
\]
which is at most \(3^{1/4}p^{m-1/4}+2p^{m-1}\). The non-injective tuples contribute at most \(\binom{m}{2}p^{m-1}\) to the triangle inequality, so the injective character sum is at most
\[
3^{1/4}p^{m-1/4}+\Bigl(2+\frac{m(m-1)}{2}\Bigr)p^{m-1}.
\]
Dividing by \(p^m\) bounds one non-rotational permutation by \(3^{1/4}p^{-1/4}+(2+m(m-1)/2)/p\). At most \(m!\) permutations are available. Adding the collision bound \(m!\,m(m-1)/(2p)\) produces
\[
m!\Bigl(3^{1/4}p^{-1/4}+\frac{m(m-1)+2}{p}\Bigr).
\]
This is Theorem 2 for \(p\ge 5\). The coefficient \(+2\) is the sum of the \(x_i=0\) term and the zero locus of \(L_i\); dropping either term is not the argument above.

The monomials \(x_a^{-1}x_b\) on \((\mathbb F_p^\times)^m\), for \(a\ne b\), are distinct reduced monomials once \(p\ge 5\), because the exponent \(-1\) is not congruent to \(1\) modulo \(p-1\). Distinct reduced monomials are linearly independent functions on the torus. Consequently \(\Phi_\rho\) is not the zero function on the torus when \(\rho\) is not a rotation, and that permutation is correctly excluded from the main term.

For \(m=1\) and \(m=2\) the flat-matrix evaluation does not see \(\pi\). The limit \(m\) follows for each fixed \(m\), since both error terms tend to \(0\). For the logarithmic window, \(m!\le m^m\). If \(m\le c\log p/\log\log p\) with \(c<1/4\), then \(m\log m\le c\log p\) for all large \(p\), so \(m!\le p^c\). Both \(m!\,p^{-1/4}\) and \(m!\,m^2/p\) tend to \(0\), and \(m^2=o(p)\).

## 6. Self-audit

The factor \(2m\) is not claimed at time two. A \(2\)-cycle equals its reversal, the orbit has size \(2\) rather than \(4\), and `BGS-TRACE-127` gives the exact value \((2N-1)/N\).

The constant \(m!(1+m(m-1))\) is a union bound. At time three the exact difference from \(6P(N,3)/N^3\) is \((9N-8)/N^2\), while the bound is \(42/N\). The inequality is in the right direction and is not sharp. The same comparison at time four, recomputed through \(N=49\), has \(N\) times the difference increasing only from \(17.73\) at \(N=7\) to \(23.09\) at \(N=49\), against the constant \(24\cdot 13=312\).

The inversion constant carries an extra \(2m!/p\) beyond \(m!\,m(m-1)/p\). That extra term is proved, and a bound that omits it is not. On the certificate range the numerical slack is positive against either expression; the theorem uses the proved one. The fourth-moment exponent \(3/4\) is not claimed to be sharp.

At \(p=3\) the inversion model is the symmetric model. Theorem 2 says so, and the inequality there is the trivial estimate \(m!+m\), not a Kloosterman bound.

The fourth-moment count allows the two families of quadruples to overlap, so \(3(p-1)^2\) is an upper bound and not a census. Lean decides the census at \(p=5\) and \(p=7\).

Tanner, Journal of Physics A 34 (2001), 8485–8500, and Pakoński–Życzkowski–Kuś, Journal of Physics A 34 (2001), 9303–9317, remain the priority references for the ensemble and the occupation constraint, as recorded in `BGS-TRACE-127`. Kloosterman's \(p^{3/4}\) bound is used only in Theorem 2, through the argument of Section 4. Weil's square-root bound is not used.

Two independent diagonals were considered and rejected as a break of time reversal. If \(D_1\) and \(D_2\) are diagonal unitaries, conjugating with \(D_2\) gives
\[
D_2(D_1 M_N D_2)D_2^{-1}=(D_2 D_1)M_N.
\]
The right-hand side is one diagonal times \(M_N\), so the spectrum is the spectrum of Theorem 1 whenever \(M_N\) is symmetric. The square-root formula \(D_2^{1/2}(D_1 M_N D_2)D_2^{-1/2}=(D_2^{1/2}D_1 D_2^{1/2})M_N\) does not hold. The inversion model is a different matrix.

A same-day referee correction replaced four steps. The Kloosterman scaling is \(S(ra,sa^{-1})=S(r,s)\), not \(S(ra,sa)=S(r,s)\). The phase gap is \(\delta=3\cdot 4^{-1}-9\). The monomials \(x_a^{-1}x_b\) are reduced monomials, not characters. The second diagonal is removed by conjugating with \(D_2\).

No Heisenberg-scale form factor is claimed, and the sixteen-phase ensemble is untouched.

## 7. Certificates

- `computations/verification/diagonal_phase_short_time.py`
- `computations/cpp/diagonal_phase_short_time.cpp`
- `formalization/Bgs/DiagonalPhaseShortTimeRational.lean`
- `evidence/executions/20261029/diagonal-phase-short-time/README.md`

The programs check the symmetric inequality for \(3\le m\le 5\) on the odd moduli \(3\) through \(15\), and for \(m=4\) also at \(N=21,31,41,49\). They check the inversion inequality for \(3\le m\le 4\) on the primes from \(3\) through \(31\). At \(p=3\) they check that the inversion occupation sum equals the symmetric one for \(m=3\) and \(m=4\). On every listed prime other than \(11\) they check that the phases of \(W_{12}\) and \(W_{21}\) differ, and at \(p=11\) they check the pair \((2,0)\). Times one and two are compared with the flat-matrix formulae, and time three is compared with \((6N^2-9N+4)/N^2\). Unitarity of \(M_N\) and of \(W_p\) is a floating-point check on those dimensions, not a proof. Both programs count \(36\) Kloosterman quadruples at \(p=5\) and \(90\) at \(p=7\). A pass does not prove `BGS-TRACE-005` or `BGS-BGS-001`.
