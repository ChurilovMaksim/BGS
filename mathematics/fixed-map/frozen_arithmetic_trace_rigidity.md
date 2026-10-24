# Exact nonvanishing and scalar-return rigidity at the frozen coupling

**Claim ID:** `BGS-FM-010`. **Status:** project proof, independently
reconstructed algebraic steps and finite numerical regression; author-level
audit, no external referee. Adapted from the submitted
`REPORT_RU(1).md` and `NEW_RESULTS_RU(1).md` of 24 September 2026;
source hashes are in
[`record/two_continuations_review_20260924.md`](../../record/two_continuations_review_20260924.md).
The all-minor theorem `BGS-FM-008` and the common-reversor certificate
`BGS-FM-009` predate this continuation.

## Exact statement

For the unchanged odd-dimensional frozen model
\(U_N=e^{i\tau NA_N}M_N\), \(\tau=10^{-80}\), and every \(m\ge1\),
\[
 \boxed{\operatorname{Tr}U_N^m\ne0.}                         \tag{1}
\]
No positive power of \(U_N\) is scalar when \(N\ne7\); at \(N=7\)
the power \(U_7^3\) is scalar. For odd \(7\nmid N\), every
**algebraic-entry** matrix commuting with \(U_N\) is scalar. For
odd \(N\ge19\), every unitary normalizer of the finite Weyl group
commuting with \(U_N\) is scalar, including when \(7\mid N\).

These are exact nonvanishing and symmetry statements. In particular (1)
gives no useful *upper bound* on any trace. A unitary \(U_N\) with simple
spectrum has many nonalgebraic spectral projectors commuting with it;
the algebraic-entry qualification cannot be deleted. The stronger
antiunitary pair obstruction already belongs to `BGS-FM-009`.

## Arithmetic of the unperturbed cat map

Put \(h=2^{-1}\pmod N\) and
\[
(W_N(n,\ell)\psi)(x)=e_N\bigl(n(x+h\ell)\bigr)\psi(x+\ell),
\qquad C=\begin{pmatrix}3&2\\4&3\end{pmatrix}.
\]
Direct multiplication of the *raw modular* Weyl matrices gives
\(M_NW_N(u)M_N^{-1}=W_N(Cu)\).
Thus the trace of the superoperator \(\operatorname{Ad}(M_N^m)\)
is simultaneously \(|\operatorname{Tr}M_N^m|^2\) and the number
of fixed Weyl basis elements:
\[
 |\operatorname{Tr}M_N^m|^2
   =|\ker(C^m-I:(\mathbb Z/N)^2\to(\mathbb Z/N)^2)|.
                                                               \tag{2}
\]
Define integers \(u_m,v_m\) by
\[
P^m=u_mI+v_mJ,\quad
P=\begin{pmatrix}1&1\\2&1\end{pmatrix}=I+J,\quad
J^2=2I,\quad u_m+v_m\sqrt2=(1+\sqrt2)^m.
\]
Since \(C=P^2\), \((u_m+v_m\sqrt2)(u_m-v_m\sqrt2)=(-1)^m\),
and \(P,J,2\) are invertible modulo odd \(N\),
\[
C^m-I=
\begin{cases}
2u_mP^m,&m\ \mathrm{odd},\\
2v_mP^mJ,&m\ \mathrm{even}.
\end{cases}
\]
Consequently
\[
\boxed{|\operatorname{Tr}M_N^m|^2=
 \begin{cases}
   \gcd(N,u_m)^2,&m\ \mathrm{odd},\\
   \gcd(N,v_m)^2,&m\ \mathrm{even}.
 \end{cases}}                                                   \tag{3}
\]
This exact identity covers **every** odd \(N\), even when \(7\mid N\).
It implies that none of the traces of \(M_N^m\) vanishes.

## Algebraic time separates exact identities

