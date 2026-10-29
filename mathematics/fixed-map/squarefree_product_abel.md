# Square-free products of at least three primes

**Claim ID:** `BGS-TRACE-123`.
**Status:** project proof. The rational comparisons are typechecked in Lean 4.33.1 and recomputed in independent Python and C++ integer arithmetic. No external referee.

The argument depends on `BGS-TRACE-120` for the short-order theorem, the return-series lower bound, the comparison of the CUE value with \(1/4\), and the fixed-kick theorem under \(8\,t(N)\le3N\). It depends on `BGS-TRACE-121` for the law that an odd prime order divides \(p-\varepsilon\), and for the evaluation \(t(31)=15\). It depends on `BGS-TRACE-122` for the identification of \(t(N)\) with the least common multiple of the prime orders, for the nine orders below \(30\), for the square-free subset expansion, and for the kick-difference estimate on every odd dimension through \(10^{26}\).

`BGS-TRACE-005` and `BGS-BGS-001` remain **open**.

## 1. Statements

Keep the notation of `BGS-TRACE-120`. In particular \(N\ge3\) is odd, \(t(N)\) is the order of \(C\) modulo \(N\), and

\[
L_N(V;1)=N^{-2}\sum_{m\ge1}e^{-2m/N}\lvert\operatorname{Tr}V^m\rvert^2.
\]

The CUE value \((1-e^{-2})/4\) is strictly less than \(1/4\).

**Theorem 1 (pure cat map).** Let \(N\) be square-free and divisible by at least three distinct odd primes. Then

\[
L_N(M_N;1)>\frac34,
\]

and the distance from this value to \((1-e^{-2})/4\) is greater than \(1/2\).

**Theorem 2 (fixed kick).** Let \(\tau=10^{-80}\).

- If \(N\) is square-free, has at least four distinct prime factors, and \(N\le10^{39}\), then \(L_N(U_N;1)>3/4\).
- If \(N\) is a product of three distinct odd primes, \(15\) does not divide \(N\), and \(N\le10^{39}\), then \(L_N(U_N;1)>3/4\).
- If \(N=15r\) with \(r\) an odd prime other than \(5\), and \(N\le10^{26}\), then \(L_N(U_N;1)>3/4\).

**Boundary.** A prime square is not covered. The modulus \(315=3^2\cdot5\cdot7\) has three distinct prime factors and is not square-free; no bound is claimed there, nor for any other modulus divisible by \(p^2\). Products of two distinct primes remain the dichotomy of `BGS-TRACE-122`. No density of short, long, or split-half primes is proved. For \(N=15r>10^{26}\) the pure sum is above \(3/4\), and the kick is not claimed. The kick at \(u_{207}\) stays outside both windows. Every value above \(3/4\) lies at distance greater than \(1/2\) from the CUE value; that is the side away from \((1-e^{-2})/4\), not an identification of the limit. The signed off-diagonal sum, every \(k>2\), `BGS-TRACE-005` and `BGS-BGS-001` stay open.

## 2. Orders divide even integers

Let \(p\) be an odd prime. Theorem 1 of `BGS-TRACE-121` gives an integer \(\varepsilon=\pm1\) such that \(t(p)\) divides \(p-\varepsilon\). The integer \(p-\varepsilon\) is even and at most \(p+1\). For a square-free product \(N=\prod_{i=1}^rp_i\) of distinct odd primes, Theorem 1 of `BGS-TRACE-122` says that \(t(N)\) is the least common multiple of the orders \(t(p_i)\).

**Lemma A.** Let \(A_1,\ldots,A_r\) be positive even integers and write \(A_i=2a_i\). Then

\[
\operatorname{lcm}(A_1,\ldots,A_r)=2\operatorname{lcm}(a_1,\ldots,a_r)\le\frac{A_1\cdots A_r}{2^{r-1}}.
\]

The identity \(\operatorname{lcm}(2x,2y)=2\operatorname{lcm}(x,y)\) holds because the \(2\)-adic valuation of the left side is \(1+\max(v_2(x),v_2(y))\) and an odd prime has the same valuation on both sides. The general identity follows by induction. The inequality is \(\operatorname{lcm}(a_1,\ldots,a_r)\le a_1\cdots a_r\).

