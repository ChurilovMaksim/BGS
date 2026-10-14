# Independent audit: global fresh-phase feedback flatness

**Normalized claim.** For every fixed `C0>=1`, `kappa>0`, and every deterministic unitary initial matrix satisfying `max |S_Nij|^2<=C0/N` and `|| |S_N|^2-J_N ||op<=1/100`, uniform retained-port elimination with fresh independent uniform circle phases obeys all four bounds (F1), at every retained size from `N` down to `m=ceil(log(2N)^(4+kappa))`, with unconditional failure probability at most (F15), and hence `O_(C0,kappa)(log(2N)^(-1-kappa))`.

**Primary verdict: proved as written.** I reconstructed the mathematical chain independently from the two frozen candidates and the raw maintained proofs. I found no failed inequality, future-event conditioning, circular assumption of actual future flatness, loss of simultaneous first crossings, or missing diagonal pair. The Green constants require the explicit argument in section 4 below: at the new cutoff `delta<=1/16`, the old threshold `||M||<=1/11` gives `||G^c||<=12/11` and `||G'||<=12/5<3`. Merely copying the old `||G^c||<=3/2` bound while changing the cutoff would not suffice. The stronger bound follows directly from the frozen candidate's actual stopping rule; no modification of that input is used in this verdict.

This is an analytic internal audit, with separately bounded finite controls. It is neither external refereeing nor formal certification. The result concerns the auxiliary random feedback trajectory. It does not identify a deterministic initial microscopic eigenphase law, prove signed TRACE-005, or solve BGS.

## 1. Input binding and audit scope

Repository: `/workspace/scratch/06745ba532e4/BGS`.

The repository HEAD was exactly `53d60cbb4b51d64b3ff82d396ab74e21f704f3a9` at the beginning and end of this audit; `git status --short` was empty. The repository was read only. Audit artifacts were written solely to the requested `research_session` directory. No other agent was spawned.

| Input | SHA-256 |
|---|---|
| `global_feedback_flatness_candidate_20261013.md` | `1264e43e74652b814fef953def70eb64702e287eb06e2dd3d7d0f86ee41b2d1c` |
| `two_step_stopped_concentration_candidate_20261013.md` | `47e365b06fa460e6d503b771b9b336403ee9a6e918e81d4a17b6c6be9a60aec7` |
| `BGS/AGENTS.md` | `17b10ee329a8785ba52778b00aee31b64a5ab8ecf7053fa73b5359a20b94418a` |
| `BGS/SOURCE_OF_TRUTH.md` | `63a6cd2263c8790a431981f7bdaa8cb46eb5188aad33e65f6a387b58fbbbcaaa` |
| `mathematics/schur_censoring_gap_20261011.md` | `1e544af51d0707ccd820ca636fc035b838831ad9fa537da573e42f7366cec02f` |
| `mathematics/two_step_restoring_drift_20261012.md` | `c546a0b32e9fc1bdd1aa1ec4c80a5decc975613461e8c81a319e53aa16d86046` |
| `mathematics/green_compression_gap_20261013.md` | `fb134739b13587648ac8e820e170717343b589b4f085c6ceb74f599a39663748` |
| `mathematics/two_step_increment_variance_20261013.md` | `8780af8cf4eafc8e6b45de206faca38d7783e50308e3c7e821ffec876b049c24` |

The claim/status hierarchy in AGENTS, SOURCE_OF_TRUTH, repository conventions, RESEARCH, the claim ledger, claims registry, results and open-question surfaces was consulted. The maintained TRACE-073/075/077/078 statuses do not strengthen this new candidate. Their raw proofs, rather than their review verdicts, supplied the indicated internal inputs. The separate existing assessment of the two-step concentration candidate was not read or used. The mathbox proof-audit skill and relevant general-logic, computation, and source obligations were applied. No `.mathbox` ledger was found.

The exact conclusion is asymptotic in `N`, with fixed constants and an eventual threshold depending on `C0,kappa`. It includes diagonal ordered pairs. Norms are ordinary unnormalized operator/Schatten norms. All matrices use the same original surviving labels; `J_u=11*/u`. A missing new Green inverse is included as an exit and then excluded deterministically before any possible first crossing.

