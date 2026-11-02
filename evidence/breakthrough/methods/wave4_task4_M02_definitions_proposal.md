# Wave 4, task 4 — M02 definitions proposal sheet

## Status — read this first

This is a **proposal, not a claim about main**. Nothing in this sheet is
attributed to the BGS repository, to a theorem in main, or to any
verified result. It was written because wave 3, task 3, established
that the quantity at the centre of M02,

$$g_{\mathrm{ball}}(m) \;=\; D_m \cdot (1 - |\lambda_1(m)|),$$

is **not well-defined from main alone**: main contains three
different objects all plausibly called "the" frozen propagator, no
transfer-operator eigenvalue $\lambda_1$ anywhere, and a maintained
target (CUE, TRACE-005) that is not the ensemble M02's symmetry
discussion leans toward (COE). Until the choices below are frozen by
an owner decision, no resonance numerics may be presented as a test
of the M02 prediction. Running numbers first and fixing definitions
afterwards is exactly how a vacuous or circular test is produced.

Background (all from earlier waves, not re-proved here):

- The three $U$'s in main (wave 3, task 3): **(a)** the fixed frozen
  propagator $U_N = \exp(i\tau N A_N) M_N$ with $\tau = 10^{-80}$
  fixed, $A_N$ the Weyl quantization of the fixed 32-mode symbol
  $f - 1/10$; **(b)** the $\theta$-ensemble $U = \exp(i\eta V_\theta)
  M_N$ with $\eta = O(1)$ a free ensemble parameter, $V_\theta$ a
  random trigonometric polynomial; **(c)** the Lean trace-expansion
  model $\mathrm{kickMat}\cdot\mathrm{catMat}$ (and its
  $\mathrm{tsum}$ version $\mathrm{kickMatInf}$), whose
  identification with (a) enters the bridge only as the hypothesis
  $hTrU$ and is **not** proved in main.
- At $N \sim 100$, (a) has coupling $\tau N \approx 10^{-78}$
  (perturbative regime); (b) and (c) are run at $\eta = O(1)$.
  There is no bridge in main from (b)/(c) numerics to (a).
- $D_m = \det H_m = \mathrm{Tr}\, S^m - 2$ with
  $S = \begin{pmatrix}3 & 4\\ 2 & 3\end{pmatrix}$:
  $D_3 = 196$, $D_4 = 1152$, $D_5 = 6724$, $D_6 = 39200$,
  $D_8 = 1331712$. In main $D_m$ is a periodic-point-type count
  (size of $\mathrm{Fix}_m$), **not** the Hilbert-space dimension:
  the quantum dimension is the independent parameter $N$. M02's
  text treats $D_m$ as "the dimension of the quantum space" and
  sets the Heisenberg time to $n_H \sim D_m$. That identification
  is itself one of the decisions below (D2/D4), not a fact.
- Wave 2, M04/M05, on **models, not the project map**: the Ulam gap
  for a shear-perturbed cat map is stable ($\lvert\lambda_1\rvert
  \approx 0.68$ at the finest partition), but the resonance ansatz
  for the form factor **failed** on the model quantum map —
  deviations $\lvert\delta k\rvert \approx 0.1$–$0.19$ at $N = 400$
  while $\lvert\lambda_1\rvert^{m_0}$ was already $< 10^{-3}$.
  Any new proposal must state what that result does and does not
  kill (see D6), not silently reset the scoreboard.

---

## 1. Which operator, which dynamics — PROPOSAL P1

### 1.1 Primary choice (recommended)

**Classical object:** the one-parameter family of frozen classical
maps

$$F_\kappa = G_\kappa^{-1}, \qquad
  G_\kappa = S \circ \Phi_g^\kappa,$$

where $S$ is the cat map above and $\Phi_g^\kappa$ is the time-$\kappa$
Hamiltonian flow of the fixed symbol $g$ (the 32-mode symbol of the
fixed model; $\ell = 0$ rows real, $\ell = \pm 1$ rows carrying the
symmetry-breaking coefficients). $\kappa$ is a **parameter of the
test family**, not the project constant: the test is run at
$\kappa$ values where the kick is classically $O(1)$ (the regime
of the $\theta$-ensemble and Lean-kick numerics), and the project
value $\kappa_* = \tau/(2\pi) \approx 1.6\cdot 10^{-81}$ is treated
as a **separate, degenerate limit** (see §1.3).

