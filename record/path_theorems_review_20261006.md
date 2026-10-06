# Fixed-map path theorems: review and scope, 6 October 2026

## Primary verdict and scope

**Proved as written**, for the scoped position-chain, cyclic, reversal and
expressly marked statements in the canonical mathematical files. The actual
fixed coupling is tau=10^-80 throughout; N runs through odd dimensions.
These are internal project proofs and finite controls, with no priority,
external referee, analytic formalization or full BGS claim.

Pinned base: `0ffb20cc152d0ddd2620887e46d21d1120b95fd8`.
The review was performed read-only against this pinned base. The strongest accepted position-chain estimate owns the cyclic-ramp corollary; the earlier weaker proof is provenance only.

## Canonical claim cards

- FM-021: P_xy=|U_xy|², J_xy=1/N satisfy
  limsup ||P−J||<=10^-64, and eventually ||P^L−J||<=2^-L simultaneously for
  every integer L>=0. For the exact cyclic word-pair contribution D_m,
  D_m/m->1 uniformly on positive compact Heisenberg bands. Its Section3
  separately defines a distinct-port marked three-link expression and proves
  |E_dist(L)|<=C³N2^-max L_i, including zero-length links. It makes no
  once-counted unmarked-family assertion.
- FM-022: Q_xy=U_xy conjugate(U_yx) satisfies ||Q||->0, and the
  reverse-cyclic ordered pairs with cyclic pairs excluded are negligible
  after division by m on every such band. No decay rate or effective startup
  is claimed.

All source/target spaces and normalizations are in
`../mathematics/fixed_map_path_model.md`. Complex matrix amplitudes are retained;
no prime-N restriction, symmetry, phase averaging, noise, or variable-tau
limit is introduced.

## Corpus reconciliation and proof ownership

The pinned authorities were read: AGENTS, SOURCE_OF_TRUTH, repository
conventions, research brief, ledger, registry, results and obligation board.
There is no `.mathbox/` ledger in this checkout. Comparing the old source base
fa007c498fe116a814a90aa3215cfd65b1f2a154 to the pin shows:

- FM-001's model, forced ordinary half-shift and derivative bounds are
  unchanged; the expanded classical symmetry proof is not used here.
- FM-007 is byte-identical. It supported the older fallback proof, but the
  new canonical constant-gap proof does not depend on it.
- FM-018's relevant Weyl/Egorov sections are unchanged. Its O24 plateau
  correction was already respected by the older cyclic note. The stronger
  canonical proof no longer requires its Egorov or mixing machinery.
- Corpus repairs to noise, heat, entropy and arithmetic results do not enter
  the final dependency closure. CI is provenance, not proof of any limit.

The accepted constant-gap/marked candidate is pinned to SHA256
156808b1febd7b61a8aff4e4756314934e5cb6b471c7e5a2f15a6f5f64f216af.
The exact reviewed source hash is retained in the execution manifest; the independent marked audit is `marked_path_independent_review_20261006.md`. The common finite-difference construction and reversal argument were also reconstructed separately. No subsequent unmarking continuation is part of this theorem scope.

## Dependency graph and reconstructed obligations

Shared: exact raw matrix -> ordinary finite shifts -> exact four-branch
Gauss sum -> analytic global HJ graphs and lattice gluing -> two transport
equations -> finite Taylor residual -> unitary Duhamel -> leading kernels.

Position: shared kernels -> four near-unit branch-diagonal amplitudes +
twelve nonzero same-coordinate mixed phases at the specified tau -> shared
alias-safe discrete TT* + analytic zero-set cutoff -> constant singular gap
-> simultaneous stochastic power bound -> exact cyclic multiplicity and
repeated-word bound. The marked branch additionally uses one freely summed
uniform link and distinct-column orthogonality, then the longest-link bound.

Reversal: shared kernels -> sixteen swapped-coordinate mixed phases at the
specified tau -> shared discrete norm lemma -> ||Q||->0 -> exact reverse
multiplicity and all three reflection cases -> Heisenberg reversal decay.

No circular dependencies occur. Reversal uses its own WKB q_N=O(N^-1)
bound, not FM-021. Neither claim imports a continuous FIO theorem, classical
centralizer/mixing theorem, noisy channel gap or BGS theorem.

### Passed obligations

