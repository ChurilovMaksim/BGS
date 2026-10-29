# Every odd modulus lies above \(3/4\) or below \(5/7\)

**Claim ID:** `BGS-TRACE-124`.
**Status:** project proof. The rational comparisons are typechecked in Lean 4.33.1 and recomputed in independent Python and C++ integer arithmetic. No external referee.

The argument depends on `BGS-TRACE-120` for the short-order theorem, the return lower bound \(L_N(M_N;1)\ge R(2t(N)/N)\), the comparisons \(5/7<3/4\) and \(5/7<(3-e^{-2})/4\), and the kick-difference estimate. It depends on `BGS-TRACE-121` for Theorems 1 and 2, which place every odd prime and every odd prime power, for the half-order lemma, for the splitting law, the kernel formula, the values \(\delta(3)=\delta(5)=\delta(7)=1\) and \(\delta(13)=2\), and the two comparisons \(L_7(M_7;1)-13/420>3/4\) and \(7238798455/8237425794-13/420>3/4\). It depends on `BGS-TRACE-122` for the Chinese product, the semiprime dichotomy, the emptiness of a non-short product of \(3\) with a short prime, and the case division of the ceiling. It depends on `BGS-TRACE-123` for every square-free product of at least three primes, including the unique product \(N=195\) that fails \(12t\le5N\), and for the kick on square-free \(N=15r\) through \(10^{26}\).

`BGS-TRACE-005` and `BGS-BGS-001` remain **open**.

## 1. Statements

Keep the notation of `BGS-TRACE-120`. In particular \(N\ge3\) is odd, \(t(N)\) is the order of \(C\) modulo \(N\), and \(R(y)=1/(e^y-1)\). Write \(M=\operatorname{rad}(N)\) for the product of the distinct prime factors of \(N\).

**Theorem 1 (every odd modulus).** Let \(N\ge3\) be odd. Exactly one of the following holds.

- \(L_N(M_N;1)>3/4\). The distance from this value to \((1-e^{-2})/4\) is greater than \(1/2\).
- \(L_N(M_N;1)<5/7\). The statistic lies below \(3/4\), and its distance to \((1-e^{-2})/4\) is less than \(1/2\).

The modulus \(315=3^2\cdot5\cdot7\) is in the first case. Its radical is \(105\), which is short, so \(315\) is short by the comparison in Section 2. No separate expansion at \(315\) is required.

**Assembly of Theorem 1.** Let \(N\ge3\) be odd.

1. If \(N\) is a prime power, Theorems 1 and 2 of `BGS-TRACE-121` give the dichotomy. This includes every non-square-free prime power, whether or not its prime radical is short.
2. If \(N\) is a product of two distinct odd primes, Theorem 3 of `BGS-TRACE-122` gives the dichotomy. A split partner of order \(q-1\) does not occur, and a non-short product of \(3\) with a short prime does not occur.
3. If \(N\) is square-free and has at least three distinct odd prime factors, Theorem 1 of `BGS-TRACE-123` gives \(L_N(M_N;1)>3/4\).
4. Otherwise \(N\) is not square-free and not a prime power. Sections 2--7 place it. If the radical is short, Section 2 gives \(L_N(M_N;1)>3/4\). If the radical fails \(12\,t\le5N\), then it is a non-short semiprime or \(195\): a non-preserving power is short by Section 3, a ratio-preserving ceiling tower lies below \(5/7\) by Sections 5 and 6, and a ratio-preserving tower on the other side lies above \(3/4\) by Section 7.

A non-short prime radical is a prime power and is case 1. It is not left to the sentence that begins Section 3.

**Theorem 2 (fixed kick, partial).** Let \(\tau=10^{-80}\) and \(B=184981/160000\).

- If \(8\,t(N)\le3N\) and \(N\le10^{39}\), then \(L_N(U_N;1)>3/4\). In particular this holds for \(N=315\), and for \(N=45\).
- If \(N\le10^{26}\) and \(N\) is one of \(3\cdot7^a\) with \(a\ge2\), an inert full-order tower \(7^aq^b\) with \(a\ge2\), an inert tower \(7q^b\) with the exponent of \(7\) equal to \(1\) and \(13\le q\le39\), or \(3\cdot5^b\cdot13\) with \(b\ge2\), then \(L_N(U_N;1)>3/4\). Each of these is ratio-preserving and the pure margin exceeds \(13/420\).
- If \(N=15r\) with \(r\) an odd prime, \(r\ge7\), and \(N\le2\cdot10^{26}\), then \(L_N(U_N;1)>3/4\). The range \(N\le10^{26}\) is `BGS-TRACE-123`. The range \(10^{26}<N\le2\cdot10^{26}\) is Section 8.

