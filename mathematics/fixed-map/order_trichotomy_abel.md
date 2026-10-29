# The cat-map order is a trichotomy

**Claim ID:** `BGS-TRACE-121`.
**Status:** project proof. The rational comparisons are typechecked in Lean 4.33.1 and recomputed in independent Python and C++ integer arithmetic. No external referee.

The argument depends on `BGS-TRACE-120` for the trace-square identity, the criterion that an odd modulus divides \(u_t\) or \(v_t\), the short-order and long-order Abel theorems, the comparisons \(1/(e-1)<7/12\), \(1/(e^2-1)<1/6\) and \(5/7<(3-e^{-2})/4\), and the kick-difference estimate of its Section 7. It uses the norm majorant \(B=184981/160000\) only through that estimate. The orders \(t(3)=4\) and \(t(5)=6\) are the evaluations already proved there. The sharper divisibility in the half-order lemma is the arithmetic already stated for the order of \(S=C^T\) in Section 1 of `BGS-TRACE-009`. The proof is written in Section 3 and does not use the open cancellation hypothesis of that note.

`BGS-TRACE-005` and `BGS-BGS-001` remain **open**.

## 1. Statements

Keep the notation of `BGS-TRACE-120`. In particular \(N\ge3\) is odd, \(C=\begin{pmatrix}3&2\\4&3\end{pmatrix}\), \(t(N)\) is the order of \(C\) modulo \(N\), and

\[
L_N(V;1)=N^{-2}\sum_{m\ge1}e^{-2m/N}\lvert\operatorname{Tr}V^m\rvert^2.
\]

Write \(\lambda=3+2\sqrt2\), so \(\lambda^m=U_m+V_m\sqrt2\) with the same integers that express \(C^m=U_mI+V_mJ\). Thus \(U_m=u_{2m}\) and \(V_m=v_{2m}\).

**Theorem 1 (every odd prime).** Let \(p\) be an odd prime and \(t=t(p)\). Set \(\varepsilon=1\) if \(p\equiv1\) or \(7\pmod8\), and \(\varepsilon=-1\) if \(p\equiv3\) or \(5\pmod8\). Then \(t\) divides \(p-\varepsilon\), and exactly one of the following holds.

- **Short.** \(t\le(p-\varepsilon)/3\). For \(p\ge5\) one has \(12t\le5p\), so \(L_p(M_p;1)>3/4\) and the distance from this value to \((1-e^{-2})/4\) is greater than \(1/2\).
- **Long.** \(\varepsilon=-1\) and \(t=p+1\). Then \(L_p(M_p;1)<5/7\), so the statistic lies below \(3/4\) and its distance to \((1-e^{-2})/4\) is less than \(1/2\).
- **Split-half.** \(\varepsilon=1\) and \(t=(p-1)/2\). The only odd prime below \(17\) with \(\varepsilon=1\) is \(p=7\). At that prime \(L_7(M_7;1)>3/4\). For every split-half prime \(p\ge17\), \(L_p(M_p;1)<41/60<5/7\).

The clause \(t=(p+1)/2\) does not occur, and a split prime does not have order \(p-1\). Both exclusions are the half-order lemma in Section 3. On an odd prime the inequality \(2t\ge p+1\) is exactly the long class.

**Theorem 2 (every odd prime power).** Let \(\delta=\delta(p)\) be the largest positive integer such that \(C^{t(p)}\equiv I\pmod{p^\delta}\). For \(k\ge1\), the order of \(C\) modulo \(p^k\) is

\[
t(p^k)=t(p)\,p^{\max(k-\delta,0)}.
\]

If \(k\ge2\), exactly one of the following applies.

- If \(\delta\ge2\), or if \(\delta=1\) and \(12\,t(p)\le5p\), then \(12\,t(p^k)\le5\,p^k\), so \(L(M)>3/4\).
- If \(\delta=1\) and \(2\,t(p)\ge p+1\), then \(L(M)<5/7\). By the half-order lemma this hypothesis is exactly \(\varepsilon=-1\) and \(t(p)=p+1\).
- If \(\delta=1\), \(t(p)=(p-1)/2\) and \(p=7\), then \(L(M)>3/4\).
- If \(\delta=1\), \(t(p)=(p-1)/2\) and \(p\ge17\), then \(L(M)<5/7\).

Direct division gives \(\delta(3)=\delta(5)=\delta(7)=1\). In particular every power \(7^k\) lies strictly above \(3/4\), and every power \(p^k\) with \(p\ge17\) split-half and \(\delta=1\) lies strictly below \(5/7\).

