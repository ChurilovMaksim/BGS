# Research pass, 22 September 2026

Base: ChurilovMaksim/BGS, main at
`39d4e01ae6a6b3eb472ab30266b708ca71a70a16`.
Root tree: `602f712e6e04bbdbbf6292c50758dfeb1d55ba39`.

## Outcome

The new maintained result is the smooth finite-orbit rigidity theorem in
`../mathematics/finite_orbit_resonance_rigidity.md`: every nonconstant real
smooth observable supported on finitely many signed hyperbolic frequency
orbits has independent finite Poisson-bracket lag classes modulo L2
coboundaries. Arbitrary phases and both trace signs are included. The proof
is a project derivation with adversarial self-review; independent referee
acceptance, external priority, and full formalization are unestablished.

The associated pair-product lemma gives a common real entire all-pass
factorization when all sufficiently large pair channels vanish. Bounded
values of det(k,Ak) imply finitely many signed orbits; hence a smooth
zero-variance counterexample must have unbounded invariant values on its
Fourier support. No uniform quantitative coercivity is claimed.

## Audit scope and access boundary

The GitHub connection exposed repository reads but no write action. Direct
container access to GitHub failed. No complete checkout, commit, or push was
performed. The root tree and the relevant current research, status, proof,
source, and manuscript sections were inspected. This is not a line-by-line
audit of every file, a full restoration of the repository, or a complete CI
run. An expired historical Actions artifact was not recovered.

The delivered overlay contains only new maintained files. The separate
integration plan guards seven edits by exact Git blob hashes at the pinned
base; it does not overwrite unseen files wholesale. The root instructions
are an addition, not a replacement of an existing AGENTS.md. Historical
research is preserved. The actual remote main remains unchanged by this pass.

## Route outcomes and deduplication

1. **Finite-Fourier support geometry: existing result rederived.** A proposed
   isolated-mode argument was compared against the repository. Its conclusion
   was already proved on 7 September in `extremal_resonance_nondegeneracy.md`
   and the all-lag manuscript section. It is an audited input, not new work.
2. **Single-orbit / Fourier-line routes: existing results retained.** The
   weighted single-orbit result and the sharp Fourier-line coercivity theorem
   have different domains; neither is replaced or relabeled by this pass.
3. **Finite unions with Gevrey decay: superseded intermediate restriction.**
   Pair separation and a temporal generating-function argument first gave a
   restricted route. The common-factor argument removes the extra decay
   assumption and proves the stated C-infinity theorem. No weaker duplicate
   proof is installed as another canonical result.
4. **All-pair smooth finite-orbit route: project proof.** Large-gap separation,
   two distinct correlation products, rational-to-Laurent rigidity, a common
   real all-pass factor, and the existing finite-Fourier theorem close this
   route. Details and adverse checks are in the proof and its audit.
5. **Arbitrary infinitely many orbits: unresolved.** The exact late-collision
   identity in the proof prevents a family-uniform isolation threshold.
   Neither truncation nor generic positivity supplies a uniform lower bound.
6. **Frozen quantum family: still open.** Existing algebraic-return and
   block-memory notes already use Lindemann--Weierstrass; that qualitative
   mechanism is not new here. The fixed-family mixed-loop criterion was
   checked against Bourgade--Huang v2, Theorem 1.9. Its model-specific error
   hypothesis has not been proved.

## A concrete stale-status correction

The final paragraph of `quantitative_resonance_transversality.md` still
called the finite-polynomial several-orbit problem open. The pinned
`extremal_resonance_nondegeneracy.md` already proves it. The integration plan
replaces that paragraph with the correct finite-polynomial status, the new
smooth finite-orbit scope, and the remaining arbitrary-analytic question.
The quantitative transversality estimates themselves are not changed.

## Reproduction of this addition

From the repository root after integration:

```sh
mkdir -p build/verification
python3 computations/verification/finite_orbit_resonance.py \
  --output build/verification/finite_orbit_exact.json
g++ -std=c++20 -O2 -Wall -Wextra -pedantic \
  computations/verification/finite_orbit_degeneracy.cpp \
  -o build/verification/finite_orbit_degeneracy
build/verification/finite_orbit_degeneracy \
  > build/verification/finite_orbit_cpp.json
python3 computations/maintenance/sync_finite_orbit_section.py --check
```

The dated evidence directory contains the actual outputs from this pass.
Python checked 2,976 channel identities, eight matrices and 28,520
cross-patterns. Its displayed finite target set has a rigorous all-cross-gap
stopping rule, not a guessed orbit cutoff. C++ checked 147,456 identity
candidates, 912 identity cases, 7,680 recurrences and 40 late-collision
identities. These finite checks do not prove the infinite theorem.
The Wolfram input/output are preserved. The Lean source was not compiled.
The standalone new paper was compiled and visually inspected; the full
unified manuscript was not built in a complete checkout.

## Remaining mathematical programme

The broad goal remains a positive, correctly desymmetrized and unfolded
microscopic spectral theorem for a natural fixed chaotic quantization.
The universal formulation must distinguish classical chaos from extra
arithmetic or quantum structure; an unrestricted implication from chaos
alone is not adopted as a proved premise.

The new analytic frontier requires quantitative control of infinitely many
orbit families, including cross-family cancellations. A decisive next lemma
would bound their total contribution relative to a surviving channel using
analytic decay and arithmetic separation; no such bound is supplied here.

Separately, the fixed-map frontier requires Heisenberg-scale joint traces
or the full normalized mixed-resolvent hierarchy at every fixed order and
on arbitrary compact subsets of both half-planes. The pair Abel transform
alone is only a necessary lower-order checkpoint. Classical variance,
short-return laws, absence of smooth classical symmetries, and qualitative
absence of exact quantum returns do not replace that estimate.

The research target is not reduced by calling this partial result BGS. This
pass ends with a durable theorem on a precisely specified subsidiary class,
a corrected dependency/status boundary, and no claim of a prize-level or
complete universality result.
