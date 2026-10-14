# Independent audit of simultaneous stopped two-step concentration

**Normalized claim and primary verdict: proved as written.** Under the
candidate's unitary, uniform-port, fresh-uniform-phase and two-barrier
starting hypotheses, its finite bound (S7) controls every surviving ordered
pair, including diagonal pairs, at every reached depth through the full
first global crossing. Combining that bound with the maintained
TRACE-077 prefix theorem gives its simultaneous `9/u` corollary on the
reached interval `m <= u <= d`, through the first entry crossing. This is
an analytic project proof of a stopped-prefix subsidiary statement. It is
not a proof of early entry survival, all-time entry flatness, a deterministic
microscopic law, TRACE-005 or BGS.

The verdict was obtained by reconstructing the scalar process and its
conditional estimates; the candidate's proposed conclusion was not used
as evidence. This is an independent internal review, not an external
referee certificate or a formalization.

## 1. Pinned target and authority

- Repository: `/workspace/scratch/06745ba532e4/BGS`.
- Observed clean base HEAD: `53d60cbb4b51d64b3ff82d396ab74e21f704f3a9`.
- Exact audited candidate:
  `/workspace/scratch/06745ba532e4/research_session/two_step_stopped_concentration_candidate_20261013.md`.
- Candidate SHA256:
  `47e365b06fa460e6d503b771b9b336403ee9a6e918e81d4a17b6c6be9a60aec7`.
- Review date: 13 October 2026.
- No repository files, claim statuses or source conventions were edited.

The applicable `AGENTS.md`, `SOURCE_OF_TRUTH.md`, repository conventions,
research brief, results index, open obligations, current ledger entries and
machine-readable entries were read. There is no `.mathbox/` ledger in this
checkout. The current ledger is the scientific-status authority. It treats
TRACE-075, TRACE-077 and TRACE-078 as project proofs with independent internal
reconstruction, and still leaves accumulated concentration and early entry
survival open at this base. The audit does not silently promote the candidate
into that ledger.

The three raw authoritative proofs were read, rather than relying on their
dashboard status:

| Source | SHA256 |
|---|---|
| `mathematics/two_step_restoring_drift_20261012.md` (TRACE-075) | `c546a0b32e9fc1bdd1aa1ec4c80a5decc975613461e8c81a319e53aa16d86046` |
| `mathematics/green_compression_gap_20261013.md` (TRACE-077) | `fb134739b13587648ac8e820e170717343b589b4f085c6ceb74f599a39663748` |
| `mathematics/two_step_increment_variance_20261013.md` (TRACE-078) | `8780af8cf4eafc8e6b45de206faca38d7783e50308e3c7e821ffec876b049c24` |
| `record/claim_ledger.md` | `ac8eaa7c86f84706fe1d310aa54796314d87c0716142b3831db8143652d0f97a` |
| `record/claims.json` | `399264987681a9c9775e439011e961969d98d408614fd60d4e0991d7ba7d791e` |

Prior logs were searched. In particular, the earlier TRACE-075 averaging
correction places the base subtraction inside the survivor-port sum. The
candidate respects that corrected convention. The static unistochastic
obstruction and the earlier insufficient entry-bracket route are not used
as dynamic theorems.

## 2. Claim card and dependency graph

The finite theorem quantifies over integers `b>m>=3`, constants `D,C>0`
with `m>=16D`, and any deterministic `S_b in U(b)` satisfying
`delta_b<=D/b` and `max(P_b^3)<=C/b`. It chooses each port uniformly from
all currently retained labels and then samples an independent uniform
circle phase. It stops globally after the first full new state violating
either barrier, and considers only actual surviving entries through that
state. For

\[
a=4/3,\quad F=5C+2D^2/m,\quad \beta=F/a,\quad
V=2600D^2(D+C),\quad R=64D^{3/2},
\]

the event that any such entry has

\[
u(P_u^2)_{ij}>\beta+D\prod_{v=u+1}^{b}(1-a/v)+\eta
\]

has unconditional probability at most

\[
b^3\exp\left[-\frac{\eta^2}
 {2\{V/m+R\eta/(3\sqrt m)\}}\right].
\]

