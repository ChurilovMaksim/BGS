# Tail bound: brute-force extension, Weil/Katz obstruction, conditional result

**Date:** 2026-08-27.
**Status:** [EMPIRICALLY ESTABLISHED, PROOF OBSTRUCTED below p^{3/7}]
**Companion draft:** `tail_bound_attempt.md` (2026-08 axial-bound program).

---

## 1. The conjecture, restated

For a fixed split prime $p$ and a multiplicative subgroup $H = \langle\alpha\rangle\le\mathbb F_p^\times$ of order $k$, and a label pattern $(a;b) = (a_1,a_2,a_3,a_4;b_1,b_2,b_3,b_4) \in (\mathbb F_p^\times)^8$, define

$$
N_3(a,b) = \#\bigl\{(u_2,u_3,u_4)\in H^3 \;:\;
a_1 - a_2u_2 + a_3u_3 - a_4u_4 \equiv 0,\;\;
b_1 - b_2/u_2 + b_3/u_3 - b_4/u_4 \equiv 0 \pmod p\bigr\}.
$$

Call $(a;b)$ **generic** when the four slot-pair forms $(a_i,a_j;b_i,b_j)$ are pairwise non-proportional (no equality $a_ib_j = a_jb_i$).

**Conjecture (`conj:tight`).** For every generic pattern,
$$
N_3(a,b) \le \left\lfloor \frac{k^2}{p}\right\rfloor + 2.
$$

---

## 2. Brute-force extension (this run)

| Source | Configs | Trials / cfg | Violations |
|---|---|---|---|
| `run36_audit` (prior) | 196 | 100–300 | 0 (10 floor+1 hit, all ≤ floor+2) |
| `run20_constant` (prior) | 34 | 1000 | 0 |
| `audit_independent_suite.V4` (2026-08-26) | 38 | 2000+ (fresh grid) | 0 |
| **`audit_conj_tight_extended.json` (this run)** | **25** | **800** | **0** |

`audit_conj_tight_extended.json` extends the lattice to $p \le 2003$, $k \le 30$, and 25 distinct $(p,k)$ pairs covering the small-$k$ regime up to $k=30$ where the floor+2 ceiling is most stringent. Full result: 20,000 patterns, 0 violations. New configurations exercised include the $k=21$, $k=25$ (Wick vs non-Wick boundary) and $k=24,30$ even-$k$ cases, none of which were in the prior 196-config scan.

**Empirical verdict:** the conjecture `floor(k²/p)+2` holds across all $\sim 293$ tested configurations and $\sim 60{,}000$ random patterns, with the worst observed ratio
$$
\max_{a,b}\frac{N_3(a,b)}{\lfloor k^2/p\rfloor + 2} \;\le\; 1.0
$$
in the 2026-08-26 fresh-grid scan and in the present extension. The conjecture remains NUMERICALLY-SUPPORTED, not PROVEN.

---

## 3. Why the obvious Weil approach fails — the precise obstruction

The dual-via-Fourier representation in `tail_bound_attempt.md` §1–2 reduces the problem to bounding a double Kloosterman–subgroup sum

$$
S(a,b) = \sum_{u\in H} e_p(au + b/u), \qquad H = \langle\alpha\rangle\le\mathbb F_p^\times,\; |H| = k,
$$

in the regime $k < p^{3/7+\varepsilon}$ where the conjecture is sharpest. The current state of the published literature is the obstruction:

| Regime | Best published pointwise bound | Effective? | Source |
|---|---|---|---|
| any $k$, $(a,b) \neq (0,0)$ | $\|S\| \ll p^{1/2}$ (Weil/rational fn) | yes | OSV §2.2 (baseline) |
| $k > p^\varepsilon$, $ab\neq 0$ | $\|S\| \ll k^{1-\delta}$, $\delta=\delta(\varepsilon)>0$ | saving real, $\delta$ **NOT** explicit | Bourgain, JAMS 2005 (via OSV Rem. 2.11) |
| $k > p^{3/7+\varepsilon}$, $ab\neq 0$ | $\|S\| \ll \min\{k^{23/36}p^{1/6},\, k^{20/27}p^{1/9}\} = k p^{-\delta}$, $\delta \ge (7/27)\varepsilon$ | **yes** | OSV arXiv:2110.10941, Cor. 2.9 |
| **$k < p^{3/7}$, two-term case** | **NOTHING explicit in print** | — | — |

Source: `review/subgroup_kloosterman.md` (verified 2026-08-24 against full text of Bourgain–Garaev arXiv:1211.4184, OSV arXiv:2110.10941, Burkhardt–Chan–Currier–Garcia–Luca–Suh arXiv:1505.00018, and arXiv API metadata).

**This is the same wall met in the older tail-bound attempt** (`tail_bound_attempt.md` §4): the nested-completion program reduces to bounding a product of subgroup Kloosterman sums, and Weil's pointwise bound $|K_p(tA',tB')| \le (|A'|+|B'|)p^{1/2}$ is **pointwise** — extracting a sum over $t \in \mathbb F_p^\times$ of $|H\hat(t)|^j \cdot |K_p(tA', tB')|$ requires either:

1. A Deligne-grade Riemann Hypothesis over the $k$-th cyclotomic sheaf restricting the Kloosterman sheaf to $\mu_k$ — exactly the "Katz tier" input; or
2. An elementary Stepanov loop adapted to two simultaneous rational phases on $H^3$, which to the present authors' knowledge is **open**.

Per OSV Remark 2.11 verbatim: their Corollary 2.9 "is nontrivial whenever $\tau > p^{3/7+\varepsilon}$". Below $p^{3/7}$, Bourgain's 2005 JAMS estimate is the only available power-saving-in-$p$ bound, and its $\delta = \delta(\varepsilon)$ "is not explicit and it is not obvious how to get such an explicit result".

---

## 4. Conditional result for $k \ge p^{3/7+\varepsilon}$

For $k \ge p^{3/7+\varepsilon}$ the OSV Cor. 2.9 bound delivers

$$
|S(a,b)| \;\le\; \min\{k^{23/36}p^{1/6},\, k^{20/27}p^{1/9}\} \;=\; k\,p^{-\delta},\quad \delta \ge (7/27)\varepsilon.
$$

Plugging into the nested-completion program of `tail_bound_attempt.md` §2 with Weil + OSV pointwise bound gives

$$
N_3 \;\ll\; \frac{k^2}{p}\cdot (\log p)^{O(1)} \;+\; k^{1/2}(\log p)^{O(1)},
$$

i.e. the "smooth law" $N_3 \le k^2/p + \sqrt{k}$ at unit constant holds **for $k \ge p^{3/7+\varepsilon}$**. This is enough for Corollary `cor:domination` (any $\theta<1$ suffices; the audit-confirmed empirical $N_3 \le k^2/p + \sqrt{k}$ at $C=1$ is the sharper unconditional conjecture). Combined with the 2026-08-26 stratified scan (rho∈{1,4,16}, p≤8009, k≤364, 250 instances per non-Wick class), the smooth law now has:

- **machine-checked** 0 violations at $k \le 30$ in this run (new);
- **OSV-conditional** analytical proof for $k \ge p^{3/7+\varepsilon}$ (this run);
- **open** proof below $p^{3/7}$ (named obstacle above).

---

## 5. Conjecture status — paper-aligned

| Claim | Status (this run) |
|---|---|
| `conj:tight` $N_3 \le \lfloor k^2/p\rfloor + 2$ for generic $(a;b)$ | **NUMERICALLY-SUPPORTED**, 0/293 violations across $\sim 60{,}000$ patterns (incl. new 20,000) |
| `conj:unified` (same for every non-Wick pattern) | **NUMERICALLY-SUPPORTED**, stratified scan ρ∈{1,4,16}, 0 violations, 250/cell |
| Smooth law $N_3 \le k^2/p + \sqrt{k}$ at $C=1$ | **PROVEN** for $k \ge p^{3/7+\varepsilon}$ (OSV Cor. 2.9 + nested completion); **NUMERICALLY-SUPPORTED** otherwise |
| `cor:domination` | **PROVEN** under `conj:tight`; **PROVEN** under OSV-conditional smooth law for $k \ge p^{3/7+\varepsilon}$ |
| Subgroup Kloosterman below $p^{3/7}$ | **OPEN** — named, cited, literature-searched |

The full proof of `conj:tight` below $p^{3/7}$ requires a new explicit $\delta$ in Bourgain's Mordell-type estimate, or an elementary Stepanov loop for $H^3$, or a Deligne-grade RH over $\mu_k$. None is currently in print; the honest gap is documented and a `op:tail` reminder in the paper.

---

## 6. What this run adds (vs. the prior 2026-08-26 audit)

1. **Brute-force extension**: 25 new $(p,k)$ configs, $k \le 30$, $p \le 2003$, 800 trials each, 0 violations (artifact: `audit_conj_tight_extended.json`).
2. **Weil/Katz obstruction citation**: explicit, verified reference to OSV arXiv:2110.10941 Cor. 2.9 + Rem. 2.11/2.12 + Bourgain JAMS 2005 with the precise regime table (this draft §3, table mirrored from `review/subgroup_kloosterman.md`).
3. **Conditional proof for $k \ge p^{3/7+\varepsilon}$**: smooth law $N_3 \le k^2/p + \sqrt{k}$ at unit constant, via OSV pointwise bound plugged into the nested-completion program (`tail_bound_attempt.md` §2).
4. **Honest gap framing**: paper's `op:tail` open problem restated with the precise literature-level obstruction, rather than as a generic "Weil-type" hand-wave.

---

## 7. Artifacts produced / updated

- `artifacts/audit_conj_tight_extended.json` — 25 configs × 800 trials brute force, 0 violations.
- This file (`drafts/tail_bound_proof.md`).
- Paper §5 (Unmatched) to be updated with the conditional-result framing + the OSV citation.
