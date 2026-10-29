# Fixed-time limits for a general hyperbolic cat map

**Claim ID:** `BGS-TRACE-132`.
**Status:** project proof. Python and C++ recompute the occupation sums in floating point for equal-diagonal and unequal-diagonal matrices, and they check the stated inequalities, including at \(N=5,7,11\). The Lean file decides only the arithmetic of the integers \(42\), \(312\), \(13+9=22\), \(22/36=11/18\), and \(121\cdot 11>6\cdot 18\). Those comparisons do not formalize the occupation estimate or the form factor. No external referee.

The quantization, the flatness, and the time-three closed form are Theorem 1 and its corollary in `BGS-TRACE-131`. The Kloosterman fourth-moment bound is the lemma of `BGS-TRACE-128`, Section 4. The occupation expansion is that of `BGS-TRACE-127`, Section 2. `BGS-TRACE-005` and `BGS-BGS-001` remain **open**.

## 1. Statements

Keep the notation of `BGS-TRACE-131`. In particular \(S=\begin{pmatrix}\alpha&\beta\\\gamma&\delta\end{pmatrix}\in\mathrm{SL}(2,\mathbb Z)\) with \(|t|\ge 3\), \(N\ge 3\) is odd, \(\gcd(\beta,N)=1\), and \(M_N(S)\) is the quantization of that note. Write \(P(N,m)=N(N-1)\cdots(N-m+1)\) for \(m\le N\) and \(P(N,m)=0\) for \(m>N\).

**Theorem 1 (Haar diagonal, short-time value \(2m\)).** Let \(D\) be diagonal with independent uniform phases and let \(U=DM_N(S)\). Then \(\mathbb E\lvert\operatorname{Tr} U\rvert^2=1\) and \(\mathbb E\lvert\operatorname{Tr} U^2\rvert^2=(2N-1)/N\). For every integer \(m\ge 3\),
\[
\Bigl\lvert\mathbb E\lvert\operatorname{Tr} U^m\rvert^2
-2m\,\frac{P(N,m)}{N^m}\Bigr\rvert
\le\frac{m!\,(1+m(m-1))}{N}.
\]
For each fixed \(m\ge 3\),
\[
\lim_{\substack{N\to\infty\\ N\text{ odd},\ \gcd(\beta,N)=1}}
\mathbb E\lvert\operatorname{Tr} U^m\rvert^2=2m.
\]
The same bound gives the limit along \(m(N)\le c\log N/\log\log N\) for any fixed \(c<1\), and it does not reach \(m\le N^{\alpha}\). The antiunitary \(\Theta'=DEK_0\) of `BGS-TRACE-131` reverses \(DM_N(S)\) for every \(S\) in the family. It reduces to \(DK_0\) precisely when \(\alpha\equiv\delta\pmod N\). The value \(2m\) is the short-time count coming from a cycle and its reversal under that antiunitary. The orthogonal-class name is the heuristic attached to \(\Theta'\). The measure is Haar measure on an \(N\)-torus, not Haar measure on the circular orthogonal ensemble. At time one the limit is \(1\), not \(2\). At time two the limit is \(2\), not \(4\), because a \(2\)-cycle equals its reversal.

**Theorem 2 (finite cosine, perturbative window).** Let \(m\ge 1\) be fixed and let the kick be a finite cosine as in `BGS-TRACE-131`, with energy \(\sigma\) and majorant \(B\). Let \(N\ge 3\) be odd and satisfy \(\gcd\bigl(N,\beta(2-u_m)\bigr)=1\). Then \(\lvert\ker(S^m-I)\rvert=1\) and
\[
\bigl\lvert\mathbb E_\varphi\lvert\operatorname{Tr} U(\eta,\varphi)^m\rvert^2-1\bigr\rvert
\le 2m^2\sigma\eta^2
+N^2\Biggl(\frac{x^3}{6}\Bigl(2+\frac{x^3}{6}\Bigr)+\frac{x^4}{4}\Biggr),
\]
where \(x=m B\lvert\eta\rvert\). If \(\eta_N\to 0\) and \(N^2\lvert\eta_N\rvert^3\to 0\), the expectation tends to \(1\). Every sequence \(\eta_N=o(N^{-2/3})\) along this set of moduli lies in the range. The set contains every odd prime outside the finite list of prime divisors of \(\beta(2-u_m)\). The limit is not \(2m\).