For the candidate's named actual-family application, `mathematics/position_chain_mixing.md` states `limsup_(odd N)||P_N-J_N||op<=10^-64`, which supplies the eventual `1/100` initial bound; its WKB display also states `max P_N=O(1/N)`. Its SHA-256 is `3a589f988defb569d12f075add16dda669c9409dabd4a81f59c4d0b5d5e44b09`. This is a hypothesis match to the named maintained FM-021/WKB inputs, not a fresh audit of their full parametrix chain or an effective startup estimate.

## 2. Dependency graph and obligation matrix

The nonprobabilistic leaves are unitary feedback, bistochasticity, circle Fourier moments, row/column Parseval, Cauchy--Schwarz, and the centered Green compression/resolvent identities. The probabilistic leaves are the internally reconstructed Schatten quadratic smoothness estimate, its elementary martingale iteration and Doob estimate, and the scalar Taylor-series Bernstein proof in the companion candidate. There is no load-bearing unverified external theorem in this flatness audit.

The complete implication graph is:

1. Initial entry bound and singular norm give initial row/column energies, initial two-step bound, and `||M_N||<=1/99`.
2. Exact feedback and Parseval give row/column mean, raw second moment, and pointwise range.
3. One predictable joint stop imposes old entry, Green, energy, and two-step caps. These are old stopped-state bounds, not assumptions about an un-stopped future trajectory.
4. Centered compression plus the adapted fixed-`N` Green martingale excludes a Green first exit with exception (F12).
5. Scalar energy concentration excludes an energy first exit with exception (F13).
6. Old energy and Green caps bound the complete three-step forcing; the reconstructed all-pair two-step drift/variance then excludes a two-step first exit with exception (F14).
7. Old two-step control bounds the exact amplitude bracket; amplitude concentration excludes an entry first exit with exception (F15a).
8. The ordinary union of these unconditional exceptions excludes every possible first joint exit, including simultaneous exits; the parameter estimates give the stated failure rate.

This contains a bootstrap of stopped old-state bounds, not a logical cycle. Each proposed first exit is tested using a transition whose old state obeys all caps, and each concentration event was proved for that same stopped process without conditioning on any other eventual good event.

| Obligation | Result | Evidence |
|---|---|---|
| Quantifiers, deterministic initial law, fixed parameters | passed | Candidate section 1; no ensemble assumption introduced |
| Exact feedback and phase moments | passed | Direct expansion and geometric Fourier sums |
| Nonnormal row/column forcing estimate | passed | `row(R^2)=row(R)R`, `R=P-J` |
| Fourth-power energy mean (F3)--(F6) | passed | Reconstruction in section 3 |
| Fourth-power raw second moment/range (F7)--(F10) | passed | Six coefficient sums, including omitted diagonal coefficient |
| Changed Green threshold/constants | passed | Explicit `12/11`, `6/11`, `12/5` argument below |
| Green martingale and future random projections | passed | Increments embedded first; final compression only in a pathwise norm bound |
| Diagonal extension of two-step drift and second moment | passed | General coefficient expansion and one-element frozen endpoint set |
| Endpoint removal and virtual scalar continuations | passed | Removing transition included in the old uniform-port mean; later recurrence deterministic |
| Scalar Bernstein and deterministic weights | passed | Companion (S13)--(S14) reconstructed directly |
| All-depth/all-pair concentration without startup | passed | Initial scaled values `<=C0`; barriers have fixed positive margins |
| Amplitude bracket, real/imaginary union and constants | passed | Reconstruction in section 6 |
| Full simultaneous first crossings | passed | Every component uses the same full crossing transition |
| Asymptotics | passed | Powers and constants recomputed in section 7 |
| Effective threshold, growing-order/edge/microscopic law/BGS | out of scope | Not asserted by the candidate |
| Finite controls as a universal proof | out of scope | Explicit finite arithmetic/coverage boundary in section 8 |

## 3. Independent reconstruction of the energy estimates

Let `R=P-J_v`, let `E_i=sum_j P_ij^2`, and reserve `A_i=sum_j P_ij(P^2)_ij` for the positive forcing scalar. Since `PJ=JP=J`,

`A_i=1/v+<row_i R,row_i R^2> <=1/v+rho(E_i-1/v)`.

This uses `row_i R^2=(row_i R)R`; symmetry and normality are unnecessary. The transposed unitary has exactly the transposed feedback rule, so the column argument has the same domain and constants.

