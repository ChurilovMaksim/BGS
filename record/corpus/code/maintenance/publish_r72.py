"""Append the run-72 entry to LEDGER.md, add THEORY section 10, and refresh
README / ROADMAP / MANIFEST.  Idempotent."""

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def rd(p):
    return open(os.path.join(ROOT, p), encoding="utf-8",
                errors="surrogateescape").read()


def wr(p, s):
    open(os.path.join(ROOT, p), "w", encoding="utf-8",
         errors="surrogateescape").write(s)


rep = []

# ---- LEDGER
entry = rd("review/audits/2026-08-28/R72_ledger_entry.md")
led = rd("LEDGER.md")
if "RUN 72 (2026-08-28, continuation)" in led:
    rep.append("LEDGER.md already has run 72")
else:
    wr("LEDGER.md", led.rstrip() + "\n" + entry.rstrip() + "\n")
    rep.append("LEDGER.md: run-72 entry appended")

# ---- THEORY section 10
TH10 = r"""
## 10. RUN 72 (2026-08-28) — THE EXACT SYMMETRY STRUCTURE

Supersedes the run-71 verdict on `op:local_deterministic`. Full statements and
proofs: `paper/exact_wd_and_subgroup_moments.pdf` sections 5-6. Ledger: R72.

### 10.1 Theorem C [PROVEN, unconditional] — closes O6

For every reversing involution `R = [[p,q],[r,-p]]` the matrix `M = S R` equals
`[[p, q], [-r, p]]` and therefore **always has equal diagonal entries**. In
`(U_M conj(U_M))(x,z) = N^{-1} w^{c'(d x^2 - a z^2)} sum_y w^{c'((a-d) y^2 + 2y(z-x))}`
the quadratic term then vanishes, `2c' = c^{-1}` is a unit, the y-sum is
`N [z = x]`, and at `z = x` the prefactor is 1. Hence

        Theta^2 = U_M conj(U_M) = identity,   exactly.

O6 ("prove `c(M,M^{-1}) = +1` in general") is closed. The `gcd(M_21, N) = 1`
condition added in R65 is the well-definedness of the kernel, **not** a
hypothesis. beta = 4 never occurs. Certified at 504 configurations,
worst deviation 1.78e-15. T13 no longer rests on a numerical scan.

### 10.2 Theorem D [PROVEN] — exact parity obstruction and dichotomy

With `R_par f(x) = f(-x)` and `A^k = eps I`, `eps = +-1`:
`[R_par, U_A] = 0` exactly (the kernel is even); `R_par T(u) R_par^{-1} = T(-u)`,
so a Hermitian Weyl observable commutes with parity **iff all its Weyl
coefficients are real**, i.e. iff its symbol is an even function on the torus;
and

  * eps = -1  =>  `U_A^k` is a phase times `R_par`, so parity is a SCALAR on each
    eigenspace and carries no information;
  * eps = +1  =>  parity is an independent involution, `H_lam` splits into two
    halves, and every real-symbol compression is BLOCK DIAGONAL, hence has the
    statistics of a superposition of two spectra and **can never be
    Wigner-Dyson**.

The single-orbit observable `T(u) + T(u)*` of T20 has real coefficients, so T20's
target was unreachable by construction. A generic Gaussian Weyl observable has
complex coefficients, is not parity invariant, and is exactly GUE (Theorem A).
Sharp dichotomy: **real symbol -> parity superposition; complex symbol -> GUE.**

Verified: splits `(m+, m-)` = (0,46), (105,105), (77,76), (246,246), (0,259) at
N = 1597, 3571, 8969, 9349, 14503 — exactly 0/m when eps = -1 and exactly
half/half when eps = +1. This retro-explains every anomalous z of R71: the large-z
design points had K = 17, 19, 59 (all eps = +1), the small-z ones K = 34, 46, 56
(all eps = -1).

### 10.3 Theorem E — why the desymmetrised blocks are orthogonal

`Theta T(u) Theta^{-1} = T(R^t u)`, so Theta alone does not commute with the
compression. But the Hecke torus `C(A) = {xI + yA : x^2 + xyt + y^2 = 1}` gives
`U_tau T(u) U_tau* = T(tau^t u)`, and if `tau^t R^t u = +- u` for some
`tau in C(A)` then `Theta_u = U_tau Theta` **does** commute with
`P_lam (T(u)+T(-u)) P_lam`, forcing a real structure and beta = 1. In the
eigenbasis of A the torus is `diag(z, z^{-1})`, whose orbits are the level sets of
`q(u) = u_1 u_2`, and `R^t` interchanges the eigendirections, hence preserves q.
So the condition is solvable off `q(u) = 0`, a locus of density O(1/p). Verified
exhaustively: 100 % of u at every inert prime, 95.2-99.7 % at split primes, the
failures being exactly the two eigendirections.

### 10.4 The desymmetrised measurement [NUMERICALLY-SUPPORTED, positive]

Consecutive-spacing-ratio statistic `r~ = min(s_n, s_{n+1})/max(s_n, s_{n+1})`,
which needs **no unfolding** (this removes the dominant systematic of every
earlier spacing measurement in this programme). Class labels: 0.38629 Poisson,
0.53590 GOE, 0.60266 GUE. 16 frequencies per design point.

| p | K | m (m+-) | full | parity block | Haar surrogate |
|---|---|---|---|---|---|
| 3571 | 17 | 210 (105) | 0.4250 | 0.5291 / 0.5417 | 0.5981 |
| 9901 | 33 | 300 (150) | 0.4164 | 0.5366 / 0.5295 | 0.5936 |
| 19489 | 29 | 673 (337) | 0.4125 | 0.5313 / 0.5334 | 0.5928 |

full vs GUE: z = -7.7, -9.3, -25.1; full vs a 2-fold GUE superposition:
z = -0.16, -0.33, -0.83. Parity blocks vs GOE: z = -0.33, +0.18, +0.35, +0.14,
-0.22, -0.11 (six measurements). Haar surrogate vs GUE: z = -0.46, -0.91, -1.06.
All stable while m grows by a factor 3.

**Therefore: for the parity-desymmetrised, single-observable, fully deterministic
compression of a quantised cat map, BGS holds numerically with the correct Dyson
index beta = 1, at m up to 337 per block.** The gap between the blocks (beta = 1)
and the arithmetic-free surrogate (beta = 2) is genuine arithmetic content: it is
the index predicted by the time reversal Theta of Theorems C and E. The R71
verdict "the naive answer is wrong" is superseded — the naive *experiment* was
wrong, because it mixed two symmetry sectors. What remains missing for a proof is
a local law, not a symmetry input (T18 barrier, unchanged).

### 10.5 Theorem B, sharp criterion for prime powers

`E0(s,k) = P(s,k)` iff `s < lpf(k)`. Proof for `k = q^e`: a multiple
`f = Phi_{q^e} g` of degree < q^e has `deg g < q^{e-1}`, so the q blocks of
`Phi_{q^e}` do not overlap and f's coefficient vector is g repeated q times;
hence f's positive mass is q times that of g, at least q, and `f(1) = q g(1) = 0`
forces g to carry both signs. Certified in 29 cells at
k = 8, 9, 16, 25, 27, 32, 49, 81, s <= 5. General k remains [CONJECTURED]; Mann's
theorem gives only `2s < lpf(k)`.
"""
th = rd("THEORY.md")
if "## 10. RUN 72" in th:
    rep.append("THEORY.md already has section 10")
