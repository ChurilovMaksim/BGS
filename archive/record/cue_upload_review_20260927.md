# Audit of cue_project.zip, 27 September 2026

**Primary verdict: incomplete, with a missing higher joint-trace implication.**
The submitted TG-mean assumptions, if imposed on an exact decomposition with
the stated remainder, imply the scalar pair-Abel limit. They do not establish
all microscopic correlations. Several supporting statements are also false
as written or concern the wrong classical symbol. The original quantum
matrix builder does implement the maintained frozen model.

This is an author-level audit of another agent's submission, not independent
external refereeing. The entire `solution.tex` and the verification path were
read. Exploratory scripts were inspected for mathematical role and dependencies;
not every standalone experiment was rerun. No broad novelty claim was checked.

**Source identity:** archive SHA-256
`d57addcb06dfb0fcd82db5326c5930532bccbd19ed04b6ceeb886650edeeb3bd`;
`solution.tex` SHA-256
`4732cac1eb173a0308c12dfb61e2622b9dd2ec9dcfc8aae8e1d573bc6680217c`.
The [member manifest](../evidence/20260927/cue_upload_manifest.json) pins every
attached file. The original archive remains the submitted source, not an
active repository manuscript. Cached paper text, bytecode and exploratory
duplicates were not imported into the maintained corpus.

## 1. Claim and dependency audit

| Submitted item | Obligation / verdict | Integration decision |
|---|---|---|
| T1 unitarity and symmetry class | Unitarity is elementary and reproduced. Checking two involutions does not classify all fixed classical involutions; its ordinary symbol is wrong. | Reuse existing BGS-FM-001 and FM-009 within their stated scopes. |
| T2 global law | The displayed error $mC\tau N$ does not vanish as $N\to\infty$ at fixed $\tau$. The subsequent FIO reference is an additional argument, not supplied by this inequality. | No promotion from this proof. |
| T3 ordered trace product | Passed as an algebraic identity. Its classical symbol translation needs correction. | Already in `frozen_spectral_flow_controls.md`. |
| T4, T5, T12 pure trace/kernel identity and receding revivals | Correct arithmetic content, already covered more strongly by BGS-FM-010. Floating closeness plus root-of-unity discreteness alone needs a certified error to prove a particular phase. | No duplicate theorem; retain exact-grid consequence below. |
| T6, T7, T8, T9 stationary phase / diagonal / Ehrenfest | T6 explicitly withdrawn in part; T7 assumes diagonal dominance and genericity; T8/T9 omit quantitative symbol-dependent remainders. The raw-symbol critical circles are not those of the actual physical symbol. | No fixed-strength or Heisenberg promotion. |
| TG-mean, main theorem (a) | Conditional pair-Abel implication is a direct weighted-sum argument. The needed model-specific decomposition estimates are open. | Record precise logical boundary, not a proved input. |
| Main theorem (b), Newton and loop hierarchy | Failed implication from pair moduli to higher correlations; loop assumptions also include unspecified QE errors and a sine input. | No all-order theorem. Exact counterexample below. |
| T10, Addenda H/J: $|\operatorname{Tr}(A_NM_N)+1.1|\approx160/N$ | Refuted across odd residue classes without Gauss-phase normalization. Constant 160 is a fit, not a proved estimate. | Add regression guarding the missing phase. |
| T11, Addenda L/U/X: kick expansion and breakdown | First derivative exact; a general uniform trace remainder needs the dimension factor. A finite-matrix exponential is entire, so failed low-order truncation is not a finite convergence/Borel radius. | Retain corrected finite Taylor identities and bounds below. |
| Addenda H/O: annihilator, exact averaging | Correct mechanism; floating search does not prove the all-time threshold. Bandwidth is 9, not 8. | BGS-FM-012 supplies exact rectangular lattices and all-time proof for the physical symbol. |
| Addenda D/E/G: short pairs and diagonal counts | Finite short-pair sum is $O(N^{-2})$ under the specified linear-map amplitudes. $\sum_\gamma d_\gamma^2/|P_m|$ is an exact expression, not identically $m$ (e.g. $m=2$: $60/32$). | Useful scope clarification, not a nonlinear diagonal or plateau theorem. |
| Addenda F/K/V: Cayley formula | Small cases agree after a fitted eighth-root phase; full reciprocity/phase derivation remains a sketch. | Finite validation only; no global exact formula promoted. |
| Addenda M/N/T: pair, variance, bispectrum checks | Pair Fourier identity and infinite Parseval identity are standard. The submitted bispectrum has the inverse Fourier sign wrong and counts coincident indices. | Explicit counterexample and corrected distinct-triple formula below; general bridge already BGS-TRACE-001/002. |
| Addenda J/V: Dolgopyat impossibility | An available upper bound tending to one is not a lower bound on the actual radius. Unitarity on $L^2$ does not determine the spectrum on an anisotropic space. | Claimed general no-go not established; no source theorem imported. |
| Numerical C/I/M/R/S/T/W/X and HANDOFF | Proxy matrix data reproduced at stated instances. Trimmed slopes, broad tolerances, degenerate eigenbases and two-point rate fits do not prove CUE, QUE, a noise mechanism or a convergence rate. | Preserve scoped evidence and correct the Abel tail. |

