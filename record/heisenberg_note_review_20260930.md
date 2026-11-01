# Audit and completion of the submitted Heisenberg-time note

Date: 30 September 2026. **Primary verdict: incomplete, with useful exact
subsidiary results and several repairable errors.** The note does not prove
the fixed-map CUE estimate. Its own Sections 35--44 acknowledge substantial
missing implications; its final architecture is a research programme.

This is an author-level audit and proof completion, without subagents or
independent external refereeing. All 44 numbered sections, the intervening
architecture and the coefficient appendix were read. Exact finite checks
are distinguished from the analytic proofs and external theorem use below.
No claim of world-first discovery or a solved BGS conjecture is supported.

The exact submitted bytes are retained as an **inactive reference input** in
[submitted_note.md](../evidence/reference/heisenberg-note-20260930/submitted_note.md).
Its name and SHA-256 are pinned in the
[manifest](../archive/evidence/20260930/heisenberg_note_manifest.json).
The corrected maintained sources supersede it wherever they disagree.

## 1. Results retained and completed

- [FM-014](../mathematics/fixed-map/frozen_phase_finite_type.md): exact coefficient
  isolation proves the submitted order-15 transversality; removing one zero
  of the annihilator improves the plain phase to order 14. The order-15
  version remains uniform under an arbitrary linear addition. A complete
  sublevel/partition argument proves the corresponding scalar cancellation
  rates, with the exact macroscopic-distance hypothesis preserved.
- [FM-015](../mathematics/fixed-map/frozen_commutator_action.md): the classical
  commutator loop has a specified local mixed-coordinate action
  $s=t\Delta g+E$, with $\|E\|_{C^{15}}\le10^{61}t^2$ and normalized
  pure-$q$ derivatives bounded by $10^{49}t^2$. The actual Hamiltonian
  time $t=\tau/(2\pi)$ preserves both finite-type lower bounds.
  This completes the classical obligation, not the quantum FIO obligation.
- [FUP-001](../mathematics/fixed-map/offdiagonal_digit_fup.md): repair of the false
  line classification proves the ideal base-7 Fourier FUP, by the prior
  Cohen criterion. The argument extends to an exact parity classification:
  every odd base and the binary base pass; even bases at least 4 have
  exact compression norm 1 at every scale, proved by a discrete supported
  unit vector. The binary norm is exactly $\sqrt{2/N}$.
  This concerns the ideal digit model alone.
- [Supporting lemmas](../mathematics/trace-bridge/heisenberg_trace_support.md): a
  complete finite factorial CUE cycle formula; determinant and tensor
  representations; a quantitative conditional Fejér estimate; and
  near-unitary transfer at positive and negative Heisenberg times.
  Existing stronger repository pair-Abel/local bridges remain authoritative.

These completions are project deductions. The CUE determinant density,
partition--Möbius inversion, scalar oscillatory methods, generating functions
and Cohen's FUP theorem are prior mathematics. A priority search for the
specific alphabet corollary and constants was not completed.

## 2. Section-by-section disposition