**Quantum object (Tier 1):** the Lean-model propagator with a
diagonal, even kick,

$$U_N = \mathrm{kickMat}(N, \hat g_{\mathrm{even}})
        \cdot \mathrm{catMat}(N), \qquad N\ \text{odd},$$

where $\hat g_{\mathrm{even}}$ is the $\ell = 0$ (diagonal) row of
the fixed symbol only, symmetrised so that
$\hat g_{-k} = \hat g_k$. Reasons for this restriction, stated
plainly:

- Only for a real diagonal kick does main contain an antiunitary
  identity ($\Theta = D K_0$, $\Theta^2 = I$,
  $\Theta U \Theta^{-1} = U^\dagger$) — and even that identity is
  **not** a COE form-factor theorem (see §5).
- Only under $\hat g_{-k} = \hat g_k$ is parity a block symmetry
  of $\mathrm{kickMat}\cdot\mathrm{catMat}$, so that parity
  sectors are well-defined blocks (see §5.3).
- The pure $\mathrm{catMat}$ alone is **excluded** as a test
  object: it is a proved non-generic example (Hecke degeneracies),
  so agreement or disagreement of its spectrum proves nothing
  about the kicked map.

**Quantum object (Tier 2, exploratory only):** the full fixed
propagator (a) with all 32 modes. Tier 2 has **no** justified
desymmetrization and **no** antiunitary in main (see §5), so Tier 2
results are reported as exploration, never as a pass/fail test of
M02, until a symmetry of the full $U_N$ is proved.

**Explicitly not chosen as the primary object:** the
$\theta$-ensemble (b). It is retained only as a **numerical error
control** (averaging over $\theta$ to estimate statistical noise
of a spectral statistic at fixed classical $F$), exactly as M02
§4 recommends for candidate C. An ensemble result must never be
renamed as a result about one frozen map; the concentration step
from ensemble to single map is a separate, named, unproved step.

### 1.2 Why not simply "the frozen map"

Because "the frozen map" currently denotes at least three
non-identified objects with couplings differing by $\sim 80$
orders of magnitude. Any test sheet that writes "$U_m$" without
saying which of (a)/(b)/(c) it means, and at which coupling, is
not a test sheet — it is a label under which incompatible numbers
can be compared. P1 fixes Tier 1 to (c)-diagonal-even, Tier 2 to
(a), and (b) to error control only.

### 1.3 The $\kappa \to \kappa_*$ problem (do not hide it)

At $\kappa_* \approx 1.6\cdot 10^{-81}$ the classical map $F_{\kappa_*}$
is, at every computationally accessible resolution,
indistinguishable from the linear cat map $S$. Its Ruelle
resonances are therefore (to that resolution) those of $S$, and a
test at $\kappa = O(1)$ says nothing, by itself, about
$\kappa_*$. The proposal therefore splits the programme in two,
and an owner must decide which programme a "positive" result is
allowed to claim (D1):

- **Programme T (testable):** M02's mechanism at $O(1)$ kick —
  does the classical gap control form-factor deviations for a
  kicked cat map at all? Wave 2's model result already casts
  doubt on the ansatz in this regime (see D6).
- **Programme P (project):** the $\tau = 10^{-80}$ fixed map —
  where the classical gap is essentially the cat gap, the quantum
  coupling is $10^{-78}$, and the whole question is whether an
  $O(1)$-kick mechanism survives a $10^{-80}$ perturbation. That
  is a different, harder problem, and no $O(1)$ numerics settles
  it.

---

## 2. State space and kernel of the transfer operator — PROPOSAL P2

### 2.1 The operator

The Perron–Frobenius (transfer) operator of a measure-preserving
map $F$ on the torus $\mathbb{T}^2$ is

$$(\mathcal{L}_F f)(x) = f(F^{-1} x), \qquad
  \int_{\mathbb{T}^2} \mathcal{L}_F f = \int_{\mathbb{T}^2} f.$$

