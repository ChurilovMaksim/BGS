(* TRACE-011: actually evaluated 1 October 2026; exact algebra only. *)
Clear[s, theta, q, d];
theta = 2 (s - 3)/(s - 2);
{FullSimplify[(1 - 2/s) - (theta/2 + (1 - theta)/s)],
 FullSimplify[(3 - theta)/s],
 FullSimplify[(d q)^3/((d q^3) d^2)],
 FullSimplify[(d q)^2/((d q^3) d)],
 FullSimplify[d q^4/(d q^3)],
 Table[{r, (r-3)/(r-2), 1/(r-2)}, {r, {10/3, 7/2, 4}}]}

(* Independent stable Gaussian algebra; the Python check uses the CUE density. *)
Clear[gm, terms];
gm[m_] := Module[{p, n, values},
 p = Select[m, # > 0 &]; n = -Select[m, # < 0 &];
 If[Max[Total[p], Total[n]] > 4, Return[$Failed]];
 If[Sort[p] =!= Sort[n], Return[0]];
 values = DeleteDuplicates[p];
 Times @@ ((#^Count[p, #] Factorial[Count[p, #]]) & /@ values)];
terms = {{{1, 1, -2}, 1}, {{1, -2}, 2}, {{-2}, 1}, {{1, 1}, 1}, {{1}, 2}};
{Sum[(l-1)! StirlingS2[4,l], {l,1,4}], BellB[3], BellB[6],
 Sum[terms[[i,2]] terms[[j,2]] gm[Join[terms[[i,1]], -terms[[j,1]]]],
 {i,Length[terms]}, {j,Length[terms]}]}