| Submitted sections | Audit finding | Maintained disposition |
|---|---|---|
| 1--2: model and all-order target | Correct physical symbol and fixed coupling; the all-order weighted target is a sufficient comparison criterion, not a proved estimate. | Preserve FM-001 and TRACE-001--005. |
| 3--4: pair window and Abel equivalence | Correct route, but convergence on $(0,\infty)$ alone needs care at zero/escape to infinity. | Existing `weighted-secular/determinant_boundary.md`, Section 3, already gives a stronger moment argument on a compactified variable and the converse tail control. No duplicate claim. |
| 5: adjoint resolvent | Correct equivalent parametrization, including the zero Fourier term. | Existing RES-006. |
| 6: cubic benchmark | Correct finite positive-part formula and equal-height Laplace reference; this is Haar CUE, not the frozen map. | Existing exact CUE reference and loop controls. |
| 7--9: cycle, determinant, tensors | Passed, including resonance hyperplanes and the coefficient's absence of an extra factorial. | Supporting note Section 1, checked against the prior cumulant/Möbius and independent density calculations. |
| 10--13 and appendix: factorization, 32 modes, translation rigidity | Fourier coefficients and factorizations pass. Translation rigidity and stronger classical symmetry conclusions already exist. | FM-001 plus a full coefficient reconstruction; no duplicate symmetry theorem. |
| 14: finite type | Exact annihilator and constants pass. Separation is an actual circle distance, not merely different strip labels. | FM-014, strengthened and with scalar proof completed. |
| 15: Weyl lattice | Ordinary coefficients cannot be used unchanged in the raw modular basis. Transport direction is left unspecified in the note. | Correct $W_N(m,n)=(-1)^{nm}T_N(m,n)$ and raw $M T(a,b)M^*=T(S(a,b))$; Section 4 of supporting note, direct matrix controls. |
| 16: interaction picture | Ordered conjugated exponentials are correct; collapsing them into one exponential is not allowed. | Existing `frozen_spectral_flow_controls.md`. |
| 17: smooth Fejér suppression | Uniform $o(1)$ Egorov errors do not imply the claimed $O(1/\log N)$ rate after summation. The weighted observable statement is weaker than pair counting. | Complete estimate (2) in supporting note, conditional on summable correlations and the stated quantitative error. |
| 18: Hessian and nonlinear map | Compatible with the maintained physical-symbol Hessian; not a BGS closure. | Existing FM-001. |
| 19--20: natural transfer operator | Source trace theorem is genuine for its isolated outer-band operator with specified damping, not automatically for $U_N$. | Exact version/locator audit in `literature/heisenberg_note_sources.md`; no new model theorem from citation alone. |
| 21: all-order transfer | Valid after a norm/identification repair. Near-unitarity itself controls powers; general isomorphisms require their condition numbers. Negative times need inverse control. | Supporting note Section 3 proves both signs and the $O(N^{k-K})$ weighted bound. The all-order identification remains open. |
| 22: symbolic matching | A calculus does not solve the global recursive matching/holonomy problem. Choosing a new family for each order is weaker than one flat identification. | Open obligation, no promotion. |
| 23: seven-cut model | Full-space trace-norm perturbation and spectral transfer are already proved; cutting seven bonds is not a quantum baker identification. | Existing FM-007; no new block universality. |
| 24: 2026 anisotropic FUP | Jin--Zhang--Zhang's base hypothesis is $M_1>M_2\ge2$. It cannot be specialized directly to the isotropic $7\times7$ alphabet. Their general anisotropic continuous counterpart is explicitly unproved. | Inapplicable source-to-model arrow removed; isotropic Cohen criterion used for the ideal alphabet instead. |
| 25: isotropic line criterion | Claim that only slope-1 lines occur is false: $(1,-6)$ occurs even in the limiting base-7 set. Grid-boundary axis lines also require more than the first drawing. The FUP conclusion can nevertheless be repaired. | FUP-001 with a new geometric proof and explicit parity/binary checks. |
| 26--27: normal form and bad channels | Useful description of a missing model-to-FUP implication; finite type alone is not a line-sector compression gap. | Retain as open research obligations, not exact results. |
| 28: half shift | Critical circles and Hessian range pass. Two local Morse--Bott neighborhoods do not classify other critical points or prove a global $1/2$ rate. | FM-014 Section 5 states the local result and its boundary. |
| 29--30: orbit pairs and twisted transfer | Long-time trace formula does not prove phase cancellation. Diagonal/off-diagonal labels must account for orbit time-shift correlations; vanishing off-diagonal sum alone does not derive the plateau. | No CUE estimate promoted. |
| 31--32: partial diagonals and multi-Fejér | Möbius algebra is exact; identifying classical diagonal sectors and quantitative higher mixing is additional work. Log-time smooth sectors cannot control all microscopic eigenoperators. | Supporting algebra retained; higher-sector theorem remains programmatic. |
| 33--38: insufficiency and self-criticism | Relevant restrictions: low moments, symmetry checks, semiclassical diagrammatics and averaged graphs do not close this deterministic theorem. | Preserve the existing open frontier and add precise missing arrows below. |
| 39: classical action completion | The note asks for an explicit $C^{15}$ bound but does not construct the action. Its flow parameter needs the $2\pi$ conversion. | Completed in FM-015 in a specified local type-2 chart. |
| 40: quantum kernel | Unproved FIO representation, amplitude control, parameter uniformity and trace normalization. With conventional unnormalized HS pairing, $\langle T,T\rangle_{HS}=N$; the submitted decay scale needs specification. | Open; normalized HS coefficients would have an extra $N^{-1}$. |
| 41--42: logarithmic blocks and coding | Entrywise decay cannot simply be multiplied into an operator norm bound. No actual survivor-set coding or uniform distorted Fourier normal form is supplied. | Open compression/FUP obligation. |
| 43--44 and final architecture | First-return identities and universal cycle weights are proposed, not proved. A spectral gap does not itself generate $\min(m,N)$ or all CUE cycles. | Open renewal and all-order trace obligations. |

