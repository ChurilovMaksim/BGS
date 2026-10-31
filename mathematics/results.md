# Theorem families and their limits

## H_arg removed, the light-cone identity and the Weil range in frozen R′ (Line K), 31 October 2026

* [TRACE-234](fixed-map/lineK_harg_removal.md) (proved; exact integers, sieve, Lean finite part): gap lemma for b′ ≥ 447, exceptions 504, 560, 616, 840.
* [TRACE-235](fixed-map/lineK_harg_removal.md) (proved): **Theorem K3**. S⁺ ∩ {3p : p ≡ p₀ (56)} is infinite for every unit p₀, with no hypothesis on
  arg ξ. H_arg ([TRACE-233](fixed-map/lineJ_d7_twisted_coefficient.md)) is bypassed, not proved.
* [TRACE-236](fixed-map/lineK_harg_removal.md) (proved, computer-assisted inputs): the J3 dichotomy holds on an infinite S⁺; frozen R′ is false under H♮
  alone.
* [TRACE-237](fixed-map/lineK_harg_removal.md) (proved): light-cone identity at prime levels.
* [TRACE-238](fixed-map/lineK_harg_removal.md) (proved): large levels d ≥ L_m absorbed by positivity (non-vacuous only from m ≈ 1.68·10⁹, numerical).
* [TRACE-240](fixed-map/lineK_harg_removal.md) (conditional): frozen R′ false under H♮ or H♮_mid ([TRACE-239](fixed-map/lineK_harg_removal.md), open).
* [TRACE-241](fixed-map/lineK_harg_removal.md), [TRACE-242](fixed-map/lineK_harg_removal.md), [TRACE-243](fixed-map/lineK_harg_removal.md) (proved): Weil-range lemmas W1–W3 (W1 modulo the cited Weil bound, EXT-WEIL-1948).
* [TRACE-245](fixed-map/lineK_harg_removal.md) and [TRACE-246](fixed-map/lineK_harg_removal.md) (conditional on OP, [TRACE-244](fixed-map/lineK_harg_removal.md), open): Theorem W and
  Theorem K2′. Conjecture C1 ([TRACE-247](fixed-map/lineK_harg_removal.md)) is open.

Limits: [TRACE-206](fixed-map/resonance_classification_lineG.md) (R′) stays open and is not refuted.

## The d = 7 twisted coefficient in frozen R′ (Line J), 31 October 2026

* [TRACE-221](fixed-map/lineJ_d7_twisted_coefficient.md) (proved; exact checks; Lean core: mod-49 period): every top twisted orbit has coefficient exactly (8th
  root of unity)/2. In the ρ = (2,8) + (−2,8) combination, the sectors 2 and 6 (including class 1:3) cancel exactly, and the sectors
  0 and 4 (classes 2:1 and 0:1) survive with |B| = |W|/2.
* [TRACE-222](fixed-map/lineJ_d7_twisted_coefficient.md) (proved): sector-level antiunitary map.
* [TRACE-223](fixed-map/lineJ_d7_twisted_coefficient.md) (proved, computer-assisted): |μ₂:₁| ∈ [1.28359503, 1.28359523], and |μ*μ₂:₁| ≥ 2.4586893 > √λ.
* [TRACE-224](fixed-map/lineJ_d7_twisted_coefficient.md) (proved; Lean core): window lemma.
* [TRACE-225](fixed-map/lineJ_d7_twisted_coefficient.md) (proved, computer-assisted): **Theorem J**. The frozen d = 7, (±2,8) contribution to W′/m is
  ≥ K_j·1.0184224^m/m in absolute value, with each sign, for some m in every 6 consecutive members of each class j mod 168
  (m ≡ 3 mod 6, m ≥ M0(j) ∈ [297, 495]).
* [TRACE-226](fixed-map/lineJ_d7_twisted_coefficient.md) and [TRACE-227](fixed-map/lineJ_d7_twisted_coefficient.md) (proved; 227 computer-assisted): the (±2,16) members at d = 7 are
  ≤ 1 % for m ≥ 243.
* [TRACE-228](fixed-map/lineJ_d7_twisted_coefficient.md), [TRACE-229](fixed-map/lineJ_d7_twisted_coefficient.md) and [TRACE-230](fixed-map/lineJ_d7_twisted_coefficient.md) (proved): inheritance, prime-level complete
  sums and the r(q) lemma.
* [TRACE-231](fixed-map/lineJ_d7_twisted_coefficient.md) (conditional): frozen R′ is false along m = 3p under H♮ ([TRACE-232](fixed-map/lineJ_d7_twisted_coefficient.md), open) and
  H_arg ([TRACE-233](fixed-map/lineJ_d7_twisted_coefficient.md), open). Unconditionally, if R′ holds, the conductor ∉ {1, 7} parts must cancel the d = 7 term
  exponentially on S⁺.

Limits: [TRACE-206](fixed-map/resonance_classification_lineG.md) (R′) stays open and is not refuted.

## Reduction of Conjecture R′ and the d = 7 twisted certificates (Line I), 31 October 2026

[TRACE-211](fixed-map/lineI_rprime_reduction.md) (proved): relative phase split. [TRACE-212](fixed-map/lineI_rprime_reduction.md) (proved; Lean core): the dilation-coset L² law and the per-member Gauss-sum formula Z_t = ω_t Z0/d + Δ_t for every odd d | h_m. [TRACE-213](fixed-map/lineI_rprime_reduction.md) (proved): W′_m = (non-resonant sum) + φ⁻¹ Σ Dev_d(ρ) exactly, so R′ follows from (E″), (T″) and (D); none of these is proved. [TRACE-214](fixed-map/lineI_rprime_reduction.md) (proved): Fourier/Ramanujan expansion of weighted horocycle sums. [TRACE-215](fixed-map/lineI_rprime_reduction.md) (proved, computer-assisted): the d = 7 square term is ≤ 0.01 for every m ≡ 3 (mod 6), m ≥ 321 (k1 kick, η = 2; ρ = (±2,8) only, the (±2,16) level-7 members are not controlled). [TRACE-216](fixed-map/lineI_rprime_reduction.md) (proved): exact monomial intertwiners. [TRACE-217](fixed-map/lineI_rprime_reduction.md) (proved, computer-assisted): three simple top twisted eigenvalues with 1.262 < |μ| < 1.45, so r_tw > √λ/μ₀ and the operator-radius route to the d = 7 cross term fails. [TRACE-218](fixed-map/lineI_rprime_reduction.md) (proved): aliasing/Möbius identity. [TRACE-219](fixed-map/lineI_rprime_reduction.md) (proved modulo BHV): h_m has a new odd prime for every m ≥ 16. [TRACE-220](fixed-map/lineI_rprime_reduction.md) (open): Conjecture R′_A. Limits: [TRACE-206](fixed-map/resonance_classification_lineG.md) (R′) stays open and is neither proved nor disproved; c(β) ≠ 0 is not certified.

## Certified 49-state spectrum for the Line B kick (Line H), 30 October 2026

[TRACE-207](fixed-map/lineH_49state_certificate.md) (proved): the κ lemma and the full-alphabet 49-state lifted trace identity for the Line B kick. [TRACE-208](fixed-map/lineH_49state_certificate.md) (proved, computer-assisted): at η = 2 and s = −1, V_0 has exactly one eigenvalue in |z| > 1.5, simple, with |μ*| ∈ [1.846834, 1.946835]; the rest of the spectrum is certified inside. [TRACE-209](fixed-map/lineH_49state_certificate.md) (proved, computer-assisted): W̃rest_m(2)/m ≥ 1.4·10⁴ for every odd m ≥ 47 with 3 ∤ m. Consequence: [TRACE-179](fixed-map/derandomized_fixed_kick.md) (Conjecture R as stated) is refuted. Limits: R_NSW ([TRACE-210](fixed-map/derandomized_fixed_kick.md), split from 179) is open; the odd m with 3 ∤ m in 17–43, 3 | m, η ≠ 2 and s = +1 are not covered; TRACE-196 stays conditional as stated; nothing about BGS itself.

## Resonant residues of the fixed kick (Line E), 30 October 2026

[TRACE-183](fixed-map/resonant_residue_lineE.md) (proved): the exact collapse of the Pell phase at N ≡ −4 (mod h_m). [TRACE-184](fixed-map/resonant_residue_lineE.md) (proved): the m-independent IFS transfer-operator law, finite alphabet. [TRACE-185](fixed-map/resonant_residue_lineE.md)–[187](fixed-map/resonant_residue_lineE.md) (proved, computer-assisted, k1 kick only): the certified leading eigenvalue, the exponential lower bound for all m ≥ m0 for the truncated kick, and |W̃rest_m| > m for odd m ∈ [17,39] at η = 2 (also m ∈ [19,27] at η = 1.75 and m ∈ [23,33] at η = 1.5). [TRACE-188](fixed-map/resonant_residue_lineE.md) (conditional): asymptotic failure of the k1 analogue of R under H∞. [TRACE-189](fixed-map/resonant_residue_lineE.md)–[192](fixed-map/resonant_residue_lineE.md) (open; numerical records, the ∓196 resonance of the Line B kick when 3 ∤ m, η-interval certification, and the identification of the TRACE-182 outlier). After a second referee audit: [TRACE-193](fixed-map/resonant_residue_lineE.md)–[195](fixed-map/resonant_residue_lineE.md) (proved: the 7-mode corollary, computer-assisted via 187; the a²-resonance law; computer-assisted Line B kick bounds at m = 11 and 13 only, with an m = 17 certificate pending) and [TRACE-196](fixed-map/resonant_residue_lineE.md) (conditional failure of R along 3 ∤ m). Limits: no o(m) statement is disproved, and Conjecture R (TRACE-179) stays open. (Later: Line H, above, refutes Conjecture R as stated at η = 2.)

## Fixed diagonal kick, 29 October 2026

[TRACE-163](fixed-map/derandomized_fixed_kick.md) is the exact Pell-norm trace formula for the fixed diagonal kick, the orbit form, and $B_m=2m$ at $m\le 8$ (proved). [TRACE-164](fixed-map/derandomized_fixed_kick.md) is conditional on $\mathrm{ND}_m$. [TRACE-165](fixed-map/derandomized_fixed_kick.md) is the Ramanujan kernel and the exact odd-$m$ ramp (proved). [TRACE-166](fixed-map/derandomized_fixed_kick.md) is the $p$-splitting lemma (proved). [TRACE-167](fixed-map/derandomized_fixed_kick.md) is automatic admissibility (proved, after the second reader's repair). [TRACE-168](fixed-map/derandomized_fixed_kick.md) is Theorem N for eleven certified NSW primes (proved; nontrivial from $m=29$). [TRACE-169](fixed-map/derandomized_fixed_kick.md) is the norm-class formula (proved). [TRACE-170](fixed-map/derandomized_fixed_kick.md) is the parity decomposition and the transfer formula (proved). [TRACE-171](fixed-map/derandomized_fixed_kick.md) is the lower bound for odd $m\ge 5$ (proved). [TRACE-172](fixed-map/derandomized_fixed_kick.md) is the majorant framework (proved). [TRACE-173](fixed-map/derandomized_fixed_kick.md) is the certified decay on $\eta\in[1,81.574]$ (proved only with the directed-rounding constants; the authors' float constants are excluded). [TRACE-174](fixed-map/derandomized_fixed_kick.md) is conditional on (I1)–(I3). [TRACE-175](fixed-map/derandomized_fixed_kick.md) is the $N$-average theorem (proved). [TRACE-176](fixed-map/derandomized_fixed_kick.md) is conditional on $\mathrm{ND}^{(\le k)}$. [TRACE-178](fixed-map/derandomized_fixed_kick.md) is the trivial torsion-split identity (proved; the reading is numerical). [TRACE-177](fixed-map/derandomized_fixed_kick.md), [TRACE-179](fixed-map/derandomized_fixed_kick.md), [TRACE-180](fixed-map/derandomized_fixed_kick.md), [TRACE-181](fixed-map/derandomized_fixed_kick.md) and [TRACE-182](fixed-map/derandomized_fixed_kick.md) are open. Nothing is proved at $\tau=m/N=O(1)$. This is not progress on BGS-BGS-001 or BGS-TRACE-148. "$B_m\to 2m$" is not claimed.

## Random-phase encounter pairs, 29 October 2026

[TRACE-143](fixed-map/random_phase_encounter_pairs.md) identifies the Haar diagonal-phase cat map at odd $N$ with Tanner's random-phase DFT. [TRACE-144](fixed-map/random_phase_encounter_pairs.md) is the exact Gauss-sum formula, rational for every $p\equiv 3\pmod 4$. [TRACE-145](fixed-map/random_phase_encounter_pairs.md) classifies the order-$1/p$ pairs as $2$-opt, swap and figure-eight. [TRACE-146](fixed-map/random_phase_encounter_pairs.md) gives $a_2=-2m^2$ for every $m\ge 5$ and every prime $p>4^m$. Gnutzmann–Seif 2004 derived $2\tau-2\tau^2$ diagrammatically for this ensemble, Gnutzmann–Altland 2005 and Pluhař–Weidenmüller 2014 predict the full COE form factor non-rigorously, and Berkolaiko–Keating 1999 did exact all-pairs combinatorics for random-phase star graphs; new here is only the rigorous fixed-$m$ exact-in-$p$ result, the complete classification including swaps, and the $m\le 12$ expansions. The explicit remainder is non-informative below $(C_m/2m^2)^2$. [TRACE-147](fixed-map/random_phase_encounter_pairs.md) is verification-pending: the computer-assisted expansion through $m=12$ deviates from the fixed-$m$ COE value $2m^3$ at $m=5,6,8,9,12$, and an independent referee replay of every coefficient at $171$ primes is deposited. Promotion is a separate status decision, as for BGS-RES-022. [TRACE-148](fixed-map/random_phase_encounter_pairs.md) is the open scaling-limit conjecture. The values at $m=1,2,3$ remain TRACE-127. This does not prove BGS-TRACE-005 or BGS-BGS-001, and it does not cover the fixed kick.

