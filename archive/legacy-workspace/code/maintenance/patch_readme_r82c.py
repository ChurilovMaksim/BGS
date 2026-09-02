"""RUN 82 (third block) README rows: hidden-degeneracy test and the C = C* diagnosis."""
import io

NL = chr(10)
P = "README.md"
s = io.open(P, encoding="utf-8").read()

rows = (
 "| **R82: no hidden degeneracies** - min bulk spacing and `N_pairs(t)`, "
 "t = 0.02..0.2, all within `+-2.1 sigma` of matched GOE with alternating signs "
 "at 3 designs (N = 3571/95419/144481); smallest-ever spacings behave like "
 "extreme-value draws; repulsion at full GOE strength. The subleading-coincidence "
 "failure mode - the last structural way BGS could fail here without aggregate "
 "statistics noticing - is excluded at ~10^4 pooled levels per design | "
 "**NUMERICALLY-SUPPORTED** |" + NL +
 "| **R82 diagnosis**: for the real-character (even) block `C_ij = conj(C_ji)` "
 "entrywise to 4e-11, so `M = C + C* = 2C` and the naive C/C* word split is "
 "structurally degenerate; `m(mu_4 - 2)` = 2.2-2.8 at m_+ = 105 (GOE scale, "
 "shape-modulation dominated) | recorded; exact-trace pipeline preserved |" + NL +
 NL)

rep = "## Layout" + NL
assert rep in s
s = s.replace(rep, rows + rep, 1)

anchor = ("py src/large_m/rigidity_control_v2.py            "
          "# R82: the unfolding-degree control that killed the artifact")
assert anchor in s
s = s.replace(anchor, anchor + NL +
  "py src/large_m/small_spacings.py              # R82: level repulsion / hidden-degeneracy test", 1)

io.open(P, "w", encoding="utf-8").write(s)
print("README updated:", len(s), "chars")
