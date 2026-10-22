# Claim addendum: rare-phase, fixed Gaussian noise, and uniform pure-loss limits (2026-09-07)

This scoped note records the information-theoretic claims from the session. Repository-wide authority is now `record/claim_ledger.md` together with `record/claim_ledger_addendum_20260907.md`; the latter incorporates and governs the claims below.

- **EXACT + FINITE-CERTIFICATE:** rare-phase balance radius `x_n~n/e`, radial Hellinger profile, exact aperture exponent, and certified scalar `2.9086102383180<C_*<2.9086102383183` for the explicit fixed-moment vacuum/high-Fock pair.
- **EXACT + FINITE-CERTIFICATE:** for `n=128`, mean photon number one, exactly 10 unrestricted input copies first reach 75% known-pair success; ordinary heterodyne needs more than `3e18`, unit-aperture censored heterodyne more than `3e218`.
- **EXACT:** for every fixed finite-mode phase-insensitive Gaussian product channel with positive gains and at least one strictly noisy mode, inaccessible environment, and no pre-channel encoding, moment-class input tomography has minimax expected input trace-distance risk `Theta((log B)^(-beta/2))` even against arbitrary collective output POVMs; randomized product homodyne attains the upper order.
- **EXACT:** the corresponding deterministic inverse modulus is `Theta((log(1/delta))^(-beta/2))` for fixed channel parameters.
- **EXACT + FINITE-CERTIFICATE:** at 50% pure loss, the `n=128` known pair has optimal collective-output 75% copy threshold `3e39 < B_75 <= 4e39`.
- **EXACT + FINITE-REGRESSION:** for the explicit pure-loss pair, `0<u<=1/16`, `t=B u eta^n`,
  `|D(sigma_+^B,sigma_-^B)-sqrt(1-exp(-4t))| <= 5ut+sqrt(u(43t+8sqrt(t)))`, with the stated varying-loss critical law and copy penalty `eta^{-n}`.
- **OPEN:** a matching full moment-class minimax transition when the physical channel noise vanishes with `B`.
- **OPEN:** microscopic BGS/GOE/COE universality; the Heisenberg-scale joint-trace/local-resolvent closure remains missing.

Proofs and evidence: `mathematics/bosonic_information_limits_20260907.md`, `mathematics/pure_loss_discrimination.md`, `record/rare_phase_gaussian_review_20260907.md`, `record/pure_loss_discrimination_review_20260907.md`, and the dated JSON certificates in `evidence/certificates/`.