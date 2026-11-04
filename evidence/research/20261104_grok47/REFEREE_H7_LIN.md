# Self-referee of the aggregate Lin note

The note is `proofs/h7_lin.md`. The scoping sentence is `proofs/h7_scope.md`. The failure mode throughout is to turn a piece into the sum.

## 1. A one-orbit enclosure is not an enclosure of Lin_d

The closure condition bounds \(\bigl|\sum_{\beta\not\equiv 0}\kappa_d(N\beta)\hat Z(\beta)\bigr|\). Lemma 1 gives \(\kappa\) for the three crossing frequencies, and Section 4 encloses the section trace of those three orbits. Cyclicity multiplies by the orbit length and by nothing else. The rest of \((\mathbb Z/d\mathbb Z)^2\) is not in the certificate.

At \(d=3437426497\), \(d^2=11815900922277691009\) and \(d^2\equiv 1\pmod{57}\), so \((d^2-1)/57=207296507408380544\). That is how many length-\(57\) orbits there would be if every nonzero class had orbit length \(57\). It is not a count of equal contributions. The isotropic orbits at the prime \(457\) were summed completely, in both surviving sectors, and \(|S_{\mathrm{iso}}|\) is about \(8\) and about \(40\). That sum is the isotropic part of the section at one prime factor. It is not the off-isotropic part, and it is not \(\mathrm{Lin}_d\).

## 2. The prime 457 does not stand in for the composite

Section 2 is the J3-F5 splitting, which is BGS-TRACE-228, plus the observation that the section phase depends on \(\beta\) only through \(\operatorname{Tr}(\beta\lambda^j)/d\). The coefficient of \(\Lambda_{457}\) inside \(\mathrm{Lin}_{3437426497}\) is \((7521721-2)/7521721^2<1.33\cdot 10^{-7}\). The exact-conductor term has coefficient \(1\). An isotropic sum at \(q=457\), even a complete one, is a piece of \(\Lambda_{457}\) and then a \(10^{-7}\) piece of the composite. Calling it \(\mathrm{Lin}_d\) reverses the splitting.

## 3. Float propagators are not certificates

`logs/h7_lin_validate.json` compares two float implementations of a truncation with \(K=20\), letters \(|n|\le 10\), at \(q=41\), \(m=15\). The absolute error \(1.33\cdot 10^{-10}\) checks that the Gauss kernel and the \(\beta\)-sum agree with each other. It does not enclose either one, and it is not the section of `proofs/h7_multidisc.md`.

`logs/h7_lin_kappa_check.json` is the same kind of check for Lemma 1 at \(d=287\): a float member sum against a ball product. The lemma is the proof. The check is not a substitute at \(d=3437426497\), where the member set was not enumerated. The proof does not enumerate it.

A Hutchinson average was not run. N7b's Monte Carlo of \(|\hat Z/Z|\) at \(p=19\) is not cited. That sample did not see the rate-\(1.46\) orbit certified in the previous note, so it is not evidence that the sum is small.

## 4. The Frobenius majorant does not decide, and neither does alignment

\(\|L\|_F\le 50.490459330663754\) is an upper bound on one step. Raised to the period it exceeds the threshold \(|S|\ge z_{\mathrm{lo}} d^2/(2h_p)\) by many orders. An upper bound that large neither shows \(\eta\le\kappa_0\) nor shows \(\eta>\kappa_0\).

A matching lower bound would need the terms to share a phase. Nothing in the certificate forces that. Triangle inequality the other way, \(|S|\ge |S_{\mathrm{orbit}}|-|S_{\mathrm{rest}}|\), needs an upper bound on the rest that is smaller than the orbit. The Frobenius bound is not smaller. One orbit therefore does not prove \(\eta>0\) for the sum, and does not prove \(\eta\) small.

## 5. Section trace, true \(\hat Z\), edge

The enclosed trace is the vertex section. Line J writes \(\hat Z=c_m\sum_a c_a\tfrac13(\operatorname{Tr} V-\operatorname{Tr} E)\) with \(|c_a|=1/2\) and \(c_m=1-\lambda^{-m}\). The edge trace was not enclosed. The passage from the section to the untruncated vertex is the gap in `proofs/h7_multidisc.md` §5 and is not closed here.

The section ratio uses the section's own \(\beta=0\) trace in the denominator. That cancels a common sector coefficient inside one sector. It does not cancel a sum of two sectors, and it is not \(\eta\) for the true \(Z_\rho\). The comparison against \(z_{\mathrm{lo}}\) is marked mixed for that reason. Using \(z_{\mathrm{lo}}\) as if it were the section trace, or the section trace as if it were \(z_{\mathrm{lo}}\), is the mistake the note is written to avoid.

Sector \(4\) at \(\beta=0\), period \(57\), has section trace about \(10^{-14}\). Dividing a sector-\(4\) orbit by that trace is not a meaningful \(\eta\). The note uses the sector-\(0\) untwisted trace as the section scale, including for the isotropic sector-\(4\) sum, whose modulus is about \(40\) and whose share against that denominator is \(<3\cdot 10^{-13}\).

## 6. What the scoping sentence is allowed to say

`proofs/h7_scope.md` says three things, and each has a different source.

- The sufficient reading fails on the finite section because three certified lower endpoints lie above \(1.42785\). The source is `logs/h7_multidisc_enclose.json`. The gap to \(1.42785\) is at least \(0.03\), so a \(10^{-12}\) float conversion does not close it.
- The aggregate is open because the sum was not enclosed. A small one-orbit \(\eta\) is compatible with that sentence. It does not upgrade it to "the aggregate holds".
- Theorem v5 is unaffected because \(19<1409\) and \(29<1409\). The draft's other threshold \(3307\) is larger. Neither prime is replaced. H7* stays a hypothesis of v5 at \(p\ge p_{\mathrm{thr}}\).

No row of `record/claims.json` was edited. H7*, H8, H1, H3 and frozen R′ stay open.
