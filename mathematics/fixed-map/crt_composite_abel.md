# Chinese product for the cat-map trace square

**Claim ID:** `BGS-TRACE-122`.
**Status:** project proof. The rational comparisons are typechecked in Lean 4.33.1 and recomputed in independent Python and C++ integer arithmetic. No external referee.

The argument depends on `BGS-TRACE-120` for the trace-square identity, the short-order theorem, the comparisons \(5/7<(3-e^{-2})/4\) and \(5/7<3/4\), and the kick-difference estimate of its Section 7. It depends on `BGS-TRACE-121` for the splitting law, the trichotomy, the kernel formula, and the evaluation \(L_7(M_7;1)>3/4+13/420\). The orders \(t(3)=4\), \(t(5)=6\) and \(t(7)=3\) are the evaluations already proved in those notes; the six further orders below \(30\) are read here from the same divisibility criterion.

`BGS-TRACE-005` and `BGS-BGS-001` remain **open**.

## 1. Statements

Keep the notation of `BGS-TRACE-120`. In particular \(N\ge3\) is odd, \(C=\begin{pmatrix}3&2\\4&3\end{pmatrix}\), \(t(N)\) is the order of \(C\) modulo \(N\), and

\[
L_N(V;1)=N^{-2}\sum_{m\ge1}e^{-2m/N}\lvert\operatorname{Tr}V^m\rvert^2.
\]

Write \(R(y)=1/(e^y-1)\).

**Theorem 1 (Chinese product).** Let \(N=\prod_ip_i^{k_i}\) be odd and let \(m\ge0\) be an integer. Then

\[
\lvert\operatorname{Tr}M_N^m\rvert^2=\prod_i\lvert\operatorname{Tr}M_{p_i^{k_i}}^m\rvert^2,
\]

and \(t(N)\) is the least common multiple of the orders \(t(p_i^{k_i})\).

**Theorem 2 (square-free sum).** Let \(N=\prod_{i=1}^rp_i\) be a product of distinct odd primes, and write \(t_i=t(p_i)\). For each subset \(S\) of \(\{1,\ldots,r\}\) set \(d_\emptyset=1\), \(d_S=\operatorname{lcm}\{t_i:i\in S\}\) when \(S\) is nonempty, and

\[
c_S=\Bigl(\prod_{i\in S}(1-p_i^{-2})\Bigr)\Bigl(\prod_{i\notin S}p_i^{-2}\Bigr).
\]

Then

\[
L_N(M_N;1)=\sum_Sc_S\,R(2d_S/N).
\]

Every coefficient \(c_S\) is positive, and the coefficients sum to \(1\).

**Theorem 3 (semiprime dichotomy).** Let \(N=pq\) with odd primes \(p<q\), and let \(T=t(N)\). Exactly one of the following holds.

- If \(12T\le5N\), then \(L_N(M_N;1)>3/4\). The distance from this value to \((1-e^{-2})/4\) is greater than \(1/2\).
- If \(7\) divides \(N\) and \(12T>5N\), then again \(L_N(M_N;1)>3/4\), with the same distance. The partner is then an inert prime of order \(q+1\), or else \(N=21\).
- In every remaining case, \(L_N(M_N;1)<5/7\). The statistic lies below \(3/4\), and its distance to \((1-e^{-2})/4\) is less than \(1/2\).

The two clauses which previously stood beside these alternatives do not occur. A split prime does not have order \(q-1\), and no prime has order \((q+1)/2\), by the half-order lemma of `BGS-TRACE-121`. Every product of \(3\) with a short prime \(q\ge5\) satisfies \(12T\le5N\), by the lemma in Section 7, so it falls under the first alternative.

**Corollary (kick).** Let \(\tau=10^{-80}\) and let \(B=184981/160000\). If \(N=21\le10^{26}\), then \(L_N(U_N;1)>3/4\).

The hypothesis \(N=7q\) with \(q\equiv1\) or \(7\pmod8\), \(t(q)=q-1\) and \(3\nmid(q-1)\) does not occur. The hypothesis \(N=3q\) with \(q\) short, \(t(q)\) odd and \(12T>5N\) does not occur. Neither hypothesis is a kick window.

