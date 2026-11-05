# Scoping note for H7* at the three included crossings

> **Integrated copy (2026-11-05).** Source: `evidence/research/20261104_grok47/proofs/h7_scope.md` on draft PR #85 (branch `research-grok46-1104`, commit `b8e91215`), rewritten to the referee's safe registry wording (`evidence/executions/20261105/h7_scope/referee/AUDIT.md`, section "Safe registry wording"). Fixes applied: 4a (vertex-only wording; edge and trace-versus-radius are [N] only), 4c (TRACE-325 attribution; hypotheses needed at infinitely many primes), 4d(iii)/2d (d = 4663 at p = 7; eighteen open conductors). Registered as BGS-TRACE-347 (scope) on the certificate BGS-TRACE-346; arithmetic BGS-TRACE-344, 345. The aggregate comparison `proofs/h7_lin.md` remains on PR #85 and is not integrated.

H7* (BGS-TRACE-305) asks for \(|\mathrm{Lin}_d|\le\varepsilon_d|Z_\rho|^2/h_p\) with \(\sum\varepsilon_d\le\kappa_0\), over the included levels below \(L_{\mathrm{fl}}\) other than \(h_p\) and \(e\cdot h_p\). That is the registered `closure_condition`. The phrase "i.e. cross-correlation growth \(< T'=1.42785\)" in the TRACE-305 title is a sufficient majorant of that sum, obtained by replacing \(\sum_\beta\kappa_d(N\beta)\hat Z(\beta)\) with \((\sum|\kappa|)\max|\hat Z|\). It is not the closure condition.

**Arithmetic [P] (BGS-TRACE-344, 345).** For every prime \(p\ge 5\): \(7\mid K_p\), \(7\nmid h_p\), \(\gcd(h_p,K_p)=1\), and every prime factor of \(K_p\) is \(\equiv 1 \pmod 3\) (\(q=2\) cannot occur since \(K_p\) is odd). [P, finite] Complete factorisations of \(K_p\) for \(5\le p\le 31\). The included \(K_p\)-divisors other than \(7\) at \(p\in\{5,7,19,29\}\) are \(31, 217\); \(49, 4663\); ten at \(p=19\); ten at \(p=29\).

**Certificate [CA, finite section only] (BGS-TRACE-346).** On the compression of the TRACE-223 multi-disc **vertex** operator to centres \(|c|\le 3\), modes \(<40\), letters \(|n|\le 16\) (dimension \(280\); calibrated: level-7 classes \(2{:}1\), \(1{:}3\), \(0{:}1\) inside or under the TRACE-223 bounds), the sector-\(0\) per-step spectral radius of one \(\lambda\)-orbit exceeds \(T'=1.42785\) at

| \(d\) | factorisation | \(p\) | \(\beta\) | certified lower bound | \(\lfloor h_{3p}/d^2\rfloor\) |
| --- | --- | --- | --- | --- | --- |
| \(3437426497\) | \(457\cdot 7521721\) | \(19\) | \((-208,0)\) | \(\ge 1.4587724663\) | \(278\) |
| \(24061985479\) | \(7\cdot 457\cdot 7521721\) | \(19\) | \((227,227)\) | \(\ge 1.5119805975\) | \(5\) |
| \(2735635252619983\) | \(7\cdot 13921\cdot 28073057689\) | \(29\) | \((-89,0)\) | \(\ge 1.4686852948\) | \(133\) |

Each \(d\) divides \(K_p\), is coprime to \(h_p\) (so it is neither \(h_p\) nor \(e\cdot h_p\)), and has \(d^2\le h_{3p}\) (included by TRACE-273). Consequently a per-orbit cap at \(T'\) — the sufficient reading "cross-correlation growth \(< T'\)" of TRACE-305 — cannot be certified from this section.

**Not shown.** Any bound on the untruncated monodromy (the one-step tail is \(<9.65\cdot 10^{-5}\), but the product of \(57\) or \(87\) steps was not bounded usefully); on the edge operator (floated only, rates \(\approx 0.35\), [N]); on trace versus spectral radius (\(\hat Z\) involves \(\operatorname{Tr}V^m-\operatorname{Tr}E^m\), TRACE-221; numerically the section monodromy is rank one to \(2\cdot 10^{-16}\), not certified); or on the aggregate \(\sum_\beta\kappa_d(N\beta)\hat Z(\beta)\). One \(\lambda\)-orbit is a single term of that sum.

**H7* (TRACE-305) stays open;** it is neither proved nor refuted at these levels. Its state, title, boundary and closure condition are unchanged.

**Theorem R♯-mod v5 (TRACE-325) is unaffected.** Its registered hypotheses (H0, H1, H5–H8 at \(p\), and \(B_p\ge\kappa>0\)) are required for infinitely many primes \(p\ge p_{\mathrm{thr}}\); the draft's \(\mathcal{P}\)-subsequence form (`THEOREM_DRAFT_v5.md`, line 128) likewise needs \(\mathcal{P}\) infinite. A failure at the finitely many primes \(19\) and \(29\) can neither fire nor block the implication. Independently, \(p_{\mathrm{thr}}\ge p_1\ge 1409>29\) (registered thresholds \(3307\) at \(C\le 0.082\), fragile; \(1409\) at \(C\le 8.8\cdot 10^{-4}\), robust).

Frozen R′ (BGS-TRACE-206) stays open. **Conductors not exhausted:** \(4663\) (at \(p=7\), not searched at all) and the seventeen others at \(p=19, 29\) listed in `proofs/h7_rates.md` §8 — eighteen in total.
