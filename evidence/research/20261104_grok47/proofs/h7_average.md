# The averaged operator for the section aggregate

Tags in this file are local to the note. **[P]** is proved here, or is an external theorem with the locator named in the sentence. **[CA]** is a finite enclosure in ball arithmetic. **[N]** is a floating-point observation. A finite enclosure is not an asymptotic bound, and it is not an enclosure of \(\sum_\beta\kappa\hat Z\). `record/claims.json` was not edited.

The question is whether
\[
S_a=\sum_{\beta\not\equiv 0}\kappa_d(N\beta)\,\operatorname{Tr} Q_{\beta,a}
\]
at \(d=3437426497=457\cdot 7521721\), \(P=57\), sector \(a=0\), can be written as the trace of one operator, and whether the norm or the spectral radius of that operator puts \(|S_0|\) under the \(\eta=1\) threshold of `proofs/h7_lin.md` §5. The operator is identified. Its weighted norm is at most \(246/100\), the cap of `proofs/h7_uniform.md`. The two trace majorants that follow from that norm both exceed the threshold, and both are coarser than the triangle bound already computed there. One arithmetic piece, the constant term in the Gauss transform of \(\kappa_d\), lies under the threshold. The complementary piece is not bounded under the threshold.

The section, the product formula for \(\kappa_d\), and the threshold are those of `proofs/h7_multidisc.md`, `proofs/h7_lin.md`, and `proofs/h7_uniform.md`. This note does not replace them.

## 1. The operator [P]

Let \(\mathcal O=\mathbb Z[\sqrt 2]\) and let \(G=\mathcal O/d\mathcal O\), a group of order \(d^2\). A class \(\beta=b_x+b_y\sqrt 2\) is a residue, not an element of \(\mathbb Z/d\mathbb Z\). The trace pairing on \(G\) is the field trace
\[
\operatorname{Tr}(\beta\xi)=2(b_x\xi_x+2b_y\xi_y)\pmod d,
\]
which is the pairing used by `h7_multidisc.py` for the twist \(\tau_j=\operatorname{Tr}(\beta\lambda^j)\). For \(d\) odd this pairing is nondegenerate: the coefficient matrix is \(2\operatorname{diag}(1,2)\), of determinant \(8\), coprime to \(d\).

Let \(V\) be the section space, dimension \(280\). On \(H=V\otimes\ell^2(G)\),
\[
(T\Phi)(\beta)=L\bigl(\operatorname{Tr}(\beta)/d\bigr)\,\Phi(\lambda^{-1}\beta),
\qquad
(M\Phi)(\beta)=\kappa_d(N\beta)\,\Phi(\beta).
\]
Here \(L(t)=\sum_{|n|\le 16}e(nt)A_n\) is the section step of `proofs/h7_uniform.md` §1, and \(N(\beta)=b_x^2-2b_y^2\). Since \(N(\lambda)=1\), one has \(N(\lambda\beta)=N(\beta)\), so \(MT=TM\).

**Theorem 1.** \(\operatorname{Tr}_H(MT^P)=\sum_{\beta\in G}\kappa_d(N\beta)\,\operatorname{Tr} Q_\beta\), where \(Q_\beta=\prod_{j=0}^{P-1}L(\operatorname{Tr}(\beta\lambda^j)/d)\) and the product is ordered so that \(j=0\) is the rightmost factor. The Lin section sum is this trace with the identity class removed,
\[
S=\operatorname{Tr}_H(MT^P)-\kappa_d(0)\,\operatorname{Tr} Q_0.
\]
At a prime \(q\parallel h_m\), \(\kappa_q(0)=q-2\). At \(d=q_1q_2\), Lemma 1 of `proofs/h7_lin.md` gives \(\kappa_d(0)=(q_1-2)(q_2-2)\).

*Proof.* The fibre at \(\lambda^{-1}\beta\) is sent to the fibre at \(\beta\) by \(L(\operatorname{Tr}(\beta)/d)\). After \(P\) steps, \(\lambda^{-P}\equiv 1\), and
\[
(T^P\Phi)(\beta)=L(\tau_0)L(\tau_{-1})\cdots L(\tau_{-(P-1)})\,\Phi(\beta),
\]
with \(\tau_j=\operatorname{Tr}(\beta\lambda^j)/d\). The trace of a product is invariant under cyclic permutation, so the fibre trace is \(\operatorname{Tr} Q_\beta\). Summing the diagonal and inserting \(M\) multiplies by \(\kappa_d(N\beta)\). ∎

