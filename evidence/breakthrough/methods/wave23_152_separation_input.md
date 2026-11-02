# Wave 23, task 4 — What 152's separation step must see instead

## The question

hSep's input is mode sums `S_k(ξ) = Σ_j e(kξ_j)`; route (b)'s input is
`(sorted(y), sorted(w_y))`. Both fail to separate Γ-orbits inside
fibers (waves 7, 18, 22). What new input would separate — computable
from the step's data, or a named explicit extension of it?

## 1. Impossibility for the old input classes

**Symmetric data — theorem, no computation needed.** A fiber is by
definition the level set of the coordinate multiset, and every
symmetric function factors through the multiset. Hence every function
of mode sums, power sums, pair sums, or class sums is constant on
fibers and cannot separate orbits inside a fiber. Any repair keeping
the input symmetric is impossible in principle (wave 13 §4, wave 22).

**(fiber, w)-data — 152 explicit counterexamples.** The wave-18 census
of split fibers fully in support at m = 12 contains 152
(fiber, w)-classes — same `sorted(y)`, same `sorted(w)` — holding ≥ 2
Γ-orbits. So no function of route-(b) input separates either.

**Corollary.** The step must gain genuinely cyclic-order data: data
that varies inside a fiber while being Γ-invariant. That data is not
computable from the step's current input and must be added explicitly.

## 2. What suffices at m = 12: one scalar

Define the cyclic sum (kernel symmetric in its arguments, hence
dihedral-invariant, i.e. well-defined on Γ-orbits; 0 violations on
50 fibers × 24 perms, and structurally forced):

```
C(y) = Σ_i y_i · y_{i+1} · |y_i − y_{i+1}|   (indices mod 12)
```

**C separates all 762 split fibers on support and all 152 failing
(fiber, w)-classes at m = 12** (exact integers, census orbit reps).
So the minimal new input at m = 12 is one scalar beyond (fiber, w)-data.

Battery (separated groups; level A = 762 split fibers,
level B = 152 failing classes):

| kernel | A | B |
|---|---|---|
| ab | 269 | 0 |
| absdiff (≈ min ≈ max — see below) | 731 | 144 |
| a2b2 | 753 | 143 |
| a3b3 | 761 | 151 |
| **ab·|a−b|** | **762** | **152** |
| triple product | 596 | 70 |
| direction changes | 438 | 66 |

Two structural notes. First, absdiff/min/max are the same separator:
`max − min = |a−b|` and `max + min = a+b`, with `Σ(a+b)` fiber-constant.
Second, ab fails at level B for a reason: `Σ y_i w_i` is constant on
all 152 failing classes (verified), and the identity
`⟨y, Hy⟩ = 6Σy_i² − 2Σ y_i y_{i+1} = D·Σ y_i w_i` then forces the ab-sum
to be (fiber, w)-constant. So ab cannot separate at level B at m = 12.

Why low-degree kernels are unreliable: the wave-22 exhibit pair
satisfies `y2[i] = y1[5i+4]` — an affine position permutation — so
y2's 1-step edges are y1's 5-step edges, and every low kernel agrees
on the pair (its Adj multisets are even fully disjoint, symmetric
difference 24). Unit-step correlations are often degenerate for Fix
vectors: 5- and 7-step ab-sums agree with 1-step sums on 143/201
sampled census reps (11-step agreement is trivial, being reversal).
This is an observation, not a theorem, and it is why a mixed higher
kernel like `ab·|a−b|` is needed.

## 3. The answer: what the step must gain

- **Minimal at m = 12, on support:** the scalar `C(y)` alongside
  (fiber, w)-data. But C is census-fitted: a fixed kernel carries no
  general-m guarantee (exponentially many fibers versus one fixed
  kernel; a generic-kernel argument shows *some* kernel separates any
  finite census, but that is a per-m certificate, not a uniform lemma).
- **Robust general input:** `Adj(y)` itself — the full adjacent-pair
  multiset. It separates 762/762 at m = 12 (wave 21), 39/39 at m = 8,
  10/10 at m = 16 (wave 22) — every known split fiber — and is
  Γ-invariant cyclic-order data that mode sums provably do not
  determine (wave 22).
- **Restated separation lemma:** "given the fiber, the w-class, AND
  Adj(y) (resp. C(y) at m = 12), Γ-orbits are separated" — provable
  per m by certificate (orbit representatives + Adj/C table), never
  by a symmetric invariant.
- **Alternative:** bypass separation entirely. The corrected route
  `R = Bsym_fiber − Δ` (wave 19) needs orbit phases, not adjacency;
  Adj is not needed for Δ.

## Scope limits (honest)

- C(y) is tested at m = 12 on support only; no claim at any other m.
- Adj at m = 16 on support is untested (sampling bound only, wave 22).
- `Σ y_i w_i` constancy on (fiber, w)-classes is empirical at m = 12;
  its general-m mechanism is open.
- Scripts: `wave23_separation_cyclic.py` (battery, invariance check,
  exhibit pair), `wave23_separation_cyclic2.py` (extended battery,
  greedy, affine mechanism). Repository untouched; no Lean build.