$\mathcal{L}_F$ acts on **densities**, not on quantum states.
Its $L^2$ spectrum lies on the unit circle (unitary), so on $L^2$
there is **no gap** and no $\lambda_1$ with
$\lvert\lambda_1\rvert < 1$ to speak of. Ruelle–Pollicott
resonances are eigenvalues of $\mathcal{L}_F$ only after
restriction to an **anisotropic** function space: smooth along
unstable directions, distributional along stable directions.
The choice of that space is part of the definition of
$\lambda_1$, not a technicality to be filled in later.

**Proposed analytic space (primary):** an anisotropic Sobolev
space $H^{s,t}(\mathbb{T}^2)$ with $s > 0$ (regularity in the
unstable direction) and $t < 0$ (allowed distributional order in
the stable direction), $s, t$ fixed at freeze time (proposal
values: $s = 1$, $t = -1$; these numbers are **choices**, not
theorems — see D3). The essential-spectrum radius on such a
space is bounded by roughly
$r_{\mathrm{ess}} \lesssim \max(\Lambda_u^{-s},
\Lambda_s^{\lvert t\rvert})$ where $\Lambda_u > 1$,
$\Lambda_s < 1$ are the extremal expansion/contraction rates of
$F$; $\lambda_1$ is only meaningful if it is **isolated**,
i.e. $\lvert\lambda_1\rvert > r_{\mathrm{ess}}$ with a stated
margin (proposal: $\lvert\lambda_1\rvert - r_{\mathrm{ess}}
> 0.05$; again a choice, D3). If no eigenvalue clears that bar,
$\lambda_1$ is **undefined** for test purposes — the test does
not proceed with a fitted substitute.

**Alternative analytic route (must agree or the test stops):**
resonances as poles of the dynamical zeta function / zeros of
the Fredholm determinant for $F$. If the zeta route and the
anisotropic-space route disagree beyond the stated tolerance,
that disagreement is a finding (the resonance is not robustly
defined for this map), not a discrepancy to be averaged away.

### 2.2 The numerical kernel (Ulam matrix)

For a partition $\mathcal{P}_K$ of $\mathbb{T}^2$ into $K^2$
cells $C_i$ of equal area, the Ulam matrix is the row-stochastic
matrix