A split full-order tower does not occur. A non-short product of \(3\) with a short prime does not occur. Neither is a kick window. The value \(r=3\) gives \(N=45=3^2\cdot5\), which is not square-free. Here \(\delta(3)=1\), so \(t(9)=t(3)\cdot3=12\), and \(t(5)=6\), hence \(t(45)=\operatorname{lcm}(12,6)=12\). Then \(8\cdot12=96\le135=3\cdot45\), and the first bullet applies. The value \(r=5\) gives \(N=75=3\cdot5^2\), a ratio-preserving tower over the ceiling semiprime \(15\); the kick is not claimed on a ceiling tower.

**Boundary.** The kick is not claimed for a ratio-preserving tower over a ceiling semiprime. At \(3\cdot23\) the tower majorant of Section 5 leaves a gap \(575/22594\) below \(5/7\), and \(575/22594<13/420\), so that majorant does not absorb the defect. The kick is not claimed for an inert full-order tower \(7q^b\) with the exponent of \(7\) equal to \(1\) and \(q\ge40\). The comparison which proves \(L>3/4\) on that tail lies below \(82/105\). The kick is not claimed for \(N=15r>2\cdot10^{26}\). The same defect majorant exceeds \(1\) at every integer of \(79\) digits, and `BGS-TRACE-119` already shows that no nonnegative remainder about the pure second-order center proves the gap at \(u_{207}\). No density is proved. The signed off-diagonal sum, the limit, and every \(k>2\) stay open. A value above \(3/4\) lies at distance greater than \(1/2\) from the CUE value, on the side away from \((1-e^{-2})/4\).

## 2. The ratio cannot increase when an exponent is raised

Let \(N=\prod_pp^{k_p}\) with each \(k_p\ge1\), and let \(T=t(M)\). Theorem 2 of `BGS-TRACE-121` gives \(t(p^{k})=t(p)\,p^{r_p}\) with \(r_p=\max(k_p-\delta(p),0)\), and \(p\) does not divide \(t(p)\) because \(t(p)\) divides \(p-\varepsilon\). Theorem 1 of `BGS-TRACE-122` says that \(t(N)\) is the least common multiple of these prime-power orders. Therefore the valuation of a prime \(p\) dividing \(N\) in \(t(N)\) is \(\max(r_p,v_p(T))\), while every prime outside \(N\) has the same valuation in \(t(N)\) as in \(T\). Hence

\[
t(N)=T\prod_{p\mid N}p^{\max(0,\,r_p-v_p(T))}.
\]

The exponent of \(p\) in \(t(N)/N\) divided by \(T/M\) is

\[
e_p=\max(0,\,r_p-v_p(T))-(k_p-1).
\]

If \(k_p=1\), then \(r_p=0\) and \(e_p=0\). If \(k_p\ge2\), the inequality \(\delta(p)\ge1\) forces \(e_p\le0\). Equality holds if and only if \(\delta(p)=1\) and \(p\) does not divide \(T\). Thus \(t(N)/N\le T/M\). Call the power **ratio-preserving** when equality holds, and **non-preserving** otherwise.

If \(12\,T\le5M\), then \(12\,t(N)\le5N\). Theorem 1 of `BGS-TRACE-120` gives \(L_N(M_N;1)>3/4\). If also \(8\,T\le3M\), then \(8\,t(N)\le3N\), and Theorem 3 of the same note gives the kicked gap whenever \(N\le10^{39}\).

In particular \(M=105=3\cdot5\cdot7\) has \(t(105)=\operatorname{lcm}(4,6,3)=12\), and both \(12\cdot12\le5\cdot105\) and \(8\cdot12\le3\cdot105\). Every odd \(N\) with radical \(105\), including \(315=3^2\cdot5\cdot7\), is therefore short, and strongly short. The same conclusion applies to every odd \(N\) whose radical is a short square-free modulus. By `BGS-TRACE-123`, the only square-free odd modulus with at least three prime factors that fails \(12\,t\le5N\) is \(195\).

## 3. A non-preserving power is short

Inside case 4 of the assembly, consider a non-square-free \(N\) that is not a prime power and whose radical \(M\) fails \(12\,t(M)\le5M\). Then \(M\) is square-free and has at least two distinct prime factors. By `BGS-TRACE-122` and `BGS-TRACE-123`, the only such moduli are a non-short semiprime and \(195\).

