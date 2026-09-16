(* Exact controls for mathematics/shadow_tube_history_bridge.md.
   Executed in the connected Wolfram kernel on 2026-09-16.
   Finite computations do not prove BGS or geometric periodic equidistribution. *)
ClearAll["Global`*"];
h = {{1,1},{1,-1}}/Sqrt[2];
b = {{1,1},{1,0}}/Sqrt[2];
p = {{1,1},{1,0}}/2;
c = {{1,Sqrt[2]},{Sqrt[2],-1}}/Sqrt[3];
mask = {{1,1},{1,0}};
checks = {
  Simplify[Transpose[h].h] == IdentityMatrix[2],
  Eigenvalues[b], Eigenvalues[p],
  Simplify[Eigenvalues[c mask]]
};
data = Table[
  {r, Total[Flatten[MatrixPower[p,r]]]/2,
      FullSimplify[Tr[MatrixPower[b,r]]]},
  {r,{2,4,8,12}}
];
base = {{4/5,1/5},{3/10,7/10}};
q = KroneckerProduct[base,base];
markov = Flatten[Table[
  t = MatrixPower[q,n+1];
  g = Table[q[[a,1]] q[[1,1]]^(n-1) q[[1,d]], {a,4},{d,4}];
  pm = Min[Flatten[g/t]];
  bad = t-g;
  Table[
    TrueQ[Tr[MatrixPower[bad,j]]/Tr[MatrixPower[t,j]] <= (1-pm)^j],
    {j,{2,4,8,16}}
  ], {n,{1,2,3,5}}
]];
If[!TrueQ[checks[[1]]] || !And@@markov, Abort[]];
{checks,data,Length[markov],And@@markov}
