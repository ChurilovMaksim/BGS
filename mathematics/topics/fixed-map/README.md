# Fixed deterministic map

## Operator resolution and short traces

[TRACE-114 short-trace barrier](../../fixed-map/balanced_rounding_research_20261027.md) and [TRACE-115/116 operator stability and pair transfer](../../trace-bridge/microscopic_unitary_stability_20261027.md) continue the uniform-trace theorem. Exact matrix approximations and general changed-quantizer examples have different scopes; the original pair law remains open.

The [final spectral edition](../../spectral_research/README.md) provides the
complete thematic source corpus. New maintained notes: [coordinate return](../../fixed-map/coordinate_return_quartic.md),
[inserted trace](../../fixed-map/inserted_trace_coboundary.md), [spectral distance](../../fixed-map/spectral_orbit_distance.md),
and [weighted Pell curvature](../../fixed-map/pell_weighted_curvature.md).

The [22 October dependency review](../../../record/spectral_research/trace_closure.md)
closes the inserted-trace and global spectral-distance inputs. The
[finite-grid correction](../../fixed-map/finite_grid_one_step_trace.md),
[classical displacement density](../../fixed-map/displacement_density_trace_bound.md)
and [uniform power-trace theorem](../../fixed-map/fixed_kick_uniform_trace_bound.md)
have separate proofs. Their logarithmic/global conclusions leave the
microscopic signed plateau and higher factorial defects open.

## Reviewed 7 October phase checkpoint

[Current claim card](../../trace-bridge/phase_trace_checkpoint.md) and
[accepted results / next estimates](../../../record/checked_research_checkpoint_20261007.md)
separate uniform charge gap, fixed-word laws, source/Schur reductions,
ordinary-body bounds and actual q=1,theta=0 radial control from the still-open
balanced limit, signed offcharge endpoint and higher factorial comparison.

The exact odd-dimensional frozen propagator uses fixed tau=10^(-80), the corrected ordinary Weyl symbol, and explicit exceptional dimensions. Structural and algebraic results do not themselves control Heisenberg traces.

## Current theorem capsules

