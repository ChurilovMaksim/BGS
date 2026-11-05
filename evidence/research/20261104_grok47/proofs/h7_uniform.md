# A uniform bound on the finite-section trace

Tags in this file are local to the note. **[P]** is proved here, or is an external theorem with the locator named in the sentence. **[CA]** is a finite enclosure in ball arithmetic. **[N]** is a floating-point observation. A finite enclosure is not an asymptotic bound, and it is not an enclosure of \(\sum_\beta\kappa\hat Z\). `record/claims.json` was not edited.

The question is whether one norm, valid for every twist, gives \(|\operatorname{Tr} Q(\beta)|\le C R^P\) on the finite multi-disc section with \(R\) well below the Frobenius majorant \(M\approx 50.49\), and whether that bound times the residue weight puts
\[
\eta=\frac{|\mathrm{Lin}_d|\,h_p}{|Z|^2}
\]
under \(1\) at \(d=3437426497\). The norm bound is proved for the section, with \(R=246/100\). The product with the residue weight is larger than the \(\eta=1\) threshold by a factor \(1.746\cdot 10^{17}\). The rate that would meet the threshold is \(R_*=1.225865206681737\), a factor \(2.006745918386011\) below the certified \(R\). That \(R_*\) also lies below the untwisted spectral radius, so no induced-norm bound of this shape meets the threshold.

The section and the three crossings are those of `proofs/h7_multidisc.md` and `proofs/h7_lin.md`. This note does not replace either.

## 1. The norm [P]

The section is centres \(|c|\le 3\), modes of degree \(<40\), letters \(|n|\le 16\), dimension \(280\), disc radius \(6/5\). It is forward-invariant on this alphabet (`h7_multidisc_cert.py` reports no exit). A step is the matrix
\[
L(t)=\sum_{|n|\le 16} e(nt)\,A_n,
\]
with the letter \(A_n\) carrying \(\hat g(n)\,e(Cn^2/2)\), the composition, and the factor \(e(Cnc)\), as in `proofs/h7_multidisc.md` §1. The sector phase \(e(an/8)\) is the same formula with \(t\) shifted by \(a/8\). A bound for every real \(t\) is a bound for every sector.

Let \(s\in\mathbb R^{280}\) be the positive vector stored as binary64 hex in `logs/h7_uniform_weights.json`, normalised to have maximum entry \(1\). Write \(D=\mathrm{diag}(s)\) and
\[
\|x\|_s=\|Dx\|_2,\qquad \|B\|_s=\|DBD^{-1}\|_2.
\]
This is an induced operator norm, so it is submultiplicative, and a similarity does not change the trace or the spectrum. For any phases \(t_0,\ldots,t_{P-1}\),
\[
\bigl|\operatorname{Tr}(L(t_{P-1})\cdots L(t_0))\bigr|
\le 280\,\|L(t_{P-1})\cdots L(t_0)\|_s
\le 280\prod_{j<P}\|L(t_j)\|_s.
\]
The same \(D\) is used at every step. The phases of a \(\lambda\)-orbit are one sequence of this form. So is every other sequence. The bound is uniform over twists, and it upper-bounds the joint spectral radius of the family \(\{L(t)\}\).

## 2. The certificate [CA]

**Theorem 1.** For every real \(t\), \(\|L(t)\|_s\le 246/100\).

The proof is a finite check with an explicit remainder. Let \(M_n\) be the binary64 midpoint of the weighted letter \(DA_nD^{-1}\), and let \(\rho_n\) be an arb upper bound on the Frobenius norm of the entrywise radius, including one unit in the last place for the midpoint conversion. Let \(\|M_n\|_F\) be enclosed by summing the squared dyadic entries in ball arithmetic. Then, for every \(t\),
\[
\|L''(t)\|_s\le\Lambda_2,\qquad
\Lambda_2=\sum_n(2\pi n)^2\bigl(\|M_n\|_F+\rho_n\bigr),
\]
because \(\|L''(t)\|_s\le\sum_n(2\pi n)^2\|DA_nD^{-1}\|_2\) and \(\|\,\cdot\,\|_2\le\|\,\cdot\,\|_F\). The enclosure is \(\Lambda_2<2585.523025\).