Ordered original labels provide a fixed set of `b^2` scalar objects.
Diagonal pairs have one removing endpoint port, distinct pairs have two.
All matrices and scalars are finite dimensional; the relevant field is
complex for the unitary matrices and real for their intensities and scalar
martingales. No limits, infinite completions, or spectral-law identifications
enter the finite theorem.

The implications are:

1. Exact Schur feedback, phase moments, bistochasticity and path-swap Cauchy
   imply the one-step mean (S1); the diagonal case is separately reconstructed
   below. This is internal finite algebra from TRACE-075.
2. Exact complete increment expansion and unitary Parseval imply the raw
   second moment (S2); the diagonal case is separately reconstructed below.
   This is internal finite algebra from TRACE-078, not a dependency on its
   concentration conclusion, which does not exist at the base.
3. Pointwise coefficient bounds give (S3), without phase averaging.
4. A predictable active mask, endpoint freezing, and deterministic scalar
   continuation give the drift, variance and range of scalar noise.
5. Positive deterministic integrating factors and the explicitly derived
   conditional exponential estimate give the fixed-depth tail.
6. A finite union over ordered labels and depths gives (S7).
7. The maintained TRACE-077 stopped Green theorem supplies a high-probability
   three-step barrier before entry exit; combining events after proving the
   scalar bound gives the asymptotic corollary.
8. FM-021 and initial WKB flatness are used only for the named eventual
   initial conditions of the maintained map. They supply neither survival
   nor deterministic microscopic identification.

The finite concentration proof has no load-bearing external concentration
theorem. Its Bernstein/Freedman-type inequality is derived in the candidate
and is independently derived below. TRACE-077 is an inherited internal
theorem input to the corollary; it uses only the indicated parts of
TRACE-073, not the latter's conditional all-time conclusion. No circular
dependency was found.

## 3. Obligation matrix

| Obligation | Status | Decisive reason |
|---|---|---|
| Exact input and hypotheses | passed | Pinned file and clean base; no conventions changed |
| Diagonal mean extension | passed | One excluded port; base loss `-K_ii+P_ii^2`; other terms are subsums |
| Diagonal raw second moment | passed | Parseval and all six sums are valid at `j=i`; same omitted term |
| Complete increment range | passed | All six groups in (V2), including cubic and quartic terms, are bounded |
| Uniform denominator | passed | Always `v`; endpoint increments are zero, not omitted by conditioning |
| Conditional scaled drift/variance | passed | Old state controls `Y_v`; fresh port and phase remain unconditioned |
| Endpoint removal | passed | Frozen removing transition occurs once, then scalar deactivation |
| Full first crossing | passed | Its full update is included; old state is still admissible |
| Artificial continuation | passed | Deterministic recurrence; centered increment zero afterward |
| Integrating factors | passed | Strictly positive deterministic coefficients at all used sizes |
| Conditional exponential estimate | passed | Taylor-series majorization and a variance-compensated supermartingale |
| All pairs and depths | passed | At most `b^2` fixed ordered pairs and `b` deterministic final depths |
| Green event combination | passed | Startup measurable from the past; future good event unioned afterward |
| `9/u` asymptotic constant/rate | passed | `beta=15/2+o(1)`, transient `o(1)`, failure exponent superlogarithmic |
| Universal proof from finite controls | out of scope | Finite checks support algebra only |
| Probability of reaching the range | out of scope | No survival estimate appears |
| Post-crossing matrices and BGS | out of scope | Neither conclusion is asserted or derived |

## 4. Diagonal and complete one-step reconstruction

Write `K=P^2`, `delta=max P`. Bistochasticity gives `K_ij<=delta` for
every pair, since `sum_k P_kj=1`.

### 4.1 Mean

For any pair let `E={i,j}` as a set. The frozen law gives the exact
coordinate average

\[
v\,\mathbb E\Delta K_{ij}
=\sum_{e\notin E}\left(\sum_{k\ne e}
 \mathbb E_w[P'_{ik}P'_{kj}]-K_{ij}\right).
\]

Thus the loss from the old product is
`-sum_(e notin E)P_ie P_ej`. At `i=j` it is exactly

\[
-K_{ii}+P_{ii}^2\le-K_{ii}+2\delta P_{ii}.
\]

The coherent phase term pairs
`T_ek=S_ie S_ek S_kj` with `T_ke`. Even when the truncated domain is not
swap invariant, each of its two squared-amplitude sums is a subsum of the
full nonnegative `(P^3)_ij` path sum. Consequently its modulus is at most
`(P^3)_ij/(1-delta)`. This remains true when `j=i`.