The hypothesis \(\gcd(N,2-u_m)=1\) is necessary for the limit \(1\). For the model matrix at time \(3\), one has \(2-u_3=-196\), and the kernel has order \(49\) at each of \(N=35,77,91,707\). Along those dimensions the pure term does not tend to \(1\).

If \(\eta\) is independent of \(N\) and nonzero, the displayed majorant tends to infinity. It does not prove a limit, and it does not prove the value \(2m\). At time one, `BGS-TRACE-131` already gives the exact value \(1\) for every real \(\eta\) whenever \(\gcd(2-t,N)=1\).

**Theorem 3 (coupling sent to infinity first).** Suppose \(m\ge 3\) and the frequency set contains \(\{1,\ldots,m\}\), with every amplitude nonzero. For every odd \(N>m\) with \(\gcd(\beta,N)=1\),
\[
\lim_{\eta\to\infty}\mathbb E_\varphi\lvert\operatorname{Tr} U(\eta,\varphi)^m\rvert^2
=\mathbb E\lvert\operatorname{Tr}(DM_N(S))^m\rvert^2.
\]
Therefore
\[
\lim_{\substack{N\to\infty\\ N\text{ odd},\ \gcd(\beta,N)=1}}
\lim_{\eta\to\infty}
\mathbb E_\varphi\lvert\operatorname{Tr} U(\eta,\varphi)^m\rvert^2
=2m.
\]
The opposite order, \(N\to\infty\) at fixed \(\eta\), is not identified, except for the window of Theorem 2 and for time one.

**Theorem 4 (what does not produce the value \(m\)).** Let \(D_1\) and \(D_2\) be diagonal unitaries. Conjugation by \(D_2\) gives
\[
D_2(D_1 M_N(S) D_2)D_2^{-1}=(D_2 D_1)M_N(S).
\]
The spectrum is the spectrum of Theorem 1. A second position-diagonal factor does not replace \(2m\) by \(m\).

Let \(p\) be an odd prime not dividing \(\beta\), let \(\pi(0)=0\) and \(\pi(x)=x^{-1}\) for \(x\neq 0\), and let \((W_p)_{xy}=(M_p(S))_{\pi(x),y}\). At \(p=3\), \(\pi\) is the identity. For \(p\ge 5\) and \(m\ge 3\),
\[
\Bigl\lvert\mathbb E\lvert\operatorname{Tr}(DW_p)^m\rvert^2
-m\,\frac{P(p,m)}{p^m}\Bigr\rvert
\le m!\Biggl(3^{1/4}p^{-1/4}+\frac{m(m-1)+2}{p}\Biggr).
\]
For each fixed \(m\ge 3\), the limit along such primes is \(m\). This inversion is not a position-diagonal kick.

If a momentum term \(\varepsilon B_N\) with \(B_N=(T_N(1,0)-T_N(-1,0))/(2i)\) and \(\varepsilon\neq 0\) is added to a position-diagonal kick, the propagator leaves the class \(DM_N(S)\). The antiunitary of `BGS-TRACE-130` is not claimed, and the form factor is not identified. A proof that this ensemble has short-time value \(m\) would need the reversal amplitudes to separate and the non-rotational character sums, including the reversals, to be \(o(1)\), as they are for \(W_p\). That estimate is not proved here.