**Theorem 3 (fixed kick).** Let \(\tau=10^{-80}\).

- If \(p\le10^{26}\) is long, or split-half with \(p\ge17\), then \(L_p(U_p;1)<5/7\). Also \(L_7(U_7;1)>3/4\).
- If \(N=p^k\le10^{26}\) falls under the long clause or the \(p=7\) clause of Theorem 2, the same comparison holds for \(U_N\).
- If \(N=p^k\le10^{25}\) falls under the large split-half clause of Theorem 2, then \(L_N(U_N;1)<5/7\).
- If \(p\ge11\) is short and \(N=p^k\le10^{39}\), then \(8\,t(N)\le3N\), so `BGS-TRACE-120` gives \(L_N(U_N;1)>3/4\).

**Corollary (odd Pell dimensions).** For every odd integer \(n\ge5\), \(t(u_n)\) divides \(n\) and \(12n\le5u_n\). Thus \(L_{u_n}(M_{u_n};1)>3/4\). The integer \(u_{207}\) has \(79\) digits, so none of the kick windows contains it.

**Crossing.** The verifiers recompute the recurrence below. One has \(t(13)=14\) and \(\delta(13)=2\), so \(L_{13}(M_{13};1)<5/7\) while \(L_{169}(M_{169};1)>3/4\). Likewise \(t(31)=15\) and \(\delta(31)=2\), so \(L_{31}(M_{31};1)<41/60\) while \(L_{961}(M_{961};1)>3/4\).

**Boundary.** These statements classify every odd prime and every odd prime power. The long class is the inert full order. The value \(t=(p+1)/2\) does not occur, and a split prime does not have order \(p-1\). They do not classify a modulus divisible by two distinct primes; that semiprime case is `BGS-TRACE-122`. They do not give a density of any order class, and they do not give the CUE value. The Abel weight \(e^{-2m/N}\) is the Heisenberg-time weight, but the comparison is only with the thresholds \(3/4\) and \(5/7\). The off-diagonal sum, every \(k>2\), the limit, `BGS-TRACE-005` and `BGS-BGS-001` stay open.

## 2. Where the characteristic polynomial splits

The polynomial \(x^2-6x+1\) has discriminant \(32\). Over an odd prime it splits if and only if \(2\) is a square.

In \(\mathbb F_p^\times\) the squaring map has kernel \(\{\pm1\}\), so there are \((p-1)/2\) nonzero squares. Fermat's theorem gives \(a^{p-1}=1\), hence \(a^{(p-1)/2}=\pm1\). Every nonzero square is a root of \(x^{(p-1)/2}-1\), and that polynomial has at most \((p-1)/2\) roots. Therefore a nonzero residue is a square if and only if its \((p-1)/2\)-th power equals \(1\).

Let \(\mu\) be the number of integers \(k\) with \(1\le k\le(p-1)/2\) and \(2k>p/2\), equivalently \(k>p/4\). Then

\[
\mu=\frac{p-1}2-\Bigl\lfloor\frac p4\Bigr\rfloor.
\]

The residues \(2,4,\ldots,p-1\), reduced to the symmetric interval, are \(\pm1,\ldots,\pm(p-1)/2\) up to order, and the number of minus signs is \(\mu\). Comparing products,

\[
2^{(p-1)/2}\Bigl(\frac{p-1}2\Bigr)!
\equiv(-1)^\mu\Bigl(\frac{p-1}2\Bigr)!\pmod p,
\]

so \(2^{(p-1)/2}\equiv(-1)^\mu\). The four odd classes modulo \(8\) give

| \(p\) | \(\mu\) | square? |
|---|---|---|
| \(8m+1\) | \(2m\) | yes |
| \(8m+3\) | \(2m+1\) | no |
| \(8m+5\) | \(2m+1\) | no |
| \(8m+7\) | \(2m+2\) | yes |

Thus \(\varepsilon=1\) exactly when \(2\) is a square modulo \(p\).

## 3. The order divides \(p-\varepsilon\)

The same recurrence that defines \(u_m,v_m\) holds for \(\lambda\). Section 3 of `BGS-TRACE-120` says that \(C^m\equiv I\pmod p\) if and only if \(U_m\equiv1\) and \(V_m\equiv0\).

