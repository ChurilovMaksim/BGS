"""Record R82.21 in THEORY.md and MANIFEST (file-based; heredocs mangle parens)."""
import io

NL = chr(10)

add = (
 NL + "### 19.8 The Catalan law: status after the crossing experiment [R82.21]" + NL + NL +
 "Proven (19.5): the `k <= 2` values.  The attempted proof of the `k >= 3`" + NL +
 "deficits by showing that crossing matchings contribute zero FAILED," + NL +
 "informatively: the whole-product constraint `prod(c x_i - 1) = h prod(x_i - 1)`" + NL +
 "does not depend on the matching, so a per-matching decomposition is not" + NL +
 "well-defined at that level; the correct object is the pairing of EXPANDED" + NL +
 "factors (`op:pairing`).  The Catalan law itself is confirmed independently by" + NL +
 "direct summation at a 4th design and 5th moment: deviations of" + NL +
 "`<|J|^{2k}>/N^k` from `C_k` are -0.013/-0.034/-0.096/-0.283 at N = 19489 and" + NL +
 "-0.003/-0.010/-0.033/-0.110 at N = 95419 (k = 2..5), decaying faster than" + NL +
 "`N^{-1/2}`, while the factorial alternative is excluded at 100x sigma" + NL +
 "(e.g. e8: 13.97 +- 0.03 vs 24)." + NL)
with io.open("THEORY.md", "a", encoding="utf-8") as f:
    f.write(add)

row = ("| **R82.21 Catalan law cross-verified** at a 4th design (N=19489, K=29) and "
       "k=5: deviations from C_k = -0.013/-0.034/-0.096/-0.283 (N=19489), "
       "-0.003/-0.010/-0.033/-0.110 (N=95419) for k=2..5, faster than N^{-1/2} decay; "
       "factorial alternative dead (e8: 13.97+-0.03 vs 24). The per-matching "
       "decomposition attempt FAILED (constraint is matching-independent) - `op:pairing` "
       "is the named open problem | `r82/catalan_verify.json`, "
       "`sixth_moment_direct.json`, `crossing_deficit.json` (negative), logs | "
       "inline (LEDGER R82.21) |" + NL)
with io.open("artifacts/MANIFEST.md", "a", encoding="utf-8") as f:
    f.write(row)
print("THEORY 19.8 + MANIFEST row written")