For a surviving row coordinate, `P'=x+q alpha+conj(q alpha)+|q|^2 b`, with `|alpha|^2=xb`. Its square has a `2xb` term from the original intensity times the quadratic update and another `2xb` term from the two conjugate coherent updates. This gives the `4xb/d` coefficient in (F3). The two conjugate cubic terms give `4 Re(conj(a) alpha b)/d^2`. The constant Fourier coefficients are `Eq=Eq^2=0`, `E|q|^2=1/d`, `E(q|q|^2)=conj(a)/d^2`, and `E|q|^4=(1+|a|^2)/d^3`.

For the frozen row-removal convention the coordinate base decrement is exactly `-E_i+P_ii^2`. It is not a decrement averaged conditional on survival. Extending only the nonnegative majorants to all ports gives the positive quadratic sum `<=4A_i/(1-delta)`. The cubic sum satisfies

`sum |a alpha b| <=delta sum_e P_ie^(3/2) sqrt(B_ie) <=delta sqrt(E_i A_i)`,

where `B_ie=sum_j P_ij P_ej` and `sum_e P_ie B_ie=A_i`. The first step factors `sqrt(P_ee P_ej)<=delta` and then uses `sum_j P_ej=1`; the second is Cauchy--Schwarz with factors `P_ie` and `sqrt(P_ie B_ie)`. AM--GM supplies the candidate's half-sum. The quartic sum is at most `delta(1+delta)E_i/(1-delta)^3`. Therefore the functions `c,d` in (F5) are correct.

At `delta=1/16`, exact arithmetic gives `c=752/3375`, `d=992/225`, and `c+d/10=448/675<2/3`. Substituting the forcing bound gives (F6). The remaining constant forcing can safely be bounded by `5/v^2`; `P_ii^2/v<=delta^2/v`.

For the exact expansion (F7), the row coefficients are respectively `2 sum x alpha`, `4 sum xb`, `sum alpha^2`, `2 sum alpha b`, `sum b^2`. The coefficient `2` in the first definition is required and is present. The full Parseval linear coefficient has squared port sum at most `4 delta^2 E_i`. Deleting the `j=e` coefficient `2 S_ee P_ie^2` and applying `|a-b|^2<=2|a|^2+2|b|^2` yields `8(1+delta)delta^2 E_i<=10delta^2 E_i` in the used range.

The other coefficient sums follow from `B_ie<=delta`, `P_ie B_ie<=delta^2`, and its port sum `A_i`. Weighted Cauchy for the cubic coefficient gives `|D_e|^2<=4P_ie^3 E_e B_ie<=4delta^3 P_ie B_ie`. The quartic coefficient obeys `F_e<=delta P_ie^2`. The resulting six-group squared bound is exactly

`6delta^2[(161+256delta^2)E_i+(320+1024delta)A_i]`.

At `delta<=1/4` its two constants are at most `1062` and `3456`, both below `3500`. Division by the original `v`, with the actual frozen port increment zero, proves (F9). The displayed coefficient bounds in (F8) are used in the range `delta<=1/4`; that restriction is needed for the rounded linear-coefficient constant `10` and is satisfied throughout this theorem.

Pointwise Cauchy gives `|A_e|<=2delta sqrt(E_i)`, `B_e<=4delta^2`, `|C_e|<=delta^2`, `|D_e|<=2delta^(5/2)`, and `F_e<=delta^3`. With `|q|<=2`, the non-linear part contributes `(25+32sqrt(delta)+16delta)delta^2<=34delta^2` at `delta<=1/16`. This proves (F10).

For `Y_v=vE_i`, the normalization identity is `DeltaY=(v-1)DeltaE-E_i`, including a removing transition frozen at the old unscaled value. The exact drift from (F6) is stronger than the selected coefficient `-Y_v/v`; weakening it as in the candidate gives `F_R=5+D^2/m`. The second moment and twice the pointwise range give exactly `V_R/v^2` and `16D sqrt(L)/sqrt(v)+68D^2/v`. After deactivation the stated affine recurrence has zero centered noise and the same drift inequality with equality. Telescoping gives initial weight `u/N`, deterministic positive weights at most one, and total variance `<=V_R/u`. The proposed energy barrier follows because `max(C0,F_R)+1<L` eventually.

## 4. Green compression and the changed threshold

