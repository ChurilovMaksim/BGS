# Open mathematical obligations

Only unresolved obligations belong here. Closed routes, corrected theorems and finite controls are indexed in `results.md` and `results_20260907_addendum.md`; false or superseded statements belong in `../record/retractions.md`.

## A. Improve pointwise Cayley energy to the centered quadratic scale

The off/off elliptic correlation layer is no longer an independent open problem: after extraction of the coherent reducible fibre, `offoff_elliptic_spike_theorem.md` proves

```text
Var O << p E_+(A)+K^2p+K^4 sqrt(p)+K^4.
```

The mixed/off-off bottleneck is therefore the same Cayley additive energy.

Three complementary pointwise bounds are now closed:

1. the older Vyugin--Makarychev route gives `E_+(A)<34K^(8/3)` in its explicit range;
2. `cayley_curve_uniform.md`, using Corvaja--Zannier, gives globally for every subgroup order `K>=2`

```text
E_+(A) << K^(8/3)+K^4/p;
```

3. `cayley_fourier_hybrid.md`, using the classical mixed Weil bound after the exact annihilator-character expansion, gives the centered estimate

```text
0 <= E_+(A)-(K-1)^4/p <= 4(K-1)(p-K+1),
```

and therefore

```text
E_+(A)-(K-1)^4/p
 << min(pK, K^(8/3)+K^4/p).
```

The Fourier branch is strictly stronger than the previous worst-curve scale when `K>p^(3/5)`; for `K=p^(alpha+o(1))`, `alpha>3/5`, it has centered exponent `1+1/alpha<8/3` in `K`. It approaches the quadratic scale as `alpha->1`, but it does not improve the sparse arithmetic regime.

The sharp pointwise target remains

```text
E_+(A)=(K-1)^4/p+O(K^(2+o(1))),
```

or equivalently

```text
sum_(q!=0)|1_Ahat(q)|^4 << p K^(2+o(1)).
```

The remaining material intermediate target is now specifically the sparse/intermediate range: obtain any explicit centered `K^(2+delta)` bound with `delta<2/3` where the complete mixed-Weil `pK` branch is not already stronger. The exact split-prime support machinery, scalar resultants, Frobenius amplification and dyadic averaged theorems remain available inputs. None currently gives that sparse pointwise cancellation.

## B. Prove Heisenberg-scale desymmetrized joint-trace estimates

For the correct `N x N` spectral block, the deterministic bridge is exact:

```text
C_(2,N)(U;phi)
 = N^(-2) sum_m phihat(m/N)(|Tr U^m|^2-N),
```

and the higher factorial correlations are partition-Mobius sums of joint traces. Compact Fourier support probes powers `|m|=Theta(N)`.

**Closure condition:** prove the weighted joint-trace comparison with the appropriate GOE/COE/GUE target on the Heisenberg scale for a clearly specified natural deterministic family, with all symmetry reduction and unfolding conventions fixed before the estimate.

Classical Green--Kubo positivity, global moment laws, recurrence-time normal forms and finite cyclic-module identities do not substitute for this estimate.

## C. Scope of Fourier-support control

The former separate tail obligation is **closed as a deterministic implication**
for positive normalized averages of finite-circle spectral measures. By
`bandlimited_correlation_extension.md`, comparison on every compact Fourier
support with a reference Schwartz limit extends to every Schwartz correlation
test. The proof supplies uniform translated-cube bounds from one nonnegative
band-limited majorant. It does not bound the absolute Fourier trace tail.

**Remaining scope requirement:** the trace comparison in B must hold for every
compact Fourier support, not merely a common fixed cap. The clock/period-two
counterexample proves that the latter is insufficient. Signed averages,
Hamiltonian window boundaries, and conversion from correlation functions to a
full point-process or spacing law require separately stated hypotheses.

## D. Positive microscopic BGS universality for a natural fixed map

The project contains several strong negative and structural lessons:

- arithmetic cat maps retain exceptional symmetries;
- some kicked families remain smoothly or all-orders conjugate to the arithmetic model;
- bounded clustering in the Pell critical regime is incompatible with GOE/COE under global unfolding;
- weak Egorov information alone allows spectral rounding counterexamples.

**Closure condition:** identify a natural fixed chaotic map/quantization family not protected by the known conjugacies, determine the correct desymmetrized ensemble, and prove B on every compact Fourier support with the hypotheses in C. Only then can a positive BGS/GOE/COE/GUE microscopic theorem be asserted.

## E. All-members analytic resonance nondegeneracy

The generic infinite-support part is now closed substantially beyond analytic strips. `resonance_wiener_stability.md` gives an explicit weighted-Wiener stability ball around every nonconstant real trigonometric polynomial. `generic_wiener_resonance.md` proves that `{Gamma_A>0}` is open and dense in the natural weighted-Wiener Banach space, every fixed analytic Wiener strip, every `H^s(T^2)` with `s>2`, and `C^infinity(T^2)` with its Frechet topology. Exact zero-variance cancellations are therefore closed and nowhere dense in all of those spaces.

Two further analytic mechanisms are also closed:

1. `analytic_bracket_rigidity.md` proves

```text
{g,C_A g}=0 identically and g real analytic  =>  g constant.
```

So the separated-support pointwise-zero mechanism cannot occur for a nonconstant analytic observable.

2. `analytic_coboundary_regularization.md` proves that an analytic zero-orbit-sum observable has an analytic cohomological transfer, with an explicit positive strip-width loss. Hence any hypothetical nonconstant analytic `g` with `Gamma_A(g)=0` must satisfy

```text
{g,C_A g}/(4*pi)=u-C_A u,
{g,C_A g} != 0,
u real analytic.                                                (*)
```

The remaining question is therefore sharply reduced:

**Open question:** can the nonlinear analytic cohomological equation (*) have a nonconstant real-analytic solution `g`, or can one prove it impossible? Equivalently, is `Gamma_A(g)>0` for every nonconstant real-analytic observable?

The known compactly supported Gevrey counterexample is not analytic; the project's nontrivial entire temporal all-pass gauges of one harmonic are proved to lie in no finite Gevrey class. Neither resolves (*).

This question may inform perturbation theory but is not itself the missing BGS theorem.

## F. Full vanishing-noise tomography transition

For every fixed strictly noisy phase-insensitive Gaussian product channel, moment-class input tomography has logarithmic minimax risk, and the explicit pure-loss binary pair has a uniform varying-loss transition with penalty `eta^{-n}`.

**Open question:** determine the matching minimax transition for the full moment class when the physical channel noise vanishes with the copy budget. The binary-pair theorem supplies a lower-bound mechanism but is not a complete minimax characterization.

## G. Formalization depth

The active Lean tree contains finite certificates and algebraic lemmas, not formalizations of the full analytic asymptotic theorems. Native certificates have the trust boundary described in `../formalization/README.md`. All 16 active modules compiled on 8 September 2026.

**Open engineering/mathematical task:** formalize load-bearing algebraic pieces when doing so reduces proof risk, especially exact finite-support/cohomological identities and finite Cayley bookkeeping. Do not label source presence as compilation or analytic formalization.

## Engineering boundary

Julia migration is complete and is not an open mathematical task. The current computational roles are Python/SymPy for transparent exact/CAS orchestration, C++20 for independent exact/exhaustive kernels, Lean for kernel-checked finite residues, and TeX for the publication-facing proof record. GitHub-hosted workflow attempts that terminate with `steps=[]` provide no execution evidence. The pinned Lean 4.33.1 build now succeeds locally; the earlier environment
block is resolved. This changes execution status, not the scope of the
formalized mathematics. Full analytic formalization remains open.
