# Phase memory and rational-inner jets: source and overlap review

**Reviewed:** 8 October 2026. **Scope:** the three newly reconstructed proofs,
not a priority certification or review of every historical BGS result.

The supplied file is `BGS_verified_manuscript_2026-10-07(1).pdf`, 293 pages,
SHA-256 `0f7af7c3867f6e3a179a4d2458bac18ff3dc441a6968b7e553dea40a68957090`.
Its title page says revised 6 October; neither its filename nor PDF metadata
is an acceptance certificate. Sections 89.1--89.3 contain TRACE-053--055.

## Coverage of the complete attachment

The article is preserved as a scientific source, not accepted as one indivisible
theorem. Sections 1--68 were not re-certified in this pass. Sections 69--85
substantially overlap indexed main results; the maintained proof and ledger
determine their scope, including qualified Wave2 and complete **unmasked**
Wave3 conclusions. The table below records the additional assertions in
Sections 86--88 without turning their source labels into accepted registry IDs.
The PDF cites separate raw proofs/reviews that are not embedded in the supplied
file; the closing evidence paragraph of Section 86 also distinguishes
unauthenticated author-suite output from replayed evidence.

“Pending” below means that the full argument and its dependency closure have
not been reconstructed. It does not mean that a counterexample is known.

| Article locator and source label | Asserted mathematical content | Maintained disposition |
|---|---|---|
| 86.1, TRACE-030 | All-degree absorbed current resummation and a finite cutoff/current identity | Candidate; the actual signed current estimate $\mathbb E J_N(q,1)=o(N^2)$ is still a separate input |
| 86.2, TRACE-031 | Dressed-coordinate comparison with a logarithmic rate | Candidate; its leading coordinate-phase statistic is not identified with CUE |
| 86.3--86.4, TRACE-032/033 | Finite one-$Q$ compact completion and a specific large-deformation obstruction | Pending reconstruction of the exact functional and obstruction; not a universal no-go theorem |
| 86.5, FM-032 | Absolute Weyl tube for the literal fixed map | Pending full uniform locality argument |
| 86.6--86.7, TRACE-034/035 | Signed first returns and sparse signed kick-class reductions | Pending complete signed identities and once-counted class bounds |
| 86.8, FM-035 | Relative-frequency lightcone | Pending the stated all-dimension lightcone argument |
| 86.9, TRACE-036 | Secular Gram and weighted-minor energy identities | Pending normalization and complete minor-energy derivation |
| 86.10, TRACE-037 | Reused-phase cavity bounds for a fixed prescribed small eliminated set | Pending covariance/concentration proof; fixed-set control does not give simultaneous adaptive control over all subsets |
| 86.11, FM-033 | Further literal-time arithmetic cases, including the $N=4375$ endpoint | Pending raw splitting/nonreturn certificates and their analytic bridge; inherited bounded cases keep their existing main status |
| 86.12--86.13, FM-034/036 | Transverse-moment and curved-boundary splitting | Pending complete arithmetic branch coverage; no all-$j$ conclusion is inferred |
| 87.1, FM-037 | Simple spectrum of the unchanged $U_N(t)$ for $N=7\cdot5^e$, $e\ge1$, every nonzero real algebraic $t$ | Pending complete disjoint cat-group splitting and all inherited endpoints; main FM-026's multiplicity bound is not relabelled as this stronger theorem |
| 87.2, FM-038 | All-output two-translation decay and a $d^{259}/N$ grid bound at fixed $\tau$ | Pending the uniform oscillatory proof; main's earlier $262$ exponent remains its accepted scope |
| 87.3, TRACE-038 | Diagonal source covariance and deterministic paving of four Hermitian parts | Pending exact covariance orientation and the external paving hypothesis map |
| 87.4--87.5, TRACE-039/040 | Separate even finite-jet and logarithmic compact Ward functionals, with localization failures | Pending each functional's full algebra and the scope of its negative control |
| 87.6--87.7, TRACE-041/042 | Fixed-fraction and near-full random-cavity propagation | Pending all-time concentration and stopped-process inputs; no changed phase law is substituted |
| 87.9, TRACE-043 | Physical-source increment and second-moment reduction | Pending proof; the leading radial energy remains an unevaluated quantity |
| 87.10, TRACE-044 | Arbitrary complex-source covariance for deterministic contractions, with input/output defect weights | Pending self-contained covariance proof; same-phase adaptive source matrices are excluded by the article itself |
| 87.11, TRACE-045 | Original-radius anisotropic physical-source equivalence in the near-full regime | Pending complete proof, including the corrected complex-conjugation convention and the actual delay inside the exponential |
| 87.12, TRACE-046 | Diagonal delay concentration and $mN^{-2}\operatorname{Tr}T^2\to2-m/N$ | Pending joint barriers and concentration; diagonal isotropy would not imply matrix scalarization |
| 87.13, TRACE-047 | Fixed-flatness reused-phase channel and averaged eigenbasis pinching | Covered by the stronger maintained TRACE-053, as checked below |
| End of 87.7, FM-039 | Optional reverse-kernel decay rate | Conditional source assertion with three named WKB leaves; not an input to maintained TRACE-053 |
| 88.1 | Weak source-weighted $L^2$ scalarization and the actual third-delay-moment formula | Pending the weighted source proof and stopped moment/concentration argument; TRACE-056 is an unweighted normally absorbed $L^1$ theorem |
| 88.2 | Defect-weighted logarithms, all fixed mixed source moments and determinant-ratio reduction to a near-full cavity | Pending full rare-event, covariance and analytic-continuation proofs; the actual scalar cavity law remains unidentified |
| 88.3 | Polylogarithmic all-time boundary flatness and stochastic-complement mixing | Pending all-time proofs; the article separately retains physical delay barriers as inputs at this depth |