If \(\varepsilon=1\), choose \(s\in\mathbb F_p\) with \(s^2=2\). The element \(\lambda_p=3+2s\) satisfies \(\lambda_p(3-2s)=1\), and the binomial recurrence gives \(\lambda_p^m=U_m+V_ms\). Hence \(C^m\equiv I\) if and only if \(\lambda_p^m=1\). Fermat gives \(\lambda_p^{p-1}=1\), so the order divides \(p-1\).

If \(\varepsilon=-1\), work in the ring \(\mathbb F_p[x]/(x^2-2)\). It is a field because \(x^2-2\) has no root. Let \(\lambda_p=3+2x\). Then \(\lambda_p(3-2x)=1\). Freshman's dream and Fermat give

\[
(a+bx)^p=a+bx^p,\qquad x^p=x\cdot2^{(p-1)/2}=-x,
\]

so the conjugate of \(\lambda_p\) is \(\lambda_p^p\), and \(\lambda_p^{p+1}=\lambda_p\cdot\lambda_p^p=1\). The same coefficient comparison shows that \(C^m\equiv I\) if and only if \(\lambda_p^m=1\). The order therefore divides \(p+1\).

In both cases \(t(p)\) divides \(p-\varepsilon\).

**Lemma (half-order obstruction).** Let \(p\) be an odd prime and \(t=t(p)\). Write \(\alpha=1+\sqrt2\). Then \(N(\alpha)=\alpha(1-\sqrt2)=-1\) and \(\lambda=\alpha^2=3+2\sqrt2\).

- If \(\varepsilon=1\), then \(t\) divides \((p-1)/2\). In particular \(t\neq p-1\) and \(t\neq(p+1)/2\).
- If \(\varepsilon=-1\), then \(\lambda^{(p+1)/2}=-1\) in \(\mathbb F_p[\sqrt2]\). Hence \(t\) does not divide \((p+1)/2\). Since \(t\) divides \(p+1\), the positive cofactor \((p+1)/t\) is odd. In particular \(t\neq(p+1)/2\), and \(t\) is even. The full order \(t=p+1\) has cofactor \(1\) and is not excluded.

If \(\varepsilon=1\), choose \(s\in\mathbb F_p\) with \(s^2=2\) and set \(\alpha_p=1+s\). Then \(\alpha_p^2=3+2s=\lambda_p\) and \(\alpha_p\neq0\). Fermat's theorem in \(\mathbb F_p^\times\) gives \(\alpha_p^{p-1}=1\), so \(\lambda_p^{(p-1)/2}=1\). The order of \(\lambda_p\) is \(t\), so \(t\) divides \((p-1)/2\).

If \(\varepsilon=-1\), work in the field \(\mathbb F_p[x]/(x^2-2)\) and set \(\alpha_p=1+x\). Then \(\alpha_p^2=\lambda_p\) and \(\alpha_p(1-x)=1-x^2=-1\). For \(0<r<p\) the prime \(p\) divides \(\binom{p}{r}\), and Fermat gives \(a^p=a\), so \((a+bx)^p=a^p+b^px^p=a+bx^p\). Also \(x^2=2\), hence \(x^p=x\cdot2^{(p-1)/2}\). Section 2 gives \(2^{(p-1)/2}=-1\), so \(x^p=-x\) and \(\alpha_p^p=1-x\). Therefore \(\alpha_p^{p+1}=(1+x)(1-x)=-1\), and \(\lambda_p^{(p+1)/2}=\alpha_p^{p+1}=-1\neq1\). The order \(t\) does not divide \((p+1)/2\). If the cofactor \((p+1)/t\) were even, \(t\) would divide \((p+1)/2\). The cofactor is therefore odd. Since \(p+1\) is even, \(t\) is even. The value \(t=(p+1)/2\) would have cofactor \(2\), so it does not occur.

The same two divisibility statements are already recorded for the order of \(S=C^T\) in Section 1 of `BGS-TRACE-009`. The argument here does not use the open hypothesis of that note.

Both programs check the matrix form for every odd prime through \(10^6\). If \(\varepsilon=1\), then \(C^{(p-1)/2}\equiv I\pmod p\). If \(\varepsilon=-1\), then \(C^{(p+1)/2}\equiv -I\pmod p\). On the same range they recompute \(t(p)\) and check the two exclusions, the parity of the inert cofactor, and, for every short prime \(q\ge5\), the inequality \(12\operatorname{lcm}(4,t(q))\le15q\) used in `BGS-TRACE-122`. Through \(500\) that order agrees with the order read by multiplying \(C\). The range is a finite check. The lemma is the proof for every odd prime.

## 4. Proof of the trichotomy