The same identity holds with the sector phase \(e(an/8)\) absorbed into \(L\), because that phase is a shift of \(t\). The argument below is written for a general real family \(\{L(t)\}\) and then specialised to sector \(0\).

\(T\) preserves the span of the fibres along each \(\lambda\)-orbit. Orbit lengths divide \(P\). On an orbit of length \(L\) the trace of \(T^P\) is \(L\) times the trace of the length-\(P\) product at any representative, and \(\kappa_d\) is constant on the orbit. The identity class is an orbit of length \(1\). Its contribution is \(\kappa_d(0)\operatorname{Tr} Q_0\), with no factor \(P\).

## 2. The norm and the spectral radius [P]

Let \(s\in\mathbb R^{280}\) be the positive diagonal of `logs/h7_uniform_weights.json`, and let \(\|\,\cdot\,\|_s\) be the weighted norm of `proofs/h7_uniform.md` §1. Put
\[
\|\Phi\|_{H,s}^2=\sum_{\beta\in G}\|\Phi(\beta)\|_s^2.
\]

**Theorem 2.** In this norm,
\[
\|T\|=\max_{\beta\in G}\bigl\|L\bigl(\operatorname{Tr}(\beta)/d\bigr)\bigr\|_s\le\sup_{t\in\mathbb R}\|L(t)\|_s\le 246/100.
\]
The inequality on the right is Theorem 1 of `proofs/h7_uniform.md`. The fibre at \(\beta=0\) is invariant and acts as \(L(0)\), so
\[
\rho\bigl(L(0)\bigr)\le\rho(T)\le 246/100.
\]
The Newton enclosure in `logs/h7_uniform.json` puts the left end at least \(1.9154732041332492\).

*Proof.* Let \(D=\operatorname{diag}(s)\). Passing to \((D\otimes I)T(D^{-1}\otimes I)\) replaces each fibre map by its weighted conjugate, so it is enough to treat \(\|\,\cdot\,\|_s\) as the Hilbert norm on \(V\). Then
\[
\|T\Phi\|^2=\sum_{\beta\in G}\bigl\|L\bigl(\operatorname{Tr}(\beta)/d\bigr)\Phi(\lambda^{-1}\beta)\bigr\|^2
\le\Bigl(\max_\beta\bigl\|L\bigl(\operatorname{Tr}(\beta)/d\bigr)\bigr\|\Bigr)^2\sum_{\beta}\|\Phi(\lambda^{-1}\beta)\|^2.
\]
Multiplication by \(\lambda\) permutes \(G\). A function supported on a single fibre where the maximum is attained gives the matching lower bound. The phases \(\operatorname{Tr}(\beta)/d\) are \(d\)-torsion. The maximum over that finite set is at most the maximum over every real phase, and the latter is at most \(246/100\). ∎

The same estimate with the unweighted \(\ell^2\) norm gives \(\|T\|_2=\max_\beta\|L(\operatorname{Tr}(\beta)/d)\|_2\). A \(4096\)-node float sample of the unweighted norm on the circle, recorded by `h7_avg_orbit.py`, lies in \([8.658961044960337,\ 11.115528813823087]\) (`[N]`; the upper end matches the known \(\|L(0)\|_2\)). The weighted norm is the one that enters the bounds below. The sample is not the certificate.

**Corollary 3.** \(\lvert\operatorname{Tr}_H(MT^P)\rvert\le \dim(H)\,\|\kappa_d\|_\infty\,\|T\|^P\). Here \(\dim(H)=280\,d^2\) and \(\|\kappa_d\|_\infty=\kappa_d(0)=(457-2)(7521721-2)\). This is a bound. It is not \(\lvert\operatorname{Tr}\rvert\le\dim(H)\,\rho(T)^P\): \(MT^P\) is not asserted to be normal.

## 3. The Gauss transform [P]