The source's Section 87.8 explicitly corrects an unrestricted exact delay
martingale statement. Any reconstruction must keep the stopping rule and
the crossing-state contribution, rather than reusing that rejected shortcut.
Section 88.1's proposed cubic law is

$$\frac{m^2}{N^3}\operatorname{Tr}T^3
=6-6\frac mN+\left(\frac mN\right)^2+o(1)$$

in its stated near-full regime. This is recorded as a **candidate input**, not
a consequence of the sharp matrix-jet inequality. The latter bounds derivative
energy by a cubic moment; it cannot provide that moment in the reverse direction.
Section 89.3 claims a deeper endpoint $m=\lceil\log(2N)^{20}\rceil$; that
assertion has the explicit TRACE-055 pending disposition in the current ledger.

### Checked fixed-flatness overlap

For Section 87.13, assume $\delta\le C/m$, $C\ge1$. Maintained TRACE-053 gives

$$\|T_n-A^n\|
\le(n!-1)\sqrt C\,m^{-1/2}+n!n(n-1)C/m.$$

For $n\ge2$, $(n!-1)\sqrt C\le n!C^{n-1}$ and
$C\le C^{n-1}$. Thus it implies the article's
$n!C^{n-1}[m^{-1/2}+n(n-1)/m]$ bound. Degree one is exact in both formulations;
the exact degree-two norm and averaged pinching also agree. This checks a
genuine overlap without importing any cavity, reverse-kernel or physical-source
assertion from the adjoining sections.

## Exact relationship to the submission

| Submitted statement | Maintained disposition | Mathematical change |
|---|---|---|
| Section 89.1, max-entry phase channel | [TRACE-053](../mathematics/max_entry_phase_channel.md), project proof | Full unrestricted-mark argument, both occupation-collision corrections, exact degree-two norm, explicit delta-only pinching rate |
| Section 89.2, integrated second jet with 13/3 | [TRACE-054](../mathematics/sharp_inner_jet.md), strengthened project proof | Optimal universal 4/3 for all square finite rational inner matrices F=zG, lower-order corrections, smooth localization with its derivative penalty |
| Section 89.3, actual polylogarithmic deep-source hierarchy | TRACE-055, verification-pending | The summary asserts quantitative joint barriers and covariance/continuation inputs whose raw proofs have not been reconstructed; no unconditional promotion |
| Real-flow normally absorbed scalar consequence | [TRACE-056](../mathematics/phase_channel_real_flow.md), direct project proof | Independent eigenphase transport and common-phase L1 smoothing; no dependence on the submitted physical-cavity assertions |

The phase occupation expansion, Fejer positivity, Poisson kernel identities,
finite inner factorization, matrix weighted Cauchy and common-phase smoothing
are familiar mechanisms. Their use here is not a claim to have invented them.
The matrix proof gives a complete cascade argument for the stated sharp
right-weighted inequality; its external priority remains unresolved.

## Primary sources inspected and exact limits

1. Daniel Alpay, Palle Jorgensen and Izchak Lewkowicz,
   [Characterizations of rectangular (para)-unitary rational Functions,
   arXiv:1410.0283v2](https://arxiv.org/abs/1410.0283v2), revised 4 January 2015;
   published in *Opuscula Mathematica* 36(6), 2016, starting at page 695,
   [DOI 10.7494/OpMath.2016.36.6.695](https://doi.org/10.7494/OpMath.2016.36.6.695).
   The primary abstract expressly includes Blaschke--Potapov characterization
   and distinguishes square and rectangular cases. This is precedent for
   factorization, not a retrieved theorem establishing our derivative bound.
   TRACE-054 includes its own finite square-factorization proof, so this
   bibliographic item is not a load-bearing unverified theorem leaf.
2. T. S. Mardvilko,
   [Integrate inequalities for the higher derivatives of Blashke product](https://www.mathnet.ru/eng/bgumi125),
   *Journal of the Belarusian State University. Mathematics and Informatics*
   1 (2018), 10--16. The primary journal abstract concerns scalar higher
   derivative Lp estimates. Only metadata/abstract were checked in this pass;
   they do not establish absence of an overlapping weighted inequality.
3. Jonathan P. Keating and Sebastian Mueller,
   [Resummation and the semiclassical theory of spectral statistics](https://arxiv.org/abs/0708.2375).
   The retrieved primary paper discusses the generic quantum-chaos question
   and known arithmetic exceptions. It does not imply a deterministic
   all-system theorem or supply the maintained map's signed trace estimate.

## Search coverage and novelty boundary

Web searches covered exact combinations of rational matrix inner, boundary
delay, weighted second derivative, cubic trace, Blaschke derivative and
Potapov factorization. A SciSpace semantic search used the full proposed
matrix inequality and returned relevant factorization literature and many
unrelated delay-equation inequalities. Such search results are leads, not
theorem verification. This was not exhaustive coverage of operator-valued
Bernstein inequalities, passive-system delay bounds or unpublished work.

Consequently the maintained status is **proved within this project, priority
not established**. No Fields/Poincare-level or world-first attribution is
made. No new external dependency is needed for the self-contained proofs.