Dependency closure: exact lattice factorization $\to$ finite character
orthogonality $\to$ linear periodic-point average is proved below the BGS
frontier. Separately, an exact trace decomposition + TG-mean diagonal/off-diagonal
and remainder estimates $\to$ scalar Abel limit is conditional. The arrow
from this scalar information to mixed traces of every order is missing.
The maintained BGS-TRACE-003 criterion asks for those mixed traces explicitly.

## 2. The classical symbol mismatch

The upload uses $a(q,p)=v(q)+r(q)\cos(2\pi p-\alpha)/100$ in
`classical_pairs.py`, `orbits.py` and the article. With its actual modular
midpoint $h=(N+1)/2$, the ordinary symbol is instead
$$
 g(q,p)=v(q)+r(q+1/2)\cos(2\pi p-\alpha)/100.
$$
This is the already maintained BGS-FM-001 dictionary. At odd $N>18$,
quantizing $a$ with ordinary midpoints gives the exact discrepancy
$N^{-1}\|A_N-\operatorname{Op}^{\rm ordinary}_N(a)\|_{HS}^2=1/5000$.
The new regression confirms it at $N=19,31,101$.
This is not an $O(1/N)$ correction, and the unchanged quantum builder
does not validate the substituted classical orbit sums.

For example, at $q=1/7$, $p=\alpha/(2\pi)+1/4$,
$$
 \partial_p g=-\frac{2\pi}{100}\,2(1-\cos(2\pi/7))\ne0.
$$
Thus the raw-symbol critical circle at $q=1/7$ is not a critical circle
of the physical symbol. The full critical circles $q=0,1/2$ do persist;
we make no claim here classifying its remaining isolated critical points.
The corrected linear averages happen to agree with the raw ones because
the changed modes are killed by the annihilator. This does not rescue
nonlinear Birkhoff weights or stationary-phase assertions.

## 3. Retained all-time arithmetic result

[BGS-FM-012](../mathematics/frozen_periodic_point_annihilator.md) proves
$$
 (S^m-I)^T\mathbb Z^2=
 \begin{cases}2x_m\mathbb Z^2,&m\text{ odd},\\
 2y_m\mathbb Z\times4y_m\mathbb Z,&m\text{ even},\end{cases}
 \quad (1+\sqrt2)^m=x_m+y_m\sqrt2.
$$
The shortest infinity-norm vectors are $2,4,14,24,82,140$ for $m=1,\ldots,6$,
and at least 14 for every $m\ge3$. The physical symbol has bandwidth 9
and averages $-1/10,-1/20,0$ at $m=1,2,\ge3$ respectively. This is a
modest exact extension of existing Pell arithmetic, not a priority claim.

