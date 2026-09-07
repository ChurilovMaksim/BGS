# Rare-phase and Gaussian-channel review — 2026-09-07

## Claims and verdicts

1. For the fixed-moment pair `sqrt(1-u)|0> +/- sqrt(u)|n>`, `u=E/n^beta`, complete/censored heterodyne Hellinger information has balance radius `x_n~n/e`, a universal radial profile and an exact aperture discrimination exponent. **Verdict: proved in the project proof.** The scalar constant is independently interval-certified; quadrature is diagnostic only.
2. For any fixed product of physical phase-insensitive Gaussian channels with positive gains and at least one noisy mode, input-state tomography under the sole total-number beta-moment constraint has minimax expected input trace distance `Theta((log B)^(-beta/2))`, even allowing arbitrary collective output POVMs. Randomized product homodyne attains the upper order. **Verdict: proved in the project proof under the stated fixed-channel/no-environment/no-preencoding model.**
3. For the n=128 mean-energy-one pair, exactly 10 unrestricted input copies are first sufficient for 75% binary success; ordinary heterodyne needs more than `3e18`, unit-aperture censored heterodyne more than `3e218`; after 50% pure loss, the optimal collective-output threshold is strictly above `3e39` and at most `4e39`. **Verdict: exact finite inequalities.**

External priority and independent referee acceptance are not asserted. None of these results is a microscopic BGS universality theorem.

## Adversarial proof audit

### Rare phase

The radial identity is obtained before asymptotics by angular averaging. With `x=x_n+y`, `n/x_n->e`; the two half-lines are dominated respectively by `4 exp(-y)` and `4 exp((kappa-1)y)` for fixed `1<kappa<e`. The exact angular series has nonnegative squared-binomial coefficients and an analytic tail bound. The aperture exponent is derived from the maximum of the minimum of the vacuum and number-state coherent probabilities. The critical likelihood limit uses a compensated integrand dominated by the same Hellinger majorant; the Bayes-error test function `min(1,exp(z))` is bounded and continuous. The fixed-test Chernoff statement uses a measure-preserving involution and is not promoted to adaptive critical optimality.

### Gaussian inverse problem

The upper proof inverts only low Fock matrix entries and does not assume a cutoff of the unknown characteristic function: the discarded integral is controlled by uniform exponential decay of the known low-Fock Weyl kernel. On the retained ball the known Gaussian noise is inverted explicitly; randomized product homodyne provides unbiased characteristic-function samples of unit modulus. A cutoff proportional to `log B` balances exponential inverse amplification against photon-moment projection bias.

The lower proof is measurement-independent. Pure loss suppresses the hard vacuum/high-Fock coherence exponentially and fidelity controls all collective POVMs on tensor powers. Quantum-limited amplification is handled separately by an exponentially decaying trace-norm bound for the image of `|0><n|`. Physical phase-insensitive channels with nonzero noise factor through the corresponding hard loss/amplifier channel followed by additional Gaussian noise, and trace-distance contractivity transfers the lower bound.

The later uniform pure-loss theorem strengthens the varying-loss binary limit for the explicit hard pair. It does not by itself supply a matching full moment-class minimax theorem when channel noise vanishes with B.

## Independent computation

Repeated before publication:

- `rare_phase_testing.py`: 8192-term outward-rounded interval arithmetic, 4096 central-binomial tail checks, four exact finite-copy checks, five angular quadratures and four radial finite-n diagnostics at 80 decimal digits: PASS.
- `rare_phase_certificate.cpp`: independent Boost.Multiprecision central-binomial construction; replay interval contained in the Python certificate; six half-loss rational inequalities: PASS with strict compiler warnings enabled.
- certified constant: `2.908610238318050510439407... < C_* < 2.908610238318273566707832...`, implying `2.9086102383180 < C_* < 2.9086102383183`.
- `rare_phase_limit.py`: independent 112-by-1536 compensated quadrature: PASS; numerical diagnostic only.
- `gaussian_channel_minimax.py`: dimension 4 / 65 digits gives 256 exact Weyl matrix-unit inversion checks; dimension 6 / 95 digits gives 1296. Each run also gives 512 exact pure-loss identities, four exact additive-noise factorizations, six exact n=128 half-loss inequalities, 18 independent Kraus/characteristic checks, nine fidelity checks, 146 low-Fock Weyl-kernel checks, 16 amplifier trace-norm checks and four negative controls: PASS.

The computations audit finite algebra and implementation; they do not replace continuum/asymptotic arguments.

## Literature boundary checked 2026-09-07

Primary/official source metadata were rechecked before integration: Ivan-Sabapathy-Simon (Gaussian-channel/Kraus machinery), Butucea-Guta-Artiles (noisy homodyne/Wigner minimax work under different classes/loss), Lami and Sabapathy-Winter (restricted-measurement bosonic data hiding), and Mele et al. (general continuous-variable state learning under energy/moment conditions). These establish prior-work attribution and scope, not global novelty or world priority of the current formulations.