Let \(M=p-\varepsilon\), so \(t\mid M\) and \(M\in\{p-1,p+1\}\). Both values are even. If a positive divisor \(d\) of \(M\) satisfies \(d<M/2\), then \(M/d\ge3\), hence \(d\le M/3\). The only divisors that can exceed \(M/3\) are therefore \(M/2\) and \(M\). The half-order lemma removes two of the four formal possibilities.

- If \(\varepsilon=1\), then \(t\) divides \(M/2\), so \(t\neq M\). The case \(t=M/2\) is split-half: \(2t=p-1<p+1\) and \(t>(p-1)/3\). The case \(t\le M/3\) is short. There is no long split prime.
- If \(\varepsilon=-1\), then \(t\neq M/2\). The case \(t=M\) is the long class \(t=p+1\), and \(2t=2(p+1)\ge p+1\). The case \(t\le M/3\) is short. The formal value \(t=(p+1)/2\) does not occur.

For a short order and \(p\ge5\), \(3t\le p-\varepsilon\), so \(12t\le4(p-\varepsilon)\le4(p+1)\). Also \(4(p+1)\le5p-1\), because \(5\le p\). Thus \(12t\le5p-1\), and Theorem 1 of `BGS-TRACE-120` gives \(L_p(M_p;1)>3/4\). The CUE value is strictly less than \(1/4\), so the distance is greater than \(1/2\).

For a long order, Theorem 2 of that note gives \(L_p(M_p;1)<5/7\). Its Section 5 gives \(5/7<3/4\) and \(5/7<(3-e^{-2})/4\).

The odd primes below \(17\) with \(\varepsilon=1\) are exactly the prime \(7\). Every other split-half prime is at least \(17\).

## 5. The prime \(p=7\)

Here \(7\equiv7\pmod8\), so \(\varepsilon=1\) and \(M=6\). The value \(u_3=7\) is divisible by \(7\), while \(u_1=1\) is not, so \(t(7)=3=(7-1)/2\). Section 4 of `BGS-TRACE-120` gives \(\lvert\operatorname{Tr}M_7^m\rvert^2=49\) when \(3\mid m\) and equals \(1\) otherwise. Therefore

\[
L_7(M_7;1)
=\Bigl(1-\frac1{49}\Bigr)\frac1{e^{6/7}-1}
+\frac1{49}\frac1{e^{2/7}-1}.
\]

For \(z>0\) and an integer \(n>z\),

\[
e^z
\le\sum_{j=0}^{n-1}\frac{z^j}{j!}
+\frac{z^n/n!}{1-z/(n+1)},
\]

because \((n+k)!\ge n!(n+1)^k\). At degree \(3\) the majorants are

\[
e^{6/7}\le\frac{23441}{9947},\qquad e^{2/7}\le\frac{45187}{33957}.
\]

Both programs recompute these values. Substituting them produces the lower bound

\[
L_7(M_7;1)
\ge\frac{19796077}{25256270}.
\]

The cleared comparison \(19796077\cdot4>25256270\cdot3\) says that this fraction exceeds \(3/4\). The inequality is strict because each exponential majorant is strict, so \(L_7(M_7;1)>3/4\). The distance to the CUE value is greater than \(1/2\).

The return subsum alone is below \(3/4\), by the comparison \(R(6/7)<2401/3246\) in `BGS-TRACE-120`. The unit-trace terms are what cross the threshold.

## 6. Large split-half primes

Let \(p\ge17\) and \(t=(p-1)/2\). Section 4 of `BGS-TRACE-120` gives

\[
R(y)\le L_p(M_p;1)<R(y)+\frac1{2p},
\]

where \(y=(p-1)/p\) and \(R(y)=1/(e^y-1)\). The ratio \(y\) increases with \(p\), and \(1/(2p)\) decreases, so the upper bound is largest at \(p=17\). There \(y=16/17\). The partial sum of \(e^{16/17}\) through degree \(4\) equals \(213457/83521\). Since

\[
213457\cdot667>83521\cdot1687,
\]

this partial sum exceeds \(1687/667\). The exponential series continues with positive terms, so \(e^{16/17}>1687/667\) and

\[
R(16/17)<\frac{667}{1020}.
\]

Also \(667/1020+1/34=41/60\), because \((667\cdot34+1020)\cdot60=41\cdot1020\cdot34\). Hence

\[
L_p(M_p;1)
<R(16/17)+\frac1{34}
<\frac{41}{60}
<\frac57.
\]