## Band-limited random kicks, 29 October 2026

[TRACE-149](fixed-map/band_limited_kick_bridge.md) is the exact bridge $E|\mathrm{Tr}\,U^m|^2=\Psi_m(t_N)$ for few-mode random kicks at every odd $N$ with $\gcd(N,D_m)=1$ (Line B's Theorem 1 per realisation; Boasman–Keating mechanism, not new). [TRACE-150](fixed-map/band_limited_kick_bridge.md) gives the $1/N$ expansion and the residue period bound $g'_m$; the remainder is not uniform in $\eta$ or $K$. [TRACE-151](fixed-map/band_limited_kick_bridge.md) is the orbit-pair form with the Gauss-weight support. [TRACE-152](fixed-map/band_limited_kick_bridge.md) proves the strong-kick limit $B_m^{\mathrm{sym}}$ at every residue under dihedral-class separation; the instances $m\le7$ are verification-pending ([TRACE-153](fixed-map/band_limited_kick_bridge.md)); [TRACE-154](fixed-map/band_limited_kick_bridge.md) proves $B_m^{\mathrm{sym}}<2m$ for odd $m$, even $m$ is open ([TRACE-155](fixed-map/band_limited_kick_bridge.md)); [TRACE-156](fixed-map/band_limited_kick_bridge.md) is multiset separation and half-turn collisions. [TRACE-157](fixed-map/band_limited_kick_bridge.md): the dihedral-diagonal part of $c_1$ vanishes and $c_1$ is odd in the residue; [TRACE-158](fixed-map/band_limited_kick_bridge.md) (conditional, Gaussian ensemble only) gives $c_1\to0$; [TRACE-159](fixed-map/band_limited_kick_bridge.md) (uniform phases) is open. [TRACE-160](fixed-map/band_limited_kick_bridge.md) transfers Line C to the full band; [TRACE-161](fixed-map/band_limited_kick_bridge.md) and [TRACE-162](fixed-map/band_limited_kick_bridge.md) (intermediate band; crossover conjecture with Monte Carlo diagnostics) are open. On main at d6fa6e2a the next free TRACE identifier was 149, so this block is registered as BGS-TRACE-149 through BGS-TRACE-162; the Line B packet had not merged. This does not prove BGS-TRACE-005 or BGS-BGS-001.

## Twisted closure and revival at the scalar return, 29 October 2026

[TRACE-133](fixed-map/revival_closure_law.md) gives the twisted closure formula for the position-diagonal kick at every time, with cocycle phase \(\beta\) and \(|\Lambda_m|=N^{m-2}\). [TRACE-134](fixed-map/revival_closure_law.md) gives a pointwise bound at the scalar return and the \(\exp(-\eta^2 t\sigma_d/2)\) limit on the minimal-period sequence; the explicit bound is non-informative at computable \(N\) (first below \(1\) near \(N\approx10^{191}\) at \(\lambda=1/4\)). [TRACE-135](fixed-map/revival_closure_law.md) reduces the scalar-return trace when \(S^{t/2}\equiv -I\). [TRACE-136](fixed-map/revival_closure_law.md) and [TRACE-137](fixed-map/revival_closure_law.md) are open conjectures for even and odd order respectively. Position-diagonal kick only (\(\sigma_d=13203/32000\)). BGS-TRACE-005 stays open.

## Fixed-time limits for a general hyperbolic cat map, 29 October 2026

[TRACE-140](fixed-map/momentum_phase_cue.md) gives the short-time unitary value for Haar phases in position and in momentum. For an odd prime not dividing \(\beta\delta\), with \(\lambda=\delta^{-1}\not\equiv -1\), the distance from \(\mathbb E\lvert\operatorname{Tr} U^m\rvert^2\) to \(m P(p,m)/p^m\) is at most \((m!)^2(1+2m(m-1))/p\) when \(m\ge 3\). At time two the same congruence is required, and the distance to \(2\) is at most \(20/p\); if \(\delta\equiv -1\) the limits are \(4\) and \(2m\). [TRACE-141](fixed-map/momentum_phase_cue.md) gives the moment \(k!\,m^k\). [TRACE-142](fixed-map/momentum_phase_cue.md) identifies the Gaussian main term \(m(1+e^{-vm})\); the non-injective remainder is not bounded, so the limit is verification-pending. The odd symbol energy is \(9/125000\). The choice \(v=\sigma_{\mathrm{odd}}\eta^2\) is a convention, and partner-variance matching gives twice this. The count \(m\) is the diagonal count of Tanner and of Pakoński–Życzkowski–Kuś; the finite-\(p\) error constant is the extension proved here. BGS-TRACE-005 stays open.

[TRACE-132](fixed-map/hyperbolic_short_time_limit.md) identifies the fixed-time limits. For Haar diagonal phases the limit is \(2m\) at each \(m\ge 3\), with distance at most \(m!(1+m(m-1))/N\) from \(2m P(N,m)/N^m\). The antiunitary \(\Theta'=DEK_0\) reverses \(DM_N\) for every hyperbolic \(S\). Times one and two tend to \(1\) and \(2\). A finite cosine with \(\eta=o(N^{-2/3})\) tends to \(1\) along odd \(N\) coprime to \(\beta(2-u_m)\); along \(N\) divisible by \(7\) (e.g. \(35,77,91,707\)) the time-\(3\) kernel has order at least \(49\), so the limit \(1\) fails when \(\gcd(N,\beta(2-u_m))>1\). If the frequencies \(1\) through \(m\) are present, sending \(\eta\to\infty\) before \(N\to\infty\) recovers \(2m\). A second diagonal factor does not replace \(2m\) by \(m\). Row inversion on an odd prime has limit \(m\). A momentum sine leaves the class, and its form factor is not identified. The orthogonal-class name remains a heuristic for \(\Theta'\). BGS-TRACE-005 stays open.

## Diagonal phase average for every hyperbolic cat map, 29 October 2026

[TRACE-131](fixed-map/hyperbolic_diagonal_form_factor.md) extends the phase average from one cat map to every hyperbolic matrix in \(\mathrm{SL}(2,\mathbb Z)\). For odd \(N\) coprime to the upper-right entry, the quantization is unitary and flat, and it is symmetric exactly when the diagonal entries agree modulo \(N\). The antiunitary \(\Theta'=DEK_0\) reverses the kicked propagator for every such matrix. The pure squared trace equals the order of the kernel. A finite cosine kick with independent uniform phases has quantum average equal to a Bessel-weighted path sum, and the order-two expansion is \(|\ker|+\eta^2 D_2+\rho\) with an explicit remainder. The trace, the Pell companion, and the splitting of the discriminant determine the prime kernel when the prime does not divide the upper-right entry. Two matrices of trace \(-16\) have different kernels modulo \(3\), and both of those upper-right entries are divisible by \(3\). At an identity revival the second-order coefficient is \(-m(\sigma-\sigma_0)p^2\). Time one equals \(1\) whenever \(\gcd(2-\operatorname{tr} S,N)=1\). This is not the all-order revival law and not a fixed-time limit. BGS-TRACE-005 stays open.

## Local antiunitary for a position-diagonal kick, 29 October 2026

[TRACE-130](fixed-map/sixteen_phase_symmetry.md) proves that for every real diagonal kick the antiunitary \(\Theta=DK_0\) satisfies \(\Theta^2=1\) and \(\Theta U\Theta^{-1}=U^\dagger\). The orthogonal-class name is a heuristic. It is not a COE form factor, and it does not exclude a CUE form factor. Each of the rows \(\ell=\pm 1\) has energy \(9/160000\). The full symbol is \(K_0\)-even only for some phases. The momentum sine has symbol energy \(1/2\), and a nonzero multiple is not a function of position. BGS-TRACE-005 stays open.

## Scalar-return orbit sum, 29 October 2026

[TRACE-129](fixed-map/scalar_return_bessel.md) gives the Bessel average of the classical position-diagonal orbit sum at a return \(S^m\equiv I\). It is not an identity for the quantum sixteen-phase average. The degree-two jet is \(\exp(-m\sigma_{\mathrm{diag}}\eta^2)\). The degree-four gap is the quadruple excess of the position orbit. It vanishes at \(7\), \(31\), \(41\) and \(47\), and it equals \(120\) at \(11\). Time one equals \(1+\rho_1\) inside the perturbative window. Each momentum row \(\ell=\pm 1\) has energy \(9/160000\). No form-factor limit at times of order \(N\) is proved. BGS-TRACE-005 stays open.

## Short-time diagonal-phase limits, 29 October 2026

[TRACE-128](fixed-map/diagonal_phase_short_time.md) gives the fixed-time limit of the diagonal-phase form factor. For the symmetric cat map the limit is \(2m\) at each \(m\ge 3\), and the distance to \(2m P(N,m)/N^m\) is at most \(m!(1+m(m-1))/N\). The logarithmic window \(m\le c\log N/\log\log N\) with \(c<1\) is included. A power \(m\le N^{\alpha}\) is not. Row inversion by \(x\mapsto x^{-1}\) on an odd prime produces the limit \(m\), except at \(p=3\), where the permutation is the identity. A second diagonal factor is conjugate, by \(D_2\), to one diagonal times \(M_N\). The sixteen-phase ensemble of TRACE-126 is not evaluated. BGS-TRACE-005 stays open.

## Diagonal random-phase form factor, 29 October 2026

[TRACE-127](fixed-map/diagonal_phase_form_factor.md) evaluates \(U=DM_N\) with independent uniform phases on the \(N\) position sites. For every flat matrix, the phase-averaged squared trace is \(1\) at time one, \((2N-1)/N\) at time two, and at most \(m!\) at time \(m\). For the cat-map quantization at every odd \(N\ge 3\), the time-three value is \((6N^2-9N+4)/N^2\). The pure squared trace is \(1\) at time two. At time three it is \(49\) when \(7\) divides \(N\) and \(1\) otherwise, including at \(N=49\). The diagonal-phase value lies above the pure value at time two, above it at time three when \(7\) does not divide \(N\), and below \(6\) when the pure value is \(49\). The time-three limit \(6\) equals \(2\cdot 3\): the antiunitary \(\Theta=DK_0\) squares to \(1\) and reverses \(U\), which is a heuristic orthogonal label and not a COE form factor, and a \(2\)-cycle is its own reversal so the time-two limit is \(2\). The sixteen-phase ensemble of TRACE-126 is not evaluated. A twenty-four-draw sample of that ensemble is recorded and is not a limit. BGS-TRACE-005 stays open.

## Phase-averaged form factor, 29 October 2026

[TRACE-126](fixed-map/interaction_phase_form_factor.md) is an average over independent phases on the 16 mode pairs of the kick. For every odd dimension and every power, the averaged squared trace equals \(|K_m|+\eta^2 D_2+\rho\), with \(D_2\) a Gauss-sum coefficient and with an explicit remainder. At an odd prime \(p\) the second-order revival term is \(-m(\sigma-\sigma_0(p))p^2\), with \(\sigma_0(p)=0\) for \(p\ge 11\) and with the three exceptions \(\sigma_0(3)=81/64000\), \(\sigma_0(5)=1/320000\), \(\sigma_0(7)=81/200\). The fixed kick has a linear term, nonzero at \(N=11\), \(m=3\). Parity and position conjugation fail for the kicked propagator when \(0<\lvert\eta\rvert<\pi/B\), except at dimension \(7\), where \(A_7=(9/10)I\). The signed off-diagonal sum and any limit with \(\tau^2 N^3\) tending to a positive constant remain open. BGS-TRACE-005 stays open.

## Kick-blind arithmetic spikes, 28 October 2026

[TRACE-117](fixed-map/kick_blind_arithmetic_spike.md) keeps the pure cat-map Abel statistic a distance greater than \(1/2\) from the CUE value at every \(N=u_n\) with \(n\) odd and at least \(5\). The same gap survives the fixed kick on the 99 odd indices from \(5\) through \(201\), including the 77-digit dimension \(u_{201}\). The rational comparisons are a Lean `decide` witness plus independent Python and C++ integer checks. The one-term estimate is inconclusive at \(n=203\).

[TRACE-118](fixed-map/orbit_orthogonal_kick_spike.md) clears that index. At \(N=u_{203}\) a second-order expansion, using trace orthogonality of the symbol orbit up to one explicit overlap, gives \(L_N(U_N;1)>3/4\). The same third-order majorant, and the Hilbert--Schmidt triangle, are silent at \(n=205\). At \(n=207\) the pure second-order center itself satisfies \((1-\varepsilon_2)^2<3/4\). Signed cancellation for the remaining dimensions, and BGS-TRACE-005, remain open.

[TRACE-119](fixed-map/positive_time_spike.md) clears \(n=205\) by a positive-time expansion. Resonant diagrams of degree at most \(11\) are exact archimedean zeros, indecomposable gaps are at most \(4\), and the resulting activity bound leaves an Abel term above \(3/4\) at \(N=u_{205}\) (79 digits). The \(n=207\) disk remains below \(3/4\). BGS-TRACE-005 stays open.

[TRACE-120](fixed-map/order_ladder_abel.md) replaces the next single-index disk by the order of \(C\) modulo \(N\). If \(12t(N)\le5N\), the pure cat map satisfies \(L_N(M_N;1)>3/4\). If \(p\) is an odd prime and the order is at least \((p+1)/2\), the same statistic lies at distance less than \(1/2\) from the CUE value. The fixed kick preserves the short side for every such odd \(N\le10^{39}\) and the long side for every such prime \(p\le10^{26}\). The dimension \(N=35\), of order \(6\), is not a Pell number, and one return there lies below \(3/4\). The kicked map at \(u_{207}\) stays unresolved. BGS-TRACE-005 stays open.

[TRACE-121](fixed-map/order_trichotomy_abel.md) removes the intermediate interval for primes and prime powers. The order modulo an odd prime divides \(p-\varepsilon\) and is short, long, or split-half. The long class is the inert full order \(t=p+1\). The clause \(t=(p+1)/2\) does not occur, and a split prime does not have order \(p-1\). The prime \(p=7\) lies above \(3/4\), and every larger split-half prime lies below \(41/60\). The lifting depth decides every higher power: powers of \(7\) stay above \(3/4\), while depth at least two puts \(13^2\) and \(31^2\) above \(3/4\) even though those primes themselves lie on the CUE side of distance \(1/2\). The fixed kick preserves the new comparisons through \(10^{26}\), except depth-one powers of a split-half prime \(p\ge17\), which stop at \(10^{25}\). For every odd \(n\ge5\) the pure map at \(u_n\), including \(u_{207}\), is already above \(3/4\). The kick at \(u_{207}\) stays unresolved. No density is proved. BGS-TRACE-005 stays open.

[TRACE-122](fixed-map/crt_composite_abel.md) extends the trace square to every odd modulus by the Chinese remainder theorem, and gives the square-free Abel sum as a finite combination of geometric series. Every product of two odd primes is then decided: short composite orders and non-short multiples of \(7\) lie above \(3/4\), every product of \(3\) with a short prime is short, and every remaining semiprime lies below \(5/7\). The fixed kick preserves the gap above \(3/4\) through \(10^{26}\) for \(N=21\). A split full-order multiple of \(7\) does not occur, and every product of \(3\) with a short prime \(q\ge5\) is short.

[TRACE-123](fixed-map/squarefree_product_abel.md) places every square-free product of at least three distinct odd primes above \(3/4\). The fixed kick preserves that gap through \(10^{39}\) for four or more prime factors and for three prime factors not divisible by \(15\), and through \(10^{26}\) for \(N=15r\). The modulus \(N=195\) is settled by the eight-term subset expansion, not by the short-order test. A prime square is outside this statement.

[TRACE-124](fixed-map/odd_modulus_abel.md) places every odd modulus on one side of the pair of thresholds: \(L_N(M_N;1)>3/4\) or \(L_N(M_N;1)<5/7\). The modulus \(315=3^2\cdot5\cdot7\) is short because its radical \(105\) is short. The fixed kick preserves the gap above \(3/4\) when \(8t(N)\le3N\) and \(N\le10^{39}\), through \(10^{26}\) on the ratio-preserving families whose pure margin exceeds \(13/420\), and through \(2\cdot10^{26}\) for \(N=15r\). The kick is not claimed for a ceiling tower, for an inert partner \(q\ge40\) at exponent one, for \(15r>2\cdot10^{26}\), or at \(u_{207}\). No density is proved. BGS-TRACE-005 stays open.

[TRACE-125](fixed-map/uniform_orbit_overlap.md) gives the same transported overlap at every odd Pell return. For odd \(n\ge5\) and \(N=u_n\), \(\gamma(r)=0\) on \(1\le r\le n-1\) except \(\gamma(1)=\gamma(n-1)=-7/2000000\), so \(\operatorname{Tr}(S^2)/N=n\cdot1650797/4000000\). This is the second derivative of the transported-product trace at zero coupling. It does not bound the third-order remainder and does not move the signed off-diagonal sum. BGS-TRACE-005 stays open.

## Aristotle formalization integration, 28 October 2026

Adapted all 39 substantive modules from the older Aristotle snapshot into the existing Lean 4.33.1 graph. The [coverage map](../formalization/MATHLIB_LAYER_RU.md) and [receipt](../evidence/formalization/aristotle_20261027/receipt.json) record exact theorem scope, 589 axiom-audited declarations and the successful aggregate build. ERR-060 corrects the pure-loss scalar identity in the proof and manuscript. Current claim states, TRACE-114–116 and pinned dependencies are retained; no BGS closure is asserted.

## Operator resolution and the short-trace barrier, 27 October 2026

[TRACE-114](fixed-map/balanced_rounding_research_20261027.md) shows that even absolute $o(1)$ preservation of polynomially many short traces and eigenvectors does not determine a microscopic law for a general quantizer. [TRACE-115/116](trace-bridge/microscopic_unitary_stability_20261027.md) prove bounded-test and positive-energy stability, then transfer the original-family pair test through $O(N^{-2})$ matrix errors using TRACE-113. The unitary error is $O(1/\log N)$; the nonunitary finite-trace error is $O(1/\sqrt{\log N}+1/N)$. These are analytic author proofs, not external refereeing. The [disposition review](../record/trace005_continuation_review.md) credits existing results and tracks the unadopted candidate estimates. The original pair limit and all-order hierarchy remain open.

## Trace results and dependency closure, 22 October 2026

The [review](../record/spectral_research/trace_closure.md) closes the inserted-trace input in TRACE-109 by a
finite-grid corrected-amplitude proof. TRACE-110 now has proved global
$O(1/\log N)$ spectral matching and a matching Pell lower order.
[TRACE-112](fixed-map/displacement_density_trace_bound.md) supplies an
independent logarithmic-time upper-bound route;
[TRACE-113](fixed-map/fixed_kick_uniform_trace_bound.md) proves the
uniform power-trace input with one threshold for all iterates.
All statements have analytic project proofs with author check, not external
refereeing. Microscopic signed cancellation and BGS remain open.

## Final spectral research edition, 21 October 2026

[Thematic results and individual proofs](spectral_research/README.md) integrate
all fourteen rounds. [TRACE-108](fixed-map/coordinate_return_quartic.md) is the
quartic one-step intensity theorem; [TRACE-111](fixed-map/pell_weighted_curvature.md)
sums the initial gradient/Hessian and proves an early inflection.
[TRACE-109](fixed-map/inserted_trace_coboundary.md) and
[TRACE-110](fixed-map/spectral_orbit_distance.md) now include proved global asymptotic applications; their
21 October input qualifications were closed on 22 October. The fixed-coupling signed
Heisenberg hierarchy remains open. [Review](../record/spectral_research/spectral_final_integration.md).

## Physical-kick bounds, 21 October 2026

[Uniform trace decay and scalar-distance limits](fixed-map/physical_kick_trace_decay.md)
(TRACE-106) and [all-order polynomial approximation with Pell alias limits](fixed-map/physical_trace_polynomial_approximation.md)
(TRACE-107) are now recorded with full proofs. The imported exponent 1/25 is
strengthened to 1/9 for the single kick. The original microscopic trace hierarchy
remains open. [Review scope](../record/spectral_research/spectral_master_audit.md).


This file is a narrative index of theorem families and their limits,
grouped by family and date; it is not a complete per-claim index.
For the complete per-claim index use the generated
[claim registry](../record/claim_registry.md) and the
[scientific corpus atlas](../docs/corpus_atlas.md); claim status is
controlled by [claims.json](../record/claims.json).

## Integrated continuation, 19 October 2026

[TRACE-095 through TRACE-105](trace-bridge/phase_ensemble_continuation.md)
cover the checked auxiliary phase research. The full four-port zero and total
defect-two sum are complete at the stated scope. The joint local-defect-at-most-two
sum has a quartic limit for tau<1/9 and uniform finite-size control; it retains
a nonzero -3 tau^3 term. The exact positive Cauchy projection laws do not identify
a matrix law, as shown by an explicit signed-source counterexample.
[Integration, evidence audit and next obligations](../archive/record/chat_integration_20261019.md).
BGS-TRACE-005 and BGS-BGS-001 remain OPEN. Conditional G/TC/R premises remain explicit.

## Checked continuation, 16 October 2026

- **BGS-TRACE-092:** [Positive Abel decomposition and optimal square-root clock rigidity](trace-bridge/abel_clock_rigidity.md), including stationary processes and multiple eigenvalues.
- **BGS-TRACE-093:** [Flat-sector Gaussian comparison for every m=o(N), exact Heisenberg exponential rate and collision mean](trace-bridge/gaussian_equal_edge.md).

The Gaussian benchmark and its sinh crossover are prior results. The subsequent
[TRACE-094 proof](trace-bridge/wick_collision_poisson.md) closes the flat
Heisenberg collision law and exact ratio B/G->exp(-alpha^2). It also gives
geometric vertex occupations and a bounded radial-entry comparison. The
physical non-flat extension and original signed BGS hierarchy remain open.
[Current proof outcome and next obligations](../archive/record/wick_poisson_continuation_20261016.md).
The [earlier checkpoint](../archive/record/research_continuation_20261016.md) retains its original scope.

## Research-record integration, 16 October 2026

[Exact review and 90-entry inventory](../archive/record/chat_integration_20261016.md).
The all-order process implication no longer requires an independent UI premise.
The actual signed hierarchy, physical parameter moment and positive Hardy
excess limits remain unproved. Resonance deletion is sufficient only.

- **BGS-FM-032** — [Prime cyclic cohomology and parity-resolved susceptibility](fixed-map/quantum_cyclic_cohomology.md); proved within its stated scope.
- **BGS-TRACE-084** — [Mesoscopic block number-variance criterion and collective trace-energy boundary](trace-bridge/resonant_mesoscopic_criterion.md); proved within its stated scope.
- **BGS-TRACE-085** — [Exact root lifting and failure of necessity for resonance-sector deletion](trace-bridge/root_lifting_sector_boundary.md); proved within its stated scope.
- **BGS-TRACE-086** — [All-order signed diagonal hierarchy implies local Sine2 and local moment UI](trace-bridge/all_order_process_closure.md); proved within its stated scope.
- **BGS-FM-033** — [All-label-scale one-step Weyl overlap and prime-orbit corollaries](fixed-map/scaled_weyl_overlap.md); conditional within its stated scope.
- **BGS-CUE-002** — [All-positive-frequency CUE trace-square covariance and exact coupling derivative](trace-bridge/full_pair_cue_covariance.md); proved within its stated scope.
- **BGS-TRACE-087** — [Exact parameter bandwidth and quantitative de-averaging to a fixed coupling](trace-bridge/parameter_deaveraging.md); proved within its stated scope.
- **BGS-TRACE-088** — [Rooted BEST count, extensive equal-edge mass and unitary compensation](trace-bridge/equal_edge_occupation.md); proved within its stated scope.
- **BGS-TRACE-089** — [Factorially weighted square-root-time equal-edge collision crossover](trace-bridge/collision_crossover.md); proved within its stated scope.
- **BGS-TRACE-090** — [Contractive full-spectrum radial ratios and mixed-moment weak-process criterion](trace-bridge/bounded_radial_ratios.md); proved within its stated scope.
- **BGS-TRACE-091** — [Sharp clock minimum and exact radial and Abel Hardy remainders](trace-bridge/hardy_spectral_remainder.md); proved within its stated scope.


[TRACE-083](spectral-obstructions/coherent_first_return_pulse.md) evaluates
a single observed memory coefficient for the TRACE-081 family.
At time 2p it is almost an isometry on nearly all centered diagonal
directions, although its remaining monitored energy tail is at most
16 N^-6. Unconjugated first and second pulse traces can vanish while
the cubic trace stays large. Repeated completed excursions and a
later first-return coefficient are different operators. These are
abstract-family conclusions; the original physical signed source
and the BGS limit remain open.

[TRACE-081](spectral-obstructions/flat_spectrum_obstruction.md) proves that
perfect intensity mixing, a vanishing coordinate reversal norm, simple
spectrum and a uniform macroscopic phase law can coexist with an empty
origin-averaged microscopic limit and clustered spacings. The construction
is an abstract unitary family; it is not the fixed smooth chaotic model.
[TRACE-082](spectral-obstructions/coherence_memory_plateau.md) identifies
exact coherent return memory and proves a universal obstruction:

$$
\mathcal E=\mathcal Q\operatorname{Ad}_U\mathcal Q,
\qquad \|\mathcal E^r\|_{\mathrm{HS}\to\mathrm{HS}}=1
\quad(0\le r<N).
$$

Here Q removes the diagonal part and the norm acts on Hilbert--Schmidt
matrix space. A general early norm contraction cannot replace the missing
source-specific signed cancellation. [Exact outcome](../archive/record/spectral_coherence_continuation_20261014.md).

[TRACE-080](trace-bridge/unconditional_feedback_flatness.md) now
proves unconditional entry flatness from any deterministic unitary startup
with intensity bound C0/N and centered singular norm at most 1/100.
Uniform ports and fresh uniform phases preserve flatness, a small intensity
gap, bounded row/column fourth-power energies and a uniform two-step bound
at every depth down to ceil(log(2N)^(4+kappa)), with failure
O(log(2N)^(-1-kappa)). Fixed-order clocks and the empirical weak law are
unconditional on that same cutoff; reversal convergence uses its separate
initial-channel assumption. The actual odd-N fixed-coupling family has
these named eventual startup inputs. The deterministic microscopic law
and BGS remain open.

[TRACE-079](trace-bridge/two_step_stopped_concentration.md) supplies
the all-pair stopped concentration input, including the diagonal and full
first crossings. [Exact outcome](../archive/record/feedback_flatness_continuation_20261013.md).

[TRACE-078](trace-bridge/two_step_increment_variance.md) adds
an exact raw second-moment bound for the complete two-step feedback
increment: `2600 delta²[(P²)ij+(P³)ij]/u` for a uniform port and any
phases, with frozen endpoints. Its one-step conclusion is complemented
by the separate TRACE-079/080 concentration and trajectory proofs.

[TRACE-077](trace-bridge/green_compression_gap.md) linearizes
classical elimination in centered Green coordinates. Its decaying initial
compression and adapted martingale give a shrinking intensity singular
norm on the entry-stopped prefix, with quantitative failure probability.
This proves the deep-range three-step forcing estimate on reached states.
The stopped theorem alone supplies no entry-survival probability;
TRACE-080 closes it under its smaller startup-gap hypothesis.
[Exact outcome](../archive/record/green_compression_continuation_20261013.md).

[TRACE-076](trace-bridge/haar_feedback_clock_law.md) supplies the exact Haar
feedback scattering/delay joint law, inverse-Jacobi spectrum, finite
moment threshold and exact first moment. Haar all-time flatness closes
the conditional clock premise in that ensemble. The full-depth laws at
every fixed order and empirical weak law hold unconditionally for
independent initial distributions of relative entropy O(log N) relative
to Haar. A bounded-entropy prescribed-gap example excludes the associated
fixed-origin Sine₂ implication. The deterministic microscopic law and BGS remain open; the separate
TRACE-080 theorem now supplies the feedback probability and cutoff-matched
unconditional clocks for its explicit deterministic startup class.

The [12 October unistochastic obstruction](trace-bridge/unitary_two_step_obstruction.md)
(TRACE-074) constructs genuine unitary intensities with logarithmic
two-step peaks despite logarithmic flatness and a vanishing centered
singular norm. Its correct higher-step estimate explains why three-step
mixing does not supply the entry bracket's two-step kernel.
No maintained trajectory or BGS counterexample is asserted.

[TRACE-075](trace-bridge/two_step_restoring_drift.md) supplies a positive
companion: the exact one-step phase average has a restoring drift
controlled by a complete three-step path-swap bound. At the constructed
peaks, its mean decrement is asymptotic to \(K_{ij}/u\). Concentration and joint persistence are supplied separately by TRACE-079/080
on their explicit startup/cutoff regime; a deterministic microscopic
identification is still not obtained.

The [reviewed Schur continuation](../archive/record/cavity_continuation_20261011.md)
strengthens [TRACE-060](trace-bridge/all_moment_delay_bootstrap.md) to all fixed
killed clock upper bounds and [uniform equality laws at every fixed order](trace-bridge/conditional_clock_universality.md)
at the log^(1+kappa) cutoff. The [full-depth clock measure](trace-bridge/full_depth_clock_measure.md)
includes its exact reference atom, matched by a pathwise finite-rank lower bound. [TRACE-073](trace-bridge/schur_censoring_gap.md) proves
ordered classical/general-contraction singular-value bounds and conditional
intensity/reversal gap propagation at log^(3+kappa). The maintained deterministic
startup now receives the TRACE-080 probability and cutoff-matched
applications at log^(4+kappa). The scalar microscopic law remains open.

## Maximal paths and source continuation, 11 October 2026

[TRACE-071](trace-bridge/laplace_path_transport.md) transports the entire centered
phase-ensemble local point-process path and every fixed normal-source product.
[TRACE-072](trace-bridge/deterministic_path_transport.md) gives the deterministic
maximal time-average bound and the actual-map growing interval. The initial
local law remains unidentified. [The complete disposition](../archive/record/chat_integration_20261011.md)
also indexes reconstructed physical-source covariance, conditional joint delays,
clock obstructions, signed finite-field collisions and frozen circular laws.


## Reviewed phase-memory and sharp-jet continuation, 8 October 2026

[The research checkpoint](../archive/record/research_checkpoint_20261008.md) reconstructs
TRACE-053's max-entry channel and explicit averaged-pinching rate, proves
TRACE-054's optimal 4/3 matrix inner jet bound with localization correction,
and proves TRACE-056's direct real-flow absorbed scalar L1 comparison.
TRACE-055's submitted polylogarithmic deep-source hierarchy remains
verification-pending. Scalar cavity identification, signed undamped/high-switch
comparison, every-fixed-order TRACE-005 and deterministic BGS remain OPEN.


## Reviewed phase checkpoint, 7 October 2026

[The checked checkpoint](../record/checked_research_checkpoint_20261007.md)
strengthens the current pair residual to checksum-free low-switch removal and
adds independently reviewed Schur/source reductions, literal fixed-word laws,
actual radial/resolvent control and ordinary-body coercivity. The exact
remaining pair tasks are the complete balanced microscopic law and signed
undamped high-switch offcharge endpoint; higher factorial TRACE-005 and BGS
remain open. [Exact scopes](trace-bridge/phase_trace_checkpoint.md) distinguish
accepted proofs, source corrections, changed-family obstructions and deferred
candidates. Main publication follows aggregate checks and fresh review.

This is the current reading index, not a second status authority. [The claim ledger](../record/claim_ledger.md) controls scientific status; [exact proof topics](topics/README.md) retain every canonical source path. The [corpus revision](../archive/record/corpus_revision_20261006.md) distinguishes inventory, internal proof review, source checks and finite execution.

**Deterministic BGS and TRACE-005 remain open.** The scoped corpus revision passed remote acceptance; research proceeds with its named conditional boundaries preserved.

## Fixed deterministic map

The exact odd-dimensional frozen propagator uses fixed tau=10^(-80), the corrected ordinary Weyl symbol, and explicit exceptional dimensions. Structural and algebraic results do not themselves control Heisenberg traces. [Position mixing](fixed-map/position_chain_mixing.md) now controls the cyclic path contribution and a specified marked three-link contraction; [reversal decay](fixed-map/reversed_path_decay.md) controls the reverse-cyclic family. These do not bound the complete signed noncyclic remainder.

[Theorems, reading path and complete sources](topics/fixed-map/README.md).

[Conditional loop tests and normalized logarithmic deletion](../supplement/fixed_map/resolvent-flow/loop_test_reductions.md) reduce the required tests and remove short legs at relative error O(N^(-1/40) log N). The actual signed long-long target and all-order mixed hierarchy remain open.

**Boundary:** Actual signed deterministic noise removal and all-order Heisenberg comparison remain open.

## Trace identities and microscopic limits

Exact factorial partition identities connect local correlations to complete signed Fourier sums. A sufficient absolute estimate is different from the attainable deterministic target.

[Theorems, reading path and complete sources](topics/trace-bridge/README.md).

**Boundary:** The actual TRACE-005 estimate is open. Pair control alone does not imply every higher factorial correlation.

## Cayley arithmetic and finite-field geometry

Finite-field pair keys, energy reductions, curve bounds, resultant support and arithmetic trace laws form a separate programme. Each proof retains its prime, subgroup-size and noncentral-row restrictions.

[Theorems, reading path and complete sources](topics/cayley-arithmetic/README.md).

**Boundary:** The sparse centered K^(2+o(1)) energy target remains open. Arithmetic averaging is not a fixed-matrix microscopic law.

## Arithmetic return laws

Recurrence, parity and return-law theorems apply at their stated arithmetic subsequences, regularity and perturbation scales. A global return law does not determine unfolded local statistics.

[Theorems, reading path and complete sources](topics/returns/README.md).

**Boundary:** Heisenberg-scale fixed-strength universality and identification of actual conditional local limits are not consequences of these return laws.

## Pell, echoes and harmonic transitions

Pell arithmetic produces exact recurrence structures and controlled perturbative models. Quantum kick amplitude and classical coupling must be distinguished in every theorem.

[Theorems, reading path and complete sources](topics/pell/README.md).

**Boundary:** Fixed classical strength, growing replicas and complete local-law transfer remain separate obligations.

## Resonance, cohomology and regularity

The corpus separates oriented and signed frequency orbits, finite support from infinite orbit families, and linear transport from the nonlinear frozen dynamics.

[Theorems, reading path and complete sources](topics/resonance-cohomology/README.md).

**Boundary:** The all-members analytic nonlinear resonance question remains open; finite certificates do not prove unrestricted analytic limits.

## Locality and Fourier tails

Locality estimates specify the symbol class, approximation budget, coupling and time range. They cannot be extended to Heisenberg time by naming a semiclassical limit.

[Theorems, reading path and complete sources](topics/locality/README.md).

**Boundary:** These estimates do not supply the missing full signed spectral hierarchy.

## Spectral obstruction tests

[Microscopic rounding](spectral-obstructions/microscopic_rounding_control.md) preserves the whole unnormalized trace vector through each specified K_N=o(N^(1/3)) and coarse position/reversal/Egorov controls, yet violates a fixed stable-band pair target. It refines prior project rounding by changing the operator; exact quantization and subprincipal data are outside its scope.

Negative controls reject specific invalid implications. [TRACE-014](spectral-obstructions/isospectral_clock_moment_control.md) gives a same-ensemble clock spectrum whose induced-HS moment channels approach Haar uniformly in all orders. An abstract spectrum is not automatically a quantization of the actual chaotic map.

[Theorems, reading path and complete sources](topics/spectral-obstructions/README.md).

**Boundary:** A failed shortcut does not refute BGS. Retain the strongest positive statement that survives each witness.

## Identifiability and information theory

These are separate mathematical applications. Observation model, photon-moment constraint, aperture, rank and measurement access determine the conclusion.

[Theorems, reading path and complete sources](topics/information-theory/README.md).

**Boundary:** The full vanishing-noise moment-class transition remains open. These results do not establish BGS.

## Foundations and conventions

Use the current source-of-truth hierarchy and corrected Weyl conventions. Historical exposition is useful context, not an authority that overrides later corrections.

[Theorems, reading path and complete sources](topics/foundations/README.md).

**Boundary:** Read exact assumptions and recorded corrections before transporting an old argument into a maintained proof.

## Previous chronological catalogue

The previous catalogue is retained byte-for-byte in [the dated snapshot](../archive/history/2026/corpus_revision_20261006/mathematics__results.md.txt). Its dated open/closed statements must be read against the current ledger. No proof or execution evidence was deleted during this editorial separation.

<!-- Stable fragment targets retained from the pre-revision reader entry. -->
<a id="current-results-and-exact-scope"></a>
<a id="original-ordered-two-pair-microscopic-mass-6-october-2026"></a>
<a id="uniform-two-copy-collective-diffusion-6-october-2026"></a>
<a id="actual-weyl-transfer-and-common-noise-invariants-6-october-2026"></a>
<a id="exact-pair-heat-and-actual-start-smoothing-5-october-2026"></a>
<a id="actual-growing-projection-and-a-particular-local-inverse-boundary-5-october-2026"></a>
<a id="critical-noise-and-actual-fixed-degree-projections-5-october-2026"></a>
<a id="all-fixed-correlation-orders-for-the-original-random-chain-5-october-2026"></a>
<a id="exact-noise-defect-and-transfer-boundaries-5-october-2026"></a>
<a id="actual-start-comparison-and-logarithmic-regularity-4-october-2026"></a>
<a id="polynomial-original-coboundary-limit-4-october-2026"></a>
<a id="fixed-time-trace-closure-and-expansionmemory-boundary-4-october-2026"></a>
<a id="projected-square-control-and-block-crowding-1-october-2026"></a>
<a id="resonant-density-mechanism-and-its-critical-boundary-1-october-2026"></a>
<a id="absolute-obstruction-and-signed-cubic-continuation-30-september-2026"></a>
<a id="prime-resonant-sector-audit-30-september-2026"></a>
<a id="heisenberg-note-completions-30-september-2026"></a>
<a id="simultaneous-random-kick-limit-30-september-2026"></a>
<a id="actual-coboundary-steps-and-möbius-reduction-29-september-2026"></a>
<a id="quadratic-noise-dynamics-29-september-2026"></a>
<a id="quadratic-noise-mechanism-and-exact-boundaries-28-september-2026"></a>
<a id="all-time-periodic-point-arithmetic-and-upload-audit-27-september-2026"></a>
<a id="singular-cue-benchmark-and-coboundary-spectral-flow-25-september-2026"></a>
<a id="seven-cut-smooth-transfer-and-two-clock-gram-falsifier-25-september-2026"></a>
<a id="pair-resolvent-universal-abel-floor-and-spectral-flow-audit-25-september-2026"></a>
<a id="arithmetic-returns-and-effective-submicroscopic-gap-24-september-2026"></a>
<a id="exact-fixed-coupling-seven-cut-and-algebraic-bounds-24-september-2026"></a>
<a id="nonlinear-classical-pressure-boundary-23-september-2026"></a>
<a id="full-lag-gap-and-exact-generator-rank-23-september-2026"></a>
<a id="clustered-abel-transform-and-positive-time-windows-22-september-2026"></a>
<a id="smooth-finite-orbit-rigidity-22-september-2026"></a>
<a id="fixed-map-continuation-21-september-2026"></a>
<a id="fixed-family-reductions-20-september-2026"></a>
<a id="recovered-finite-window-result-and-scope-corrections"></a>
<a id="short-returns-and-ergodic-local-limits"></a>
<a id="general-hyperbolic-return-laws-and-sharp-regularity"></a>
<a id="harmonic-scale-laws-of-the-actual-kicked-return-propagator"></a>
<a id="harmonic-scale-transition-in-the-fixed-pell-cat-map"></a>
<a id="september-9-full-cayley--jacobi-trace-gaussian-limit"></a>
<a id="1-pair-key--fourth-moment-reduction--exact"></a>
<a id="2-cayley-additive-energy-reduction--exact"></a>
<a id="3-best-uniform-pointwise-theorem--exact--external-theorem"></a>
<a id="4-fixed-product-rows--exact"></a>
<a id="5-exact-maximal-real-order-three-support--exact--external-theorem"></a>
<a id="6-characteristic-zero-trace-intercept-rigidity--exact--external-theorem"></a>
<a id="7-cyclotomic-unit-matching-and-general-scalar-support--exact"></a>
<a id="8-inverse-row-reflection--exact"></a>
<a id="9-inverse-pair-sum-perfect-square--exact"></a>
<a id="10-inverse-pair-sums-are-a-translated-half-degree-resultant--exact"></a>
<a id="11-square-collision-resultants-and-canonical-discriminants--exact"></a>
<a id="12-global-split-prime-mass-and-averaged-theorems--exact--external-theorem"></a>
<a id="13-frobenius-amplification-in-minimal-finite-extensions--exact"></a>
<a id="14-full-cayleyjacobi-trace-identity--exact"></a>
<a id="15-corrected-offoff-elliptic-theorem--exact--external-theorem"></a>
<a id="16-exact-trace-to-local-statistics-bridge--exact"></a>
<a id="17-verification-and-adversarial-controls"></a>
<a id="18-current-frontier--open"></a>
<a id="magnetic-quotient-restricted-global-law-2026-09-05"></a>
<a id="pell-floquet-normal-form-and-recurrence-spectrum-2026-09-05"></a>
<a id="compact-test-microscopic-obstruction-in-the-pell-family"></a>

## Current algebraic and selected-family frontier

The actual pair commutant is classified for odd N>=3 with the exact N=7
exception ([FM-024](fixed-map/actual_seven_primary_commutant.md)); its 7∤N leaf
now has fresh independent review. [FM-025](fixed-map/uniform_five_cluster_simplicity.md)
gives the pure-five kick family, while [FM-026](fixed-map/literal_time_multiplicity_bounds.md)
gives literal-time multiplicity<=7 and precise simple-eigenvalue counts on
N=7*5^e. Finite U-simplicity cases remain explicitly bounded. The
[FM-010 companion](fixed-map/uniform_trace_square_transcendence.md) concerns
one-step squared traces for odd N>=3,N!=7.

[TRACE-019](fixed-map/selected_weighted_coefficient.md) controls a selected
full-weight WKB family. Separately, [TRACE-020](fixed-map/factorial_ordered_diagonal.md)
removes the specified ordered-diagonal sector from every fixed-order factorial
Fourier expression at O_k(log^(2k)N/N), using actual entrywise flatness alone.
Its collective and exponential long-cycle companions have distinct bounds;
none is identified with WKB path masks.
[TRACE-021](fixed-map/hamming_low_switch_residual.md) removes disjoint balanced
and off-charge Hamming sectors plus a high-Hamming low-switch family from the
actual pair trace, with exponentially small error. One explicit signed
residual projector remains unestimated; this does not settle higher orders.
The exact signed complement, plateau/torsion mechanism and higher factorial
hierarchy remain open; no BGS conclusion follows.

[Earlier detailed checkpoints](../archive/history/2026/cohesive_frontier_20261006/prior_results_tail.txt)
retain component provenance; current statements are the linked theorem owners.


## Reviewed Wave2 bounded theorem family

[TRACE-024](fixed-map/actual_one_pinch_disappearance.md): actual unmasked one-pinch disappearance (bounded positive/smooth signed weights, no rate). [FM-031](fixed-map/ordinary_compact_stratum_centering.md): a.e. ordinary centering and fixed-N complete signed-source cutoff. [TRACE-025](fixed-map/rounding_simple_spectrum_endpoint_barriers.md): changed-family endpoint barriers with a separating-estimate restriction. [TRACE-026](fixed-map/hook_tree_phase_current_reduction.md): corrected exact finite hook/tree/current identities and conditional Abel reduction. [Phase source audit](../literature/wave2_phase_orbit_source_qualification_20261007.md) adds no universality/priority theorem. Masked T16, balanced law, TRACE-005 and BGS remain OPEN.


## Reviewed weighted coherence covariance

[TRACE-027](fixed-map/weighted_phase_coherence_covariance.md): exact finite covariance, nontrivial Green–Kubo term, complete signed Ward upper-half slow-window law, and actual degree-two mixed-moment exception removal. No microscopic Ward (13) or all-fixed-degree CUE identification.


## Reviewed complete unmasked pinch continuation

[TRACE-028](fixed-map/right_frame_unmasked_pinch_hierarchy.md) closes actual/annealed complete separated averages and the all-z unmasked convex hierarchy through a new centered S3 tail. [TRACE-029](fixed-map/convex_pinch_weak_noise_and_deconvolution.md) gives exact finite-N resummation bounds, bounded-u signed weak-noise stability and the sharp actual unsigned large-log deconvolution obstruction. Identity cancellation and all mask/extraction/zero-insertion limits remain explicit.


[Deleted-clock Hardy boundary](trace-bridge/deleted_clock_hardy_boundary.md): an exact positive excess of order 1/N can vanish despite bounded fixed traces.

<!-- BEGIN GENERATED: registered family tables (render_status.py). Do not edit this section by hand. -->

## Registered theorem families (generated)

This closing section is generated from `../record/claims.json`
by `../computations/maintenance/render_status.py`; the analytical
text above it is hand-written and preserved. Registered status is
controlled by claims.json; the complete per-claim surface, with
boundaries and closure conditions, is the generated
[claim registry](../record/claim_registry.md).

**331 registered claims: 266 proved, 15 verification-pending, 19 conditional, 30 open, 1 refuted.**

### BGS family (1 claim)

| Claim | State | Title |
|---|---|---|
| `BGS-BGS-001` | **OPEN** | Fixed-strength microscopic BGS universality for the maintained frozen map |

### CAYLEY family (11 claims)

| Claim | State | Title |
|---|---|---|
| `BGS-CAYLEY-001` | **PROVED** | Pair-key and fourth-moment reduction |
| `BGS-CAYLEY-002` | **PROVED** | Cayley additive-energy reduction |
| `BGS-CAYLEY-003` | **VERIFICATION-PENDING** | Direct K^(8/3) Cayley energy bound in the explicit subgroup-size range |
| `BGS-CAYLEY-004` | **PROVED** | Uniform subgroup-curve Cayley energy bound |
| `BGS-CAYLEY-005` | **OPEN** | Sharp centered pointwise Cayley energy target |
| `BGS-CAYLEY-006` | **PROVED** | Pointwise sparse and density Gaussian limits of the full Cayley-Jacobi trace |
| `BGS-CAYLEY-007` | **PROVED** | Three-scalar exact split support for fixed-degree Cayley row intersections |
| `BGS-CAYLEY-008` | **PROVED** | Scaling rigidity of the Cayley collision family |
| `BGS-CAYLEY-009` | **PROVED** | Quantitative magnetic-quotient moment bound and global semicircle law |
| `BGS-CAYLEY-010` | **PROVED** | Uniform parity sector for exact finite spectra of arbitrary hyperbolic matrices |
| `BGS-CAYLEY-011` | **PROVED** | Exact difference energy of Fibonacci/Lucas ratios (finite residue certified; general case conditional on Carmichael's primitive-divisor theorem) |

### CUE family (2 claims)

| Claim | State | Title |
|---|---|---|
| `BGS-CUE-001` | **PROVED** | Stable singular pair energy in Haar CUE and weak-local obstruction |
| `BGS-CUE-002` | **PROVED** | All-positive-frequency CUE trace-square covariance and exact coupling derivative |

### FLOW family (25 claims)

| Claim | State | Title |
|---|---|---|
| `BGS-FLOW-001` | **PROVED** | Uniform finite coboundary eigenphase-flow bound and sharpness sequence |
| `BGS-FLOW-002` | **PROVED** | Coboundary kicks have sine curvature but no infinitesimal Dyson diffusion |
| `BGS-FLOW-003` | **PROVED** | Quadratic coboundary covariance, ellipticity, corrected Dyson generator and transfer boundaries |
| `BGS-FLOW-004` | **PROVED** | Quantitative raw-noise/Dyson coupling and phase-averaged local transfer |
| `BGS-FLOW-005` | **PROVED** | Haar-reversible drift, gradient identity and short-time path total variation |
| `BGS-FLOW-006` | **PROVED** | Raw and reversible fixed-trace OU limits and fixed-time coupling obstruction |
| `BGS-FLOW-007` | **PROVED** | Clock-to-Sine local limit for quadratic noise and obstruction to generic noise removal |
| `BGS-FLOW-008` | **PROVED** | Exact fourth-order drift of Gaussian coboundary steps |
| `BGS-FLOW-009` | **PROVED** | Mobius spectral reduction and iterated clock-to-Sine limit for uncentered coboundary kicks |
| `BGS-FLOW-010` | **PROVED** | Dimension-quantitative simultaneous clock-to-Sine limit for uncentered Gaussian coboundary kicks |
| `BGS-FLOW-011` | **PROVED** | Polynomial-step original Gaussian coboundary joint limit with dimension-uniform derivatives |
| `BGS-FLOW-012` | **PROVED** | Polynomial original-coboundary comparison preserving bounded-trace initial data |
| `BGS-FLOW-013` | **PROVED** | Prescribed-time empty Dyson limits from globally uniform bounded-trace simple spectra |
| `BGS-FLOW-014` | **PROVED** | Gap-independent circular Dyson relaxation and original-chain Sine_2 from the actual frozen start |
| `BGS-FLOW-015` | **PROVED** | Exact microscopic noise defect, flat heat jets and scoped stationarity, inversion and entropy boundaries |
| `BGS-FLOW-016` | **PROVED** | Local moment transport and all-order projected diffusion comparison at t^2 log N -> 0 |
| `BGS-FLOW-017` | **PROVED** | All fixed factorial orders and one-chain L2 signed CUE comparison for the actual-start original coboundary chain |
| `BGS-FLOW-018` | **PROVED** | Exact clock covariance, sharp signed pair relaxation and all-order critical noise law |
| `BGS-FLOW-019` | **PROVED** | Actual fixed-degree neutral projections: vanishing heat defects and projected compact CUE rate |
| `BGS-FLOW-020` | **PROVED** | Growing neutral degree, actual logarithmic projection rate and fixed local pair heat-inverse obstruction |
| `BGS-FLOW-021` | **PROVED** | Exact stable Heisenberg pair heat compensation and actual-start superpolynomial smoothed form factor |
| `BGS-FLOW-022` | **PROVED** | Critical resonance law for the kicked Pell propagator |
| `BGS-FLOW-023` | **PROVED** | Second-order critical law for coboundary kicks of a fixed cat map |
| `BGS-FLOW-024` | **PROVED** | Negative microscopic consequences at the second-order coboundary scale |
| `BGS-FLOW-025` | **PROVED** | Obstruction and necessary kick scale for the kicked Pell family |

### FM family (37 claims)

| Claim | State | Title |
|---|---|---|
| `BGS-FM-001` | **PROVED** | Frozen-model classical symmetry theorem |
| `BGS-FM-002` | **PROVED** | Odd-Pell full-symbol Gaussian crossover |
| `BGS-FM-003` | **PROVED** | Fixed-map moment controls, falsifier, and perturbation transfer |
| `BGS-FM-004` | **CONDITIONAL** | Three-orientation mixed-resolvent lower barrier |
| `BGS-FM-005` | **PROVED** | Actual frozen-kick Jacobi decomposition and exact low-rank obstruction |
| `BGS-FM-006` | **PROVED** | Nonlinear bracket pressure growth and frozen-map linear-normalization boundary |
| `BGS-FM-007` | **PROVED** | Exact seven-cut frozen-generator reduction and microscopic trace-norm stability |
| `BGS-FM-008` | **PROVED** | Total nonvanishing of frozen metaplectic minors and qualitative fixed-time spectral simplicity |
| `BGS-FM-009` | **PROVED** | Exact commutator-cube obstruction to common antiunitary reversal |
| `BGS-FM-010` | **PROVED** | Nonvanishing of every fixed-model power trace and classification of scalar returns |
| `BGS-FM-011` | **PROVED** | Effective but submicroscopic eigenphase gap floor at the frozen algebraic coupling |
| `BGS-FM-012` | **PROVED** | Exact all-time periodic-point grids and physical-symbol averages for the fixed linear cat |
| `BGS-FM-013` | **PROVED** | Bounded fixed-time traces for the unchanged odd-dimensional frozen map |
| `BGS-FM-014` | **PROVED** | Uniform finite type and scalar cancellation for translated physical-symbol differences |
| `BGS-FM-015` | **PROVED** | Explicit classical commutator generating action at the maintained fixed coupling |
| `BGS-FM-016` | **PROVED** | Egorov overlap rigidity and actual fixed-power separation from affine quantizations |
| `BGS-FM-017` | **PROVED** | Logarithmic initial Poisson regularity, local heat-phase saddles and unweighted vertical tails |
| `BGS-FM-018` | **PROVED** | Actual Weyl-frequency coercivity, regularized singular gap and exact common-noise two-copy invariant space |
| `BGS-FM-019` | **PROVED** | Uniform two-copy collective diffusion gap and refined common-noise Heisenberg mass |
| `BGS-FM-020` | **PROVED** | Original ordered two-pair Heisenberg-dominating singular mass |
| `BGS-FM-021` | **PROVED** | Fixed-map position-chain singular mixing, cyclic ramp and marked three-link cancellation |
| `BGS-FM-022` | **PROVED** | Fixed-map reversed-coordinate-path norm decay and reverse-cyclic suppression |
| `BGS-FM-023` | **PROVED** | Quantitative exclusion of bounded-power arithmetic translation algebras |
| `BGS-FM-024` | **PROVED** | Actual scalar joint commutant in every odd dimension except seven |
| `BGS-FM-025` | **PROVED** | Uniform actual kick simplicity on the pure five-primary seven family |
| `BGS-FM-026` | **PROVED** | Literal-time multiplicity and simple-eigenvalue counts on N=7*5^e |
| `BGS-FM-027` | **PROVED** | Uniform actual one-step cyclic-charge gap |
| `BGS-FM-028` | **PROVED** | Actual q1 theta0 charge-pinching radial shell and resolvent |
| `BGS-FM-029` | **PROVED** | Literal kick/cat moment laws, triple-log word window and strong-freeness obstruction |
| `BGS-FM-030` | **PROVED** | Global scalar and block body coercivity with real absorption |
| `BGS-FM-031` | **PROVED** | Ordinary compact-stratum centering and effective fixed-N source cutoff |
| `BGS-FM-032` | **PROVED** | Prime cyclic cohomology and parity-resolved susceptibility |
| `BGS-FM-033` | **CONDITIONAL** | All-label-scale one-step Weyl overlap and prime-orbit corollaries |
| `BGS-FM-034` | **PROVED** | Fixed-strength all-orders comparison for the single-exponential coboundary kick |
| `BGS-FM-035` | **PROVED** | Classical interpretation of the fixed-strength quantized map |
| `BGS-FM-036` | **PROVED** | Microscopic stability along Pell moduli: K clusters and spacing collapse |
| `BGS-FM-037` | **PROVED** | Finite torus level sets and branch scales at p=199 (Q = a²-ab-b², cyclic action of order 11) |

### FORMAL family (3 claims)

| Claim | State | Title |
|---|---|---|
| `BGS-FORMAL-001` | **PROVED** | Active Lean graph: finite kernels and scoped Mathlib theorems |
| `BGS-FORMAL-002` | **PROVED** | Bounded rank-two four-cut executable certificate |
| `BGS-FORMAL-003` | **PROVED** | Compiled seven-primary finite GF(5) array certificate |

### FUP family (1 claim)

| Claim | State | Title |
|---|---|---|
| `BGS-FUP-001` | **PROVED** | Parity classification of Fourier FUP for ideal off-diagonal digit alphabets |

### INFO family (1 claim)

| Claim | State | Title |
|---|---|---|
| `BGS-INFO-001` | **OPEN** | Full vanishing-noise tomography transition |

### LOOP family (1 claim)

| Claim | State | Title |
|---|---|---|
| `BGS-LOOP-001` | **CONDITIONAL** | Full mixed loop hierarchy implies target compact anchored correlations |

### RES family (23 claims)

| Claim | State | Title |
|---|---|---|
| `BGS-RES-001` | **PROVED** | Sharp Fourier-line resonance coercivity |
| `BGS-RES-002` | **PROVED** | Local-jet resonance obstruction |
| `BGS-RES-003` | **OPEN** | All-members analytic resonance nondegeneracy |
| `BGS-RES-004` | **PROVED** | Smooth finite-orbit Poisson-bracket lag independence |
| `BGS-RES-005` | **PROVED** | Full-lag uniform classical Riesz gap for the frozen physical symbol under linear transport |
| `BGS-RES-006` | **PROVED** | Exact adjoint-resolvent representation and pair-Abel equivalence |
| `BGS-RES-007` | **PROVED** | Smooth scalar-resolvent transfer between the original and seven-cut full propagators |
| `BGS-RES-008` | **PROVED** | Sharp resonance minimum on a hyperbolic Fourier orbit |
| `BGS-RES-009` | **PROVED** | Uniform spectral positivity and temporal Riesz bounds for the spectral module |
| `BGS-RES-010` | **PROVED** | Root-circle classification of high-lag coercivity |
| `BGS-RES-011` | **PROVED** | Complete finite-symbol high-lag criterion |
| `BGS-RES-012` | **PROVED** | Cyclic module and variance at every time in the finite quantum module |
| `BGS-RES-013` | **PROVED** | Balanced-phase completion and even-order phase-rank transition |
| `BGS-RES-014` | **CONDITIONAL** | Full Riesz criterion for the two-variable resonance lattice |
| `BGS-RES-015` | **PROVED** | Two-window phase crossover: rectangular Gram lower edge |
| `BGS-RES-016` | **PROVED** | Sharp multiradius and concentric-sphere polynomial rigidity |
| `BGS-RES-017` | **PROVED** | Balanced phase and quantum controllability for odd N |
| `BGS-RES-018` | **PROVED** | Infinite-orbit independence and entire temporal all-pass gauges |
| `BGS-RES-019` | **PROVED** | Explicit weighted-Wiener stability of the isolated resonance mode |
| `BGS-RES-020` | **PROVED** | Generic weighted-Wiener nondegeneracy |
| `BGS-RES-021` | **PROVED** | Analytic rigidity of zero resonance mechanisms |
| `BGS-RES-022` | **VERIFICATION-PENDING** | Radius-eight resonance nondegeneracy (ND.3) |
| `BGS-RES-023` | **PROVED** | Constructive margin for the radius-eight certificate (ND.10): explicit constant pi^2/41472 * 2^(-2^715) |

### RET family (4 claims)

| Claim | State | Title |
|---|---|---|
| `BGS-RET-001` | **PROVED** | Harmonic return law for the actual kicked Pell propagator |
| `BGS-RET-002` | **PROVED** | Harmonic-scale global transition in the fixed Pell cat map |
| `BGS-RET-003` | **CONDITIONAL** | Noncommuting return words: all-orders quantum conjugacy under the exact return identity |
| `BGS-RET-004` | **PROVED** | Explicit return-word example: certified disjoint tower and nonzero bracket with Gamma_T(g)=0 |

### TRACE family (222 claims)

| Claim | State | Title |
|---|---|---|
| `BGS-TRACE-001` | **PROVED** | Partition-Mobius formula for distinct-index spectral sums |
| `BGS-TRACE-002` | **PROVED** | Exact Fourier trace representation of microscopic factorial statistics |
| `BGS-TRACE-003` | **PROVED** | Weighted Heisenberg-scale joint-trace comparison is sufficient for band-limited microscopic RMT correlations |
| `BGS-TRACE-004` | **PROVED** | Every-compact-bandwidth comparison extends to Schwartz correlation tests |
| `BGS-TRACE-005` | **OPEN** | Model-specific signed Heisenberg-scale desymmetrized joint-trace estimate |
| `BGS-TRACE-006` | **PROVED** | Clustered Abel lower bound and simple-spectrum Heisenberg-window falsifier |
| `BGS-TRACE-007` | **PROVED** | Universal sharp Abel lower bound attained by the clock spectrum |
| `BGS-TRACE-008` | **PROVED** | Two-clock falsifier for sufficiency of the CUE Gram second moment |
| `BGS-TRACE-009` | **PROVED** | Prime-resonant sector mass criterion, exact spectral comb and coherent-mode obstruction |
| `BGS-TRACE-010` | **PROVED** | Universal deterministic absolute-norm obstruction against CUE and signed cancellation controls |
| `BGS-TRACE-011` | **PROVED** | Resonant cubic deletion by local density and a pair-compatible critical cluster obstruction |
| `BGS-TRACE-012` | **PROVED** | Folded-square signed resonant cubic control, explicit root allocation and factorial block-crowding obstruction |
| `BGS-TRACE-013` | **PROVED** | Arithmetic coherent words despite uniform auxiliary quantum expansion and exact spectral exclusions |
| `BGS-TRACE-014` | **PROVED** | All-order Haar moment-channel proximity with a rigid isospectral clock spectrum |
| `BGS-TRACE-015` | **PROVED** | Once-counted distinct-port three-block signed Heisenberg cancellation |
| `BGS-TRACE-016` | **PROVED** | Once-counted reduced distinct-port four-block signed cancellation |
| `BGS-TRACE-017` | **PROVED** | Actual fixed-order WKB instantiation of the complete factorial trace reduction |
| `BGS-TRACE-018` | **PROVED** | Actual winding-defect localization and phase-only Frostman averages |
| `BGS-TRACE-019` | **PROVED** | Full-weight selected homoclinic coefficient and cyclic-family bound |
| `BGS-TRACE-020` | **PROVED** | Ordered-diagonal factorial sector and scoped collective trace reductions |
| `BGS-TRACE-021` | **PROVED** | Disjoint Hamming and low-switch pair residual reduction |
| `BGS-TRACE-022` | **PROVED** | Exact full balanced-pair Schur energy and three-radius equivalence |
| `BGS-TRACE-023` | **PROVED** | Completed compact pair source and uniform complex microscopic source bounds |
| `BGS-TRACE-024` | **PROVED** | Actual unmasked occupation-subtracted q1 one-pinch disappearance |
| `BGS-TRACE-025` | **PROVED** | Changed-family rounded and simple-spectrum signed endpoint barriers |
| `BGS-TRACE-026` | **PROVED** | Corrected hook-cycle cancellation, Eulerian trees and phase-current reduction |
| `BGS-TRACE-027` | **PROVED** | Weighted phase coherence, classical covariance and upper-half slow-window signed Ward law |
| `BGS-TRACE-028` | **PROVED** | Actual right frame, separated compositions and complete unmasked convex pinch hierarchy |
| `BGS-TRACE-029` | **PROVED** | Complete convex weak-noise stability and actual unsigned logarithmic deconvolution obstruction |
| `BGS-TRACE-053` | **PROVED** | Max-entry phase memory and averaged eigenbasis pinching |
| `BGS-TRACE-054` | **PROVED** | Optimal right-weighted second jets of rational matrix inner functions |
| `BGS-TRACE-055` | **VERIFICATION-PENDING** | Submitted actual polylogarithmic deep-source hierarchy |
| `BGS-TRACE-056` | **PROVED** | Direct normally absorbed scalar-source transport along a real unitary flow |
| `BGS-TRACE-057` | **PROVED** | Arbitrary-source phase covariance |
| `BGS-TRACE-058` | **PROVED** | Integrable all-order phase absorption |
| `BGS-TRACE-059` | **PROVED** | Anisotropic physical-source transport |
| `BGS-TRACE-060` | **CONDITIONAL** | All fixed conditional clock powers, full-depth measure and exact rank atom |
| `BGS-TRACE-061` | **PROVED** | Finite frame identities, Stiefel threshold and clock-basis obstruction |
| `BGS-TRACE-062` | **PROVED** | Flat completion with arbitrary clock law |
| `BGS-TRACE-063` | **PROVED** | Global noncommuting ordinary-body coercivity |
| `BGS-TRACE-064` | **PROVED** | Sharp maximal-torus contraction for compact simple groups |
| `BGS-TRACE-065` | **PROVED** | Signed finite-field cycle and collision calculus |
| `BGS-TRACE-066` | **PROVED** | Birthday rank law and thinned collision limit |
| `BGS-TRACE-067` | **PROVED** | Sharp balanced Laurent Jack coefficient bound |
| `BGS-TRACE-068` | **PROVED** | Frozen circular phase laws in the three symmetry classes |
| `BGS-TRACE-069` | **PROVED** | All-order critical CSE trace limit |
| `BGS-TRACE-070` | **PROVED** | Complete CUE and CSE form-factor curves |
| `BGS-TRACE-071` | **PROVED** | Maximal phase point-process paths and all fixed normal-source products |
| `BGS-TRACE-072` | **PROVED** | Deterministic maximal microscopic observable flow |
| `BGS-TRACE-073` | **CONDITIONAL** | Singular-spectrum censoring and stopped intensity/reversal gap propagation |
| `BGS-TRACE-074` | **PROVED** | Unistochastic two-step obstruction and the correct higher-step singular bound |
| `BGS-TRACE-075` | **PROVED** | Fresh-phase two-step restoring drift from a complete three-step path-swap bound |
| `BGS-TRACE-076` | **PROVED** | Exact Haar feedback delay law and unconditional entropy-stable full-depth clocks |
| `BGS-TRACE-077` | **PROVED** | Green compression and shrinking intensity gaps on the entry-stopped prefix |
| `BGS-TRACE-078` | **PROVED** | Uniform-port second moment of the complete two-step feedback increment |
| `BGS-TRACE-079` | **PROVED** | Simultaneous all-pair stopped two-step concentration |
| `BGS-TRACE-080` | **PROVED** | Unconditional deterministic-start feedback flatness and fixed-order clock laws |
| `BGS-TRACE-081` | **PROVED** | Perfect intensity mixing, small reversal and simple spectrum do not identify microscopic statistics |
| `BGS-TRACE-082` | **PROVED** | Exact coherence return memory and universal singular-norm plateau before dimension time |
| `BGS-TRACE-083` | **PROVED** | Observed first-return pulses and cyclic coherence survive perfect intensity mixing |
| `BGS-TRACE-084` | **PROVED** | Mesoscopic block number-variance criterion and collective trace-energy boundary |
| `BGS-TRACE-085` | **PROVED** | Exact root lifting and failure of necessity for resonance-sector deletion |
| `BGS-TRACE-086` | **PROVED** | All-order signed diagonal hierarchy implies local Sine2 and local moment UI |
| `BGS-TRACE-087` | **PROVED** | Exact parameter bandwidth and quantitative de-averaging to a fixed coupling |
| `BGS-TRACE-088` | **PROVED** | Rooted BEST count, extensive equal-edge mass and unitary compensation |
| `BGS-TRACE-089` | **PROVED** | Factorially weighted square-root-time equal-edge collision crossover |
| `BGS-TRACE-090` | **PROVED** | Contractive full-spectrum radial ratios and mixed-moment weak-process criterion |
| `BGS-TRACE-091` | **PROVED** | Sharp clock minimum and exact radial and Abel Hardy remainders |
| `BGS-TRACE-092` | **PROVED** | Exact positive Abel decomposition and optimal square-root clock rigidity |
| `BGS-TRACE-093` | **PROVED** | Flat equal-edge Gaussian comparison, exact Heisenberg exponential rate and Wick collision mean |
| `BGS-TRACE-094` | **PROVED** | Heisenberg Wick collision Poisson law, exact flat ratio and geometric vertex occupations |
| `BGS-TRACE-095` | **CONDITIONAL** | Dimension-uniform deep feedback Gaussian limit |
| `BGS-TRACE-096` | **VERIFICATION-PENDING** | Exact transmission spectral averaging and bounded eigenvector ratio criterion |
| `BGS-TRACE-097` | **CONDITIONAL** | Conditional full positive Heisenberg path-current limit |
| `BGS-TRACE-098` | **VERIFICATION-PENDING** | Complete fixed-trace law and secular hierarchy for the symplectic phase ensemble |
| `BGS-TRACE-099` | **VERIFICATION-PENDING** | Polynomial trace windows in the auxiliary bilinear phase ensembles |
| `BGS-TRACE-100` | **VERIFICATION-PENDING** | Exact signed phase expansion and first two stable coefficient cancellations |
| `BGS-TRACE-101` | **VERIFICATION-PENDING** | Neutral peeling and finite primitive schemes at every fixed defect |
| `BGS-TRACE-102` | **VERIFICATION-PENDING** | Complete second-defect sector and full four-port open zero |
| `BGS-TRACE-103` | **VERIFICATION-PENDING** | All local-defect-one-or-two clusters: quartic exponential resummation |
| `BGS-TRACE-104` | **VERIFICATION-PENDING** | Local Cayley comparison with diagonal Cauchy disorder for an involution |
| `BGS-TRACE-105` | **VERIFICATION-PENDING** | Positive Cauchy projection self-duality with maximal matrix-law separation |
| `BGS-TRACE-106` | **PROVED** | Uniform physical-kick trace decay, positive-square exponent 1/9 and scalar-distance limit |
| `BGS-TRACE-107` | **PROVED** | Physical polynomial approximation at every fixed factorial order and exact Pell alias threshold |
| `BGS-TRACE-108` | **PROVED** | Quartic diagonal coordinate return with explicit fixed-coupling remainder |
| `BGS-TRACE-109` | **PROVED** | Inserted trace, quantum commutant projection and two-copy coboundary obstruction |
| `BGS-TRACE-110` | **PROVED** | Spectral orbit distance and exact scalar-root comparison lemmas |
| `BGS-TRACE-111` | **PROVED** | Full weighted Pell gradient, negative initial Hessian and forced early inflection |
| `BGS-TRACE-112` | **PROVED** | Uniform classical displacement density and independent logarithmic global spectral comparison |
| `BGS-TRACE-113` | **PROVED** | Uniform original-family power-trace bound from continuous Gaussian scalar and strict pressure gap |
| `BGS-TRACE-114` | **PROVED** | Balanced spectral rounding preserves polynomial short traces without a local law |
| `BGS-TRACE-115` | **PROVED** | Bounded microscopic stability and positive pair-energy comparison for unitary perturbations |
| `BGS-TRACE-116` | **PROVED** | Original-family compact pair test transfers through O(N^-2) matrix error |
| `BGS-TRACE-117` | **PROVED** | Kick-blind arithmetic spikes of the fixed cat map |
| `BGS-TRACE-118` | **PROVED** | Orbit-orthogonal kick at the Pell dimension u_203 |
| `BGS-TRACE-119` | **PROVED** | Positive-time trace expansion at the Pell dimension u_205 |
| `BGS-TRACE-120` | **PROVED** | Cat-map order governs the fixed-map Abel statistic |
| `BGS-TRACE-121` | **PROVED** | Cat-map order trichotomy for primes and prime powers |
| `BGS-TRACE-122` | **PROVED** | Chinese product for the cat-map trace square |
| `BGS-TRACE-123` | **PROVED** | Square-free products of at least three primes lie above 3/4 |
| `BGS-TRACE-124` | **PROVED** | Every odd modulus lies above 3/4 or below 5/7 |
| `BGS-TRACE-125` | **PROVED** | Uniform Pell-orbit overlap of the fixed symbol |
| `BGS-TRACE-126` | **PROVED** | Phase-averaged form factor and classical symmetry defects of the kicked cat map |
| `BGS-TRACE-127` | **PROVED** | Diagonal random-phase form factor of the cat map at times one, two and three |
| `BGS-TRACE-128` | **PROVED** | Short-time limits of the diagonal-phase form factor |
| `BGS-TRACE-129` | **PROVED** | Bessel form of the scalar-return orbit sum |
| `BGS-TRACE-130` | **PROVED** | Local antiunitary for a position-diagonal kick |
| `BGS-TRACE-131` | **PROVED** | Diagonal phase average for every hyperbolic cat map |
| `BGS-TRACE-132` | **PROVED** | Fixed-time limits for a general hyperbolic cat map |
| `BGS-TRACE-133` | **PROVED** | Twisted closure formula for the diagonal-kick cat map at every time |
| `BGS-TRACE-134` | **PROVED** | Pointwise revival bound at the scalar return and its limit on the minimal-period sequence |
| `BGS-TRACE-135` | **PROVED** | Half-period parity reduction of the scalar-return trace |
| `BGS-TRACE-136` | **OPEN** | Free-with-parity revival law at even order (conjecture) |
| `BGS-TRACE-137` | **OPEN** | Exponential revival law at odd order for generic dimensions (conjecture) |
| `BGS-TRACE-140` | **PROVED** | Unitary short-time form factor for Haar momentum phases |
| `BGS-TRACE-141` | **PROVED** | Unitary moment hierarchy for Haar momentum phases |
| `BGS-TRACE-142` | **VERIFICATION-PENDING** | Gaussian momentum-phase crossover from 2m to m |
| `BGS-TRACE-143` | **PROVED** | Haar diagonal-phase cat map equals the random-phase DFT star graph |
| `BGS-TRACE-144` | **PROVED** | Exact Gauss-sum and partition-lattice formula for the Haar diagonal-phase form factor |
| `BGS-TRACE-145` | **PROVED** | Complete classification of the first off-diagonal pairs: 2-opt, swap and figure-eight |
| `BGS-TRACE-146` | **PROVED** | Exact tau^2 coefficient of the Haar diagonal-phase cat-map form factor at fixed time |
| `BGS-TRACE-147` | **VERIFICATION-PENDING** | Computer-assisted exact expansions to m=12 and the fixed-m tau^3 deviation from COE |
| `BGS-TRACE-148` | **OPEN** | Scaling-limit conjecture for the Haar diagonal-phase cat-map form factor |
| `BGS-TRACE-149` | **PROVED** | Band-limited random kick: exact trace bridge E\|Tr U^m\|^2 = Psi_m(t_N) |
| `BGS-TRACE-150` | **PROVED** | Band-limited random kick: 1/N expansion and residue period g'_m |
| `BGS-TRACE-151` | **PROVED** | Band-limited random kick: orbit-pair formula and Gauss-weight support |
| `BGS-TRACE-152` | **PROVED** | Band-limited random kick: strong-kick limit B_m^sym at every residue under P_K-separation |
| `BGS-TRACE-153` | **VERIFICATION-PENDING** | Band-limited random kick: computer-assisted instances m=3..7 (B^sym values, Gamma-separation, K=1 collisions) |
| `BGS-TRACE-154` | **PROVED** | B_m^sym < 2m for every odd m |
| `BGS-TRACE-155` | **OPEN** | B_m^sym < 2m for even m beyond the computed range |
| `BGS-TRACE-156` | **PROVED** | P_K separates point multisets for K containing {1..m}; half-turn collisions for odd K at even m |
| `BGS-TRACE-157` | **PROVED** | 1/N coefficient: Gamma-diagonal part vanishes; oddness in the residue |
| `BGS-TRACE-158` | **CONDITIONAL** | 1/N coefficient, Gaussian ensemble: c_1 -> 0 as eta -> infinity under Gamma-separation |
| `BGS-TRACE-159` | **OPEN** | 1/N coefficient for uniform phases (J0) at large eta |
| `BGS-TRACE-160` | **PROVED** | Full-band random kick equals the maximal random-phase ensemble up to p^m exp(-c p) |
| `BGS-TRACE-161` | **OPEN** | Intermediate band K = kappa N |
| `BGS-TRACE-162` | **OPEN** | Crossover conjecture: R-scaling of the band-limited deviation and the mode threshold |
| `BGS-TRACE-163` | **PROVED** | Fixed diagonal kick: exact Pell-norm trace formula, orbit form and kernel structure; 2m law at m <= 8 |
| `BGS-TRACE-164` | **CONDITIONAL** | 2m law for the eta-Bohr mean at general m, conditional on ND_m |
| `BGS-TRACE-165` | **PROVED** | Ramanujan kernel and exact odd-m diagonal ramp (Prop K, Lemma S + Addendum, Lemma F, Theorem D) |
| `BGS-TRACE-166` | **PROVED** | p-splitting lemma for vanishing sums and symbol facts (C2, C3) |
| `BGS-TRACE-167` | **PROVED** | Automatic admissibility for NSW-prime m (Frobenius argument) |
| `BGS-TRACE-168` | **PROVED** | Theorem N: unconditional formal non-degeneracy bound for the eleven certified NSW-prime m |
| `BGS-TRACE-169` | **PROVED** | Proposition C: norm-class formula for the fixed-eta second moment, all odd m |
| `BGS-TRACE-170` | **PROVED** | Theorem W (parity decomposition) and Theorem T (transfer-operator formula for chi_m) |
| `BGS-TRACE-171` | **PROVED** | Lemma V and Proposition L: lower bound chi_m(eta) >= 1 - m sigma^2 eta^2 / 2 for odd m >= 5 |
| `BGS-TRACE-172` | **PROVED** | Tilted majorant, cycle inequality and Collatz-Wielandt trace bound for the parity transfer operator |
| `BGS-TRACE-173` | **PROVED** | Theorem D_cert: certified exponential decay of chi_m on eta in [1, 81.574] |
| `BGS-TRACE-174` | **CONDITIONAL** | Decay of chi_m at every fixed eta != 0 |
| `BGS-TRACE-175` | **PROVED** | Theorem U: the N-average reproduces the nu-average, with explicit error and window |
| `BGS-TRACE-176` | **CONDITIONAL** | Theorem G: joint (nu, Bohr-eta) moments and a conditional moment CLT |
| `BGS-TRACE-177` | **OPEN** | Numerical observations: ND^(2) at small m, mu(eta) spectrum, m_* crossover, W~rest tables, fixed-eta CLT numerics, torsion-split numbers |
| `BGS-TRACE-178` | **PROVED** | Exact torsion-class split F = F_gen + F_tor |
| `BGS-TRACE-179` | **REFUTED** | Conjecture R: W~rest_m(eta) = o(m) uniformly on compact eta-ranges |
| `BGS-TRACE-180` | **OPEN** | Fixed-eta (nu-only) central limit law |
| `BGS-TRACE-181` | **OPEN** | Non-degeneracy ND_m for composite h_m and for even m |
| `BGS-TRACE-182` | **OPEN** | The (m, eta) = (11, 2) outlier |
| `BGS-TRACE-183` | **PROVED** | Line E E1: resonant residue N == -4 mod h_m; exact collapse of the Pell phase to q/2 + kappa (sum n)^2/8 |
| `BGS-TRACE-184` | **PROVED** | Line E E2: exact IFS transfer-operator law at the resonant residue (finite alphabet) |
| `BGS-TRACE-185` | **PROVED** | Line E E3: certified spectrum of the L-truncated k1-kick IFS operators on a 9-point eta grid |
| `BGS-TRACE-186` | **PROVED** | Line E E4: exponential lower bound \|Z_L(m)\| > 0 for all odd m >= m0 (truncated k1 kick) |
| `BGS-TRACE-187` | **PROVED** | Line E E5: finite-range violation of the k1-kick analogue of Conjecture R |
| `BGS-TRACE-188` | **CONDITIONAL** | Line E E6: the k1-kick analogue of Conjecture R fails at eta = 2 under hypothesis H_infinity |
| `BGS-TRACE-189` | **OPEN** | Line E E7: m = 15 prediction versus outcome (k1 kick, eta = 2) |
| `BGS-TRACE-190` | **OPEN** | Line E E8: Line B kick, giant traces at N == -/+196 mod h_m when 3 does not divide m |
| `BGS-TRACE-191` | **OPEN** | Line E E9: eta-interval (not grid) certification of the resonant growth |
| `BGS-TRACE-192` | **OPEN** | Line E E10: the TRACE-182 (m, eta) = (11, 2) outlier is the +-196 resonance |
| `BGS-TRACE-193` | **PROVED** | Line E E11: pure 7-mode kick, Z_f7(nu) = Z_k1(49 nu); E5 bounds hold verbatim for f7 when 3 does not divide m |
| `BGS-TRACE-194` | **PROVED** | Line E E12: exact a^2-resonance law; 49-state IFS law for the Line B kick at N == -/+196 when 3 does not divide m |
| `BGS-TRACE-195` | **PROVED** | Line E E13: Gauss-completed orbit formula (Prop. G) and rigorous finite-m lower bounds for the TRACE-179 kick at eta = 2 |
| `BGS-TRACE-196` | **CONDITIONAL** | Line E E14: conditional asymptotic failure of Conjecture R for the Line B kick at eta = 2 along 3 not dividing m |
| `BGS-TRACE-197` | **PROVED** | Line F F1: lifted vertex-minus-edge trace identity for the full-alphabet resonance transfer operators |
| `BGS-TRACE-198` | **PROVED** | Line F F2: certified spectrum of the lifted k1 operators at eta = 2 (full alphabet), and the sector-2/6 reflection lemma |
| `BGS-TRACE-199` | **PROVED** | Line F F3: for every odd m >= 15 the k1-kick analogue of Conjecture R fails at eta = 2 (unconditional, computer-assisted) |
| `BGS-TRACE-200` | **PROVED** | Line F F4: the all-m failure transfers to the pure 7-mode kick f7 for 3 not dividing m |
| `BGS-TRACE-201` | **PROVED** | Line F F5: certified all-m growth at the grid points eta in {1.25, 1.5, 1.75, 2.25, 2.5} (k1, full alphabet) |
| `BGS-TRACE-202` | **OPEN** | Line F F6: float growth window eta in (0.951, 3.212) for the k1 sector-4 eigenvalue |
| `BGS-TRACE-203` | **PROVED** | Line G G1/G1'/G2: general (a,b) partial-trace transfer law for Z_m(nu), finite alphabet |
| `BGS-TRACE-204` | **PROVED** | Line G G3: dilution identity along divisors d of h_m |
| `BGS-TRACE-205` | **OPEN** | Line G classification record: resonant families, growth rates, G5 (h_d \| h_m), G6 (sparsity), G7 (moment heuristic), eta-scan |
| `BGS-TRACE-206` | **OPEN** | Line G: Conjecture R' (corrected mean law for the k1 kick at eta = 2) with a pre-registered m = 17 test |
| `BGS-TRACE-207` | **PROVED** | Line H: kappa lemma (\|c_b\| = 1/2 for all odd m, 3 not dividing m) and the full-alphabet 49-state lifted trace identity for the Line B kick |
| `BGS-TRACE-208` | **PROVED** | Line H: certified spectrum of the 49-state lifted operators for the Line B kick f_B at eta = 2, s = -1 (N == +196) |
| `BGS-TRACE-209` | **PROVED** | Line H: Conjecture R fails for the Line B kick: W~rest_m(2)/m >= 1.4e4 for every odd m >= 47 with 3 not dividing m |
| `BGS-TRACE-210` | **OPEN** | Conjecture R_NSW: W~rest_m(eta) = o(m) along m with h_m prime |
| `BGS-TRACE-211` | **PROVED** | Line I Prop I1: relative phase split Z_m(nu0+delta) = Z_m(nu0) sigmahat(delta) (k1 kick, any unit nu0) |
| `BGS-TRACE-212` | **PROVED** | Line I Prop I2/I2': dilation-coset L^2 law and per-member Gauss-sum formula for the members Z_m(nu0 + 2hj/d), d odd, d \| h_m |
| `BGS-TRACE-213` | **PROVED** | Line I Thm I4: exact reduction of Conjecture R' to (E''), (T'') and the dilation remainder (D) |
| `BGS-TRACE-214` | **PROVED** | Line I Lemma I5': Fourier expansion of weighted horocycle sums of \|Z_nu\|^2 (all residues and units via Ramanujan sums) |
| `BGS-TRACE-215` | **PROVED** | Line I Thm I6 v2: certified bound on the d = 7 dilation square term for the k1 kick at eta = 2, rho = (+-2,8), all m == 3 (mod 6) |
| `BGS-TRACE-216` | **PROVED** | Line I: exact monomial intertwiners between the eight (m mod 24, a = +-2) cases of the (+-2,8) twisted G2 operators and the beta -> -beta reflection |
| `BGS-TRACE-217` | **PROVED** | Line I Thm I9: certified top twisted spectrum for d = 7 (classes 1:3, 2:1): three simple eigenvalues with 1.262 < \|mu\| < 1.45, so r_tw > sqrt(lambda)/mu0 |
| `BGS-TRACE-218` | **PROVED** | Line I: aliasing (Moebius) identity for the unit-residue mean F_m |
| `BGS-TRACE-219` | **PROVED** | Line I: unbounded prime support of h_m (a new odd prime for every m >= 16; every finite prime set fails for all large m) |
| `BGS-TRACE-220` | **OPEN** | Line I: Conjecture R'_A (amended mean law with actual dilation-member values) for the k1 kick at eta = 2 |
| `BGS-TRACE-221` | **PROVED** | Line J Prop J-C: exact sector law, exact leading d = 7 coefficient B_C, exact cancellation of sectors 2, 6 and survival of sectors 0, 4 for rho = (+-2,8) |
| `BGS-TRACE-222` | **PROVED** | Line J: sector-level antiunitary map sigma(V^(-2)_{beta,a+4}) = conj sigma(V^(+2)_{beta,a}) (and likewise for E) for the (+-2,8) twisted sector operators |
| `BGS-TRACE-223` | **PROVED** | Line J: certified top-orbit and rest certificates for the d = 7 sector operators: \|mu_2:1\| in [1.28359503, 1.28359523], \|xi\| = \|mu* mu_2:1\| >= 2.4586893 > sqrt(lambda) |
| `BGS-TRACE-224` | **PROVED** | Line J window lemma: for theta in [theta_lo, theta_up] subset (0, pi], among N = ceil(2 pi/theta_lo) consecutive k some cos(alpha + k theta) >= cos(theta_up/2) and some <= -cos(theta_up/2) |
| `BGS-TRACE-225` | **PROVED** | Line J Theorem J: the frozen d = 7, (+-2,8) contribution oscillates with growth >= 1.0184224^m: both signs in every 6 consecutive members of each class mod 168 (m == 3 mod 6) |
| `BGS-TRACE-226` | **PROVED** | Line J3 Lemma L16: lifted trace formula for rho = (+-2,16) restricted to the exact 2-dimensional monomial blocks |
| `BGS-TRACE-227` | **PROVED** | Line J3: the d = 7 contribution of rho = (+-2,16) (with inherited copies) is <= 1% of (K_min/2) xi_lo^m for m >= 243 |
| `BGS-TRACE-228` | **PROVED** | Line J3 inheritance theorem: W_{ce, e beta'} = (n_e/e^2) W_{c, beta'} for coprime odd c, e with ce \| h_m (composite levels carry positive multiples of lower-level class sums) |
| `BGS-TRACE-229` | **PROVED** | Line J3: prime-level complete-sum bound: \|W_{q,beta}\| <= 2/q^2 for non-isotropic beta, (q-2)/q^2 for the 2(q-1) isotropic beta (q \|\| h_m) |
| `BGS-TRACE-230` | **PROVED** | Line J3 r(q) lemma: for odd m and an odd prime q, q \| h_m iff r(q) := ord_q(lambda) divides m |
| `BGS-TRACE-231` | **CONDITIONAL** | Line J3 Theorem J3 (conditional): frozen R' is false along m = 3p under H-natural and H_arg; unconditionally, if R' holds the conductor-not-in-{1,7} parts must cancel the d = 7 term exponentially on S+ |
| `BGS-TRACE-232` | **OPEN** | Line J3 hypothesis H-natural: the conductor-not-in-{1,7} part O-natural_m does not cancel the d = 7 term on infinitely many m in S+ |
| `BGS-TRACE-233` | **OPEN** | Line J3 hypothesis H_arg: arg(xi_2:1)/2 pi is irrational |
| `BGS-TRACE-234` | **PROVED** | Line K Lemma K3 (gap lemma): for b' >= 447, b' not in {504, 560, 616, 840}, every unit class mod gcd(56, b') has maximal cyclic gap < A b' among the units mod b' in that class (A = arccos(0.84431)/pi) |
| `BGS-TRACE-235` | **PROVED** | Line K Theorem K3: S+ contains infinitely many m = 3p with p == p0 (mod 56) for every unit p0 mod 56, unconditionally (H_arg removed) |
| `BGS-TRACE-236` | **PROVED** | Line K Corollary K3: frozen R' implies phi^-1 O-natural_m <= -0.99 K_j 1.0184224^m + 4m + o(m) on an infinite set of m = 3p (each unit class p0 mod 56); hence H-natural alone refutes frozen R' |
| `BGS-TRACE-237` | **PROVED** | Line K Theorem K1 (light-cone identity): for a prime q != 7, q \|\| h_m, 2 a square mod q, sum_{beta != 0} Zhat_beta W_{q,beta} = D_iso - E_b/q |
| `BGS-TRACE-238` | **PROVED** | Line K Prop K2 (large levels by positivity): for m = 3p >= 495 the levels d >= L_m = (mu*^2/xi)^{m(1+eta_m)} contribute >= -0.01 (K_min/2) xi_lo^m; S_Z <= 0.5000001; eta_m <= (2.010 + o(1))/log(2p+1) |
| `BGS-TRACE-239` | **OPEN** | Line K hypothesis H-natural_mid: for some delta > 0 and infinitely many m in S+, O-natural_m^{<L} >= -(1 - delta) 0.98 (K_j/2) xi_lo^m |
| `BGS-TRACE-240` | **CONDITIONAL** | Line K Theorem K (conditional): frozen R' is false under H-natural or under the alternative hypothesis H-natural_mid |
| `BGS-TRACE-241` | **PROVED** | Line K Lemma W1 (Weil bound over the orbit subgroup): for q prime, H = <l> subset F_q^* of order r and A, B in F_q not both 0, \|sum_{h in H} e((Ah + B/h)/q)\| <= 2 sqrt q (<= sqrt q if AB = 0); degeneracy criterion |
| `BGS-TRACE-242` | **PROVED** | Line K Lemma W2' (non-cyclic block AM-GM, every bounded read-out): \|Tr(J X)\| <= C_J max(1, sup\|\|L\|\|)^{2k} e^2 max(1, (1/m) sum_{i<m} \|\|P(i)\|\|_HS^2)^{(Q-1)/2} |
| `BGS-TRACE-243` | **PROVED** | Line K Lemma W3 (orbit average): (1/r) sum_{i<r} f_k(beta lambda^i/q) <= I_k + 2 sqrt q A_k/r + T_k(q) for q \|\| h, beta != 0, with T_k(q) -> 0 (6 sqrt q for conductor 7q) |
| `BGS-TRACE-244` | **OPEN** | Line K operator input (OP_k, delta): the cat-map second moments satisfy (I_k^F)^{1/2k} <= (1 - delta) 1.28359 for every (+-2,8) family and <= (1 - delta) 1.4742 for every (+-2,16) family |
| `BGS-TRACE-245` | **CONDITIONAL** | Line K Theorem W (conditional on OP): for p >= p0(k), the conductors q, 7q with q prime, q \| h_{3p}, q <= c_k p^2 contribute o(xi_lo^m) to O-natural on S+, including inherited copies |
| `BGS-TRACE-246` | **CONDITIONAL** | Line K Theorem K2' (conditional on OP): frozen R' implies that for all large m in S+ some open conductor c of h_m carries a slow lambda-orbit |
| `BGS-TRACE-247` | **OPEN** | Line K Conjecture C1: for the true twisted operator families, lim_k (I_k^F)^{1/k} = 1 |

<!-- END GENERATED: registered family tables (render_status.py) -->