The other nonnegative quadratic sums are bounded by `2(P^3)_ij/(1-delta)`.
The two nonzero-deleted-diagonal cubic terms total at most
`2delta[K_ij+(P^3)_ij]/(1-delta)^2`. The quartic contribution is at most
`delta(1+delta)K_ij/(1-delta)^3`. The same row and column stochastic sums
apply on the diagonal. Combining them gives the same `c(delta),d(delta)`
as TRACE-075, with `c(1/16)=752/3375<1/2` and
`d(1/16)=992/225<5`. Hence (S1) holds for all pairs.

### 4.2 Raw second moment

Retain the exact six-group expansion (V2) from TRACE-078. No step in its
row/column Parseval argument needs `i!=j`. In particular, the full linear
coefficient has the two Parseval bounds `delta^2 K_ij`; their sum has
squared-sum bound `4delta^2K_ij`. Removing `k=e` subtracts exactly
`2S_ee P_ie P_ej`, also when `j=i`. Its squared-sum bound is
`4delta^3K_ij`, yielding `sum_e|A_e|^2<=10delta^2K_ij` for `delta<=1/4`.

The remaining sums are

\[
\begin{aligned}
\sum r_e^2&\le\delta^2K_{ij},\\
\sum B_e^2&\le6\delta^2(P^3)_{ij}+12\delta^2K_{ij},\\
\sum |C_e|^2&\le\delta^2K_{ij},\\
\sum |D_e|^2&\le4\delta^3(P^3)_{ij},\\
\sum F_e^2&\le\delta^4K_{ij}.
\end{aligned}
\]

For example, the coherent quadratic and `C_e` bounds both use
`r_e (sum_k P_ek P_ke)(sum_k P_ik P_kj)<=r_e delta K_ij`.
The cubic bound uses `sum_e P_ej K_ie=(P^3)_ij` and its reversed
row/column counterpart. None requires distinct endpoints. Extending
coefficients algebraically to all ports is used only for nonnegative sum
bounds; actual endpoint increments remain zero.

Since `|q|<=2`, (V2) gives

\[
|\Delta_e|\le r_e+4|A_e|+4|B_e|+8|C_e|+16|D_e|+16F_e.
\]

Six-group Cauchy and the displayed sums give
`sum_(e notin E)Delta_e^2<=2598delta^2[K_ij+(P^3)_ij]`.
Uniform selection divides this by `v`, even on the diagonal. Rounding
2598 upward to 2600 proves (S2).

### 4.3 Pointwise range

At a surviving port, direct Cauchy gives

\[
\begin{aligned}
|A_e|&\le2\delta\sqrt{K_{ij}},\\
|B_e|&\le2\delta^2+2\delta^{3/2}\sqrt{K_{ij}},\\
|C_e|&\le\delta^{3/2}\sqrt{K_{ij}},\\
|D_e|&\le2\delta^{5/2},\qquad F_e\le\delta^3,
\qquad r_e\le\delta^2.
\end{aligned}
\]

For the first linear component, use
`sqrt(P_ie) sqrt(sum_k P_kj^2 P_ik) sqrt(sum_k P_ek)`;
the last two factors are at most `sqrt(delta K_ij)` and 1. The other
component is the column counterpart. For each cubic component,
`|D1_e|^2<=delta P_ie P_ej^2 K_ie<=delta^5`, and similarly for `D2_e`.
These controls apply unchanged to the diagonal.

Substitution into the complete expansion yields

\[
|\Delta K_{ij}|\le\delta^{3/2}
 (8+25\sqrt\delta+32\delta+16\delta^{3/2})
\le(61/2)\delta^{3/2}<32\delta^{3/2}
\]

for `delta<=1/4`; the candidate needs only `delta<=1/16`. At frozen ports
the increment is zero. No higher feedback group or port case was dropped.

## 5. Stopped scalar process and conditional estimates

Use the chronological past before selecting the next port as the scalar
conditioning sigma-algebra. It contains the current full matrix, retained
labels, and active masks. Uniform averaging is performed over the fresh
port as well as the fresh phase. The intermediate sigma-algebra in
TRACE-077, which reveals the chosen port before its phase, is compatible
with this coarser scalar conditioning.

