# Uniform Pell-orbit overlap of the fixed symbol

**Claim ID:** `BGS-TRACE-125`.
**Status:** project proof. The integer seeds, the lag-1 coefficient, the exponent-1 box count, and the exhaustive scan at \(N=41\) are typechecked in Lean 4.33.1 and recomputed in independent Python and C++ integer arithmetic. No external referee.

The argument uses two facts from `BGS-TRACE-117`: the phase-free conjugation \(M_NW_N(v)=W_N(Cv)M_N\), and the scalar return \(M_N^n=\zeta I\) at \(N=u_n\) for odd \(n\ge5\), together with the matrix form \(C^n-I=2u_nP^n\) of that return. It re-derives the lag-1 coefficient. The same coefficient at the single index \(n=203\) is `BGS-TRACE-118`, and at \(n=205\) and \(n=207\) it is `BGS-TRACE-119`. Those notes are prior special cases. Their Abel gaps are not lemmas here.

`BGS-TRACE-005` and `BGS-BGS-001` remain **open**. The reason this identity is not a disproof of `BGS-BGS-001` is recorded in the [strategy note](offdiagonal_strategy.md).

## 1. Statement

Let \(N\) be odd and at least \(3\). The operators \(W_N\), \(M_N\), and \(A_N\) are those of `BGS-TRACE-117`, with the same symbol coefficients \(c_{kl}\) and the same fixed coupling \(\tau=10^{-80}\). Write \(\theta=\tau N\) and \(U_N=\exp(i\theta A_N)M_N\). The integers \(u_m,v_m\) are the Pell companion of that note, and \(C=\begin{pmatrix}3&2\\4&3\end{pmatrix}\).

Let \(n\ge5\) be odd and set \(N=u_n\). Write \(A_j=M_N^jA_NM_N^{-j}\) and \(S=\sum_{j=0}^{n-1}A_j\). For an integer \(r\), the overlap \(\gamma(r)\) is the sum of the products \(c_wc_z\) over the nonzero modes satisfying \(C^rz\equiv-w\pmod N\).

**Theorem.** For every odd integer \(n\ge5\), at \(N=u_n\),

