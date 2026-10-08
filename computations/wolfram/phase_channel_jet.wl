(* Exact symbolic controls, not proofs of the matrix or asymptotic theorems. *)
Clear[r, th, p, m];
p = (1-r^2)/(1-2 r Cos[th]+r^2);
checks = {
  FullSimplify[3 D[p,th]^2/p-p^3+p-2 D[p,{th,2}],
    Assumptions -> 0<r<1 && Element[th,Reals]],
  FullSimplify[((1+4 r^2+r^4)/(1-r^2)^2-1)/3-2 r^2/(1-r^2)^2],
  FullSimplify[36 Binomial[m,3]+9 m (m-1)+m-(6 m^3-9 m^2+4 m),
    Assumptions -> Element[m,Integers] && m>=3]
};
If[checks =!= {0,0,0}, Print["FAIL: ",checks]; Exit[1]];
Print[checks];
