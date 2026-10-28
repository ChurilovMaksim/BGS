# Positive-time trace expansion at the Pell dimension \(u_{205}\)

**Claim ID:** `BGS-TRACE-119`.
**Status:** project proof. The integer comparisons are typechecked in Lean 4.33.1 and recomputed in independent Python and C++ integer arithmetic. No external referee.

The argument uses `BGS-TRACE-118` for the fixed-family notation, the scalar return \(M_N^n=\zeta I\), the value \(\sum\lvert c_{kl}\rvert\le B\), the mass \(\sigma\), and the overlap proposition at \(n=205\): \(\gamma(r)=0\) for \(1\le r\le 204\) except \(\gamma(1)=\gamma(204)=-7/2000000\). It does not use the third-order operator-norm remainder of that note. That remainder is at least \(1\) at \(n=205\).

`BGS-TRACE-005` and `BGS-BGS-001` remain **open**.

## 1. Statement

Let \(n=205\) and \(N=u_{205}\), with \(\theta=\tau N\) and \(\tau=10^{-80}\). Write \(\sigma_\star=1650797/4000000\) and
\[
\varepsilon_2=\frac{n\sigma_\star\theta^2}2.
\]
The Abel statistic and the Pell companion are those of `BGS-TRACE-118`.

**Theorem.** At this single dimension,
\[
L_N(U_N;1)>\frac34.
\]
The distance from \(L_N(U_N;1)\) to \((1-e^{-2})/4\) is therefore greater than \(1/2\). The integer \(u_{205}\) has \(79\) decimal digits. Any statement that this distance is less than \(1/2\) for every odd \(N\ge N_0\) requires \(N_0>u_{205}\).

**Boundary.** The conclusion is the single dimension \(N=u_{205}\). The third-order operator-norm remainder and the Hilbert--Schmidt triangle remain silent, as proved in `BGS-TRACE-118`; the expansion below is a different estimate. At \(n=207\) the pure second-order center still satisfies \((1-\varepsilon_2)^2<3/4\), so no disk of the form \(N(1-\varepsilon_2-E)\) with \(E\ge0\) proves the gap there. The estimate does not decide \(\lim_{N\to\infty}\), a generic odd dimension, the off-diagonal sum, or any \(k>2\).

## 2. Diagram expansion

By `BGS-TRACE-118`, Sections 2 and 4,
\[
\lvert\operatorname{Tr}U_N^n\rvert=\bigl\lvert\operatorname{Tr}P(1)\bigr\rvert,
\qquad
P(t)=\prod_{j=0}^{n-1}\exp(tB_j),\qquad B_j=i\theta A_j,
\]
and the normalized trace \(\tau=\operatorname{Tr}P(1)/N\) has Taylor coefficients \(c_0=1\), \(c_1=0\) and \(c_2=-\varepsilon_2\). The same section gives \(\operatorname{Tr}(S^2)/N=n\sigma_\star\), which is the identity used for \(c_2\).

Each factor expands as \(\exp(B_j)=\sum_{k\ge0}B_j^k/k!\). Substituting \(A_j=\sum c_wW_N(C^jw)\) writes \(P(1)\) as a sum of ordered diagrams. A diagram of degree \(m\) chooses, at each time \(j\), an ordered \(k_j\)-tuple of box modes with \(\sum k_j=m\). Its scalar prefactor has modulus
\[
\frac{\theta^m}{\prod_j k_j!}\prod\lvert c\rvert.
\]

The matrix rule in `BGS-TRACE-118`, Section 3, says that \(W_N(k,\ell)\) is nonzero only on the diagonal \(y=x+\ell\), where the entry is \(e_N(k(x+\ell/2))\). The product of two such matrices is supported on the shift \(\ell+\ell'\). Its phase at \(x\) is
\[
k\bigl(x+\tfrac\ell2\bigr)+k'\bigl(x+\ell+\tfrac{\ell'}2\bigr)
=(k+k')\bigl(x+\tfrac{\ell+\ell'}2\bigr)+\tfrac{k'\ell-k\ell'}2.
\]
Since \(N\) is odd, multiplication by \(1/2\) in the exponent is integral, and the second term is an \(x\)-independent \(N\)th root of unity. Thus \(W_N(k,\ell)W_N(k',\ell')=\mu W_N(k+k',\ell+\ell')\) with \(\lvert\mu\rvert=1\). By induction, a product of any number of Weyl matrices is \(\mu W_N(v)\) with \(\lvert\mu\rvert=1\). If the labels sum to \(0\) in \((\mathbb Z/N\mathbb Z)^2\), the product is \(\mu I\) and the trace has modulus \(N\). Otherwise the trace of a single nonzero Weyl matrix vanishes, by the same one-matrix computation as in that section. Therefore only resonant diagrams contribute to \(\tau\), and the contribution of each resonant diagram has modulus equal to its absolute prefactor.