Cover the circle by \(N=233\) intervals of length \(1/233\), with centres \(\theta_k=(2k+1)/466\) and half-width \(\delta=1/466\). On the \(k\)-th interval, Taylor's formula with the integral remainder gives, for \(|\tau|\le\delta\),
\[
L(\theta_k+\tau)=L(\theta_k)+\tau L'(\theta_k)+R_2(\tau),
\qquad \|R_2(\tau)\|_s\le\Lambda_2\,\tau^2/2\le\Lambda_2\delta^2/2.
\]
The remainder is \(<5.953148\cdot 10^{-3}\). The map \(\tau\mapsto\|B+\tau C\|_2\) is convex, so on \([-\delta,\delta]\) its maximum is attained at an endpoint. Therefore
\[
\max_{|t-\theta_k|\le\delta}\|L(t)\|_s
\le\max_{\sigma=\pm 1}\|L(\theta_k)+\sigma\delta L'(\theta_k)\|_s+\Lambda_2\delta^2/2.
\]
Each endpoint is the linear combination \(\sum_n c_n A_n\) with
\[
c_n=e(n\theta_k)\,(1+\sigma\delta\cdot 2\pi i n).
\]
The coefficient is enclosed in ball arithmetic. The combination of the midpoint matrices is evaluated sequentially in binary64. The error of that evaluation is at most
\[
\alpha\sum_n|c_n|\,\|M_n\|_F,
\qquad
\alpha=\sqrt{2}\Bigl(6u+\gamma_k(1+6u)\Bigr),
\quad
u=2^{-52},\quad
\gamma_k=\frac{ku}{1-ku},
\]
with \(k=33\) letters. A complex product of two binary64 numbers has absolute error at most \(6u\) times the product of the moduli. Each of the real and imaginary parts is two rounded products and one rounded addition, so the factor \((1+u)^2-1\le 3u\) multiplies \(|ac|+|bd|\) and \(|ad|+|bc|\). Each of those sums is at most \(\sqrt{2}\) times the product of the moduli, and the Euclidean norm of the two components is then at most \(6u\). Recursive summation of \(k\) real numbers has error at most \(\gamma_k\) times the sum of absolute values (Higham, *Accuracy and Stability of Numerical Algorithms*, Theorem 3.1, using \(\gamma_k\ge\gamma_{k-1}\)). Applied to each component of the already-rounded products, this contributes the factor \(6u+\gamma_k(1+6u)\). The modulus of a two-component error is at most \(\sqrt{2}\) times that factor, which is \(\alpha\). The value in the log is \(\alpha<1.225\cdot 10^{-14}\). A fused multiply-add only reduces the product error. Adding the radius terms \(\sum |c_n|\rho_n\) and the midpoint defect of \(c_n\) gives the full distance from the binary64 matrix to the true endpoint. The script subtracts that distance, endpoint by endpoint, before the Cholesky cap. The constant \(\alpha\) is below \(1.225\cdot 10^{-14}\), so the distance is negligible beside the Taylor remainder.

A binary64 number \(r\) at most the lower end of \(246/100\) minus the Taylor remainder minus this distance is then a cap for the binary64 matrix. The cap is certified by a Cholesky witness. Let \(G\) be the lower-triangular factor, in binary64, of a floating-point Hermitian part of \(r^2 I-M^*M\). Ball arithmetic encloses \(E=r^2 I-M^*M-GG^*\) and \(F=I-GB\), where \(B\) is a binary64 inverse of \(G\). Frobenius norms upper-bound the operator norms. If \(\|F\|_F<1\) and
\[
\sigma=\frac{1-\|F\|_F}{\|B\|_F}
\]
satisfies \(\sigma^2>\|E\|_F\), then every matrix in the residual ball is positive definite, so \(\|M\|_2\le r\). All \(466\) endpoints pass. The smallest slack \(\sigma^2-\|E\|_F\) has lower endpoint \(0.016316926498566642\). The run did not need a larger numerator than \(246\).

Thus \(\|L(t)\|_s\le 246/100\) for every real \(t\), and for every twist sequence of length \(P\)
\[
|\operatorname{Tr} Q|\le 280\cdot\Bigl(\frac{246}{100}\Bigr)^P.
\]
At \(P=57\) the power is enclosed as \(1.9199994526364492\cdot 10^{22}\), and the trace cap is \(5.3759984673812578\cdot 10^{24}\).

