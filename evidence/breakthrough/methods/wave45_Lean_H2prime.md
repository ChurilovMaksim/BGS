# Wave 45, task 8 — Lean draft: H2' growth lemma + collision factorisation

## Verdict

Draft BUILDS (0 errors) with exactly 3 `sorry`. It is statement
well-formedness plus two genuinely proved identities — NOT a proof of H2'.
Repository untouched; all work in the test-copy project.

## File

- Draft: `~/workspace/bgs-formalization/formalization/Bgs/Breakthrough/H2primeGrowth.lean`
  (import `Mathlib` on line 1, namespace `Bgs.H2primeGrowth`, sequential build only)
- Build: `export PATH="$HOME/.elan/bin:$PATH"; lake build Bgs.Breakthrough.H2primeGrowth`
- Result: 8706 jobs, 1084 s, 0 errors, 3 `sorry` warnings, olean 294 KB
  (`.lake/build/lib/lean/Bgs/Breakthrough/H2primeGrowth.olean`)

## Theorem inventory (general commutative ring `R`, not `ℤ[√2]`)

| Theorem | Status | Axioms |
|---|---|---|
| `growth_step` (binomial step: `(1 + p^k γ)^p = 1 + p^(k+1) γ'`, `γ' ≡ γ mod p`, `p` prime) | SORRY | propext, sorryAx |
| `growth_iter` (`β^(d p^j) = 1 + p^(j+1) γj`, `γj ≡ γ mod p`) | proved by induction from `growth_step` | propext, sorryAx (inherited only) |
| `growth_congr` (`p^j ∣ β^(d p^(j-1)) − 1`, `j ≥ 1`) | proved | (via `growth_iter`) |
| `order_formula` (`orderOf β = d p^(j-1)` in `R ⧸ (p^j)`, needs `γ ≢ 0 mod p`) | SORRY | — |
| `collision_identity` (`(β^t−1)(β^(2b+t)+1) = 2sβ^(b+t)(B(b+t)−B b)`, from `β·βc = 1` and `2s·B k = β^k − βc^k`) | PROVED (`linear_combination`) | propext, Quot.sound — NO sorryAx |
| `factorisation_scaled` (divisibility of the product ⟺ divisibility of the scaled difference) | PROVED (rewrite of the identity) | propext, Quot.sound — NO sorryAx |
| `factorisation` (full equivalence to `(B(b+t) − B b)`, needs `2sβ^(b+t)` a unit mod `p^f`) | SORRY | — |

`grep -c sorry` on the file is 4: the 3 tactic `sorry` plus one mention in
the header comment. Axiom audit via `#print axioms` on the built olean
confirms the table (no `Classical.choice` anywhere).

## Build history (honest)

- First build: 7568 s, 1 error — my `linear_combination` coefficient was
  wrong: the identity needs `β^t * βc^t = 1` as well as `β^b * βc^b = 1`
  (the leftover goal was `−1 + β^t·β^b·βc^t·βc^b = 0`).
- Fix: added `h2 : β^t * βc^t = 1` and coefficient
  `(β^t * βc^t − β^t) * h1 + h2`. Second build: success, as above.
- The `EXIT:0` printed by the first build's pipeline was `tail`'s status,
  not the build's: the build itself failed (`Lean exited with code 1`).

## NOT claimed

- The instantiation to `ℤ[√2]` (`βc = star β`, `s = √2`, `B k = (β^k).im`)
  is NOT in this draft. `Zsqrtd` does exist in this Mathlib
  (`Mathlib/NumberTheory/Zsqrtd/Basic.lean`) — that is the natural next
  step, not done here.
- The binomial step, the order minimality, and the quotient-unit transfer
  are open formal content, not hidden by the proved identities.
- No Lean built in the BGS repository; no change to `main`.