The distance to the CUE value is less than \(1/2\).

## 7. The depth of the first return

Let \(t=t(p)\) and write \(\lambda^t=U+V\sqrt2\). Since \(C^t\equiv I\pmod p\), one has \(p\mid V\). Set \(\delta=v_p(V)\ge1\).

The norm \(U^2-2V^2=1\) gives \((U-1)(U+1)=2V^2\). Reducing modulo \(p\) and using \(U\equiv1\) shows that \(p\) does not divide \(U+1\), so \(v_p(U-1)=2\delta\). Consequently \(C^t\equiv I\pmod{p^e}\) if and only if \(e\le\delta\): the integer \(\delta\) is the depth named in Theorem 2.

**Lemma (lifting).** Let \(U,V\) be integers with \(U^2-2V^2=1\), \(U\equiv1\pmod p\) and \(v_p(V)=\delta\ge1\). Define \(U_n+V_n\sqrt2=(U+V\sqrt2)^n\). Then

\[
v_p(V_n)=\delta+v_p(n),\qquad v_p(U_n-1)=2v_p(V_n),
\]

and \(U_n\equiv1\pmod p\).

The last congruence holds because every term of the binomial expansion except \(U^n\) contains a factor \(V\), and \(U^n\equiv1\). In particular \(U_n\not\equiv-1\pmod p\). The norm identity then forces \(v_p(U_n-1)=2v_p(V_n)\) as soon as the valuation of \(V_n\) is known, since \(v_p(U_n+1)=0\).

The odd part of the expansion is

\[
V_n=\sum_{q\ge0}\binom{n}{2q+1}U^{n-2q-1}V^{2q+1}2^q.
\]

If \(p\) does not divide \(n\), the summand \(q=0\) has valuation \(\delta\), while every \(q\ge1\) has valuation at least \(3\delta\ge\delta+2\). Thus \(v_p(V_n)=\delta\).

Replacing the base by a pair that already satisfies the lemma, the same estimate with exponent \(p\) gives

\[
v_p(V_{pn})=v_p(V_n)+1.
\]

The leading summand is \(p\,U_n^{p-1}V_n\). For \(3\le r\le p-1\), \(v_p\bigl(\binom{p}{r}\bigr)=1\) and the power of \(V_n\) contributes at least \(3v_p(V_n)\). The summand \(r=p\), which occurs only for odd \(p\), contributes \(p\,v_p(V_n)\). Both exceed \(v_p(V_n)+1\). Iterating from the original pair produces valuation \(\delta+j\) at exponent \(p^j\). A final coprime exponent does not change the valuation. This is the lemma.

Apply it to \(\lambda^t\). If \(t\) divides \(m\), write \(m=t\,p^j s\) with \(p\nmid s\). Then \(v_p(V_m)=\delta+j\), because \(p\) does not divide \(t\). If \(t\) does not divide \(m\), Section 4 of `BGS-TRACE-120` says that \(C^m-I\) is invertible over \(\mathbb F_p\). Its determinant is then a unit modulo \(p^k\), so the only fixed vector modulo \(p^k\) is \(0\).

## 8. Kernel size

Let \(N=p^k\) and suppose \(t\mid m\), with \(\rho=v_p(V_m)=\delta+v_p(m)\). The matrix of \(C^m-I\) is

\[
\begin{pmatrix}a&b\\2b&a\end{pmatrix},
\qquad a=U_m-1,\quad b=V_m,
\]

and \(v_p(a)=2\rho\), \(v_p(b)=\rho\). The norm identity is \(a(a+2)=2b^2\).

If \(\rho\ge k\), the matrix is \(0\) modulo \(p^k\) and the kernel has \(p^{2k}\) elements. If \(\rho<k\), write \(a=p^{2\rho}a_1\) and \(b=p^\rho b_1\) with \(p\nmid b_1\). The norm becomes \(2b_1^2=2a_1+a_1^2p^{2\rho}\), so \(p\nmid a_1\) as well. The two congruences reduce to

\[
x\cdot 2a_1\equiv0\pmod{p^{k-\rho}}.
\]

Since \(2a_1\) is a unit, \(x\) is divisible by \(p^{k-\rho}\), and the same divisibility follows for \(y\). Every such pair satisfies both original congruences. There are \(p^\rho\) admissible \(x\) and \(p^\rho\) admissible \(y\), so the kernel has \(p^{2\rho}\) elements.

Combining the cases,

