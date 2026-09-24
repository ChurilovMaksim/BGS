# Open mathematical obligations

Only unresolved obligations belong here. Stable IDs are assigned in
`../record/claims.json`; current status authority remains
`../record/claim_ledger.md`. Closed routes and finite controls are indexed in
`results.md`; false or superseded statements belong in
`../record/retractions.md`.

## Frontier board

| Claim ID | Priority / role | Closure condition |
|---|---|---|
| `BGS-TRACE-005` | **central fixed-map bottleneck** | Prove the correctly desymmetrized weighted Heisenberg-scale joint-trace comparison, or an equivalent mixed-resolvent hierarchy, on every compact Fourier support. |
| `BGS-BGS-001` | **terminal microscopic target** | Combine `BGS-TRACE-005` with the exact trace bridge, every-bandwidth extension, fixed unfolding, and correct symmetry-class hypotheses to prove the positive microscopic law for the maintained frozen map. |
| `BGS-CAYLEY-005` | arithmetic fourth-moment frontier | Prove centered Cayley energy `(K-1)^4/p + O(K^(2+o(1)))`, or a genuinely equivalent support/divisor theorem in the intended pointwise regime. |
| `BGS-RES-003` | analytic resonance frontier | Resolve the nonlinear analytic coboundary equation for arbitrary nonconstant real-analytic observables. |
| `BGS-INFO-001` | information-theory application frontier | Determine matching minimax upper/lower transitions for the full moment class when physical Gaussian-channel noise vanishes with copy budget. |
| `BGS-FORMAL-001` | verification-depth task | Rebuild the current 17-module Lean source graph and deepen formalization only where it materially reduces proof risk. |

The principal BGS route is therefore not “prove everything above first”.
`BGS-TRACE-005` is the direct model-specific obligation. The Cayley,
resonance, and information-theory frontiers are valuable independent
programmes and possible sources of techniques, but they are not silently
treated as prerequisites for `BGS-BGS-001`.

The 23 September exact kick-rank result `BGS-FM-005` does not estimate joint
traces at Heisenberg times. The all-lag classical gap `BGS-RES-005` uses
linear transport of one physical symbol. The subsequent
[`BGS-FM-006`](nonlinear_bracket_pressure.md) proves that **the same**
linear normalization has no uniform nonlinear full-lag upper bound for the
actual kicked map. This classical pressure obstruction does not supply the
`BGS-TRACE-005` quantum joint-trace estimate. The separate arbitrary-analytic
resonance question remains `BGS-RES-003`.

After the 24 September seven-cut reduction (`BGS-FM-007`), the same
compact-frequency signed joint-trace obligation may be proved for either
the original $U_N$ or the **full** approximant
$V_N=e^{i\tau N A_N^{\rm cut}}M_N$. Their full fixed-order local-law
statements are equivalent, and their pair/Abel tests differ by
$O(\tau/\log N)$. The seven path projectors of $A_N^{\rm cut}$ do not
commute with $V_N$; assume no independent spectra. Algebraic
simple-spectrum (`BGS-FM-008`, only $7\nmid N$) and common antiunitary
obstruction (`BGS-FM-009`, except $N=7$) exclude exact degeneracy
mechanisms within their scopes but give no quantitative mixed-trace
cancellation. A concrete necessary pair milestone is
$N^{-1}\operatorname{Tr}\Gamma_{N,N}^2\to4/3$, where
$\Gamma_{N,N}=[N^{-1}\operatorname{Tr}U_N^{b-a}]_{0\le a,b<N}$;
this has not been proved for the model.

The later exact [arithmetic trace theorem](frozen_arithmetic_trace_rigidity.md)
(`BGS-FM-010`) proves *nonvanishing* of every positive-power trace,
including at \(7\mid N\), but gives no **upper** estimate in the Abel
sum. The [effective gap floor](frozen_effective_gap_floor.md)
(`BGS-FM-011`) for \(7\nmid N\) is vastly smaller than the mean gap;
it gives no local occupation control. Neither result changes the
closure condition of `BGS-TRACE-005`.

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

