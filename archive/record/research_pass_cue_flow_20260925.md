# Audit of the 25 September CUE and coboundary continuations

**Review type:** author self-review of the exact statements, external
dependency, and finite computations. The candidate BGS endpoint is
unchanged: all-order local statistics of the explicitly fixed
odd-dimensional propagator require model-specific signed joint traces
at times of order $N$. This record does not claim independent
refereeing or global priority.

## Claims, dependency closure, and verdicts

| Claim | Dependencies | Verdict | Missing implication for BGS |
|---|---|---|---|
| BGS-CUE-001 | Published Ben Arous--Bourgade 2013 Theorem 1.1 for Haar CUE; internally proved determinantal tail estimate | **Project deduction, conditional on the checked external theorem**; exact finite mean and infinite variance proved directly | No determinant-process law, microscopic repulsion, or comparable tail bound for the fixed deterministic map |
| BGS-FLOW-001 | Elementary finite matrix identities, pre-existing project normal-form lemma for attribution | **Finite-dimensional project proof; conditional asymptotic transfer explicitly separated** | Quantitative adjoint Birkhoff decay and commutator hierarchy for the maintained family |
| BGS-FLOW-002 | Existing project eigenphase derivative formula and Gaussian matrix covariance | **Exact finite-dimensional calculation** | Excludes only the stated first-order-in-noise coboundary mechanism, not general stochastic comparison |

The first candidate manuscript note had an editorial error in its
four-point variance identity: a comma appeared where the
integration differential should be. The maintained equation
in the CUE proof has the correct $d\mu^4$.
The note also compressed a genuine source nuance: the published
marked Poisson theorem assumes position arcs inside $(0,2\pi)$.
The maintained proof now gives a seam-excision argument before
integrating out the mark. Neither correction changes the constants
or the conclusion.

The second-order three-exponential estimate already appeared as
Lemma 3 in the earlier Pell coboundary proof. It is explicitly
credited there; no duplicate-priority claim was promoted here.
The fourth CUE trace cumulant computed during exploration is
also present in the smooth pair-statistics literature and is
treated as a verification benchmark, not as a new theorem.

## Adversarial checks of the CUE proof

1. **Ordered/unordered pair factor:** each rare neighboring
   gap contributes twice to the ordered energy. The external
   intensity of $N^{4/3}$ times the *unfolded-in-radians*
   gap is $x^2dx/(24\pi)$. Hence the jump map is
   $x\mapsto 2/x^p$, giving Lévy density
   $2^{3/p}y^{-1-3/p}dy/(24\pi p)$.
2. **Mean and tail constants:** the exact two-point expansion is
   $N^2(N^2-1)\delta^2/12+O(N^6\delta^4)$.
   In particular $\mathbb EF_{N,2}=N(N^2-1)/6$;
   the centered close-pair expectation at scale
   $b=RN^{-4/3}$ tends to $R/(12\pi)$.
   Fischer's inequality controls four distinct indices;
   the one-point Schur complement controls three.
   The resulting normalized variance of the centered
   far-pair sum is at most
   $\pi^3/(96R)+N^{-1/3}/9$.
3. **Small gaps and wrap-around:** the normalized expected
   energy below $\varepsilon N^{-4/3}$ is at most
   $\pi\varepsilon/48$. A nonneighboring close pair
   requires a triple in an arc of width $RN^{-4/3}$,
   whose expected count is $O(R^6/N)$.
   To transfer the published theorem from interior arcs
   to the full circle, first omit a seam arc; the small-pair
   two-point expectation in an arc of length $a$ is
   $O(aR^3)$, uniformly at fixed $R$.
4. **Heavy tail:** finite CUE dimension has local
   collision density proportional to $\delta^2$.
   The $p$-energy has finite mean for $p<3$, but
   infinite variance for $p\ge3/2$. It is incorrect
   to assume the small-gap Poisson sum itself lies in
   $L^2$; only compensated increments *above*
   any fixed positive gap cutoff do.