**Boundary.** The product in Theorem 1 is the diagonal trace square of \(M_N\). It does not estimate the signed off-diagonal sum of the kicked propagator. Theorem 3 stops at two prime factors: \(N=195=3\cdot5\cdot13\) has order \(84\) and \(12\cdot84>5\cdot195\), so the short-order theorem does not apply, and this note gives no bound there. The square-free case of three or more primes is `BGS-TRACE-123`, and every odd modulus is `BGS-TRACE-124`. A split full-order partner and a non-short product of \(3\) with a short prime do not occur. No density of short, long, or split-half primes is proved. The pure ceilings in Section 8 are not shown to lie \(13/420\) below \(5/7\), and the majorant of Section 6 at \(q=13\) is not shown to lie \(13/420\) above \(3/4\), so the kick is not transferred on those classes. The kick at \(u_{207}\) stays outside every window. The limit, every \(k>2\), `BGS-TRACE-005` and `BGS-BGS-001` stay open.

## 2. Product of fixed vectors

The Chinese remainder theorem gives a ring isomorphism \(\mathbb Z/N\mathbb Z\cong\prod_i\mathbb Z/p_i^{k_i}\mathbb Z\), and therefore

\[
(\mathbb Z/N\mathbb Z)^2\cong\prod_i(\mathbb Z/p_i^{k_i}\mathbb Z)^2.
\]

The integer matrix \(C^m-I\) acts on each factor through its reduction. A vector is fixed modulo \(N\) if and only if every component is fixed, so the number of solutions is the product of the numbers of solutions. Section 2 of `BGS-TRACE-120` identifies each of those numbers with a trace square. This is the product in Theorem 1.

The same isomorphism says that \(C^t\equiv I\pmod N\) if and only if \(C^t\equiv I\) modulo every \(p_i^{k_i}\), hence if and only if every \(t(p_i^{k_i})\) divides \(t\). The least positive such \(t\) is the least common multiple.

## 3. The square-free sum

Let \(k_i=1\). Section 4 of `BGS-TRACE-120` gives \(\lvert\operatorname{Tr}M_{p_i}^m\rvert^2=p_i^2\) when \(t_i\) divides \(m\), and equals \(1\) otherwise. Theorem 1 therefore yields

\[
N^{-2}\lvert\operatorname{Tr}M_N^m\rvert^2
=\prod_{i=1}^r\Bigl(1_{t_i\mid m}(1-p_i^{-2})+p_i^{-2}\Bigr).
\]

Expanding the product produces \(\sum_Sc_S\,1_{d_S\mid m}\). Summing the geometric series,

\[
\sum_{j\ge1}e^{-2d_Sj/N}=R(2d_S/N),
\]

which is Theorem 2. For two primes \(p<q\), with \(t=t(p)\), \(s=t(q)\) and \(T=\operatorname{lcm}(t,s)\), the four subsets are

\begin{align*}
A&=(1-p^{-2})(1-q^{-2}),&
B&=(1-p^{-2})q^{-2},\\
C&=(1-q^{-2})p^{-2},&
D&=N^{-2},
\end{align*}

and

\[
L_N(M_N;1)
=AR(2T/N)+BR(2t/N)+CR(2s/N)+DR(2/N).
\]

The identity \(A+B+C+D=1\) is the expansion of \(\bigl((1-p^{-2})+p^{-2}\bigr)\bigl((1-q^{-2})+q^{-2}\bigr)\).

## 4. Orders below thirty

Section 3 of `BGS-TRACE-120` says that an odd prime \(p\) divides the order index \(m\) exactly when \(m\) is odd and \(p\mid u_m\), or \(m\) is even and \(p\mid v_m\). The recurrence \(u_{n+1}=u_n+2v_n\), \(v_{n+1}=u_n+v_n\), with \(u_0=1\) and \(v_0=0\), produces the witnesses

| \(p\) | \(t(p)\) | witness | class |
|---|---:|---|---|
| \(3\) | \(4\) | \(v_4=12=3\cdot4\) | long |
| \(5\) | \(6\) | \(v_6=70=5\cdot14\) | long |
| \(7\) | \(3\) | \(u_3=7\) | split-half |
| \(11\) | \(12\) | \(v_{12}=13860=11\cdot1260\) | long |
| \(13\) | \(14\) | \(v_{14}=80782=13\cdot6214\) | long |
| \(17\) | \(8\) | \(v_8=408=17\cdot24\) | split-half |
| \(19\) | \(20\) | \(v_{20}=15994428=19\cdot841812\) | long |
| \(23\) | \(11\) | \(u_{11}=8119=23\cdot353\) | split-half |
| \(29\) | \(10\) | \(v_{10}=2378=29\cdot82\) | short |