For an odd prime \(q\equiv 1\pmod 8\) and a missing label \(t_b\not\equiv 0\), write \(\kappa(0)=q-2\) and \(\kappa(v)=-1-e(\bar t_b\, v/q)\) for \(v\not\equiv 0\), as in Lemma 1 of `proofs/h7_lin.md`. Equivalently \(\kappa(v)=-1-e(\bar t_b\, v/q)+q\,1_{v=0}\). Define
\[
\Gamma_q(\xi)=\sum_{\beta\in\mathcal O/q\mathcal O}\kappa\bigl(N(\beta)\bigr)\,e\bigl(\operatorname{Tr}(\beta\xi)/q\bigr).
\]

**Theorem 4.** Let \(w^2\equiv 2\pmod q\), which exists because \(q\equiv\pm 1\pmod 8\), and here \(q\equiv 1\pmod 8\). Then
\[
\Gamma_q(\xi)=
\begin{cases}
q(q-2), & N(\xi)\equiv 0,\\
-q\bigl(1+e(-t_b N(\xi)/q)\bigr), & N(\xi)\not\equiv 0.
\end{cases}
\]
In particular \(\|\Gamma_q\|_2^2=q^3(q-2)(2q-3)\), and \(\sum_\beta\lvert\kappa(N\beta)\rvert^2=q(q-2)(2q-3)\).

*Proof.* Both \(457\) and \(7521721\) are \(1\pmod 8\). Write \(\tau=\bar t_b\) and \(\psi(\xi)=e(-t_b N(\xi)/q)\), and expand \(\kappa(v)=-1-e(\tau v/q)+q\,1_{v=0}\). Then \(\Gamma_q\) is \(-S_{\mathrm{full}}-G+q\,S_{\mathrm{iso}}\), with the three sums below.

The complete sum \(S_{\mathrm{full}}=\sum_\beta e(\operatorname{Tr}(\beta\xi)/q)\) factors as a product of two geometric sums. The coefficient of \(b_x\) is \(2\xi_x\) and the coefficient of \(b_y\) is \(4\xi_y\). Both \(2\) and \(4\) are units, so \(S_{\mathrm{full}}=q^2\) at \(\xi=0\) and \(S_{\mathrm{full}}=0\) otherwise.

Since \(2\) is a square, set \(u=b_x-wb_y\) and \(v=b_x+wb_y\). Then \(N(\beta)=uv\), and \((u,v)\) runs through \(\mathbb F_q^2\) as \(\beta\) does, because \(2\) and \(w\) are units. The zero set is the union of the lines \(u=0\) and \(v=0\), which meet at the origin. On \(v=0\) one has \(b_x=u/2\), \(b_y=-u/(2w)\) and \(\operatorname{Tr}(\beta\xi)=u(\xi_x-w\xi_y)\), using \(2/w=w\). On \(u=0\) one has \(\operatorname{Tr}(\beta\xi)=v(\xi_x+w\xi_y)\). Each line contributes a geometric sum, and the origin is counted twice, so
\[
S_{\mathrm{iso}}=q\,1_{\xi_x=w\xi_y}+q\,1_{\xi_x=-w\xi_y}-1.
\]

For the quadratic sum, complete the square with \(\tau=\bar t_b\):
\begin{align*}
\tau b_x^2+2\xi_x b_x&=\tau(b_x+\xi_x\tau^{-1})^2-\xi_x^2\tau^{-1},\\
-2\tau b_y^2+4\xi_y b_y&=-2\tau(b_y-\xi_y\tau^{-1})^2+2\xi_y^2\tau^{-1}.
\end{align*}
The leftover phase is \(e((-N(\xi))/(\tau q))=e(-t_b N(\xi)/q)\). The translated sum factors as
\[
\Bigl(\sum_{z}e(\tau z^2/q)\Bigr)\Bigl(\sum_{z}e(-2\tau z^2/q)\Bigr).
\]
For an odd prime \(q\) and \(a\not\equiv 0\), \(\sum_z e(az^2/q)=(a/q)\sum_z e(z^2/q)\). The sum on the right equals \(\sqrt q\) when \(q\equiv 1\pmod 4\) and \(i\sqrt q\) when \(q\equiv 3\pmod 4\) (Ireland–Rosen, *A Classical Introduction to Modern Number Theory*, Chapter 6, the evaluation of the quadratic Gauss sum). Each factor therefore contributes a Legendre symbol times \(\sqrt q\), and the product of the symbols is
\[
\Bigl(\frac{\tau}{q}\Bigr)\Bigl(\frac{-2\tau}{q}\Bigr)=\Bigl(\frac{-2}{q}\Bigr)=\Bigl(\frac{-1}{q}\Bigr)\Bigl(\frac{2}{q}\Bigr)=1,
\]
because \(q\equiv 1\pmod 4\) and \(q\equiv 1\pmod 8\). The quadratic sum equals \(q\,\psi(\xi)\) at every \(\xi\), including \(0\).

