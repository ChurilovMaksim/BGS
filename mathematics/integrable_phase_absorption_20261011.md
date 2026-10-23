# Optimal integrable absorption bounds in every fixed L^p

**Stable claim:** BGS-TRACE-058. **State:** PROVED.
**Boundary:** Every fixed Lp absorption bound and Abel continuity; no uniformity as p grows and no local-law identification.
**Integration and review:** [11 October disposition](../archive/record/chat_integration_20261011.md).
**Original input:** [dated source](../archive/evidence/executions/20261011/chat-research/original/integrable_phase_absorption.md).


8 October 2026. Outside-repository continuation. This is a phase-ensemble regularity statement for arbitrary deterministic contractions, not a limiting spectral law. External novelty is unverified.

Let F be any n by n deterministic contraction, D independent uniform coordinate phases, and

X_(n,F)(v)=n^−1 Tr[(I−exp(−v/n)DF)^−1−I],   Re v>0.

For every fixed integer p≥2 there is a dimension-free constant C_p such that, for 0<Re v≤1,

||X_(n,F)(v)||_p ≤ C_p (Re v)^(−1+1/p).                 (1)

The exponent is optimal in this uniform class: n=1,F=1 gives a scalar Cauchy kernel whose p-th norm has precisely this order. In particular the derivative of the logarithm is integrable down to zero absorption in every finite L^p.

If log det(I−DF) is defined by its radial Abel limit, then that limit exists in L^p for each fixed n,F, and, uniformly in n,F and 0<s≤1,

||log det(I−exp(−s/n)DF)−log det(I−DF)||_p ≤ C'_p s^(1/p).       (2)

Neither individual boundary log determinants nor their norms are claimed bounded uniformly in n; the uniform assertion is their difference from positive scalar absorption.

## Refined arc-count moment bound

For F unitary, the finite rank-one resampling argument in physical_source_transport_20261011.md gives E(Z)_k≤mu^k and Var Z≤mu for a connected-arc count Z, mu=E Z. If mu≤1, the identity Z^p=sum_(k=1)^p S(p,k)(Z)_k gives E Z^p≤C_p mu. Therefore ||Z−mu||_p≤C_p mu^(1/p).

If mu≥1, the positive centered tail is bounded by the Poisson Chernoff estimate, giving ||(Z−mu)_+||_p≤C_p(sqrt(mu)+1). The negative part satisfies E(mu−Z)_+^p≤mu^(p−2)Var Z≤mu^(p−1). Thus for all mu≥0,

||Z−mu||_p≤C_p[mu^(1/p)+mu^(1−1/p)].                  (3)

Here p is fixed; constants are not controlled uniformly in growing p.

Integrating centered arc counts against the derivative of the circular Cauchy kernel as in physical_source_transport_20261011.md yields, with r=exp(−Re v/n), d=1−r,

||X_(n,F)(v)||_p≤C_p[(nd)^(−1+1/p)+(nd)^(-1/p)].        (4)

Indeed n^−1 integral_0^pi (nu)^alpha/(d+u)² du≤C_alpha(nd)^(alpha−1) for 0<alpha<1. Since nd≥1−exp(−Re v)≥Re v/2 for 0<Re v≤1, (1) follows for unitary F. Complex v is reduced by common-phase rotation.

## Poisson extension from unitaries to contractions

Write a singular-value decomposition F=U diag(sigma_j)V*, 0≤sigma_j≤1. For each phase realization D and fixed Re v>0, the scalar function

f(z_1,...,z_n)=n^−1 Tr[(I−exp(−v/n)D U diag(z_j)V*)^−1−I]

is holomorphic on the polydisk and continuous on its closure. Repeated Poisson representation in each coordinate expresses f(sigma_1,...,sigma_n) as the average of f(exp(i theta_1),...,exp(i theta_n)) against the product Poisson measures with parameters sigma_j. A parameter equal to 1 uses a point mass. Each boundary matrix U diag(exp(i theta_j))V* is unitary. Jensen and averaging D transfer (4) unchanged to every contraction F. The same product measures are independent of D; no random replacement of the actual phases is made.

This extension avoids incorrectly applying eigenvalue interlacing to a nonnormal contractive matrix.

## Abel logarithm and sharpness

The Neumann log determinant has derivative partial_s log det(I−exp(−s/n)DF)=X_(n,F)(s). Integrate (1) over 0<s≤1. The integral of s^(−1+1/p) is p s^(1/p), so the logarithms are Cauchy in L^p as s decreases to zero. This defines the branch in (2), and the same estimate proves it. For strictly contractive F it agrees with its usual Neumann logarithm at zero absorption.

For n=1,F=1 and real v↓0, r=e^−v and |r exp(i theta)/(1−r exp(i theta))| is comparable to (v²+theta²)^−1/2 on a fixed neighborhood of theta=0. Its p-th integral is comparable to v^(1−p) for p>1, proving optimality of the exponent in (1).

## Current limitation

Estimate (2) removes scalar absorption from log determinants in every fixed finite L^p. It does not by itself improve the physical-source comparison beyond L²: that improvement also needs control of the real-flow boundary logarithm in the stronger norm, including its large-absorption tail. This missing step must not be bypassed by boundedness in a smaller norm.
