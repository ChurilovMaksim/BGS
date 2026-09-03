"""
Consolidation pass: cross-check every cited path and every headline number in the
papers against the artifacts, and report anything stale, missing or inconsistent.
Read-only; it fixes nothing, it only reports.
"""

from __future__ import annotations

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
problems: list[str] = []
notes: list[str] = []


def rd(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8",
              errors="surrogateescape") as fh:
        return fh.read()


def art(rel):
    return json.load(open(os.path.join(ROOT, "artifacts", rel), encoding="utf-8"))


# ------------------------------------------------ 1. cited paths must exist
print("1. CITED PATHS")
cited = set()
for doc in ("README.md", "artifacts/MANIFEST.md", "ROADMAP.md"):
    txt = rd(doc)
    for m in re.finditer(r"`([A-Za-z0-9_./\\-]+\.(?:py|jl|json|md|tex|pdf|log))`", txt):
        cited.add((doc, m.group(1)))
missing = []
# citations explicitly annotated "(absent ...)" in the document are intentional
cited = {(doc, q) for (doc, q) in cited
         if f"`{q}` (absent" not in rd(doc)}
for doc, p in sorted(cited):
    base = os.path.basename(p)
    hit = os.path.exists(os.path.join(ROOT, p))
    if not hit:
        for d_, _, fs in os.walk(ROOT):
            if base in fs:
                hit = True
                break
    if not hit:
        missing.append((doc, p))
print(f"   {len(cited)} distinct cited paths, {len(missing)} missing")
for doc, p in missing:
    problems.append(f"MISSING PATH cited in {doc}: {p}")
    print(f"   MISSING  {doc} -> {p}")

# ------------------------------------------- 2. headline numbers in the papers
print("2. HEADLINE NUMBERS vs ARTIFACTS")
checks = []


def close(a, b, tol=5e-3):
    return abs(a - b) <= tol * max(1.0, abs(b))


# Theorem A certification
d = art("r71/theoremB_covariance.json")
w = max(r["B2_cov_rel"] for r in d["rows"])
checks.append(("Thm A: max B2 covariance deviation <= 3.3e-14", w <= 3.3e-14, w))

# Theorem C
d = art("r72/theta_square_theorem.json")
v = d["verdict"]
checks.append(("Thm C: 504 configurations certified",
               v["C2_configs_certified"] == 504, v["C2_configs_certified"]))
checks.append(("Thm C: worst |Theta^2-1| <= 1.8e-15",
               v["C2_worst_theta2_deviation"] <= 1.8e-15,
               v["C2_worst_theta2_deviation"]))
checks.append(("Thm C: O6 closed", v["O6_closed"] is True, v["O6_closed"]))

# Theorem D dichotomy
d = art("r72/parity_desymmetrised.json")
splits = {r["N"]: (r["m_plus"], r["m_minus"]) for r in d["rows"]}
checks.append(("Thm D: splits (0,46),(105,105),(77,76),(246,246),(0,259)",
               splits == {1597: (0, 46), 3571: (105, 105), 8969: (77, 76),
                          9349: (246, 246), 14503: (0, 259)}, splits))
checks.append(("Thm D: dichotomy holds everywhere",
               d["verdict"]["D3_dichotomy_holds_everywhere"] is True,
               d["verdict"]["D3_dichotomy_holds_everywhere"]))

# ratio statistic table
d = art("r72/desym_ratio_statistic.json")
tab = {r["p"]: (round(r["measured"]["full"]["rtilde_mean"], 4),
                round(r["measured"]["plus"]["rtilde_mean"], 4),
                round(r["measured"]["minus"]["rtilde_mean"], 4),
                round(r["measured"]["haar"]["rtilde_mean"], 4)) for r in d["rows"]}
checks.append(("R72.4 full <r~> = 0.4250/0.4164/0.4125",
               [tab[p][0] for p in (3571, 9901, 19489)] == [0.4250, 0.4164, 0.4125],
               [tab[p][0] for p in (3571, 9901, 19489)]))
checks.append(("R72.4 haar <r~> = 0.5981/0.5936/0.5928",
               [tab[p][3] for p in (3571, 9901, 19489)] == [0.5981, 0.5936, 0.5928],
               [tab[p][3] for p in (3571, 9901, 19489)]))

# Theorem E operator level
d = art("r73/theoremE_operator.json")
v = d["verdict"]
checks.append(("Thm E: 81 configs, W = +I always, Theta_u^2 = +1 always",
               d["totals"]["checked"] == 81 and d["totals"]["W_eq_plusI"] == 81
               and d["totals"]["c_plus1"] == 81,
               (d["totals"]["checked"], d["totals"]["W_eq_plusI"],
                d["totals"]["c_plus1"])))
checks.append(("Thm E: block real-structure defect <= 2.9e-14",
               v["block_real_structure_max"] <= 2.9e-14,
               v["block_real_structure_max"]))
checks.append(("Thm E: upgraded to theorem",
               v["E_upgraded_to_theorem"] is True, v["E_upgraded_to_theorem"]))