On the constant-orthogonal space `M=(I-P+J)^(-1)-I=(P-J)(I-P+J)^(-1)`. The initial singular norm gives `||M_N||<=1/99`. At any active old state, the classical single-port complement exists since `1-P_ee>=15/16`. Centered compression gives `||M^c||<=1/11`, so

`||G^c||<=1+1/11=12/11`.

The fresh quantum noise is conditionally centered after the chosen port is revealed, has both stochastic sums zero, and obeys `||Xi||<=8delta<=1/2`. Consequently

`||G^c Xi||<=6/11<1`,

and the first new inverse exists with

`||G'||<= (12/11)/(1-6/11)=12/5<3`.

This remains valid at the full first crossing. Relaxing the linear bound to `(3/2)^2*8delta=18delta` and the remainder bound to `(3/2)^2*64delta^2*3=432delta^2` is therefore safe. The sentence that the smaller threshold is below `1/2` alone would not verify these numbers at the changed entry cutoff; the above stronger estimate supplies the required check from the actual hypotheses.

For `G'=G^c+G^cXiG^c+G^cXiG^cXiG'`, the noncommuting factor order is correct. The old joint stop mask is predictable. Conditional centering holds first over the fresh phase given the port and then over the uniform port. Padding each resulting operator on the retained original coordinates produces ordinary fixed-`N` martingale differences. Random future projections are absent from the increments. Nested zero-sum projections telescope pathwise, and only afterward give `||Q_u Z_u Q_u||<=||Z_u||`.

The quadratic Schatten smoothness input follows by differentiating the even trace power, applying trace Hölder to each second-derivative word, and dropping the nonpositive squared first-derivative term. Hermitian dilation cancels its scaling factor. Conditional iteration gives `E||Z_m||_p^2<=324N^(2/p)(p-1)D^2/m`. The scalar norm is a nonnegative submartingale; Doob's factor four yields (F12). One elementary derivation of that factor is to integrate the level-crossing estimate, obtaining `E(max A)^2<=2E[A_terminal max A]`, then use Cauchy--Schwarz. All moments here are finite from the bounded increments.

The remainder is `<=432D^2/m`. Since `1/11-1/99-1/40=221/3960>0`, its eventual smallness excludes a first Green exit even when another cap exits on the same transition. No future joint-admissibility event is conditioned on.

## 5. All-pair two-step concentration and the companion proof

I reconstructed the companion (S1)--(S14) rather than using its assessment. With `x=P_ik`, `y=P_kj`, `alpha=S_ie S_ek conj(S_ik)`, `beta=S_ke S_ej conj(S_kj)`, `b=P_ie P_ek`, and `d=P_ke P_ej`, multiplying the two updated intensities gives the six TRACE-078 coefficients. This formula still holds when `i=j`, including `k=i`, when some factors coincide. No independence of those factors is assumed.

For `i=j`, the base port sum is `-K_ii+P_ii^2`, so the same `2delta P_ii` upper forcing is safe. The coherent path swap is controlled by the two full nonnegative three-step sums even though the truncated domain need not be swap invariant. All cubic and quartic bounds remain subsums of the same full sums. Thus (S1) is valid on the diagonal.

In the second-moment proof, the full linear coefficient has squared port sum `<=4delta^2K_ij`; its omitted coefficient is still `2S_ee P_ie P_ej`, including the diagonal. Parseval in rows and columns then yields the same rounded `10delta^2K_ij`. The remaining bounds use the full nonnegative sums, `K_ij<=delta`, and `sum_e P_ej K_ie=sum_e P_ie K_ej=(P^3)_ij`. None requires distinct labels. Removing one endpoint port on the diagonal instead of two only decreases the relevant nonnegative port sum. Averaging continues to divide by all `v` ports. This proves (S2) for every ordered pair.

Before substituting `K_ij<=delta`, the pointwise expansion has coefficients `(8+16sqrt(delta))delta sqrt(K_ij)` and `(9+32sqrt(delta)+16delta)delta^2`. These are bounded by `12delta sqrt(K_ij)+18delta^2` at `delta<=1/16`, exactly as used by (F14).

Old joint energy and Green caps give the stronger forcing

`|(P^3-J)_ij|<=rho sqrt[(E_i-1/v)(E^col_j-1/v)]<=g(L-1)/v`.

