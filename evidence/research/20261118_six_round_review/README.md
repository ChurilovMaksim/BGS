# Review of the six-round fixed-map research packet (18 November 2026)

**Classification:** supplementary research intake / restricted proof audit, **no changes to claim status**.  
**Base repository:** `ChurilovMaksim/BGS`, `main` at `3d21de1f3cca6470e352f4272cf354ee2eb39d4e` (5 November 2026).  
**Source:** user-supplied `BGS_all_runs_2026-11-18_bundle.zip`; SHA-256 `557a771f672dde40bce265f80782fe6d73ffa48a9ce2b332d80932a85ee92360`. The ZIP contains 164 files (including its nested historical editions) and 9,430,504 uncompressed bytes. The 185-page cumulative PDF has SHA-256 `de56133d9cf1b6116e20cdaf905887a3b8a4c5b4796577c4bf4048c286773160`; the newest standalone round-6 PDF has 29 pages.

This intake is **not** a claim that all 185 pages have undergone an independent referee-level analysis. It documents the subset whose proof can be reconstructed from maintained BGS definitions without importing new, unverified analytic dependencies. The historical ZIP/PDF is not copied wholesale into the maintained tree. The original artifact is identified by its immutable digest; the math retained below is self-contained and reproducible.

## 1. Reproduction actually performed

On the **original unpacked ZIP bytes**, not on regenerated/reassembled PDFs:

- `python verification/verify_certificates.py`: **passed**; the three round-6 programs confirmed their delivered exact finite outputs (the quadratic midpoint jet, 1,128 translated-field principal-angle pair checks, and 211,008 balanced eight-letter cases). This verifies the finite certificates at their own scope, not the semiclassical deductions subsequently made from them.
- `python verification/verify_artifacts.py`: **passed**; 163 recorded file hashes, 185 PDF pages, 924 named destinations, 619 internal PDF links, zero blank pages, zero replacement-character pages, zero unresolved internal links, and unchanged text of all 156 historical pages.
- Independent integer modular calculation verified `S^(3*7^(j-1)) == I mod 7^j` for j=2,3,4; the accompanying elementary binomial proof works for every j.
- Separate floating-point checks of the explicit metaplectic M_N at N=49 and 343 observed `M_N^(3N/7)` scalar to numerical tolerance. **Illustrative only:** the general assertion follows from exact Egorov and the modular proof, not from these floating-point examples.

No `git clone`, full repository checkout, full BGS CI suite, Lean build, or main manuscript build was executed for this intake. The repository was inspected and written through the connected GitHub interface. The attached ZIP's provenance is external to Git; its original programs are not assumed to be authoritative.

**Reproducible repository-local arithmetic check:** [finite verifier](../../../computations/verification/torsion_history_20261118/verify_finite_inputs.py); its scope is deliberately narrower than the full proof.

The transcendence input for the accepted exact argument reuses the repository's existing registered `EXT-POPESCU-2023` (Theorem 3.2); no new literature registry entry is needed.

## 2. Incorporated result: torsion-history interference

The independently reconstructable argument is maintained in [torsion_interference_vertical_outliers_20261118.md](../../../mathematics/fixed-map/torsion_interference_vertical_outliers_20261118.md).

For every N=7^j, j>=2, at the special times k divisible by 3N/7, the exact complete interference between distinct 49-sector trace histories satisfies

$$
\mathcal I_{N,k}(0)=\frac{48}{49}N^2,\qquad
\mathcal I_{N,k}(\tau N)\ne0
\quad(\tau=10^{-80}).
$$

The proof uses the 49 character projections, the modular cat return, and a finite algebraic exponential polynomial with the Lindemann-Weierstrass nonvanishing argument. In contrast, the complete Hilbert-Schmidt norm of the projected histories squares and sums exactly to N.

**Critical restriction:** no positive lower bound for \(|\mathcal I_{N,k}(\tau N)|/N^2\), no sign and no conclusion for the prescribed nonalgebraic bump weights follows. This does not refute or prove the pair (P) or the full Sine2 limit.