On \(N(\xi)=0\) exactly one of the two lines contains \(\xi\) if \(\xi\not=0\), and both contain it if \(\xi=0\). Substituting the three evaluations produces \(q(q-2)\) on the isotropic set. Off that set \(S_{\mathrm{iso}}=-1\) and \(S_{\mathrm{full}}=0\), so \(\Gamma_q=-q(1+\psi)\). The same substitution is the rewrite \(\Gamma_q=-q-q\psi+q^2 1_{N=0}\) used in §5.

For the norm, Parseval for the un-normalised sum reads \(\sum_\xi\lvert\Gamma_q\rvert^2=q^2\sum_\beta\lvert\kappa(N\beta)\rvert^2\). The form \(uv\) represents \(0\) exactly \(2q-1\) times and represents every nonzero value exactly \(q-1\) times. As \(v\) runs through \(\mathbb F_q^\times\), so does \(\bar t_b\, v\), and
\[
\sum_{k=1}^{q-1}\lvert 1+e(k/q)\rvert^2=2(q-2),
\]
because \(\sum_{k=1}^{q-1}\cos(2\pi k/q)=-1\). Hence
\[
\sum_\beta\lvert\kappa\rvert^2=(q-2)^2(2q-1)+(q-1)\cdot 2(q-2)=q(q-2)(2q-3),
\]
and \(\|\Gamma_q\|_2^2=q^3(q-2)(2q-3)\). ∎

`h7_average.py check` compares the closed form with the direct sum at \(q=17\), \(t_b=3\), on every norm class. The largest gap is \(1.7955268718282194\cdot 10^{-13}\). The same run compares the scalar form of the pairing in §4, three letters and a full period of length \(8\), with the direct sum over \(\beta\). The gap is \(2.153132083222681\cdot 10^{-13}\) (`logs/h7_average.json`, both `[N]`). The identities used below are Theorem 4 and the character sum, not these comparisons.

**Corollary 5.** For \(d=q_1q_2\) with the two primes distinct and \(1\pmod 8\),
\[
\Gamma_d(\xi)=\sum_{\beta\in G}\kappa_d(N\beta)\,e\bigl(\operatorname{Tr}(\beta\xi)/d\bigr)
\]
factors by the Chinese remainder theorem: if \(u_i\equiv (d/q_i)^{-1}\pmod{q_i}\), then
\[
\Gamma_d(\xi)=\Gamma_{q_1}^{(t_1)}(u_1\xi\bmod q_1)\,\Gamma_{q_2}^{(t_2)}(u_2\xi\bmod q_2),
\]
where the local missing labels \(t_i\) are those of Lemma 1 of `proofs/h7_lin.md` after the unit \(u_i\) is absorbed, and \(\Gamma^{(t)}\) means Theorem 4 at that label. Consequently
\[
\|\Gamma_d\|_2=\|\Gamma_{q_1}\|_2\,\|\Gamma_{q_2}\|_2.
\]
The \(\ell^2\) norm does not depend on the missing label.

*Proof.* Lemma 1 writes \(\kappa_d\) as a product of local sums, with argument \(N(\beta)\cdot u_i\) and missing label \(t_c(q_i)\equiv t_b(q_i)\cdot(d/q_i)\). The exponential splits as \(e(k/d)=\prod_i e(k u_i/q_i)\). Each local sum is the sum in Theorem 4 after the change of variables that multiplies the frequency by the unit \(u_i\) and replaces the missing label by \(u_i^{-1}t_c(q_i)\). Multiplication by \(u_i\) is a bijection, so the \(\ell^2\) norms multiply. ∎

## 4. The trace as a pairing, and the majorants [P, CA]