\[
\lvert\operatorname{Tr}M_{p^k}^m\rvert^2
=
\begin{cases}
p^{2\min(k,\delta+v_p(m))}& \text{if }t(p)\mid m,\\
1& \text{otherwise.}
\end{cases}
\]

The full kernel \(p^{2k}\) occurs exactly when \(\delta+v_p(m)\ge k\) and \(t(p)\mid m\), that is, when \(t(p)\,p^{\max(k-\delta,0)}\) divides \(m\). The least such positive integer is the order stated in Theorem 2.

## 9. Prime powers

Throughout this section \(k\ge2\) and \(N=p^k\).

### Short towers

The order \(t(p)\) divides \(p-\varepsilon\), so \(t(p)\le p+1\). If \(\delta\ge2\), then for \(p\ge5\)

\[
12(p+1)\le5p^2,
\]

because \(5\cdot5^2-12\cdot5-12=53\) and

\[
5p^2-12p-12-(5\cdot25-12\cdot5-12)=(p-5)(5p+13).
\]

The right side is nonnegative for every integer \(p\ge5\). Therefore \(12\,t(p^k)\le5\,p^k\): if \(k\le\delta\) the order remains \(t(p)\) and the modulus is at least \(p^2\); if \(k>\delta\) the ratio \(2t(p^k)/p^k\) equals \(2t(p)/p^\delta\le2(p+1)/p^2\). Theorem 1 of `BGS-TRACE-120` gives the gap.

The prime \(p=3\) is not in this clause. The value \(\lambda^4=577+408\sqrt2\) has \(v_3(408)=1\), so \(\delta(3)=1\).

If instead \(\delta=1\) and \(12\,t(p)\le5p\), the order modulo \(p^k\) is \(t(p)\,p^{k-1}\) and the ratio \(2t(p^k)/N\) equals \(2t(p)/p\le5/6\). The same theorem applies.

### Long towers

Now \(\delta=1\) and \(2t\ge p+1\), with \(t=t(p)\). The full-return ratio is \(y=2t/p>1\). Group the times at which \(t\) divides \(m\) by \(j=v_p(m)\). The contribution of level \(j\) is at most

\[
p^{-2\max(k-1-j,0)}
\sum_{\substack{s\ge1\\ p\nmid s}}e^{-b s},
\qquad
b=\frac{2t}{p^{1+(k-1-j)}}
\]

when \(j\le k-2\), and it is the ordinary return series \(R(y)\) when \(j\ge k-1\). For \(0<q<1\),

\[
\sum_{\substack{s\ge1\\ p\nmid s}}q^s
=\frac1{e^{b}-1}-\frac1{e^{bp}-1}
<\frac1b
\]

with \(q=e^{-b}\). Each partial level \(r=k-1-j\ge1\) therefore contributes less than \(p^{1-r}/(2t)\). Summing the geometric series,

\[
\sum_{r\ge1}\frac{p^{1-r}}{2t}
=\frac{p}{2t(p-1)}
\le\frac{p}{(p+1)(p-1)}.
\]

The terms with \(t\nmid m\) contribute less than \(1/(2N)\le1/(2p^2)\), by the bound \(1/(e^a-1)<1/a\) of `BGS-TRACE-120`.

For \(p=3\), \(t=4\) and \(y=8/3>2\), so \(R(y)<1/(e^2-1)<1/6\). The level bound is \(3/16\) and the unit-trace bound is \(1/18\). Hence

\[
L_{3^k}(M;1)
<\frac16+\frac3{16}+\frac1{18}
=\frac{59}{144}
<\frac57.
\]

For \(p=5\), the evaluation \(t(5)=6\) gives \(y=12/5>2\) and level bound \(5/48\). Also \(\lambda^6=19601+13860\sqrt2\) has \(v_5(13860)=1\), so \(\delta(5)=1\) and the short clause does not apply. Then

\[
L_{5^k}(M;1)
<\frac16+\frac5{48}+\frac1{50}
=\frac{349}{1200}
<\frac57.
\]

For \(p\ge11\), \(R(y)<1/(e-1)<7/12\) and the level bound is at most \(11/120\). Also \(1/(2p^2)\le1/242\). Hence

\[
L_{p^k}(M;1)
<\frac7{12}+\frac{11}{120}+\frac1{242}
=\frac{3287}{4840}
<\frac57.
\]

### The seven-power tower

Here \(p=7\), \(t=3\) and \(\lambda^3=99+70\sqrt2\), so \(v_7(70)=1\) and \(\delta=1\). The full-return ratio remains \(6/7\) at every \(k\). Keep the full returns and the single level \(r=1\), whose ratio is \(p^{-2}=1/49\) and whose step is \(6/49\). Every other term is nonnegative, so

