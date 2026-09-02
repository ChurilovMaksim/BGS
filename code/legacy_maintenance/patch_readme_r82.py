"""RUN 82 README patch (written as a file, not a heredoc -- LESSON on this box:
bash heredocs mangle backslashes)."""
import io

BS = chr(92)
P = "README.md"
s = io.open(P, encoding="utf-8").read()


def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)


rep("**Single root:** this directory. **Last run:** R80, 2026-08-29.",
    "**Single root:** this directory. **Last run:** R82, 2026-08-30.")

rows = (
 "| **Thm I (R82)**: the observable family is a ONE-PARAMETER arithmetic curve "
 "— `V_n = P_+(T(n)+T(-n))P_+` depends on `n` only through the Hecke-torus "
 "invariant `Q(n) = n1^2 - n1 n2 - n2^2 mod N`, so there are at most `N` "
 "distinct spectra, not `(N^2-1)/K`; each nonzero level set is one torus orbit "
 "carrying `|T|/K = m` cat-map orbits | **PROVEN**, 15/15 certificates at 3 "
 "designs (full spectra agree to 2e-13 across 8 distinct orbits per level set; "
 "11-13 decades of separation between levels); combinatorial half machine-checked "
 "in Lean (`formal/`) |" + chr(10) +
 "| **Cor (R82)**: the R81.4 \"coherent arithmetic fluctuation mode\" IS that "
 "curve; an i.i.d.-GOE ensemble statement is false for an exact reason; ensemble "
 "averaging over `n` equals averaging over the single scalar `q`, so it cannot "
 "substitute for a per-system local law | **PROVEN** (given Thm I) — supersedes "
 "the R81.4/R81.5 \"modulated universality, driver unknown\" reading |" + chr(10) +
 "| **R82**: the modulation in closed form — a Fibonacci frequency comb: 16 "
 "frequencies `+-v_j` (`A^j = u_j I + v_j A`, `v_j = 1,3,8,21,55,144,377,987`) "
 "carry 90% of the variance of `Tr(V_q^4)` and `Tr(V_q^6)`; an 8-pair fit gives "
 "`R^2 = 0.9426` for `Tr(V_q^4)` and **0.98655** for `mu_4(q)`, exhaustively over "
 "all 3570 level sets | **NUMERICALLY-SUPPORTED** (coefficients fitted, not "
 "derived); consistent with Kurlberg-Rudnick's SU(2)-trace conjecture for matrix "
 "elements |" + chr(10) +
 "| **R82**: the even/odd split of the R81.4 excess — `Var_arith/Var_GOE` = "
 "81/71/78/100 at Chebyshev modes `k = 4,6,8,10` versus 1.0/1.6/2.8/5.8 at "
 "`k = 3,5,7,9` (m+ = 105), and 375/306/302/352 versus 0.5/2.9/5.2/10.8 at "
 "m+ = 246; Haar control 0.3-0.6 throughout | **NUMERICALLY-SUPPORTED**, matched "
 "GOE reference at 4x samples |" + chr(10) +
 "| **R82**: `op:dpbug` CLOSED — the dense relation-count DP was correct; "
 "R81.6's retraction of it came from a width-cap mismatch inside the CHECK. Exact "
 "BigInt run to `R = 150` passing supermultiplicativity at every pair: "
 "`S(150) = 1.87137e53`, hence **`2.265415 <= C_dense <= 3`** | **PROVEN "
 "(sandwich)** / R81.6 partly retracted |" + chr(10) + chr(10))

rep("## Layout" + chr(10), rows + "## Layout" + chr(10))

rep("paper/       two articles (.tex + .pdf)",
    "formal/      Lean 4 project (no Mathlib): machine-checked counting core of Thm I"
    + chr(10) + "paper/       two articles (.tex + .pdf)")

old_env = ("Environment: Python " + chr(8805) + "3.13 with `numpy`, `scipy`, `sympy`; Julia 1.11.9 at"
           + chr(10) + "`C:" + BS + "Tools" + BS + "julia" + BS + "julia-1.11.9" + BS + "bin" + BS
           + "julia.exe` for `tools/*.jl`; Lean 4.33.1 with the" + chr(10)
           + "mathlib cache at `C:" + BS + "Users" + BS + "churi" + BS + "lean-projects" + BS
           + "mephisto-lean` (a full `lake build`" + chr(10) + "still exceeds 8 GB RAM).")
new_env = ("Environment (re-probed R82, 2026-08-30): Python 3.13.6 with `numpy`, `scipy`,"
           + chr(10) + "`sympy` (invoked as `py`, not `python`); Julia 1.11.4 at" + chr(10)
           + "`C:" + BS + "Users" + BS + "churi" + BS + "AppData" + BS + "Local" + BS
           + "Programs" + BS + "Julia-1.11.4" + BS + "bin" + BS + "julia.exe` (the" + chr(10)
           + "`C:" + BS + "Tools" + BS + "julia` path in older text does NOT exist);"
           " Lean/lake 4.33.1 via elan —" + chr(10)
           + "the workspace-internal project `formal/` builds with `lake build` and needs no"
           + chr(10) + "Mathlib; 6 cores, 15.94 GB RAM.  The external `C:" + BS + "Users" + BS
           + "churi" + BS + "lean-projects" + BS + "`" + chr(10)
           + "tree referenced by R80.7 is GONE, so that run's Lean claim has no retrievable"
           + chr(10) + "artifact (LESSON 82-E: load-bearing artifacts live inside the workspace).")
rep(old_env, new_env)

rep("julia src/large_m/julia_bigdp.jl                # R80 (Julia): S(R) to R=80",
    "julia src/shape_automaton/dp_exact.jl                  # R82 (Julia): exact self-checking count DP" + chr(10) +
    "julia src/shape_automaton/dp_push.jl 150 240          # R82 (Julia): exact S(R) to R=150 -> C_dense >= 2.265415" + chr(10) +
    "py src/large_m/shape_modes.py                  # R82: Chebyshev decomposition of the R81.4 excess" + chr(10) +
    "py src/large_m/density_shape.py               # R82: macroscopic law, outliers, resonance count C_4" + chr(10) +
    "py src/large_m/orbit_invariant.py             # R82: orbit invariance + exact-projector two-key check" + chr(10) +
    "py src/large_m/torus_rigidity.py              # R82: Theorem I, certificates C1-C5, three designs" + chr(10) +
    "py src/large_m/q_curve.py                     # R82: the full modulation curve q -> spec(V_q)" + chr(10) +
    "cd formal && lake build                    # R82: Lean certificate for the counting core of Thm I" + chr(10) +
    "julia src/large_m/julia_bigdp.jl                # R80 (Julia): S(R) to R=80")

io.open(P, "w", encoding="utf-8").write(s)
print("README updated:", len(s), "chars")
