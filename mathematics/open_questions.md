# Open mathematical obligations

Only unresolved obligations belong here. Closed routes, corrected theorems and finite controls are indexed in `results.md` and `results_20260907_addendum.md`; false or superseded statements belong in `../record/retractions.md`.

## A. Improve pointwise Cayley energy to the centered quadratic scale

The off/off elliptic correlation layer is no longer an independent open problem: after extraction of the coherent reducible fibre, `offoff_elliptic_spike_theorem.md` proves

```text
Var O << p E_+(A)+K^2p+K^4 sqrt(p)+K^4.
```

The mixed/off-off bottleneck is therefore the same Cayley additive energy.

Two uniform polynomial-scale theorems are already closed:

1. the older Vyugin--Makarychev route gives `E_+(A)<34K^(8/3)` in its explicit range;
2. `cayley_curve_uniform.md`, using Corvaja--Zannier, gives globally for every subgroup order `K>=2`

```text
E_+(A) << K^(8/3)+K^4/p.
```

The latter removes the odd-order and subgroup-size restrictions but does not improve the exponent.

The sharp pointwise target remains

```text
E_+(A)=(K-1)^4/p+O(K^(2+o(1))),
```

or equivalently

```text
sum_(q!=0)|1_Ahat(q)|^4 << p K^(2+o(1)).
```

A material intermediate advance would be any explicit pointwise `K^(2+delta)` bound with `delta<2/3` after complete propagation through the exact `B(t)` decomposition.

The exact split-prime support machinery, scalar resultants, Frobenius amplification and dyadic averaged theorems remain available inputs. None currently implies the centered pointwise bound.

## B. Prove Heisenberg-scale desymmetrized joint-trace estimates

For the correct `N x N` spectral block, the deterministic bridge is exact:

```text
C_(2,N)(U;phi)
 = N^(-2) sum_m phihat(m/N)(|Tr U^m|^2-N),
```

and the higher factorial correlations are partition-Mobius sums of joint traces. Compact Fourier support probes powers `|m|=Theta(N)`.

**Closure condition:** prove the weighted joint-trace comparison with the appropriate GOE/COE/GUE target on the Heisenberg scale for a clearly specified natural deterministic family, with all symmetry reduction and unfolding conventions fixed before the estimate.

Classical Green--Kubo positivity, global moment laws, recurrence-time normal forms and finite cyclic-module identities do not substitute for this estimate.

## C. Remove the Fourier band-limit

Even a complete Heisenberg-scale comparison for compactly supported Fourier tests yields only band-limited microscopic correlations.

**Closure condition:** prove a uniform high-frequency tail estimate strong enough to pass from compact Fourier support to the intended Schwartz/local test class without changing the symmetry block or unfolding.

This is logically separate from the trace-to-local Fourier identity, which is already exact.

## D. Positive microscopic BGS universality for a natural fixed map

The project contains several strong negative and structural lessons:

- arithmetic cat maps retain exceptional symmetries;
- some kicked families remain smoothly or all-orders conjugate to the arithmetic model;
- bounded clustering in the Pell critical regime is incompatible with GOE/COE under global unfolding;
- weak Egorov information alone allows spectral rounding counterexamples.

**Closure condition:** identify a natural fixed chaotic map/quantization family not protected by the known conjugacies, determine the correct desymmetrized ensemble, and close B and C for that family. Only then can a positive BGS/GOE/COE/GUE microscopic theorem be asserted.

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

The active Lean tree contains kernel-checked finite residues and algebraic lemmas, not formalizations of the full analytic asymptotic theorems.

**Open engineering/mathematical task:** formalize load-bearing algebraic pieces when doing so reduces proof risk, especially exact finite-support/cohomological identities and finite Cayley bookkeeping. Do not label source presence as compilation or analytic formalization.

## Engineering boundary

Julia migration is complete and is not an open mathematical task. The current computational roles are Python/SymPy for transparent exact/CAS orchestration, C++20 for independent exact/exhaustive kernels, Lean for kernel-checked finite residues, and TeX for the publication-facing proof record. GitHub-hosted workflow attempts that terminate with `steps=[]` provide no execution evidence. A fresh local Lean build remains environment-blocked here: the repository pins `leanprover/lean4:v4.33.1`, but the present container has no Lean toolchain and cannot fetch the large release archive through its restricted network.