- **[Random-phase encounter pairs](../../fixed-map/random_phase_encounter_pairs.md)** — TRACE-143–146: for Haar diagonal phases on \(S=\begin{pmatrix}3&4\\2&3\end{pmatrix}\), the coefficient of \(1/p\) is \(-2m^2\) for each fixed \(m\ge 5\), with the pairs classified as \(2\)-opt, swap and figure-eight. Gnutzmann–Seif 2004 derived \(2\tau-2\tau^2\) diagrammatically for this ensemble, Gnutzmann–Altland 2005 and Pluhař–Weidenmüller 2014 predict the full COE form factor non-rigorously, and Berkolaiko–Keating 1999 did exact all-pairs combinatorics for random-phase star graphs; new here is only the rigorous fixed-\(m\) exact-in-\(p\) result, the complete classification including swaps, and the \(m\le 12\) expansions. TRACE-147 is verification-pending: the computer-assisted expansion deviates from the fixed-\(m\) COE value \(2m^3\) at \(m=5,6,8,9,12\), and an independent referee replay is deposited. TRACE-148 is the open scaling-limit conjecture. The fixed kick is not covered.
- **[Resonant residues (Line E)](../../fixed-map/resonant_residue_lineE.md)** — TRACE-183–196. At N ≡ −4 (mod h_m) the fixed-kick trace of a finitely supported kick is governed by m-independent IFS transfer operators. For the single-cosine kick, the leading eigenvalue of the L-truncated operators is certified, and |W̃rest_m| > m is proved on finite m-ranges; conditionally on a spectral hypothesis, for all large m. For the Line B kick (second referee audit): a 49-state law at N ≡ ∓196 when 3 ∤ m, computer-assisted bounds at m = 11 and 13 only (m = 17 pending), and a conditional failure of Conjecture R. (Later: Conjecture R is refuted as stated by Line H, TRACE-209.)
- **[Lifted transfer operators (Line F)](../../fixed-map/lifted_transfer_lineF.md)** — TRACE-197–202. The vertex/edge lift gives trace-class full-alphabet operators and an exact trace identity; for the single-cosine kick at η = 2, |W̃rest_m| > m is proved for every odd m ≥ 15 (computer-assisted), the conclusion of TRACE-188 on a different space. Conjecture R itself is not addressed.
- **[Resonance classification (Line G)](../../fixed-map/resonance_classification_lineG.md)** — TRACE-203–206. A general partial-trace law for every unit ν (proved, finite alphabet); the dilution identity, the outlier classification and the corrected mean law R′ (pre-registered m = 17 test) are open.
- **[49-state certificate (Line H)](../../fixed-map/lineH_49state_certificate.md)** — TRACE-207–209. For the Line B kick at η = 2 (s = −1), the lifted 49-state operator V_0 has one certified simple eigenvalue with |μ*| ∈ [1.846834, 1.946835], and W̃rest_m(2)/m ≥ 1.4·10⁴ for every odd m ≥ 47 with 3 ∤ m (computer-assisted, refereed). Conjecture R (TRACE-179) as stated is therefore refuted; R_NSW is the separate open TRACE-210. The odd m with 3 ∤ m in 17–43, 3 | m, η ≠ 2 and s = +1 are not covered, and BGS itself is not addressed.
- **[Reduction of Conjecture R′ (Line I)](../../fixed-map/lineI_rprime_reduction.md)** — TRACE-211–220. An exact reduction of R′ (TRACE-206) to (E″), (T″) and the dilation remainder (D), none of which is proved. It uses the dilation-coset L² law with a per-member Gauss-sum formula. Lean covers only the finite coset algebra and the norm counts; the Fourier step and the Gauss-sum formula are paper proofs. For d = 7 there are computer-assisted certificates: the square term is ≤ 0.01 for m ≥ 321 (ρ = (±2,8) only; the (±2,16) level-7 members are not controlled), and the twisted radius is r_tw > 1.262 > √λ/μ₀, so operator radii cannot control the cross term. Also: exact intertwiners, an aliasing identity, and the unbounded prime support of h_m. R′ stays open; R′_A (TRACE-220) is open.
- **[The d = 7 twisted coefficient in frozen R′ (Line J)](../../fixed-map/lineJ_d7_twisted_coefficient.md)** — TRACE-221–233.
  - The exact sector law gives the leading d = 7 coefficient exactly: class 1:3 cancels exactly, and 2:1 and 0:1 survive.
  - Theorem J (computer-assisted) shows that the frozen d = 7, (±2,8) contribution to W′/m is ≥ K_j·1.0184224^m/m with both signs in
    every 6 consecutive members of each class mod 168. The (±2,16) members are negligible for m ≥ 243.
  - Also: the inheritance theorem, prime-level complete sums, and the r(q) lemma.
  - Theorem J3 (TRACE-231) is conditional: R′ is false along m = 3p under the open H♮ (TRACE-232) and H_arg (TRACE-233).
  - Lean covers only the arithmetic cores: the mod-49 period, the n_q counts, the ring identity of the r(q) lemma, and the window
    step and constants.
  - R′ stays open.
