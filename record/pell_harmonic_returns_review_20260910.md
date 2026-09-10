# Harmonic return law: proof and execution review

Date: 10 September 2026. Base commit:
`50ed425c62d6b63f80cf02032ac67fbd9014121c`.
Checkpoint: `pell-harmonic-returns-20260910`.

## Exact result and research decision

`mathematics/pell_harmonic_returns.md` proves the global eigenvalue law
of the actual unitary $U_{\epsilon,a}^K$ with
$\epsilon=\tau/\sqrt{2K}$, fixed $\tau$, and sampled unit harmonics
$a\le L_K=N^{\beta+o(1)}\le\sqrt N$. Every fixed Fourier moment converges
in $L^2$. The endpoint moments are wrapped normal and free unitary Brownian;
an ordered cycle-pair series defines the intermediate measures.
For $\beta\ge1/6$ the second-return moment has a closed formula.

The primary BGS objective remains unresolved: return multiplicities are
fixed, so the theorem concerns logarithmic times. It neither controls
Heisenberg-time joint traces nor proves a local eigenphase law.

The route advanced beyond the preceding weighted-observable theorem by
proving uniform summability for time-ordered exponentials:

1. Truncate the absolute Fourier--Bessel order at $K^{2/3}$.
2. Lift all short central congruences into the integer image of the cyclic
   operator $S^2-6S+I$.
3. Use $\|Mq\|_1\ge4\|q\|_1$ and Bessel convolution to bound the entire
   nonzero aggregate contribution by $O_{m,\tau}(K^{-1})$.
4. Reduce balanced arrays to a summably dominated set of order-two active
   sites, then apply the harmonic phase lemma.

This avoids assuming that moment convergence alone gives an ordered
exponential limit. The earlier small-harmonic commuting normal form is
not extended to harmonics with macroscopic crossing phases.

## Independent proof review

One second agent reviewed the exact Weyl and Pell inputs, then independently
reconstructed the truncation, integer-image argument, modified-Bessel bound
and factorial active-site tail. It found no blocking flaw.

The same reviewer subsequently checked the written proof, initially with
SHA-256
`b4629927c8cf08a1e5b6475df832c23a403711b8643e43a5f33edcece2df8da7`:
the ordered-simplex two-copy phase limit, largest-label noncrossing
recurrence, formal Lagrange inversion, circle-clique calculation,
and probability-measure existence and continuity all passed.
It requested an explicit first-endpoint ordering convention for exact
crossing signs, and the elementary edgeless-grid limit. Both clarifications
are incorporated in the final source.

This is an independent agent review, not external referee acceptance,
a machine-checked theorem, or evidence of worldwide novelty.
The completed certificate pins the final source and generated TeX hashes.

## Finite computation contract and actual execution

Producer: `computations/verification/pell_harmonic_returns.py`.
The version-2 bounded-run manifest, result and execution logs are in
`evidence/certificates/pell_harmonic_returns_20260910/`.
The manifest validator passed with the repository root and verified
input and result hashes.

The deterministic run used Python 3.12.14 and NumPy 2.3.5, a 60-second
wall cap, 50-second CPU cap, 2 GiB address-space cap, one affinity core
and cooperative one-thread library settings. Actual elapsed time is
recorded in the manifest; no random sampling was used.

| Implemented finite assertion | Scope and outcome |
|---|---|
| Direct ordered Weyl multiplication versus signed crossing phases | 191304 exact words at $K=11$, harmonic $a=2$, labels $j^2\bmod11$, all orientations and stated cycle-type lists |
| Noncrossing type enumeration | $1\le m\le5$, $0\le\ell\le\min(m,4)$, all lists; agrees with the Laguerre coefficients |
| Independently implemented coefficient recurrence | 144 exact rational checks, $1\le m,\ell\le12$ |
| Cyclic integer-image congruences and norm inequality | 2457 vectors, $K=3,5,7$, all entries in $\{-1,0,1\}$ |
| Growing-order norm cutoffs | Exact rational checks at $K=19,31,61,127$, $R_0=7,9,15,25$ |
| Pairwise circle closeness versus unique covering arc | 17812 distinct subsets on circles of size 7, 11 and 17, subset sizes 2--4, radii below one third |
| Odd unitary matrix return versus independent Weyl/Bessel algebra expansion | Six floating controls at $(K,m)=(3,1),(3,2),(5,1)$, harmonics 1 and 2, $\epsilon=0.23$ |

The maximum finite matrix discrepancy is approximately $8.04\cdot10^{-8}$.
Every discrepancy is below its analytic omitted-Bessel-tail bound plus
$3\cdot10^{-12}$ floating tolerance. The largest truncation bound is
approximately $1.42\cdot10^{-5}$. These are approximation controls, not
exact arithmetic certificates for numerical diagonalization.

One precheck failed because the upper estimate $\sqrt2<3/2$ was too coarse
to certify the $K=19$ cutoff. Replacing it by the exact rational upper
bound $99/70$ resolved that certificate failure. The mathematical cutoff
and asymptotic argument were unchanged.

The computation validates finite identities and conventions. It cannot
establish asymptotic phase cancellation, external source claims or BGS.
No new Lean compilation was performed.

## Literature and priority

Nizar Demni, *Lagrange inversion formula, Laguerre polynomials and the free
unitary Brownian motion*, [arXiv:1606.03755v3](https://arxiv.org/pdf/1606.03755v3),
page 1, equation (1), gives exactly
$e^{-mt/2}L_{m-1}^{(1)}(mt)/m$ for the conventional free unitary Brownian
moments. The primary research paper was inspected directly. Our proof
derives the moments internally; the citation identifies the known law.
It does not supply any arithmetic quantum-map limit.

The generic graphon moment constructions and the preceding arithmetic
phase lemma retain their separate provenance in
`literature/pell_harmonic_transition_sources.md`.

Searches for cat maps with free unitary Brownian laws and graphon unitary
Brownian laws did not provide a directly matching primary theorem in the
returned results. This limited search is not evidence of priority.
The unrelated arXiv:2410.11240 concerns interacting particles on random
graphs and is not used as a proof input.

## Publication and next unresolved implication

The canonical manuscript now builds to 169 pages. The new proof is Section
25, pages 46--50; these pages and the following section transition were
rendered and visually inspected. The three-pass build passed with no
horizontal overflow or unresolved references. Its PDF SHA-256 is
`e1f053b0879c809da943c4101e8b0d50034356ab06edc9d039696bd4e1dd5b04`.

`assets/figures/pell_harmonic_returns.svg` plots analytic second-return
formulas, produced by `computations/analysis/pell_harmonic_returns_figure.py`.
It contains neither sampled finite spectra nor fitted curves.

The next discriminating problem is quantitative uniformity when the return
multiplicity grows. The current absolute bound contains an exponential
in $m^2\tau^2$, and the phase lemma discards neighborhoods whose complexity
grows with the number of chords. These dependencies must be controlled
before claiming even a growing-return regime. Replacing $m$ by $D/K$ in
the fixed-$m$ theorem is invalid. The exact Heisenberg-scale objective
remains in `mathematics/open_questions.md`.