Expanding the product of letters gives the dual form of Theorem 1. For a word \(n_0,\ldots,n_{P-1}\),
\[
\xi(n)=\sum_{j=0}^{P-1}n_j\lambda^j\in\mathcal O,
\qquad
B\bigl(\xi\bigr)=\sum_{\xi(n)=\xi}A_{n_{P-1}}\cdots A_{n_0},
\]
the product ordered so that \(A_{n_0}\) stands on the right. The phase of letter \(n_j\) at the class \(\beta\) is \(e(n_j\operatorname{Tr}(\beta\lambda^j)/d)=e(\operatorname{Tr}(\beta\cdot n_j\lambda^j)/d)\), so
\[
\operatorname{Tr}_H(MT^P)=\sum_{\xi\in G}\Gamma_d(\xi)\,\operatorname{Tr} B(\xi).
\]
The trace of a reversed word is not this trace. The matrices \(B(\xi)\) are the values of one operator, iterated \(P\) times. On functions from \(G\) to \(\operatorname{End}(V)\),
\[
(R\Phi)(\xi)=\sum_{|n|\le 16}A_n\,\Phi(\lambda\xi-n).
\]
Starting from the identity matrix at \(0\), the value \((R^P\Phi)(\xi)\) is \(B(\xi)\). The coordinate at step \(k\) is \(\lambda^{-k}\) times the partial sum \(\sum_{j<k}n_j\lambda^j\), and \(\lambda^P\equiv 1\) brings the final coordinate back to \(\xi(n)\).

**Lemma 8.** In the norm \(\bigl(\sum_\xi\|D\Phi(\xi)D^{-1}\|_{\mathrm{HS}}^2\bigr)^{1/2}\), one has \(\|R\|=\max_k\|L(k/d)\|_s\le 246/100\).

*Proof.* Let \(F\) be the unitary Fourier transform of \(\ell^2(G)\) for the pairing \(\operatorname{Tr}\), extended to \(\operatorname{End}(V)\)-valued functions. Substituting \(\tau=\lambda\xi-n\) gives
\[
\operatorname{Tr}(\xi\eta)=\operatorname{Tr}\bigl(\tau\cdot(\eta\lambda^{-1})\bigr)+n\operatorname{Tr}(\eta\lambda^{-1}),
\]
hence
\[
(FR\Phi)(\eta)=L\bigl(-\operatorname{Tr}(\eta\lambda^{-1})/d\bigr)\,(F\Phi)(\eta\lambda^{-1}).
\]
Multiplication by \(\lambda^{-1}\) permutes the fibres. The trace form is surjective and \(d\) is odd, so every \(d\)-torsion phase occurs. A fibrewise left multiplication has Hilbert–Schmidt operator norm equal to the operator norm of the fibre map. The similarity \(D\,\cdot\,D^{-1}\) is the weighted norm, and \(D\,I\,D^{-1}=I\). ∎

Cauchy–Schwarz on the pairing uses \(\lvert\operatorname{Tr} W\rvert\le\sqrt{280}\,\|DWD^{-1}\|_{\mathrm{HS}}\) and \(\|I\|_{\mathrm{HS}}=\sqrt{280}\):
\[
\bigl\lvert\sum_\xi\Gamma_d(\xi)\operatorname{Tr} B(\xi)\bigr\rvert
\le\|\Gamma_d\|_2\cdot\sqrt{280}\cdot\bigl\|R^P\Phi\bigr\|
\le\|\Gamma_d\|_2\cdot 280\cdot\bigl(246/100\bigr)^P.
\]
This is the following statement.

**Theorem 6.** \(\lvert\operatorname{Tr}_H(MT^P)\rvert\le 280\,\|\Gamma_d\|_2\,(246/100)^P\).

The pieces are enclosed in `h7_average.py majorant` at precision \(200\), reading the untwisted trace ball from `logs/h7_lin_traces.json` and the threshold arithmetic of `proofs/h7_uniform.md` §4. The log `logs/h7_average.json` records:

| quantity | value |
| --- | --- |
| \(\|\Gamma_{457}\|_2\) | \(6289834.045383471\) |
| \(\|\Gamma_{7521721}\|_2\) | \(2.1943603506088192\cdot 10^{17}\) |
| \((246/100)^{57}\) | \(1.9199994526364493\cdot 10^{22}\) |
| Cauchy–Schwarz majorant | \(7.420040412990621\cdot 10^{48}\) |
| majorant / threshold | \(1.9142415283101287\cdot 10^{21}\) |
| Koopman majorant of Corollary 3 | \(2.173974663978\cdot 10^{53}\) |
| Koopman / threshold | \(5.608476978097026\cdot 10^{25}\) |
| threshold \(T\) | \(3.8762299862656054\cdot 10^{27}\) |