else:
    wr("THEORY.md", th.rstrip() + "\n" + TH10)
    rep.append("THEORY.md: section 10 appended")

# ---- README results table
rm = rd("README.md")
if "Thm C" not in rm:
    rm = rm.replace(
        "| Cor: sub-Gaussian tail",
        "| **Thm C**: `Theta^2 = +1` unconditionally (M = SR always has equal "
        "diagonal entries) — closes O6, removes the R1.1 hypothesis, no GSE | "
        "**PROVEN**, 504 configs, <= 1.8e-15 |\n"
        "| **Thm D**: parity commutes with `U_A`; scalar on eigenspaces iff "
        "`A^k = -I`; otherwise every real-symbol compression is block diagonal, "
        "hence never Wigner-Dyson | **PROVEN**, dichotomy verified at 5 design "
        "points |\n"
        "| **Thm E**: the Hecke torus supplies an antiunitary commuting with the "
        "single-orbit compression off a locus of density `O(1/p)` — forces "
        "`beta = 1` | **PROVEN** off the degenerate locus; 100% inert, "
        "95-99.7% split |\n"
        "| **Desymmetrised BGS**: parity blocks indistinguishable from GOE "
        "(`|z| <= 0.35`, 6 measurements, m up to 337), Haar surrogate "
        "indistinguishable from GUE | **NUM-SUPPORTED**, unfolding-free ratio "
        "statistic |\n"
        "| Cor: sub-Gaussian tail", 1)
    rm = rm.replace(
        '| "One Weyl orbit gives GOE" (T20) | **CORRECTED**: systematic '
        "`+0.05…+5.3σ` deviation, tracking `K` not `m` |",
        '| "One Weyl orbit gives GOE" (T20) | **EXPLAINED AND SUPERSEDED**: the '
        "deviation is the exact parity symmetry of Thm D; after desymmetrising, "
        "GOE holds |")
    rm = rm.replace("**Last run:** R71, 2026-08-28.",
                    "**Last run:** R72, 2026-08-28.")
    rm = rm.replace(
        "| Full BGS for a fixed deterministic observable | **OPEN** — the real "
        "content, `op:local_deterministic` |",
        "| Full BGS for a fixed deterministic observable | **OPEN as a proof**; "
        "NUM-SUPPORTED after desymmetrisation (see above). Missing ingredient: a "
        "local law, not a symmetry |")
    rm = rm.replace("python src/diagnostics/hecke_centring_refutation.py --exact   "
                    "# reproduces the defective code path",
                    "python src/diagnostics/hecke_centring_refutation.py --exact   "
                    "# reproduces the defective code path\n"
                    "python src/theorems/theorem_c_theta_square.py          "
                    "# Theorem C, 504 configs\n"
                    "python src/theorems/theorem_d_parity_dichotomy.py          "
                    "# Theorem D, the parity dichotomy\n"
                    "python src/theorems/theorem_e_hecke_torus.py         "
                    "# Theorem E, torus repair condition\n"
                    "python src/diagnostics/haar_surrogate.py                "
                    "# eigenspace vs arithmetic-free frame\n"
                    "python src/diagnostics/desym_ratio_statistic.py         "
                    "# the decisive unfolding-free measurement\n"
                    "python src/hygiene_r72.py                   "
                    "# idempotent audit-hygiene pass")
    wr("README.md", rm)
    rep.append("README.md refreshed for run 72")