Hence the complete three-step entry is `<=C/v` at every active old size, including early sizes; no burn-in is used. For `Y_v=vK_ij`, (S1) gives the coefficient `-(3/2-1/(2v))Y_v/v<=-(4/3)Y_v/v` for `v>=3`. The forcing is `F_K=5C+2D^2/m`. Raw second moment and pointwise range give the stated `V_K` and `c_K` after using old `Y_v<=T`.

For endpoint removal, the old unscaled `K` is frozen for that transition, producing `DeltaY=-K`; that case remains inside the old uniform-port conditional expectation. At a global crossing a surviving pair takes the full new `K`. After either kind of deactivation the artificial affine recurrence is deterministic given the past. The resulting nonnegative drift slack is predictable. Its positive deterministic integrating factors allow the claimed upper comparison, with weights at most one. There is no survival-conditioned averaging or future-dependent transform.

The Taylor-series proof of (S13) is valid since `k!>=2*3^(k-2)` for `k>=2`, and conditional centering removes the linear term. At `lambda=eta/(sigma^2+c eta/3)`, `lambda c<3` and exponential iteration gives (S14). Applying it for each fixed size and pair, then taking the ordinary `N^3` union, proves (F14). The barrier has a strict eventual margin because `beta_K->15C/4` and `T=C0+4C+3>max(C0,15C/4)+1`.

## 6. Amplitudes, endpoints and the common first exit

For each original pair define a virtual unscaled amplitude that receives the true feedback increment `q S_ie S_ej` when active and surviving, and zero on the removing transition or after deactivation. This is equivalent to the candidate's scaled `W` freeze/continuation. In particular it is not an entry of an absent later matrix.

Conditional on the old history its increment has mean zero. Uniform port averaging, with endpoint cases included as zero, gives second modulus moment

`<=K_ij/[v(1-delta)]<=T/[v^2(1-delta)]`.

For each fixed target size `u`, multiplying these increments by the deterministic `sqrt(u)` gives a chronological martingale. The active old-state mask is predictable. The total real or imaginary conditional variance is at most `16T/15`, since `u sum_(v>u) v^-2<=1`. Every increment is bounded by `2D sqrt(u)/v<=2D/sqrt(u)`. The initial amplitude is at most `sqrt(C0)` in the scaled comparison. No future endpoint-survival event is conditioned on.

If `|W_u|>sqrt(D)`, the triangle inequality gives martingale modulus `>t=sqrt(D)-sqrt(C0)`. One of the four signed real/imaginary components is then `>t/sqrt(2)`. Bernstein therefore gives exactly exponent `-t^2/[4(sigma^2+c_A(m)t/(3sqrt(2)))]`; its four signs and at most `N^3` pair/size choices produce (F15a).

All four exceptional events were defined for the same jointly stopped old process. On their complement, suppose a first joint exit occurred at size `u`. The Green, energy, and two-step estimates bound their complete new crossing values strictly below their caps. The amplitude estimate bounds every retained new entry by its cap. Endpoint-removed virtual values are not used to evaluate actual new matrices. At least one actual cap must have failed, contradicting these simultaneous conclusions. This also treats a multiple crossing. Consequently no exit can occur down to `m`, and all required denominators/inverses exist throughout the good trajectory.

## 7. Exceptional constants and asymptotics

For fixed parameters, `D=32T ell=O(ell)` and `m=ceil ell^(4+kappa)` eventually satisfy `m<N`, `m>=16D`, the initial caps, and all margin conditions. Also `N^(2/p)<=e` for `p=2ceil ell`. Thus

`E_G=O(ell^3/m)=O(ell^(-1-kappa))`.

Both scalar variance terms at the cutoff are `O(ell^(-2-kappa))`, whereas their centered range terms are `O(ell^(-1-kappa/2))`. Their negative exponents have magnitude at least a positive constant times `ell^(1+kappa/2)`, which dominates each polynomial-in-`N` union factor. Hence `E_R,E_K` are smaller than every fixed negative power of `N` eventually. This use requires the stated strict `kappa>0`.

For amplitudes, `c_A(m)t=O(ell^(-1/2-kappa/2))`, `t^2=D(1+o(1))`, and

`D/(4sigma^2)=32T ell/[4(16T/15)]=(15/2)ell`.