The same run encloses one eigenvalue of the untwisted step \(L(0)\) by the Newton–Kantorovich routine of `h7_rates.py`. The per-step modulus lies in \([1.9154732041332492,\ 1.915473204133273]\), with Kantorovich \(h<2.3\cdot 10^{-14}\) (the log's `newton_untwisted_step`). The spectral radius is at least the lower endpoint, so the certified norm is at most the factor \(1.284277950060465\) above that floor. The binary64 spectral radius \(1.9154732041332594\) and \(|\operatorname{Tr} Q(0)|^{1/57}\) both fall inside the same interval (`logs/h7_uniform_weights.json` and the trace in `logs/h7_lin_traces.json`). That agreement is **[N]**. The Newton lower endpoint is the certified floor.

A geometric weight \((1/2)^k(0.45)^{|c|}\), on a \(361\)-point grid, has floating-point \(2\)-norm about \(2.6485\) **[N]**. The certified diagonal is the optimised vector, not that geometric formula. The optimisation itself is not a proof of minimality.

## 3. The residue weight [P]

Let \(d=457\cdot 7521721=3437426497\). Both primes are \(1\bmod 8\), so \(\bigl(\frac{2}{q}\bigr)=1\). Lemma 1 of `proofs/h7_lin.md` writes \(\kappa_d\) as a product of local missing-label sums. For \(v\not\equiv 0\),
\[
\bigl|-1-e(\bar t v/q)\bigr|=2\bigl|\cos(\pi m/q)\bigr|,
\]
where \(m=\bar t v\bmod q\) runs through \(1,\ldots,q-1\) as \(v\) does, for any missing label \(t\not\equiv 0\). The value at \(0\) is \(q-2\).

**Lemma 2.** For an odd positive integer \(q\),
\[
\sum_{k=1}^{q-1}\bigl|\cos(\pi k/q)\bigr|=\csc\bigl(\pi/(2q)\bigr)-1.
\]

*Proof.* The terms \(k\) and \(q-k\) agree, and \(q\) odd contributes no axis term, so the sum is twice \(\sum_{k=1}^{m}\cos(k\theta)\) with \(m=(q-1)/2\) and \(\theta=\pi/q\). The Dirichlet kernel gives
\[
\sum_{k=1}^{m}\cos(k\theta)=\frac{\sin(m\theta/2)\cos((m+1)\theta/2)}{\sin(\theta/2)}.
\]
The arguments are \(\pi/4-\delta\) and \(\pi/4+\delta\) with \(\delta=\pi/(4q)\), and \(\sin(\theta/2)=\sin(2\delta)\). The numerator is \((\cos\delta-\sin\delta)^2/2=(1-\sin 2\delta)/2\), so the sum is \((1-\sin(\pi/(2q)))/(2\sin(\pi/(2q)))\). Doubling produces the cosecant. ∎

**Lemma 3.** Over \(\mathbb F_q\) with \(q\equiv\pm 1\pmod 8\), the form \(N=x^2-2y^2\) has \(r(0)=2q-1\) representations and \(r(v)=q-1\) representations for \(v\not\equiv 0\).

*Proof.* Then \(2\) is a square, say \(w^2=2\). The substitution \((u,v)=(x-wy,x+wy)\) is invertible, because its determinant is \(2w\neq 0\), and \(N=uv\). The equation \(uv=0\) has \(2q-1\) solutions. For \(a\neq 0\) the coordinate \(u\) has \(q-1\) nonzero choices. ∎

**Corollary 4.** The sum of \(|\kappa_q(N(\beta))|\) over \(\beta\in\mathbb F_q^2\) equals
\[
S(q)=(2q-1)(q-2)+(q-1)\cdot 2\bigl(\csc(\pi/(2q))-1\bigr).
\]
For \(d=q_1 q_2\) with the two primes above, \(\sum_{\beta\bmod d}|\kappa_d(N\beta)|=\prod_q S(q)\), and the \(\beta=0\) term is \((q_1-2)(q_2-2)\).

*Proof.* The local factor \(|\kappa_q|\) depends on \(N(\beta)\bmod q\) only through a unit multiple, by Lemma 1 of `proofs/h7_lin.md`, and a unit permutes the nonzero residues. The Chinese remainder theorem factors the sum over \((\mathbb Z/d\mathbb Z)^2\) into the product of the local sums. ∎

The identity was checked by a direct ball sum of the cosines at \(q=5,17,41\), with gaps below \(10^{-35}\), and by a binary64 enumeration of all \(287^2\) classes at \(d=7\cdot 41\), \(m=15\), against \(S(7)S(41)\). The relative discrepancy is \(<6.71\cdot 10^{-14}\), and \(|\kappa(0)|=195\) matches \((7-2)(41-2)\) exactly (`logs/h7_uniform.json`, field `mass_check`). The enumeration is **[N]** on the cosine side of each term and an integer count on the classes. The closed form used below is the ball evaluation of Corollary 4, not the enumeration.

## 4. The comparison at \(d=3437426497\) [CA]

Ball arithmetic at precision \(160\) encloses
\[
\sum_{\beta\not\equiv 0}|\kappa_d(N\beta)|
=\bigl[125897334347624530853.46097435543174093016356183\pm 5.18\cdot 10^{-27}\bigr].
\]
The float endpoints agree at \(1.2589733434762453\cdot 10^{20}\). This is about \(10.655\,d^2\), not a small multiple of the number of orbits. The value \(|\kappa|\le 4\) is true only off the zero set of \(N\); on that set \(|\kappa_d(0)|=455\cdot 7521719\). Dropping those classes would understate the triangle bound.

The threshold at which a sum \(S\) forces \(\eta\ge 1\), granted \(|Z|\ge z_{\mathrm{lo}}\) and \(|\mathrm{Lin}|\le(2/d^2)|Z|\,|S|\), is the quantity \(T=z_{\mathrm{lo}}\,d^2/(2h_p)\) of `proofs/h7_lin.md` §5. Recomputing it from \(z_{\mathrm{lo}}=\tfrac12(1-\lambda^{-57})(1.9154712^{57}-3012.4)\), \(h_{19}=9369319\) and \(d^2=11815900922277691009\) gives the same lower endpoint \(3.8762299862656054\cdot 10^{27}\). The constant \(3012.4\) and the shape of \(z_{\mathrm{lo}}\) are BGS-TRACE-273, cited.

Theorem 1 with \(P=57\) and Corollary 4 give, for one sector,
\[
|S_a|
=\Bigl|\sum_{\beta\not\equiv 0}\kappa_d(N\beta)\,\operatorname{Tr} Q_{\beta,a}\Bigr|
\le 280\cdot\Bigl(\frac{246}{100}\Bigr)^{57}\sum_{\beta\not\equiv 0}|\kappa_d(N\beta)|.
\]
The right-hand side is enclosed as \(6.768238765003160\cdot 10^{44}\). Dividing by \(T\) produces the quotient
\[
\frac{2 h_p}{d^2 z_{\mathrm{lo}}}\,|S_a|
\le 1.7460880259903623\cdot 10^{17},
\]
whose flint ball in the log has radius below \(10^{-28}\). The mixed reading, with a section trace in the numerator and \(z_{\mathrm{lo}}\) in the denominator, is the same reading as §5 of `proofs/h7_lin.md`. It is not a value of \(\varepsilon_d\): the section trace has not been shown to upper-bound \(|\hat Z|\), because the edge and the one-step tail are not in this norm. Inserting the trace-formula factor \(|c_a|/3=1/6\) in front of one sector, or a factor \(1/3\) in front of both surviving sectors, divides the quotient by \(6\) or by \(3\). Either quotient remains above \(10^{16}\).

**The rate that meets the threshold.** Define \(R_*\) by
\[
280\cdot\Bigl(\sum_{\beta\not\equiv 0}|\kappa_d(N\beta)|\Bigr)\cdot R_*^{57}=T.
\]
The enclosed value is
\[
R_*=\bigl[1.2258652066817371968463919747074615019384198610\pm 1.34\cdot 10^{-47}\bigr].
\]
The certified rate stands above it by the factor
\[
\frac{246/100}{R_*}
=\bigl[2.0067459183860110822140279578076293103366308852\pm 3.40\cdot 10^{-47}\bigr].
\]
The quotient of the majorant by \(T\) is that factor to the \(57\)th power. So \(R\) would need to shrink by a factor \(2.006745918386011\), from \(2.46\) down to \(1.225865206681737\), before this triangle bound could sit at \(\eta=1\).

The same equation with the constant \(280\) omitted, i.e. a cap \(|\operatorname{Tr}|\le R^{57}\) rather than \(280\,R^{57}\), has its root at \(1.353241524776895\). The Newton lower endpoint \(1.9154732041332492\) is already larger than both roots, by the factors \(1.562547981370802\) and \(1.415470312625123\). The certified norm is at most the factor \(1.284277950060465\) above that floor, and the \(57\)th power of this factor is \(1.561580909329039\cdot 10^{6}\): that is how far the weighted-norm trace cap sits above the trace cap built from the Newton floor. Replacing \(246/100\) by the Newton floor, and keeping the factor \(280\), would still leave a quotient \(1.118154055\cdot 10^{11}\).

A sharper obstruction does not use the dimension factor at all. The untwisted section trace in sector \(0\), period \(57\), has modulus \(1.2295228772115986\cdot 10^{16}\) (`logs/h7_lin_traces.json`, relative accuracy \(265\) bits). Any uniform cap is at least this large. Multiplied by the residue weight and divided by \(T\), the quotient is
\[
\bigl[399340733.9317642499692052451800409812081170272\pm 3.8\cdot 10^{-38}\bigr],
\]
about \(3.993\cdot 10^{8}\). No uniform upper bound on \(|\operatorname{Tr} Q(\beta)|\), of any shape, can sit under the threshold after multiplication by \(\sum|\kappa|\), because the untwisted orbit is one of the \(\beta\) the bound has to cover. The weighted norm improves the Frobenius majorant \(50.490459330663754\) by the factor \((M/R)^{57}>10^{74}\) on the trace cap, and the improved cap is still far above the threshold.

## 5. What this does not decide

The bound is a bound on the finite section. It is not a bound on the untruncated vertex, not a bound on the edge, and not a transfer of the one-step tail \(<9.65\cdot 10^{-5}\). The joint spectral radius of the twist family is at most \(246/100\) and at least the Newton floor \(1.9154732041332492\). A norm built from longer blocks could move the upper bound down toward that floor. It cannot move it below the floor, and the floor is already above \(R_*\).

Aggregate H7* is not shown to hold at \(d=3437426497\), and it is not shown to fail. The same \(R\) at period \(87\) makes the majorant larger, so the other two conductors are not closer to the threshold by this argument. Theorem v5 does not apply H7* at \(p=19\). The sufficient per-orbit reading remains false for the finite section, by `proofs/h7_scope.md`.

## 6. Tags

- **[P]** Submultiplicativity of the weighted norm, the trace bound with constant \(280\), the Taylor remainder and the convexity of the pencil, the binary64 evaluation constant \(\alpha\), Lemmas 2 and 3, and Corollary 4.
- **[CA]** Theorem 1 at \(R=246/100\), the Newton interval \([1.9154732041332492,\ 1.915473204133273]\) for one eigenvalue of \(L(0)\), the residue weight \(1.2589733434762453\cdot 10^{20}\), the majorant \(6.768238765003160\cdot 10^{44}\), the quotient \(1.7460880259903623\cdot 10^{17}\), and \(R_*=1.225865206681737\). The untwisted-trace obstruction \(3.9934073393176425\cdot 10^{8}\) uses the trace enclosure of `logs/h7_lin_traces.json`.
- **[N]** The \(361\)-point geometric norm \(2.6485\). The agreement, to binary64, of \(|\operatorname{Tr} Q(0)|^{1/57}\) with the floating-point spectral radius of \(L(0)\). The \(d=287\) enumeration against \(S(7)S(41)\).
- **Not claimed.** \(\eta\le 1\). A value of \(\varepsilon_d\). A bound on \(\hat Z\) or on the edge. A discharge or a refutation of H7*, H8, H1, H3, or frozen R′.