5. **Deterministic scope:** moving a single eigenvalue
   by $O(N^{-1})$ can preserve weak local
   point-process limits with a random origin while
   producing $N^{-3}F_{N,2}\ge N^3/(2\pi^2)$.
   This does not claim preservation of all unbounded
   factorial moments or perturbative realization
   within the fixed quantization.

The p-range $3/2<p<3$ is required for the tail
$R^{3-2p}\to0$ and the lower-cutoff expectation
$\varepsilon^{3-p}\to0$. The endpoint cases have
not been promoted.

## Adversarial checks of the flow claim

The second-order normal form was recomputed from the derivative
$W'W^*=-\int_0^t\operatorname{Ad}_{e^{-itG}e^{iu(G-B)}}
[G,B]\,du$, not by assuming the exponentials commute.
The $T$-step averaged diagonal of $H=iN[G,B]$
is bounded by the normalized Hilbert--Schmidt
norm of the Birkhoff sum; telescoping gives the
$(T-1)\|H\|^2t^4/(16\pi N)$ term.
The positive and negative time directions and degenerate
eigenphase crossings are included in the statement.

For the sharpness control $N=2m^2$ with odd $m$,
$t=cN^{1/4}$ and $G=N^{-1/2}P$,
the shift from a $2\times2$ block tends to
$c^2/\sqrt2$, equal to the leading bound;
the remaining errors vanish. This example is a
clock with an imposed coboundary, not the fixed map.
For Gaussian $G$, the first phase derivative is
identically zero; only the regular sine curvature
survives in the averaged second-order operator.
There is no second-order phase Hessian. The general
cotangent Dyson generator cannot be imported.
An elementary nonergodic shear calculation in the
maintained note independently checks that a mean-zero
classical bracket need not have vanishing orbit average;
it is not used as an assumption about the fixed Anosov map.

## Executed verification and its scope

The maintained scripts are
[cue_singular_energy.py](../computations/verification/cue_singular_energy.py)
and [coboundary_flow.py](../computations/verification/coboundary_flow.py).
Run from the repository root with the installed Python requirements,
and a single BLAS thread if desired:

    OPENBLAS_NUM_THREADS=1 python3 computations/verification/cue_singular_energy.py
    OPENBLAS_NUM_THREADS=1 python3 computations/verification/coboundary_flow.py

The CUE script checks two-point mean quadratures at
$N=2,3,7,20$; three $N=2$ tail-variance
anchors; the Lévy constant by quadrature; and the
known fourth-cumulant formula by exact fractions for
all $1\le m,n\le7$, $1\le N\le14$.
The flow script checks the finite inequality in
24 deterministic dense cases, the scalar sharpness
sequence through $N=2(511)^2$, and complete
Gaussian Hermitian bases in dimensions 3, 4 and 7.
Both scripts passed in this integration pass. These
runs test normalizations and implementation only.
They cannot establish the asymptotic theorem or
the hypothesis needed for the original frozen family.

A separate exploratory Haar experiment from the initial
note (seed 20260925) drew 3000, 1800 and 800
QR-distributed unitary matrices at $N=16,32,64$.
It can be reproduced with
OPENBLAS_NUM_THREADS=1 python3 computations/verification/cue_singular_energy.py --sample.
At $t=5$ the corresponding empirical characteristic
functions were $0.785240-0.237826i$,
$0.769191-0.266489i$, and
$0.758923-0.268430i$. The limiting expression
is $0.661572-0.241819i$: these finite dimensions
have material bias. The experiment is a cautionary
diagnostic, not convergence evidence.

## Source and attribution boundary

The [exact-source note](../literature/cue_singular_energy_sources.md)
checks the published author's PDF (Theorem 1.1,
pp. 2650--2651), including positional arcs and
the $24\pi$ normalization. Aguirre--Soshnikov--Sumpter
arXiv:1912.07110v3 covers smooth pair tests and
trace covariance, not this inverse-square
singular substitution. A limited query and
comparison found no identical energy theorem,
but priority and publication novelty are **unverified**.

The fixed-map pair Abel target and all-order
joint-trace comparison remain **OPEN**.