The float endpoints of each ball agree to the digits printed. The radii are in the log. Both majorants exceed \(T\). The triangle majorant of `proofs/h7_uniform.md` is \(6.768238765003160\cdot 10^{44}\), a factor about \(1.10\cdot 10^{4}\) smaller than the Cauchy–Schwarz majorant and a factor about \(3.21\cdot 10^{8}\) smaller than the Koopman majorant. Moving the sum inside the trace and taking the operator norm does not improve the triangle bound.

The spectral-radius enclosure of Theorem 2 has the same consequence. The only trace inequality it supports, together with \(\|M\|=\kappa_d(0)\), is Corollary 3.

## 5. The constant piece [P, CA]

Theorem 4 rewrites the local transform as
\[
\Gamma_q=-q-q\,\psi_q+q^2 E_q,
\]
where \(\psi_q(\xi)=e(-t_b N(\xi)/q)\) and \(E_q=1_{N(\xi)=0}\). The product \(\Gamma_{q_1}\Gamma_{q_2}\) therefore has nine terms. The term \((-q_1)(-q_2)=d\) is independent of the word. Its pairing is
\[
d\sum_n\operatorname{Tr}(A_{n_{P-1}}\cdots A_{n_0})=d\,\operatorname{Tr}\bigl(L(0)^P\bigr)=d\,\operatorname{Tr} Q_0.
\]

**Theorem 7.** The constant piece of \(\operatorname{Tr}_H(MT^P)\) equals \(d\,\operatorname{Tr} Q_0\). At \(d=3437426497\) and \(P=57\), sector \(0\),
\[
d\,\lvert\operatorname{Tr} Q_0\rvert=4.226394516794827\cdot 10^{25},
\]
and \(T\) exceeds it by the factor \(91.71481675130566\). The identity-class term \(\kappa_d(0)\lvert\operatorname{Tr} Q_0\rvert\), which is the term removed to reach the Lin sum, equals \(4.207897141838002\cdot 10^{25}\), and \(T\) exceeds it by the factor \(92.11798329681781\).

The enclosures are the `term1_abs`, `T_over_term1`, `zero_mode_abs`, and `T_over_zero_mode` fields of `logs/h7_average.json`. The trace ball is the period-\(57\), sector-\(0\), \(\beta=0\) row of `logs/h7_lin_traces.json`.

The other eight pieces are not estimated by a majorant under \(T\). Each is a pairing against a function of \(\ell^2\) norm at least as large as a positive power of one of the two primes, times a coefficient \(q_1q_2\), \(q_1q_2^2\), or \(q_1^2q_2^2\). Feeding any of those readout norms through Theorem 6 reproduces a bound of the same shape as §4, above \(T\). No cancellation between the eight pieces is proved.

## 6. The local traces do not multiply [P, N]

The factorisation of \(\Gamma_d\) does not factor the trace. A scalar model makes the obstruction explicit and was evaluated exactly enough to see it.

Take letters \(n\in\{-1,0,1\}\) with coefficients \(0.3+0.1i\), \(1\), and \(-0.2+0.05i\), at the primes \(17\) and \(41\), with missing labels \(3\) and \(5\). The orders of \(\lambda\) are \(8\) and \(5\), and the composite order at \(697\) is \(40\). `h7_average.py all` sums \(\kappa\operatorname{Tr}\) by the product formula of Lemma 1. The log records
\[
\frac{S(697)}{S(17)\,S(41)}\approx -1.586633130289316-5.839859862523013\,i,
\]
of modulus \(6.05155913001261\). A product formula would force the ratio to be \(1\). The computation is binary64 (`[N]`, field `factor_check` of `logs/h7_average.json`). It is a counterexample to the equality \(S(d)=S(q_1)S(q_2)\), not an enclosure of either side.

The same obstruction applies to the section. The phase \(\operatorname{Tr}(\beta)/d\) is the sum of the two local phases, and \(L(t_1+t_2)\) is not a tensor of \(L(t_1)\) and \(L(t_2)\). An orbit that is trivial at \(q_1\) and nontrivial at \(q_2\) is not the product of a local trace at \(q_1\) with a local weight at \(q_2\).

