# Research note: certifying Estimate U (5 November 2026)

**Evidence only. No registry change.** This folder keeps the research pass `research1105c`, which tried to certify
"Estimate U": the non-resonant activity bound |z_γ| ≤ C₀ · r^{n_nr(γ)} of the N11 polymer expansion (see
[REPORT.md](REPORT.md) §1 and [CERT.md](CERT.md) §1). It produced **no new full [CA] result**, so no claim is registered
from it. The files [REPORT.md](REPORT.md), [BRIDGED.md](BRIDGED.md), [C0.md](C0.md), [CERT.md](CERT.md) and
[REFEREE_CERT.md](REFEREE_CERT.md) are verbatim copies of the working notes; `logs/` keeps the small text and JSON logs
(the large binaries and the code tree are not copied, so paths named in the notes may be absent here). The notes were
written against main `6f69baa1`.

**Tags.** [CA] interval or exact arithmetic with every input enclosed · [CA-fp] IEEE binary64 inputs under an
a-priori model, not fully enclosed · N13-conv: the eigen data Φ, ψ, s are taken as the stored binary64 values (the N13
convention) · [P-arith] arithmetic implication · [N] floating-point numerics without error control · [C] open.

## Outcomes

| Quantity | Result | Tag |
|---|---|---|
| Singles activity on the 10 single types | ≤ 0.30209 | [CA-fp] / N13-conv (inputs in float, eigenpair not enclosed) |
| All 1350 coded pairs, core \|r̃\| | ≤ 0.09375 | [CA-fp] / N13-conv (inputs in float, eigenpair not enclosed) |
| r_ε, continuum Fourier Galerkin | ≈ 0.474 | [N] |
| r_ε, discrete Hilbert–Schmidt majorant | ≤ 0.572 | [N] |
| Soft room (semiprime family of BGS-TRACE-350, C₀ = 1) | needs r < 0.600 at p = 1409 and r < 0.527 at p = 3307 | [P-arith] |
| Certificate r ≤ 0.5 | **failed** (not achieved) | — |
| Short windows (200, enumeration [P]) | 3 shorts uncertified (arb radius blow-up), so max\|z\| ≤ 0.6 is not certified for all 200 | — |
| Eigenpair enclosure (Rump / Bauer–Fike) | not achieved | — |

The referee audit ([REFEREE_CERT.md](REFEREE_CERT.md)) confirmed the method for the pairs and recorded gaps on the
eigenpair enclosure and the spectral-radius step. A forward-scan pair maximum of 0.1576 is withdrawn (precision bug;
[CERT.md](CERT.md) §B).

## Status

* **Estimate U is not certified.** Even the [N] value r_ε ≈ 0.474 would be inside the soft room at both primes only if it
  were [CA]; the [N] majorant 0.572 would cover p = 1409 only.
* **U_cross** (transfer to cross lines), **H5(b)** and **H1** remain **open**. BGS-TRACE-303 (H5), BGS-TRACE-336 (H1) and
  the conditional BGS-TRACE-355 are unchanged; Theorem R♯-mod v5 (BGS-TRACE-325) stays conditional.