**Lemma (drop).** In either case a non-preserving power satisfies \(12\,t(N)\le5N\), so Theorem 1 of `BGS-TRACE-120` gives \(L_N(M_N;1)>3/4\).

For the radical \(195\), one has \(T=84\) and \(12\cdot84=1008>5\cdot195\). A non-preserving power multiplies the ratio \(t/N\) by at most \(1/3\). The comparison \(12\cdot84<5\cdot195\cdot3\) is strict, so the power is short.

Now let the radical be a semiprime \(pq\) with \(p<q\), and let \(\pi\) be a prime whose exponent in \(N\) is at least \(2\) and whose exponent \(e_\pi\) is at most \(-1\). Then \(t(N)/N\le T/(pq\cdot\pi)\). Since \(T\le(p+1)(q+1)\), it is enough to prove \(12(p+1)(q+1)<5\,pq\cdot\pi\).

If \(p\ge5\), the difference \(5p^2q-12(p+1)(q+1)\) is increasing in \(q\) for each fixed \(p\ge5\), because its coefficient of \(q\) equals \(5p^2-12(p+1)\) and that quantity is at least \(53\) at \(p=5\). The diagonal value \(5p^3-12(p+1)^2\) equals \(193\) at \(p=5\), and its first difference \(15p^2-9p-31\) equals \(299\) there and is increasing. Thus the diagonal value stays positive, and \(12(p+1)(q+1)<5p^2q\). If the dropped prime is \(p\), this is the required bound. If it is \(q\), the same bound is stronger because \(q\ge p\). A drop by more than one power of \(\pi\) is smaller still.

If \(p=3\) and the dropped prime is \(3\), then \(\delta(3)=1\), so non-preservation means that \(3\) divides \(T\). Hence \(3\) divides \(t(q)\). The order \(t(q)\) divides the even integer \(q-\varepsilon\le q+1\). If \(t(q)\) is odd it is at most \((q+1)/2\), and \(\operatorname{lcm}(4,t(q))=4t(q)\le2(q+1)\). If \(t(q)\) is even then \(\gcd(4,t(q))\ge2\), so the same least common multiple is at most \(2t(q)\le2(q+1)\). Therefore \(12T\le24(q+1)\). For \(q\ge5\),

\[
45q-24(q+1)=21q-24\ge81>0,
\]

and \(45q=5\cdot3\cdot q\cdot3\). The power is short. If instead the dropped prime is \(q\), the cruder bound \(T\le4(q+1)\) gives \(12T\le48(q+1)\), and \(15q^2-48q-48\) equals \(87\) at \(q=5\) and increases. Again the power is short.

## 4. The Bernoulli majorant

For \(z>0\) set \(B(z)=1/z-1/2+z/12\) and

\[
h(z)=(z^2-6z+12)(e^z-1)-12z.
\]

Then \(h(0)=h'(0)=h''(0)=0\), and \(h'''(z)=z^2e^z\). The third derivative is positive for \(z>0\), so \(h(z)>0\). Also \(z^2-6z+12=(z-3)^2+3>0\). Dividing gives the strict inequality \(R(z)<B(z)\).

The degree-four lower bound used below is the one already recorded in `BGS-TRACE-121`: for \(0<z<5\),

\[
e^z<\sum_{j=0}^{3}\frac{z^j}{j!}+\frac{z^4/24}{1-z/5},
\]

and the reciprocal of the right side minus one is a strict lower bound for \(R(z)\).

## 5. Ratio-preserving towers over a ceiling semiprime

Let \(N=p^aq^b\) be ratio-preserving, with odd primes \(p<q\) and \(\max(a,b)\ge2\). Ratio preservation forces \(\delta=1\) at every prime whose exponent is at least \(2\), and neither such prime divides \(T=t(pq)\). Section 8 of `BGS-TRACE-121` then gives the normalized trace square at a prime power \(r^k\) as \(r^{-2\max(k-1-v_r(m),0)}\) when \(t(r)\) divides \(m\), and as \(r^{-2k}\) otherwise.

That weight is the finite expansion

\[
r^{-2k}+\sum_{s=0}^{k-1}(1-r^{-2})r^{-2(k-1-s)}\,1_{t(r)\,r^s\mid m}.
\]