$$P^{(K)}_{ij} \;=\;
  \frac{\lvert C_i \cap F^{-1}(C_j)\rvert}{\lvert C_i\rvert}
  \;\approx\;
  \frac{\#\{\text{sample points in } C_i
        \text{ landing in } C_j\}}
       {\#\{\text{sample points in } C_i\}},$$

estimated with a fixed, stated number of sample points per cell
(proposal: $4\times 4$ sub-points per cell, as in wave 2's M04
test; the sampling error must be reported, not absorbed).
$\lambda_1^{(K)}$ denotes the subleading eigenvalue of
$P^{(K)}$ of largest modulus, **after** discarding eigenvalues
attributable to partition artefacts by the stability criterion
of §3. The Ulam matrix is **not** the transfer operator: coarse
graining is an effective noise, and its gap is
regularization-dependent by construction. That is why §3's
stability criterion is load-bearing, and why an Ulam gap quoted
without a refinement sequence is not a resonance.

### 2.3 What is not a transfer operator here

- The quantum propagator $U_N$ itself: unitary, spectrum on the
  unit circle, no gap. Any "gap" extracted from $U_N$ directly
  (e.g. from a truncated or damped $U_N$) is a gap of the
  truncation, and must be named as such.
- A Markov matrix built from a symbolic coding that is not
  proved to be a Markov partition for $F_\kappa$: usable as a
  model, not as the resonance of $F_\kappa$.
- The $\theta$-averaged operator: averaging over kicks changes
  the dynamics (it is a noisy map), and its gap is a gap of the
  noised system (cf. wave 2's DBM-clocks result, which passed
  only for the noised system at $N = 256$).

---

## 3. Regularization and its stability criterion — PROPOSAL P3

Two regularizations are in play, and their **order of limits
must be fixed before any number is computed** (D3):

1. **Ulam refinement** $K \to \infty$ (partition cells shrink).
2. **Diffusion regularization** $\varepsilon \to 0$: replace
   $F$ by $F$ followed by a small diffusion kernel of width
   $\varepsilon$ (e.g. Gaussian noise on the torus), compute
   $\lambda_1(K, \varepsilon)$, and then remove $\varepsilon$.

**Proposed order (primary):** at fixed $\varepsilon > 0$,
refine $K$ until $\lambda_1(K, \varepsilon)$ stabilises; then
halve $\varepsilon$ and repeat; $\lambda_1$ is declared only if
the $\varepsilon$-sequence also stabilises. Reversing the order
($\varepsilon \to 0$ first) collapses back to the unitary $L^2$
operator and destroys the gap; doing only one of the two limits
leaves a regularization parameter inside the "answer".

**Pre-registered stability criterion (proposal values — owner
may tighten, not loosen silently):**

- Refinement: $\lvert\lambda_1^{(2K)} - \lambda_1^{(K)}\rvert
  < 0.01$ for **two** successive doublings of $K$
  (e.g. $K = 50 \to 100 \to 200 \to 400$), with the same
  criterion for $\lambda_2$ if the ansatz uses it.
- Diffusion: $\lvert\lambda_1(\varepsilon/2) -
  \lambda_1(\varepsilon)\rvert < 0.01$ for two successive
  halvings.
- Isolation: $\lvert\lambda_1\rvert - \lvert\lambda_2\rvert
  > 0.05$ and $\lvert\lambda_1\rvert - r_{\mathrm{ess}} > 0.05$
  at the finest $(K, \varepsilon)$ used.
- Eigenvector stability: the (coarse-grained) left/right
  eigenvectors at successive refinements must have overlap
  $> 0.9$ after optimal phase alignment; a jumping eigenvector
  with a stable-looking eigenvalue is a failed criterion, not a
  pass.

**If any criterion fails, the outcome is: "$\lambda_1$ is not
established for $F_\kappa$ at this regularization"** — not
"$\lambda_1 = 0$", not "the model is dead", and not a licence to
pick the $K$ whose value fits the quantum data. The M04 wave-2
Ulam gap ($\approx 0.68$, stable across $K = 50, 100, 200$ for
the shear-perturbed cat) is an example of a gap **passing** this
kind of criterion on a model — which is precisely why the
subsequent failure of the form-factor ansatz on that model is
informative rather than dismissible as "bad classical numerics"
(see D6).

---

## 4. What the index $m$ in $\lambda_1(m)$ means — PROPOSAL P4

This is the point on which M02's formula is most fragile, and
the proposal resolves it by **retiring the notation**
$\lambda_1(m)$ in its primary form. Three readings were
considered; only the first survives as a testable definition.

### 4.1 Primary: $\lambda_1$ is $m$-independent (P4a)

$\lambda_1$ is the leading Ruelle resonance of the **fixed**
classical map $F_\kappa$ of §1.1. It has no index $m$. The
$M02$ quantity is replaced by the standard
Heisenberg-over-ergodic ratio for a quantum map of dimension
$N$:

$$g_{\mathrm{ball}}(N) \;=\; N \cdot (1 - |\lambda_1|)
  \;\approx\; \frac{n_H}{n_{\mathrm{erg}}}, \qquad
  n_H \sim N,\quad
  n_{\mathrm{erg}} \approx \frac{1}{1 - |\lambda_1|}.$$

The test then reads (see §6): compute $\lambda_1$ once
(classical, §2–§3), diagonalise Tier-1 $U_N$ for increasing
$N$, form $k(n) = D^{-1}\lvert\mathrm{Tr}\, U_N^n\rvert^2$
with $D = N$ (the quantum dimension — **not** $D_m$), and
check the ansatz $\delta k(n) \approx \sum_{j\ge1} c_j
\lambda_j^n$ with $c_j = O(1)$ unknown constants, at most
two or three resonances, fitted **once** across all $N$ (not
refitted per $N$). The amplitude of $\delta k$ should shrink
like $1/g_{\mathrm{ball}}(N)$ as $N$ grows at fixed
$\lambda_1$.

### 4.2 Rejected: $m$-scaled operator (P4b) — vacuity proof

Suppose instead $\lambda_1(m)$ is the leading subleading
eigenvalue of an operator whose resolution scales with $m$ —
e.g. an Ulam matrix with $\sim D_m$ cells, or the transfer
operator of the $m$-th iterate $F^m$, or an operator indexed
by $\mathrm{Fix}_m$. In every such variant the gap does **not**
close with $m$:

- Ulam refinement: $\lambda_1(m) \to \lambda_1$ (the true
  resonance) as the partition refines, so
  $1 - \lvert\lambda_1(m)\rvert \to 1 - \lvert\lambda_1\rvert
  = \mathrm{const}$, and
  $g_{\mathrm{ball}}(m) = D_m \cdot \mathrm{const} \sim
  (3 + 2\sqrt2)^m \cdot \mathrm{const} \to \infty$
  exponentially. The criterion "$g_{\mathrm{ball}} \gg 1$"
  is then **automatically satisfied** for large $m$ and
  discriminates nothing.
- $m$-th iterate: resonances of $F^m$ are $\lambda_j^m$, so
  $1 - \lvert\lambda_1\rvert^m \to 1$, and again
  $g_{\mathrm{ball}}(m) \sim D_m \to \infty$.
- The only escape is a gap closing like
  $1 - \lvert\lambda_1(m)\rvert \sim D_m^{-1}$, i.e. a
  **Heisenberg-scale** gap. But a classical resonance gap at
  Heisenberg scale is not a classical output at all — it is
  precisely the quantum-scale input the test is supposed to
  predict. A formula that is non-vacuous only by assuming its
  own conclusion is circular, not a criterion.

**Conclusion:** $g_{\mathrm{ball}}(m)$ as written in M02
cannot simultaneously be (i) a well-defined classical
quantity, (ii) non-trivial as a criterion, and (iii) about
the project map. P4a keeps (i) and (ii) by moving the scaling
from $m$ to $N$; anyone who wants to keep the letter $m$
must exhibit a definition of $\lambda_1(m)$ whose gap closes
like $D_m^{-1}$ **for a classical reason**, and that burden
is on the proposer, not on the test.

### 4.3 Rejected: quantum/truncated $\lambda_1(m)$ (P4c)

A "resonance" extracted from $U_N$, from a damped $U_N$, or
from a finite section of the quantum propagator is not a
Ruelle resonance of $F_\kappa$. It may be an interesting
quantity in its own right (e.g. a decay rate of a noised
quantum map), but using it in $g_{\mathrm{ball}}$ to predict
the spectrum of the **same** $U_N$ is circular: the predictor
and the predicted object coincide.

### 4.4 Consequence for $D_m$

Under P4a, $D_m$ drops out of the test quantity entirely. It
remains relevant elsewhere in the programme (periodic-point
counts, Line-D fibre combinatorics, the $hSep$ problem), but
it is **not** the Heisenberg time of any $U_N$ in Tier 1 or
Tier 2, and no test result may be stated in units of $D_m$
without re-deriving that identification. If a future
Line-D object $U_m$ of dimension $D_m$ is ever defined in
main (a matrix indexed by $\mathrm{Fix}_m$), then §1, §5 and
this section must be rewritten for that object from scratch
— that is decision D2, and it is currently open.

---

## 5. Target ensemble and desymmetrization — PROPOSAL P5

### 5.1 Primary target: CUE

**Pre-registered target: CUE** (Haar $U(N)$ reference, Sine$_2$
local statistics), for both tiers. Reasons:

- The maintained project target for the fixed map is CUE:
  TRACE-005's reference is the exact finite-dimensional Haar
  $U(N)$ (CUE) ensemble with proved implication to Sine$_2$.
  A test that assumes COE for the fixed map would be arguing
  against the project's own maintained target, not within it.
- For the full fixed symbol, wave 3, task 3, found **no**
  quantum antiunitary in main: the symbol is not even under
  $(q,p) \mapsto (-q,-p)$ (the $r(q)\sin 2\pi q/100$ term is
  odd in $q$; $\cos(2\pi p - \alpha) \mapsto \cos(2\pi p +
  \alpha) \neq \cos(2\pi p - \alpha)$ since $\sin\alpha =
  4/5 \neq 0$), and the classical map has no $C^1$ reversor
  for $0 < \lvert\kappa\rvert \le 10^{-12}$ (FM-001 §2), a
  range containing $\kappa_*$.
- The diagonal-kick antiunitary $\Theta = D K_0$ (TRACE-130)
  covers Tier 1 only, and it does **not** imply a COE form
  factor: a symmetric unitary $O^T \Lambda O$ with CUE
  eigenvalues is the standard counterexample, and both
  project notes state twice that the "orthogonal class"
  label is heuristic only. Citing TRACE-127/TRACE-130 as a
  COE form-factor theorem is prohibited by this sheet.

**COE as alternative hypothesis (not as assumption):** for
Tier 1 only, the test also computes the COE reference curve
and reports the fit to both curves, with CUE pre-registered
as the target. The COE curve must be taken from a standard
reference (Mehta or equivalent) and frozen at test-freeze
time; deriving a COE curve ad hoc from the data, or using
the CUE curve $\min(n/N, 1)$ for COE data, invalidates the
comparison. If COE fits Tier-1 data decisively better than
CUE **and** the antiunitary is the only symmetry present,
that is a result about Tier 1 (diagonal kicks), and it still
says nothing about Tier 2 (full fixed symbol) or about the
project target without a separate argument.

**GSE/GOE:** no basis in main for either as a target for
these maps (no Kramers-type antiunitary with $\Theta^2 = -I$
is exhibited, and no real-symmetric representation is
claimed). They are not test targets under this proposal.

### 5.2 Reference curves (freeze before data)

- CUE (primary): $k_{\mathrm{RMT}}(n) = \min(n/N, 1)$ for the
  normalised form factor $k(n) = N^{-1}\lvert\mathrm{Tr}\,
  U_N^n\rvert^2$, $n \ge 1$, after desymmetrization (§5.3)
  and removal of exact degeneracies.
- COE (alternative, Tier 1 only): the standard COE form-factor
  curve from the frozen reference, stated in the test header
  with its normalisation. **Do not** substitute the CUE curve.
- Plateau: $k \to 1$ (CUE normalisation) for $n \gg N$; the
  test window is $1 \le n \lesssim 2N$, covering ramp and
  plateau onset, so that a "ramp-only" fit cannot hide a
  plateau failure.

### 5.3 Desymmetrization (freeze before data)

- **Tier 1 (diagonal even kick):** parity sectors separately,
  never pooled. Parity $R\lvert x\rangle = \lvert -x\rangle$
  commutes with the unkicked quantization and with an even
  diagonal kick; sector dimensions for odd $N$ are
  $(N+1)/2$ ($+1$) and $(N-1)/2$ ($-1$). Each sector's spectrum
  is unfolded/desymmetrized separately and compared with the
  CUE curve at its own dimension. Pooling the two sectors
  reproduces the day-1 trap (a pooled even-kick spectrum
  looks Poisson-like, $\langle r\rangle \approx 0.37$, while
  the sectors separately are RMT-like) and is prohibited.
- **Tier 2 (full fixed symbol):** **no** desymmetrization is
  justified by main. Parity splitting or pooling are both
  unjustified until a symmetry of full $U_N$ is proved, so
  Tier-2 spectra are reported as raw exploration with both
  splittings shown as sensitivity analysis, neither claimed.
- **$\Gamma$/affine desymmetrization is a different thing:**
  the Line-D fibre/affine-orbit structure (wave 3: O$^*$ holds
  in the separation sense at $m = 8$, fails strictly; the
  $B_{\mathrm{sym}}$ for claim 152 needs restatement through
  the affine analogue) concerns a Line-D object indexed by
  $\mathrm{Fix}_m$, not Tier-1/Tier-2 $U_N$. It must not be
  imported as the desymmetrization of $U_N$, and parity
  sectors must not be imported as the desymmetrization of a
  Line-D object. Conflating the two is a category error this
  sheet is written to prevent.
- **Degeneracies:** exact degeneracies (Hecke degeneracies of
  the pure cat map, any degeneracy forced by a proved symmetry)
  are removed before unfolding, and the removal is logged.
  Unexplained near-degeneracies are reported, not silently
  unfolded away.

---

## 6. The test protocol under this proposal

Freeze, in the test header, before any Tier-1 number is
computed: (i) the Tier-1 kick coefficients $\hat g_{\mathrm{even}}$
verbatim; (ii) $F_\kappa$ and the $\kappa$ grid; (iii) the
anisotropic-space parameters $(s, t)$ and the Ulam/diffusion
grids; (iv) the stability tolerances of §3; (v) the CUE curve
and (for Tier 1) the COE curve with reference; (vi) the
desymmetrization of §5.3; (vii) the kill criteria below.
Changing any of (i)–(vii) after seeing data restarts the test
as a new, exploratory test — it does not amend the old one.

Steps:

1. **Classical:** compute $\lambda_1, \lambda_2$ for $F_\kappa$
   by §2–§3. If §3 fails, stop: the M02 test is not runnable
   for this $\kappa$. (This is an outcome, not a delay.)
2. **Quantum:** diagonalise Tier-1 $U_N$ for a geometric
   ladder of $N$ (proposal: $N = 101, 201, 401$ at minimum,
   odd, with parity sectors separated), compute $k(n)$ per
   sector, subtract $k_{\mathrm{RMT}}$.
3. **Comparison:** fit $\delta k(n) \approx \sum_{j=1}^{J}
   c_j \lambda_j^n$ with $J \le 3$, $c_j$ fitted **once**
   across all $N$ and all sectors, $\lvert c_j\rvert$
   required to stay $O(1)$ in the $k$-normalisation
   (proposal bound: $\lvert c_j\rvert \le 5$; exceeding it
   is a failed fit, not a larger model). Report the residual
   structure as a function of $n$, not just a single
   goodness-of-fit number.
4. **Scaling:** check that the amplitude of $\delta k$
   decreases as $1/g_{\mathrm{ball}}(N)$ with
   $g_{\mathrm{ball}}(N) = N(1 - \lvert\lambda_1\rvert)$
   across the $N$-ladder. A fit that works at one $N$ and
   fails at the next is not a pass.

### Pre-registered kill criteria (any one kills the naive ansatz)

- **K1 (not only resonances):** after the best $J \le 3$
  resonance fit, the residual contains structure above noise
  localised at times of short periodic orbits (including
  repetitions) — the Bogomolny–Keating objection.
- **K2 (quantum phase at fixed classical map):** changing
  only the quantum kick phase (or $\theta$) at fixed $F_\kappa$
  changes $\delta k(n)$ by more than the statistical error —
  the classical resonances cannot be the whole story.
- **K3 (no gap):** §3 fails for $F_\kappa$ (no isolated
  $\lambda_1$) — the ballistic model in this form is
  inapplicable, and that inapplicability is itself the
  prediction to report (it predicts non-universality, not
  RMT, for that $\kappa$).
- **K4 (no scaling):** $\delta k$ does not shrink like
  $1/g_{\mathrm{ball}}(N)$ across the $N$-ladder, or
  $\lvert\delta k\rvert$ stays $\gtrsim 0.1$ while
  $\lvert\lambda_1\rvert^n < 10^{-3}$ in the test window
  (the wave-2 model pattern, now as a pre-registered
  criterion rather than a post-hoc observation).
- **K5 (wrong ensemble):** the CUE curve is rejected at
  high significance in **both** parity sectors while COE
  (Tier 1) fits — the target, not just the ansatz, must be
  revised, and no claim about the project (CUE) target
  follows from Tier 1.

A positive result (all criteria passed, scaling confirmed)
licenses **only** the following sentence: "For the Tier-1
diagonal even-kick model at $O(1)$ classical kick, classical
Ruelle resonances predict form-factor deviations as in the
ansatz." It does **not** license any sentence about the
$\tau = 10^{-80}$ fixed map, about the $\theta$-ensemble as
a single map, or about BGS in general. Each of those needs
its own, separately named argument (concentration, $\kappa
\to \kappa_*$ limit, or ensemble-to-single-map step).

---

## 7. Owner decisions — nothing here is silently fixed

| # | Decision | Proposal (this sheet) | Alternatives | If decided otherwise |
|---|----------|------------------------|--------------|----------------------|
| D1 | Kick regime | $O(1)$ classical kick, $\kappa_*$ as separate limit | (a) $\kappa_*$ only; (b) $\theta$-ensemble $\eta = O(1)$ as target | (a) test is degenerate (cat resonances); (b) result is about an ensemble, not a map |
| D2 | Which $U$ | Tier 1: Lean diagonal even kick; Tier 2: full fixed $U_N$ exploratory | Line-D $U_m$ of dimension $D_m$; $\theta$-ensemble $U$ | §§1, 4, 5 must be rewritten for that object; $D_m$ re-enters as dimension |
| D3 | Regularization | Anisotropic $H^{1,-1}$; Ulam $K \to \infty$ then $\varepsilon \to 0$; tolerances $0.01$ / $0.05$ / overlap $0.9$ | Zeta/Fredholm route as primary; different $(s,t)$; reversed limits | Tolerances are choices: tightening is safe, loosening after data is not; reversed limits destroy the gap |
| D4 | Meaning of $m$ | Retire $\lambda_1(m)$; use $\lambda_1$ (fixed) and $g_{\mathrm{ball}}(N)$ | Keep $m$-scaled $\lambda_1(m)$ | Proposer must exhibit a classical reason for a gap $\sim D_m^{-1}$; otherwise §4.2 vacuity applies |
| D5 | Target ensemble | CUE pre-registered; COE as Tier-1 alternative only | COE as target for Tier 1 | Changes $k_{\mathrm{RMT}}$ and the licensed conclusion; says nothing about Tier 2 / project target |
| D6 | Status of wave-2 M04 | M04 pattern pre-registered as K4; model result does **not** by itself kill the project-map ansatz (different map) | Count M04 as a kill of the ansatz outright | If outright kill: the M02 programme stops here and this sheet is archival; if model-only: Tier-1 test proceeds as §6 |
| D7 | Averaging | $\theta$-averaging and energy-window averaging as error control only, widths frozen before data | Window averaging as part of the theory (Andreev et al.) | Prange objection applies: window noise is the same order as the corrections claimed; must be answered, not assumed away |
| D8 | Naming discipline | Positive Tier-1 result licenses only the Tier-1 sentence of §6 | Broader licensing (fixed map / BGS) | Requires the separate concentration and $\kappa \to \kappa_*$ arguments; without them the broader sentence is false advertising |

**Minimum freeze set to start any numerics:** D1, D2, D5
(and D4 if the letter $m$ is to appear anywhere in the test
header). D3's tolerances and D6's interpretation must also be
recorded before data, but they may be tightened later without
invalidating a pass — they may not be loosened to turn a fail
into a pass.

---

## 8. Stop conditions (do not proceed past these)

1. Do not compute a $\lambda_1$ for an operator main does not
   define and compare it with a spectrum.
2. Do not use parity sectors for the full fixed symbol, and do
   not pool the sectors of an even diagonal kick.
3. Do not cite TRACE-127/TRACE-130 as a COE form-factor
   theorem, or the $\Theta = D K_0$ identity for full $U_N$.
4. Do not import $\eta = O(1)$ $\theta$-ensemble numerics as
   evidence about the $\tau = 10^{-80}$ fixed map.
5. Do not quote $g_{\mathrm{ball}}(m)$ with $m$-scaling unless
   D4 has been decided in favour of a stated $m$-scaled
   definition with a classical $D_m^{-1}$ gap mechanism.
6. Do not present an Ulam eigenvalue without its refinement
   sequence and stability verdict (§3).
7. Do not rename a Tier-1, ensemble, or noised-map result as a
   result about the fixed map or about BGS.

---

## 9. What this sheet does not do

- It does not prove, or claim to prove, any resonance, gap,
  form-factor deviation, or ensemble statement.
- It does not fix the definitions it proposes: every numbered
  proposal (P1–P5) is a recommendation awaiting the owner
  decisions of §7. Until D1, D2 and D5 are frozen, the M02
  resonance test remains **not runnable as a test** — and
  that, rather than a set of numbers, is the deliverable of
  this task.
- It does not touch the BGS repository, build Lean, or cite
  any file in main as saying something it does not say. All
  main-references above are summaries of wave 3, task 3's
  connector-based reading, to be re-verified against the
  current HEAD before any test is frozen.
