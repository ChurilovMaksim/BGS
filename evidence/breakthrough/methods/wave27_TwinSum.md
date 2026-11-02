# Wave 27, task 4 — Twin Sum Lemma: proved on an infinite family, open in general

## Verdict

The Twin Sum Lemma is **not proved in general**, and it cannot be
proved by the methods of this program alone: its obstruction is
exactly the "prime-power-dominated D_m" phenomenon, exhibited
exactly at m = 5 and m = 7 (twin sum = D_m/4). What is proved
here: (A) the lemma holds unconditionally along every family
m = 2^k·t with t fixed, by a doubling-chain argument; (B) a clean
conditional theorem for general m, with the hypothesis stated as
the hard core it is. Repository untouched; no Lean build.

## 1. Precise statement

Let α = 3+2√2, β = α² = 17+12√2, x_m + y_m√2 = α^m, and
D_m = 2(x_m − 1) = |N(α^m − 1)| (so D_m = 4w_m² for m odd,
D_m = 8y_{m/2}² for m even). A *twin qt* is an odd prime power
qt = p^e exactly dividing D_m (qt ‖ D_m) with
3 ∤ ord_qt(β), where ord_qt(β) is the multiplicative order of β
in R_qt = (Z/qt)[√2]. (The 3-part never qualifies: ord_9(β) = 6;
the 2-part is excluded from the sum by definition, and it is
≤ 2^{2v₂(m)+3} ≤ 8m² = o(D_m) anyway, so this choice is immaterial.)

**Twin Sum Lemma.** Σ_{twin qt ‖ D_m} qt = o(D_m) as m → ∞.

Remark: the wave-26 "sign-symmetric kernel periods L ∈ {8,16}"
is the m = 48 shadow of the criterion 3 ∤ ord_qt(β): at m = 48
the twin qt are exactly 17² (ord 68) and 577² (ord 4616).

## 2. Sharpness: the lemma has no uniform rate, and H fails at small m

Exact computations (ring (Z/n)[√2], β = 17+12√2):

| m | D_m | twin qt | twin sum / D_m |
| 3 | 196 = 2²·7² | none (ord_7(β) = 3, ord_49(β) = 21) | 0 |
| 5 | 6724 = 2²·41² | 41² (ord_{41²}(β) = 205 = 5·41) | 1/4 |
| 7 | 228484 = 2²·239² | 239² (ord_{239²}(β) = 1673 = 7·239) | 1/4 |
| 12 | 2⁷·3⁴·5²·7²·11² | none (ords 15, 21, 66, all divisible by 3) | 0 |
| 16 | 2048·9·289·332929 | 289 + 332929 | 1.9×10⁻⁷ |
| 48 | ≈ 5.58×10³³ | 289 + 332929 | 6.0×10⁻³² |

At m = 5, 7 the whole odd part of D_m is a single twin prime
square, so the ratio is exactly 1/4. Hence any proof of the full
lemma must rule out infinitely many such m — i.e. must show the
Pell numbers x_m (m odd) and y_{m/2} (m even) are not
"essentially prime powers" with a twin prime infinitely often.
That is a prime-power problem for Lucas sequences, out of reach
of elementary methods; it is not settled by anything in waves
1–26. (For contrast: at m = 12 the twin sum is 0, and at
m = 16, 48 it is negligible — the lemma is a statement about the
tail, not about every m.)

## 3. Theorem A (unconditional): the lemma holds for m = 2^k·t, t fixed

Let m = 2^k·t with t fixed, k → ∞. Then D_m = 8y_{m/2}² and every
odd prime power qt ‖ D_m is a square p^{2f} with p^{f} ‖ y_{m/2}.

**Chain lemma.** y_{2n} = 2x_n y_n, x_{2n} = 2x_n² − 1, hence
y_{2^{k-1}t} = 2^{k-1}·y_t·∏_{j=0}^{k-2} x_{2^j t} (verified
exactly: k = 4, t = 1 gives 470832 = y_8; k = 3, t = 3 gives
543339720 = y_12; k = 5, t = 1 gives 627013566048 = y_16).

**Coprimality.** The factors x_{2^j t} are pairwise coprime: if
d | x_a and x_{2a} = 2x_a² − 1 then d | 1, and the same step shows
x_{2^j t} ≡ 1 (mod d) for all later doublings, so d | 1.
Also gcd(x_{2^j t}, y_t) = 1, since x_t² ≡ 1 (mod y_t) from
x_t² − 2y_t² = 1, hence x_{2^j t} ≡ 1 (mod y_t) inductively.
Each x_{2^j t} ≥ x_t ≥ 3.

**Cofactor bound.** For any odd prime p | y_{m/2}: either
p | y_t, and then y_{m/2}/p^{f_p} ≥ ∏_{j=0}^{k-2} x_{2^j t}
≥ 3^{k-1}; or p | x_{2^J t} for exactly one J, and then
y_{m/2}/p^{f_p} ≥ ∏_{j≠J} x_{2^j t} ≥ 3^{k-2}. Either way,
D_m/qt = 8·(y_{m/2}/p^{f_p})² ≥ 8·3^{2k−4}.

**Count bound.** The number ω of distinct prime powers dividing
D_m satisfies ω ≤ log₂ D_m < 3m for m ≥ 3 (D_m < 2·5.83^m).

**Conclusion.** Summing over twin qt (a subset of all odd prime
powers, so the bound below applies a fortiori):
Σ qt / D_m = Σ 1/(D_m/qt) ≤ ω / (8·3^{2k−4})
≤ 3·2^k·t / (8·3^{2k−4}) = (243t/8)·(2/9)^k → 0 as k → ∞. ∎

So along m = 2^k·t the twin sum is exponentially small relative
to D_m. This covers in particular m = 2^k, 3·2^k, 5·2^k, ... —
but not the full sequence m → ∞, where the odd part of m is
unbounded and the chain gives no coprime factors.

## 4. Theorem B (conditional): the general case reduced to its hard core

**Hypothesis H.** For all sufficiently large m, every twin
qt ‖ D_m satisfies qt ≤ D_m/m².

**Theorem.** Under H, the Twin Sum Lemma holds for all m.
*Proof.* Σ qt / D_m ≤ Σ_{twin qt} 1/m² ≤ ω/m² ≤ 3m/m² = 3/m
→ 0. ∎

H is exactly the statement that no twin prime power dominates
D_m. It is open, and it fails at m = 5, 7 (qt = D_m/4 there), so
Theorem B is a reduction, not a proof: the remaining content of
the Twin Sum Lemma is precisely H. Note the equivalence in the
other direction too: if some twin qt ≥ c·D_m for infinitely
many m, the lemma is false; if max twin qt = o(D_m/ω), it is
true. No intermediate position is available.

## 5. What this means for Δ(m) → 0

The wave-25 conditional proof of Δ(m) → 0 used the Twin Sum
Lemma for general m. It is now unconditional along m = 2^k·t
(t fixed) by Theorem A, and conditional on H in general by
Theorem B. The next step toward the full lemma is not more
counting: it is the arithmetic of prime powers in the Pell
sequences x_m, y_m — specifically, ruling out (or exhibiting)
infinitely many m where a twin prime power exceeds D_m/m².
