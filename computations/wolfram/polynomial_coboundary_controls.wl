(* FLOW-011: exact exponents and one scalar derivative only.
   Executed with Wolfram evaluator on 2026-10-04.
   This is not a stochastic/asymptotic proof certificate. *)
<|"EpsilonExponent"->26/3,"TimeExponent"->2/3,"StepCountExponent"->4(26/3)-2/3,"WeakLinearExponent"->9-26/3-2/3,"WeakQuadraticExponent"->10-2(26/3)-2/3,"ExitExponent"->4-26/3,"PrincipalRateExponent"->{-1/3,2/3-1},"OldBoundPolynomialCorollary"->FullSimplify[n^20 Exp[c l] n^-a /. l->Log[n]/Log[Log[n]],Assumptions->{n>Exp[E],a>20,c>0}],"GaussianSixthDerivative"->Simplify[D[Exp[-y^2/2],{y,6}]/Exp[-y^2/2]]|>