Thus, with \(A_i=p_i-\varepsilon_i\),

\[
t(N)\le\operatorname{lcm}(A_1,\ldots,A_r)\le\frac{(p_1+1)\cdots(p_r+1)}{2^{r-1}}.
\]

The first comparison holds because \(t(p_i)\) divides \(A_i\), so every prime valuation of the least common multiple of the orders is at most the corresponding valuation of \(\operatorname{lcm}(A_1,\ldots,A_r)\).

## 3. Four or more prime factors

Let \(r\ge4\). Lemma A gives

\[
8\,t(N)\le\frac{(p_1+1)\cdots(p_r+1)}{2^{r-4}}.
\]

**Lemma B.** Let \(N\ge3\) and \(s\ge1\) be integers. Then \(8s\le3N\) implies \(12s\le5N\). Indeed \(24s=3\cdot(8s)\le9N\). If \(N\) is even then \(N\ge4\) and \(9N/2\) is an integer, so \(12s\le9N/2\), and \(5N-9N/2=N/2\ge2\). If \(N\) is odd then \(9N\) is odd, so \(12s\le(9N-1)/2\), and

\[
5N-\frac{9N-1}2=\frac{N+1}2\ge2.
\]

In both cases \(12s\le5N-2\).

Sort the prime factors as \(p_1<\cdots<p_r\). Then \(p_1\ge3\), \(p_2\ge5\), \(p_3\ge7\) and \(p_4\ge11\), and the same lower bounds hold for the first \(r\) odd primes \(q_i\).

For \(r=4\), the comparisons \((p_i+1)q_i\le(q_i+1)p_i\) multiply to

\[
(p_1+1)(p_2+1)(p_3+1)(p_4+1)\cdot3\cdot5\cdot7\cdot11
\le4\cdot6\cdot8\cdot12\cdot p_1p_2p_3p_4.
\]

The integer \(4\cdot6\cdot8\cdot12=2304\) is at most \(3\cdot3\cdot5\cdot7\cdot11=3465\), so the product of \(p_i+1\) is at most \(3N\). Combined with the opening bound, \(8\,t(N)\le3N\).

For \(r\ge5\) let \(N_r=\prod_{i=1}^r(q_i+1)\), \(D_r=\prod_{i=1}^rq_i\) and \(B_r=3\cdot2^{r-4}\). The case \(r=5\) is

\[
4\cdot6\cdot8\cdot12\cdot14=32256\le6\cdot3\cdot5\cdot7\cdot11\cdot13=90090,
\]

so \(N_5\le B_5D_5\). If this holds at \(r\) and \(q\) is the next odd prime, then \(q+1\le2q\) and

\[
N_{r+1}=N_r(q+1)\le B_rD_r(q+1)\le2B_rD_rq=B_{r+1}D_{r+1}.
\]

Thus \(N_r\le B_rD_r\) for every \(r\ge5\). For a general tuple the same cross-multiplication used at \(r=4\), one prime at a time, yields

\[
\prod_{i=1}^r(p_i+1)\le B_r\prod_{i=1}^rp_i.
\]

Therefore \(8\,t(N)\le3N\). Lemma B gives \(12\,t(N)\le5N\). Theorem 1 of `BGS-TRACE-120` gives \(L_N(M_N;1)>3/4\), and the distance to the CUE value is greater than \(1/2\) because that value is strictly less than \(1/4\). If also \(N\le10^{39}\), Theorem 3 of the same note gives \(L_N(U_N;1)>3/4\).

## 4. Three prime factors, except one product

Now \(N=pqr\) with odd primes \(p<q<r\). Lemma A gives \(t(N)\le(p+1)(q+1)(r+1)/4\), hence

\[
12\,t(N)\le3(p+1)(q+1)(r+1).
\]

If \(p\ge5\), then \(q\ge7\) and \(r\ge11\). The comparisons \((p+1)\cdot5\le6p\), \((q+1)\cdot7\le8q\) and \((r+1)\cdot11\le12r\) multiply to

\[
3(p+1)(q+1)(r+1)\cdot5\cdot7\cdot11
\le3\cdot6\cdot8\cdot12\cdot pqr=1728\,pqr.
\]

