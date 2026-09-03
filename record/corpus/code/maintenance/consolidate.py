"""Consolidation fixes: recursive path resolution in the audit, repair the stale
citations the audit found, tidy stray logs and empty directories. Idempotent."""
import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
rep = []


def rd(rel):
    return open(os.path.join(ROOT, rel), encoding="utf-8",
                errors="surrogateescape").read()


def wr(rel, s):
    open(os.path.join(ROOT, rel), "w", encoding="utf-8",
         errors="surrogateescape").write(s)


# --- 1. make the auditor resolve paths recursively (most "missing" were false)
p = "src/maintenance/consistency_audit.py"
s = rd(p)
old = """    cand = [p, os.path.join("artifacts", p), os.path.join("src", p)]
    if not any(os.path.exists(os.path.join(ROOT, c)) for c in cand):"""
new = """    base = os.path.basename(p)
    hit = os.path.exists(os.path.join(ROOT, p))
    if not hit:
        for d_, _, fs in os.walk(ROOT):
            if base in fs:
                hit = True
                break
    if not hit:"""
if old in s:
    wr(p, s.replace(old, new, 1))
    rep.append("auditor: path resolution made recursive")
else:
    rep.append("auditor: already recursive")

# --- 2. repair the citations that really are stale
fixes = {
    "ROADMAP.md": [
        ("`src/hygiene_r72.py`", "`src/maintenance/hygiene_r72.py`"),
        ("`src/theta_sign.py`",
         "`src/theta_sign.py` (absent; the claim it generated is now moot, "
         "Theorem C)"),
        ("`drafts/bgs_paper_complete.tex`",
         "`drafts/bgs_paper_complete.tex` (absent; superseded by "
         "`paper/exact_wd_and_subgroup_moments.tex`)"),
    ],
    "artifacts/MANIFEST.md": [
        ("`src/hygiene_r72.py`", "`src/maintenance/hygiene_r72.py`"),
        ("`src/patch_theory_r71.py`", "`src/maintenance/patch_theory_r71.py`"),
        ("`src/repair_legacy_paper.py`",
         "`src/maintenance/repair_legacy_paper.py`"),
        ("`campaign_tail_constant.py`",
         "`campaign_tail_constant.py` (absent on disk; historical)"),
    ],
    "README.md": [
        ("`src/hygiene_r72.py`", "`src/maintenance/hygiene_r72.py`"),
    ],
}
for doc, subs in fixes.items():
    s = rd(doc)
    n = 0
    for a, b in subs:
        if a in s and b not in s:
            s = s.replace(a, b)
            n += 1
    if n:
        wr(doc, s)
    rep.append(f"{doc}: {n} citation(s) repaired")

# --- 3. tidy stray logs into their run folders
moves = {"r73_desym_large_m.log": "r73", "r73_desym_large_m2.log": "r73"}
moved = []
for fn, dst in moves.items():
    src = os.path.join(ROOT, "artifacts", fn)
    if os.path.exists(src):
        os.makedirs(os.path.join(ROOT, "artifacts", dst), exist_ok=True)
        shutil.move(src, os.path.join(ROOT, "artifacts", dst, fn))
        moved.append(fn)
if moved:
    for doc in ("artifacts/MANIFEST.md", "README.md", "LEDGER.md", "THEORY.md"):
        s = rd(doc)
        for fn in moved:
            s = s.replace(f"`{fn}`", f"`r73/{fn}`").replace(
                f"artifacts/{fn}", f"artifacts/r73/{fn}")
        wr(doc, s)
rep.append(f"stray logs moved into artifacts/r73/: {moved or 'none'}")
# the two remaining root-level logs belong to the legacy runs; leave them but say so
note = os.path.join(ROOT, "artifacts", "README_logs.txt")
if not os.path.exists(note):
    with open(note, "w", encoding="utf-8") as fh:
        fh.write("audit_verify_all2_rerun.log and ring1_rerun_audit_tail_bound.log\n"
                 "are legacy run logs (pre-R71) kept at this level for provenance;\n"
                 "run-specific logs live in artifacts/r71..r74/.\n")
    rep.append("artifacts/README_logs.txt written")

# --- 4. empty directories
removed = []
for d_ in ("src/archive/debug_scratch", "_archive/run70_portable_shell/BGS"):
    full = os.path.join(ROOT, d_)
    if os.path.isdir(full) and not os.listdir(full):
        os.rmdir(full)
        removed.append(d_)
rep.append(f"empty directories removed: {removed or 'none'}")

print("\n".join(rep))