**Boundary.** Hyperbolicity is used to know that \(2-u_m\neq 0\), so Theorem 2 excludes only finitely many prime factors of the modulus. Theorem 1 uses flatness and the phase of \(M_N(S)\), not the size of the trace. The factor \(2m\) is the dihedral count of Tanner, Journal of Physics A 34 (2001), 8485–8500, arXiv:nlin/0104014, Sections II.2 and III.1, and of Pakoński, Życzkowski and Kuś, Journal of Physics A 34 (2001), 9303–9317, arXiv:nlin/0011050, Section V. The extension of their constant to every hyperbolic \(S\) in the normalization of `BGS-TRACE-131` is the new step, and it is a modest one. The comparison values \(\min(m,N)\) for the circular unitary ensemble and the orthogonal moments are those of Diaconis and Shahshahani, Journal of Applied Probability 31A (1994), 49–62, and of Rains, Probability Theory and Related Fields 107 (1997), 219–241. The short-time orthogonal shape \(2\tau-\tau\log(1+2\tau)\) is the form factor in Haake's compendium; the limit proved here is the fixed-\(m\) value \(2m\), not that curve. Keating and Mezzadri, Nonlinearity 13 (2000), 747–774, are the prior account of the pseudo-symmetry \(\Theta'\). None of these sources is an input of the error term. No Heisenberg-scale statement is proved. The sixteen-phase ensemble of `BGS-TRACE-126` is not evaluated. `BGS-TRACE-005` and `BGS-BGS-001` remain open.

## 2. The dihedral count

The occupation expansion writes the Haar expectation as a sum of \(A(x)\overline{A(y)}\) over words with the same occupation. A non-injective word contributes at most \(m!\,m(m-1)/(2N)\), by the union bound of `BGS-TRACE-128`, Section 2.

For an injective word the permutations of its index set split into the dihedral group of order \(2m\) and the rest. A rotation preserves the product of entries. A reversal preserves it as well: the sum of the square terms in the quadratic form is \(\kappa(\alpha+\delta)\sum_i x_i^2\) in every ordering of a closed word, and the cross term \(-2\kappa\,xy\) is symmetric. The cancellation is the content of the identity \(M_N=E M_N^{\mathsf T} E^{-1}\) from `BGS-TRACE-131`: a reversal of a closed word has the same amplitude for every \(S\) in the family. There are \(P(N,m)\) injective words, so the dihedral permutations contribute \(2m\,P(N,m)/N^m\).

If \(\rho\) is not dihedral, the undirected edge sets differ, so the phase difference
\[
\beta^{-1}\sum_t\bigl(x_t x_{t+1}-x_{\rho(t)}x_{\rho(t+1)}\bigr)
\]
has some coefficient \(\pm\beta^{-1}\) in front of a product \(x_i x_j\) with \(i\neq j\). There is no square term. Since \(\gcd(\beta,N)=1\), that coefficient is a unit. The bilinear lemma of `BGS-TRACE-128`, Section 2, bounds the character sum by \(N^{m-1}\). The same arithmetic as in that section produces the error \(m!(1+m(m-1))/N\).

The limit \(2m\) is the limit of the main term. The logarithmic window is the estimate \(m!\le m^m\) already recorded in `BGS-TRACE-128`. A positive power of \(N\) overtakes the hypothesis \(m!=o(N)\), so the bound does not reach \(m\le N^{\alpha}\).

## 3. The perturbative window

If \(\gcd(N,2-u_m)=1\), then \(S^m-I\) is invertible over \(\mathbb Z/N\mathbb Z\), so \(\lvert K_m\rvert=1\). The coprimality with \(\beta\) is the quantization hypothesis. Hyperbolicity supplies \(2-u_m\neq 0\), so only finitely many primes divide the second factor. The expansion of `BGS-TRACE-131` then gives the displayed majorant, because \(\lvert D_2\rvert\le 2m^2\sigma\). If \(x\to 0\) and \(N^2 x^3\to 0\), both terms tend to \(0\). The relation \(x=m B\lvert\eta\rvert\) with \(m\) and \(B\) fixed converts \(N^2\lvert\eta\rvert^3\to 0\) into the hypothesis. The four composite dimensions in Theorem 2 are divisible by \(7\), and \(7\) divides \(196=u_3(6)-2\), so they are outside the hypothesis. The programs count the kernel \(49\) at each of them.

The comparison \(11\cdot 121>6\cdot 18\) is the case \(m=3\), \(N=11\), \(x=1\): the pure remainder majorant is \(N^2\cdot 11/18\), which already exceeds \(6=2\cdot 3\). A fixed coupling inside \(x=1\) is not forced near \(2m\) by this estimate.

## 4. Infinite coupling, then dimension