Since \(\sum\lvert c_{kl}\rvert\le B\), the sum of those prefactors over all diagrams of degree \(m\), resonant or not, is \((n\theta B)^m/m!\). Hence
\[
\lvert c_m\rvert\le\frac{x^m}{m!},\qquad x=n\theta B.
\]

## 3. Low-degree resonances are archimedean zeros

Let a diagram use \(m\le11\) modes, at \(s\le m\) distinct times. The \(s\) circular gaps are positive integers summing to \(n\), so the largest gap is at least \(\lceil n/s\rceil\ge\lceil n/m\rceil\). The circular diameter \(D\), the length of the complementary arc, therefore satisfies
\[
D\le n-\lceil n/m\rceil.
\]
For \(m\le11\) the right side is at most \(205-\lceil205/11\rceil=186\). Both verifiers check the ceiling arithmetic.

The embedding of Section 5 of `BGS-TRACE-118` gives
\[
\alpha^{2t}(2k+\ell\sqrt2)=2X+Y\sqrt2
\]
for the unreduced image \((X,Y)=C^t(k,\ell)\). Both verifiers enumerate the \(32\) nonzero modes and prove \(\lvert2k\pm\ell\sqrt2\rvert\le18\) by the integer square test. The times of a diagram are residues modulo \(n\). Let the minimal covering arc have length \(D\) and begin at a residue \(t_\ast\). For each occupied residue choose the representative \(t'\) in the integer interval \([t_\ast,t_\ast+D]\), by adding \(n\) when the residue lies before the cut. Successive differences of these representatives are the circular gaps.

The norm \(u_n^2-2v_n^2=-1\), rechecked at this odd index, expands \(\alpha^{2n}=(u_n+v_n\sqrt2)^2\) into \(u_{2n}=2u_n^2+1\) and \(v_{2n}=2u_nv_n\). Hence
\[
C^n-I=N\begin{pmatrix}2N&2v_n\\4v_n&2N\end{pmatrix}.
\]
The integer vector \(C^{t+n}(k,\ell)\) therefore differs from \(C^t(k,\ell)\) by a multiple of \(N\). Summing the arc representatives, a resonant diagram has
\[
L=\sum_j\alpha^{2t'_j}\xi_j=N(2a+b\sqrt2)
\]
for some integers \(a,b\), where \(\xi_j=2k_j+\ell_j\sqrt2\). Factor \(\alpha^{2t_\ast}\). With lags \(0\le s_j\le D\) along the arc,
\[
\lvert L\rvert\le18m\,\alpha^{2(t_\ast+D)},\qquad\lvert L'\rvert\le18m\,\alpha^{-2t_\ast},
\]
so the product is at most \((18m)^2\alpha^{2D}\). The same product bound holds when the arc does not cross the cut, because then every representative is already the original exponent.

The norm of \(2a+b\sqrt2\) is \(2(2a^2-b^2)\). It vanishes only for \(a=b=0\), and otherwise its absolute value is at least \(2\). Thus a nonzero pair \((a,b)\) would force
\[
\lvert L\rvert\,\lvert L'\rvert\ge2N^2.
\]
At \(m=11\) and \(D=186\) the verifiers and Lean prove
\[
(18\cdot11)^2\alpha^{372}<2u_{205}^2.
\]
For every smaller \(m\le11\) both the mode count and the pigeonhole diameter are smaller, and \(\alpha^{2D}\) increases with \(D\), so the same comparison applies. Hence \((a,b)=(0,0)\). Every resonant diagram of degree at most \(11\) is an exact zero in \(\mathbb Z[\sqrt2]\).

## 4. Indecomposable gaps

The identity \(L=0\) of Section 3 is an equality in \(\mathbb Z[\sqrt2]\). Factor \(\alpha^{2(t_\ast+D)}\). With lags measured backward from the latest point of the arc, the diagram is \(\sum_{i=1}^m\beta^{s_i}\xi_i=0\) in \(\mathbb R\), where \(\beta=\alpha^{-2}=3-2\sqrt2\) and \(0=s_{(1)}\le\cdots\). A wrap across the residue \(0\) is an ordinary gap in this coordinate. An indecomposable diagram has no nonempty proper submultiset of labels summing to \(0\) in \((\mathbb Z/N\mathbb Z)^2\). An archimedean zero is a modular zero, because a vanishing arc lift has vector sum \(0\). Every proper nonempty subsum is therefore a nonzero element of \(\mathbb Z[\sqrt2]\).

Consider one circular gap inside the minimal arc, of successive-time difference \(\delta\ge1\). Let the suffix on the late side of the gap use \(K\ge1\) modes, occupy lags \(0\) through \(G\), and leave \(T=m-K\ge1\) modes at lags at least \(G+\delta\). The suffix sum \(R\) is nonzero. Clearing the denominator,
\[
\Lambda=\alpha^{2G}R=\sum\alpha^{2(G-s)}\xi
\]
lies in \(\mathbb Z[\sqrt2]\). Each summand \(u+v\sqrt2\) times \(2k+\ell\sqrt2\) has even rational part, because the rational part is \(2(ku+\ell v)\). So the rational part \(P\) of \(\Lambda\) is even. The norm \(P^2-2Q^2\) is therefore divisible by \(2\), and it is a nonzero integer, so its absolute value is at least \(2\).

The conjugate satisfies \(\lvert\Lambda'\rvert\le18K\). Hence \(\lvert\Lambda\rvert\ge2/(18K)=1/(9K)\) and
\[
\lvert R\rvert=\lvert\Lambda\rvert\beta^G\ge\frac{\beta^G}{9K}.
\]
The early side contributes at most \(18T\beta^{G+\delta}\). A gap with \(\delta\ge5\) would require
\[
\frac1{9K}\le18T\beta^5,
\]
that is \(\beta^5\ge1/(162KT)\). For \(K+T\le11\) and \(K,T\ge1\) the product \(KT\) is at most \(30\), attained at \((5,6)\) and \((6,5)\). Both verifiers and Lean prove the strict inequality \(4860\beta^5<1\). Thus \(\delta\le4\).

An indecomposable diagram of degree \(m\le11\) therefore has at most \(m-1\) successive gaps inside its minimal arc, each at most \(4\), and its circular diameter is at most \(4(m-1)\). It is supported on some arc of \(W_m=4(m-1)+1\) consecutive times.

## 5. Absolute majorant

Let \(\beta=\sum\lvert c_{kl}\rvert\le B\). For a fixed set \(S\) of times, the sum of the absolute prefactors of all degree-\(m\) diagrams supported on \(S\) equals \((\lvert S\rvert\theta\beta)^m/m!\). Each time contributes the absolute generating function \(\exp(\theta\beta)\), and the degree-\(m\) part of a product of \(\lvert S\rvert\) such factors is that multinomial value. On a window of \(W\) consecutive times, the diagrams that use a distinguished endpoint therefore have total absolute mass
\[
\bigl(W^m-(W-1)^m\bigr)\frac{(\theta\beta)^m}{m!}\le\bigl(W^m-(W-1)^m\bigr)\frac{(\theta B)^m}{m!}.
\]
There are \(n\) choices for the latest endpoint of such a window. A diagram of circular diameter at most \(W-1\) is supported on the window that ends at its latest occupied time, and it uses that endpoint, so it is counted at least once. A diagram with more than one maximal gap is counted more than once. The sum of the absolute prefactors is therefore at most
\[
\Phi(m,W)=n\bigl(W^m-(W-1)^m\bigr)\frac{(\theta B)^m}{m!}.
\]

Degree-\(2\) resonances have circular diameter at most \(1\), by the overlap proposition of `BGS-TRACE-118` at \(n=205\): the only nonzero lags are \(0\), \(1\) and \(n-1\), and \(\{0,n-1\}\) is an adjacent pair on the circle. Thus their absolute activity is at most \(\Phi(2,2)\). For \(3\le m\le11\), Section 4 puts every indecomposable of degree \(m\) inside \(\Phi(m,W_m)\). Write
\[
\Phi_2=\Phi(2,2),\qquad\Phi_{\ge3}=\sum_{m=3}^{11}\Phi(m,W_m),\qquad\varphi=\Phi_2+\Phi_{\ge3}.
\]

A resonant diagram partitions into indecomposable subdiagrams by removing nonempty zero-sum submultisets until none remain. A single nonzero mode is not resonant, so every piece has degree at least \(2\). If \(k_j=\sum_a k_{j,a}\) is the split of the ordered factors at time \(j\), the absolute prefactor \(w\) of the whole diagram and the prefactors \(w_a\) of the pieces satisfy
\[
w=\prod_a w_a\cdot\prod_j\frac{\prod_a k_{j,a}!}{k_j!}\le\prod_a w_a,
\]
because \(k_j!\ge\prod_a k_{j,a}!\). The pieces of one partition are distinct diagrams. Summing \(\prod_a w_a\) over ordered \(k\)-tuples and dividing by \(k!\) therefore counts each such partition once and majorizes the sum over diagrams with at least two pieces by \(\sum_{k\ge2}\varphi_{\mathrm{true}}^k/k!\), where \(\varphi_{\mathrm{true}}\le\varphi\) is the sum of the absolute activities of the indecomposable diagrams of degree \(2\) through \(11\). A diagram of degree less than \(12\) has no piece of degree \(12\) or more. The map \(t\mapsto e^t-1-t\) is increasing for \(t\ge0\), so the multi-piece sum is at most \(e^\varphi-1-\varphi\).

The empty diagram contributes \(1\). The single degree-\(2\) diagrams contribute exactly \(c_2=-\varepsilon_2\). Every other diagram of degree at most \(11\) is either one indecomposable of degree at least \(3\), or a union of at least two indecomposables. The degree-\(\ge12\) remainder is at most \(\sum_{m\ge12}x^m/m!\). Hence
\[
\bigl\lvert\tau-(1-\varepsilon_2)\bigr\rvert
\le\bigl(e^{\varphi_{\mathrm{true}}}-1-\varphi_{\mathrm{true}}\bigr)+\Phi_{\ge3}+\sum_{m\ge12}\frac{x^m}{m!}.
\]
For \(0\le t<3\),
\[
e^t-1-t=\sum_{j\ge0}\frac{t^{2+j}}{(2+j)!}\le\frac{t^2}{2}\sum_{j\ge0}\Bigl(\frac t3\Bigr)^j=\frac{t^2}{2(1-t/3)},
\]
because \(3\cdot4\cdots(2+j)\ge3^j\). The right side increases with \(t\). The series tail increases with \(x\) on \((0,13)\), and
\[
\sum_{m\ge12}\frac{x^m}{m!}\le\frac{x^{12}}{12!}\cdot\frac1{1-x/13}.
\]

Both verifiers and Lean prove the comparisons \(x<7/2\),
\[
\Phi_2<\frac9{100},\qquad\Phi_{\ge3}<\frac1{23},\qquad\frac9{100}+\frac1{23}<\frac7{50},
\]
and
\[
\frac{(7/2)^{12}}{12!}\cdot\frac{13}{13-7/2}<\frac1{100}.
\]
Therefore \(\varphi<7/50\) and the tail is \(<1/100\), so the error is strictly less than
\[
\frac{(7/50)^2}{2\bigl(1-(7/50)/3\bigr)}+\frac1{23}+\frac1{100}=\frac{2097}{32890}<\frac1{12}.
\]
The last comparison is an integer identity, checked by both verifiers and by Lean. Thus
\[
\bigl\lvert\tau-(1-\varepsilon_2)\bigr\rvert<\frac1{12}.
\]

## 6. The Abel term

The inequality \(e^{-y}\ge1-y\) for \(y\ge0\) is the one recorded in `BGS-TRACE-118`, Section 6. One nonnegative Abel term gives
\[
L_N(U_N;1)\ge\Bigl(1-\frac{2n}N\Bigr)\lvert\tau\rvert^2.
\]
The disk bound of Section 5 yields \(\lvert\tau\rvert>1-\varepsilon_2-1/12\), and \(2n=410\). Both verifiers and Lean prove
\[
\Bigl(1-\frac{410}{u_{205}}\Bigr)\Bigl(1-\varepsilon_2-\frac1{12}\Bigr)^2>\frac34
\]
by clearing the positive denominator \(8\cdot10^{166}\). Since \((1-e^{-2})/4<1/4\), the distance to the CUE value is greater than \(1/2\).

## 7. Where this expansion stops

The same majorant does not cross \(n=207\). `BGS-TRACE-118` proves \(0<\varepsilon_2<1\) and \((1-\varepsilon_2)^2<3/4\) there. Any lower bound \(\lvert\tau\rvert\ge1-\varepsilon_2-E\) with \(E\ge0\) then lies strictly below \(\sqrt{3/4}\), and the Abel comparison built from it stays below \(3/4\). Passing that index needs a center larger than \(1-\varepsilon_2\), or a different statistic. No such improvement is proved here.

## 8. Certificates

| Check | What it certifies |
|---|---|
| `computations/verification/positive_time_spike.py` | The \(32\) modes and \(\lvert2k\pm\ell\sqrt2\rvert\le18\); the pigeonhole \(D\le186\); the norm block at \(m=11\), \(D=186\); \(4860\beta^5<1\); \(x<7/2\); \(\Phi_2<9/100\); \(\Phi_{\ge3}<1/23\); the tail bound at \(7/2\); \(2097/32890<1/12\); the cleared Abel comparison at \(E=1/12\) |
| `computations/cpp/positive_time_spike.cpp` | The same integers, in an independent base-\(10^9\) type |
| `formalization/Bgs/PositiveTimeRational.lean` | `decide` proofs of the norm block, the gap comparison, \(x<7/2\), the two activity bounds, the tail bound, the coarse chain, and the cleared Abel comparison. It does not formalize the Weyl product or the diagram expansion |

The aggregate `lake build` was not rerun: the Mathlib cache was not present. The new module imports only the Lean prelude. GitHub Actions on the preceding spike was skipped in about three seconds; this certificate was checked locally.