Since \(1728\le1925=5\cdot5\cdot7\cdot11\), one has \(12\,t(N)\le5N\).

If \(p=3\) and \(q\ge7\), then \(r\ge11\). The same comparison at the factors \(q\) and \(r\) gives

\[
4(q+1)(r+1)\cdot7\cdot11\le4\cdot8\cdot12\cdot qr=384\,qr,
\]

and \(384\le385=5\cdot7\cdot11\). Multiplying by \(3\) produces \(12\,t(N)\le5N\).

If \(p=3\) and \(q=5\), the same estimate is \(12\,t(N)\le72(r+1)\). For every integer \(r\ge29\),

\[
75r-72(r+1)=3r-72\ge3\cdot29-72=15>0,
\]

so \(72(r+1)\le75r=5\cdot15r\). Every prime partner \(r\ge29\) is therefore short.

The only products not covered by these three paragraphs are \(N=3\cdot5\cdot r\) for a prime \(r\in\{7,11,13,17,19,23\}\). Their orders are the evaluations in Section 4 of `BGS-TRACE-122`:

| \(N\) | orders | \(t(N)\) | \(12\,t(N)\) | \(5N\) |
|---:|---|---:|---:|---:|
| \(105\) | \(4,6,3\) | \(12\) | \(144\) | \(525\) |
| \(165\) | \(4,6,12\) | \(12\) | \(144\) | \(825\) |
| \(255\) | \(4,6,8\) | \(24\) | \(288\) | \(1275\) |
| \(285\) | \(4,6,20\) | \(60\) | \(720\) | \(1425\) |
| \(345\) | \(4,6,11\) | \(132\) | \(1584\) | \(1725\) |
| \(195\) | \(4,6,14\) | \(84\) | \(1008\) | \(975\) |

The first five satisfy \(12\,t(N)\le5N\). The product \(N=195\) does not. Theorem 1 of `BGS-TRACE-120` gives the strict gap for every square-free modulus in this section except \(N=195\).

## 5. The modulus \(N=195\)

Here \(t(3)=4\), \(t(5)=6\), \(t(13)=14\) and \(t(195)=\operatorname{lcm}(4,6,14)=84\). Theorem 2 of `BGS-TRACE-122` expands the normalized trace square into the eight subset contributions. The exponential series and the geometric sum \((z^4/24)/(1-z/5)=\sum_{k\ge0}z^{4+k}/(24\cdot5^k)\), valid for \(0<z<5\), give

\[
e^z
=\sum_{j=0}^{3}\frac{z^j}{j!}
+\sum_{k\ge0}\frac{z^{4+k}}{(4+k)!}.
\]

The terms \(k=0\) and \(k=1\) agree with the majorant, because \(4!=24\) and \(5!=120=24\cdot5\). For \(k\ge2\) the factorial comparison is strict. It holds at \(k=2\), since \(720>600\), and if it holds at \(k\) then

\[
(5+k)!=(5+k)\,(4+k)!>(5+k)\cdot24\cdot5^k.
\]

The coefficient \(5+k\) is at least \(7\), hence greater than \(5\), and the right side exceeds \(24\cdot5^{k+1}\). Every later term of the exponential is therefore strictly smaller than the corresponding term of the majorant. The term of degree \(6\) is positive, so

\[
e^z
<\sum_{j=0}^{3}\frac{z^j}{j!}+\frac{z^4/24}{1-z/5}.
\]

The reciprocal comparison reverses on the positive numbers \(e^z-1\) and the same quantity formed from the majorant. Every subset order at \(N=195\) divides \(84\), so

\[
0<\frac{2d_S}{195}\le\frac{168}{195}<5,
\]

the last step being \(168<975\). Substituting the majorant for each exponential produces the rational lower bound

\[
\frac{54421025909829591004375115797555753149956840906272969117235}{53966707446709005093212565207656544939196850800058844271758}.
\]

Both programs recompute it. The comparison with \(3/4\), and with \(3/4+13/420=82/105\), is strict. Thus \(L_{195}(M_{195};1)>3/4\), and the distance to the CUE value is greater than \(1/2\).

This completes the proof of Theorem 1.

## 6. The kick