## 3. Incorporated result: vertical exceptional channels

For a **fixed** odd d>=3 dividing odd N, the pure-kick vertical compression has at least \(2\lfloor L/d\rfloor+1\) singular values at least

$$
1-121\pi^2\tau(L+1)^2/N
$$

when \(0\le L\le N/4\). The proof is a direct estimate for the *centered literal* raw-Weyl tridiagonal A_N plus Duhamel and singular-value min-max.

This is a warning against promoting **bulk singular laws** to an operator-norm gap. It concerns \(E_dK_NE_d\), **not** the full 49-character oldspace or \(P U_N P\). In the uncentered convention used in parts of the packet, the corresponding reference scalar is \(e^{i\tau N}\); in the canonical BGS-centered convention it is \(e^{i(9/10)\tau N}\). The singular-value conclusion is identical.

## 4. Valuable research claims **not** promoted

The six rounds contain many more ambitious statements. They have **not** been imported as registered theorems or as replacements for maintained BGS arguments, because their new infinite-dimensional or long-time steps were not independently reconstructed to the required level during this integration.

| Packet topic | Current disposition | Specific unresolved review dependency |
|---|---|---|
| Round-6 all-order vertical torsion/kick freeness and oldspace limits | Candidate theorem / independent packet audit, no registry promotion | Validate the homogeneous-cylinder free-product argument, exact fixed-word Egorov and the inference for all fixed moments, not merely three finite certificates |
| Four full 7-primary oldspace principal-angle moments | Finite symbolic checks reproduced; global asymptotic scope unpromoted | Validate complete nontrivial-word zero-area argument for all words up to length eight and match all normalization and projector ranks |
| Superpolynomial cancellation of all repeated geometric orbits | Candidate theorem, **not** silently accepted | Verify the cited Faure--Tsujii high-frequency/marked-holonomy estimates, the transfer to actual closed periodic weights, and uniformity in m~N; squared-amplitude weights cannot replace coherent weights |
| Sharp central compression resonance and spectral-radius limit | Candidate theorem, no manuscript/registry promotion | Independently review the high-dimensional contour, the all-time trace-class summability and nonnormal leading-eigenvalue inference |
| Round-3--5 boundary/central/sector estimates and external countermodels | Retained in external packet, not copied wholesale | Check overlap with existing maintained BGS results, exact dependence on analytic parameter \(\tau N\), and all claim boundaries; alternate matrices do **not** refute the original family |
| Quantitative microscopic Sine2, pair (P), Abel (A/R), all-order (H) | **OPEN** (unchanged) | Quantitative full primitive--primitive signed interference at times m~N; then an all-order criterion |

The packet uses \(A_N^\mathrm{packet}=A_N^\mathrm{BGS}+\tfrac1{10}I\) in some sections. Transferring complex traces or resonance locations requires the scalar \(e^{it/10}\); transferring conjugation identities, squared moduli or singular values does not. This was checked explicitly against [the canonical model](../../../mathematics/fixed-map/fixed_map_resolvent_frontier.md). For the ordinary midpoint symbol the last term is \(r(q+\tfrac12)\cos(2\pi p-\alpha_0)/100\); the half-period shift is mandatory.

## 5. Scientific and repository consequences

This review adds **two narrowly scoped mathematical observations** and a reproducible finite-input checker. It does **not** change `record/claims.json`, `record/errata.json`, any generated status surface, any external-dependency entry, the frozen manuscript, or any pre-existing theorem/proof file.

All 438 registered claims preserve their 5 November states. In particular BGS-BGS-001, BGS-TRACE-005 and BGS-TRACE-206 remain open; BGS-TRACE-325 remains conditional. The main missing mechanism is coherent, model-specific cancellation between **distinct primitive** contributions on the Heisenberg time scale. No result here supplies that estimate.

This review is a lower-scoped addition to the research record, not an independent refereeing certificate for the cumulative mathematical packet.
