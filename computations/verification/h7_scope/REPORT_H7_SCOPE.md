# H7* scope integration: K_p arithmetic, the three included crossings on the finite vertex section, and what they do to H7* and Theorem v5

Integration of the referee-confirmed parts of draft PR #85 (branch `research-grok46-1104`, commit `b8e91215`, directory `evidence/research/20261104_grok47/`) into the registry as BGS-TRACE-344..347. Hostile referee audit: [`AUDIT.md`](../../../evidence/executions/20261105/h7_scope/referee/AUDIT.md) (nothing WRONG; every NEEDS FIX item is applied here). Receipt: [`receipt.json`](../../../evidence/executions/20261105/h7_scope/receipt.json).

Tags: **[P]** paper proof; **[P, finite]** exact finite integer computation; **[CA]** ball-arithmetic certificate of the named finite object; **[N]** floating point only. A finite enclosure is not an asymptotic bound.

Notation: \(u_0=1\), \(u_1=7\), \(u_{n+1}=6u_n-u_{n-1}\); \(h_p=u_{(p-1)/2}\); \(K_p=4h_p^2+3\); \(h_{3p}=h_pK_p\) (BGS-TRACE-265); \(\lambda=3+2\sqrt2\); \(T'=1.42785\).

## 1. BGS-TRACE-344 [P]: 7 | K_p, 7 ∤ h_p, gcd(h_p, K_p) = 1, prime factors of K_p are ≡ 1 (mod 3)

Proof: [`notes/h7_h8.md`](notes/h7_h8.md) §1, Lemmas 3 and 4 (checked by hand by the referee).

- *Lemma 4.* Mod 7 the recurrence is \(u_{n+1}\equiv -u_n-u_{n-1}\); from \((1,0)\) the residues from index 1 are \(0,-1,1\) repeating, so \(7\mid u_n\iff n\equiv 1\pmod 3\iff p\equiv 3\pmod 6\), i.e. only \(p=3\). For \(p\ge 5\), \(h_p\equiv\pm1\), \(K_p\equiv 4+3\equiv 0\pmod 7\). (\(K_3=199\equiv 3\).)
- *Lemma 3.* Mod 3 the sequence is \(1,1,2,2,\dots\), never 0, so \(3\nmid h_p\) and \(\gcd(h_p,K_p)\mid 3\) gives 1. If a prime \(q\mid K_p\) then \((2h_p)^2\equiv-3\pmod q\). \(q=2\) cannot occur because \(K_p\) is odd (referee fix 1b), \(q=3\) is excluded, and for \(q\ne 2,3\) reciprocity gives \((-3/q)=(q/3)\), so \(q\equiv 1\pmod 3\).
- *Exact check* (`code/kp_arith.py`, `logs/kp_arith.json`; referee `ints.py` independently): for all 301 primes \(5\le p<2000\), \(7\mid K_p\), \(7\nmid h_p\), \(3\nmid h_p\), \(K_p\) odd, \(\gcd(h_p,K_p)=1\), \(u_{(3p-1)/2}=h_pK_p\). Lean: `Bgs.H7KpArith.seven_dvd_K` (`decide +kernel`, primes \(5\le p<200\)).

Prior work: the identity \(h_{3p}=h_pK_p\), the rank-\(3p\) statement and \(7\mid K_p\) for \(p=5,\dots,23\) are BGS-TRACE-265; TRACE-344 adds the general \(7\mid K_p\) for every prime \(p\ge5\) and the quadratic constraint. The stronger congruence \(q\equiv1\pmod{6p}\) (N8b) is not re-proved here; it is only checked on the factorisations of §2.

## 2. BGS-TRACE-345 [P, finite, exact integers]: factorisations for 5 ≤ p ≤ 31 and the inclusion facts

| \(p\) | \(h_p\) | \(h_p\) prime | \(K_p\) | included \(K_p\)-divisors other than 7 (\(d^2\le h_{3p}\)) |
| --- | --- | --- | --- | --- |
| 5 | 41 | yes | \(7\cdot31^2\) | 31, 217 |
| 7 | 239 | yes | \(7^2\cdot4663\) | 49, 4663 |
| 11 | 8119 | no | \(7\cdot37667521\) | none |
| 13 | 47321 | no | \(7\cdot313\cdot4088137\) | 313, 2191, 4088137 |
| 17 | 1607521 | no | \(7\cdot409\cdot3610372009\) | 409, 2863, 3610372009 |
| 19 | 9369319 | yes | \(7\cdot457\cdot14593\cdot7521721\) | ten |
| 23 | 318281039 | no | \(7\cdot57887325592525441\) | none |
| 29 | 63018038201 | yes | \(7\cdot13921\cdot5806729\cdot28073057689\) | ten |
| 31 | 367296043199 | no | \(7\cdot2643247\cdot7159513\cdot4073551591\) | twelve |

Every factor is \(<2^{64}\) (BPSW deterministic there; `h7h8.py` additionally proves each factor prime by trial division), \(\equiv 1\pmod 3\), and every factor other than 7 is \(\equiv1\pmod{6p}\). \(31^2=961>\sqrt{h_{15}}\) (\(525^2<275807<526^2\)). The ten divisors at \(p=19\): 457, 3199, 14593, 102151, 6669001, 7521721, 46683007, 52652047, 3437426497, 24061985479; at \(p=29\): 13921, 97447, 5806729, 40647103, 28073057689, 80835474409, 196511403823, 565848320863, 390805036088569, 2735635252619983.

The three crossing conductors:

| \(d\) | factorisation | \(p\) | \(d\mid K_p\) | \(\gcd(d,h_p)\) | \(\lfloor h_{3p}/d^2\rfloor\) | \(\gcd(\beta,d)\) | \(\mathrm{ord}_d\lambda\) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3437426497 | \(457\cdot7521721\) | 19 | yes | 1 | 278 | 1 | 57 |
| 24061985479 | \(7\cdot457\cdot7521721\) | 19 | yes | 1 | 5 | 1 | 57 |
| 2735635252619983 | \(7\cdot13921\cdot28073057689\) | 29 | yes | 1 | 133 | 1 | 87 |

Since \(\gcd(d,h_p)=1\), no \(d\) is \(h_p\) or \(e\cdot h_p\); \(d^2\le h_{3p}\) and TRACE-273 (every odd \(m\in[15,20001]\) and beyond) include all three. The order of \(\lambda\) is \(3p\) for all 24 included conductors at \(p=5,7,19,29\) (referee 2c/Lemma 3 of `h7_rates.md`), including **\(d=4663\) at \(p=7\)**: \(4663\mid K_7=228487\), \(4663^2=21743569\le h_{21}=54608393\), order 21 (referee fix 2d; this conductor was missing from the PR #85 target list). Lean: `Bgs.H7KpArith.K_factorisations`, `crossings`, `d4663` (`decide +kernel`; primality of the factors is not checked in Lean).

## 3. BGS-TRACE-346 [CA, finite vertex section only]: sector-0 spectral radii above T'

**Object.** The compression of the TRACE-223 multi-disc **vertex** transfer operator (`lineJ/code/certG_build_sector.py` conventions: \(\rho=1.2\), \(C=-1/(4\sqrt2)\), \(\hat g(n)=i^nJ_n(1.8)\)) to centres \(|c|\le 3\), monomials of degree \(<40\), letters \(|n|\le16\): dimension 280. The core is forward-invariant on this alphabet (\(19/\lambda<3.26\); no rounding within \(10^{-8}\) of a half-integer). For a \(\lambda\)-orbit of \(\beta\) at conductor \(d\) and sector \(a\), the per-step rate is \(r=\rho(\prod_{j<P}L_{a/8+\tau_j})^{1/P}\) with \(\tau_j=\mathrm{Tr}(\beta\lambda^j)/d\bmod 1\), \(P=\mathrm{ord}_d\lambda\). Notes: [`notes/h7_multidisc.md`](notes/h7_multidisc.md) §§1–4.

**Certificate** (`code/h7_multidisc_cert.py enclose`, arb precision 320, Newton–Kantorovich with all error sums in ball arithmetic after referee fix 3c; rerun 2026-11-05, `logs/h7_multidisc_enclose.json`):

| orbit | \(P\) | \(h\) | lower | upper | PR #85 lower |
| --- | --- | --- | --- | --- | --- |
| \(d=3437426497\), \(\beta=(-208,0)\), \(a=0\) | 57 | \(1.01\cdot10^{-14}\) | 1.4587724663901533 | 1.4587724663901547 | 1.458772466390154 |
| \(d=24061985479\), \(\beta=(227,227)\), \(a=0\) | 57 | \(1.79\cdot10^{-14}\) | 1.511980597518887 | 1.5119805975188885 | 1.5119805975188876 |
| \(d=2735635252619983\), \(\beta=(-89,0)\), \(a=0\) | 87 | \(1.37\cdot10^{-14}\) | 1.4686852948918225 | 1.468685294891824 | 1.4686852948918232 |

All three lower bounds exceed \(T'\) (gaps \(0.03092\), \(0.08413\), \(0.04083\)). The shifts from PR #85 are the directed one-ulp float conversions now applied at each conversion.

**Independent re-enclosure** (referee, `referee/mine/krawczyk.py`: own orbit, trace and product without rescaling, Krawczyk/Brouwer box test on the exact quadratic expansion; shares only `build_blocks`/`assemble`, checked by hand; rerun at integration from the relative paths): \(d=3437426497\): \([1.45877246639015403,\ 1.45877246639015426]\), box \(9.5\cdot10^{-6}\), \(\|I-RJ_0\|_\infty=1.9\cdot10^{-7}\).

**Level-7 calibration against BGS-TRACE-223** (same section, period 3):

| class | sector | this section (Newton) | referee Krawczyk | TRACE-223 |
| --- | --- | --- | --- | --- |
| 2:1 | 4 | [1.2835951329030864, 1.2835951329030906] | [1.2835951321515, 1.2835951336547] | inside the disc [1.2835950326, 1.2835952326] |
| 1:3 | 6 | [1.2837142953109733, 1.2837142953109817] | [1.2837142951988, 1.2837142954232] | under the cap 1.2837144 |
| 0:1 | 0 | — | [1.2624306303209, 1.2624306304893] | under the cap 1.2624308 |

The section reproduces the operator TRACE-223 certifies, at a coarser mode cutoff than the dimension-1980 build; it does not reproduce the \(10^{-10}\) perturbation of that build.

**Numerical only, not claimed.** (i) The edge section was floated only (`logs/h7_multidisc_edge.json`, rates \(\approx0.35\)) — the **edge comparison is [N]**. (ii) The **trace-versus-spectral-radius step is [N]**: numerically \(|\mu_2|/|\mu_1|\approx 2\cdot10^{-16}\) on the \(d=3437426497\) orbit, but the other 279 eigenvalues are not bounded. (iii) **The untruncated operator is not claimed**: the one-step tail section → core is \(<9.646772214969685\cdot10^{-5}\) [P, arb] (`notes/h7_multidisc.md` §4), but no useful bound on the \(57\)- or \(87\)-step product follows (§5).

The single-disc Galerkin model of [`notes/h7_rates.md`](notes/h7_rates.md) crosses at the same three orbits (rerun `logs/rerun/orbit_*.json`: 1.458772466584507, 1.5119805994002584, 1.4686852970394262 lower); that is a different projection and is not registered.

## 4. BGS-TRACE-347 [P on TRACE-346]: scope of H7* at these levels

The safe wording ([`notes/h7_scope.md`](notes/h7_scope.md); referee "Safe registry wording", fixes 4a, 4c, 4d):

1. TRACE-305's closure condition is the aggregate bound \(|\mathrm{Lin}_d|\le\varepsilon_d|Z_\rho|^2/h_p\), \(\sum\varepsilon_d\le\kappa_0\). "Cross-correlation growth \(<T'\)" in its title is a sufficient per-orbit majorant. By TRACE-346, that **per-orbit sufficient reading fails on the finite vertex section** at \(d=3437426497, 24061985479\) (\(p=19\)) and \(d=2735635252619983\) (\(p=29\)): a per-orbit cap at \(T'\) cannot be certified from this section.
2. **The aggregate H7* (TRACE-305) stays open**: no enclosure of \(\sum_\beta\kappa_d(N\beta)\hat Z(\beta)\) exists at these conductors; one orbit is one term. H7* is neither proved nor refuted. TRACE-305 is not edited (no amendment entry is needed: its state, title, boundary and closure condition remain accurate).
3. **Theorem R♯-mod v5 (TRACE-325) is unaffected**: its hypotheses are required at infinitely many primes \(p\ge p_{\mathrm{thr}}\) (and the draft's \(\mathcal P\)-subsequence form, `THEOREM_DRAFT_v5.md` line 128, needs \(\mathcal P\) infinite), so a failure at the finitely many primes 19, 29 cannot fire or block it; independently \(p_{\mathrm{thr}}\ge p_1\ge1409>29\).
4. **18 included conductors remain unsearched / not exhausted**: \(d=4663\) (\(p=7\)) and the seventeen at \(p=19,29\) of `notes/h7_rates.md` §8.

Frozen R′ (TRACE-206) stays open.

## 5. Referee fixes applied

| item | fix |
| --- | --- |
| 1b | Lemma 3 excludes \(q=2\) (\(K_p\) odd) — `notes/h7_h8.md`, TRACE-344 |
| 2d | \(d=4663\) at \(p=7\) added; "eighteen" open conductors — `notes/h7_rates.md` §0, §8; `code/h7_rates.py` (`UNSEARCHED_INCLUDED`, self-test) |
| 3c | `newton_enclose`: every error sum in arb; directed one-ulp float conversion (`hi_f`, `lo_f`); rerun confirms all numbers |
| 4a | vertex-only wording; edge and trace-vs-radius [N] — `notes/h7_scope.md`, `notes/h7_multidisc.md` §6, TRACE-346/347 |
| 4c | TRACE-325 attribution; infinitely-many-primes reason — same files |
| 4d | (i)–(iii) as above |
| repro | hard-coded `/workspace/...` `sys.path` replaced by paths relative to the file (also in the referee's `krawczyk.py`); `if not __debug__` guard in every script |

## 6. Not integrated

From PR #85: the ε-span law and Prop. K sharpening (registered separately via PR #88 as BGS-TRACE-337..341), `h7_lin.md` (aggregate Lin comparison), §§3–5 of `h7_h8.md` (Lemma E return length, H8 obstruction, Prop. 9), and the Galerkin-model theorems of `h7_rates.md` (copied as context; not registered).