In particular, an inequality \(\lvert S_d\rvert\le\lvert S_{457}\rvert\sum\lvert\kappa_{7521721}\rvert\) is not a consequence of the splitting. The inner sum at a frozen residue modulo \(7521721\) is a different family of phases from the sum at the prime \(457\).

## 7. A float scan at the prime 457 [N]

The norm bounds do not see cancellation between orbits. At the prime \(q=457\), sector \(0\), every \(\lambda\)-orbit was multiplied in binary64 by `h7_avg_orbit.py`. The run took \(722.51\) s and covered \(457^2\) classes: \(3664\) orbits of length \(57\) and the identity orbit of length \(1\) (`logs/h7_avg_orbit_q457_a0.json`). `h7_average.py orbit` folds that table. The derived values are in `logs/h7_average.json`, field `orbit457`.

The identity contribution has modulus \(5.594329091312814\cdot 10^{18}\). The sum of the other \(3664\) contributions has modulus \(64.36874328884288\), and the sum of their moduli is \(373.22983980635564\). The largest twisted trace has modulus \(0.34968689979938067\). The sixteen nonzero isotropic orbits reproduce the certified isotropic sum \(7.8450076177326356\) with gap \(2.842170943040401\cdot 10^{-14}\). The identity trace reproduces the certified untwisted modulus with relative gap \(7.157247874848233\cdot 10^{-15}\).

These comparisons are floating-point observations. The script also stored a Frobenius majorant built from an unweighted Lipschitz grid. Its largest entry is \(6.087378898382624\cdot 10^{47}\). That column does not enclose the traces. The largest twisted Frobenius norm along a product is \(1041.2577603166462\), which is consistent with traces of size at most \(1\) and is not a certificate.

Sector \(4\) was not scanned. Its untwisted trace and its certified isotropic sum are the negligible quantities already in `logs/h7_lin_traces.json` and `logs/h7_lin_iso_sum.json`.

The same cancellation is not a theorem at \(d=457\cdot 7521721\). Section 6 blocks the product of a local trace with a local weight. What the threshold does say, as a comparison of two enclosures, is the room in a uniform trace cap. `orbit457.trace_room` is
\[
\frac{T}{\sum_{\beta\not\equiv 0}\lvert\kappa_d(N\beta)\rvert}=30788816.98609009.
\]
If every nonzero section trace at this \(d\) satisfied \(\lvert\operatorname{Tr} Q_\beta\rvert\le 30788816.98609009\), the triangle bound would be at most the threshold. Equality in every term would put the triangle on the threshold. The certified uniform cap \(280\cdot(246/100)^{57}\) is larger than this room by the factor \(1.7460880259903623\cdot 10^{17}\) already computed in `proofs/h7_uniform.md`. The float maximum \(0.35\) at the prime \(457\) sits under the room. No argument in this note promotes that maximum to a uniform cap at the composite.

## 8. Decision

On the finite section, \(S\) is the trace of \(MT^P\) with the identity class removed. The weighted norm of \(T\) is at most \(246/100\), and the spectral radius of \(T\) lies between the untwisted spectral radius and that norm. The Cauchy–Schwarz majorant of Theorem 6 exceeds the \(\eta=1\) threshold by \(1.9142415283101287\cdot 10^{21}\). The Koopman majorant exceeds it by \(5.608476978097026\cdot 10^{25}\). Both are coarser than the triangle bound of `proofs/h7_uniform.md`. The constant Gauss piece \(d\operatorname{Tr} Q_0\), and the identity-class term, each lie under the threshold by a factor near \(92\). The complementary sum is where any further cancellation would have to occur, and no bound in this note puts that complementary sum under the threshold. At the prime \(457\), a binary64 scan puts the twisted sector-\(0\) remainder near \(64\), against an identity term near \(5.6\cdot 10^{18}\). That scan is not an enclosure, and §6 blocks its transfer to the composite. A uniform trace cap of \(30788816.98609009\) would put the residue triangle under the threshold. The proved cap is larger by \(1.7460880259903623\cdot 10^{17}\).

Aggregate H7* is not shown to hold and not shown to fail. The operator is an operator on the finite section, not on \(\hat Z\). H1, H3, H8, and frozen R′ are not touched.
