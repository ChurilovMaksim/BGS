# Self-referee: the averaged section operator

The note is `proofs/h7_average.md`. The arithmetic is `code/h7_average.py`, log `logs/h7_average.json`. The norm cap is the certificate of `proofs/h7_uniform.md`, not a new one. Nothing here edits `record/claims.json`.

## What would make the argument false

- Reading the state space as the section tensored with \(\mathbb Z/d\mathbb Z\). The class \(\beta\) is an element of \(\mathcal O/d\mathcal O\), of cardinality \(d^2\). A one-coordinate model does not carry \(N(\beta)=b_x^2-2b_y^2\).
- Claiming \(\|T\|<\sup_t\|L(t)\|_s\). Theorem 2 identifies the norm with the maximum of \(\|L\|\) over the \(d\)-torsion phases. That maximum is at most \(246/100\). It is not shown to be smaller, and it cannot be smaller than \(\rho(L(0))\).
- Bounding the trace by \(\dim(H)\,\rho(T)^P\). Corollary 3 uses the operator norm. \(MT^P\) is not asserted to be normal, so the spectral radius does not by itself bound the trace.
- Replacing the word sum by the trace of the reversed word. \(\operatorname{Tr}(A_{n_0}\cdots A_{n_{P-1}})\) is not \(\operatorname{Tr}(A_{n_{P-1}}\cdots A_{n_0})\). The accumulator in §4 is \((R\Phi)(\xi)=\sum_n A_n\Phi(\lambda\xi-n)\), whose \(P\)-th iterate carries \(A_{n_{P-1}}\cdots A_{n_0}\) at \(\xi=\sum_j n_j\lambda^j\). The scalar check in the log is this order.
- Claiming \(S(d)=S(q_1)S(q_2)\) because \(\Gamma_d\) factors. Section 6 records a scalar ratio that is not \(1\). The phase at the composite is the sum of the local phases, and \(L(t_1+t_2)\) is not a tensor product.
- Using \(\lvert S_d\rvert\le\lvert S_{457}\rvert\sum\lvert\kappa_{7521721}\rvert\). The inner sum at a frozen residue modulo \(7521721\) is a different twist from the sum at the prime \(457\).
- Reading either majorant as a lower bound, or as an improvement of the triangle bound. The Cauchy–Schwarz majorant is about \(10^{4}\) times the triangle majorant of `proofs/h7_uniform.md`. The Koopman majorant is larger still. Both exceed the threshold.
- Treating the constant piece \(d\operatorname{Tr} Q_0\) as the whole trace. Theorem 7 isolates that piece. The other eight pieces of the product \(\Gamma_{q_1}\Gamma_{q_2}\) are not bounded under the threshold.
- Transferring the section operator to \(\hat Z\), or to the edge. The comparison with \(z_{\mathrm{lo}}\) is the mixed comparison already labelled in `proofs/h7_lin.md` §5.

## What the check does not cover

The sign of the quadratic Gauss sum is cited from Ireland–Rosen, Chapter 6. The script's direct-sum comparison at \(q=17\) is a float check of the closed form and of the scalar pairing. It is not the proof.

`h7_average.py` does not multiply the \(280\times 280\) section letters along a composite orbit. The factorisation counterexample is scalar, binary64, at \(17\cdot 41\).

The orbit decomposition in §1 reduces the trace to a sum of length-\(P\) products. It does not reduce the norm below \(\max\|L(k/d)\|_s\).

No enclosure of the complementary eight-term sum is claimed, at \(d=3437426497\) or at either prime.

The binary64 scan at \(q=457\) reproduces the certified isotropic sum to a gap of \(2.8\cdot 10^{-14}\) and the certified identity trace to a relative gap of \(7\cdot 10^{-15}\). Those two comparisons do not enclose the anisotropic orbits. The column `err_frob` reaches \(6\cdot 10^{47}\) and is not a bound. Sector \(4\) was not scanned. A small remainder at one prime is not a remainder at the composite.

## Decision the note is allowed to state

\(S\) is \(\operatorname{Tr}(MT^P)\) with the identity class removed. On the finite section, \(\|T\|\le 246/100\) and \(\rho(L(0))\le\rho(T)\le 246/100\). The Cauchy–Schwarz majorant exceeds the \(\eta=1\) threshold by the factor in `logs/h7_average.json`, and the Koopman majorant exceeds it by the larger factor in that log. The constant piece \(d\operatorname{Tr} Q_0\) and the identity-class term each lie under the threshold by a factor near \(92\). Aggregate H7* is not decided. H1, H3, H8, and frozen R′ are not touched.