\[
\gamma(r)=0\qquad(1\le r\le n-1,\ r\notin\{1,n-1\}),
\]
and
\[
\gamma(1)=\gamma(n-1)=-\frac7{2000000}.
\]
Consequently
\[
\frac{\operatorname{Tr}(S^2)}{N}=n\cdot\frac{1650797}{4000000}.
\]
If \(f(t)=\operatorname{Tr}\prod_{j=0}^{n-1}\exp(ti\theta A_j)\), then \(f(0)=N\), \(f'(0)=0\), and
\[
f''(0)=-\theta^2 Nn\cdot\frac{1650797}{4000000}.
\]

**Boundary.** The indices \(n=203\), \(n=205\), and \(n=207\) are the special cases already proved. The new statement is the same coefficient for every odd \(n\ge5\). The index \(n=5\) is a finite modular scan of the two middle lags. Every odd \(n\ge7\) is the size, archimedean, and quadratic-form argument below. The identity determines the second derivative at zero coupling. It does not bound the third-order remainder, it does not give \(L_N(U_N;1)>3/4\) at any new dimension, and it does not identify the weighted off-diagonal sum at times of order \(N\). The pure cat map is already away from the CUE Abel value by `BGS-TRACE-117`, Theorem 1. `BGS-TRACE-005` and `BGS-BGS-001` remain open.

## 2. Pell arithmetic

The sequences start at \(u_0=1\), \(v_0=0\) and obey \(u_{m+1}=u_m+2v_m\), \(v_{m+1}=u_m+v_m\). The norm flips at each step:
\[
(u+2v)^2-2(u+v)^2=-(u^2-2v^2).
\]
Starting from \(u_0^2-2v_0^2=1\), one has \(u_m^2-2v_m^2=(-1)^m\). The first values are
\[
\begin{align*}
(u_1,v_1)&=(1,1),&
(u_2,v_2)&=(3,2),&
(u_3,v_3)&=(7,5),\\
(u_4,v_4)&=(17,12),&
(u_5,v_5)&=(41,29),&
(u_6,v_6)&=(99,70),\\
(u_7,v_7)&=(239,169).
\end{align*}
\]
Both verifiers and the Lean file recompute these pairs from the recurrence and check the norm. For \(m\ge1\), \(v_m\ge1\), so \(u_{m+1}-u_m=2v_m\ge2\) and \(v_{m+1}-v_m=u_m\ge1\). Thus \((u_m)_{m\ge1}\) and \((v_m)_{m\ge0}\) are strictly increasing. Also \(u_m-v_m=v_{m-1}\), so \(v_m\le u_m-1\) for every \(m\ge2\).

The closed step used below is
\[
u_{m+2}=3u_m+4v_m,\qquad v_{m+2}=2u_m+3v_m,
\]
and therefore \(u_{m+3}=7u_m+10v_m\). Two linear identities follow. First,
\[
2v_m=u_m+u_{m-1},
\]
because the right side equals \(2u_{m-1}+2v_{m-1}=2v_m\). Hence
\[
u_{m+3}-10u_m=10v_m-3u_m=2u_m+5u_{m-1},
\]
and
\[
u_{m+3}-(10u_m+9)=2u_m+5u_{m-1}-9.
\]
Second, \(3u_m-4v_m=u_{m-2}\), because substituting the step of length \(2\) cancels the \(v_{m-2}\) terms. Hence
\[
u_{m+3}-u_m-18v_m=2u_{m-2},
\]
and
\[
u_{m+3}-(u_m+18v_m+1)=2u_{m-2}-1.
\]
Both identities are used only for \(m\ge2\), where \(u_{m-2}\) is defined. The unit equation \(u_m+v_m\sqrt2=(1+\sqrt2)^m\) is the same recurrence.

By `BGS-TRACE-117`, Section 3, \(C^n-I=2u_nP^n\) for odd \(n\). Every entry of \(C^n-I\) is therefore divisible by \(u_n\), and \(C^n\equiv I\pmod{u_n}\) as a matrix over \(\mathbb Z\). The same section gives \(M_N^n=\zeta I\) with \(\lvert\zeta\rvert=1\).

## 3. Transported product and the overlap

By `BGS-TRACE-117`, Section 2, \(M_NW_N(k,\ell)=W_N(C(k,\ell))M_N\). Iterating gives
\[
A_j=\sum c_{kl}\,W_N(C^j(k,\ell)).
\]
The scalar return then gives
\[
U_N^n=\Biggl(\prod_{j=0}^{n-1}\exp(i\theta A_j)\Biggr)M_N^n,
\]
so \(\lvert\operatorname{Tr}U_N^n\rvert\) equals the modulus of the trace of the product. This identification is not used to bound that modulus. It only names the function \(f\).

The matrix \(W_N(k,\ell)\) is nonzero only on the diagonal \(y=x+\ell\). The trace vanishes when \(\ell\not\equiv0\). When \(\ell\equiv0\) it equals \(N\) if \(k\equiv0\) and equals \(0\) otherwise. Every nonzero coefficient in the box \(\lvert k\rvert\le9\), \(\lvert\ell\rvert\le1\) has \((k,\ell)\ne(0,0)\): the constant term of the symbol is removed by the centering \(-1/10\). For \(N=u_n\ge u_5=41>18\) none of these labels is \(0\) in \((\mathbb Z/N)^2\), so \(\operatorname{Tr}A_N=0\).

The adjoint is \(W_N(k,\ell)^*=W_N(-k,-\ell)\). The coefficient symmetry \(c_{-k,-\ell}=\overline{c_{kl}}\) is the term-by-term Hermitian property of \(A_N\). Both verifiers recompute all \(32\) modes and this symmetry. The product rule is the same phase count as in `BGS-TRACE-118`, Section 3: \(W_N(v)W_N(w)\) has trace \(N\) when \(w\equiv-v\pmod N\), and trace \(0\) otherwise.

Let \(P(t)=\prod_{j=0}^{n-1}\exp(tB_j)\) with \(B_j=i\theta A_j\), and let \(f(t)=\operatorname{Tr}P(t)\). Then \(f(0)=N\). Differentiating the product gives \(f'(0)=i\theta n\operatorname{Tr}A_N=0\). The second derivative is
\[
f''(0)=\operatorname{Tr}\Bigl(\Bigl(\sum_{j=0}^{n-1}B_j\Bigr)^2\Bigr)=-\theta^2\operatorname{Tr}(S^2).
\]
Expanding the square and applying the trace rule,
\[
\frac{\operatorname{Tr}(S^2)}{N}=\sum_{r=-(n-1)}^{n-1}(n-\lvert r\rvert)\,\gamma(r).
\]
The diagonal value is \(\gamma(0)=\sigma=\sum\lvert c_{kl}\rvert^2\), because \(c_{-z}=\overline{c_z}\). The swap \((w,z)\mapsto(z,w)\) identifies \(\gamma(-r)\) with \(\gamma(r)\).

The coefficients are those of `formalization/Bgs/TraceStatement.lean`. Write \(r(0)=1\), \(r(\pm1)=1/2\), \(r(\pm7)=-1/2\), \(r(\pm6)=r(\pm8)=-1/4\), and \(r(k)=0\) otherwise. Then \(c_{k0}\) is \(r(k)/10\) plus \(1/2\) at \(k=\pm7\), plus the imaginary sine term \((r(k-1)-r(k+1))/(200i)\), minus \(1/10\) at the origin. For \(\ell=\pm1\),
\[
c_{k,\pm1}=r(k)\frac{-3\mp4i}{1000}.
\]
Both verifiers sum the \(32\) squares and obtain
\[
\sigma=\frac{66033}{160000}.
\]

## 4. The lag-1 coefficient

The integer matrix \(C\) sends \((k,\ell)\) to \((3k+2\ell,4k+3\ell)\). Inside the box \(\lvert k\rvert\le9\), \(\lvert\ell\rvert\le1\), the image lies in the same box only for
\[
(k,\ell)\in\{(0,0),(1,-1),(-1,1)\}.
\]
Indeed \(\lvert4k+3\ell\rvert\le1\) forces \(\lvert k\rvert\le1\). The case \(k=0\) forces \(\ell=0\). The case \(k=\pm1\) forces \(\ell=\mp1\), and those two images are \((1,1)\) and \((-1,-1)\). The Lean file decides that these three domain points are box hits and that the box count is exactly three. The inverse matrix \(C^{-1}=\begin{pmatrix}3&-2\\-4&3\end{pmatrix}\) has exactly the three box hits \((0,0)\), \((1,1)\), and \((-1,-1)\), by the same decision.

The origin is not a nonzero mode. The two nonzero solutions are
\[
C(1,-1)=(1,1)=-(-1,-1),\qquad C(-1,1)=(-1,-1)=-(1,1).
\]
Since \(r(\pm1)=1/2\),
\[
c_{1,1}=c_{-1,1}=\frac{-3-4i}{2000},\qquad
c_{1,-1}=c_{-1,-1}=\frac{-3+4i}{2000}.
\]
The lag-\(r=1\) sum is the sum of the two squares
\[
\Bigl(\frac{-3-4i}{2000}\Bigr)^2+\Bigl(\frac{-3+4i}{2000}\Bigr)^2
=\frac{-7+24i}{4000000}+\frac{-7-24i}{4000000}
=-\frac7{2000000}.
\]
Both verifiers recompute the same value from the full coefficient table, not from this four-term shortcut alone. The shortcut is the evaluation of those four table entries.

## 5. No modular wrap off the middle index

Let \(1\le r\le n-1\) and set \(t=\min(r,n-r)\), so \(1\le t\le(n-1)/2\). Since \(C^n\equiv I\pmod N\), the power \(C^r\) is congruent to \(C^t\) or to \(C^{-t}\). With \(u=u_{2t}\) and \(v=v_{2t}\),
\[
C^t(k,\ell)=(uk+v\ell,\,2vk+u\ell),
\qquad
C^{-t}(k,\ell)=(uk-v\ell,\,-2vk+u\ell).
\]
On the box, the absolute values are at most \(9u+v\) and \(u+18v\).

Consider first \(1\le t\le(n-3)/2\), so \(2\le 2t\le n-3\). The sequences are increasing on this range, and the largest bounds occur at \(m=n-3\ge2\). There \(v_m\le u_m-1\), so
\[
9u_m+v_m+9\le10u_m+8<10u_m+9.
\]
The linear identity of Section 2 gives
\[
u_n-(10u_m+9)=2u_m+5u_{m-1}-9.
\]
At \(n=5\), this difference is \(2\cdot3+5\cdot1-9=2\). At \(n\ge7\), one has \(m\ge4\), so \(u_m\ge17\) and \(u_{m-1}\ge7\), and the difference is at least \(2\cdot17+5\cdot7-9=60\). In every case \(10u_m+9<u_n\), hence \(9u_m+v_m+9<u_n\). The second component satisfies
\[
u_n-(u_m+18v_m+1)=2u_{n-5}-1.
\]
At \(n=5\) the right side is \(2u_0-1=1\). At \(n\ge7\) it is at least \(2u_2-1=5\). Thus both
\[
9u_m+v_m+9<u_n,\qquad u_m+18v_m+1<u_n
\]
hold for every odd \(n\ge5\). A congruence \(C^{\pm t}z\equiv-w\pmod N\), with both labels in the box, is therefore an equality of integer vectors: the difference of each coordinate is divisible by \(N\) and strictly smaller than \(N\) in absolute value.

Applying \(C^t\) turns an inverse equality into a forward equality. For \(t\ge2\) the forward equality is impossible, by the next section. The only remaining possibility inside this range is \(t=1\), whose nonzero solutions are the two pairs of Section 4. Those pairs occur at \(r=1\) and, through \(C^{-1}\), at \(r=n-1\). Every other lag with \(t\le(n-3)/2\) has \(\gamma(r)=0\).

For \(n=5\) the inequality \(t\le(n-3)/2\) is exactly \(t=1\). The middle value \(t=2\) is Section 8. For every odd \(n\ge7\) the only index outside this range is the single middle index \(t=(n-1)/2\), treated in Section 7.

## 6. The archimedean gap

Let \(\alpha=1+\sqrt2\). The component formulae and the unit equation give, for the forward image \((X,Y)=C^t(k,\ell)\),
\[
\alpha^{2t}(2k+\ell\sqrt2)=(u_{2t}+v_{2t}\sqrt2)(2k+\ell\sqrt2)=2X+Y\sqrt2.
\]
Suppose \(t\ge2\) and \((X,Y)=(-k',-\ell')\) with \(\lvert k'\rvert\le9\) and \(\lvert\ell'\rvert\le1\). Then
\[
\alpha^{2t}\lvert2k+\ell\sqrt2\rvert=\lvert2k'+\ell'\sqrt2\rvert\le18+\sqrt2.
\]
If \((k,\ell)=(0,0)\), the image is the origin, which is not a nonzero mode. If \((k,\ell)\ne(0,0)\) and \(\lvert\ell\rvert\le1\), the factor \(\lvert2k+\ell\sqrt2\rvert\) is at least \(2-\sqrt2\). The pairs \((\pm1,\mp1)\) attain it. The line \(\ell=0\) gives at least \(2>2-\sqrt2\). The line \(k=0\), \(\ell=\pm1\), gives \(\sqrt2\), and \(\sqrt2>2-\sqrt2\) because \(\sqrt2>1\). Every \(\lvert k\rvert\ge2\) gives at least \(4-\sqrt2>2-\sqrt2\).

The fourth power is
\[
(1+\sqrt2)^4=(3+2\sqrt2)^2=17+12\sqrt2,
\]
and
\[
(17+12\sqrt2)(2-\sqrt2)=10+7\sqrt2.
\]
The comparison \(10+7\sqrt2>18+\sqrt2\) is the positive integer inequality \(104^2\cdot2>128^2\): the difference of the squares is \(104\sqrt2-128\), and \(104^2\cdot2-128^2=5248\). Both verifiers and the Lean file decide this comparison. Therefore
\[
\alpha^{4}(2-\sqrt2)>18+\sqrt2,
\]
and no exact box hit exists for any \(t\ge2\). Combined with Section 5, every non-middle lag is settled for every odd \(n\ge5\): the overlap vanishes except at \(r=1\) and \(r=n-1\), where it equals \(-7/2000000\).

## 7. The middle index, for every odd \(n\ge7\)

Let \(n\ge7\) be odd and set \(t=(n-1)/2\ge3\), \(m=n-1\), \(u=u_m\), and \(v=v_m\). Then \(m\ge6\) is even, so \(u^2-2v^2=1\), and \(u\ge u_6=99\ge17\). A congruence \(C^tz\equiv-w\pmod N\) reads
\[
X=uk+v\ell=-k'+aN,\qquad Y=2vk+u\ell=-\ell'+bN,
\]
with \(\lvert k'\rvert\le9\) and \(\lvert\ell'\rvert\le1\). The bounds \(\lvert X\rvert\le9u+v\) and \(\lvert Y\rvert\le u+18v\) give
\[
\lvert a\rvert N\le9u+v+9,\qquad \lvert b\rvert N\le u+18v+1.
\]
The recurrence \(u_n=u+2v\) converts these into comparisons with \(u\) and \(v\). The first is strict once \(9v>4u+9\), because
\[
5u_n-(9u+v+9)=9v-4u-9.
\]
Both \(9v\) and \(4u+9\) are positive. Squaring and clearing the denominator \(2\) in \(v^2=(u^2-1)/2\) gives
\[
81(u^2-1)-2(4u+9)^2=49u^2-144u-243.
\]
Call the right side \(f(u)\). The difference \(f(s+1)-f(s)=98s-95\). For every integer \(s\ge17\) this linear form is at least \(98\cdot17-95=1571>0\). The value \(f(17)=11470\) is positive. By induction \(f(s)>0\) for every integer \(s\ge17\), so \(9v>4u+9\). Thus \(\lvert a\rvert\le4\).

The second comparison is strict once \(5u-1>6v\). Both sides are positive for \(u\ge17\). Squaring and using \(36v^2=18(u^2-1)\) produces
\[
(5u-1)^2-18(u^2-1)=7u^2-10u+19.
\]
The identity
\[
7(7u^2-10u+19)=(7u-5)^2+108\ge108
\]
shows that the quadratic is positive for every integer \(u\). Thus \(\lvert b\rvert\le5\).

The norm identity \(2X^2-Y^2=(u^2-2v^2)(2k^2-\ell^2)\) collapses to \(Q(k,\ell)=2k^2-\ell^2\). Substituting the congruences,
\[
Q(z)-Q(w)=N\bigl(-4ak'+2b\ell'+N(2a^2-b^2)\bigr).
\]
On the box, \(2k^2\le162\) and \(\ell^2\le1\), so \(-1\le Q\le162\) and \(\lvert Q(z)-Q(w)\rvert\le163\). For \(n\ge7\), \(N=u_n\ge u_7=239>163\). The two quadratic values therefore agree, and
\[
N(2a^2-b^2)=2(2ak'-b\ell').
\]
The right side has absolute value at most \(2(2\cdot4\cdot9+5)=154\). A nonzero value of \(2a^2-b^2\) would make the left side at least \(N>154\).

The remaining equation \(b^2=2a^2\) forces \(a=b=0\). If \(a\ne0\), then \(b\) is even. Writing \(b=2c\) gives \(a^2=2c^2\), so \(a\) is even. Writing \(a=2a_1\) gives \(c^2=2a_1^2\). The positive integer \(\lvert a_1\rvert=\lvert a\rvert/2\) satisfies the same equation, and descent is impossible. The resulting exact equality \(C^tz=-w\) has exponent \(t\ge3\ge2\), which Section 6 forbids.

Thus \(\gamma(r)=0\) at the two middle lags \(r=t\) and \(r=n-t\) as well. This completes the argument for every odd \(n\ge7\).

## 8. The index \(n=5\)

At \(n=5\), one has \(N=u_5=41\) and middle index \(t=2\). Section 5 already gives \(\gamma(1)=\gamma(4)=-7/2000000\) and excludes every non-middle mechanism. The divisibility of Section 7 does not apply: \(163>41\), so equal quadratic values are not forced. The two lags \(r=2\) and \(r=3\) are a finite computation.

There are \(32\) nonzero modes. Both verifiers, and the Lean file, test every ordered pair of them against \(C^2\) and \(C^3\) modulo \(41\). No pair satisfies the congruence. The same scan repeats the lags \(r=1\) and \(r=4\) and recovers exactly the two ordered pairs of Section 4 at each of those lags, with the same rational overlap. The Lean decision is the boolean `middleScan`. The Python and C++ scans at \(n=7\), \(n=9\), and \(n=11\) repeat the same count on three indices already covered by Section 7. Those three scans are checks. They are not the argument for \(n\ge7\).

## 9. Assembly

For every odd \(n\ge5\),
\[
\frac{\operatorname{Tr}(S^2)}{N}
=n\sigma+2(n-1)\gamma(1)+2\gamma(1)
=n\Bigl(\sigma+2\gamma(1)\Bigr).
\]
The rational arithmetic
\[
\frac{66033}{160000}+2\Bigl(-\frac7{2000000}\Bigr)
=\frac{66033\cdot25-28}{4000000}
=\frac{1650797}{4000000}
\]
is the identity \(66033\cdot25-28=1650797\) together with \(160000\cdot25=4000000\). Both verifiers recompute it from the summed squares and the summed lag-1 products. Therefore
\[
\frac{\operatorname{Tr}(S^2)}{N}=n\cdot\frac{1650797}{4000000},
\]
and \(f''(0)\) is the displayed multiple of \(-\theta^2 N\).

The second-order center built from this coefficient is an explicit function of \(n\). `BGS-TRACE-119` already shows that the center lies below \(3/4\) at \(n=207\). The present theorem does not turn that fact into a bound on \(L_N(U_N;1)\), because the integral remainder is not estimated. Times of order \(N\) remain outside the short return \(n\ll N\).

## 10. Certificate scope

- `computations/verification/uniform_orbit_overlap.py`
- `computations/cpp/uniform_orbit_overlap.cpp`
- `formalization/Bgs/UniformOrbitOverlapRational.lean`
- `evidence/executions/20261029/uniform-orbit-overlap/receipt.json`

The three certificates recompute the \(32\) modes, the mass \(\sigma\), the Hermitian symmetry, the exact lag-1 products, the exponent-1 box count, the archimedean integer \(5248\), the quadratic seeds \(f(17)\) and \(98\cdot17-95\), the positivity identity for \(7u^2-10u+19\), the Pell values through \(u_7\), and the exhaustive pair scan at \(N=41\). A pass does not prove `BGS-TRACE-005`.
