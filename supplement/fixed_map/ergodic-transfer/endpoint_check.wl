(* Executed with Wolfram, 18 September 2026. *)
Clear[t,s,a,b];
e={{Cos[b],I Sin[b]},{I Sin[b],Cos[b]}};
u=DiagonalMatrix[{Exp[I a],Exp[-I a]}];
{FullSimplify[Tr[e.u],Assumptions->Element[{a,b},Reals]],
 FullSimplify[Det[e.u]],
 Limit[(ArcCos[Cos[t] Cos[Pi t]]/t-Pi)/(2 Pi),
       t->0,Direction->"FromAbove"],
 FullSimplify[Limit[Sin[s t]^2 Cos[Pi t]^2/
                   (1-Cos[s t]^2 Cos[Pi t]^2),t->0],Assumptions->s>0]}
(* Returned {2 Cos[a] Cos[b],1,
  (-Pi+Sqrt[1+Pi^2])/(2 Pi),s^2/(Pi^2+s^2)}.
  The limit engine also emitted intermediate Power::infy and
  Infinity::indet warnings. These are not suppressed or treated as proof.
  The following separate coefficient calculation checks both limits
  without evaluating a singular quotient at zero. *)
Clear[t,s];
{SeriesCoefficient[Cos[t] Cos[Pi t],{t,0,2}],
 SeriesCoefficient[Sin[s t]^2 Cos[Pi t]^2,{t,0,2}],
 SeriesCoefficient[1-Cos[s t]^2 Cos[Pi t]^2,{t,0,2}]}
(* Returned {(-1-Pi^2)/2,s^2,Pi^2+s^2}, without warnings. *)