Indeed, if \(t(r)\) does not divide \(m\) every indicator vanishes. If it does, and \(v=v_r(m)\), the geometric sum from the admissible levels equals \(r^{-2\max(k-1-v,0)}\). The coefficients are positive. The same identity at exponent \(1\) is the square-free weight of `BGS-TRACE-122`.

Because a raised prime does not divide \(T\), and a prime that stays at exponent \(1\) contributes no extra power,

\[
\operatorname{lcm}(t(p)\,p^s,\,t(q)\,q^u)=T\,p^sq^u
\]

throughout the range of the expansion. Set \(\alpha=2T/(pq)\), \(\sigma=a-1-s\) and \(\tau=b-1-u\). The joint levels become

\[
(1-p^{-2})(1-q^{-2})\,p^{-2\sigma}q^{-2\tau}\,R(\alpha\,p^{-\sigma}q^{-\tau}),
\]

with \(0\le\sigma<a\) and \(0\le\tau<b\). The two side series and the constant floor are the remaining three blocks of the product. Write \(\zeta=p^{-a}q^{-b}\), so the floor is \(\zeta^2R(2\zeta)\) and \(2/N=2\zeta\).

Let \(A=(1-p^{-2})(1-q^{-2})\) and extend the joint sum over the whole quadrant \(\sigma,\tau\ge0\). Replacing \(R\) by \(B\) and summing the three geometric series produces exactly

\[
U=\frac{(1+1/p)(1+1/q)}{\alpha}-\frac12+\frac{\alpha}{12}K(p)K(q),
\qquad
K(r)=\frac{r(r+1)}{r^2+r+1}.
\]

The four blocks of the actual sum are strictly smaller than the corresponding \(B\)-sums, so \(L_N(M_N;1)<U\).

The finite rectangle is termwise smaller because \(R<B\). For a fixed \(p\)-level, the side on which \(q\) has been replaced by its floor has mass equal to the mass of the quadrant \(\tau\ge b\), and its argument is \(\mu\theta\) with \(\theta=\alpha p^{-\sigma}q^{-b}\) and

\[
\mu=\frac{q\cdot\gcd(t(p),t(q))}{t(q)}.
\]

Since \(t(q)\le q+1\), one has \(\mu\ge\mu_{\min}=q/(q+1)\). The normalized quadrant weights \(w_k=(1-q^{-2})q^{-2k}\) satisfy

\[
\sum_{k\ge0}w_kB(\theta q^{-k})=B(\mu_{\min}\theta)+\frac{\theta}{12}\Bigl(K(q)-\mu_{\min}\Bigr).
\]

The difference of the two rational factors is \(q^2/((q^2+q+1)(q+1))>0\). Thus the weighted \(B\)-sum is strictly larger than \(B(\mu_{\min}\theta)\), which is itself strictly larger than \(R(\mu_{\min}\theta)\). Because \(R\) decreases, \(R(\mu\theta)\le R(\mu_{\min}\theta)\). The side is therefore strictly below its quadrant. The symmetric side is the same argument with the primes exchanged.

For the floor, the \(B\)-sum of the double tail \(\sigma\ge a\), \(\tau\ge b\) is strictly larger than \(\zeta(1+1/p)(1+1/q)/\alpha-\zeta^2/2\), because every term \(\operatorname{arg}/12\) is positive and the masses sum to \(\zeta^2\). The floor itself is strictly smaller than \(\zeta^2B(2\zeta)=\zeta/2-\zeta^2/2+\zeta^3/6\). The quadratic terms cancel. The orders satisfy \(t(p)\le p+1\) and \(t(q)\le q+1\). If both are even then their gcd is at least \(2\), so \(T\le(p+1)(q+1)/2\). If one is odd, that odd order divides the odd part of an even integer \(p-\varepsilon\) or \(q-\varepsilon\) and is at most half of \(p+1\) or \(q+1\), so again \(2T\le(p+1)(q+1)\). If both are odd the product of the halves is smaller. Hence \(\alpha\le(1+1/p)(1+1/q)\), and the difference of tail and floor is at least \(\zeta/2-\zeta^3/6\). A ratio-preserving tower has a squared factor, so \(\zeta\le1/45\). Then \(3\cdot45^2>1\) and the difference is positive.

Finally \(U\) is strictly decreasing in \(\alpha\) on the range \(\alpha\le(1+1/p)(1+1/q)\). The derivative in \(\alpha\) is negative once \(\alpha^2<12(1+1/p)(1+1/q)\), and both \(K(p)K(q)\le1\) and \((1+1/p)(1+1/q)\le8/5\) hold for odd primes \(p<q\). A lower bound on \(\alpha\) may therefore be substituted when an upper bound on \(U\) is required. Replacing \(K(q)\) by \(1\) only increases the majorant. Call that larger value \(U_1\).

