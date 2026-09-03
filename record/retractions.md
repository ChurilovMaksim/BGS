# Retractions and permanent quarantines

These statements or proof routes are false, superseded, or too weak for the
conclusion historically attached to them. The current branch records the
failure mechanism without carrying a duplicate executable museum; exact old
bytes remain in Git history, with
`d0e414ec26ff7e43ad59e80f77c9d8c679e87c4b` as the last pre-cleanup curated
archive snapshot.

1. **Historical Möbius-fiber / M4D proof of M1.** Unsaturated elimination
   inserted a phantom `(1,1)` key and mishandled the multiplicity-`p-2`
   diagonal. The resulting cross-term object is not the corrected pair-key
   object.
2. **Run 93.2 one-sided mixed count.** It included diagonal→off but omitted the
   distinct ordered off→diagonal class, producing a factor error.
3. **Historical uniform Möbius-fiber square-root bound.** The `d=0` fiber is
   degenerate/constant; `formalization/Bgs/HistoricalMobiusDegenerateFiber.lean`
   keeps a finite regression guard.
4. **“Moment/Catalan data + an ESY citation implies BGS.”** False. A structured
   deterministic arithmetic family is not automatically a Wigner ensemble.
5. **R86/R87 noncommutative trace shortcut.** Invalid as stated.
6. **Historical `N=95419` spacing verdict.** It compared different statistics.
7. **IID-KS interpretation of pooled unfolded spacing samples.** Withdrawn:
   within-spectrum and pooled gaps are dependent.
8. **Historical “number variance” label and two-sigma pass criterion.** The
   algorithm uses forward windows anchored at eigenvalues with edge truncation,
   not stationary `Sigma^2(L)`.
9. **Old word-trace “certificate” and all-orders arcsine/Catalan promotion.**
   A higher-word rewrite case remained unresolved; finitely many moments do not
   prove the universal law.
10. **Unrestricted historical twisted-Jacobi closed form.** The omitted domain
    condition `n1 != 0` matters; finite nonzero-q regressions remain usable
    where that condition is automatic.
11. **Hecke-centering Julia series.** Failed line; later red-team work exposed
    basis-selection and centering/noise artifacts.
12. **`cdense_transfer.jl` Perron bracket.** Falsified by the zero digit's
    zero-cost self-loop of weight one.
13. **`sol6_closed_form.jl` closed-form claim.** Falsified by exact finite rows;
    the count depends on the prime in cases where the filename suggested
    otherwise.
14. **Projective-order comment at `p=31`.** The historical Julia comment said
    `5` while the implemented condition was `A^k=I`; the exact full matrix
    order is `15`.
15. **General `Sp(2g)` conclusion from diagonal/coset flatness.** Not
    established.
16. **A complete explicit cyclotomic exceptional-set theorem for arbitrary
    growing prime `K`.** Complete resultant enumerations are current only for
    `K=11,13`; `(p,K)=(461,23)` is an explicit non-uniformity warning.
17. **Finite GOE resemblance as proof of a limiting BGS law.** Numerical
    evidence does not supply the microscopic comparison/local-law bridge.

## Editorial/implementation corrections

During the 2026-09-03 audit, an intermediate note had the inverse pair-key
formula with the wrong sign. From `u=x/y` and `v=(x-1)/(y-1)`, the correct
inverse is

```text
y=(1-v)/(u-v),   x=u(1-v)/(u-v),
```

while `d=(u-1)(v-1)/(v-u)` was already correct. Active code used the correct
formula, so finite certificates were not invalidated.

The historical Cayley finite verifier also had a one-way exception regression:
a prime expected to be exceptional could pass without requiring observed
excess collisions. The maintained Python and C++ gates now test actual
generic/exceptional behavior in both directions.

Finally, the maintained `jacobi_matrix` contract now accepts validated
annihilator **sub-sectors** (including the parity sectors used by spectral
diagnostics) while rejecting characters outside the annihilator. The previous
equality-to-full-annihilator contract was too strict and made the active API
inconsistent with legitimate sector computations.