## 4. Two-point data cannot supply the missing higher moments

Take two simple nine-dimensional unitary spectra with phases $X/101$ and
$Y/101$, where
$$
 X=\{0,1,4,10,11,14,22,23,26\},\qquad
 Y=\{0,1,4,12,13,16,22,23,26\}.
$$
They are $A+B$ and $A+(22-B)$ with $A=\{0,1,4\}$ and $B=\{0,10,22\}$;
all sums are distinct. Their Fourier sums factor, so $|p_m(X)|^2=|p_m(Y)|^2$
for every integer $m$, and their entire pair-Abel functions agree for all $s$.
But the number of distinct anchored triples with offsets $(6,18)$ modulo 101
is one for $X$ (anchor 4) and zero for $Y$.
This finite counterexample refutes the purported universal *reconstruction*
from pair data. It is not a counterexample to CUE for the frozen model.
Newton identities use the complex traces, not only their squared moduli.

For phases in cycles, $p_n=\sum_j e^{2\pi in\theta_j}$ and offsets
$x_j-x_l$ with $x_j=N\theta_j$, the positive-power triple numerator is
$$
 B(a,b)=p_a p_b\overline{p_{a+b}}.
$$
It must be reconstructed with $e^{-2\pi i(as_1+bs_2)/N}$, or conjugated
before using a positive inverse exponential. The uploaded `bispec.py` uses
two positive signs and therefore reconstructs the simultaneous reflection.
For $N=3$, $\theta=(0,.1,.35)$, Gaussian width $.08$, offsets $(.3,1.05)$,
and Fourier cutoff 80, real-space reconstruction is $8.296652747923948$;
the submitted sign gives $0.007333911684443$. Correcting the sign recovers
$8.296652747923947$. The upload's smoothed broad-tolerance test misses this.

Moreover, its all-index triples are not factorial correlations. Inclusion
and exclusion yields the distinct-index numerator
$$
 B^{\ne}(a,b)=B(a,b)-|p_{a+b}|^2-|p_a|^2-|p_b|^2+2N.             \tag{1}
$$
The three pair-identification events give the three subtractions, and
their common intersection gives $+2N$. This is the $k=3$ specialization
of the repository's pre-existing partition-Mobius bridge. The corrected
regression checks (1) against enumeration, including zero frequencies.

## 5. Corrected finite controls

**Phase.** The upload already records the Gauss phase
$\operatorname{Tr}M_N=1,i,-1,-i$ for $N=1,3,5,7\pmod8$.
Its T10 raw error nevertheless omits it. At $N=8005$ the measured raw
error is $2.1999022621$, versus $160/N\approx.01999$.
The phase-normalized error $|\operatorname{Tr}(A_NM_N)/\operatorname{Tr}M_N+1.1|$
is $.01930850265$. These are floating diagnostics, not a certified
uniform constant or a Heisenberg-time estimate. Fitting a continuous phase
to the very trace being compared, as `gap_test.py` does, only compares
magnitudes and cannot test a predicted complex phase.

**Taylor expansion.** For any finite Hermitian $A$, unitary $M$, real
$\lambda$, and positive integer $m$, let $p_m(\lambda)=\operatorname{Tr}(e^{i\lambda A}M)^m$.
Product differentiation and trace cyclicity give
$$
 p'_m(0)=im\operatorname{Tr}(AM^m),
$$
$$
 p''_m(0)=-m\operatorname{Tr}(A^2M^m)
 -2\sum_{d=1}^{m-1}(m-d)\operatorname{Tr}(AM^dAM^{m-d}).         \tag{2}
$$
Each $k$th product derivative is bounded in norm by
$(m\|A\|)^k$, by the multinomial theorem and unitarity at real parameter.
Taylor's integral remainder therefore proves
$$
 \left|p_m(\lambda)-\sum_{j=0}^K\frac{\lambda^j}{j!}p_m^{(j)}(0)\right|
 \le \frac{N(m\|A\||\lambda|)^{K+1}}{(K+1)!}.                 \tag{3}