## 6. The case division for the ceiling

Section 8 of `BGS-TRACE-122` places every ceiling semiprime in one of the classes below. A ratio-preserving tower has the same ratio \(\alpha=2T/(pq)\) as its radical, so the majorant depends only on that semiprime. Throughout, \(5/7-U_1\) is a ratio of integer polynomials. Both programs recompute the identity at the start of each tail and at two later integers, and they recompute the numerator, its first difference, and the constant second difference.

The five products that lie below the tails are evaluated at the actual ratio, not at an envelope.

| \(N\) | \(\alpha\) | \(U\) |
|---:|---:|---:|
| \(15\) | \(8/5\) | \(499/806\) |
| \(39\) | \(56/39\) | \(8705/14274\) |
| \(65\) | \(84/65\) | \(2283/3782\) |
| \(11\cdot13\) | \(168/143\) | \(1383/2318\) |
| \(23\cdot37\) | \(836/851\) | \(11512715/17117562\) |

Each is strictly less than \(5/7\). The product \(11\cdot13\) has actual order \(\operatorname{lcm}(12,14)=84\), so \(\alpha=168/143\). The envelope \(144/143\) is not attained, and it is not used. Likewise \(23\cdot31\) is short, and the envelope at \(q=31\) is not used.

For a fixed full order the non-short classes of `BGS-TRACE-122` have \(\alpha\ge t(p)(q-1)/(pq)\). The resulting \(U_1\) has numerator and denominator

| \(p\) | tail | \(N(q)\) | \(D(q)\) |
|---:|---:|---|---|
| \(3\) | \(q\ge23\) | \(61q^2-1097q-56\) | \(546q(q-1)\) |
| \(5\) | \(q\ge19\) | \(51q^2-877q-42\) | \(434q(q-1)\) |
| \(11\) | \(q\ge17\) | \(33q^2-541q-24\) | \(266q(q-1)\) |
| \(13\) | \(q\ge17\) | \(961q^2-15647q-686\) | \(7686q(q-1)\) |
| \(19\) | \(q\ge23\) | \(2029q^2-32633q-1400\) | \(16002q(q-1)\) |

Each denominator is positive for \(q>1\). At the start of the tail the numerator is positive, the first difference is positive, and the second difference is the positive constant \(122\), \(102\), \(66\), \(1922\), or \(4058\) respectively. The first difference therefore stays positive, and the numerator stays positive. The envelope at \(p=5\), \(q=17\) and the envelope at \(p=11\), \(q=13\) make \(U_1>5/7\); those products are respectively short and the explicit row \(11\cdot13\), so the tails begin where the numerator is positive. The only non-short product of \(5\) below its tail is \(N=65\).

For \(p=23\) the only non-short class is a full partner with gcd \(1\), and \(\alpha\ge22(q-1)/(23q)\). The orders below \(50\) are the evaluations of Section 4 of `BGS-TRACE-122` together with four further witnesses read from the same divisibility criterion. The companion value \(v_{38}\) equals \(124145519261542\) and is divisible by \(37\). The value \(u_5=41\) is divisible by \(41\). The companion value \(v_{44}\) equals \(24580185800219268\) and is divisible by \(43\). The value \(u_{23}\) equals \(318281039\) and is divisible by \(47\). Both programs recompute the recurrence, check that no smaller positive index is divisible by the prime, and deduce the orders \(38\), \(5\), \(44\), and \(23\). The products of \(23\) with \(29\), \(31\), \(41\), \(43\), and \(47\) are short. The product with \(37\) is the explicit row above. For every integer \(q\ge50\) the numerator \(533q^2-26109q-968\) is positive, by the value \(26082\) at \(q=50\), the positive first difference \(27724\), and the positive second difference \(1066\). The denominator \(12166q(q-1)\) is positive. Thus \(U_1<5/7\) on that tail.

For a split-half prime \(p\ge31\), or a non-split non-short prime \(p\ge37\), Section 8 of `BGS-TRACE-122` leaves only classes with

\[
\alpha\ge\Bigl(1-\frac1p\Bigr)\Bigl(1-\frac1q\Bigr),\qquad q\ge p+2.
\]

