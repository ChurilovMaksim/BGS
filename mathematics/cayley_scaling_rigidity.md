# Cayley collision-curve equivalence

The complete maintained proof is in `manuscript/unified_sections/cayley_scaling.tex`.
For characteristic different from two and distinct parameters rho,sigma outside
{0,1,-1}, diagonal coordinate scalings and scalar multiples identify exactly
(rho,sigma) and (rho^-1,sigma^-1) over an algebraic closure. Unimodular Laurent
monomial changes add at most (sigma,rho) and (sigma^-1,rho^-1). All four
transformations preserve H x H when the parameters belong to an odd-order
multiplicative subgroup H. The class has two members when rho*sigma=1.

The proof uses the scaling invariants I=ae/(bd), J=c^2/(bd), a reciprocal
quadratic in rho, and the signed-permutation symmetries of the Newton square.
It excludes one fixed-polynomial averaging shortcut, not every averaging route.
The pointwise additive-energy exponent remains 8/3. No BGS conclusion follows.

Exact symbolic and finite-field verification:
`python computations/verification/cayley_scaling_rigidity.py --prime-limit 251`.
The finite checks support implementation correctness, not the unbounded proof.