For a fixed original pair, while it is active let `Y_v=vK_ij`. At an
endpoint-removing transition set `Y_(v-1)=(v-1)K_ij` and then deactivate.
At a global crossing with endpoints retained use the actual new `K_ij`
and then deactivate. If both happen, endpoint freezing is the scalar
convention and that pair is no longer a surviving matrix entry. After
deactivation use exactly

\[
Y_{v-1}=(1-a/v)Y_v+F/v.
\]

This scalar is not an assertion about any later intensity matrix. The
old-state active mask is predictable. In particular, the first crossing
is not preemptively masked or clipped.

Before an active transition, `delta<=D/v<=1/16`, so `Y_v<=D`; the
Schur denominator is nonzero since `|S_ee|<=1/4`. All first-crossing
updates exist. Using `Delta Y=(v-1)Delta K-K_ij`, (S1) implies

\[
\mathbb E\Delta Y\le
-\left(\frac32-\frac1{2v}\right)\frac{Y_v}{v}
+\frac{5C}{v}+2\delta^2
\le-\frac{aY_v}{v}+\frac Fv.
\]

The second inequality uses `v>=3`, `Y_v>=0`, and
`2delta^2<=2D^2/v^2<=2D^2/(mv)`. On a deactivated transition it holds
with equality regardless of the continuation scalar's size.

For active transitions, (S2) gives

\[
\operatorname{Var}(\Delta Y\mid\mathcal F)
\le\frac{(v-1)^2}{v}\,2600\delta^2
 \{K_{ij}+(P^3)_{ij}\}
\le2600\delta^2(Y_v+C)\le V/v^2.
\]

The fixed old subtraction `-K_ij` cancels in conditional centering.
Since the raw `Delta K` lies in `[-32delta^(3/2),32delta^(3/2)]`, its
centered version has magnitude at most `64delta^(3/2)`. Therefore

\[
\xi_v=Y_{v-1}-\mathbb E(Y_{v-1}\mid\mathcal F),\quad
|\xi_v|\le R/\sqrt v,
\quad \mathbb E(\xi_v^2\mid\mathcal F)\le V/v^2.
\]

Endpoint-removal randomness is included in both inequalities. After
deactivation `xi_v=0`. No assumption on the new crossing state's barriers
was used. The adapted slack
`epsilon_v=(1-a/v)Y_v+F/v-E(Y_(v-1)|past)` is predictable and nonnegative.
Thus the recursion with noise and slack is exact.

## 6. Integrating factors and elementary exponential bound

Fix a deterministic final size `u`. All coefficients `1-a/v` used by
the recursion are strictly positive. Unrolling it gives

\[
Y_u\le\beta+r_{b,u}(Y_b-\beta)
 +\sum_{v=u+1}^{b}w_{v,u}\xi_v,\qquad
w_{v,u}=\prod_{r=u+1}^{v-1}(1-a/r)\in(0,1].
\]

The slack terms enter with nonnegative coefficients and so may be
dropped. The forcing identity follows from `F=a beta`. Since
`Y_b<=D`, the deterministic part is at most `beta+Dr_(b,u)`. Crucially,
the weights depend only on sizes, and each original pair is fixed before
future random deletions. The weighted sum is a real martingale terminal
value in chronological time. Its predictable variance is at most
`V sum_(v=u+1)^b v^-2<=V/u`, and each increment is at most `R/sqrt(u)`.
No future projection or future surviving-label selection occurs within
these martingale increments.

For a centered conditional increment `X` with `|X|<=c`, and
`0<=lambda<3/c`, expand its exponential. Conditional centering removes
the linear term; for `k>=2`,
`|E X^k|<=c^(k-2)E X^2` and `k!>=2*3^(k-2)`. Therefore

\[
\mathbb E(e^{\lambda X}\mid\mathcal F)
\le\exp\left(\frac{\lambda^2\mathbb E(X^2\mid\mathcal F)}
 {2(1-\lambda c/3)}\right).
\]

Subtracting this conditional-variance compensator in the exponent gives
a nonnegative supermartingale of expectation at most 1. A deterministic
upper bound `sigma^2` on the total predictable variance then gives
`E exp(lambda sum X)<=exp(lambda^2 sigma^2/[2(1-lambda c/3)])`.
Markov with `lambda=eta/(sigma^2+c eta/3)` has `lambda c<3` because
`sigma^2>0`, and yields