With both factors \(K\) replaced by \(1\), write \(U_1(p,q)\) for the resulting majorant. Set \(A=1-1/p\) and \(G=1+1/p\), so the envelope ratio is \(A(1-1/q)\) and the prefactor is \(G(1+1/q)\). The derivative of \(U_1\) in \(q\) is

\[
\frac{G}{A}\cdot\frac{-2}{(q-1)^2}+\frac{A}{12q^2}.
\]

This is negative once \(24Gq^2>A^2(q-1)^2\). Since \((q-1)/q<1\), it is enough that \(24G>A^2\), that is \(24(1+1/p)>(1-1/p)^2\), which rearranges to \(23p^2+26p-1>0\). The last polynomial is positive for every odd prime \(p\). The worst value is therefore at \(q=p+2\), where

\[
\frac57-U_1(p,p+2)=\frac{11p^3-311p^2-701p-7}{84p(p-1)(p+2)}.
\]

The denominator is positive. The numerator equals \(7092\) at \(p=31\). Its first difference \(33p^2-589p-1001\) equals \(12453\) there, and the second difference of that first difference equals \(66p-556\), which equals \(1490\) at \(p=31\) and increases. The numerator stays positive for every integer \(p\ge31\).

In every ceiling class, \(L_N(M_N;1)<U\le U_1<5/7\). Section 5 of `BGS-TRACE-120` supplies the distance statement. This is the second alternative of Theorem 1 for these towers. The gap at the attained corner \(3\cdot23\) is

\[
\frac57-\frac{108945}{158158}=\frac{575}{22594}<\frac{13}{420}.
\]

The kick is not transferred on any ceiling tower.

## 7. Towers on the side above \(3/4\)

The remaining ratio-preserving towers lie over a non-short multiple of \(7\), or in the family \(3\cdot5^b\cdot13\). A non-preserving power in either family is already short by Section 3. A split full-order partner does not occur. A product of \(3\) with a short prime is short by Section 7 of `BGS-TRACE-122`, so it is not a tower over a non-short radical.

### Split full order

The hypothesis \(t(q)=q-1\) with \(q\) split contradicts the half-order lemma of `BGS-TRACE-121`: a split order divides \((q-1)/2\). The tower is empty. It is not a kick window, and the subsum previously written for it is not used.

### The tower over \(21\)

Here \(T=\operatorname{lcm}(4,3)=12\). Raising \(3\) divides the ratio by \(3\) and Section 3 applies. Raising \(7\) preserves the ratio, because \(\delta(7)=1\) and \(7\) does not divide \(12\). For \(a\ge2\) and \(N=3\cdot7^a\), the times divisible by \(4\) and by the top two powers of \(7\) contribute

\[
\frac{48}{49}R\Bigl(\frac87\Bigr)+\frac1{49}R\Bigl(\frac8{49}\Bigr).
\]

The times divisible by \(3\cdot7^{a-1}\) but not by \(4\) have \(3\)-weight \(1/9\) and \(7\)-weight \(1\). Their contribution is \((1/9)(R(2/7)-R(8/7))\). Adding these disjoint sets gives

\[
\frac{383}{441}R\Bigl(\frac87\Bigr)+\frac1{49}R\Bigl(\frac8{49}\Bigr)+\frac19R\Bigl(\frac27\Bigr).
\]

All three arguments are strictly less than \(5\). The degree-four lower bound equals \(265028515609711/309078510309860\), which is strictly larger than \(82/105\). For \(N\le10^{26}\) the defect of Section 9 of `BGS-TRACE-122` gives the kicked gap.

### Inert full order, exponent of \(7\) at least two

Let \(\varepsilon=-1\), \(t(q)=q+1\), \(3\nmid(q+1)\) and \(q\ge13\). The primes below \(13\) in this class are excluded by Section 6 of `BGS-TRACE-122`. If \(7\) divides \(q+1\), raising \(7\) is non-preserving and Section 3 applies. Otherwise the ratio is preserved and the top two \(7\)-levels, with \(q\)-weight \(1\), contribute

\[
\frac{48}{49}R(\alpha)+\frac1{49}R(\alpha/7),
\qquad
\alpha=\frac{6(q+1)}{7q}.
\]

The ratio \(\alpha\) decreases in \(q\), so \(R\) increases. The smallest subsum is at \(q=13\), where the arguments are \(12/13\) and \(12/91\). Its degree-four lower bound equals \(26832108548323/33947639168772\), which is strictly larger than \(82/105\). For \(N\le10^{26}\) the kicked gap follows.

### Inert full order, exponent of \(7\) equal to one