After the `4N^3` union, `E_A=N^(-9/2+o(1))`. The sum of exceptions in (F15) therefore proves the normalized claim with the stated order. The eventual threshold is not claimed effective for the maintained fixed-coupling odd-`N` family.

## 8. Finite checks actually run

Independent code: `research_session/global_feedback_flatness_independent_checks_20261013.py`.

Output: `research_session/global_feedback_flatness_independent_checks_20261013.json`.

Command:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 research_session/global_feedback_flatness_independent_checks_20261013.py
```

The program imports no repository verifier or prior assessment. Assertions were enabled.

Exact `fractions.Fraction` controls use the 64-dimensional normalized Walsh unitary, with nonzero deleted diagonals, rows `0,13`, ordered pairs `(0,0),(0,13),(13,13)`, all applicable retained-port choices, and phases `+1,-1`. They checked 252 exact row expansions and 376 exact pair expansions, 628 total, together with the row coefficient squared sums, drift arithmetic, raw port-square bounds, and the displayed rational constants. The diagonal pairs are included explicitly.

Complex128 controls use a phase-decorated Fourier unitary and a reproducible complex row/column rotation of it, seed `20261013`, dimension 64, including transposes. The second intensity matrix is nonnormal, with `delta=0.030792344470811982` and `rho=0.06563381453739835`; it is an old-state one-step fixture with `rho<=1/10`, not a fixture claiming the theorem's smaller initial gap. Selected rows are `0,13,46`, selected pairs `(0,0),(0,13),(13,13),(13,46)`, all applicable ports, three port-dependent phase choices, and 1024-point circle quadrature for the mean. The maximum row expansion discrepancy was `1.2034644114589099e-17`; the maximum phase-mean quadrature discrepancy was `4.553649124439119e-18`. The largest sampled raw-second-moment/bound ratio was below `0.001817`.

These are finite algebra and floating controls. The phase grids and unitary fixtures are not exhaustive. Quadrature is not a certified circle integral. The check does not implement or numerically establish the asymptotic trajectory probability, eventual threshold, all-depth bootstrap, or clock/microscopic law. Those conclusions rest on the analytic reconstruction above. No full repository build, Lean run, or C++ run was performed for this scratch audit.

| Audit artifact | SHA-256 |
|---|---|
| `global_feedback_flatness_independent_checks_20261013.py` | `c107c417faa44b0d605227e63abbf67ac507766ddc2de01038dba6a63f6f6bcd` |
| `global_feedback_flatness_independent_checks_20261013.json` | `f0e53281e9094eace6209ab48ad229a18df73ad8332739b468ea63fd0f8ce8b3` |

## 9. Separately requested clock consequence

**Scope of this additional check:** process and hypothesis matching only. The maintained all-fixed-order equality theorem is a named internal input, not re-audited here in full. This consequence is separate from the flatness verdict above.

| Named input | SHA-256 |
|---|---|
| `mathematics/conditional_clock_universality_20261011.md` | `8517456f3c4b7b5e6243d6f644b705ea80e4267e92b6e0ab157db0bc7c1d08dc` |
| `mathematics/full_depth_clock_measure_20261011.md` | `d7d13458f1c5a7a31ed3632bb6e54668dca3b85610ea0f48b28e84dbd5f0e3e2` |
| `mathematics/delay_bootstrap_20261011.md` | `fdf990b240f70e4433e6b8a0e1f424718cbbc5f08b60d326e1fdbe931b527027` |
| `mathematics/all_moment_delay_bootstrap_20261011.md` | `18b82c616d2eba73f08e55cb80d01775029db7bbd7d14dfa2fdd495db933c2ac` |

Take the same deterministic initial `S_N` and start the matrix inner-function process with `F_N(z)=zS_N`. At `z=1` its scattering update is precisely `S'=S_AA+q S_Ae S_eA`, so it agrees pathwise with this candidate under the same ports and revealed phases. Differentiation gives `T_N=S_N^*F_N'(1)=I`; outgoing `Q_N=I` follows. The old revealed phases are retained as constants in subsequent feedback functions. Each port is eliminated once, so the fresh-phase generation can equivalently be represented by independent uniform phases assigned to original labels and revealed at their removal. Conditionally uniform retained-port draws are likewise an independent uniform original coordinate permutation. The unrevealed original phases do not enter the current feedback state. This matches the conditional clock theorem's process.

Set `K=K0=32T` and `kappa_clock=3+kappa`, both fixed. Then its cutoff is exactly

`ceil ell^(1+kappa_clock)=ceil ell^(4+kappa)=m`.

The flatness result gives `P(A_m^c)=O(ell^(-1-kappa))->0` for its exact entry premise `A_m`. The named fixed-order theorem gives `P(A_m intersect Bad_(L,N))->0` for every fixed integer `L`. An ordinary union, `P(Bad_(L,N))<=P(A_m^c)+P(A_m intersect Bad_(L,N))`, yields unconditional convergence in probability for all its displayed normalized clock diagonal, off-diagonal, and mixed entries, uniformly over `u>=m`. There is no conditioning of phase averages on `A_m` and no inverse-probability cost.

Its section 5 together with the named full-depth reference proposition therefore yields the unconditional uniform empirical weak clock law with reference `mu_(u/N)`, and at `u=m` the `x=0` density with endpoints `3+-2sqrt(2)`. This is a weak clock law, not a microscopic scattering eigenphase law. Its full-depth atom/rank assertion retains the exact boundary in the named reference source.

This deduction does not establish a cutoff `ceil ell^(1+kappa_clock)` for any smaller `kappa_clock<=3`, growing moment orders, edge statistics, unrestricted expectations on rare failure events, the deterministic initial microscopic spectral law, or BGS. The conclusion is accepted as a corollary using the indicated maintained internal theorem, rather than being represented as a fresh independent re-audit of all TRACE-060 induction or its external background.

## 10. Separately requested reversal consequence

This is another process/hypothesis check using TRACE-073 (C9) as a named internal input. It does not add a reversal hypothesis to the abstract flatness theorem or the clock corollary. Assume additionally, for the particular initial family under consideration, that `rho_(R,N)=||R(S_N)||op->0`, where `R(S)_ij=S_ij conj(S_ji)`.

The candidate's entry event is exactly (C9)'s `A_m` with `K=K0`, and its uniform retained-port choice satisfies (C9)'s more general permitted adapted-port rule. Its phase law is the same fresh independent uniform law. Put `p=2ceil ell`; then `N^(1/p)<=sqrt(e)`. For any fixed `g_R>0`, eventually `N^(1/p)rho_(R,N)<g_R/2`, so (C9) gives

`P(A_m intersect {max_(u>=m)||R_u||op>=g_R}) <=256 N^(2/p)(p-1)K0^2 ell^2/(m g_R^2)=O_(K0,g_R)(ell^(-1-kappa))`.

Adding `P(A_m^c)=O_(C0,kappa)(ell^(-1-kappa))` by an ordinary union proves `max_(u>=m)||R_u||op->0` in probability. No phase average is conditioned on future flatness. The input family need not have an effective startup threshold.

The maintained odd-dimensional fixed-coupling FM-022 source defines its Hermitian matrix as `Q_xy=U_xy conj(U_yx)` and states `||Q_N||op->0`. Thus its `Q_N` is precisely this initial reversal matrix `R(S_N)` when `S_N=U_N`. This is a notation/process match and a named use of FM-022, not a new audit of its parametrix or discrete norm estimates. Its source `mathematics/reversed_path_decay.md` has SHA-256 `c8fea232fdc36fed8d0c8ce9975025050179fca1f3d67e6ddf4d5fb4515ded47`. Complete symmetry classification, an actual microscopic eigenphase reference, and BGS remain outside this consequence.

## 11. Remaining gap and next check

There is no remaining mathematical implication missing from the stated abstract flatness theorem within this reconstruction. The strongest safe statement is exactly (F1)--(F15) for the specified random trajectory and fixed deterministic initial hypotheses. The separately checked clock corollary is valid on the same `ell^(4+kappa)` cutoff with its named internal inputs. The additional reversal consequence is valid only when its separately stated initial reversal-norm assumption is supplied.

For integration, the cheapest useful follow-up is a transfer check of the final maintained statement/proof against the frozen candidates, explicitly retaining the `12/11` Green argument, diagonal endpoint convention, artificial continuations, full crossing state, and ordinary exceptional-event union. Updating scientific status or applying initial hypotheses to the actual fixed-coupling family requires that separate authorized integration step. No such repository changes were made here.
