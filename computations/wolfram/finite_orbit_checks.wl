(* Executed through WolframLanguageEvaluator, timeConstraint=30, 22 Sep 2026.
   Auxiliary exact identities, not a proof of the smooth theorem. *)
Clear[q0,q1,q2,u,v,l,b,x,aa,bb,cc];
<|
 "doubleRoot" -> Reduce[q1+q2==2 q0 && q1 q2==q0^2,{q1,q2},Reals],
 "quadraticCoefficients" -> CoefficientList[
   Expand[x ((u+q0) x+(v+q0)/x+(q1+q2-2 q0))],x],
 "threePointVandermonde" -> Factor[Det[
   {{1,x,x^2},{1,l^2 x,l^4 x^2},{1,l^4 x,l^8 x^2}}]],
 "gaussianCompletion" -> Expand[-cc (x-bb/(2 cc))^2+bb^2/(4 cc)]
|>
