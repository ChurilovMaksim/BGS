Module[{n, b, t, u, v, k, l, root, dim, coe, cse, mean, variance,
  expected, rows, gapControls, fourthControls, mass, checks},
 dim[w_List] := Product[(w[[k]] - w[[l]] + l - k)/(l-k),
   {k,1,Length[w]-1},{l,k+1,Length[w]}];
 rows = Table[
   root = Join[{1},ConstantArray[0,n-2],{-1}];
   coe = dim[2 root]; cse = dim[Flatten[Transpose[{root,root}]]];
   {n,coe,cse,coe == n^2(n-1)(n+3)/4,
    cse == n^2(2n-3)(2n+1)}, {n,2,8}];
 gapControls = Table[
   mean = Integrate[(2+2 Cos[t]) Sin[t/2]^b,{t,0,2 Pi}]/
      Integrate[Sin[t/2]^b,{t,0,2 Pi}];
   variance = Integrate[(2+2 Cos[t]-mean)^2 Sin[t/2]^b,
      {t,0,2 Pi}]/Integrate[Sin[t/2]^b,{t,0,2 Pi}];
   {b,mean,variance,mean==4/(b+2),
      variance==32(b+1)/((b+2)^2(b+4))}, {b,{1,2,4}}];
 fourthControls = Table[
   mean = Integrate[(2+2 Cos[n t]) (6-8 Cos[t]+2 Cos[2 t]),
       {t,0,2 Pi}]/(12 Pi);
   variance = Integrate[(2+2 Cos[n t])^2 (6-8 Cos[t]+2 Cos[2 t]),
       {t,0,2 Pi}]/(12 Pi);
   {n,mean,variance}, {n,1,6}];
 mass = Sum[Coefficient[Coefficient[Normal[Series[
       (Exp[u+v]-1)^n,{u,0,2},{v,0,2}]],u,2],v,2]/(2 n),{n,1,4}];
 checks = {And@@Flatten[rows[[All,{4,5}]]],
   And@@Flatten[gapControls[[All,{4,5}]]],mass==13/4,
   fourthControls=={{1,2/3,1},{2,7/3,22/3},{3,2,6},{4,2,6},{5,2,6},{6,2,6}}};
 ExportString[<|"all_passed"->And@@checks,"checks"->checks,
   "dimension_controls"->rows,"N2_gap_controls"->gapControls,
   "N2_CSE_trace_controls"->fourthControls,"coefficient_mass"->ToString[mass,InputForm]|>,
 "RawJSON"]
]