\[
\mathbb P\{\sum X\ge\eta\}
\le\exp\left[-\frac{\eta^2}{2(\sigma^2+c\eta/3)}\right].
\]

Take `sigma^2=V/u` and `c=R/sqrt(u)`. Union over at most `b^2` original
ordered pairs and `b` final depths, then weaken `u>=m` to `m`. This gives
(S7). The empty weighted sum at `u=b` and the empty product `r_(b,b)=1`
are harmless. Logarithmic product comparison gives

\[
\log r_{b,u}\le-a\sum_{v=u+1}^b1/v
\le-a\log\frac{b+1}{u+1},
\]

which is (S8). The martingale comparison controls a scalar continuation
at every deterministic depth. Whenever an actual surviving entry is
asserted in the theorem, that scalar still equals the actual scaled entry.
This proves the exact stopped-prefix event, including the crossing.

The same proof works conditional on the entire revealed admissible
starting history, because every bound is uniform in the input matrix and
labels, and future port/phase randomness has its prescribed conditional law.

## 7. Green combination without future conditioning

Let `E_G` be the good event furnished by TRACE-077 with
`ell=log(2N)`, `m=ceil(ell^(7+kappa))`, and `b=floor(N/ell^2)`.
Its complement has probability `O_(K0)(ell^-kappa)`. The theorem's
Green decomposition and shrinking compression bound give
`rho_u=O_(C0,K0)(ell^-2)` at all reached old entry-admissible states
`m<=u<=b` on this event. The elementary higher-step bound, valid for
every ordered pair including the diagonal, is

\[
(P_u^3)_{ij}\le1/u+\rho_u(\delta_u-1/u)
\le\{1+\rho_u(K_0\ell-1)\}/u\le2/u
\]

eventually. Its proof is the row/column norm estimate for
`(P-J)^3=(P-J)(P-J)(P-J)`, with both outer squared norms at most
`delta-1/u`. It is used at old admissible states, not at an entry-violating
crossing state.

For complete precision, define the candidate's **revealed admissible
startup event** by

\[
\Gamma_b=\{\text{the entry prefix reaches }b\text{ without an entry exit},
\ \delta_b\le K_0\ell/b,\ \max P_b^3\le2/b\}.
\]

Both starting barriers belong in the word "admissible": conditioning on
entry admissibility alone would not justify applying the finite theorem
on every history. This is a useful explicit definition for later
exposition; it imposes no new restriction on the claimed corollary. On
`E_G`, any entry-admissible reached `b` already satisfies it. If the entry
exit has occurred at or above `b`, there is no reached depth in
`m<=u<=d=floor(b/ell)` for all sufficiently large `N`.

On `Gamma_b`, run the finite theorem with `D=K0 ell,C=2`, starting from
the revealed matrix and labels and adding its `P^3` stop. Conditional
only on that past, its failure probability is at most the same deterministic
`q_N` for every admissible input. Thus the event `E_C` that `Gamma_b`
occurs and the auxiliary stopped estimate fails satisfies

\[
\mathbb P(E_C)
=\mathbb E[1_{\Gamma_b}\mathbb P(E_C\mid\mathcal F_b)]
\le q_N\mathbb P(\Gamma_b)\le q_N.
\]

There is no division by the probability of reaching `b`. On `E_G`, the
additional three-step barrier cannot be the first exit strictly before an
entry exit. A simultaneous exit is included in the full update. Hence on
`E_G` the auxiliary prefix agrees with the entry prefix through its first
crossing, whenever it has been started. The desired corollary's violation
event is contained in `E_G^c union E_C`. This uses a union bound only;
the scalar martingale is never conditioned on the future event `E_G`.

## 8. Asymptotic `9/u` reconstruction

All numerical hypotheses hold eventually for fixed `C0,K0,kappa>0`:
`m>=32K0 ell`, `m>=16D`, `C0<=K0 ell`, and `m<d<b<N`.
For `C=2,D=K0 ell`,

\[
\beta=\frac34(10+2K_0^2\ell^2/m)=15/2+o(1).
\]

Uniformly for `u<=d`,

\[
Dr_{b,u}\le K_0\ell\left(\frac{d+1}{b+1}\right)^{4/3}
=O_{K_0}(\ell^{-1/3})=o(1).
\]

