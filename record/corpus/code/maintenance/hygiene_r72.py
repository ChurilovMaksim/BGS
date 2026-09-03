"""Run-72 hygiene pass: close every remaining defect listed in the 2026-08-28
audit (`review/audits/2026-08-28/ledger_claim_map.md` section 7).  Idempotent;
each edit verifies its target first and reports NOOP if already applied."""

import json
import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rep = []


def rd(p):
    return open(os.path.join(ROOT, p), encoding="utf-8", errors="surrogateescape").read()


def wr(p, s):
    open(os.path.join(ROOT, p), "w", encoding="utf-8",
         errors="surrogateescape").write(s)


# ---------------------------------------------------------------- H1  bad JSON
p = "artifacts/ring2/discriminator.json"
s = rd(p)
try:
    json.loads(s)
    rep.append("H1  NOOP  discriminator.json already valid")
except Exception:
    import re
    fixed = re.sub(r",(\s*[}\]])", r"\1", s)
    json.loads(fixed)                      # will raise if still broken
    wr(p, fixed)
    rep.append("H1  fixed trailing comma in artifacts/ring2/discriminator.json")

# ------------------------------------------------------- H2  broken REPRO paths
p = "artifacts/ring3/REPRO.md"
s = rd(p)
subs = 0
for bad, good, note in [
    ("`artifacts/ring2/big_sweep.json` (Deligne line B)",
     "`artifacts/ring2/line_B_big_sweep.json` (Deligne line B)",
     "line_B_big_sweep"),
    ("`artifacts/ring0/MOVE_COUNT.json` (move_count = 0)",
     "`artifacts/ring3_hygiene.json` (the ring-0 move count was folded into "
     "the ring-3 hygiene artifact; `artifacts/ring0/` does not exist)",
     "ring0 MOVE_COUNT"),
]:
    if bad in s:
        s = s.replace(bad, good)
        subs += 1
if subs:
    hdr = ("> **Run-72 correction (2026-08-28).** Two cited paths in this file "
           "did not exist: `artifacts/ring2/big_sweep.json` (the real name is "
           "`line_B_big_sweep.json`) and `artifacts/ring0/MOVE_COUNT.json` (no "
           "`ring0/` directory was ever written). Both are corrected below. "
           "The Deligne line-B headline in row 5, `max |S|/Weil = 0.99999`, is "
           "**withdrawn**: the JSON field is `ratio_over_weil_only` with "
           "`weil_only = min(k, 2 sqrt p) = 4`, so the true ratio to `2 sqrt p` "
           "is 0.032 and the datum says the *trivial* bound is tight.\n\n")
    s = hdr + s
    wr(p, s)
    rep.append(f"H2  repaired {subs} paths + withdrew the 0.99999 headline in REPRO.md")
else:
    rep.append("H2  NOOP  REPRO.md paths already repaired")

# ------------------------------------- H3  quarantine retracted r6 artifacts
os.makedirs(os.path.join(ROOT, "artifacts", "retracted"), exist_ok=True)
moved = []
for fn in ("run16_r6.json", "run22_classify.json", "run25_partition.json"):
    src = os.path.join(ROOT, "artifacts", fn)
    dst = os.path.join(ROOT, "artifacts", "retracted", fn)
    if os.path.exists(src):
        shutil.move(src, dst)
        moved.append(fn)
if moved:
    note = os.path.join(ROOT, "artifacts", "retracted", "README_r6_signbug.txt")
    with open(note, "w", encoding="utf-8") as fh:
        fh.write(
            "Quarantined 2026-08-28 (run 72), per the run-71 audit.\n\n"
            "run16_r6.json, run22_classify.json, run25_partition.json were\n"
            "produced by the r=6 driver that carried the sign bug recorded in\n"
            "LEDGER R32-R42 (MASTER AUDIT SUMMARY). They are retained for\n"
            "provenance only and must not be cited. The live r<=5 evidence is\n"
            "artifacts/master_general.json, regenerated 2026-08-28 (5/5 PASS).\n")
    rep.append(f"H3  quarantined {', '.join(moved)} into artifacts/retracted/")
else:
    rep.append("H3  NOOP  r6 artifacts already quarantined")