Each witness shows that the order divides the displayed index. Both programs recompute the recurrence and check that no smaller positive index is divisible by \(p\), so the order equals that index. Theorem 1 of `BGS-TRACE-121` then assigns the class. In particular there is no short odd prime below \(29\). The half-order lemma of that note says that no odd prime, among these nine or outside them, has order \((p+1)/2\).

## 5. Which semiprimes are short

Throughout, \(p<q\) are odd primes, \(t=t(p)\), \(s=t(q)\), \(g=\gcd(t,s)\) and \(T=ts/g\). Every order divides \(p-\varepsilon\) or \(q-\varepsilon\), so \(t\le p+1\) and \(s\le q+1\). A short order is at most \((q+1)/3\).

**Lemma A.** If \(p\ge5\) and \(q\) is short, then \(12T\le5N\). The same conclusion holds when both primes are at least \(29\) and at least one order is short.

Indeed \(T\le(p+1)(q+1)/3\), so \(12T\le4(p+1)(q+1)\). The difference

\[
5pq-4(p+1)(q+1)=(p-4)(q-4)-20
\]

is at least \(1\cdot25-20=5\) when \(p\ge5\) and \(q\ge29\). If instead the smaller prime is the short one and both are at least \(29\), the same bound on \(T\) applies with the two factors exchanged.

**Lemma B.** Every product \(17q\) is short. Here \(t(17)=8\). If \(g\ge2\), then \(T\le4s\le4(q+1)\). If \(g=1\), then \(s\) is odd. The modulus \(q-\varepsilon\) is even, so its largest odd divisor is at most \((q+1)/2\), and again \(T=8s\le4(q+1)\). Thus \(12T\le48(q+1)\). For \(q\ge17\),

\[
85q-48(q+1)=37q-48\ge37\cdot17-48>0.
\]

The four products in which \(17\) is the larger prime are short by the orders of Section 4: \(\operatorname{lcm}(4,8)=8\) at \(N=51\), \(\operatorname{lcm}(6,8)=24\) at \(N=85\), \(\operatorname{lcm}(12,8)=24\) at \(N=187\), and \(\operatorname{lcm}(14,8)=56\) at \(N=221\).

**Lemma C.** If \(p=3\) and \(q\) is short, and if \(g\ge2\), then the composite is short. Here \(T\le2s\le2(q+1)/3\), so \(12T\le8(q+1)\) and \(15q-8(q+1)=7q-8>0\).

## 6. The seven family

Let \(q\neq7\) and \(N=7q\). If \(3\) divides \(s=t(q)\), then \(T=s\le q+1\) and \(12(q+1)\le35q\), so the composite is short. If \(3\) does not divide \(s\), then \(T=3s\). The trichotomy leaves the following possibilities. The half-order lemma of `BGS-TRACE-121` removes two of them.

- A short partner has \(s\le(q+1)/3\), hence \(T\le q+1\), and the composite is short.
- A split-half partner has \(s=(q-1)/2\), hence \(12T=18(q-1)\le35q\).
- An inert partner of order \((q+1)/2\) does not occur.
- A split partner of order \(q-1\) does not occur, because a split order divides \((q-1)/2\).
- An inert full partner has \(s=q+1\). Then \(12T=36(q+1)\), which exceeds \(35q\).

Thus a non-short multiple of \(7\) has inert full partner order not divisible by \(3\). The products \(5\cdot7\) and \(3\cdot7\) are the cases in which \(7\) is the larger prime. The first has \(T=6\) and is short. The second is \(N=21\), treated below; its partner \(q=3\) is the full order \(4\), not divisible by \(3\).

### Split full order

The hypothesis \(\varepsilon=1\) and \(s=q-1\) contradicts the half-order lemma: a split order divides \((q-1)/2\), which is strictly smaller than \(q-1\). The family is empty. It is not a kick window, and the subsum previously written for it is not used.

### The direct modulus \(N=21\)

Here \(t=4\), \(s=3\) and \(T=12\), so the four ratios are \(8/7\), \(8/21\), \(2/7\) and \(2/21\). For \(0<z<5\) the degree-four remainder majorant of `BGS-TRACE-121`,

\[
e^z
\le\sum_{j=0}^{3}\frac{z^j}{j!}+\frac{z^4/24}{1-z/5},
\]

is strict, because \((4+k)!>24\cdot5^k\) for every \(k\ge2\). Substituting the four ratios and the coefficients of Section 3 produces the rational lower bound

\[
\frac{1485928284770040951}{1861068320411356730}.
\]

