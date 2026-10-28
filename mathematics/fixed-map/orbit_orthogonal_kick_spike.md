# Orbit-orthogonal kick at the Pell dimension \(u_{203}\)

**Claim ID:** `BGS-TRACE-118`.
**Status:** project proof. The integer comparisons are typechecked in Lean 4.33.1 and recomputed in independent Python and C++ integer arithmetic. No external referee.

The argument uses two facts from `BGS-TRACE-117`: the phase-free conjugation \(M_NW_N(v)=W_N(Cv)M_N\), and the scalar return \(M_N^n=\zeta I\) at \(N=u_n\) for odd \(n\ge5\). It does not use the one-term majorant of that note. At \(n=203\) that one-term majorant is at most \(3/4\).

`BGS-TRACE-005` and `BGS-BGS-001` remain **open**.

## 1. Statement

Let \(N\) be odd and at least \(3\). The operators \(W_N\), \(M_N\), \(A_N\) and \(U_N=\exp(i\tau N A_N)M_N\) are those of `BGS-TRACE-117`, with the same symbol coefficients \(c_{kl}\) and the same fixed coupling \(\tau=10^{-80}\). Write \(\theta=\tau N\) and

\[
L_N(V;1)=N^{-2}\sum_{m\ge1}e^{-2m/N}\lvert\operatorname{Tr}V^m\rvert^2.
\]

The integers \(u_m,v_m\) are the same Pell companion, and \(C=\begin{pmatrix}3&2\\4&3\end{pmatrix}\). The CUE value \((1-e^{-2})/4\) is strictly less than \(1/4\).

**Theorem.** At \(n=203\) and \(N=u_{203}\),

\[
L_N(U_N;1)>\frac34.
\]

The distance from \(L_N(U_N;1)\) to \((1-e^{-2})/4\) is therefore greater than \(1/2\). The integer \(u_{203}\) has \(78\) decimal digits. Any statement that this distance is less than \(1/2\) for every odd \(N\ge N_0\) requires \(N_0>u_{203}\).

**Boundary.** The kicked conclusion is the single dimension \(N=u_{203}\). At \(n=205\) the third-order remainder and the Hilbert--Schmidt triangle are both silent, although the pure second-order center still lies above \(3/4\). At \(n=207\) that center itself lies strictly below \(3/4\). The estimate does not decide \(\lim_{N\to\infty}\), a generic odd dimension, the off-diagonal sum, or any \(k>2\).

## 2. Transported product

By `BGS-TRACE-117`, Section 2, \(M_NW_N(k,\ell)=W_N(C(k,\ell))M_N\). Iterating and inverting the unitary \(M_N\) gives

\[
M_N^jA_NM_N^{-j}=\sum c_{kl}\,W_N(C^j(k,\ell)).
\]

Write \(A_j\) for this conjugate and \(B_j=i\theta A_j\). Then

\[
U_N^n=\Biggl(\prod_{j=0}^{n-1}\exp(i\theta A_j)\Biggr)M_N^n.
\]

By `BGS-TRACE-117`, Theorem 1, \(M_N^n=\zeta I\) with \(\lvert\zeta\rvert=1\). Hence \(\lvert\operatorname{Tr}U_N^n\rvert\) equals the modulus of the trace of the product. Section 3 of that note gives \(C^n-I=2u_nP^n\) for odd \(n\), so \(C^n\equiv I\pmod{u_n}\).

## 3. Weyl trace

The matrix \(W_N(k,\ell)\) has a nonzero entry only on the diagonal \(y=x+\ell\), where that entry is \(e_N(k(x+\ell/2))\). If \(\ell\not\equiv0\), the trace is \(0\). If \(\ell\equiv0\), the trace is \(\sum_x e_N(kx)\), equal to \(N\) when \(k\equiv0\) and equal to \(0\) otherwise. Every nonzero coefficient in the box \(\lvert k\rvert\le9\), \(\lvert\ell\rvert\le1\) has \((k,\ell)\ne(0,0)\). For \(N=u_{203}>18\) none of these labels is \(0\) in \((\mathbb Z/N)^2\), so \(\operatorname{Tr}A_N=0\).

