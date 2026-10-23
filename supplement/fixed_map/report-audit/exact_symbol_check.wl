(* Executed with Wolfram on 19 September 2026. *)
Clear[x,p,q];
aa=(3+x)/2; bb=x^2-x+1;
poly=Expand[(aa^2+bb^2+4 aa bb)/64];
claimed=53/256-9 Sin[4 Pi p]/128-33 Cos[8 Pi p]/512+Cos[16 Pi p]/512;
f=Cos[2 Pi (q+1/5)]+Cos[2 Pi (2 q+1/15)]
 +Sin[2 Pi (q+1/5)] Sin[2 Pi (p+1/8)]
 +Sin[2 Pi (2 q-7/20)] Sin[4 Pi p];
{poly,
 FullSimplify[(poly/.x->Sin[4 Pi p])-claimed,Assumptions->Element[p,Reals]],
 FullSimplify[(2 D[f,{p,2}]-4 D[f,{q,2}])/.{q->0,p->0}],
 FullSimplify[(f/.p->1/4-p)-f,Assumptions->Element[{p,q},Reals]]}
(* Returned, without warnings:
 {37/256-9 x/128+29 x^2/256+x^4/64,
  0,
  2 Pi^2 (-2+2 Sqrt[5]+Sqrt[5+Sqrt[5]]+32 Cos[2 Pi/15]),
  0}
 The equality of the trace derivative with the report's trigonometric
 expression is additionally checked exactly by SymPy in verify.py.
*)
