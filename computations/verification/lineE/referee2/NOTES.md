> **Repository copy.** Absolute scratch-directory paths of the audit machine are replaced by placeholders in angle brackets (`<referee-dir>` = the first referee's working tree, copied to `computations/verification/lineE/referee/`; `<referee2-dir>` = this audit's working tree, copied to `computations/verification/lineE/referee2/`; `<author-packet>` = the author packet; `<audit-clone>` = a fresh clone of the repository). They are not part of the repository. The text is otherwise unchanged.

# PR57 audit notes
- cloned <audit-clone>, branch pr57 = e3b83dcb, base 347f1730 OK
## 09:3x
- LineE.lean sha b3a91202 = refereed copy (unchanged) OK
- Lean pkgs copied from <lean-build-tree> (manifest identical), cache get running -> lake_cache_get.log
- Paper: E11 OK. E12 re-derived (split, mod8, mod a^2 via beta-bar identity beta-bar = beta*lambda^m, (1-l^-m)sum n sigma identity) OK.
  Prop G re-derived (shift identity, gamma=-t'Hw, char term integer since h|sum z, t=(16nu)^-1) OK, sign e(+tR/h).
- Nit: doc says "gamma in {11,38} one value per root r" -- Lean cert49 uses one root (li=32) with gamma=11 (s=+1), 38 (s=-1); gamma=-s*iota(c): depends on (r,s).
- Nit: cert_class F_lower sums ALL 4 residues (±196 and ±4) not "two residues alone" (diff ~5.6e-4 in F/2m at m=11).
- zres errbound: products recursion OK (BPZ sqrt5 u), row sums sqrt2 gamma_n n(1+e) OK, long double totals OK. Check compile flags/binary used.
- Own interval kernel code/ivsum.c (FE_UPWARD intervals) + code/ivcert.py. m=5,7 match author to 1e-12. m=11 f_B: F/2m>=3.52270646930, Wrest/m>=3.04541293860 (author 3.5227064692, 3.0454129383) CONFIRMED. width 5e-6.
- m=13 running in bg -> logs/ivcert_m13.out
- Lean: build OK (Bgs.LineE 40s, LineEResonance 22s); axioms <= propext,Classical.choice,Quot.sound; no sorry/native_decide; my controls (wrong kappa/gamma/nu/s/m=9) -> false; Neg57 decide fails as expected. logs/lean_audit.out, lean_neg.out
- E12 exact phase identity with theorem's own kappa/gamma formulas: 178/178 OK (a=1,7,17,23,31; m 5..25; both roots, s=±1). logs/e12_phase.log. gamma=-s*iota_r(c): (r=10,s=+)->11, (r=39,s=-)->11.
- Prop G vs n-sum non-even complex kick: m=3 4e-8, m=5 6e-6 at L=12 (truncation), sign-flip control breaks (rel 4.8, 25). logs/propG_nsum*.log
- e12_trace.py running (Galerkin 49-state vs brute) -> logs/e12_trace.log
- repo checks: all render --check OK, sci registry OK (280 claims), repository_audit PASS; bibliographic_metadata_audit --self-test rc=1 (EXT-BR-1975 dependency graph changed) — SAME FAILURE ON main 347f1730 (pre-existing). sync_return_sections needs pandoc (absent).
- zres binary in <author-workspace>: no FMA instrs (objdump) OK.
- PROVED gamma = -s*iota(c) for all m: k==s h^-1, v==8^-1 mod a^2, B(1-l^-m)=iota(beta-bar - beta)=r h/2 => gamma = -s r/8. Doc labels it [N] "not needed" but E14 needs m-independence of operators -> required fix: promote to [P].
- E14 wording: "|Z(nu_{7,±})| ≍ |mu_inf|^m" wrong for the sign whose leading eig is smaller (1.884 vs 1.897); hypothesis should be per-s.
- Box clock is Asia/Yekaterinburg (+05). m17 cert started 06:39:55Z = 07:39:55 CET OK; predictions self-timestamped 06:41Z.
- receipt sha256: 9/9 match. README evidence mentions cert_m17_full.out which is NOT committed (nit).
- absolute scratch-directory paths in: referee/NOTES.md:10, referee/REPORT.md:3,4,310,369-373, referee/logs/lean_neg.out:1, evidence lean_controls.log:3,8,13,18,23 (precedent on main: 614 files). No secrets.
- README.md/README.ru.md: "Z_m is then the trace of m-independent IFS transfer operators" lacks "finite alphabet"; "leading eigenvalue certified" lacks "L-truncated". minor fix.
- TeX Thm 194 says "m-independent operators" -> only true given gamma=-s iota(c) (author labels [N]); my proof fixes it.
- F7/F8/F9 code fixes verified (cache key, explicit tail with factor 2, rho assert, vendored model import).
- E11 rigorous at m=7: f7@∓196 == k1@∓4 (my interval kernel). 
- m=13 INTERVAL CONFIRMED (722 s, 8 thr): F/2m>=6.4579491729, Wrest/m>=8.9158983459 (author 6.4579491707 / 8.9158983413). S width 5e-4 (author a-priori 1.7e-2). logs/ivcert_m13.out
- multi-t kernel; m=11 rerun logs/ivcert_m11_multi.out identical.
- E12 trace law own Galerkin vs brute: 5e-15..7e-14 (m=5,7; a=1,7; s=±1; both roots); gamma+1 control fails O(1). logs/e12_trace.log
- Author step2 reruns: cert49_py, check_phase logs reproduce identically; check_trace/check_propG running (<scratch-dir>)
- inventory source_blob_sha = git blob of claims.json OK. Only open claims carry closure_condition (repo convention) OK.
- NEW FINDING (safe-direction rounding): quoted certified bounds rounded to nearest, not safe direction:
  E3 table md 211-219 + claims.json:6900 + tex:34: lower endpoints 1.9154751 (cert 1.91547505) etc inward for 9/18 endpoints.
  E5 table md 238-239, md:69, claims.json:6951: 5.99(5.9881),7.98(7.9763),20.3,36.6,36.0,68.0,84.3,88.0,172,331,1851,1355,2706,1426,2848,404,804 rounded UP.
  eta1.25 "0.45 at most" (0.4477).
  E13 table md 451-452: 290544.5725 (cert lo 290544.57246; TRUE value 290544.57248 < .5725 => statement FALSE), 4203360.8595 (lo .85946), W 8.9159 (lo 8.915898) in md:452, claims.json:7157, tex:65, inventory:10432.
- Author zres rebuilt with README flags: 0 FMA; reproduces m=11 jsonl bit-identically. Without -ffp-contract=off gcc emits 10 FMA instrs.
- bounds.py rerun on cert_L6, cert_L8b reproduces _bounds.json.
