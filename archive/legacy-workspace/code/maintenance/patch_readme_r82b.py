"""RUN 82 (continued) README patch: Theorem II, the derived comb, and the
large-m BGS test.  Written as a file (heredocs mangle backslashes here)."""
import io

P = "README.md"
s = io.open(P, encoding="utf-8").read()
NL = chr(10)

assert "**Single root:** this directory. **Last run:** R82, 2026-08-30." in s
rows = (
 "| **Thm II (R82)**: the family in CLOSED FORM — in the Hecke basis (= the "
 "multiplicative characters) `<f_chi|T(n)|f_psi> = e_N(-q/2) conj(chi)(n1) psi(n1) "
 "J(chi,psi;q)/(N-1)` with `J` a twisted Jacobi sum `sum_x conj(chi)(x) psi(x-1) "
 "e_N(qx)`, `|J| <= 2 sqrt N` by Weil–Deligne | **PROVEN**; `M_q` rebuilt from the "
 "sums alone reproduces the pipeline `mu_4` over EVERY level set (198 sets to "
 "6.1e-14 at N=199, 3570 sets to 2.4e-13 at N=3571), scale `c = L_{K-1}` |" + NL +
 "| **R82**: the second moment exactly — `Tr(C C*)` is a finite sum over the "
 "`(2K)^2` tuples `(sigma,tau,j,j')`; verified against the numeric trace 24/24 to "
 "5.2e-14. Hence the residual `E(q)` of `Tr(V_q^2) = N/K^2 + E(q)` is an exact "
 "exponential sum, and the measured Fibonacci comb is CONTAINED in the derived "
 "460-frequency set (16/16) | **PROVEN + certified** |" + NL +
 "| **R82: BGS tested at m_+ up to 2851** (11.6x the previous ceiling; the closed "
 "form removes the N x N wall). Per-system `<r~>` vs matched GOE MC at 8x samples: "
 "0.53135/0.53072/0.53153/0.53782 at m_+ = 336/837/1680/2851 against "
 "0.53073/0.53104/0.52963/0.53334 → z = +0.18/-0.14/+1.04/+1.27, z vs Poisson "
 "+43/+67/+95/+45; spacing KS inside the 95% noise floor everywhere (at m_+=2851 "
 "smaller than GOE's own); `Sigma^2(L)` matching within 1-2 sigma | "
 "**NUMERICALLY-SUPPORTED**, the strongest BGS evidence in this workspace |" + NL +
 "| **R82 calibration**: the remaining gap is a missing TECHNOLOGY, not a missing "
 "lemma — spacing universality has never been proven for any explicit "
 "deterministic family; Thm I shows this one has no independence to exploit and "
 "the moment route reaches only scale `1/log m`. The single missing input is "
 "quantitative entrywise decorrelation of the twisted Jacobi sums (a Katz-type "
 "equidistribution statement) | **OPEN, precisely located** |" + NL + NL)

rep = "## Layout" + NL
assert rep in s
s = s.replace(rep, rows + rep, 1)

anchor = ("py src/large_m/q_curve.py                     "
          "# R82: the full modulation curve q -> spec(V_q)")
assert anchor in s
s = s.replace(anchor, anchor + NL +
              "py src/large_m/normal_form.py                 # R82: equivariant normal form (moduli + coboundary)" + NL +
              "py src/theorems/theorem_ii_twisted_jacobi.py                 # R82: Theorem II, verified over every level set" + NL +
              "py src/large_m/bgs_large_m.py                 # R82: BGS at m_+ = 336, 837, 1680" + NL +
              "py src/large_m/bgs_large_m.py --big           # R82: BGS at m_+ = 2851" + NL +
              "py src/large_m/second_moment_exact.py         # R82: the exact second-moment tuple formula", 1)

io.open(P, "w", encoding="utf-8").write(s)
print("README updated:", len(s), "chars")
