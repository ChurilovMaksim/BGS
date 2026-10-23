# Analytic rigidity of pointwise Poisson-bracket cancellation

**Status: EXACT.** This project proof excludes the pointwise-zero mechanism for nonconstant real-analytic observables of a hyperbolic toral automorphism. It does not by itself exclude a nonzero Poisson bracket which is a dynamical coboundary, so it is not yet an all-analytic variance theorem. External priority is not assessed.

Let `S in SL(2,Z)` be hyperbolic and write `C g=g o S`. The torus Poisson bracket is

```text
{f,h}=f_x1 h_x2-f_x2 h_x1.
```

## Theorem

If `g:T^2->R` is real analytic and

```text
{g,C g}=0                                                 (1)
```

identically, then `g` is constant.

Equivalently, every nonconstant real-analytic observable has a nonzero second-order Poisson bracket with its first hyperbolic translate.

## Proof

Assume that `g` is nonconstant. Its regular set

```text
R={x: d g_x != 0}
```

is open and has full Lebesgue measure. Indeed at least one first derivative of `g` is a nonzero real-analytic function, and the zero set of a nonzero real-analytic function has measure zero; the critical set is contained in that zero set.

On `R` define the tangent line to the level set

```text
L(x)=ker(d g_x) in RP^1.                                 (2)
```

At any point for which both `x` and `Sx` are regular, equation (1) says that the two nonzero covectors

```text
d g_x,
d(Cg)_x=d g_(Sx) o S
```

are linearly dependent. Hence their kernels agree, and therefore

```text
L(Sx)=S L(x).                                            (3)
```

Let

```text
R_infty=intersection_(n in Z) S^(-n) R.
```

This still has full measure. By Poincare recurrence, almost every `x in R_infty` is recurrent. For such an `x` choose positive integers `n_j->infinity` with

```text
S^(n_j)x -> x.
```

The line field (2) is continuous on the open set `R`, so

```text
L(S^(n_j)x) -> L(x).                                     (4)
```

But iteration of (3) gives

```text
L(S^(n_j)x)=S^(n_j)L(x).                                 (5)
```

Let `E^s,E^u` be the two real eigenlines of the hyperbolic matrix `S`. Its projective action has exactly these fixed lines; every line other than `E^s` converges under positive iteration to `E^u`. Combining (4)--(5), a recurrent regular point must therefore satisfy

```text
L(x) in {E^s,E^u}.                                      (6)
```

Equation (6) holds almost everywhere in `R`. Since `L` is continuous, it actually holds everywhere in `R`: otherwise a neighbourhood of a point whose line stays a positive projective distance from `{E^s,E^u}` would have positive measure, contradicting (6).

On each connected component `U` of `R`, continuity and discreteness of the two-point target imply that `L` is constant, equal to one of the eigenlines. Choose one nonempty component and an eigenvector `e` spanning that line. Then

```text
D_e g=0 on U.                                            (7)
```

The directional derivative `D_e g` is real analytic. Since it vanishes on a nonempty open set, analytic continuation gives

```text
D_e g=0 on all of T^2.                                   (8)
```

An eigenline of a hyperbolic integral determinant-one matrix has irrational slope: a rational eigenline would give a rational algebraic-integer eigenvalue, hence an integer dividing the determinant, necessarily `+/-1`, contradicting hyperbolicity. The linear flow in direction `e` is therefore dense on `T^2`. Equation (8) makes `g` constant along every such orbit, so continuity forces `g` to be constant on the torus, a contradiction.

This proves the theorem.

## Consequence for the remaining analytic variance problem

For real analytic `g`, the bracket

```text
h_g={g,Cg}/(4*pi)
```

is analytic. If an analytic observable with `Gamma_S(g)=0` exists, the theorem shows that it cannot use the separated-support mechanism `h_g=0`. It must instead satisfy

```text
h_g != 0,
Gamma_S(g)=0,                                            (9)
```

i.e. its nonzero analytic bracket must have zero sum on every oriented frequency orbit and hence lie in the dynamical coboundary class selected by the orbit-sum criterion.

Thus the all-analytic frontier is reduced to a genuine cohomological-cancellation problem. The compactly supported Gevrey counterexample and the non-finite-Gevrey temporal gauges do not realize (9).

Nothing here supplies Heisenberg-scale quantum trace control or microscopic BGS universality.