# ------------------------------- H4  in-place retraction warnings in LEDGER.md
LED = "LEDGER.md"
s = rd(LED)
WARN = {
    "## R11-C EXTENSION TO ALL FIXED EVEN ORDERS":
        "> **RETRACTION WARNING (added 2026-08-28, run 72).** This section is\n"
        "> downstream of the R11 fine-scale theorem, retracted as R12-A. The\n"
        "> `k = o(p^{1/(r-1)})` all-even-moments claim is **VOID**. What survives\n"
        "> is the fixed-order statement `Tr(V_lam^r) = WD_r + O_F(k^r/p^2)` for\n"
        "> r <= 4 with no threshold on k.\n",
    "## RUN 16: r=6 EXTENSION - FIRST DATA [R16]":
        "> **RETRACTION WARNING (added 2026-08-28, run 72).** The r=6 driver used\n"
        "> here carried the sign bug found in the R32-R42 audit. The artifacts\n"
        "> `run16_r6.json`, `run22_classify.json`, `run25_partition.json` are\n"
        "> quarantined in `artifacts/retracted/` and must not be cited.\n",
    "## RUN 22: r=6 CLASSIFICATION FIRST DATA [R22]":
        "> **RETRACTION WARNING (added 2026-08-28, run 72).** Same r=6 sign bug\n"
        "> as R16; artifacts quarantined in `artifacts/retracted/`.\n",
    "## RUN 20: UNIVERSAL CONSTANT CAMPAIGN [R20-TIGHT]":
        "> **CORRECTION (added 2026-08-28, run 72).** The tail-bound constant is\n"
        "> **2**, not 1: `audit_tail_bound.py` records 0/196 violations of\n"
        "> `N_3 <= floor(k^2/p) + 2` but 10 violations of the `+1` form. Any\n"
        "> statement here at constant 1 is void.\n",
    "## RUN 13 FINAL: FULL PAPER + QUANTUM EXPERIMENT":
        "> **RETRACTION WARNING (added 2026-08-28, run 72).** The quantum\n"
        "> experiment of this run is superseded: `artifacts/retracted/\n"
        "> run13_quantum_w4.json` is already quarantined, and the observable\n"
        "> used was a random Weyl combination, for which exactly-GUE statistics\n"
        "> are a theorem with no arithmetic content (run 71, Theorem A). The\n"
        "> measurement is therefore not evidence about BGS.\n",
}
added = 0
for anchor, warn in WARN.items():
    if anchor in s and warn.split("\n")[0] not in s.split(anchor)[0][-1200:]:
        s = s.replace(anchor, warn + "\n" + anchor, 1)
        added += 1
if added:
    wr(LED, s)
    rep.append(f"H4  inserted {added} in-place retraction warnings in LEDGER.md")
else:
    rep.append("H4  NOOP  LEDGER warnings already present")

# ------------------------------- H5  THEORY: mark the refuted C1 support
TH = "THEORY.md"
s = rd(TH)
anchor = "Empirical support: for F = {|n_i| <= 2}"
anchor2 = "Empirical support: for F = {|n_i| ≤ 2}"
if "REFUTED (run 3 audit" not in s:
    for a in (anchor, anchor2):
        if a in s:
            s = s.replace(a, "**REFUTED (run 3 audit; see the banner at the top "
                             "of this file): raw N_4 is ~99% non-Wigner, so the "
                             "coincidence quoted below is not support for C1.** "
                             "Historical text: " + a, 1)
            wr(TH, s)
            rep.append("H5  flagged the refuted C1 empirical support in THEORY.md")
            break
    else:
        rep.append("H5  NOOP  C1 support anchor not found")
else:
    rep.append("H5  NOOP  C1 support already flagged")

# ------------------------------- H6  MANIFEST: flag the never-existing rows
MAN = "artifacts/MANIFEST.md"
s = rd(MAN)
if "NEVER EXISTED BEFORE 2026-08-28" not in s:
    s = ("> **Run-72 provenance warning.** The rows citing "
         "`run13_strong_master.json` and `run13_master_cert.json` refer to files "
         "that **NEVER EXISTED BEFORE 2026-08-28**: they were absent from the "
         "121-file pre-run snapshot in `review/audits/2026-08-28/pre/` and were "
         "created for the first time by the run-71 re-run. No number in them was "
         "ever independently reproduced before that date.\n\n") + s
    wr(MAN, s)
    rep.append("H6  added the MANIFEST provenance warning")
else:
    rep.append("H6  NOOP  MANIFEST warning already present")

# ------------------------------- H7  T13 row in the legacy paper -> unconditional
PA = "archive/papers/resonance_laws_catmaps.tex"
s = rd(PA)
old = "PROVEN on the\nchart $\\gcd(M_{21},N)=1$ (every"
if old in s:
    s = s.replace(
        old,
        "PROVEN UNCONDITIONALLY (run 72, Thm.~C: $M=SR$ always has\n"
        "$M_{11}=M_{22}$, so the $y$-Gauss-sum in $U_M\\overline{U_M}$ collapses\n"
        "to $N\\delta_{x,z}$ and $\\Theta^2=+1$ exactly; the condition\n"
        "$\\gcd(M_{21},N)=1$ is merely the well-definedness of the kernel, not a\n"
        "hypothesis). Certified at 504 configurations, $\\le1.8\\times10^{-15}$;\n"
        "supersedes the numerical scan (every", 1)
    wr(PA, s)
    rep.append("H7  legacy paper T13 row upgraded to the unconditional Theorem C")
else:
    rep.append("H7  NOOP  T13 row already updated or anchor changed")

print("\n".join(rep))
