# Mapped domain check and qualification of the nonlinear-slice witness

6 October 2026. This adds to `report.md` §3 and the `nonlinear_constraint` object in `checks.json`. Those original files are preserved. No canonical files changed.

## Precisely scoped conclusion

At a **fixed zero-mode coordinate**, the stated componentwise change of variables does not map the new linear zero-sum slice to the old linear zero-sum slice. An accompanying change of zero-mode coordinate can repair the slice in the scalar example. Therefore the witness identifies a missing change-of-slice justification, not an impossibility of a gauge reparametrization, an error lower bound for the integrated observable, or a refutation of the universality conclusion.

## Source and strict interior

Source: H. A. Weidenmüller, *Massive Modes for Quantum Graphs*, arXiv:1812.00655v1. Local PDF SHA-256 `51d115ced63d8e673c377b2886681dd5d7dcabdb5eca0566157c9b7499492f0d`. Primary URL: https://arxiv.org/pdf/1812.00655v1 . Exact locators: (6)–(7), printed pp.3–4; (18)–(23), printed pp.5–6; (33)–(35), printed p.9.

Equation (7) has the bosonic disk condition |Z_BB|<1 and the associated conjugacy condition. Set all Grassmann variables and all fermionic-body entries to zero. Take the zero mode g0=I, so Y=0 and the original bosonic Z equals xi by (22). Set tilde variables equal to the real bosonic variables. The scalar form of (33) is xi=psi/sqrt(1+psi²), with inverse psi=xi/sqrt(1-xi²).

Use the stricter witness

psi=(1/4,1/4,-1/2,0),
xi=(1/sqrt(17),1/sqrt(17),-1/sqrt(5),0).

Then sum psi=0, but

sum xi = 2/sqrt(17)-1/sqrt(5)>0,

because 4/17>1/5. Every |psi_i|<=1/2 and every |xi_i|<1/2. In particular

1-xi_i²=(16/17,16/17,4/5,1),

strictly positive, bounded away from the bosonic boundary. All square roots and inverses are regular. The matrices g(xi_i) in (14) satisfy g(xi_i)^* diag(1,-1) g(xi_i)=diag(1,-1), verified exactly. This is an admissible ordinary bosonic body of the source's local chart.

For arbitrarily small epsilon>0 one may instead take (epsilon,epsilon,-2epsilon,0). The transformed sum is

2epsilon/sqrt(1+epsilon²)-2epsilon/sqrt(1+4epsilon²)
=3epsilon³+O(epsilon^5)>0.

Thus the fixed-coordinate mismatch occurs in every neighborhood of the origin. Padding zeros or repeating the four-coordinate block preserves validity in higher even dimensions. This is solely a pointwise statement; the witness makes no assertion about the integration weight of these configurations.

The original larger witness also had |xi_i|<1 and regular bosonic denominators: psi_BB is not itself restricted to the unit disk under (33). The smaller witness avoids any reliance on that distinction and is the preferred witness for later citation.

## A simultaneous zero-mode adjustment is genuinely possible

Let z_i be the four displayed xi_i. For c in (-1,1), define

xi_i'(c)=(z_i-c)/(1-c z_i),
F(c)=sum_i xi_i'(c).

The source's real bosonic Möbius action gives exactly

z_i=(c+xi_i'(c))/(1+c xi_i'(c)).

All denominators are positive. Moreover

F'(c)=sum_i (z_i²-1)/(1-c z_i)²<0,
F(-1)=4, F(1)=-4.

Hence there is a unique c in (-1,1) with sum_i xi_i'(c)=0. It is positive since F(0)>0. Taking Y=c and the corresponding U(1,1) zero-mode element represents the same z_i with the old linear slice restored. This is a change of the collective zero-mode coordinate, not merely the stabilizer freedom g->gk that leaves the coset point fixed.

Accordingly, the exact caution is: the componentwise map (33), with Y held fixed, does not preserve (23) when one imposes (35). Equality or asymptotic equivalence of the full integrals would additionally require a consistent collective-coordinate transformation, the induced constrained measure, and transformed source factors. The scalar witness neither rules that out nor proves that the missing integral error survives N->infinity.

## Execution

`python3 domain_checks.py > domain_checks.json` passed in exact SymPy rational/algebraic arithmetic. It checks disk margins, inverse-map identities, U(1,1) membership, the Möbius reconstruction and derivative identity, and the small-epsilon leading coefficient. The printed numerical root is illustrative only; existence and uniqueness follow from the exact monotonicity argument. Original `report.md`, `checks.py` and `checks.json` were not overwritten.