## 3. Corrected proof boundary

The newly closed chain is
physical symbol $\to$ uniform finite type $\to$ explicit classical mixed
action remainder $\to$ finite type of that action at the fixed coupling.
Separately, the ideal digit alphabet $\to$ no orthogonal pair
$\to$ Fourier FUP is proved using the pinned prior theorem.

The following arrows remain unproved:

1. The actual quantum commutator $\to$ a uniform torus FIO whose phases
   and amplitudes support the required normalized coefficient estimates.
2. Actual doubled seven-cut dynamics $\to$ a controlled open compression
   with appropriate survivor sets and operator norm decay. The full
   Hilbert--Schmidt adjoint is unitary and has invariant eigenoperators;
   an unrestricted spectral-gap claim would be false.
3. Such a gap $\to$ an exact renewal identity with the CUE plateau and
   the correct weighted Heisenberg-time remainder.
4. Pair information $\to$ joint traces of every order. The general
   algebraic bridge is proved; the model estimates are not.

Natural quantization is a parallel conditional route. A one-step
power-law comparison in a prior source is insufficient for its requested
all-order transfer. Neither route presently proves BGS-TRACE-005 or
BGS-BGS-001.

## 4. Reproduction and review scope

The maintained checker is
`computations/verification/heisenberg_note_audit.py --output PATH`.
Use the pinned project requirements; this workspace additionally uses the
SymPy installation and cache override recorded in the execution manifest.
The promoted [finite report](../archive/evidence/20260930/heisenberg_note_checks.json)
contains exact coefficients, annihilator arithmetic, analytic-bound
arithmetic, 3900 cycle/cumulant comparisons, 16 independent density checks,
252 rational line-membership checks, 12 exhaustive discrete support-line
cases through side length 4096, binary norms through $N=32$, three
independent quantum matrix dictionaries and nine Fejér checks.
Floating computations use complex128; no matrix exceeds dimension 32.

The analytic ODE, closed-form/primitive argument, scalar sublevel proof,
limiting-set geometry and external Cohen theorem are mathematical proof
steps, not certified by those finite checks. No Lean compilation is claimed.
The audit inspected the relevant theorem statements in pinned full primary
text for Faure--Tsujii, Cohen and Jin--Zhang--Zhang. Other broad literature suggestions in the note were not
used as load-bearing theorems and were not exhaustively priority-checked.

Source synchronization, registry checks and the full manuscript build are
recorded separately in the execution manifest. Prior dated evidence has
not been rewritten. Local and remote publication hashes are recorded in
the final delivery rather than inserted into an evidence hash cycle.