The [clustered Abel calculation](clustered_abel_window_boundary.md) gives a
quantitative corollary in the existing compensated pinning range, and a
simple-spectrum counterexample to inferring a positive-time Heisenberg-window
form-factor bound from cluster containment, spacing collapse, or Abel
divergence alone. The example does not model the prescribed frozen map; it
clarifies why its mixed-resolvent estimate must still be proved separately.

The 21 September continuation narrows the loop-equation route without closing
it.  Exact moment inequalities strengthen the first two mixed levels, and a
second orientation ((w,w,v)) yields a strictly stronger conditional
differential barrier.  Conversely, repeated-clock spectra show that
arbitrarily many one-upper tests ((w,v,\ldots,v)) at one selected height can
all vanish while the pair statistic remains non-CUE.  Hence any successful
route must control the relevant orientations and varying off-real arguments,
not merely one residual row.


The short-return necessary condition is now explicit in
`return_trace_obstruction.md`: an ergodic intensity-one local limit requires
all normalized sublinear-time traces to vanish, and mesoscopic empirical
densities to become uniform in spatial L1. For the current positive-variance
Gevrey return regime this requires $K\epsilon_K^2\to\infty$.
The converse fails for clock spectra, and density-dependent unfolding changes
the critical obstruction. No positive trace comparison is supplied by this
necessary condition.

The intensity-loss extension now gives the sharp abstract bound
$\alpha\le\operatorname*{ess\,inf}\rho$ for an ergodic local limit and
return density $\rho$. At the free Brownian endpoint with $0<t<4$, such a
limit must be empty. Identifying the actual nonergodic local limit, or its
conditional law after unfolding by $\rho$, remains open for the kicked map.
The inverse-density construction produces the same complete return law
with different unfolded local laws among abstract spectra. Thus return-law
identification alone cannot close this conditional-law obligation.


The September 10 harmonic return theorem now does concern powers of the
actual kicked propagator: `pell_harmonic_returns.md` proves its global
return law, including a free unitary Brownian endpoint. Its multiplicity
$m$ is fixed and its times $mK$ are logarithmic in dimension.
Extending the diagram phase estimates and summability uniformly to
$m\asymp D/K$, and obtaining the required joint-trace comparison, are
unresolved. A marginal free probability law supplies neither estimate.

The September 9 all-order budget now proves a Gaussian distribution theorem
for the full Cayley--Jacobi trace in logarithmic pointwise and subpolynomial
dyadic density regimes; see `cayley_trace_gaussian_limit.md`.
This concerns `Tr M_S(mq)` as an additive parameter varies. The following
obligation concerns `Tr U^m` for a single correctly desymmetrized propagator.
No identity transferring the new theorem to that obligation has been proved.

For the arithmetic trace itself, extending the CLT to fixed polynomial
subgroup size is also open. At order `r`, the current averaged error contains
`Q^(r/2+1)/X`; no fixed positive exponent `Q=X^theta` makes it small for every
order. A stronger all-order estimate or a different distributional argument
is needed to cross this boundary.

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

For the prescribed frozen model, the ordinary midpoint symbol is now derived
exactly from the raw Weyl convention.  Its classical map is analytic Anosov,
has only power (C^1) commuters, has no (C^1) reversor, and is not
(C^1)-conjugate to the relevant affine model in the proved small-coupling
range containing the actual (\tau/(2\pi)).  Thus smooth inherited classical
symmetry is no longer a plausible missing explanation.  This does not rule
out (N)-dependent quantum arithmetic structure.

The full-symbol odd-Pell crossover also proves that bounded
(|\epsilon_K|\sqrt K) is incompatible with the CUE pair transform.  The
actual frozen strength eventually escapes that obstruction, so the theorem
locates rather than closes the hard regime.


