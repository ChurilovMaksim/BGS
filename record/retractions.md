# Retractions and permanent quarantines

These statements or proof routes are false, superseded, or too weak for the conclusion historically attached to them. Their source material is retained only when it remains useful as provenance, a counterexample, or a regression target.

1. **Historical Möbius-fiber / M4D proof of M1.** Unsaturated elimination inserted a phantom `(1,1)` key and mishandled the multiplicity-`p-2` diagonal. The resulting cross-term object is not the corrected pair-key object.
2. **Run 93.2 one-sided mixed count.** The producer included diagonal→off but omitted the distinct ordered off→diagonal class, giving a factor error in the fourth-moment coupling total.
3. **Historical uniform Möbius-fiber square-root bound.** The `d=0` fiber is degenerate/constant; the active Lean falsifier records this finite failure mechanism.
4. **“Moment/Catalan data + an ESY citation implies BGS.”** False. A structured deterministic arithmetic family is not automatically a Wigner ensemble, and no verified microscopic comparison/resolvent mechanism is supplied by such a citation.
5. **R86/R87 noncommutative trace shortcut.** Invalid as stated.
6. **Historical `N=95419` spacing verdict.** It compared different statistics (gap ratio versus ordinary spacing CDF).
7. **IID-KS interpretation of the promoted spacing samples.** Withdrawn. Polynomial unfolding, within-spectrum gaps, and pooling produce dependent observations, so the textbook IID KS critical value does not justify a pass/fail claim here. The CDF distances remain descriptive data.
8. **The historical “number variance” label and two-sigma pass criterion.** The code uses forward windows anchored at eigenvalues with edge truncation, not the stationary number variance `Sigma^2(L)`. The matched cat-map/GOE values remain a descriptive same-algorithm diagnostic only.
9. **Old word-trace “certificate” and all-orders arcsine/Catalan promotion.** A higher-word rewrite case remained unresolved; finitely many matching moments do not prove the universal law.
10. **Unrestricted historical twisted-Jacobi closed form.** The omitted domain condition `n1 != 0` matters. The finite nonzero-q regressions remain usable where that condition is automatic.
11. **Hecke-centering Julia series.** Failed line; later red-team work exposed basis-selection and centering/noise artifacts.
12. **`cdense_transfer.jl` Perron bracket.** Falsified: the zero digit creates a zero-cost self-loop of weight one.
13. **`sol6_closed_form.jl` closed-form claim.** Falsified by preserved exact finite rows; the count depends on the prime in cases where the filename suggested otherwise.
14. **Projective-order comment at `p=31`.** The historical Julia comment said 5 while the implemented condition was `A^k=I`; the exact full matrix order is 15.
15. **General `Sp(2g)` conclusion from diagonal/coset flatness.** Not established.
16. **A complete explicit cyclotomic exceptional-set theorem for arbitrary growing prime `K`.** Not established by the currently promoted computation. Complete resultant enumerations are current only for `K=11` and `K=13`; `(p,K)=(461,23)` is an explicit non-uniformity warning.
17. **Finite GOE resemblance as proof of a limiting BGS law.** Numerical evidence never supplies the missing microscopic local-law bridge.

## Editorial corrections that did not change computed certificates

During the 2026-09-03 full audit, the written inverse pair-key formula was found with a sign error in an intermediate note. From `u=x/y` and `v=(x-1)/(y-1)`, the correct inversion is

`y=(1-v)/(u-v)`, `x=u(1-v)/(u-v)`,

while `d=(u-1)(v-1)/(v-u)` was already correct. Active code and Lean used the correct `u-v` inversion, so existing finite certificates were not invalidated; the mathematical text and manuscript were corrected.

The historical Cayley finite verifier also had a one-way regression condition: a prime expected to be exceptional could pass without requiring observed excess collision energy. The active verifier now requires agreement in both directions on the audited designs.

Retraction means “do not infer from this line”, not “erase the failure mechanism”. Exact historical bytes live under `record/corpus/`, `record/checkpoints/`, or Git history as appropriate.