Section 9 of `BGS-TRACE-122` records that, for the fixed kick and every odd dimension \(N\le10^{26}\),

\[
\bigl\lvert L_N(U_N;1)-L_N(M_N;1)\bigr\rvert<\frac{13}{420}.
\]

In particular \(L_N(U_N;1)>3/4\) whenever \(L_N(M_N;1)>82/105\). Section 4 of `BGS-TRACE-120` also gives the return lower bound \(L_N(M_N;1)\ge R(2t(N)/N)\) for every odd \(N\), where \(R(y)=1/(e^y-1)\). The function \(R\) is strictly decreasing.

### Three primes not divisible by fifteen

The case of four or more prime factors was settled in Section 3. Let \(N=pqr\).

If \(p\ge5\), Lemma A gives \(8\,t(N)\le2(p+1)(q+1)(r+1)\). The comparisons of Section 4 multiply to

\[
2(p+1)(q+1)(r+1)\cdot5\cdot7\cdot11
\le2\cdot6\cdot8\cdot12\cdot pqr=1152\,pqr,
\]

and \(1152\le1155=3\cdot5\cdot7\cdot11\). Thus \(8\,t(N)\le3N\).

If \(p=3\) and \(q=7\), then \(r\ge11\). The orders are \(t(3)=4\) and \(t(7)=3\), so \(t(N)=\operatorname{lcm}(12,t(r))\). The positive integer \(M=r-\varepsilon\) is even and at most \(r+1\), and \(t(r)\) divides \(M\). Hence

\[
\operatorname{lcm}(12,t(r))
\le\operatorname{lcm}(12,M)
=\frac{12M}{\gcd(12,M)}
\le6M
\le6(r+1),
\]

where the middle inequality uses \(\gcd(12,M)\ge2\). Therefore \(8\,t(N)\le48(r+1)\). The difference \(63r-48(r+1)=15r-48\) equals \(117\) at \(r=11\) and increases with \(r\). Since \(3N=63r\), one has \(8\,t(N)\le3N\).

If \(p=3\) and \(q\ge11\), Lemma A gives \(8\,t(N)\le8(q+1)(r+1)\). Set

\[
g(q,r)=9qr-8(q+1)(r+1).
\]

Then \(g(q,r)-g(q,r-1)=q-8\) and \(g(q,r)-g(q-1,r)=r-8\). The three corners are

\begin{align*}
g(11,37)&=15,&
g(13,23)&=3,&
g(17,19)&=27.
\end{align*}

The first increases with \(r\) by \(3\), the second by \(5\). For every pair of integers \(q\ge17\) and \(r\ge19\), both increments are positive along a path from \((17,19)\), so \(g(q,r)\ge27\). Consequently \(8(q+1)(r+1)\le9qr=3N\), and therefore \(8\,t(N)\le3N\), except for the eight products in which the partner is too small to reach the corner:

| \(N\) | orders | \(t(N)\) | \(8\,t(N)\) | \(3N\) |
|---:|---|---:|---:|---:|
| \(429\) | \(4,12,14\) | \(84\) | \(672\) | \(1287\) |
| \(561\) | \(4,12,8\) | \(24\) | \(192\) | \(1683\) |
| \(627\) | \(4,12,20\) | \(60\) | \(480\) | \(1881\) |
| \(759\) | \(4,12,11\) | \(132\) | \(1056\) | \(2277\) |
| \(957\) | \(4,12,10\) | \(60\) | \(480\) | \(2871\) |
| \(1023\) | \(4,12,15\) | \(60\) | \(480\) | \(3069\) |
| \(663\) | \(4,14,8\) | \(56\) | \(448\) | \(1989\) |
| \(741\) | \(4,14,20\) | \(140\) | \(1120\) | \(2223\) |

The order \(t(31)=15\) is the evaluation in `BGS-TRACE-121`. Every other order in the table is one of the nine evaluations in `BGS-TRACE-122`. Each row satisfies \(8\,t(N)\le3N\).

Every product of three distinct odd primes not divisible by \(15\) therefore satisfies \(8\,t(N)\le3N\). Theorem 3 of `BGS-TRACE-120` gives the kicked gap whenever \(N\le10^{39}\).

