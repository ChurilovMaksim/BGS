(* Exact symbolic check only; the proof is given in the mathematical text. *)
Clear[q,p,t,a,r];
r[q_] := (1-Cos[14 Pi q]) (1+Cos[2 Pi q]);
a[q_,p_] := Cos[14 Pi q]+r[q]/10+r[q] Sin[2 Pi q]/100-1/10+
  r[q+1/2] (-3 Cos[2 Pi p]+4 Sin[2 Pi p])/500;
FullSimplify[
 {a[0,p], D[a[q,p],q]/.q->0, D[a[q,p],p]/.q->0,
  D[a[q,p],{q,2}]/.q->0, D[a[q,p],q,p]/.q->0,
  D[a[q,p],{p,2}]/.q->0},
 Assumptions->Element[p,Reals]
]