Now \(a=1\) and \(b\ge2\), with the same inert hypothesis, and with \(\delta(q)=1\) so that the power of \(q\) preserves the ratio. The top \(q\)-level and the square-free \(7\)-weight contribute \((48/49)R(\alpha)+(1/49)R(\gamma)\). One \(q\)-level lower has \(q\)-weight \(q^{-2}\). Removing the overlap with the top level, the disjoint combination is

\[
\Bigl(1-q^{-2}\Bigr)\Bigl(\frac{48}{49}R(\alpha)+\frac1{49}R(\gamma)\Bigr)
+q^{-2}\Bigl(\frac{48}{49}R(\alpha/q)+\frac1{49}R(\gamma/q)\Bigr),
\]

where \(\gamma=2(q+1)/(7q)\). For each integer \(q\) from \(13\) through \(39\), every argument is strictly less than \(5\) and the degree-four lower bound exceeds \(82/105\). The value at \(q=13\) is \(16323101582366123785899971/20875800430500088687646340\). Both programs recompute all twenty-seven comparisons. Thus \(L>3/4\) on this range, and for \(N\le10^{26}\) the kicked gap follows.

For \(q\ge40\) the same subsum is strictly larger than \((1-q^{-2})\) times the two-term series at the smaller ratio belonging to \(q\). That two-term series increases with \(q\), and \(1-q^{-2}\) increases as well. Both are therefore at least their values at \(q=40\). The degree-four lower bound of the two-term series at the arguments \(123/140\) and \(41/140\), multiplied by \(1599/1600\), equals \(13146189928817400/17402756940259603\), which is strictly larger than \(3/4\) and strictly smaller than \(82/105\). Hence \(L_N(M_N;1)>3/4\) for every such tower, and the kick is not claimed once \(q\ge40\).

### Three times a short prime

Section 7 of `BGS-TRACE-122` proves that if \(q\ge5\) is short and \(T=\operatorname{lcm}(4,t(q))\), then \(12T\le15q\). The three cases are the ones used there. If \(4\) divides \(t(q)\), then \(T=t(q)\) and \(12T\le4(q+1)\le15q\). If \(t(q)\equiv2\pmod4\), then \(T=2t(q)\) and \(12T=24t(q)\le8(q+1)\le15q\). If \(t(q)\) is odd, the half-order lemma forces \(q\) to be split and \(t(q)\le(q-1)/6\le(q+1)/4\), so \(T=4t(q)\) and \(48t(q)\le12(q+1)\le15q\). Thus \(3q\) is short, and so is every higher power, by Section 2. The conditional non-short family is empty. No short prime is asserted to exist.

Both programs still recompute the unused degree-four values \(114226176533733/112075008606140\) and \(2228970493853307/2479202684534320\). Those comparisons are not a kick window.

### Powers of \(195\)

The radical \(195=3\cdot5\cdot13\) has \(T=84=2^2\cdot3\cdot7\). Thus \(3\) divides \(T\), while \(5\) does not. Also \(\delta(13)=2\). The only ratio-preserving powers are \(N=3\cdot5^b\cdot13\) with \(b\ge2\). For these, \(2t(N)/N=56/65\). The top two \(5\)-levels, on which the weights at \(3\) and at \(13\) remain \(1\) because \(4\), \(6\), and \(14\) all divide \(84\), contribute the disjoint subsum

\[
\frac{24}{25}R\Bigl(\frac{56}{65}\Bigr)+\frac1{25}R\Bigl(\frac{56}{325}\Bigr).
\]

Both arguments are strictly less than \(5\). The degree-four value \(50134551873841695/54792051773384968\) exceeds \(82/105\). The return \(R(56/65)\) alone lies below \(3/4\); both terms are required. For \(N\le10^{26}\) the kicked gap follows. The square-free case \(b=1\) remains the eight-term bound of `BGS-TRACE-123`.

## 8. The kick on products of fifteen, and the two obstructions

The windows of Theorem 2 that come from a pure margin of \(13/420\), or from strong shortness, have already been named. Two further questions were left open by `BGS-TRACE-123`.

Let \(N=15r\) with \(r\ge7\) an odd prime and \(10^{26}<N\le2\cdot10^{26}\). Then \(N\) is square-free. Section 6 of `BGS-TRACE-123` gives \(t(N)\le6(r+1)\), hence

\[
\frac{2t(N)}{N}\le\frac{4(r+1)}{5r}=\frac45+\frac{4}{5r}.
\]