Let \(A=A^*\) and \(M\) have algebraic entries. Every entry of
\(Z(t)=e^{itA}M\), and every polynomial in those entries with algebraic
coefficients, has the form
\(f(t)=\sum_\beta c_\beta e^{it\beta}\), with algebraic
\(c_\beta,\beta\). After equal frequencies are combined, the
Lindemann–Weierstrass theorem for exponentials of distinct algebraic
numbers ([Popescu, Theorem 3.2](https://arxiv.org/pdf/2306.14352))
shows that for any **nonzero algebraic** \(t_*\),
\[
 f(t_*)=0\quad\Longleftrightarrow\quad f\equiv0.
                                                               \tag{4}
\]
Indeed \(it_*\beta\) remain distinct algebraic numbers. Apply (4) to
\(f(t)=\operatorname{Tr}(e^{itA_N}M_N)^m\). A zero at
\(t_*=\tau N\) would force \(f(0)=\operatorname{Tr}M_N^m=0\),
contradicting (3). This proves (1) without a lower bound uniform in \(N\).

The same coefficient separation shows, for any algebraic-entry matrix
\(S\),
\[
 [S,U_N]=0\quad\Longleftrightarrow\quad
 [S,A_N]=[S,M_N]=0.                                           \tag{5}
\]
In the eigenbasis of \(A_N\), which is simple for \(7\nmid N\),
the first equality on the right makes \(S\) diagonal. Every matrix
entry of \(M_N\) in that basis is nonzero by `BGS-FM-008`;
the second equality forces all diagonal entries of \(S\) to agree.
This proves the stated algebraic-commutant corollary.

## Classification of exact scalar returns

If \(U_N^m\) is scalar at \(t_*=\tau N\), apply (4) to every
off-diagonal entry of \(Z(t)^m\) and every difference of its diagonal
entries. Then \(Z(t)^m\) is scalar **for every complex \(t\)**;
in particular \(M_N^m\) is scalar. Conversely, scalar \(M_N^m\)
implies \(C^m=I\pmod N\) because the Weyl operators span the full
matrix algebra.

For \(N\ge19\), the raw Weyl symbol of \(A_N\) has 32 distinct
nonzero modes and zero constant coefficient. At \(w=(7,0)\)
its coefficient is \(9/20\); the sum of the absolute values of
the negative real parts among all other modes is at most
\(14/125\). Hence for **every** \(C\)-orbit \(\mathcal O\)
containing \(w\),
\[
 \operatorname{Re}\sum_{u\in\mathcal O}a_u
   \ge \frac9{20}-\frac{14}{125}
   =\frac{169}{500}=:\delta>0.                              \tag{6}
\]
The other modes can only improve this bound. Set
\(S_m=\sum_{j=0}^{m-1}M_N^jA_NM_N^{-j}\).
If \(M_N^m\) is scalar, the orbit length \(L\) of \(w\)
divides \(m\). Orthogonality of the Weyl basis then gives
\[
\frac1N\operatorname{Tr}S_m^2
 \ge L\left|\frac mL\sum_{u\in\mathcal O}a_u\right|^2
 \ge\delta^2\frac{m^2}{L}\ge\delta^2m>0.                  \tag{7}
\]
But \(S_m\) has trace zero, and differentiation of \(Z(t)^m\)
at \(t=0\) gives \(iS_mM_N^m\). Were \(Z(t)^m\) scalar
for all \(t\), \(S_m\) would be scalar, then zero, in contradiction
with (7). Thus no scalar power occurs for \(N\ge19\).

For \(N=3,5,9,11,13,15,17\), the earlier `BGS-FM-008`
applies (all have \(7\nmid N\)) and yields a simple spectrum for
*every* positive power. For \(N=7\), all seven kick edges vanish,
\(A_7=(9/10)I\), and \(C^3=I\pmod7\); irreducibility of the
Weyl representation makes \(M_7^3\), hence \(U_7^3\), scalar.
This completes the classification on the whole odd sequence.

## Weyl-normalizer corollary

For odd \(N\ge19\), distinct raw kick frequencies do not alias.
The unique coefficient-modulus classes of
\(\pm(1,0)\) and \(\pm(0,1)\) are respectively
\(\sqrt{101}/200\) and \(1/200\).
A unitary Weyl normalizer preserving \(A_N\) therefore sends each
of these pairs to itself. Its action on frequency labels is
\(g=\operatorname{diag}(\varepsilon_1,\varepsilon_2)\), and
\(\det g=1\) leaves only \(g=\pm I\). For \(g=I\), matching
the two nonzero generator coefficients makes the accompanying
Weyl character trivial, so irreducibility makes the normalizer
scalar. For \(g=-I\), the pure imaginary coefficient
\(v_2=-i/400\) would require \(\chi(2,0)=-1\).
A character of the odd-order group \((\mathbb Z/N)^2\)
cannot attain \(-1\). Any unitary normalizer is algebraic up to an
irrelevant scalar phase (solve the algebraic intertwining equations
and normalize). Equation (5) then transfers this classification from
\(A_N\) to a normalizer commuting with \(U_N\).

This corollary concerns the **finite Weyl normalizer only** at
\(7\mid N\); it does not classify the entire complex commutant.
No part of this theorem controls a Heisenberg-scale trace sum or the
microscopic CUE law.

## Separately reviewed one-step companion

[Uniform squared-trace transcendence](uniform_trace_square_transcendence.md)
now covers every odd N>=3 except7 for one-step U(t) at nonzero real algebraic
t. This companion leaves the all-power theorem above and its review boundary
unchanged; no higher-power seven-divisible transcendence is inferred.
