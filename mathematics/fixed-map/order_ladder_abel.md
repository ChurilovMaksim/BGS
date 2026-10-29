# The cat-map order governs the Abel statistic

**Claim ID:** `BGS-TRACE-120`.
**Status:** project proof. The rational comparisons are typechecked in Lean 4.33.1 and recomputed in independent Python and C++ integer arithmetic. No external referee.

The argument depends on `BGS-TRACE-117` for the phase-free conjugation, the unitarity of \(M_N\), the conclusion that \(C^t\equiv I\pmod N\) makes \(M_N^t\) scalar, and the norm majorant \(B\). It does not use the one-term Pell bound of that note as a lemma. A sum over several returns is the estimate TRACE-117, Section 6, explicitly left open.

The identity \(\lvert\operatorname{Tr}M_N^m\rvert^2=\#\{v:C^mv\equiv v\pmod N\}\) is proved below from that conjugation. A form of the count appears in the historical note `mathematics/spectral_research/proofs/research_round14_2026_10_21/obstruction/r14_original_spectral_orbit_barrier.md`; that note is not a lemma here.

`BGS-TRACE-005` and `BGS-BGS-001` remain **open**.

## 1. Statements

Keep the notation of `BGS-TRACE-117`: \(N\ge3\) is odd, \(M_N\) is the cat-map quantization, \(C=\begin{pmatrix}3&2\\4&3\end{pmatrix}\), \(\tau=10^{-80}\), \(\theta=\tau N\), \(U_N=\exp(i\theta A_N)M_N\), and

\[
L_N(V;1)=N^{-2}\sum_{m\ge1}e^{-2m/N}\lvert\operatorname{Tr}V^m\rvert^2.
\]

The CUE value \((1-e^{-2})/4\) is strictly less than \(1/4\). The integers \(u_m,v_m\) and the matrix \(P=I+J\), \(J=\begin{pmatrix}0&1\\2&0\end{pmatrix}\), are those of Section 3 of that note, so \(C=P^2\) and \(P^m=u_mI+v_mJ\). Write \(t(N)\) for the least positive integer with \(C^{t(N)}\equiv I\pmod N\).

**Theorem 1 (short order, pure cat map).** If \(12\,t(N)\le5N\), then

\[
L_N(M_N;1)>\frac34,
\]

and the distance from this value to \((1-e^{-2})/4\) is greater than \(1/2\).

**Theorem 2 (long order, pure cat map).** Let \(p\) be an odd prime and \(t=t(p)\). If \(p=3\), then \(t=4\). If \(p\ge5\) and \(2t\ge p+1\), or if \(p=3\), then

\[
L_p(M_p;1)<\frac57<\frac34,
\]

and the distance from \(L_p(M_p;1)\) to \((1-e^{-2})/4\) is less than \(1/2\).

**Theorem 3 (short order, fixed kick).** If \(8\,t(N)\le3N\) and \(N\le10^{39}\), then \(L_N(U_N;1)>3/4\), and the same distance is greater than \(1/2\).

**Theorem 4 (long order, fixed kick).** Let \(p\le10^{26}\) be an odd prime satisfying the hypothesis of Theorem 2. Then \(L_p(U_p;1)<5/7\), so the statistic lies below \(3/4\) and its distance to \((1-e^{-2})/4\) is less than \(1/2\).

**Boundary.** These are order criteria, not a limit and not a statement about every odd \(N\). The dimension \(N=35\) has order \(6\), is not a Pell number \(u_n\), and its first return alone is strictly below \(3/4\); the ladder of later returns is what crosses the threshold. At the prime \(p=7\) one has \(t(7)=3\), and neither \(12\cdot3\le5\cdot7\) nor \(2\cdot3\ge8\) holds. The return subsum at that order is itself below \(3/4\); this note does not decide the full sum \(L_7(M_7;1)\). The kicked Pell dimension \(u_{207}\) has more than \(39\) digits, so Theorems 3 and 4 do not apply to it. No estimate is claimed for a generic odd \(N\) whose order lies strictly between \(5N/12\) and \((N+1)/2\), for the off-diagonal sum, or for any \(k>2\).

## 2. Trace square

For odd \(N\) and every label \((n,\ell)\),

\[
\bigl(W_N(n,\ell)\psi\bigr)(x)=e_N\bigl(n(x+2^{-1}\ell)\bigr)\psi(x+\ell).
\]

The matrix entry in row \(x\) and column \(y\) is \(e_N(n(x+\ell/2))\) when \(y\equiv x+\ell\), and \(0\) otherwise. Therefore

\[
\operatorname{Tr}\bigl(W_N(n,\ell)^*W_N(n',\ell')\bigr)
\]

vanishes when \(\ell\not\equiv\ell'\), because the two matrices have disjoint supports. When \(\ell\equiv\ell'\), the sum is

\[
\sum_{x\in\mathbb Z/N\mathbb Z}e_N\bigl((n'-n)(x+\ell/2)\bigr),
\]

which equals \(N\) if \(n\equiv n'\) and equals \(0\) otherwise. The \(N^2\) operators \(W_N(v)\) are pairwise orthogonal and nonzero in a space of dimension \(N^2\), so they are an orthogonal basis and \(\lVert W_N(v)\rVert_{\mathrm{HS}}=\sqrt N\).

Section 2 of `BGS-TRACE-117` gives \(M_NW_N(v)=W_N(Cv)M_N\). Since \(M_N\) is unitary, it is invertible, and iterating the conjugation produces

\[
M_N^mW_N(v)M_N^{-m}=W_N(C^mv).
\]

In the orthonormal basis \(W_N(v)/\sqrt N\), the trace of this conjugation is the number of labels fixed by \(C^m\). The same trace, computed in an orthonormal eigenbasis of the unitary \(M_N^m\), is \(\lvert\operatorname{Tr}M_N^m\rvert^2\). Hence, for every integer \(m\ge0\),

\[
\lvert\operatorname{Tr}M_N^m\rvert^2=\#\{v\in(\mathbb Z/N\mathbb Z)^2:C^mv\equiv v\pmod N\}.
\]

In particular, \(C^t\equiv I\pmod N\) implies that every label is fixed, so \(\lvert\operatorname{Tr}M_N^t\rvert=N\). The same section of TRACE-117 already concludes that \(M_N^t=\zeta I\) with \(\lvert\zeta\rvert=1\). Then \(M_N^{kt}=\zeta^kI\) and \(\lvert\operatorname{Tr}M_N^{kt}\rvert=N\) for every integer \(k\ge0\).

## 3. Divisibility criterion

The addition rule \(u_{a+b}=u_au_b+2v_av_b\) and \(v_{a+b}=u_av_b+v_au_b\) gives

\[
u_{2t}=u_t^2+2v_t^2,\qquad v_{2t}=2u_tv_t,
\]

and \(C^t=P^{2t}=u_{2t}I+v_{2t}J\). The norm \(u_t^2-2v_t^2=(-1)^t\) forces \(\gcd(u_t,v_t)=1\). Every \(u_t\) is odd.

If \(t\) is odd, then \(u_{2t}-1=2u_t^2\) and

\[
C^t-I=2u_tP^t.
\]

The entries of \(P^t\) are \(u_t\), \(v_t\) and \(2v_t\), with gcd \(1\), so the gcd of the entries of \(C^t-I\) is \(2u_t\). An odd \(N\) divides every entry if and only if \(N\) divides \(u_t\).

If \(t\) is even, then \(u_{2t}-1=4v_t^2\) and

\[
C^t-I=2v_t(2v_tI+u_tJ).
\]

The entries of the second factor are \(2v_t\), \(u_t\) and \(2u_t\). Their gcd is \(\gcd(2v_t,u_t)=1\), so the gcd of the entries of \(C^t-I\) is \(2v_t\). An odd \(N\) divides every entry if and only if \(N\) divides \(v_t\).

Thus \(C^t\equiv I\pmod N\) if and only if \(t\) is odd and \(N\mid u_t\), or \(t\) is even and \(N\mid v_t\). The order \(t(N)\) is the least such positive integer. It exists because \((\mathbb Z/N\mathbb Z)^2\) is finite and \(C\) is invertible.

## 4. Exact values at an odd prime

Let \(p\) be an odd prime and write \(u=u_{2m}\), \(v=v_{2m}\), so \(u^2-2v^2=1\) and

\[
C^m-I=\begin{pmatrix}u-1&v\\2v&u-1\end{pmatrix}.
\]

The determinant is \((u-1)^2-2v^2=2(1-u)\). Over \(\mathbb F_p\):

- if \(u\not\equiv1\), the matrix is invertible and the only fixed vector is \(0\);
- if \(u\equiv1\) and \(v\not\equiv0\), the matrix is \(vJ\), and \(\det J=-2\not\equiv0\), so again only \(0\) is fixed;
- if \(u\equiv1\) and \(v\equiv0\), then \(C^m\equiv I\) and every vector is fixed.

Section 3 says the third case is exactly \(t(p)\mid m\). Section 2 therefore yields

\[
\lvert\operatorname{Tr}M_p^m\rvert^2=
\begin{cases}
p^2& \text{if }t(p)\mid m,\\
1& \text{otherwise.}
\end{cases}
\]

Let \(t=t(p)\), \(y=2t/p\) and \(a=2/p\). Splitting the Abel sum gives

\[
L_p(M_p;1)
=\sum_{k\ge1}e^{-ky}
+p^{-2}\sum_{t\nmid m}e^{-am}.
\]

The first series equals \(1/(e^y-1)\). The second is nonnegative and at most

\[
p^{-2}\sum_{m\ge1}e^{-am}=p^{-2}\frac1{e^a-1}.
\]

For \(a>0\), \(e^a>1+a\), so \(1/(e^a-1)<1/a\) and the error is strictly less than \(1/(2p)\). Writing \(R(y)=1/(e^y-1)\),

\[
R(y)\le L_p(M_p;1)<R(y)+\frac1{2p}.
\]

The same return series is a lower bound for every odd \(N\), prime or not: each time \(kt(N)\) contributes exactly \(e^{-ky}\), and every other term is nonnegative.

## 5. Rational exponential bounds

For \(z>0\) and an integer \(n\ge1\) with \(z<n+1\),

\[
e^z
\le\sum_{j=0}^{n-1}\frac{z^j}{j!}
+\frac{z^n/n!}{1-z/(n+1)}.
\]

The tail after \(n-1\) is at most the displayed geometric majorant because \((n+k)!\ge n!(n+1)^k\). All partial sums of the exponential series are strict lower bounds.

At \(z=5/6\) and \(n=2\) the majorant is

\[
1+\frac56+\frac{(5/6)^2/2}{1-(5/6)/3}
=\frac{11}6+\frac{25}{52}
=\frac{361}{156}.
\]

Since \(361\cdot3=1083<1092=156\cdot7\), one has \(361/156<7/3\). Thus \(e^{5/6}\le361/156\), and

\[
\frac1{e^{5/6}-1}\ge\frac{156}{205}.
\]

Also \(156\cdot4=624>615=205\cdot3\), so \(156/205>3/4\).

At \(z=3/4\) and \(n=2\) the majorant equals \(17/8\):

\[
1+\frac34+\frac{(3/4)^2/2}{1-(3/4)/3}
=\frac74+\frac38=\frac{17}8.
\]

Hence \(e^{-3k/4}\ge(8/17)^k\). The four-term sum is

\[
\sum_{k=1}^{4}\Bigl(\frac8{17}\Bigr)^k
=\frac8{9}\Bigl(1-\Bigl(\frac8{17}\Bigr)^4\Bigr)
=\frac{70600}{83521}.
\]

The cleared comparison \(361\cdot70600>300\cdot83521\) is exactly

\[
\Bigl(\frac{19}{20}\Bigr)^2\cdot\frac{70600}{83521}>\frac34.
\]

The partial sum of \(e\) through degree \(6\) equals \(1957/720\). Since \(1957\cdot7>720\cdot19\), one has \(e>19/7\), hence \(1/(e-1)<7/12\).

The partial sum of \(e^2\) through degree \(5\) equals \(109/15>7\). Thus \(e^2>7\), \(e^{-2}<1/7\), and

\[
\frac{1-e^{-2}}4+\frac12
=\frac{3-e^{-2}}4
>\frac{3-1/7}4
=\frac57.
\]

Finally \(7/12<5/7<3/4\), because \(49<60\) and \(20<21\), and \(41/60<5/7\), because \(287<300\).

At \(z=6/7\), the partial sum through degree \(4\) equals \(5647/2401>7/3\). The verifiers recompute that sum. Therefore \(e^{6/7}>7/3\) and

\[
R(6/7)<\frac{2401}{3246}<\frac34,
\]

since \(9604<9738\). Any return time with \(y\ge6/7\) has return subsum strictly below \(3/4\).

## 6. Proof of the pure statements

Let \(t=t(N)\) and \(y=2t/N\). Sections 2 and 3 give \(\lvert\operatorname{Tr}M_N^{kt}\rvert=N\).

If \(12t\le5N\), then \(0<y\le5/6\), so \(e^y\le e^{5/6}\le361/156\) and

\[
L_N(M_N;1)
\ge\sum_{k\ge1}e^{-ky}
=\frac1{e^y-1}
\ge\frac{156}{205}
>\frac34.
\]

The CUE value is strictly less than \(1/4\), so the distance is greater than \(1/2\). This is Theorem 1. The first term of the series need not itself exceed \(3/4\); Section 10 records a dimension where it does not.

Now let \(p\) be an odd prime and \(t=t(p)\). First take \(p=3\). Then

\[
C\equiv\begin{pmatrix}0&2\\1&0\end{pmatrix}\pmod3,
\qquad
C^2\equiv -I\pmod3,
\]

so the order is exactly \(4\). Here \(y=8/3>2\), hence \(R(y)<1/(e^2-1)<1/6\). Section 4 gives

\[
L_3(M_3;1)<\frac16+\frac1{6}=\frac13<\frac57.
\]

Next take \(p\ge5\) and \(2t\ge p+1\). Then \(y\ge(p+1)/p>1\), so \(R(y)<1/(e-1)<7/12\). Section 4 gives

\[
L_p(M_p;1)
<\frac7{12}+\frac1{2p}
\le\frac7{12}+\frac1{10}
=\frac{41}{60}
<\frac57.
\]

In both cases \(L_p(M_p;1)<5/7\). Section 5 gives \(5/7<(3-e^{-2})/4\), so the distance to the CUE value is less than \(1/2\). Also \(5/7<3/4\). This is Theorem 2.

The prime \(p=7\) is not in Theorem 2: \(t(7)=3\) because \(7\mid u_3\), while \(12\cdot3=36>35=5\cdot7\) and \(2\cdot3<8\). Its return ratio equals \(6/7\), so the return subsum is below \(3/4\) by the last comparison of Section 5. The unit-trace terms of Section 4 are still present, and this note does not estimate them at \(p=7\).

## 7. The kick

Let \(B=184981/160000\) be the majorant of Section 5 of `BGS-TRACE-117`, recomputed from the same \(32\) modes by both verifiers, and set \(x=BN/10^{80}\). For \(0\le s<1\), \(\exp(s)-1\le s/(1-s)\). Whenever \(x<1\),

\[
\lVert\exp(i\theta A_N)-I\rVert
\le\frac{x}{1-x}.
\]

The telescoping identity used in that section, applied at an arbitrary positive time \(m\), gives

\[
\lvert\operatorname{Tr}U_N^m-\operatorname{Tr}M_N^m\rvert
\le Nm\frac{x}{1-x}.
\]

If \(C^t\equiv I\) and \(\rho_k=ktx/(1-x)\le1\), then \(\lvert\operatorname{Tr}U_N^{kt}\rvert\ge N(1-\rho_k)\).

### Short order

Assume \(8t\le3N\) and \(N\le10^{39}\), with \(t=t(N)\). Then \(y\le3/4\). Also

\[
\rho_4
\le4\cdot\frac{3N}8\cdot\frac{BN}{10^{80}-BN}
=\frac{(3/2)BN^2}{10^{80}-BN}.
\]

The inequality \(\rho_4\le1/20\) rearranges to \(BN(30N+1)\le10^{80}\). The left side increases with \(N\). At \(N=10^{39}\) it is the integer comparison

\[
184981\cdot10^{39}\cdot(30\cdot10^{39}+1)
<160000\cdot10^{80},
\]

which is strict, so \(\rho_4<1/20\) throughout the range, and \(x<1\). For \(1\le k\le4\),

\[
L_N(U_N;1)
\ge\sum_{k=1}^{4}e^{-ky}(1-\rho_k)^2
\ge\Bigl(\frac{19}{20}\Bigr)^2\sum_{k=1}^{4}e^{-3k/4}
\ge\Bigl(\frac{19}{20}\Bigr)^2\sum_{k=1}^{4}\Bigl(\frac8{17}\Bigr)^k
>\frac34.
\]

The distance to the CUE value is again greater than \(1/2\). This is Theorem 3.

### Long order

Let \(p\le10^{26}\) satisfy Theorem 2, and write \(a=2/p\). For each \(m\),

\[
\bigl\lvert\lvert\operatorname{Tr}U^m\rvert^2-\lvert\operatorname{Tr}M^m\rvert^2\bigr\rvert
\le2p\cdot p\cdot\frac{mx}{1-x},
\]

because both traces are at most \(p\) in modulus. Summing the Abel weights,

\[
\lvert L_p(U_p;1)-L_p(M_p;1)\rvert
\le\frac{2x}{1-x}\sum_{m\ge1}me^{-am}
=\frac{2x}{1-x}\cdot\frac{e^{a}}{(e^{a}-1)^2}.
\]

The derivative of \(e^{s}(1-s)\) is \(-se^{s}<0\) for \(s>0\), so \(e^{a}<1/(1-a)\). Combined with \(e^{a}-1>a\),

\[
\frac{e^{a}}{(e^{a}-1)^2}
<\frac1{(1-a)a^2}
=\frac{p^3}{4(p-2)}.
\]

Hence the difference is strictly less than

\[
\frac{Bp^{4}}{2(p-2)(10^{80}-Bp)}.
\]

On the interval \(3\le s\le10^{26}\) the logarithm of \(s^4/((s-2)(10^{80}-Bs))\) has derivative

\[
\frac4s-\frac1{s-2}+\frac{B}{10^{80}-Bs}
=\frac{3s-8}{s(s-2)}+\frac{B}{10^{80}-Bs}>0,
\]

so the bound increases with \(p\). Its value at the right endpoint is strictly less than \(13/420\), by the integer comparison

\[
184981\cdot(10^{26})^4\cdot420
<26\cdot(10^{26}-2)\cdot(160000\cdot10^{80}-184981\cdot10^{26}).
\]

Theorem 2 supplies \(L_p(M_p;1)<41/60\) for \(p\ge5\), and \(L_3(M_3;1)<1/3<41/60\). Therefore

\[
L_p(U_p;1)
<\frac{41}{60}+\frac{13}{420}
=\frac57.
\]

Theorem 4 follows from \(5/7<3/4\) and from \(5/7<(3-e^{-2})/4\).

## 8. A dimension where one return is not enough

The companion values through index \(6\) are

\[
\begin{align*}
u&=(1,1,3,7,17,41,99),\\
v&=(0,1,2,5,12,29,70).
\end{align*}
\]

Section 3 gives \(t(35)=6\), since \(35\mid v_6\) and \(35\) divides none of \(u_1,v_2,u_3,v_4,u_5\). The same list shows that \(35\) is not a value \(u_n\). The inequality \(12\cdot6=72\le175=5\cdot35\) puts \(N=35\) under Theorem 1, and \(8\cdot6=48\le105=3\cdot35\) together with \(35\le10^{39}\) puts it under Theorem 3.

The first return has weight \(e^{-12/35}\). The linear lower bound \(1+12/35=47/35\) already exceeds \(4/3\), because \(141>140\). Thus \(e^{12/35}>4/3\) and \(e^{-12/35}<3/4\). One return does not prove the gap. The geometric series does.

For comparison, \(t(5)=6\) as well, and \(2\cdot6\ge6\), so the prime \(5\) is on the long-order side of Theorem 2. The two theorems are not the same statement read twice.

## 9. What this does not prove

The kicked window of Theorem 3 stops at \(39\) decimal digits, and the kicked window of Theorem 4 stops at \(26\) decimal digits. Both stops are failures of these majorants when \(BN/10^{80}\) or \(Bp^3/10^{80}\) becomes large. They are not a proof that \(L_N\) drops. In particular they do not decide \(U_N\) at \(N=u_{207}\).

Theorem 2 does not say that a long-order prime has the CUE value. It says only that the Abel statistic has crossed to the CUE side of the distance \(1/2\). The unresolved orders are those with

\[
\frac{5N}{12}<t(N)<\frac{N+1}2
\]

for primes, and every composite order that fails Theorem 1. No density among primes is asserted. Passing the Python, C++ and Lean checks does not prove `BGS-TRACE-005`.

## 10. Certificates

| Check | What it certifies |
|---|---|
| `computations/verification/order_ladder_abel.py` | The series values \(361/156\), \(17/8\), \(70600/83521\), \(1957/720\), \(109/15\) and \(5647/2401\); the cleared comparisons of Section 5; the two digit-window inequalities; the gcd of \(C^t-I\) through \(t=40\); agreement of the divisibility order with the matrix order for every odd \(N\le300\); the witnesses \(N=35\), \(p=5\) and \(p=7\); the \(32\)-mode majorant; an exact cyclotomic evaluation of \(\lvert\operatorname{Tr}M_p^m\rvert^2\) at \(p=5\) and \(p=7\) |
| `computations/cpp/order_ladder_abel.cpp` | The same series values, cleared comparisons, digit windows, gcd check, order agreement through \(N=300\), witnesses and majorant, in independent integer arithmetic. It does not repeat the cyclotomic trace |
| `formalization/Bgs/OrderLadderRational.lean` | `decide` proofs of \(361/156<7/3\), \(1957/720>19/7\), \(109/15>7\), \(7/12<5/7\), \(41/60<5/7\), the four-term activity, the \(N=35\) one-return failure, the \(p=7\) return ceiling \(2401/3246<3/4\), and the two digit-window inequalities. Typechecked with Lean 4.33.1. It does not formalize Sections 2–4 or 7 |

The aggregate `lake build` was not rerun: the Mathlib cache was not present. The new module imports only the Lean prelude.