With `eta=1`, the finite threshold is consequently `17/2+o(1)<9`
eventually. The scalar failure bound is at most

\[
q_N=N^3\exp\left[-\frac1{2\{V/m+R/(3\sqrt m)\}}\right],
\]

where `V=2600(K0 ell)^2(K0 ell+2)` and `R=64(K0 ell)^(3/2)`.
The terms in its denominator have sizes

\[
V/m=O_{K_0}(\ell^{-4-\kappa}),\qquad
R/(3\sqrt m)=O_{K_0}(\ell^{-2-\kappa/2}).
\]

Thus its exponent is at least `c_(K0) ell^(2+kappa/2)`, which dominates
`3log N` and any fixed multiple of `log N`. The scalar failure is
superpolynomially small in `N`. The Green failure therefore controls the
combined `O_(C0,K0,kappa)(ell^-kappa)` rate. This proves
`max_(i,j retained)(P_u^2)_ij<=9/u` simultaneously at every reached
`m<=u<=d` through the first entry crossing, including that state when its
depth lies in the interval. No post-crossing state or nonempty-prefix
probability is asserted.

## 9. Separate finite controls and actual commands

Analytic sections 4--8, rather than the following computation, establish
the general theorem. A fresh independent scratch script was written and
executed:

```text
python research_session/two_step_stopped_concentration_independent_checks_20261013.py
```

The script uses Python `Fraction` arithmetic. Its matrix is exactly
`S=R(H_64/8)C`, with rational planar rotations of numerators `(5,12)`
and `(3,4)` and denominators 13 and 5, respectively. An independent
integer Gram calculation checks exact orthogonality. The resulting
intensity maximum is `14161/270400<1/16`.

The checked pairs are `(0,0)`, `(17,17)`, `(0,17)`, and `(31,47)`.
For each pair, all 64 algebraically extended coefficient ports were
checked, with only the actual frozen endpoint ports omitted from the
moment sum. Exact circle moments through bidegree `(4,4)` were calculated
by the interior-pole residue derivative of
`w^(p-1)/[(1-aw)^p(w-a)^q]`, separately from the phase-expanded drift
formula. They verify the exact uniform-phase mean and raw second-moment
bounds for these four inputs, including both diagonals.

At every surviving port, five exact rational unit-circle phases
`1,-1,i,-i,(3+4i)/5` compare the direct Schur product with the entire
six-group expansion and check the pointwise range. There are 1250 exact
port/pair/phase comparisons. All assertions passed. The endpoint
conventions, coefficient squared sums, and numerical endpoint constants
were also checked exactly. These finite controls are not exhaustive over
unitary matrices or phases, and do not test stochastic survival,
first-crossing frequency, asymptotic concentration or BGS.

Artifacts:

- Script:
  `/workspace/scratch/06745ba532e4/research_session/two_step_stopped_concentration_independent_checks_20261013.py`,
  SHA256 `eea97f1ce168dbdc57480da91937e205e425f0268779629657634684ea24007a`.
- Exact receipt:
  `/workspace/scratch/06745ba532e4/research_session/two_step_stopped_concentration_independent_checks_20261013.json`,
  SHA256 `7668e98955b8e65d7aeabaa99b029174cd50afd6c65e765d046b290ff3044cc8`.

Read-only inspection also used `git rev-parse HEAD`, `git status --short`,
`rg` searches over proofs/current claims/prior records, and SHA256 hashing
of the exact input files. No full repository regression, manuscript
build, formal-kernel compilation or external-source theorem verification
was run or claimed by this review. The exponential estimate is proved
directly, so an unread external Freedman source is not a proof leaf.

## 10. Remaining gap and strongest safe statement

No missing implication was found in the candidate's stated stopped theorem
or its asymptotic stopped corollary. The cheapest remaining exposition
improvement is to write `Gamma_b` explicitly with both starting barriers,
as in section 7, while preserving its past measurability.

The strongest safe conclusion is simultaneous two-step control on the
reached stopped range stated above. A different argument is still required
to estimate early entry survival, to control matrices after the first
entry exit, or to identify a deterministic microscopic law. This review
does not turn the subsidiary result into BGS or change the maintained
fixed-coupling, odd-N and ineffective-startup boundaries.
