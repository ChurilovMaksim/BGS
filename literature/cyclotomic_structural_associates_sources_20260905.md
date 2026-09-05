# Source audit for inverse structural associates — 2026-09-05

This note records the bounded literature check around
`mathematics/cayley_inverse_structural_associates.md`.  It is deliberately
conservative about novelty.

## 1. Bass: complete relations among cyclotomic differences

H. Bass, **Generators and relations for cyclotomic units**, *Nagoya
Mathematical Journal* **27** (1966), 401--407,
DOI `10.1017/S0027763000026258`.

Bass proves a complete relation theorem for the multiplicative group generated
by cyclotomic differences `1-zeta`.  The prime-conductor specialization is
already a load-bearing source in `cayley_trace_intercept_rigidity.md`.

For the new structural-associate theorem, Bass supplies background explaining
why quotients of products of sine/cyclotomic factors are natural units.  The
four `w_e = epsilon w_f` identities are not imported from Bass; they are proved
by explicit Laurent factorization in the project.

## 2. Ennola: relations between cyclotomic units

V. Ennola, **On relations between cyclotomic units**, *Journal of Number
Theory* **4** (1972), 236--247,
DOI `10.1016/0022-314X(72)90050-9`.

Ennola develops explicit relations among cyclotomic units and is part of the
classical relation theory cited by later applications.  This makes a novelty
claim based merely on finding a sparse quotient of sine units inappropriate
without a much deeper comparison.

No statement from Ennola is currently used as a theorem input for the four
inverse-row identities.

## 3. Fu: projective equivalence and cyclotomic-unit matching

H. Fu, **Projective Equivalence for the Roots of Unity**, *Journal of
Algebraic Combinatorics* **56** (2022), 823--871,
DOI `10.1007/s10801-022-01134-1`, arXiv `1905.01510`.

Fu converts equality of cross-ratios of roots of unity into multiplicative
relations among cyclotomic differences / their absolute values and invokes the
Bass--Ennola--Washington relation framework.  This is the closest mechanism
found in the bounded search to the present use of real sine units.

The present reduced-edge elements

```text
w_(a,b)=2-v_a-v_b
```

are not themselves just one cyclotomic difference, and the project theorem
proves a specific `K mod 5` family of associations between such sums.  The
bounded search did not locate these four formulas verbatim or an immediately
identical theorem in Fu.  That absence is **not** evidence of novelty.

## 4. Hoechsmann: cyclotomic units over finite fields

K. Hoechsmann, **Cyclotomic units over finite fields**, *Rendiconti del
Circolo Matematico di Palermo* **44** (1995), DOI `10.1007/BF02849803`.

The abstract studies the image of the cyclotomic-unit group of the real
prime-cyclotomic ring modulo a rational prime `q`.  This is closer to the new
active problem than a characteristic-zero unit-basis theorem: after the
structural associations are understood, the project needs to control how many
reduced edge elements can vanish in one residue embedding.

**Status: lead, not theorem input.**  The exact hypotheses and quantitative
content have not yet been matched to the row-multiplicity problem from the full
paper.

## 5. Formal-library lead

Current mathlib documentation contains primitive-root cyclotomic-unit lemmas,
including association of `zeta^i-1` and `zeta^j-1` when the exponents are
coprime to the root order.  This is relevant to a future formalization of the
unit status of the `eta_n`, but the present structural theorem has not been
formalized in Lean.

## 6. Bounded-search conclusion

Searches covered the phrases/mechanisms

```text
cyclotomic-unit relations,
ratios of sines at rational angles,
roots of unity and projective equivalence,
regular-polygon / trigonometric cyclotomic identities,
finite-field images of cyclotomic units.
```

The closest verified sources are Bass, Ennola and Fu.  No exact prior statement
matching all four inverse-row `K mod 5` identities was found in this bounded
search, but **no novelty claim is made**.  The identities may be special
Pluecker/Ptolemy/pentagonal consequences inside classical cyclotomic relation
theory.

The next literature task with higher information value is not another generic
cyclotomic-unit search.  It is to inspect finite-field image / unit-equation
results for a quantitative bound on the number of reduced edge values that can
vanish at one split prime ideal, uniformly as the conductor varies.