### Products of fifteen

Let \(N=15r\) with \(r\ge7\) prime and \(r\neq5\). The same estimate as in the seven case gives \(t(N)=\operatorname{lcm}(12,t(r))\le6(r+1)\), so

\[
\frac{2t(N)}{N}\le\frac{4(r+1)}{5r}.
\]

For every integer \(r\ge37\),

\[
4(r+1)\cdot185-152\cdot5\cdot r=740-20r\le0,
\]

with equality at \(r=37\). Thus \(2t(N)/N\le152/185\). Since \(R\) decreases,

\[
L_N(M_N;1)\ge R\Bigl(\frac{2t(N)}{N}\Bigr)\ge R\Bigl(\frac{152}{185}\Bigr).
\]

The ratio \(152/185\) is strictly less than \(5\), because \(152<925\). The degree-four majorant of Section 5 produces

\[
R\Bigl(\frac{152}{185}\Bigr)
>\frac{4894346125}{6236939544}
>\frac{82}{105}.
\]

Both programs recompute the rational. For \(15r\le10^{26}\) the defect of Section 9 of `BGS-TRACE-122` therefore yields \(L_N(U_N;1)>3/4\).

The primes \(r<37\) are \(7,11,13,17,19,23,29,31\). The orders already cited give

| \(N\) | \(t(N)\) | \(8\,t(N)\) | \(3N\) |
|---:|---:|---:|---:|
| \(105\) | \(12\) | \(96\) | \(315\) |
| \(165\) | \(12\) | \(96\) | \(495\) |
| \(255\) | \(24\) | \(192\) | \(765\) |
| \(285\) | \(60\) | \(480\) | \(855\) |
| \(435\) | \(60\) | \(480\) | \(1305\) |
| \(465\) | \(60\) | \(480\) | \(1395\) |

Each of these six satisfies \(8\,t(N)\le3N\) and \(N\le10^{39}\), so Theorem 3 of `BGS-TRACE-120` applies. The two products that miss this stronger shortness are \(N=345\) and \(N=195\).

For \(N=345\), \(t(N)=132\) and \(2t(N)/N=88/115\). This ratio is strictly less than \(5\), because \(88<575\). The same majorant produces

\[
R\Bigl(\frac{88}{115}\Bigr)
>\frac{740666125}{851428424}
>\frac{82}{105}.
\]

The return lower bound and the defect give \(L_{345}(U_{345};1)>3/4\). Section 5 gives the same comparison at \(N=195\). Both dimensions are at most \(10^{26}\).

This is Theorem 2.

## 7. What this does not prove

Theorem 1 uses the exact trace square of the pure cat map. In the decomposition of a kicked trace into its cat-map diagonal and a signed off-diagonal sum, the second sum is untouched. A square-free modulus with three or more prime factors lies above \(3/4\), hence at distance greater than \(1/2\) from the CUE value. Inside the windows of Theorem 2 the fixed kick does not remove that gap. Nothing here proves that the statistic tends to \((1-e^{-2})/4\).

The bound \(t(N)\le6(r+1)\) on a product \(15r\) does not imply \(8\,t(N)\le3N\). The kick for that family is the return bound plus the defect, and it stops at \(10^{26}\). Above that window the pure sum remains above \(3/4\) and the kick is not estimated. The Pell dimension \(u_{207}\) has \(79\) digits, so neither \(10^{26}\) nor \(10^{39}\) contains it.

No statement counts the primes in a short, long, or split-half class. A pass of the certificate does not prove `BGS-TRACE-005` or `BGS-BGS-001`.

## 8. Certificates

The Python and C++ programs recompute the ten orders, every least common multiple in the tables, the corner integers, the two degree-four return bounds, and the eight-term lower bound at \(N=195\). The Lean file certifies those integer comparisons. It does not formalize the divisibility of the orders, the least-common-multiple bound, or the kick telescoping. The analytic comparisons themselves were checked by the author and were not given an independent referee.

- `computations/verification/squarefree_product_abel.py`
- `computations/cpp/squarefree_product_abel.cpp`
- `formalization/Bgs/SquarefreeProductRational.lean`
- `evidence/executions/20261029/squarefree-product/README.md`
