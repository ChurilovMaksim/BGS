# Poisson kernel polynomial identity: symbolic check

Wolfram Language evaluator, 27 October 2026:

```wolfram
FullSimplify[Expand[(1+r^2-2 r c)^2-(1-r^2)^2 (1-c^2)-(2 r-(1+r^2)c)^2]]
```

Output: `0`.

A second exact call returned `{-1/6, -1/4, True}` for

```wolfram
{FullSimplify[1+2/3-2(11/12)],FullSimplify[2/3-11/12],
 Simplify[2 Exp[-x]/(1-Exp[-2 x])==1/Sinh[x],Assumptions->x>0]}
```

The polynomial identity is an elementary certificate used in the [pair-energy note](../../../../mathematics/trace-bridge/microscopic_unitary_stability_20261027.md). The two exponents occur in the [rounding note](../../../../mathematics/fixed-map/balanced_rounding_research_20261027.md). These calls do not certify the surrounding arguments, asymptotic limits or the original local law.