The harmonic-transition theorem realizes circle-graphon global laws,
including a free semicircular endpoint, in the same fixed Pell cat map.
It varies and samples the observable frequency up to $\sqrt N$. It does not
change the unperturbed propagator's arithmetic spectrum.
The harmonic return theorem subsequently perturbs the propagator and
identifies its global recurrence law, but the quantum kick vanishes,
harmonics are sampled, and microscopic universality remains unproved.

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

2. `analytic_coboundary_regularization.md` proves that an analytic zero-orbit-sum observable has an analytic cohomological transfer, with no loss of the exponent in its adapted frequency norm (and a positive strip width in ordinary coordinates). Hence any hypothetical nonconstant analytic `g` with `Gamma_A(g)=0` must satisfy

```text
{g,C_A g}/(4*pi)=u-C_A u,
{g,C_A g} != 0,
u real analytic.                                                (*)
```

A complete infinite-dimensional subfamily is now closed: for every
Fourier-line observable (g(x)=G(v\cdot x)) in the stated (H^{1+\beta})
coercive range, the 21 September theorem gives a sharp positive orbit-sum
bound and excludes an (L^2) coboundary.  In particular (H^{3/2}) positivity
holds for every such line when (|\operatorname{tr}A|\ge6).  An exact local
polynomial example simultaneously shows that fixed-point Taylor jets alone
cannot settle the global periodic equation.

The remaining question is therefore sharply reduced:

**Open question:** can the nonlinear analytic cohomological equation (*) have a nonconstant real-analytic solution `g`, or can one prove it impossible? Equivalently, is `Gamma_A(g)>0` for every nonconstant real-analytic observable?

**22 September partial closure.** The project proof in
`finite_orbit_resonance_rigidity.md` excludes zero variance, and proves all
finite-lag independence, for every nonconstant real smooth observable whose
support is contained in finitely many signed A-orbits. Equivalently, it
covers support with bounded `abs(det(k,Ak))`. Any remaining analytic
counterexample must have infinitely many such orbits and unbounded invariant
values. The large-gap separation threshold is not uniform in the family;
no passage to arbitrary analytic support is justified by truncation alone.

The known compactly supported Gevrey counterexample is not analytic; the project's nontrivial entire temporal all-pass gauges of one harmonic are proved to lie in no finite Gevrey class. Neither resolves (*).

This question may inform perturbation theory but is not itself the missing BGS theorem.

## F. Full vanishing-noise tomography transition

For every fixed strictly noisy phase-insensitive Gaussian product channel, moment-class input tomography has logarithmic minimax risk, and the explicit pure-loss binary pair has a uniform varying-loss transition with penalty `eta^{-n}`.

**Open question:** determine the matching minimax transition for the full moment class when the physical channel noise vanishes with the copy budget. The binary-pair theorem supplies a lower-bound mechanism but is not a complete minimax characterization.

## G. Formalization depth

The active Lean tree contains finite certificates and algebraic lemmas, not formalizations of the full analytic asymptotic theorems. Native certificates have the trust boundary described in `../formalization/README.md`. The historical 16-module build passed on 8 September 2026; the subsequently added `CueLoopKernels` module has source-level status pending a fresh full build.

**Open engineering/mathematical task:** formalize load-bearing algebraic pieces when doing so reduces proof risk, especially exact finite-support/cohomological identities and finite Cayley bookkeeping. Do not label source presence as compilation or analytic formalization.

## Engineering boundary

Julia migration is complete and is not an open mathematical task. The current computational roles are Python/SymPy for transparent exact/CAS orchestration, C++20 for independent exact/exhaustive kernels, Lean for kernel-checked finite residues, and TeX for the publication-facing proof record. GitHub-hosted workflow attempts that terminate with `steps=[]` provide no execution evidence. The pinned Lean 4.33.1 build succeeded for the earlier 16-module revision; a full build including the newer module remains to be recorded. This changes execution status, not the scope of the
formalized mathematics. Full analytic formalization remains open.