- **[Fixed diagonal kick](../../fixed-map/derandomized_fixed_kick.md)** — TRACE-163, 165–173, 175 and 178: the fixed-$m$, fixed-kick derandomized analogue of the random-phase short-time results. The exact Pell-norm trace formula gives $B_m=2m$ for $m\le 8$; the odd-$m$ ramp, Theorem N for eleven certified NSW primes, the parity decomposition, and a directed-rounding decay certificate on $\eta\in[1,81.574]$ are proved. TRACE-173 uses only the directed-rounding constants. TRACE-164, 174 and 176 are conditional. TRACE-177 is numerical-only and is filed as open. TRACE-180–182 are open; TRACE-179 (Conjecture R) is refuted as stated by Line H (TRACE-209). Nothing is proved at $\tau=m/N=O(1)$. This is not progress on BGS-BGS-001 or BGS-TRACE-148. "$B_m\to 2m$" is not claimed.
- **[Band-limited random kicks](../../fixed-map/band_limited_kick_bridge.md)** — TRACE-149–152 and TRACE-154, TRACE-156, TRACE-157 and TRACE-160: for a fixed finite set of random cosine modes, the exact bridge \(E|\operatorname{Tr} U^m|^2=\Psi_m(t_N)\) at every odd \(N\) with \(\gcd(N,D_m)=1\), the \(1/N\) expansion (not uniform in \(\eta\) or \(K\)), the orbit-pair form, the strong-kick limit \(B_m^{\mathrm{sym}}\) under dihedral-class separation, \(B_m^{\mathrm{sym}}<2m\) for every odd \(m\), multiset separation, oddness of \(c_1\), and the full-band transfer of TRACE-146. The bridge and the orbit form are Line B's Theorem 1 per realisation and the Boasman–Keating mechanism, not new. TRACE-153 (instances \(m\le 7\)) is verification-pending. TRACE-158 is conditional and Gaussian-only. TRACE-155, TRACE-159, TRACE-161 and TRACE-162 are open. This does not prove BGS-TRACE-005 or BGS-BGS-001, and it says nothing about eigenvalue statistics beyond the second moment of Tr U^m at fixed m.
- **[Revival closure law](../../fixed-map/revival_closure_law.md)** — TRACE-133–135: twisted closure formula, scalar-return revival bound and minimal-period limit, and half-period parity reduction for the position-diagonal kick (\(\sigma_d=13203/32000\)). TRACE-136 and TRACE-137 are open conjectures. The explicit bound of 134 is non-informative at computable \(N\) (first below \(1\) near \(N\approx10^{191}\) at \(\lambda=1/4\)).
- **[Fixed-time limits](../../fixed-map/hyperbolic_short_time_limit.md)** — TRACE-132: for every hyperbolic matrix, Haar diagonal phases have fixed-time limit \(2m\) when \(m\ge 3\), with the error \(m!(1+m(m-1))/N\). The antiunitary \(\Theta'=DEK_0\) reverses \(DM_N\) for every such matrix. A finite cosine with \(\eta=o(N^{-2/3})\) has limit \(1\) along odd \(N\) coprime to \(\beta(2-u_m)\); along \(N\) divisible by \(7\) (e.g. \(35,77,91,707\)) the time-\(3\) kernel has order at least \(49\), so the limit \(1\) fails when \(\gcd(N,\beta(2-u_m))>1\). Sending \(\eta\to\infty\) first, with frequencies \(1\) through \(m\) present, recovers \(2m\). Row inversion has limit \(m\). A momentum sine is not identified.
- **[Hyperbolic diagonal form factor](../../fixed-map/hyperbolic_diagonal_form_factor.md)** — TRACE-131: for every hyperbolic \(S\in\mathrm{SL}(2,\mathbb Z)\) and odd \(N\) coprime to the upper-right entry, the quantization is unitary and flat, and symmetric exactly when the diagonal entries agree modulo \(N\). The antiunitary \(\Theta'=DEK_0\) reverses the kicked propagator for every such matrix. A finite cosine kick has phase average \(|\ker|+\eta^2 D_2+\rho\). The prime kernel depends on the trace when \(p\) does not divide \(\beta\). At an identity revival the second-order coefficient is \(-m(\sigma-\sigma_0)p^2\). This is not the all-order revival law and not a fixed-time limit.
- **[Momentum-phase unitary value](../../fixed-map/momentum_phase_cue.md)** — TRACE-140/141: Haar position phases and Haar momentum phases give \(\mathbb E\lvert\operatorname{Tr} U^m\rvert^2\to m\) for each fixed \(m\ge 3\), with an explicit error, on odd primes with \(\delta\not\equiv -1\). The moment of order \(2k\) tends to \(k!\,m^k\). TRACE-142 identifies the Gaussian main term \(m(1+e^{-vm})\); the non-injective remainder is not bounded, so the limit is verification-pending. The odd symbol energy is \(9/125000\).
- **[Position-diagonal antiunitary](../../fixed-map/sixteen_phase_symmetry.md)** — TRACE-130: for every real diagonal kick, \(\Theta=DK_0\) satisfies \(\Theta^2=1\) and \(\Theta U\Theta^{-1}=U^\dagger\). The orthogonal-class name is a heuristic and does not exclude a CUE form factor. Each of the rows \(\ell=\pm 1\) has energy \(9/160000\). The momentum sine has symbol energy \(1/2\) and is not a function of position.
- **[Scalar-return orbit sum](../../fixed-map/scalar_return_bessel.md)** — TRACE-129: at \(S^m\equiv I\) the classical orbit sum of a position-diagonal kick has an exact Bessel average. Its degree-two jet is \(\exp(-m\sigma_{\mathrm{diag}}\eta^2)\). The degree-four gap is the quadruple excess of the position orbit. Time one equals \(1+\rho_1\) inside the perturbative window. Each of the rows \(\ell=\pm 1\) has energy \(9/160000\). The identity is not the quantum average.- **[Short-time diagonal-phase limits](../../fixed-map/diagonal_phase_short_time.md)** — TRACE-128: for \(DM_N\) the fixed-time limit is \(2m\) when \(m\ge 3\), with an explicit gap from \(2m P(N,m)/N^m\). Row inversion on an odd prime gives the limit \(m\). Neither window reaches \(m\le N^{\alpha}\).
- **[Diagonal random-phase form factor](../../fixed-map/diagonal_phase_form_factor.md)** — TRACE-127: independent phases at the \(N\) position sites give \(\mathbb E\lvert\operatorname{Tr} U\rvert^2=1\), \(\mathbb E\lvert\operatorname{Tr} U^2\rvert^2=(2N-1)/N\), and \(\mathbb E\lvert\operatorname{Tr} U^m\rvert^2\le m!\). For the cat map at time three the value is \((6N^2-9N+4)/N^2\). It separates from \(\lvert\ker(S^m-I)\rvert\) at times two and three. It is not the sixteen-phase ensemble and not a CUE limit.
- **[Phase-averaged form factor](../../fixed-map/interaction_phase_form_factor.md)** — TRACE-126: the average of \(|\operatorname{Tr} U^m|^2\) over independent phases on the 16 mode pairs equals \(|K_m|+\eta^2 D_2+\rho\), with \(D_2\) a Gauss-sum coefficient. At an odd prime \(p\) the second-order revival term is \(-m(\sigma-\sigma_0(p))p^2\), and \(\sigma_0(p)=0\) for every prime \(p\ge 11\). Parity and position conjugation fail for the kicked propagator when \(0<\lvert\eta\rvert<\pi/B\), except at dimension \(7\), where \(A_7=(9/10)I\). The signed off-diagonal sum and the revival limit stay open.
- **[Uniform Pell-orbit overlap](../../fixed-map/uniform_orbit_overlap.md)** — TRACE-125: for every odd \(n\ge5\), at \(N=u_n\), the fixed symbol overlaps only at lags \(1\) and \(n-1\), with value \(-7/2000000\). The quadratic trace coefficient is \(n\cdot1650797/4000000\). This is \(f''(0)\), not \(f(1)\). The third-order remainder and the signed off-diagonal sum stay open. The [strategy note](../../fixed-map/offdiagonal_strategy.md) is not a theorem and does not decide the eigenvalues of \(U_N\).
- **[Every odd modulus](../../fixed-map/odd_modulus_abel.md)** — TRACE-124: every odd \(N\ge3\) has pure Abel value above \(3/4\) or below \(5/7\). The modulus \(315=3^2\cdot5\cdot7\) is short because its radical \(105\) is short. The fixed kick preserves the upper gap when \(8t(N)\le3N\) and \(N\le10^{39}\), through \(10^{26}\) on the ratio-preserving families whose pure margin exceeds \(13/420\), and through \(2\cdot10^{26}\) for \(N=15r\). The kick is not claimed for a ceiling tower, for an inert partner \(q\ge40\) at exponent one, for \(15r>2\cdot10^{26}\), or at \(u_{207}\).
- **[Square-free products of at least three primes](../../fixed-map/squarefree_product_abel.md)** — TRACE-123: every square-free odd modulus with at least three distinct prime factors has pure Abel value above \(3/4\). The fixed kick preserves that gap through \(10^{39}\) for four or more prime factors and for three prime factors not divisible by \(15\), and through \(10^{26}\) for \(N=15r\). A non-square-free modulus is the statement of TRACE-124.
- **[Chinese product for the cat-map trace square](../../fixed-map/crt_composite_abel.md)** — TRACE-122: the pure trace square multiplies over prime-power factors, and every product of two odd primes lies above \(3/4\) or below \(5/7\). The square-free case of three or more prime factors is TRACE-123.
- **[Orbit-orthogonal kick at \(u_{203}\)](../../fixed-map/orbit_orthogonal_kick_spike.md)** — TRACE-118: the second-order trace expansion clears \(L_N(U_N;1)>3/4\) at the single dimension \(N=u_{203}\). The third-order majorant and the Hilbert--Schmidt triangle are silent at \(n=205\). At \(n=207\) the pure second-order center lies below \(3/4\).
- **[Kick-blind arithmetic spikes](../../fixed-map/kick_blind_arithmetic_spike.md)** — TRACE-117: the pure cat map stays above the CUE Abel value at every \(N=u_n\) for odd \(n\ge5\), and the fixed kick preserves that gap for odd \(n\) from 5 through 201. The limit remains open.
- **[Position mixing and cyclic ramp](../../fixed-map/position_chain_mixing.md)** — Actual fixed-coupling position chain has an eventual constant singular gap; cyclic contributions and a specified marked three-link contraction are controlled.
- **[Reverse-cyclic suppression](../../fixed-map/reversed_path_decay.md)** — The actual reversed-entry kernel has vanishing operator norm; general signed noncyclic pairs remain open.

- **[Structure and exact transfer](../../fixed-map/fixed_model_symmetry_theorem.md)** — Classical symmetry, seven-cut full-propagator comparison, and algebraic nondegeneracy have distinct hypotheses.
- **[Actual-start noisy law](../../fixed-map/circular_dyson_actual_start.md)** — FLOW-014 uses logarithmic noise time and a polynomial step schedule. FLOW-017 adds all fixed factorial orders on a different superpolynomial schedule.
- **[Original common-noise rate](../../fixed-map/original_channel_gap.md)** — FM-020 gives a reviewed two-copy lower bound of order u/(log N)^2 for m=1; higher-copy and quenched-functional control are separate.

- **[Conditional loop testing and short-leg deletion](../../../supplement/fixed_map/resolvent-flow/loop_test_reductions.md)** — Fixed-order anchor/dense-test sufficiency and actual normalized logarithmic excision; signed mixed hierarchy remains open.

## Suggested reading sequence

[1. fixed model symmetry theorem](../../fixed-map/fixed_model_symmetry_theorem.md) → [2. frozen seven cut reduction](../../fixed-map/frozen_seven_cut_reduction.md) → [3. fixed time wavepacket trace bound](../../fixed-map/fixed_time_wavepacket_trace_bound.md) → [4. circular dyson actual start](../../fixed-map/circular_dyson_actual_start.md) → [5. coboundary all order limit](../../fixed-map/coboundary_all_order_limit.md) → [6. microscopic noise removal](../../fixed-map/microscopic_noise_removal.md)

This is a reading sequence, not a replacement for the exact dependency graph.

## Remaining boundary

Actual signed deterministic noise removal and all-order Heisenberg comparison remain open.

## Review coverage

See [the ongoing corpus revision](../../../archive/record/corpus_revision_20261006.md). Topic membership or a verifier pass is not certification of every theorem in this list. Exact proof paths are unchanged.

## Complete source membership

- [collective_diffusion_gap](../../fixed-map/collective_diffusion_gap.md) — Universal two-copy collective diffusion gap and refined common-noise microscopic mass; exact original two-pair rate remains insufficient for original spectral transfer.
- [frozen_operator_transfer_coercivity](../../fixed-map/frozen_operator_transfer_coercivity.md) — Actual Weyl frequency exclusion, regularized singular gap and exact finite common-noise identity/swap classification; original two-kick microscopic rate and signed spectrum remain open.
- [heisenberg_pair_heat_formula](../../fixed-map/heisenberg_pair_heat_formula.md) — Exact compensated pair heat, actual smoothed stable-band form factor and the open deterministic signed defect.
- [clock_structure_and_noise_scale](../../fixed-map/clock_structure_and_noise_scale.md) — Exact clock covariance, signed pair compensation, sharp rate and critical law.
- [growing_degree_trace_projection](../../fixed-map/growing_degree_trace_projection.md) — Actual logarithmic projection rate, exact sublinear missed pair test and particular heat-inverse obstruction.
- [fixed_degree_heat_projection](../../fixed-map/fixed_degree_heat_projection.md) — Actual fixed-degree projected CUE estimates and the open complementary evaluation.
- [local_moment_transport](../../fixed-map/local_moment_transport.md) — Maximal-density packing and all-order projected/Dyson moments at t²logN→0.
- [coboundary_all_order_limit](../../fixed-map/coboundary_all_order_limit.md) — Actual-start original-chain all fixed correlations, one-chain L2 signed CUE sums and the open exact deterministic transfer condition.
- [balanced_phase_controllability](../../fixed-map/balanced_phase_controllability.md)
- [quadratic_coboundary_noise](../../fixed-map/quadratic_coboundary_noise.md) — fourth-order covariance, ellipticity, corrected noise, and transfer boundaries.
- [coboundary_spectral_flow_bound](../../fixed-map/coboundary_spectral_flow_bound.md)
- [fixed_map_moment_control_and_transfer](../../fixed-map/fixed_map_moment_control_and_transfer.md)
- [fixed_map_resolvent_frontier](../../fixed-map/fixed_map_resolvent_frontier.md)
- [frozen_spectral_flow_controls](../../fixed-map/frozen_spectral_flow_controls.md) — exact phase flow, ordered kick powers, and an isospectral clock control.
- [frozen_algebraic_spectral_simplicity](../../fixed-map/frozen_algebraic_spectral_simplicity.md)
- [frozen_arithmetic_trace_rigidity](../../fixed-map/frozen_arithmetic_trace_rigidity.md)
- [frozen_periodic_point_annihilator](../../fixed-map/frozen_periodic_point_annihilator.md) — exact all-time grids and physical-symbol averages.
- [frozen_common_antireversor_certificate](../../fixed-map/frozen_common_antireversor_certificate.md)
- [frozen_effective_gap_floor](../../fixed-map/frozen_effective_gap_floor.md)
- [frozen_kick_rank_boundary](../../fixed-map/frozen_kick_rank_boundary.md)
- [frozen_seven_cut_reduction](../../fixed-map/frozen_seven_cut_reduction.md)
- [fixed_model_pell_crossover](../../fixed-map/fixed_model_pell_crossover.md)
- [fixed_model_symmetry_theorem](../../fixed-map/fixed_model_symmetry_theorem.md)
- [nonlinear_bracket_pressure](../../fixed-map/nonlinear_bracket_pressure.md)
- [three_orientation_resolvent_barrier](../../fixed-map/three_orientation_resolvent_barrier.md)
- [quadratic_noise_coupling](../../fixed-map/quadratic_noise_coupling.md) — Quantitative raw-noise/Dyson coupling and phase-averaged local transfer.
- [quadratic_noise_reversibility](../../fixed-map/quadratic_noise_reversibility.md) — Haar-reversible drift, gradient identity and short-time path total variation.
- [quadratic_noise_trace_fluctuations](../../fixed-map/quadratic_noise_trace_fluctuations.md) — Raw and reversible fixed-trace OU limits and fixed-time coupling obstruction.
- [quadratic_noise_clock_limit](../../fixed-map/quadratic_noise_clock_limit.md) — Clock-to-Sine local limit for quadratic noise and obstruction to generic noise removal.
- [quadratic_noise_fixed_time_input](../../fixed-map/quadratic_noise_fixed_time_input.md) — Conditional fixed-time trace input via odd-dimensional periodization.
- [coboundary_fourth_order_drift](../../fixed-map/coboundary_fourth_order_drift.md) — Exact fourth-order drift of Gaussian coboundary steps.
- [coboundary_mobius_diffusion](../../fixed-map/coboundary_mobius_diffusion.md) — Mobius spectral reduction and iterated clock-to-Sine limit for uncentered coboundary kicks.
- [coboundary_joint_limit](../../fixed-map/coboundary_joint_limit.md) — Uniform fast-mode control and a joint clock-to-Sine limit at exponential small step.
- [coboundary_polynomial_limit](../../fixed-map/coboundary_polynomial_limit.md) — Dimension-uniform coefficient derivatives and an original-chain polynomial joint limit.
- [coboundary_general_start](../../fixed-map/coboundary_general_start.md) — Polynomial comparison retaining the bounded-trace initial spectrum and its exact centered Dyson reference.
- [dyson_relaxation_obstruction](../../fixed-map/dyson_relaxation_obstruction.md) — Schedule-dependent empty noisy limits with bounded fixed traces, global uniformity and all-power nonvanishing.
- [circular_dyson_actual_start](../../fixed-map/circular_dyson_actual_start.md) — Gap-independent circular kernel/Fredholm relaxation and the original-chain Sine_2 law from the actual frozen start at a logarithmic time.
- [frozen_mesoscopic_regularity](../../fixed-map/frozen_mesoscopic_regularity.md) — Poisson regularity from the existing logarithmic trace window, local heat-phase stationary points and uniform unweighted vertical tails.
- [frozen_phase_finite_type](../../fixed-map/frozen_phase_finite_type.md)
- [frozen_commutator_action](../../fixed-map/frozen_commutator_action.md)
- [offdiagonal_digit_fup](../../fixed-map/offdiagonal_digit_fup.md)
- [prime_resonant_sector](../../fixed-map/prime_resonant_sector.md) — Exact block orientation, sector mass criterion, spectral comb and conditional coherent-mode obstruction.
- [fixed_time_wavepacket_trace_bound](../../fixed-map/fixed_time_wavepacket_trace_bound.md) — 4 October proof and exact scope.
- [egorov_overlap_rigidity](../../fixed-map/egorov_overlap_rigidity.md) — 4 October proof and exact scope.
- [microscopic_noise_removal](../../fixed-map/microscopic_noise_removal.md) — Exact signed defect, all-order flat heat jets, actual full-stationarity boundary, global inverse cost and finite-field entropy.
- [original_channel_gap](../../fixed-map/original_channel_gap.md) — Original m=1 two-copy microscopic singular mass with logarithmic loss; deterministic noise removal remains open.

- [fixed_map_path_model](../../fixed-map/fixed_map_path_model.md) — Shared exact path conventions
- [four_branch_parametrix](../../fixed-map/four_branch_parametrix.md) — Shared finite-difference WKB and sampling proof
- [position_chain_mixing](../../fixed-map/position_chain_mixing.md) — FM-021
- [reversed_path_decay](../../fixed-map/reversed_path_decay.md) — FM-022

- [three_block_unmarking](../../fixed-map/three_block_unmarking.md) — Reviewed bounded subsidiary result; see its exact scope and remaining boundary.

- [arithmetic_translation_exclusion](../../spectral-obstructions/arithmetic_translation_exclusion.md) — Reviewed bounded subsidiary result; see its exact scope and remaining boundary.

- [four_block_unmarking](../../fixed-map/four_block_unmarking.md) — Reviewed bounded subsidiary result; see its exact scope and remaining boundary.

- [four_cut_rank_two_classification](../../fixed-map/four_cut_rank_two_classification.md) — Reviewed bounded subsidiary result; see its exact scope and remaining boundary.

## Fixed-order WKB and local saddle route

Read [factorial wkb reduction](../../fixed-map/factorial_wkb_reduction.md) → [exact gaussian reciprocity](../../fixed-map/exact_gaussian_reciprocity.md) → [uniform cluster lemma](../../fixed-map/uniform_cluster_lemma.md) → [rotated local first loop](../../fixed-map/rotated_local_first_loop.md). The global rotated-box theorem controls the contour/tail step in its stated finite band. Complete signed comparison and unrestricted bands remain open; local/formal results do not establish BGS.

- [Actual higher-seven-primary scalar commutant](../../fixed-map/actual_seven_primary_commutant.md), FM-024 higher-seven component: odd 49|N and 5∤N; see the first-seven extension below; literal-U algebraic-entry corollary is separate. No spectral-simplicity or universality claim.

- [Principal WKB polar comparison](../../fixed-map/polar_wkb_quantization_stability.md): fixed smooth order-1/N correction and O(N^-2) polar defect; inherited ergodic RMS transport transfers an assumed all-order compact law between unitary endpoints. No nonnormal principal-matrix eigenvalue matching is claimed.

- [Global rotated-box trace representation](../../fixed-map/global_rotated_box_trace.md): actual traces through m<=2N equal the exact box sum up to O_J(N^(3/2-J))+O_J(sqrt(N) exp(-4N/5)). The signed box sum is not evaluated.

- [Actual first-seven commutant](../../fixed-map/actual_first_seven_commutant.md): closes 7∥N,5∤N,N>7. Together with the higher-seven component FM-024 covers odd 7|N,5∤N,N>7; prior FM-008 yields the separately attributed all-35∤N combination except N=7. The later chain-trace extension below closes first-seven ramification; the later corrected lattice proof closes odd multiples of 245.

- [First-seven chain-trace theorem with arbitrary five-adic ramification](../../fixed-map/ramified_first_seven_commutant.md): all odd N>7 with 7|N,49∤N. The combined current FM-024/008 range excludes only N=7 and odd multiples of 245; former first-seven proofs and review scopes are retained.

## Actual paired-phase route

[Exact physical label quotient](../../fixed-map/paired_character_identity.md) → [fixed-tau winding-defect locality](../../fixed-map/winding_defect_locality.md) → [phase-map monotonicity/Frostman averages](../../fixed-map/phase_map_frostman.md), TRACE-018. Only the action component and the stated Fourier-index square average are controlled; complete quantum weights and signed BGS comparison remain open.

[Corrected higher-ramified lattice proof](../../fixed-map/ramified_higher_seven_commutant.md) closes the last pair-commutant family. Combined FM-024 covers every odd N>=3 except N=7; this is not a spectral-simplicity theorem.

## Selected full-weight family

[TRACE-019](../../fixed-map/selected_weighted_coefficient.md) controls a fixed-J selected
homoclinic coefficient and its once-counted cyclic/negative family. The
[stationary residual](../../fixed-map/stationary_cyclic_residual.md) retains the signed
complement and only unremoved torsion portions. Detailed W/Q/EQ and review
links are in the theorem; full signed BGS remains open.

[FM-025](../../fixed-map/uniform_five_cluster_simplicity.md) proves pure-five kick
simplicity; its [four finite U cases](../../fixed-map/finite_seven_spectral_pivots.md)
remain bounded. [FM-010 one-step companion](../../fixed-map/uniform_trace_square_transcendence.md)
extends squared-trace transcendence without claiming higher powers at7|N.

## Collective operator sector

[TRACE-020](../../fixed-map/collective_occupation_hierarchy.md) and its
[exact Q residual](../../fixed-map/collective_projector_residual.md) use actual-U
ordered operator projectors, distinct from WKB path masks. Full balanced
and off-charge complements remain open.

[FM-026](../../fixed-map/literal_time_multiplicity_bounds.md) gives scoped literal-time
multiplicity and simple-count bounds; full uniform simplicity remains open.

[General factorial ordered-sector removal](../../fixed-map/factorial_ordered_diagonal.md)
extends TRACE-020 under entrywise flatness alone. The
[mixed long-cycle companion](../../fixed-map/mixed_ordered_diagonal.md) retains separate
singular-gap assumptions and stronger band estimates. The signed complement
remains the target.

[Intermediate old layers](../../fixed-map/literal_time_multiplicity_bounds.md) sharpen the
existing FM-026 even counts; see the canonical owner for the classifier,
return operator and residual-25 proof/review paths.

[TRACE-021: one disjoint pair residual](../../fixed-map/hamming_low_switch_residual.md)
collects separately reviewed Hamming and whole-fiber low-switch estimates.
It leaves one unestimated signed Q trace and preserves the fixed-order boundary.


## Reviewed Wave2 subsidiary scopes

- [TRACE-024 actual unmasked q1 one-pinch](../../fixed-map/actual_one_pinch_disappearance.md): bounded positive/smooth signed weights; no aggregate rate or masked extension.
- [FM-031 ordinary centering](../../fixed-map/ordinary_compact_stratum_centering.md): odd N>=3, a.e., completed signed source, fixed-N cutoff only.
- [TRACE-025 rounded/split endpoint barriers](../../fixed-map/rounding_simple_spectrum_endpoint_barriers.md): changed families and a required separating property/estimate.
- [TRACE-026 corrected hook/tree/current reduction](../../fixed-map/hook_tree_phase_current_reduction.md): exact finite identities and conditional Abel reduction; negative plateau-current limit OPEN.
- [Bounded phase-source qualification](../../../literature/wave2_phase_orbit_source_qualification_20261007.md): no graph universality or priority claim.


## Weighted coherence

- [TRACE-027](../../fixed-map/weighted_phase_coherence_covariance.md): finite covariance and nontrivial Green–Kubo structure; complete signed Ward convergence only on the slow window upper half. Actual degree-two exception removal is a separate precise family.


## Complete unmasked pinch hierarchy

- [TRACE-028](../../fixed-map/right_frame_unmasked_pinch_hierarchy.md): actual right-frame/fixed-B, separated actual/annealed averages and all-z complete convex hierarchy; no masks/rates/deconvolution.
- [TRACE-029](../../fixed-map/convex_pinch_weak_noise_and_deconvolution.md): exact finite-N resummation and bounded-u signed stability; actual full unsigned large-log divergence retains identity cancellation, without a T16 refutation.


## Checked 15 October research-record imports

- [BGS-FM-032: quantum_cyclic_cohomology_20261015](../../fixed-map/quantum_cyclic_cohomology.md) — proved within the source boundary.
- [BGS-FM-033: scaled_weyl_overlap_20261015](../../fixed-map/scaled_weyl_overlap.md) — conditional within the source boundary.

## Physical kick and its limits

- [Uniform trace decay and scalar-distance limits](../../fixed-map/physical_kick_trace_decay.md).
- [All-order polynomial approximation and Pell aliases](../../fixed-map/physical_trace_polynomial_approximation.md).
