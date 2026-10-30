# Referee certificate of record for V_0 (adopted, Line H fix 1)

Origin: the independent referee audit of Line H (/workspace/audit/lineH, REPORT.md, 2026-10-30, about 20:40 UTC+5). The files are
copied **unchanged**; their sha256 values are in `SHA256.txt` and agree with `/workspace/audit/lineH/logs/SHA256_audit.txt`.

* `ref_rig.py` is the referee's independent implementation. It uses:
  * the rounding constant √2·γ_{2n+2};
  * an a-posteriori Householder residual;
  * norms inflated by a factor 1+1e−6.
* `refV0.json` is its output on the certified matrices `data/prodV_b0_{mid,rad}.npy` and the build bounds `data/prodV.json`.
  * At R = 1.5, r₁ = 0.05: F·R₁ = 0.8947 and F·R₂ = 0.5916, so the certificate holds. That gives |μ*| ∈ [1.84683479522, 1.94683479523].
  * R = 1.55 is also certified.
* `refE0.json` is the referee's independent E_0 rest certificate: F = 0.024 at R = 1.0.
* `ref_bounds.py` re-decides every certificate and the all-m chain in exact rationals. `ref_entries.py` makes an independent check of
  the Galerkin entries.

**Status.** `refV0.json` is the **V_0 certificate of record**. The author's re-run with the archived code is a second, consistent
certificate: `code/rig_spec.py` v4, sha256 in `logs/SHA256_code_v4_runs.txt`, output `logs/v4_V0_dom.json`.

**Caveat (also noted by the author).** `ref_rig.py` reads δ₁, δ₂, Δ and ‖X‖ from JSON floats without upward padding. That is at most a
1-ulp effect, about 1e−16 relative, against a margin of at least 10% (F·R₁ = 0.895). The v4 author run pads these inputs by 1+2⁻⁴⁰.