The adjoint is \(W_N(k,\ell)^*=W_N(-k,-\ell)\). Indeed the nonzero entry of the adjoint in position \((x,x-\ell)\) is \(e_N(-k(x-\ell/2))\), which is the corresponding entry of \(W_N(-k,-\ell)\). The coefficient symmetry \(c_{-k,-\ell}=\overline{c_{kl}}\) is the same term-by-term check as in the Hermitian property of \(A_N\): \(r\) is even, the sine contribution \((r(k-1)-r(k+1))/(200i)\) conjugates to the value at \(-k\), and the modes \(\ell=\pm1\) are conjugates of each other. Both verifiers recompute all \(32\) modes and this symmetry. Consequently

\[
\operatorname{Tr}(A_N^2)=N\sigma,\qquad\sigma=\sum\lvert c_{kl}\rvert^2=\frac{66033}{160000}.
\]

The displayed value of \(\sigma\) is the exact sum produced by those verifiers.

For the product, the phase computation

\[
k\bigl(x+\tfrac\ell2\bigr)+k'\bigl(x+\ell+\tfrac{\ell'}2\bigr)
\]

shows that \(W_N(k,\ell)W_N(k',\ell')\) is diagonal precisely when \(\ell+\ell'\equiv0\), and that the diagonal phase is trivial precisely when \(k+k'\equiv0\) as well. Thus

\[
\operatorname{Tr}\bigl(W_N(v)W_N(w)\bigr)=N
\]

if \(w\equiv-v\pmod N\), and the trace is \(0\) otherwise. In particular the product of a mode with its inverse is exactly the identity, with no residual root of unity.

## 4. Second derivative

Let \(P(t)=\prod_{j=0}^{n-1}\exp(tB_j)\) and \(f(t)=\operatorname{Tr}P(t)\). Then \(f(0)=N\). Differentiating the product gives

\[
P'(0)=\sum_{j=0}^{n-1}B_j,
\]