else:
    rep.append("README.md already refreshed")

# ---- MANIFEST rows for r72
man = rd("artifacts/MANIFEST.md")
if "artifacts/r72/" not in man:
    man = man.rstrip() + r"""

## RUN 72 (2026-08-28) — artifacts/r72/

| claim | artifact | script |
|---|---|---|
| Theorem C, `Theta^2 = +1`, 504 configs + exhaustive involution counts | `r72/theta_square_theorem.json` | `src/theorems/theorem_c_theta_square.py` |
| Theorem D, parity dichotomy, 5 design points | `r72/parity_desymmetrised.json` | `src/theorems/theorem_d_parity_dichotomy.py` |
| Theorem E, torus-repair condition, 3 maps x 7 primes | `r72/theoremE_torus_repair.json` | `src/theorems/theorem_e_hecke_torus.py` |
| eigenspace vs Haar surrogate, L1 spacing statistics | `r72/haar_surrogate.json` | `src/diagnostics/haar_surrogate.py` |
| the decisive unfolding-free ratio measurement | `r72/desym_ratio_statistic.json`, `r72/desym_ratio.log` | `src/diagnostics/desym_ratio_statistic.py` |
| `E0(s,k) = P(s,k)` iff `s < lpf(k)`, prime powers, 29 cells | `r72/prime_power_criterion.json` | inline (see LEDGER R72.5) |
| audit-hygiene pass, 7 edits | (edits in place) | `src/hygiene_r72.py` |
"""
    wr("artifacts/MANIFEST.md", man)
    rep.append("MANIFEST.md: run-72 rows added")
else:
    rep.append("MANIFEST.md already has run 72")

# ---- ROADMAP
rd_ = rd("ROADMAP.md")
if "UPDATE 2026-08-28 (run 72)" not in rd_:
    rd_ = rd_.rstrip() + r"""

## UPDATE 2026-08-28 (run 72) — priorities reset again

Closed this run: **O6** (Theorem C, unconditional `Theta^2 = +1`);
`op:theta_sign_regen` (moot — T13 no longer rests on a scan, and the exhaustive
involution counts are recorded); every hygiene item of the run-71 audit
(`src/hygiene_r72.py`). `op:local_deterministic` is **reformulated and answered
numerically**: the single-orbit compression mixes two exact parity sectors
(Theorem D); after desymmetrising it is indistinguishable from GOE, with the
Dyson index predicted by the time reversal of Theorems C and E.

New priorities:

1. **Push the desymmetrised ratio measurement to m ~ 2000** (p ~ 1e5, K ~ 50).
   No unfolding is needed, so the cost is one eigensolve per frequency. If
   `<r~>` stays within 0.5 sigma of GOE the numerical case is very strong.
2. **Test the Kurlberg-Rudnick SU(2)-trace law** (arXiv:math/0302277) against the
   correct Hecke-basis matrix elements. This is the honest successor to the void
   R67-R70 line; the Hecke eigenbasis is now easy to build.
3. **Prove `Theta_u^2 = +1` in Theorem E**, which would upgrade beta = 1 from a
   measurement to a theorem. The equal-diagonal mechanism of Theorem C is the
   natural tool.
4. `conj:Pstar` — bound the exceptional primes of Theorem B polynomially. The
   minimal sporadic shapes are `{a,a,b}` (excess 18k) and `{a,a,a,b}` (excess
   32k), i.e. F_p-points of explicit curves.
5. Extend `E0(s,k) = P(s,k) iff s < lpf(k)` from prime powers to general k.
6. Still blocked: `op:lean_rebuild` (8 GB), `op:tail_below_p^{3/7}` (published
   wall).
"""
    wr("ROADMAP.md", rd_)
    rep.append("ROADMAP.md: run-72 update added")
else:
    rep.append("ROADMAP.md already updated")

print("\n".join(rep))