Here \(r>10^{26}/15>10^{24}\), so \(4/(5r)<4/(5\cdot10^{24})<10^{-24}\). Therefore \(2t(N)/N<4/5+10^{-24}<81/100\). The return subsum is exactly \(R(2t(N)/N)\), and every other time contributes a positive trace square. Since \(R\) decreases,

\[
L_N(M_N;1)>R\Bigl(\frac{81}{100}\Bigr).
\]

The degree-four lower bound equals \(3352000000/4183386507\). Its margin over \(3/4\) is \(857840479/16733546028\).

Section 9 of `BGS-TRACE-122` estimates the kick difference by

\[
D(s)=\frac{Bs^4}{2(s-2)(10^{80}-Bs)}.
\]

The logarithmic derivative computed in Section 7 of `BGS-TRACE-120` remains positive for every real \(s>8/3\) with \(Bs<10^{80}\). At \(s=2\cdot10^{26}\) one has \(Bs<10^{80}\), so \(D\) is strictly increasing on \([3,2\cdot10^{26}]\). Both programs, and Lean, check the integer comparison \(D(2\cdot10^{26})<857840479/16733546028\). Hence \(L_N(U_N;1)>3/4\) throughout this range. Together with `BGS-TRACE-123`, the kick holds for every such \(N\le2\cdot10^{26}\).

The same comparison does not reach \(3\cdot10^{26}\): this note does not claim a larger window. The bound \(t(N)\le6(r+1)\) still does not imply \(8\,t(N)\le3N\).

The defect majorant does not decide \(u_{207}\). For every integer \(N\ge10^{78}\) with \(BN<10^{80}\),

\[
D(N)>1,
\]

because \(BN^4>2N\cdot10^{80}\) already holds at \(N=10^{78}\) and \(D\) is increasing. `BGS-TRACE-121` records that \(u_{207}\) has \(79\) digits, so \(10^{78}\le u_{207}<10^{79}\). Also \(B\cdot10^{79}<10^{80}\). The majorant at \(u_{207}\) is therefore larger than \(1\), and subtracting it from a pure value above \(3/4\) does not prove a kicked value above \(3/4\). Independently, `BGS-TRACE-119` proves \(0<\varepsilon_2<1\) and \((1-\varepsilon_2)^2<3/4\) at the index \(207\). Any lower bound of the form \(N(1-\varepsilon_2-E)\) with \(E\ge0\) stays below the threshold used there. Neither estimate proves \(L_{u_{207}}(U;1)>3/4\). The kicked statistic at that dimension stays open.

## 9. What this does not prove

Theorem 1 uses the exact trace square of the pure cat map. In the decomposition of a kicked trace into its cat-map diagonal and a signed off-diagonal sum, the second sum is untouched. Every odd dimension is now on one side of the pair of thresholds \(3/4\) and \(5/7\). Inside the windows of Theorem 2 the fixed kick does not remove the gap that has been proved. Nothing here proves that the statistic tends to \((1-e^{-2})/4\).

The ceiling majorant is an upper bound, not a kick. The inert family with exponent of \(7\) equal to one is above \(3/4\) for every partner, and the kick on that family stops at partner \(39\). The extension of the kick on \(N=15r\) stops at \(2\cdot10^{26}\). The dimension \(u_{207}\) remains outside every proved kick window. No statement counts the primes in a short, long, or split-half class. A pass of the certificate does not prove `BGS-TRACE-005` or `BGS-BGS-001`.

## 10. Certificates

The Python and C++ programs recompute the fourteen orders, the five products of \(23\) with a prime below \(50\), the five explicit majorants, the tail identities and their second differences, the cubic at primes at least \(31\), the drop inequalities, the degree-four lower bounds, the twenty-seven inert comparisons, and the defect endpoint at \(2\cdot10^{26}\). The inert-domain check requires each degree-four argument to be strictly less than \(5\), including \(\gamma\) itself. The three-times-short corners and the former split full-order subsum are not kick windows: those families are empty. The Lean file certifies the closed integer comparisons, including the displayed fraction at inert partner \(13\). The other twenty-six inert rows are recomputed by both integer programs and are not repeated in Lean. Lean does not formalize the kernel expansion, the quadrant comparison, or the kick telescoping. The analytic comparisons themselves were checked by the author and were not given an independent referee.

- `computations/verification/odd_modulus_abel.py`
- `computations/cpp/odd_modulus_abel.cpp`
- `formalization/Bgs/OddModulusRational.lean`
- `evidence/executions/20261029/odd-modulus-abel/README.md`