1. Raw/ordinary dictionary, all odd composite dimensions and modular phases.
2. Exact initial Gauss identity and phase/amplitude wraparound gluing.
3. Global analytic characteristic graph at the physical time.
4. Unambiguous transport hierarchy: a0+h a1 cancels h^0 and h^1; entry
   residual O(h^(5/2)), operator/Duhamel error O(h^(3/2)).
5. Conservative C² bound ||S_tt||<=10^50 reconstructed with a
   submultiplicative derivative norm rather than an informal product count.
6. Reversal coefficient (pi/128)tau; same-coordinate difference coefficient
   at least sqrt(2)(pi/128)tau; both exceed remainder 10^50tau²=10^-110.
7. Independent small upper bound 2*10^9tau+10^50tau²<1/4, which excludes
   nonzero integer lattice aliases. Nonvanishing alone would not suffice.
8. Discrete TT*: row-pair phase denominator is bounded below by c|i−i'|/N;
   total reciprocal variation has the same inverse-distance order. Thus
   off-diagonal TT* entries are O(1/[N|i−i'|]) and the squared norm is
   O(log N/N) on each fixed good rectangle.
9. Bad-set removal uses **unnormalized** Hilbert–Schmidt norm, which dominates
   operator norm. It is distinct from normalized HS used in the old
   diagonal-channel proof. Take N->infinity before shrinking the cutoff.
10. Leading transport: |a0−1|<2*10^-66, hence |d−1|<10^-64.
11. No normality assumption in the power or trace bounds.
12. Periodic words and all reflection cases, including the two loops in
    an even edge-axis reflection.
13. Marked cancellation uses distinct ports and an unmasked endpoint. Exact
    finite counterexamples prohibit a universal unmarking prefactor and
    disprove the specified lexicographic free-endpoint shortcut.

### Out of scope/open

A once-counted unmarked reconnection estimate; every other noncyclic pair;
higher factorial comparison; effective startup; analytic Lean certification;
world priority; full TRACE-005 and deterministic BGS.

## Evidence and reproduction

Run `python computations/verification/actual_path_theorems.py` and with `python -O`.
The stdlib-only checker uses explicit RuntimeError conditions; normal and
optimized runs both pass. In both modes, `--inject-failure` returns nonzero.
It uses exact integers and Fractions, with no floating tolerances.

Coverage: all interval displacements at 119 odd N=15,...,251; all 32 Gauss
residue cases (a complete modular reduction); finite Weyl congruences at odd
N=3,...,81; all sixteen reversal coefficients and twelve position-difference
coefficients; rational fixed-time comparisons; every word for a rational
non-symmetric U(3) at m=1,...,7; every reflection; complex rational marked
contractions at (0,0,0), (0,1,2), (1,2,3), each link in turn uniform.

Original diagonal/reversal finite scripts and the independent marked check
are replayed separately, with source hashes. Their historical assert-based
implementations are not promoted as optimized-mode-safe verifiers. The
canonical checker does not rely on them. They establish finite algebra only.
No PDE or fixed-tau asymptotic was numerically simulated.

`../evidence/executions/20261006/path-theorems/receipt.json` records actual commands and outcomes;
the associated source manifest records source and overlay hashes. The manuscript
section is an integration proposal; a standalone compile is a typesetting
check, not synchronization with the repository manuscript or analytic proof.

## Exact remaining gap and cheapest integration check

For R_m^other=|Tr U_N^m|²−D_m−R_m^rev, the unproved pair target is

N^-2 sum_m w(m/N)R_m^other -> integral [min(xi,1)−xi]w(xi) dxi.

Above xi=1 this is a negative correction. Neither the strong P gap nor the
marked estimate bounds it. Higher signed factorial orders remain separate.

The maintained proofs are `../mathematics/position_chain_mixing.md`,
`../mathematics/four_branch_parametrix.md`, and
`../mathematics/reversed_path_decay.md`. Exact execution scope and source hashes
remain attached to the dated evidence; finite checks do not strengthen any
asymptotic claim. The manuscript is an exposition of these sources, not an
independent stronger theorem.

## Integration identity

The canonical position theorem changes only its proposed-ID header to stable FM-021; the reversal theorem gains a stable FM-022 header. Current proof/source hashes are pinned by the portable execution receipt. The earlier reviewed candidate and review hashes remain in the provenance discussion; no new unmarked-family continuation is included in this promotion.
