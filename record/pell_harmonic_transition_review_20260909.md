# Harmonic transition: proof review and execution record

Date: 9 September 2026. Base commit:
`580674f30007b6cbcb667895a1de61e36edfc0cc`.

## Result and exact boundary

The new proof concerns the fixed Pell cat map, unit physical harmonics
$1\le a\le L_K\le\sqrt{N_K}$, and $\log L_K/\log N_K\to\beta\in[0,1/2]$.
All fixed compressed-observable moments converge in $L^2$ over harmonics,
uniformly over the odd eigenspaces, to circle-graphon crossing moments.
The global empirical measures converge weakly in probability.

The proof also gives an explicit sixth moment, unbounded limiting support
before the semicircle endpoint, weak continuity at that endpoint, and an
ordered weighted-moment theorem with commutator limit $8\beta(1-\beta)$.
The graphon measure construction itself is prior work. Priority for its
Pell harmonic realization is not established.

These are not local eigenphase statistics of the propagator, a
fixed-observable semicircle law, or a proof of BGS. Frequencies are sampled
and grow with dimension. Convergence is not asserted for every individual
harmonic in the sampling window.

## Research decisions and proof audit

Three routes were examined:

1. Transfer the full Cayley--Jacobi trace CLT to powers of a quantum
   propagator. The exact compression identity does not make parameter
   multiples into matrix powers. The repository already has the corresponding
   restricted magnetic global law; repeating it would not close the gap.
2. Improve sparse Cayley energy using reciprocal shifted-subgroup results.
   No applicable improvement was verified. No new energy bound is claimed.
3. Change the physical harmonic scale in the fixed Pell map. This yields
   the quadratic phase and the distance-threshold mechanism proved here.

A bounded independent review caught the important normalization issue:
the physical harmonic becomes $W(aq_0,a)$, hence magnetic parameter
$a^2q_0$, not $aq_0$. That correction is incorporated throughout. The
independent review did not finish an audit of the complete limit theorem.
The remaining analytic proof was checked by the authoring assistant.
External referee acceptance and complete independent validation are pending.

The self-review checked the following load-bearing points explicitly:

- the dilation preserves each parity/character sector;
- invertibility of $a$ preserves both central-word congruences;
- the proportion of nonunits is $O(1/\log K)$ even for short windows;
- bounded-cluster counting controls nonpaired words uniformly in $a$;
- distinct edge-distance ties occupy finitely many proper affine
  hypersurfaces, including shared vertices and two-copy configurations;
- the largest separated Pell term dominates with a coefficient of modulus
  one, so high phases cannot cancel;
- quadratic differencing applies to rational phases and avoids a false
  linear-parameter geometric-sum argument;
- the two-copy estimate establishes $L^2$ convergence, not just the mean;
- the common leading term gives uniformity over sectors without a factor $K$;
- moment existence, determinacy, uniform integrability, and the two endpoints
  are justified separately;
- the triangle term is not replaced by the cube of the edge density;
- limiting unbounded support is proved from moment lower bounds, without
  making a finite-matrix edge assertion.

## Executed checks

The version-2 bounded-run manifest and result are in
`evidence/certificates/pell_harmonic_transition_20260909/`. The manifest
validator passed with the repository root, including input and output hashes.
The run used Python 3.12.14, NumPy 2.3.5, a 60-second wall limit, one
CPU affinity core and cooperative one-thread numerical-library settings.
The finite verifier finished in about 1.5 seconds.

| Check | Actual execution |
|---|---|
| Pell order/unit/phase identities | $K=3,5,7,11,19,31,61,127$ |
| Direct ordered Weyl words versus crossing phases | 192324 exact identities, through ten positions; $K=11$, three stated label arrays and harmonics 1 and 2 |
| Integer circle triangle geometry | 65 complete radius/modulus designs |
| Rational sixth-moment and commutator formulas | 119 interior parameters; exact $\beta=1/4$ witness $143/16\ne71/8$ |
| Independent physical potential versus squared-parameter block | 36 spectra; $K=3,5,7$, three sectors and four harmonics |
| Maximum correct spectral discrepancy | $2.886579864025407\cdot10^{-15}$ |
| Linear-parameter negative control | maximum discrepancy $1.963920354471784$ |
| Finite quadratic-sum inequality | 15 floating rational-phase controls |

The independent matrix construction applies the explicit Fourier/chirp
conjugation to the physical multiplication operator. It is not a comparison
of two calls to the same block assembler. The exact phase checks compare
ordered Weyl multiplication to crossing-graph bookkeeping. The finite label
arrays are not an exhaustive enumeration of all labels at every order.

Wolfram Language independently simplified the triangle-area integral to
$3b^2+(1-3b)^2\mathbf1_{\{3b\ge1\}}$ on $0\le b\le1/2$, using:

```text
FullSimplify[
  2 Integrate[2 b-z, {z,0,b}] +
  Piecewise[{{2 Integrate[2 b-z, {z,1-b,2 b}], b>=1/3}},0],
  Assumptions -> 0<=b<=1/2]
```

This is a bounded symbolic check, not an independent proof of the limiting
quantum law.

## Numerical illustration

`computations/analysis/pell_harmonic_transition_figure.py` uses exact integer
modular phases before floating evaluation. The data are in
`evidence/numerical/pell_harmonic_transition_20260909.json` and the figure is
`assets/figures/pell_harmonic_transition.svg`.

The design uses $K=31,61,127$ and $\beta=0,1/8,1/4,3/8,1/2$, with seed
20260909. For nontrivial windows, 512 accepted unit harmonics are sampled
with replacement; 128 are used for the sixth pairing proxy. At $\beta=0$
the sole harmonic is exactly $a=1$.

The fourth central term is accompanied by the proven finite block remainder
$8K^3/(N-1)$. The sixth curve is explicitly a pairing proxy without the
repeated-label subtraction. Commutators use the normalized full-space
Hilbert--Schmidt identity; the proof gives the same odd-space limit.
Sampling error bars do not include rounding or finite-size bias.
No asymptotic claim is inferred from agreement of these points with a curve.

## Publication, provenance, and limits of this pass

The canonical manuscript built successfully to **165 pages**, with no
horizontal overflow or unresolved references/citations. The new Section 24
occupies pages 40--46; all seven touched page images were visually reviewed.
The build manifest pins every TeX input. PDF SHA-256:

`c01aa753b786180cdfccfc18d74d153e46dd8499a1431bbd605b220ed379a65d`.

| Source | SHA-256 |
|---|---|
| `mathematics/pell_harmonic_transition.md` | `97504d7730110aa7e2131d3157d72d75ff7c2d4fd2e09fc00de38d3e68bfc05c` |
| `manuscript/unified_sections/pell_harmonic_transition.tex` | `df82ce787e9f2dee33a0540c42724a98eb7a9946a443082c2f0ce972c5a7bbab` |
| `computations/verification/pell_harmonic_transition.py` | `548870034d1441475b06b40a6131b729e94eeb70dce9b83b343a2c0addf7bb85` |
| `computations/analysis/pell_harmonic_transition_figure.py` | `fc8278fecee32509f0b5d2ac4ab2ad0339489e134b92e32da65b59f28c944574` |

The TeX section is a Pandoc rendering of the proof note with its labels
prefixed `pell-harmonic-` and the local Markdown source link replaced by
the reference to the preceding Pell section. The mathematical content
is the same.

No new Lean theorem was compiled. The old full verification corpus and all
16 existing Lean modules were not rerun; their earlier execution records
are not upgraded by this pass. The new finite checks and typesetting checks
are explicitly narrower than a complete audit of the whole manuscript.