$$
This supplies the missing general dimension factor. For each fixed $N,m$
the Taylor series is entire. An increasing number of terms may be needed
when $m|\lambda|$ grows; low-order breakdown alone proves no impossibility
of resummation and no finite Borel radius.

**Abel cutoff.** With $r=e^{-2s/N}$ and phases in cycles, exact geometric
summation gives
$$
 L_N(s)=\frac1{2N^2}\sum_{j,k}
 \frac{1-r^2}{1-2r\cos(2\pi(\theta_j-\theta_k))+r^2}-\frac12.   \tag{4}
$$
The discarded tail after $M$ is nonnegative and at most
$r^{M+1}/(1-r)$, since $|p_m|\le N$. The identity spectrum attains this
universal bound. The factor $1/2$ and subtraction in (4) must not be omitted.

Recomputing the actual proxy $N=1001,\tau_{\rm eff}=.05$:

| $s$ | Uploaded $8N$ sum, reproduced | Infinite sum from (4) | Discarded tail |
|---|---:|---:|---:|
| $.5$ | $.633090539674313$ | $.633423004725076$ | $.000332465050763$ |
| $1$ | $.215974432465551$ | $.215974488212308$ | $5.57468\cdot10^{-8}$ |
| $2$ | $.060442355120553$ | $.060442355120557$ | about $4\cdot10^{-15}$ |

The first tail disproves the stated $<10^{-6}$ accuracy. At $s=.5$,
the relative error from the infinite-$N$ CUE benchmark is about $.206\%$,
not evidence for the claimed fitted rate. The last row is at floating
roundoff and is not a certified tail value. None of this proxy computation
tests the fixed $\tau=10^{-80}$ asymptotic law.

## 6. Source and execution boundaries

The original `verify_all.py` ran to **52 PASS, 0 FAIL** after installing
SymPy 1.14.0 and mpmath 1.3.0 in the scratch audit environment. Its
[stdout, with trailing spaces normalized](../evidence/20260927/cue_original_suite.log) is preserved.
The suite only reads the stored N=1001 trend numbers; this audit independently
recomputed the N=1001 proxy spectrum. The original script does not exit with
a nonzero status when its `FAIL` list is nonempty. Its success is therefore
read from the log, not inferred from the process exit code alone.

The maintained, assertion-based check is
[cue_upload_audit.py](../computations/verification/cue_upload_audit.py).
Reproduction:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 computations/verification/cue_upload_audit.py --proxy --output build/cue-upload-audit.json

[Executed output](../evidence/20260927/cue_upload_audit.json) records exact
lattice checks for $1\le m\le100$, membership in the frequency box
$[-9,9]^2$, independent brute enumeration at $m=1,2,3$, rational symbol
averages, the two counterexamples, six finite Taylor cases, conventions
at the listed dimensions, and the separately labelled proxy. Integer and
rational tests are exact; complex128 diagnostics carry no interval certificate.

The source-dependent Dolgopyat/KMM/FIO implications were **not verified
in the exact required form** and are not dependencies of the retained lemma.
The [publisher record for Naud](https://ems.press/journals/jst/articles/15810)
identifies *On the rate of mixing of circle extensions of Anosov maps*,
J. Spectr. Theory 9 (2019), 791--824, DOI 10.4171/JST/263, as a study using
anisotropic Hilbert spaces. The pinned arXiv v1 PDF could not be retrieved
through the browser in this pass. Uploaded excerpts do not authenticate a
theorem asserting the claimed universal high-frequency gap closing.
No external theorem or literature priority was added on that basis.

**Remaining gap:** a fixed-coupling estimate for signed joint traces at
Heisenberg times, of every required order, together with the maintained
normalization and symmetry hypotheses. BGS-TRACE-005 and BGS-BGS-001 remain
open. The next useful check on an orbit proposal is agreement with the
physical symbol and independently fixed trace phase before estimating its
long-time remainder.
