# Self-referee: the uniform section-trace bound

The note is `proofs/h7_uniform.md`. The certificate is `code/h7_uniform.py`, log `logs/h7_uniform.json`, diagonal `logs/h7_uniform_weights.json`. Nothing here edits `record/claims.json`.

## What would make the argument false

- Treating the floating-point singular value, or the floating-point optimisation of the diagonal, as the certificate. The certificate is the Cholesky residual in ball arithmetic, on the dyadics named in the weight file. A different diagonal is a different claim.
- Claiming \(R<\rho(L(0))\). The Newton lower endpoint in the log, and the weaker floor \((|\operatorname{Tr} Q(0)|/280)^{1/57}\) from the existing trace enclosure, both sit under \(246/100\). An induced norm cannot go below the spectral radius.
- Claiming \(\eta\le 1\) because \(246/100\) is smaller than the Frobenius majorant \(50.49\). Section 4 computes the quotient. It is about \(1.75\cdot 10^{17}\).
- Using \(\sum|\kappa|\le 4d^2\). That cap is false on the zero set of \(N\), where \(|\kappa_d(0)|=(457-2)(7521721-2)\). The triangle bound uses the product of the local masses, which is about \(10.655\,d^2\).
- Reading the majorant as a lower bound on \(|S|\). It is an upper bound. The untwisted trace times the residue weight is a lower bound on every *uniform* upper bound, and that quantity already exceeds the threshold. It is not a lower bound on \(|\sum\kappa\operatorname{Tr}|\), whose terms can cancel.
- Transferring the section norm to the untruncated \(\hat Z\), or to the edge. The one-step tail of `proofs/h7_multidisc.md` is not a monodromy bound. The mixed comparison with \(z_{\mathrm{lo}}\) is labelled as mixed, as it is in `proofs/h7_lin.md` §5.
- Forgetting the dimension factor or the Taylor remainder. The constant is \(280\), and the remainder \(\Lambda_2\delta^2/2<5.96\cdot 10^{-3}\) is subtracted before the Cholesky cap.
- A failed Cholesky that was ignored. The script raises if more than six increments of the numerator still fail. The log's `attempts` list is the record of the numerator that passed, and of any that did not.

## What the check does not cover

The binary64 evaluation constant cites Higham's recursive-summation bound and a direct estimate of a complex product. It assumes IEEE-754 binary64, round to nearest, componentwise on complex values, which is the arithmetic of the run (NumPy 1.26). It does not assume the absence of fused multiply-add: a fused operation only makes the product error smaller than the bound used.

The weight vector is a float optimisation. The proof shows that this particular vector gives \(R=246/100\). It does not show that no norm gives a smaller \(R\). A smaller induced norm would still be at least the spectral radius of \(L(0)\), and that radius is already above \(R_*\).

The \(d=287\) enumeration checks the mass formula in binary64. The value used at \(d=3437426497\) is the ball evaluation of the closed form, not that enumeration.

## Decision the note is allowed to state

On the finite section, \(|\operatorname{Tr} Q|\le 280\cdot(246/100)^P\) for every twist sequence. At \(d=3437426497\) and \(P=57\), the triangle majorant against \(\sum|\kappa|\) exceeds the \(\eta=1\) threshold of `proofs/h7_lin.md` §5 by the factor computed in the log. The rate that would meet the threshold is the enclosed \(R_*\). Aggregate H7* is not decided. H1, H3, H8, and frozen R′ are not touched.
