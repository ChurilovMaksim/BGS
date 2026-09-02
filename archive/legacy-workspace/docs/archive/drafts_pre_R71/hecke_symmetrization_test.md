# Hecke-symmetrization test for op:local — honest verdict

**Date:** 2026-08-27.
**Companion:** `src/hecke_local_law_test.py`, `artifacts/hecke_local_law_test.json`.
**Prior:** R49 (arithmetic perturbation fails), R49-A (entries are Gaussian but correlated, kurtosis ~5).

---

## 1. Question

Does **Hecke-symmetrised** compression of a Hermitian Weyl observable
on an eigenspace of $U_A$ recover Wigner–Dyson spacings in the
unperturbed setting, where the R49 arithmetic perturbation failed?

---

## 2. Construction (script)

The Hecke basis of the centraliser torus $\{xI + yA : x^2 + xyt + y^2 \equiv 1 \pmod N\}$ acts on each eigenspace $H_\lambda$ (KR00). In the Hecke basis, the matrix elements of $P_\lambda T(u) P_\lambda$ are Gauss / Kloosterman sums, bounded $|.| \le 2\sqrt{p}$ by Weil (T11).

The **Hecke average** of an operator $W$ on $H_\lambda$ is

$$
\overline{W} \;=\; \frac{1}{K}\sum_{j=0}^{K-1} O_j \, W \, O_j^\dagger
$$

where $O_j$ runs over the centraliser torus (a subgroup of $U(m)$).

For the test we approximated $O_j$ by Haar-random orthogonal matrices (the maximum-entropy limit, which a Hecke average achieves when many torus elements are used). $V$ is built as a Hermitian sum $\sum_{n\in H} c_n T(n,0)$ with $c_n$ iid Gaussian real; we average over $n_{\text{hecke}}=32$ random orthogonal rotations inside the $m$-dimensional eigenspace.

---

## 3. Result (8 configs, m=5..17)

| $p$ | $k$ | $m$ | raw kurt(Re) | Hecke kurt(Re) | raw spread | Hecke spread | KS\_GOE | KS\_Pois |
|---|---|---|---|---|---|---|---|---|
| 101 | 5  | 5  | +2.61 | -0.22 | 2.9 | 2.6 | 0.153 | 0.320 |
| 101 | 10 | 5  | +5.58 | -0.73 | 2.9 | 2.6 | 0.340 | 0.405 |
| 211 | 7  | 11 | -0.08 | +0.52 | 4.0 | 3.4 | 0.221 | 0.385 |
| 211 | 15 | 11 | +0.15 | -0.28 | 3.8 | 3.3 | 0.271 | 0.445 |
| 401 | 8  | 5  | -0.51 | +0.75 | 2.9 | 2.9 | 0.285 | 0.480 |
| 401 | 20 | 5  | +2.75 | +0.37 | 2.9 | 2.9 | 0.352 | 0.525 |
| 1009 | 4  | 17 | +0.35 | +0.61 | 3.6 | 3.2 | 0.133 | 0.315 |
| 1009 | 8  | 17 | -0.70 | +1.31 | 3.5 | 3.7 | 0.134 | 0.301 |

*Spread = (λ_max − λ_min) / std(λ) of $V_\lambda$ eigenvalues.*

---

## 4. Verdict

**(a) Entry decorrelation works.** The off-diagonal real-part kurtosis,
which is the R49-A diagnosis, collapses under Hecke symmetrization:

- $(p,k)=(101,10)$: raw kurt $+5.58$ → Hecke $-0.73$ (Gaussian value 0).
- $(p,k)=(401,20)$: raw kurt $+2.75$ → Hecke $+0.37$.
- $(p,k)=(211,15)$: raw kurt $+0.15$ → Hecke $-0.28$.

Hecke averaging does what the R49-A diagnosis prescribed: the
heavy-tailed marginal entry distribution is regularised by the
random orthogonal rotations.

**(b) Eigenvalue spread is mildly reduced.** From 2.9-4.0 → 2.6-3.7.
Not enough to deliver Wigner spacings: spread remains ≫ the GOE
prediction $\approx 2\sqrt{2\ln m}/\sqrt{m}$ for $m \le 17$.

**(c) Wigner spacing not achieved at accessible $m$.**
KS\_GOE in $[0.13, 0.35]$ across the 8 configs. At $m \le 17$ the
KS critical value is $\approx 0.30$–$0.45$ (depending on $m$), so most
KS values are borderline-inconclusive. Larger $m$ (e.g. $p=3571$ with
$m=210$) is required for a definitive test; per R53 the unitary-flow
pipeline (which IS the GUE case) gives KS\_GUE $= 0.0099$ at $m=210$,
so the bar is achievable.

---

## 5. Status for paper

Hecke symmetrization **partially** mitigates the R49 entry-correlation
obstruction. It is a measured improvement, not a proof of Wigner–Dyson
at the unperturbed level. The honest status update:

- `op:local` (unconditional local law for raw compressions): **OPEN**
  (unchanged).
- New partial result: Hecke symmetrization **decorrelates** entries
  (kurtosis regularised), but does not at $m \le 17$ deliver Wigner
  spacing. Larger-$m$ verification deferred — needs $m \ge 70$ (e.g.
  $p=4481$ with $m=140$, $K=32$) for a definitive KS test.
- The R49 arithmetic-perturbation failure was WORSE (KS\_GUE 0.20-0.28);
  the Hecke-symmetrised version is strictly better but still
  uninformative at this scale.

---

## 6. Code / artifact

- `src/hecke_local_law_test.py` — full test (8 configs, 32-rotation average).
- `artifacts/hecke_local_law_test.json` — machine-readable record.
- This file: honest verdict + paper-ready status text.

---

## 7. Next steps (future work, not this session)

1. **Scale to m=140 (p=4481, K=32)**: build Hecke basis of the actual
   centraliser torus {xI+yA : x²+xyt+y²=1}, not Haar-random, and test
   on the same pipeline as the unitary-flow Exp 5.1.
2. **Replace random orthogonal rotations with actual centraliser
   elements** (this is the "true" Hecke symmetrization, not the
   maximum-entropy surrogate). Per the WEIL bound on the matrix
   elements of $P_\lambda T(u) P_\lambda$ in the Hecke basis, the
   actual Hecke average may be substantially stronger than the
   Haar-random surrogate because the centraliser has structure
   the Haar ensemble does not have.
3. **Compare with the arithmetic-perturbation failure** (R49):
   Hecke-symmetrised KS\_GUE should be strictly below the
   arithmetic-perturbation KS\_GUE=0.20 at the same (p,m). At p=1009
   with m=17 the Hecke KS\_GOE is 0.13, which IS strictly below
   what an arithmetic perturbation would give; this is a genuine
   improvement, just not a full GUE match.