\[
L_{7^k}(M;1)
\ge\Bigl(1-\frac1{49}\Bigr)\frac1{e^{6/7}-1}
+\frac1{49}\frac1{e^{6/49}-1}.
\]

The degree-\(3\) majorants are \(e^{6/7}\le23441/9947\) and \(e^{6/49}\le31780817/28118111\). They produce

\[
L_{7^k}(M;1)
\ge\frac{7238798455}{8237425794}
>\frac34.
\]

### Large split-half towers

Let \(p\ge17\), \(t=(p-1)/2\) and \(\delta=1\). The same level decomposition, extended over every \(r\ge1\) and using \(1/(e^b-1)<1/b\), gives

\[
L_{p^k}(M;1)
<R\Bigl(\frac{p-1}p\Bigr)+\frac{p}{(p-1)^2}+\frac1{2p^2}.
\]

The first summand decreases as \(p\) grows, and \(p/(p-1)^2\) is largest at \(p=17\). Also \(1/(2p^2)\le1/578\). Section 6 supplies \(R(16/17)<83521/129936\), and

\[
\frac{83521}{129936}+\frac{17}{256}+\frac1{578}
=\frac{427139065}{600824064}
<\frac57,
\]

because \(427139065\cdot7<600824064\cdot5\). Thus \(L<5/7\).

## 10. Two primes whose square changes side

Since \(13\equiv5\pmod8\), the order divides \(14\). The values \(u_1=1\), \(v_2=2\) and \(u_7=239\) are not divisible by \(13\), while \(v_{14}=80782=13\cdot6214\). Thus \(t(13)=14\), which is long. The term \(v_{28}=18457556052\) is divisible by \(13^2=169\) and leaves remainder \(1014\) on division by \(13^3=2197\), so \(\delta(13)=2\). Theorem 1 puts \(L_{13}\) below \(5/7\). Theorem 2 puts \(L_{169}\) above \(3/4\).

Since \(31\equiv7\pmod8\), the order divides \(30\). The value \(u_{15}=275807=31\cdot8897\) is divisible by \(31\), so the order divides \(15\). Neither \(u_1\), \(u_3\) nor \(u_5\) is. Thus \(t(31)=15=(31-1)/2\). The term \(v_{30}=107578520350\) is divisible by \(31^2=961\) and leaves remainder \(1922\) on division by \(31^3=29791\), so \(\delta(31)=2\). Theorem 1 puts \(L_{31}\) below \(41/60\). Theorem 2 puts \(L_{961}\) above \(3/4\).

Both programs rebuild the recurrence and repeat these divisions.

## 11. The kick

Section 7 of `BGS-TRACE-120` estimates \(\lvert L_N(U_N;1)-L_N(M_N;1)\rvert\) by comparing traces. The matrices are unitary of size \(N\), and the resulting bound

\[
\frac{BN^4}{2(N-2)(10^{80}-BN)}
\]

does not use primality. On the interval \(3\le s\le10^{26}\) that quantity is strictly increasing, and its value at \(10^{26}\) is strictly less than \(13/420\). Therefore the kick changes \(L_N(M_N;1)\) by less than \(13/420\) for every odd \(N\) with \(3\le N\le10^{26}\).

The cleared sums

\[
\frac{3287}{4840}+\frac{13}{420}
=\frac{72173}{101640}
<\frac57,
\]

\[
\frac{59}{144}+\frac{13}{420}<\frac57,
\qquad
\frac{349}{1200}+\frac{13}{420}<\frac57
\]

move the long towers, including the powers of \(3\) and \(5\), to the same side of \(5/7\). For a split-half prime \(p\ge17\), Section 6 gives a pure value below \(41/60\), and

\[
\frac{41}{60}+\frac{13}{420}=\frac57
\]

with both input inequalities strict. For \(p=7\) and for every \(7^k\) with \(k\ge2\),

\[
\frac{19796077}{25256270}-\frac{13}{420}>\frac34,
\qquad
\frac{7238798455}{8237425794}-\frac{13}{420}>\frac34.
\]

This is Theorem 3 for every kicked comparison except the large split-half towers.

For those towers the pure ceiling \(427139065/600824064\) leaves a margin \(14146865/4205768448\) below \(5/7\). At \(N=10^{25}\) the kick bound is strictly smaller than this margin:

\[
\begin{align*}
&184981\cdot(10^{25})^4\cdot4205768448\\
&\qquad<14146865\cdot2\cdot(10^{25}-2)
\cdot(160000\cdot10^{80}-184981\cdot10^{25}).
\end{align*}
\]

Monotonicity on \([3,10^{26}]\) carries the same defect bound to every smaller dimension. Thus \(L_N(U_N;1)<5/7\) for every large split-half tower with \(N\le10^{25}\).

Finally let \(p\ge11\) be short, and let \(N=p^k\le10^{39}\). Section 4 gives \(3t\le p-\varepsilon\), and \(8(p-\varepsilon)\le9p\) for every such prime, so \(8t\le3p\). The ratio \(8t(N)/N\) equals \(8t/p^{\min(k,\delta)}\le8t/p\le3\). Theorem 3 of `BGS-TRACE-120` gives the kicked gap.

## 12. Odd Pell dimensions

The identity \(u_{n+2}=3u_n+4v_n\) and the norm \(u_n^2-2v_n^2=(-1)^n\) give \((2v_n)^2=2u_n^2-2(-1)^n\). For \(n\ge2\), this is at least \(u_n^2\), so \(2v_n\ge u_n\) and \(u_{n+2}\ge5u_n\).

The inequality \(12n\le5u_n\) holds at \(n=5\), because \(60\le205\). If it holds at \(n\), then

\[
12(n+2)=12n+24\le5u_n+24\le25u_n\le5u_{n+2},
\]

where \(24\le20u_n\) because \(u_n\ge u_2=3\). Every \(u_n\) is odd, since \(u_1=1\) and \(u_{n+1}=u_n+2v_n\).

For odd \(n\), Section 3 of `BGS-TRACE-120` says that \(C^n\equiv I\pmod{u_n}\). Thus \(t(u_n)\) divides \(n\). For odd \(n\ge5\), \(12\,t(u_n)\le12n\le5u_n\), and Theorem 1 of that note gives \(L_{u_n}(M_{u_n};1)>3/4\).

Both programs compute \(u_{207}\) from the recurrence. It has \(79\) decimal digits and exceeds \(10^{39}\). Theorems 3 and 4 of `BGS-TRACE-120`, and Theorem 3 above, do not apply to the kicked map at that dimension.

## 13. What this does not prove

No statement above asserts that a positive-density set of primes is short, long, or split-half. The divisor constraint classifies every prime, but it does not count the primes in a class.

A product of two distinct odd primes is not a prime power. The kernel modulo such a product factors by the Chinese remainder theorem, and the resulting Abel sum is not estimated here. The first such intermediate order is not claimed to lie on either side of \(3/4\).

The comparisons decide whether \(L_N(M_N;1)\) and, inside the stated windows, \(L_N(U_N;1)\) lie above \(3/4\) or below \(5/7\). They do not identify the CUE value \((1-e^{-2})/4\). The weight \(e^{-2m/N}\) is concentrated at times of order \(N\), which is the Heisenberg scale of this Abel sum; that fact does not estimate a signed off-diagonal trace. Passing the certificates does not prove `BGS-TRACE-005`.

## 14. Certificates

| Check | What it certifies |
|---|---|
| `computations/verification/order_trichotomy_abel.py` | The majorants \(23441/9947\), \(45187/33957\), \(31780817/28118111\) and the partial sum \(213457/83521\); the cleared comparisons of Sections 5, 6, 9 and 11, including the \(10^{25}\) window; the Pell induction through \(u_{207}\) and its \(79\) digits; the witnesses \(p=3,5,7,13,31\); the kernel formula for every odd prime \(p\le80\) at modulus \(p^k\), \(k\le3\), and all times through \(4p\); the trichotomy for every odd prime through \(500\); the half-order congruences, the two exclusions, and the inequality \(12\operatorname{lcm}(4,t(q))\le15q\) for every short prime, through \(10^6\) |
| `computations/cpp/order_trichotomy_abel.cpp` | The same series, comparisons, window, Pell count, witnesses, kernel sample, trichotomy, and half-order scan, in independent integer arithmetic |
| `formalization/Bgs/OrderTrichotomyRational.lean` | `decide` proofs of the cleared comparisons and of the \(10^{25}\) window. Typechecked with Lean 4.33.1. It does not formalize Sections 2–4 or 7–8, and it does not formalize the half-order lemma |

The aggregate `lake build` was not rerun: the Mathlib cache was not present. The new module imports only the Lean prelude.