Both programs recompute it. The comparison with \(3/4\), and with \(3/4+13/420=82/105\), is strict.

### Inert full order

Now \(\varepsilon=-1\), \(s=q+1\) and \(3\nmid(q+1)\), with \(q\ge13\). The primes below \(13\) in this class are only \(q=3\), already treated: \(q=5\) and \(q=11\) have orders divisible by \(3\). Set \(\delta=6/(7q)\), and write \(\alpha=6/7+\delta\), \(\gamma=2/7+\delta/3\) and \(\beta=\delta\). Section 5 of `BGS-TRACE-121` supplies the strict majorants \(e^{6/7}<23441/9947\) and \(e^{2/7}<45187/33957\). For \(0<\delta<1\),

\[
e^\delta
<\sum_{k=0}^{1}\frac{\delta^k}{k!}+\sum_{k\ge2}\frac{\delta^k}{2}
=1+\delta+\frac{\delta^2}{2(1-\delta)},
\]

since \(k!>2\) for \(k\ge3\). Call the right side \(M(\delta)\). Also \(e^\delta<1/(1-\delta)\), so \(R(\delta)>(1-\delta)/\delta\). Dropping the positive term \(DR(2/N)\) gives \(L_N(M_N;1)>\varphi(q)\), where

\begin{align*}
\varphi(q)
&=\frac{48}{49}(1-q^{-2})\frac1{E_6M(\delta)-1}
+\frac{48}{49q^2}\cdot\frac{1-\delta}{\delta}\\
&\qquad+\frac{1-q^{-2}}{49\bigl(E_2M(\delta/3)-1\bigr)},
\end{align*}

with \(E_6=23441/9947\) and \(E_2=45187/33957\).

The closed forms \(M(\delta)=(49q^2-18)/(7q(7q-6))\) and \(M(\delta/3)=(49q^2-2)/(7q(7q-2))\) turn \(\varphi(q)-3/4\) into a ratio of integer polynomials. Both programs expand that ratio and, after removing the positive content and the common power of \(q\), obtain \(N(q)/(196\,D(q))\), where

\begin{align*}
N(q)
&=200914962101\,q^6+281046183404\,q^5-3360079183489\,q^4\\
&\qquad-7015097338690\,q^3+759755266431\,q^2+3854354403900\,q-610115596992
\end{align*}

and

\[
D(q)=q^2(110201q^2+69629q-70323)(275135q^2+237699q-45187).
\]

The second derivative is \(N''(q)=98Q(q)\), with

\begin{align*}
Q(q)
&=61504580235\,q^4+57356363960\,q^3-411438267366\,q^2\\
&\qquad-429495755430\,q+15505209519.
\end{align*}

For real \(x\ge13\), discarding the positive terms of \(Q\) and using \(x^2\ge169\) gives

\[
Q(x)
>x\Bigl(x\bigl(61504580235\cdot169-411438267366\bigr)-429495755430\Bigr).
\]