so \(f'(0)=i\theta n\operatorname{Tr}A_N=0\). The coefficient of \(t^2\) in the expansion of the product is \(\sum_j B_j^2/2+\sum_{j<k}B_jB_k\), and therefore

\[
f''(0)=\operatorname{Tr}\Bigl(\Bigl(\sum_{j=0}^{n-1}B_j\Bigr)^2\Bigr)=-\theta^2\operatorname{Tr}(S^2),
\]

where \(S=\sum_{j=0}^{n-1}A_j\). Since each \(A_j\) is Hermitian, \(S\) is Hermitian and \(\operatorname{Tr}(S^2)\ge0\).

Expanding the square and using the trace rule of Section 3,

\[
\frac{\operatorname{Tr}(S^2)}{N}=\sum_{r=-(n-1)}^{n-1}(n-\lvert r\rvert)\,\gamma(r),
\]

where \(\gamma(r)\) is the sum of \(c_wc_z\) over support modes satisfying \(C^rz\equiv-w\pmod N\). The diagonal value is \(\gamma(0)=\sigma\). The swap \((w,z)\mapsto(z,w)\) identifies \(\gamma(-r)\) with \(\gamma(r)\), because \(C^{-r}z\equiv-w\) if and only if \(C^rw\equiv-z\), and the scalar product \(c_wc_z\) is unchanged.

## 5. The only surviving overlaps

**Proposition.** For \(N=u_{203}\) and \(1\le r\le202\), one has \(\gamma(r)=0\) except at \(r=1\) and \(r=202\), where

\[
\gamma(1)=\gamma(202)=-\frac7{2000000}.
\]

Hence \(\operatorname{Tr}(S^2)/N=n(\sigma+2\gamma(1))=n\cdot1650797/4000000\).

Both sequences \((u_m)\) and \((v_m)\) are strictly increasing for \(m\ge1\), and \(v_m\le u_m\). The second comparison is the identity \(u_m^2-v_m^2=v_m^2+(-1)^m\): the right side is nonnegative, and it is positive for every \(m\ge2\).

Let \(t=\min(r,n-r)\), so \(1\le t\le101\). Since \(C^n\equiv I\pmod N\), the power \(C^r\) is congruent to \(C^t\) or to \(C^{-t}\). With \(u=u_{2t}\) and \(v=v_{2t}\),

\[
C^t(k,\ell)=(uk+v\ell,\,2vk+u\ell),
\qquad
C^{-t}(k,\ell)=(uk-v\ell,\,-2vk+u\ell).
\]

In either case the two components are at most \(9u+v\) and \(u+18v\) in absolute value.

For \(t\le100\) one has \(2t\le200\), so those components are at most \(10u_{200}\) and \(u_{200}+18v_{200}\). The Lean witness and both integer programs prove

\[
10u_{200}+9<u_{203},\qquad u_{200}+18v_{200}+1<u_{203}.
\]

A congruence \(C^{\pm t}z\equiv-w\pmod N\) is therefore an equality of integer vectors. Applying \(C^t\) turns an inverse equality into a forward one. For \(t\ge2\) the forward equality is impossible. Indeed \(\alpha=1+\sqrt2\) gives the exact identity

\[
\alpha^{2t}(2k+\ell\sqrt2)=2X+Y\sqrt2
\]

for the components \((X,Y)\) of \(C^t(k,\ell)\). If those components equal \((-k',-\ell')\) with \(\lvert k'\rvert\le9\) and \(\lvert\ell'\rvert\le1\), then

\[
\lvert\alpha\rvert^{2t}\lvert2k+\ell\sqrt2\rvert=\lvert2k'+\ell'\sqrt2\rvert\le18+\sqrt2.
\]

For every nonzero integer pair with \(\lvert\ell\rvert\le1\), the factor \(\lvert2k+\ell\sqrt2\rvert\) is at least \(2-\sqrt2\): the values at \((\pm1,\mp1)\) attain it, \(\lvert k\rvert\ge2\) gives at least \(4-\sqrt2\), and \(\ell=\pm1,k=0\) gives \(\sqrt2\). Also

\[
(1+\sqrt2)^4(2-\sqrt2)=(17+12\sqrt2)(2-\sqrt2)=10+7\sqrt2.
\]

The comparison \(10+7\sqrt2>18+\sqrt2\) is the positive integer inequality \(104^2\cdot2>128^2\), since the difference of the squares is \(104\sqrt2-128\). Thus no exact hit exists for \(2\le t\le100\).

For \(t=1\) the image \(C(k,\ell)=(3k+2\ell,4k+3\ell)\) lies in the box \(\lvert k\rvert\le9\), \(\lvert\ell\rvert\le1\) only for \((k,\ell)\in\{(0,0),(1,-1),(-1,1)\}\). The nonzero solutions are

\[
C(1,-1)=(1,1)=-(-1,-1),\qquad C(-1,1)=(-1,-1)=-(1,1).
\]

All four labels have \(r(\pm1)=1/2\), so each coefficient is nonzero:

\[
c_{1,1}=c_{-1,1}=\frac{-3-4i}{2000},\qquad
c_{1,-1}=c_{-1,-1}=\frac{-3+4i}{2000}.
\]

The lag-\(r=1\) sum is

\[
\Bigl(\frac{-3-4i}{2000}\Bigr)^2+\Bigl(\frac{-3+4i}{2000}\Bigr)^2
=\frac{-7+24i}{4000000}+\frac{-7-24i}{4000000}
=-\frac7{2000000}.
\]

The inverse lag \(r=202\) is the same multiset of products, because \(C^{202}\equiv C^{-1}\) and \(C^{-1}\) exchanges the two pairs.

For \(t=101\) the same reduction produces a forward congruence \(C^{101}z\equiv-w\pmod N\). Write \(m=202\), \(X=u_mk+v_m\ell=-k'+au_n\) and \(Y=2v_mk+u_m\ell=-\ell'+bu_n\). The norm \(u_m^2-2v_m^2=1\) gives

\[
2X^2-Y^2=2k^2-\ell^2.
\]

Substituting the congruences, \(u_n\) divides \(Q(w)-Q(z)\) with \(Q=2k^2-\ell^2\). On the box one has \(\lvert Q\rvert\le162\), so the difference has absolute value at most \(324\). Since \(u_{203}>326\), the quadratic values agree, and

\[
u_n(2a^2-b^2)=2(2ak'-b\ell').
\]

The same programs prove \(9u_{202}+v_{202}+9<5u_{203}\) and \(u_{202}+18v_{202}+1<6u_{203}\). Therefore \(\lvert a\rvert\le4\) and \(\lvert b\rvert\le5\), and the right side has absolute value at most \(2(18\cdot4+5)=154\). A nonzero value of \(2a^2-b^2\) would make the left side at least \(u_{203}>154\). The remaining equation \(b^2=2a^2\) forces \(a=b=0\), because the \(2\)-adic valuation of the right side is odd whenever \(a\ne0\). The resulting exact equality is impossible by the archimedean bound already proved for every exponent at least \(4\).

The Python verifier scans every lag \(1\le r\le202\) and records exactly these four ordered pairs. The C++ verifier makes the same scan, counts four hits, and recomputes \(\gamma(1)=\gamma(202)=-7/2000000\).

## 6. Third-order remainder and the Abel term

Each factor \(\exp(tB_j)\) is unitary, and its \(m\)-th derivative is \(B_j^m\exp(tB_j)\), of operator norm at most \(\lVert B_j\rVert^m\). If \(\beta\) bounds every \(\lVert B_j\rVert\), the Leibniz expansion of an \(n\)-fold product has \(m\)-th derivative bounded by \(\sum_{i_1+\cdots+i_n=m}m!/(i_1!\cdots i_n!)\,\beta^m=(n\beta)^m\). The third derivative of \(P(t)\) therefore has operator norm at most \((n\beta)^3\). Each \(W_N(k,\ell)\) is unitary and there are \(32\) nonzero modes, so \(\lVert A_N\rVert\le\sum\lvert c_{kl}\rvert\). The same strict square-root majorant as in `BGS-TRACE-117` gives

\[
\sum\lvert c_{kl}\rvert\le B=\frac{184981}{160000}.
\]

Both verifiers recompute this value. Conjugation by \(M_N^j\) preserves the operator norm, so \(\lVert B_j\rVert\le\theta B\) and

\[
\lvert f'''(t)\rvert\le N(n\theta B)^3.
\]

Taylor's formula with integral remainder yields

\[
f(1)=N+\frac{f''(0)}2+\int_0^1\frac{(1-t)^2}2 f'''(t)\,dt.
\]

The integral is at most \(N(n\theta B)^3/6\) in modulus. The second-derivative term equals \(-N\varepsilon_2\) with

\[
\varepsilon_2=\frac{n\sigma_\star\theta^2}2,\qquad\sigma_\star=\frac{1650797}{4000000},
\]

and \(\theta=N/10^{80}\). Writing \(\varepsilon_3=(n\theta B)^3/6\), the disk about the positive real number \(N(1-\varepsilon_2)\) gives

\[
\lvert\operatorname{Tr}U_N^n\rvert\ge N(1-\varepsilon_2-\varepsilon_3)
\]

as soon as \(\varepsilon_2+\varepsilon_3<1\). One nonnegative Abel term produces the lower bound below. The inequality \(e^{-x}\ge1-x\) for \(x\ge0\) is the statement that \(e^{-x}-1+x\) vanishes at \(0\) and has nonnegative derivative \(1-e^{-x}\). Therefore

\[
L_N(U_N;1)\ge\Bigl(1-\frac{2n}{N}\Bigr)(1-\varepsilon_2-\varepsilon_3)^2.
\]

Clear the positive denominators \(8\cdot10^{166}\) and \(6\cdot10^{240}\cdot160000^3\). The first divides the second, with exact quotient \(3\cdot2^{96}\cdot5^{86}\). The resulting integer comparison

\[
4(u_{203}-406)(\operatorname{den}_3-\operatorname{num})^2>3u_{203}\,\operatorname{den}_3^2
\]

is proved by `decide` in `formalization/Bgs/OrbitOrthogonalRational.lean` and recomputed by the two integer programs. It is exactly \((1-406/u_{203})(1-\varepsilon_2-\varepsilon_3)^2>3/4\).

The same witness also records the coarser bounds \(\varepsilon_2<1/1000\), \(\varepsilon_3<1/25\) and \(406/u_{203}<1/1000\), and the small comparison

\[
\frac{999}{1000}\Bigl(1-\frac1{25}-\frac1{1000}\Bigr)^2>\frac34.
\]

Either form gives the theorem. Since \((1-e^{-2})/4<1/4\), the distance to the CUE value is greater than \(1/2\).

## 7. Where the second-order disk stops

At \(n=205\) the same third-order majorant satisfies \((n\theta B)^3/6\ge1\). The Lean theorem `orbit_sentinel` is this comparison. The resulting lower bound on \(\lvert\operatorname{Tr}U_N^n\rvert\) is vacuous.

The Hilbert--Schmidt triangle is silent at the same index, for a different reason. Each factor \(\exp(i\theta A_j)\) is unitary. For a real angle \(\varphi\), \(\lvert e^{i\varphi}-1\rvert^2=2-2\cos\varphi\). The inequality \(\lvert\sin u\rvert\le\lvert u\rvert\) for real \(u\) follows by writing \(\sin u=\int_0^u\cos\) and using \(\lvert\cos\rvert\le1\), and then
\[
1-\cos\varphi=2\sin^2(\varphi/2)\le\varphi^2/2.
\]
Hence \(\lvert e^{i\theta\lambda}-1\rvert^2\le\theta^2\lambda^2\). Summing the eigenvalues of \(A_j\) gives
\[
\lVert\exp(i\theta A_j)-I\rVert_{\mathrm{HS}}\le\theta\sqrt{N\sigma},
\]
with the same \(\sigma\) as in Section 3, because conjugation preserves the trace of the square. Left multiplication by a unitary preserves the Hilbert--Schmidt norm, so the telescoping product satisfies
\[
\lVert P(1)-I\rVert_{\mathrm{HS}}\le n\theta\sqrt{N\sigma}.
\]
Therefore
\[
\operatorname{Re}\operatorname{Tr}P(1)\ge N\Bigl(1-\frac{n^2\theta^2\sigma}2\Bigr)
\]
whenever the subtracted term is at most \(1\). At \(n=205\) and \(\theta=u_{205}/10^{80}\) the rational comparison
\[
205^2\cdot66033\cdot u_{205}^2>2\cdot10^{160}\cdot160000
\]
says that the subtracted term is already greater than \(1\). Lean's `orbit_hs_triangle` is this comparison. The triangle gives no positive lower bound.

The pure second-order center is a different quantity. It uses \(\operatorname{Tr}(S^2)\), not the triangle. The overlap computation of Section 5 extends to the next two odd indices.

**Proposition.** For \(n\in\{205,207\}\) and \(N=u_n\), one has \(\gamma(r)=0\) for \(1\le r\le n-1\) except at \(r=1\) and \(r=n-1\), where \(\gamma(r)=-7/2000000\). Consequently
\[
\frac{\operatorname{Tr}(S^2)}{N}=n\sigma_\star,\qquad\sigma_\star=\frac{1650797}{4000000}.
\]

The identity \(C^n\equiv I\pmod{u_n}\) is the same odd-return fact from `BGS-TRACE-117` used in Section 2. Both verifiers recheck it at these two indices. Let \(t=\min(r,n-r)\), so \(t\le102\) when \(n=205\) and \(t\le103\) when \(n=207\). For \(t\le100\) the components of \(C^{\pm t}z\) are at most \(10u_{200}\) and \(u_{200}+18v_{200}\). Those bounds are strictly smaller than \(u_{203}\), and \(u_{203}<u_{205}<u_{207}\), so a congruence modulo \(u_n\) is an integer equality. The archimedean obstruction of Section 5 then excludes every \(t\ge2\), and the lag-\(t=1\) box is unchanged.

For \(101\le t\le(n-1)/2\) the same reduction produces a forward congruence. The norm identity gives \(2X^2-Y^2=2k^2-\ell^2\), so \(u_n\) divides a quadratic difference of absolute value at most \(324\). Since \(u_n>u_{203}>326\), the quadratic values agree and
\[
u_n(2a^2-b^2)=2(2ak'-b\ell').
\]
The Lean theorem `orbit_size_next`, recomputed by both integer programs, gives the following bounds. At \(n=205\) and \(t=101\), both components force \(a=b=0\). At \(n=205\) and \(t=102\), and at \(n=207\) and \(t=103\), one has \(\lvert a\rvert\le4\) and \(\lvert b\rvert\le5\). At \(n=207\) and \(t\in\{101,102\}\) one again has \(a=b=0\). Whenever \(\lvert a\rvert\le4\) and \(\lvert b\rvert\le5\), the right-hand side is at most \(154\), while \(u_n>154\), so \(2a^2=b^2\). The \(2\)-adic valuation forces \(a=b=0\). The resulting exact equality is impossible for \(t\ge2\) by the archimedean bound already proved. Both verifiers also scan every lag at these two dimensions and record exactly the same four ordered pairs as in Section 5.

Thus, at either dimension,
\[
\varepsilon_2=\frac{n\sigma_\star\theta^2}2,\qquad\theta=\frac{u_n}{10^{80}}.
\]
Clearing the denominator \(2\cdot10^{160}\cdot4000000\), Lean's `orbit_disk_room` is the comparison
\[
\Bigl(1-\frac{410}{u_{205}}\Bigr)(1-\varepsilon_2)^2>\frac34
\]
at \(n=205\). The center of the disk still has room above \(3/4\). The proved remainders do not: the third-order count and the Hilbert--Schmidt triangle are both larger than the gap between that center and \(\sqrt{3/4}\).

At \(n=207\) the same clearing gives \(0<\varepsilon_2<1\) and \(4(1-\varepsilon_2)^2<3\). Lean's `orbit_disk_ceiling` is this pair of comparisons. Because \(1-\varepsilon_2>0\), it is exactly \((1-\varepsilon_2)^2<3/4\). Any lower bound of the form
\[
\lvert\operatorname{Tr}U_N^n\rvert\ge N(1-\varepsilon_2-\varepsilon_{\mathrm{rem}})
\]
with \(\varepsilon_{\mathrm{rem}}\ge0\) is then strictly smaller than \(N\sqrt{3/4}\). The Abel comparison built from it, including the positive factor \(1-2n/N\), stays strictly below \(3/4\). This is a failure of the disk, not a proof that \(L_N(U_N;1)\) itself drops below \(3/4\).

The classification above is stated only at \(n=205\) and \(n=207\). A new overlap at a larger odd index could decrease \(\operatorname{Tr}(S^2)\) and move the center. No such index is decided here.

## 8. Certificates

| Check | What it certifies |
|---|---|
| `computations/verification/orbit_orthogonal_spike.py` | Hermitian symmetry and the value of \(\sigma\); the majorant \(B\); the hand value of \(\gamma(1)\); the archimedean square; the box classification at lag \(1\); the Pell norm through \(m=418\); the size inequalities, including the half-period windows at \(n=205\) and \(n=207\); a direct scan of every lag at \(n=203,205,207\); the cleared gap at \(n=203\); failure of the one-term gap at \(n=203\); the vacuous third-order remainder and the vacuous Hilbert--Schmidt triangle at \(n=205\); the pure second-order room at \(n=205\) and the pure second-order ceiling at \(n=207\) |
| `computations/cpp/orbit_orthogonal_spike.cpp` | The same integers, three four-hit scans, and the same rational comparisons, in an independent base-\(10^9\) type |
| `formalization/Bgs/OrbitOrthogonalRational.lean` | `decide` proofs of the norm at \(n=203\), the size inequalities, the denominator identity, the cleared gap, the coarse majorants, the \(n=205\) sentinel, the half-period sizes, the Hilbert--Schmidt triangle, the \(n=205\) disk room, and the \(n=207\) disk ceiling. It does not formalize Sections 2--6 |

The aggregate `lake build` was not rerun: the Mathlib cache was not present. The new module imports only the Lean prelude.
