# Strong-convexity Poincare inequality on a hard box

Checked 2026-10-06. Status: the required real-probability inequality is supported by an exact primary theorem plus an elementary limiting corollary. No implication for a quantum trace contour is asserted.

## Primary source and exact statement

A. V. Kolesnikov and E. Milman, *Brascamp-Lieb type inequalities on weighted Riemannian manifolds with boundary*, arXiv:1310.2526v7, 23 November 2017. https://arxiv.org/pdf/1310.2526v7
Published in J. Geom. Anal. 27 (2017), 1680-1702, DOI 10.1007/s12220-016-9736-5.

Theorem 3.1(1), printed p. 13, is the Neumann dimensional Brascamp-Lieb inequality. The standing assumptions are compact smooth connected oriented manifold with C^2 boundary and measure exp(-V)dVol, V in C^2. For a locally convex boundary, II>=0, and positive generalized Ricci tensor, it bounds variance for every f in C^1(M). Taking Euclidean metric and generalized dimension N=infinity gives

Var_mu(f) <= integral <(Hess V)^(-1) grad f, grad f> dmu.

Section 3.1.2, equation (3.2), explicitly gives the consequence

Hess V >= lambda I >0  =>  Var_mu(f) <= lambda^(-1) integral |grad f|^2 dmu.

There is **no Neumann condition on the test function f** in this statement. The Neumann boundary condition is used for the auxiliary elliptic problem in the proof.

## Hard-box corollary: explicit approximation

Let B=prod_j[-R_j,R_j] with all R_j>0, and suppose V and f are C^2 and C^1, respectively, on a neighbourhood of B. Assume Hess V>=lambda I on B. Set

B_k = {x: sum_j (x_j/R_j)^(2k) <= 1},  k=1,2,... .

Each B_k is a compact convex body with smooth boundary: its defining polynomial is smooth and convex, and its gradient cannot vanish on level 1. Therefore its second fundamental form is nonnegative. The interiors B_k increase and exhaust the interior of B. The same V restricted to every B_k retains the identical Hessian lower bound lambda.

Apply the source theorem to the normalized measures

mu_k(dx) = Z_k^(-1) 1_{B_k}(x) exp(-V(x)) dx.

For fixed dimension and box, exp(-V), f, f^2, and |grad f|^2 are bounded on B. Dominated convergence gives Z_k->Z_B, convergence of means, variances, and energies. Passing to the limit proves

Var_{mu_B}(f) <= lambda^(-1) E_{mu_B}|grad f|^2,
mu_B(dx)=Z_B^(-1)1_B(x)exp(-V(x))dx.

The limiting argument is performed for each finite dimension. The constant is still lambda^(-1), so it remains uniform over any family of boxes and dimensions whose Hessian lower bound is lambda. Approximation need not be uniform in dimension to establish that conclusion. Smooth functions can then be extended to the weighted Sobolev domain by the usual density argument; the polynomial observables needed here already lie in C^1.

## Application to real cubic tilts

For a real parameter s in a fixed bounded interval, put

V_s(y) = (1/2)y^T K y - s sqrt(h) W_3(y),
B_h = [-rho/sqrt(h),rho/sqrt(h)]^m.

If K>=lambda_0 I and the nearest-neighbour cubic satisfies

||Hess W_3(y)|| <= C ||y||_infty,

then on B_h,

Hess V_s >= [lambda_0-|s|C rho] I.

Thus choosing rho so that lambda=lambda_0-s_max C rho>0 proves the desired Poincare inequality uniformly in m,h,s. Normalization is finite because the box is compact. The sign of the tilt is immaterial to this Hessian estimate.

Caution: Poincare alone controls centered variances. A bound such as E_s|grad W_3|^2=O(m) additionally requires uniform local fourth moments under the tilted measure. Those moments should not be silently inferred from this Poincare theorem without controlling coordinate means or supplying a separate moment argument.

## Retained source

kolesnikov_milman_1310.2526v7.pdf SHA-256:
f86893b5051a150a6827fd0523aa3733c5970a3cccc44b17a794f58cc4601727

The retained source was checked by the independent local review. The PDF hash
pins that source; redistribution is not part of this overlay. Equation (3.2)
is on printed p. 14.
