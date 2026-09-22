# Mathematical continuation review, 6 September 2026

This is a proof-scope record, not an execution certificate. A source file or a
successful Git write does not prove that its verifier, Lean module or manuscript
has been executed. Historical execution logs retain their original scope.

## Corrections

1. A squarefree gcd does not make its roots simple in each input polynomial.
   The fixed-input shift theorem now includes gcd(f/G,G)=1. The exact negative
   control f=X^2, g=X(X-1), Res(f,g+t)=t^2 prevents the former overstatement.
2. Inverse translated-resultant transversality now uses the derivative-free
   initial form and a Sylvester kernel-to-cokernel argument. It covers an input
   multiple root and retains the ambient degree on degree-drop strata. The
   canonical row-frontier section includes the zero-input case as well.
3. All-pass filtering preserves ordinary two-point correlations and the
   zero-frequency cohomological bracket hierarchy. It does not generally
   preserve nonzero-frequency bracket cross spectra. The exact first/second
   bracket control at frequency pi gives -12*pi^2 versus +12*pi^2.
4. A rational all-pass resolvent is not automatically an automorphism of
   C-infinity. The smooth gauge group used here instead has Laurent
   coefficients summable with every exponential weight.
5. Covariance spectra, quantum observable spectra, control Lie algebras and
   the eigenphases of a fixed kicked propagator are kept distinct throughout.

## Current project derivations

The following are mathematical proofs with stated hypotheses, not claims of
independent referee acceptance, world priority or complete Lean formalization.

- weighted_wiener_resonance.md: every fixed Fourier pair visits an oriented
  hyperbolic orbit at most twice; this proves a uniform bounded synthesis
  operator on l2 for M1 observables. One harmonic makes all finite zero-
  frequency hierarchies nondegenerate outside a countable parameter set.
- resonance_riesz_regularization.md: the full two-variable covariance symbol
  is pi^2 X(theta)Y(omega-theta), modulo an operator-norm-continuous compact
  remainder. Its positive minimum is exactly the criterion for an eventual
  Riesz family in both lag and simultaneous-translation indices. One sine
  quadrature repairs every even background, with an explicit epsilon^4 bound.
- two_window_resonance_crossover.md: for the explicit fixed-support filtered
  family, the finite rectangular Gram lower edge is comparable to
  (n^(-2q)+epsilon^2)(min(n,m)^(-2q)+epsilon^2), uniformly in both window
  lengths and perturbation strength. The proof retains all boundary terms.
- two_radius_quadrature_rigidity.md: one signed-orbit finite filter has a
  constant zero-frequency tail symbol exactly for one tap or two taps in
  phase quadrature. The two-tap high-lag Gram matrix is exactly diagonal.
- multiradius_polynomial_rigidity.md: a rank-r vector polynomial is either
  radially norm-flat everywhere or flat on at most r-1 positive circles.
  The bound is independent of degree and sharp at prescribed radii.
- multisphere_polynomial_rigidity.md: r concentric spheres force a rank-r
  polynomial map to be an orthogonal sum of homogeneous Veronese blocks.
- polynomial_shell_identifiability.md: a nonzero rank-r Hermitian polynomial
  form vanishes on at most r-1 concentric circles or spheres. Two d-output
  polynomial maps with identical intensities on 2d complete concentric
  spheres are related by a fixed unitary. For a one-dimensional domain,
  2d-1 prescribed circles do not suffice; explicit sharp examples are given.
- balanced_phase_controllability.md: a pi/4-balanced Weyl mode and a transverse
  Weyl mode generate su(N) for every odd N with unit determinant modulo N,
  including composite N. A finite Lie-word determinant gives simultaneous
  controllability outside a countable parameter set. The Pell specialization
  applies to every odd N. Variable-control reachability is not fixed-map
  spectral universality and has no dimension-uniform synthesis-time bound here.
- infinite_orbit_resonance.md: every nonzero M1 observable on one signed
  hyperbolic Fourier orbit has independent finite resonance classes even
  when the spatial Fourier support is infinite.
- entire_temporal_gauge.md: all real entire temporal all-pass filters are
  classified as sign times monomial times exp(sum a_k(z^k-z^(-k))). They
  preserve the complete zero-frequency hierarchy modulo actual smooth
  coboundaries, while cubic moments can change. A nontrivial such gauge of
  one harmonic is smooth but belongs to no finite Gevrey class.
- quadratic_response_limits.md: exact finite filters have identical complete
  quadratic-response data and a coercive classical tail, but different
  third quantum observable moments. Exact cyclic quantum returns separately
  obstruct an unchanged transfer of an infinite classical Riesz bound.

## Verification and publication boundaries

The Python verifiers use exact integer, rational or cyclotomic arithmetic when
so labelled. The balanced-Weyl verifier tests a sufficient edge-gap criterion;
it does not compute a numerical Lie rank. The polynomial rigidity verifier
checks sharp constructions and finite coefficient alphabets; it is not an
arbitrary-degree proof by enumeration. Floating-point quantum tests retain
their numerical label.

The maintained manuscript remains manuscript/BGS_unified.tex. The continuation
inputs are connected through final_delivery_note.tex; no second publication
root is intended. A fresh successful fail-closed build and visual inspection
must be recorded separately before any new PDF is described as validated.
Likewise no new Lean compilation or cloud-CI success is certified by this note.

## Unresolved central task

No positive microscopic BGS/GOE/GUE/COE/CUE universality theorem is obtained.
The new observable and control results do not supply appropriately
 desymmetrized joint propagator traces or local resolvents at Heisenberg time.
The Cayley pointwise exponent and the growing-parameter split-prime support
bounds are not improved by these results. Any eventual universality proof must
supply those missing spectral estimates rather than relabel a classical Gram
bound, a control theorem, or an observable moment identity as that proof.
