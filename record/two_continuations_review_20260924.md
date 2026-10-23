# Audit of two submitted fixed-map continuations (24 September 2026)

**Primary verdict:** **INCOMPLETE as a solution of microscopic CUE/BGS.**
The two texts expressly leave the pair Abel limit and every
model-specific Heisenberg-scale mixed joint-trace comparison open.
Several claims are correct **within narrower scopes** or reproduce
already maintained results; the 492-degree finite certificate
mentioned in one text was **not provided** with the two uploaded files.
No world-level originality, external referee acceptance, or CUE law
is inferred from these inputs.

**Submission identity:** `REPORT_RU(1).md`, 626 lines,
SHA-256 `6ea9a375499b2c98cf08c3b182d8c38037f5ad09e5be13df92825cb559479fa5`;
`NEW_RESULTS_RU(1).md`, 1466 lines,
SHA-256 `0200dc40e2655776222b9eae7f3c898384730a10d40a7f7dbf631aba13aa4881`.
Only those two Markdown files were attached in this turn.
The referenced `verify_exact.py`, `exact_certificate.json`, and
`verification_results.json` were **not** among the supplied attachments;
their claimed executions are not a verification record of this audit.

## Claim-by-claim disposition

| Submitted section | Audited implication | Disposition |
|---|---|---|
| REPORT §§1–2; NEW §1 | Raw Weyl convention, \(C=\left(\begin{smallmatrix}3&2\\4&3\end{smallmatrix}\right)\), Jacobi path, kick coefficients | Correctly matches previously maintained `BGS-FM-001`/`005`; no duplicate new claim. The ordinary-symbol half-shift is already recorded. |
| REPORT §§3.1–3.3; NEW §2, §5.2 | Algebraic-time exact-identity separation and algebraic-entry commutants; Weyl normalizers | The qualitative Lindemann–Weierstrass implication is correct with **algebraic-entry** and nonzero algebraic-time hypotheses. Its scalar commutant corollary at \(7\nmid N\), and the unitary Weyl-normalizer claim for odd \(N\ge19\), are retained with full scopes in `BGS-FM-010`. No claim excludes the ordinary nonalgebraic spectral projectors of a unitary matrix. |
| NEW §3 | \(\lvert\operatorname{Tr}M_N^m\rvert^2\) gcd formula; \(\operatorname{Tr}U_N^m\ne0\) for all odd \(N,m\ge1\); scalar returns only at \(N=7\) | **Retained as `BGS-FM-010`.** Recomputed the Pell matrix identity, superoperator trace and the \(169/500\) positive orbit margin. The earlier simple-powers result `BGS-FM-008` supplies the small \(7\nmid N\) cases. Exact finite regressions are not the all-\(N\) proof. |
| REPORT §4 | Seven-cut nuclear bound and square-root Abel transfer | Correct but weaker than the **existing** `BGS-FM-007`, which also proves unconditional \(O_s(\tau/\log N)\) pair/Abel differences. No duplicate claim or weaker replacement. |
| REPORT §§5–7 | Partition/Poisson and finite CUE benchmarks, Schwartz extension, equivalence of full pair and all-\(s\) Abel limits | Correctly fits previously maintained `BGS-TRACE-001`–`004` and `supplement/fixed_map/weighted-secular/determinant_boundary.md` §3. The Abel equivalence already has a stronger countable-\(s\) formulation there. No model-specific trace bound follows. |
| NEW §§4–5 | All eigenbasis minors nonzero, fixed-algebraic-time spectral simplicity and transcendental ratios | Already maintained as `BGS-FM-008`. The submitted proof uses a different p-adic gauge and is compatible with the existing result; no second independent validation of the whole all-\(N\) argument is claimed. |
| NEW §6 | 492-degree \(\mathbb F_5\) polynomial and exclusion of pair antiunitaries at \(7\nmid N\) | **Do not import the unprovided certificate.** Its stated conclusion is already covered more strongly by the reproduced 2225-term integer certificate in `BGS-FM-009`, for all odd \(N\ne7\). No claim about reproducing the absent `exact_certificate.json` or its factor irreducibility. |
| NEW §7 | Explicit \(N\)-dependent positive eigenphase gap, \(7\nmid N\) | **Retained as `BGS-FM-011`**, with full algebraic-degree, denominator and height accounting and pinned [Roy Theorem 1.1](https://arxiv.org/pdf/1607.00579v1.pdf). Source conditions and exponent \(18S^r\) were checked directly in the primary paper. The bound is extremely smaller than \(N^{-1}\); it cannot bound microscopic crowding. |
| NEW §8 | Full classical \(C^1\) centralizer and absence of \(C^1\) reversor at the physical \(\tau\) | Already maintained, with an equal or stronger domain, in `BGS-FM-001`. No second novelty claim. The new detailed orbit/remainder chain and absent alleged script were **not** independently certified in this pass. |
| Both texts' last sections | Missing Abel sum / joint-trace cancellation | **OPEN.** Neither exact nonvanishing nor an astronomically small gap implies the upper estimates or the signed \(m\asymp N\) cancellation. |

## Independent checks and external theorem boundary

1. Derive \(\operatorname{Tr}\operatorname{Ad}(M^m)
   =|\operatorname{Tr}M^m|^2\) in the orthonormal Weyl basis.
   With \(P=I+J,\ J^2=2I,\ P^2=C\), the Pell identity
   gives \(C^m-I=2u_mP^m\) for odd \(m\) and \(2v_mP^mJ\)
   for even \(m\). Kernel counts give the exact gcd-square formula
   for every odd \(N,m\); positivity is unconditional.
2. An independent direct numerical reconstruction of the *unperturbed*
   matrix \(M_N\) for \(N=3,5,7,9,15,21,25,35\) and
   \(1\le m\le20\) matched the gcd-square formula with maximum
   absolute discrepancy \(<2.6\cdot10^{-12}\).
   The maintained **integer-only** checker
   [`frozen_arithmetic_traces.py`](../computations/verification/frozen_arithmetic_traces.py)
   reproduces 1248 fixed-point cases and the rational orbit margin;
   [its saved output](../archive/evidence/20260924/frozen_arithmetic_traces.json)
   does not evaluate the kicked \(U_N\) or prove an asymptotic law.
3. [Popescu, Theorem 3.2](https://arxiv.org/pdf/2306.14352),
   is already pinned in `EXT-POPESCU-2023`; it is used only
   for exact nonvanishing at nonzero algebraic time.
   [Roy, Theorem 1.1](https://arxiv.org/pdf/1607.00579v1.pdf),
   allows complex algebraic, \(\mathbb Q\)-independent exponents
   and integer-polynomial input. In `BGS-FM-011`, the basis,
   conjugate bound, common denominator, integer height and
   Laurent-to-polynomial conversion are given explicitly.
   Its application is author-level mathematical review, **not**
   a formal check of enormous integers or an independent referee report.

## Exact remaining task

Show, for each fixed \(s>0\), that
\[
N^{-2}\sum_{m\ge1}e^{-2sm/N}
\bigl(|\operatorname{Tr}U_N^m|^2-\min(m,N)\bigr)\longrightarrow0
\]
along all odd \(N\). This would give the pair limit, not the
full \(k\)-point result. For every \(k\ge3\), also prove the
weighted **signed** joint-trace comparison on every compact
Fourier support (`BGS-TRACE-005`). Both newly retained
auxiliary claims leave those obligations open.