# Hecke dichotomy
d = art("r73/hecke_matrix_elements.json")
row = {r["p"]: r for r in d["rows"]}
for p, dk, ok_ in ((1597, -1.0009, 0.0073), (3571, -1.0184, -0.0028),
                   (9349, -0.9771, -0.0014)):
    pf = row[p]["per_frequency"]
    checks.append((f"Hecke p={p}: diag kurt {dk}",
                   close(pf["diag_kurt"]["mean"], dk, 2e-3),
                   round(pf["diag_kurt"]["mean"], 4)))
    checks.append((f"Hecke p={p}: offdiag kurt {ok_}",
                   close(pf["off_kurt"]["mean"], ok_, 2e-2),
                   round(pf["off_kurt"]["mean"], 4)))

# Lemma F
d = art("r73/lemmaF_quadratic_phase.json")
checks.append(("Lemma F: 5000 out-of-sample checks, 0 mismatches",
               d["verdict"]["total_out_of_sample_checks"] == 5000
               and d["verdict"]["max_mismatches_per_J"] == 0,
               (d["verdict"]["total_out_of_sample_checks"],
                d["verdict"]["max_mismatches_per_J"])))
d = art("r73/lemmaF_closed_form.json")
checks.append(("Lemma F: one universal sign convention",
               d["verdict"]["conventions"] == ["(1, -1, -1)"],
               d["verdict"]["conventions"]))

# Theorem G
d = art("r73/barrier_slack.json")
rr = [x for row in d["rows"] for x in row["data"] if x["r"] >= 4]
lo, hi = min(x["ratio_to_l1"] for x in rr), max(x["ratio_to_l1"] for x in rr)
checks.append(("Thm G: max|S_J|/||a||_1 in [0.22, 0.53]",
               0.21 <= lo and hi <= 0.54, (round(lo, 3), round(hi, 3))))
lo2 = min(x["ratio_to_l2"] for x in rr)
hi2 = max(x["ratio_to_l2"] for x in rr)
checks.append(("Thm G: max|S_J|/||a||_2 in [7.5, 18.3]",
               7.4 <= lo2 and hi2 <= 18.4, (round(lo2, 2), round(hi2, 2))))

# run 74
d = art("r74/ensemble_moments.json")
checks.append(("R74.2: 1600 Chebyshev checks, 0 mismatches",
               sum(r["trials"] for r in d["C1"]) == 1600
               and sum(r["mismatches"] for r in d["C1"]) == 0,
               (sum(r["trials"] for r in d["C1"]),
                sum(r["mismatches"] for r in d["C1"]))))
d = art("r74/ensemble_excess.json")
ex = {(r["N"], r["r"]): r for r in d["rows"]}
checks.append(("R74.4: exact at r=2,4 for eps=+1",
               all(ex[(N, r)]["excess_X_r"] == 0
                   for N in (3571, 9349) for r in (2, 4)), "ok"))
checks.append(("R74.4: D_8(3571) = 122637830, trivial 117173350",
               ex[(3571, 8)]["D_r_mod_N"] == 122637830
               and ex[(3571, 8)]["trivial_effective"] == 117173350,
               (ex[(3571, 8)]["D_r_mod_N"], ex[(3571, 8)]["trivial_effective"])))

# subgroup moments
d = art("r71/moment_certification.json")
checks.append(("Thm B: Bessel closed form 40/40",
               len(d["C3"]) == 40 and all(r["equal"] for r in d["C3"]),
               len(d["C3"])))
d = art("r71/Pstar_prime_k.json")
ps = {(r["k"], r["s"]): r["P_star"] for r in d["rows"]}
checks.append(("Thm B: P*(13,4) = 911, P*(11,7) = 6469",
               ps.get((13, 4)) == 911 and ps.get((11, 7)) == 6469,
               (ps.get((13, 4)), ps.get((11, 7)))))

# Hecke-centring refutation
d = art("r71/hecke_centring_undivided.json")
r64 = [r for r in d["rows"] if r["basis"] == "project_bug_U_columns"
       and r["n_hecke"] == 64]
checks.append(("R71.6: undivided reductions 239.5x and 1432.7x reproduced",
               any(230 <= r["reduction"] <= 250 for r in r64)
               and any(1400 <= r["reduction"] <= 1470 for r in r64),
               [round(r["reduction"], 1) for r in r64]))

bad = 0
for name, ok, val in checks:
    if not ok:
        bad += 1
        problems.append(f"NUMBER MISMATCH: {name} -> measured {val}")
    print(f"   {'OK  ' if ok else 'FAIL'} {name}   ({val})")
print(f"   {len(checks) - bad}/{len(checks)} headline numbers confirmed")

# ------------------------------------------------------ 3. hygiene
print("3. HYGIENE")
stray = []
for f in sorted(os.listdir(os.path.join(ROOT, "artifacts"))):
    if f.endswith(".log"):
        stray.append(f"artifacts/{f}")
for d_, _, fs in os.walk(ROOT):
    if "__pycache__" in d_:
        stray.append(os.path.relpath(d_, ROOT))
empty = [os.path.relpath(d_, ROOT) for d_, ds, fs in os.walk(ROOT)
         if not ds and not fs]
print(f"   stray root-level logs / caches: {stray}")
print(f"   empty directories: {empty}")
notes.append(f"stray={stray}")
notes.append(f"empty={empty}")

print()
print("=" * 70)
print(f"PROBLEMS: {len(problems)}")
for p in problems:
    print("  -", p)
print(f"NOTES: {notes}")
sys.exit(1 if problems else 0)