For each fixed \(N\) the set of words is finite. As \(\eta\to\infty\), \(J_0(\eta a_k\lvert\rho_k(x)-\rho_k(y)\rvert)\) tends to \(1\) when \(\rho_k(x)=\rho_k(y)\) and to \(0\) otherwise, provided \(a_k\neq 0\). Dominated convergence on a finite set passes the limit inside the Bessel path sum of `BGS-TRACE-131`. The limit is the sum of \(A(x)\overline{A(y)}\) over words whose power sums \(p_k=\sum_t e_N(k x_t)\) agree for every \(k\in\{1,\ldots,m\}\).

Newton–Girard expresses the elementary symmetric polynomials of \(m\) complex numbers as polynomials in the first \(m\) power sums, with denominators \(1,\ldots,m\). Equal power sums therefore give the same monic polynomial, hence the same multiset of roots \(e_N(x_t)\). The map \(x\mapsto e_N(x)\) is injective on \(\mathbb Z/N\mathbb Z\), so the occupations agree. The resulting sum is the Haar expectation. Theorem 1 then gives the limit \(2m\) after \(N\to\infty\).

A thinner frequency set is not given this identification. On the certificate range the summed squares at \(N=9\), \(m=3\), with only the frequency \(1\), agreed with the Haar value even though two occupation buckets had merged. That agreement is a finite observation. It is not a theorem.

## 5. Inversion

The matrix \(W_p\) is a row permutation of the unitary matrix \(M_p(S)\), hence unitary, and it is flat. At \(p=3\), \(2\cdot 2\equiv 1\), so \(\pi\) is the identity on every matrix. For \(p\ge 5\) the \(m\) rotations still contribute \(m\,P(p,m)/p^m\). A non-rotation has a nonzero coefficient of some \(\pi(x_a)x_b\). The cross-term coefficient in the phase is \(\beta^{-1}\), a unit. The square terms cancel between orderings for the same reason as in Section 2. The inner sum in the remaining variable is a Kloosterman sum, or a degenerate geometric sum, exactly as in `BGS-TRACE-128`, Section 5, and the fourth-moment bound of that note supplies the same error. The factor \(\beta^{-1}\) does not change the bound, because it is a unit.

The trivial estimate at \(p=3\) is the one in that note: the difference from the main term is at most \(m!+m\), which is absorbed by the displayed constant. Thus the limit along primes is \(m\).

Conjugation by a second diagonal was checked algebraically in `BGS-TRACE-128`, Section 6, and the same three-line computation applies to \(M_N(S)\). The momentum sine is not a function of position, by `BGS-TRACE-130`. No character-sum bound is claimed for it.

## 6. Self-audit

The factor \(2m\) is not claimed at times one or two. The numerical values at time three approach \(6\) from below on the certificate range; the inequality is the union bound, not a sharp constant.

The perturbative limit \(1\) and the Haar limit \(2m\) are different ensembles. Sending \(\eta\to\infty\) after the frequencies \(\{1,\ldots,m\}\) are present interpolates from the first to the second. A fixed finite set of frequencies and a fixed \(\eta\) are not that interpolation.

Row inversion produces the value \(m\). It is a modification of the propagator, not a kick. The sentence that a position-diagonal kick breaks time reversal down to the value \(m\) is not in the theorem.

## 7. Certificates

- `computations/verification/hyperbolic_short_time_limit.py`
- `computations/cpp/hyperbolic_short_time_limit.cpp`
- `formalization/Bgs/HyperbolicShortTime.lean`
- `evidence/executions/20261029/hyperbolic-short-time/README.md`

The programs check the symmetric inequality for \(m=3,4\) on the odd moduli \(5\) through \(15\) for the model matrix, for \(\begin{pmatrix}2&1\\1&1\end{pmatrix}\), and for \(\begin{pmatrix}5&2\\2&1\end{pmatrix}\), and the inversion inequality on the primes \(5,7,11\). The Lean file decides the arithmetic \(3!\cdot 7=42\), \(4!\cdot 13=312\), \(13+9=22\), \(22\cdot 18=11\cdot 36\), and \(121\cdot 11>6\cdot 18\). These are the integers written in the majorant. They do not certify the occupation bound. Python and C++ check that bound on the stated range, and Python counts the kernel \(49\) at \(N=35,77,91,707\). A pass does not prove `BGS-TRACE-005` or `BGS-BGS-001`.