The inner difference equals \(9982835792349\), and the bracket at \(x=13\) equals \(129347369545107\). Both are positive, so \(Q(x)>0\). Thus \(N''>0\) on \([13,\infty)\), and \(N'\) is strictly increasing there. The value \(N'(13)=454663292137321722\) is positive, so \(N'\) stays positive and \(N\) is strictly increasing. The value \(N(13)=962927132597336369\) is positive, so \(N(x)>0\) for every \(x\ge13\).

Each quadratic factor of \(D\) is positive for the same reason:

\[
110201\cdot169-70323=18553646,
\qquad
275135\cdot169-45187=46452628.
\]

Hence \(D(q)>0\) and \(\varphi(q)>3/4\) for every integer \(q\ge13\). Therefore \(L_N(M_N;1)>3/4\) throughout the inert full-order family.

## 7. Three times a short prime is short

**Lemma.** Let \(q\ge5\) be a short odd prime, write \(t=t(q)\) and \(T=\operatorname{lcm}(4,t)\), and set \(N=3q\). Then \(12T\le5N\). Theorem 1 of `BGS-TRACE-120` gives \(L_N(M_N;1)>3/4\). The conditional family in which \(q\) is short and \(12T>5N\) is empty. No short prime is asserted to exist. The prime \(q=3\) is not in this family: it is long of order \(4\).

Short means \(t\le(q-\varepsilon)/3\le(q+1)/3\).

If \(4\) divides \(t\), then \(T=t\) and \(12T=12t\le4(q+1)\). The comparison \(4(q+1)\le15q\) is \(4\le11q\), true for every integer \(q\ge5\). Since \(5N=15q\), one has \(12T\le5N\).

If \(t\equiv2\pmod4\), then \(\gcd(4,t)=2\) and \(T=2t\), so \(12T=24t\le8(q+1)\). The comparison \(8(q+1)\le15q\) is \(8\le7q\), true for every integer \(q\ge5\).

If \(t\) is odd, then \(q\) is split. An inert prime has even order, because the cofactor \((q+1)/t\) is odd and \(q+1\) is even. The half-order lemma therefore gives \(t\mid(q-1)/2\). Write \((q-1)/2=tc\). The case \(c=1\) is the split-half order, which is not short. The case \(c=2\) gives \(t=(q-1)/4\). A split prime is congruent to \(1\) or \(7\) modulo \(8\), and divisibility of \(q-1\) by \(4\) forces \(q\equiv1\pmod8\), so \((q-1)/4=2\cdot(q-1)/8\) is even. An odd order cannot arise with \(c=2\). Hence \(c\ge3\) and

\[
t\le\frac{q-1}6\le\frac{q+1}4.
\]

The second comparison is \(4(q-1)\le6(q+1)\), that is \(0\le2q+10\). Since \(t\) is odd, \(T=4t\) and \(12T=48t\). Then

\[
48t\le48\cdot\frac{q+1}4=12(q+1)\le15q,
\]

because \(12(q+1)\le15q\) is \(12\le3q\). Thus \(48t\le15q\), which is \(12T\le5N\).

In every case the product is short. Both programs still recompute the unused degree-four value \(5704517734146/5603750430307\) at the corner ratios \(80/87\) and \(20/87\). That comparison is not a witness of a non-short product. The order scan of `BGS-TRACE-121`, through every odd prime \(q\le10^6\), checks \(12T\le15q\) whenever \(q\) is short.

## 8. The ceiling

It remains to bound every semiprime that is not short and not a non-short multiple of \(7\). Section 7 says that three times a short prime is already short. Lemmas A and B exclude every semiprime that has a short factor or the factor \(17\). Both remaining orders are therefore non-short, and neither prime is \(7\) or \(17\).

For \(z>0\) let \(P_8(z)=\sum_{j=0}^{8}z^j/j!\). The next term of the exponential series is positive, so \(e^z>P_8(z)\) and \(R(z)<1/(P_8(z)-1)\). Combined with \(R(z)<1/z\) and with \(A<1\), \(B<q^{-2}\), \(C<p^{-2}\),

\begin{equation}
L_N(M_N;1)
<\frac1{P_8(\alpha)-1}
+\frac{p}{2tq}
+\frac1{p^2\bigl(P_8(\gamma)-1\bigr)}
+\frac1{2N},
\tag{\(\ast\)}
\end{equation}

where \(\alpha=2T/N\) and \(\gamma=2s/N\), whenever the second and fourth terms are the bounds \(1/(q^2\beta)\) and \(1/(N^2\cdot2/N)\) coming from \(\beta=2t/N\). Every comparison below is this one, evaluated at a concrete corner. Both programs recompute the degree-eight sums. Each resulting rational is strictly less than \(5/7\), and the inequality (\(\ast\)) is itself strict.

A non-short order is at least \((q-1)/2\). For the fixed full orders below, every gcd \(g>2\) makes the composite short for every larger prime, and a factor \(g=2\) with a half-order partner is short as well. Each of \(t(3)\), \(t(5)\), \(t(11)\), \(t(13)\) and \(t(19)\) is even, and every full order \(q-\varepsilon\) is even, so a full partner meets these orders in \(g\ge2\). The remaining non-short classes are therefore \(g=1\) with a half-order partner and \(g=2\) with a full partner. Both have

\[
\alpha\ge\frac{t(q-1)}{pq},\qquad\gamma\ge\frac{q-1}{pq},
\]

and the second class has the larger ratio \(\gamma\). The right side of (\(\ast\)) therefore decreases as \(q\) increases, because both return ratios increase and \(P_8\) increases. The largest value on a tail \(q\ge q_0\) is the value at \(q_0\).

### Three explicit products

The orders of Section 4 give three non-short products below the tails.

- \(N=15\), \(T=\operatorname{lcm}(4,6)=12\), ratios \(8/5\) and \(4/5\). The bound is strictly less than \(5/7\).
- \(N=39\), \(T=\operatorname{lcm}(4,14)=28\), ratios \(56/39\) and \(28/39\).
- \(N=65\), \(T=\operatorname{lcm}(6,14)=42\), ratios \(84/65\) and \(28/65\).

The products \(3\cdot11\), \(3\cdot17\), \(3\cdot19\), \(5\cdot11\) and \(5\cdot17\) are short by the same orders.

### Fixed full orders

For \(p=3\), \(t=4\). The divisor \(g=4\) gives \(T\le q+1\) and \(15q-12(q+1)=3q-12>0\). The divisor \(g=2\) with a half-order partner gives \(T\le q+1\) and the same inequality. The tail of the two remaining classes starts at \(q=23\), where \(\alpha\ge88/69\) and \(\gamma\ge22/69\). The bound is strictly less than \(5/7\). Every prime from \(5\) through \(19\) is one of \(N=15\), the short products above, or the seven-family modulus \(N=21\).

For \(p=5\), \(t=6\). If \(g=6\), then \(T\le q+1\). If \(g=3\), then \(T=2s\le2(q+1)\) and \(25q-24(q+1)=q-24\), so every partner \(q\ge29\) is short. The only primes below \(29\) whose order is divisible by \(3\) are \(7\) and \(11\), and both products with \(5\) are short. A factor \(g=2\) with a half-order partner gives \(T\le3(q+1)/2\) and \(25q-18(q+1)=7q-18>0\). The tail starts at \(q=17\), with \(\alpha\ge96/85\) and \(\gamma\ge16/85\). The only non-short product below that tail is \(N=65\).

For \(p=11\), \(t=12\). Every divisor \(g\ge3\) satisfies \(12\cdot12<5\cdot g\cdot11\) by enough to absorb the factor \((q+1)/q\) for every \(q>11\): the tightest case \(g=3\) needs only \(q\ge144/(165-144)\), and \(144/21<7\). A factor \(g=2\) with a half-order partner gives \(T\le3(q+1)\) and \(55q-36(q+1)=19q-36>0\). The tail starts at \(q=13\), with \(\alpha\ge144/143\) and \(\gamma\ge12/143\).

For \(p=13\), \(t=14\). The divisors \(g=7\) and \(g=14\) give \(12T\le12\cdot14\cdot(q+1)/7\), and \(65q-24(q+1)=41q-24>0\). A half-order partner with \(g=2\) gives \(T\le7(q+1)/2\) and \(65q-42(q+1)=23q-42>0\). The tail starts at \(q=17\), with \(\alpha\ge224/221\) and \(\gamma\ge16/221\). The product \(13\cdot17\) is short by Lemma B, so the bound at \(q=17\) is only an envelope for the larger primes.

For \(p=19\), \(t=20\). Every divisor \(g\ge4\) satisfies \(12\cdot20\le5\cdot g\cdot19\) with room for \((q+1)/q\). A half-order partner with \(g=2\) gives \(T\le5(q+1)\) and \(95q-60(q+1)=35q-60>0\). The tail starts at \(q=23\), with \(\alpha\ge440/437\) and \(\gamma\ge22/437\). There is no prime strictly between \(19\) and \(23\). The partner \(23\) is split-half of order \(11\), and \(\gcd(20,11)=1\), so this corner is attained.

### The split-half prime \(23\)

Here \(t=11\). A partner divisible by \(11\) has \(T=s\le q+1\). A half-order partner has \(T\le11(q+1)/2\), and \(115q-66(q+1)=49q-66>0\) for every \(q\ge3\). A short partner is short as a composite by Lemma A. The only remaining class is a full partner, \(s\ge q-1\) and \(g=1\), with

\[
\alpha\ge\frac{22(q-1)}{23q},\qquad\gamma\ge\frac{2(q-1)}{23q}.
\]

The prime \(29\) is short, so every such partner is at least \(31\). The bound decreases in \(q\) and at \(q=31\) has ratios \(660/713\) and \(60/713\). It is strictly less than \(5/7\). The product \(23\cdot31\) itself is short, because \(31\) is split-half; the value at \(31\) is the envelope for every larger full partner.

### Split-half primes at least \(31\)

Let \(p\ge31\) be split-half, so \(t=(p-1)/2\), and let \(q\ge p+2\). A half-order partner or a gcd \(g\ge2\) gives \(T\le(p-1)(q+1)/4\). Then

\[
5pq-3(p-1)(q+1)\ge5p(p+2)-3(p-1)(p+3)=2p^2+4p+9>0,
\]

so the composite is short. A short partner is short as a composite by Lemma A. The only remaining class is a full partner with \(g=1\). Then

\[
\alpha\ge\Bigl(1-\frac1p\Bigr)\Bigl(1-\frac1q\Bigr)\ge\frac{30}{31}\cdot\frac{32}{33}=\frac{960}{1023}.
\]

The term \(1/(p^2\gamma)\) replaces the degree-eight term in \(\gamma\). Since \(\gamma\ge2(q-1)/(pq)\) and \(q/(p(q-1))\) decreases as either prime grows,

\[
\frac1{p^2\gamma}\le\frac{33}{2\cdot31\cdot32}.
\]

Likewise \(p/((p-1)q)\le31/(30\cdot33)\) and \(1/(2pq)\le1/(2\cdot31\cdot33)\). Adding \(1/(P_8(960/1023)-1)\) keeps the sum strictly below \(5/7\).

### Every other large semiprime

The smaller prime is now non-split and non-short, and at least \(37\). The odd primes below \(37\) are \(3,5,7,11,13,17,19,23,29,31\), each already placed: \(29\) is short and \(31\) is split-half. The order is long. By the half-order lemma the long class is exactly \(t=p+1\), so the order is even. The value \(t=(p+1)/2\) does not occur, whether \(p\equiv3\pmod8\) or \(p\equiv5\pmod8\).

If the partner is short, Lemma A gives a short composite. If \(g\ge3\), then \(T\le(p+1)(q+1)/3\), so \(12T\le4(p+1)(q+1)\). The difference used in Lemma A,

\[
5pq-4(p+1)(q+1)=(p-4)(q-4)-20,
\]

is positive for \(p\ge5\) and \(q\ge29\). If \(g\ge2\) and the partner is a half order, then \(t\le p+1\) and \(s\le(q+1)/2\), so \(T\le(p+1)(q+1)/4\) and \(12T\le3(p+1)(q+1)\). The difference \(5pq-3(p+1)(q+1)\) increases in each variable for \(p,q\ge3\), and its value at \((29,31)\) is \(4495-2880>0\). Every such composite is short. An inert half-order does not occur, so no further case is created by writing \((p+1)/2\) in place of the smaller order.

What remains is a full smaller order whose partner is a half order with \(g=1\), or a full order with \(g=2\). A full partner of a full smaller order cannot have \(g=1\), since both orders are even. Throughout, \(q\ge p+2\).

For a full smaller order, \(t\ge p-1\), hence

\[
\alpha\ge\frac{(p-1)(q-1)}{pq},\qquad
\gamma\ge\frac{q-1}{pq},\qquad
\frac{p}{2tq}\le\frac{p}{2(p-1)q}.
\]

The lower bound on \(\alpha\) increases with either prime. The three quantities \(p/(2(p-1)q)\), \(q/(p(q-1))\) and \(1/(2pq)\) decrease with either prime. Their extreme on \(p\ge37\) and \(q\ge p+2\) is therefore the corner \(p=37\), \(q=39\), whether or not \(39\) is prime:

\begin{align*}
\frac{36\cdot38}{37\cdot39}&=\frac{456}{481}>\frac{840}{899},&
\frac{37}{2\cdot36\cdot39}&=\frac{37}{2808}<\frac{29}{56\cdot31},\\
\frac{39}{37\cdot38}&=\frac{39}{1406}<\frac{31}{29\cdot30},&
\frac1{2\cdot37\cdot39}&<\frac1{2\cdot29\cdot31}.
\end{align*}

Since \(P_8\) is increasing, the right side of (\(\ast\)) is strictly smaller than

\begin{equation}
\frac1{P_8(840/899)-1}+\frac{29}{56\cdot31}+\frac{31}{29\cdot30}+\frac1{2\cdot29\cdot31}.
\tag{\(\ast\ast\)}
\end{equation}

The ratios \(840/899\), \(29/(56\cdot31)\) and \(31/(29\cdot30)\) are a convenient majorant. They are not values attained at a nonsplit prime: \(29\) is short and \(31\) is split-half.

No prime has inert half order, so the following comparison meets no semiprime. It is retained because both programs recompute it, and it is not an input to the exhaustion. If one assumed an odd inert half \(t=(p+1)/2\), a full partner and \(g=1\), then

\[
\alpha
\ge\frac{(p+1)(q-1)}{pq}
\ge\frac{(p+1)^2}{p(p+2)}
=1+\frac1{p(p+2)}
>1
>\frac{840}{899},
\]

so the degree-eight term is smaller than the one in (\(\ast\ast\)). The other three terms of (\(\ast\)) are at most

\[
\frac{p}{(p+1)q}+\frac{q}{2p(q-1)}+\frac1{2pq}.
\]

For fixed \(p\) each summand decreases in \(q>1\). The middle one does because \(q/(q-1)=1+1/(q-1)\), and the other two are constant multiples of \(1/q\). The maximum is at \(q=p+2\), where the sum equals

\[
g(p)=\frac{3p^2+5p+5}{2p(p+1)(p+2)}.
\]

Clearing the positive factor \(2(p+1)(p+2)\) gives

\[
(3p^2+5p+5)(p+3)-(3(p+1)^2+5(p+1)+5)p=3p^2+7p+15>0,
\]

so \(g(p)>g(p+1)\). Thus the three terms are at most \(g(37)=4297/109668\). Both programs check that this is strictly smaller than the sum of the three constant terms in (\(\ast\ast\)). The same majorant therefore bounds the inert case.

Both programs recompute (\(\ast\ast\)) and find it strictly less than \(5/7\).

This exhausts the semiprimes. In the remaining case of Theorem 3, \(L_N(M_N;1)<5/7\). Section 5 of `BGS-TRACE-120` supplies \(5/7<3/4\) and \(5/7<(3-e^{-2})/4\).

## 9. The kick on \(N=21\)

Section 7 of `BGS-TRACE-120` records, for the fixed kick and every odd dimension with \(BN<10^{80}\),

\[
\lvert\operatorname{Tr}U_N^m-\operatorname{Tr}M_N^m\rvert
\le Nm\frac{x}{1-x},
\qquad x=\frac{BN}{10^{80}}.
\]

Both propagators are unitary of size \(N\), so the same section's passage from traces to the Abel sum gives

\[
\bigl\lvert L_N(U_N;1)-L_N(M_N;1)\bigr\rvert
<\frac{BN^4}{2(N-2)(10^{80}-BN)}.
\]

The logarithm of this majorant has positive derivative on the real interval \([3,10^{26}]\), by the calculation written there for the prime case; primality is not used. The majorant is therefore largest at the right endpoint, where

\[
184981\cdot10^{104}\cdot420
<26\cdot(10^{26}-2)\cdot(160000\cdot10^{80}-184981\cdot10^{26}).
\]

Thus the difference is strictly less than \(13/420\) for every odd \(N\le10^{26}\).

The split full-order family does not occur, and Section 7 shows that three times a short prime is short, so neither family contributes a kick window. The subtraction applies to \(N=21\), whose rational lower bound exceeds \(82/105\). Hence \(L_{21}(U_{21};1)>3/4\). This is the corollary. It does not apply to a ceiling semiprime, nor to the inert full-order family, because those pure margins are not known to dominate \(13/420\). The unused corner \(5704517734146/5603750430307\) also exceeds \(82/105\); it is not the value of a semiprime.

## 10. What this does not prove

Theorem 1 controls \(\lvert\operatorname{Tr}M_N^m\rvert^2\) only. In the decomposition of a kicked trace into its cat-map diagonal and a signed off-diagonal sum, the second sum is untouched. The square-free formula is an exact finite expression, not a limit at the Heisenberg scale. The finite sandwich in the certificate, through every semiprime whose prime factors are less than \(100\), checks the case split; it is not a density and it is not an input to Sections 6--8.

The pure cat map on a long prime lies on the CUE side of distance \(1/2\) and is still arithmetically rigid: the return times contribute spikes, and the off-return trace square equals \(1\). That negative statement is not a theorem about \(U_N\). Nothing here proves `BGS-TRACE-005` or `BGS-BGS-001`.

## 11. Certificates

The Python and C++ programs recompute every rational bound in this note, the polynomial identity for \(\varphi(q)-3/4\), the positivity integers, the nine orders, the defect endpoint, the reduction of the \(p\ge37\) corner to the majorant \((\ast\ast)\), and the semiprime sandwich below \(100\). The Lean file certifies the positivity integers, the defect endpoint, the two explicit lower bounds, the short-factor corners, and that same corner reduction. The analytic comparisons themselves were checked by the author and were not given an independent referee.

- `computations/verification/crt_composite_abel.py`
- `computations/cpp/crt_composite_abel.cpp`
- `formalization/Bgs/CrtCompositeRational.lean`
- `evidence/executions/20261029/crt-composite/README.md`
