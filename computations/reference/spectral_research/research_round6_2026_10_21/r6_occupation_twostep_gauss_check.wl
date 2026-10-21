ClearAll[rts, rt, qf, maxabs, checkOne];
rts[q_Integer] := rts[q] = N[Exp[2 Pi I Range[0, q - 1]/q], 90];
rt[q_Integer, e_Integer] := rts[q][[Mod[e, q] + 1]];
qf[x_, y_] := 17 x^2 - 2 x y + 17 y^2;
maxabs[x_] := Max[Abs[Flatten[{x}]]];
checkOne[dim_Integer] := Module[
 {iv8, iv4, hf, mat, sq, ker, ki, ga, sg, rho, gg, errors,
  direct, ll, nu8, nu16, nu48, gam, ss, ys, co, pred, ce, pe, support},
 iv8 = PowerMod[8, -1, dim]; iv4 = PowerMod[4, -1, dim];
 hf = PowerMod[2, -1, dim]; gg = GCD[dim, 24];
 mat = Table[rt[dim, -iv8 (3 x^2 - 2 x y + 3 y^2)]/Sqrt[dim],
             {x, 0, dim - 1}, {y, 0, dim - 1}];
 sq = mat.mat;
 ki[x_Integer, y_Integer] := Total[Table[
  rt[48 dim, -qf[x, y + m dim]], {m, 0, 23}]]/Sqrt[24 dim];
 ker = Table[ki[x, y], {x, 0, dim - 1}, {y, 0, dim - 1}];
 ga = Total[Table[rt[dim, -3 iv4 z^2], {z, 0, dim - 1}]];
 sg = Total[Table[rt[48, -17 dim m^2], {m, 0, 23}]];
 rho = Sqrt[dim/24] sg/ga;
 If[Mod[dim, 3] != 0,
  nu48 = Mod[-PowerMod[dim, -1, 48], 48]; gam = ga/Sqrt[dim];
  direct[x_Integer, y_Integer] :=
   gam rt[48 dim, -qf[x, y]] rt[48, -nu48 qf[x, y]]/Sqrt[dim],
  ll = dim/3; nu8 = Mod[-PowerMod[dim, -1, 8], 8];
  nu16 = Mod[-PowerMod[ll, -1, 16], 16];
  gam = If[ll == 1, 1,
    Total[Table[rt[ll, -PowerMod[4, -1, ll] z^2], {z, 0, ll - 1}]]/Sqrt[ll]];
  direct[x_Integer, y_Integer] := If[Mod[x + y, 3] != 0, 0,
   Sqrt[3/dim] gam rt[48 dim, -qf[x, y]]
     rt[16, -6 nu8 (x^2 + y^2) + nu16 ((x + y)/3)^2]]
 ];
 support = Table[If[Mod[x - 17 y, gg] == 0, gg/dim, 0],
                 {x, 0, dim - 1}, {y, 0, dim - 1}];
 errors = <|
 "rho_unit" -> Abs[Abs[rho] - 1],
 "gauss_norm" -> Abs[Abs[ga]^2 - dim gg],
 "image_gauss_norm" -> Abs[Abs[sg]^2 - 24 gg],
 "matrix_identification" -> Sqrt[dim] maxabs[ker - rho sq],
 "support_modulus" -> maxabs[Abs[ker]^2 - support],
 "row_norm" -> maxabs[(Total[Abs[#]^2] - 1 &) /@ ker],
 "direct_gauss" -> Sqrt[dim] maxabs[sq -
   Table[direct[x, y], {x, 0, dim - 1}, {y, 0, dim - 1}]],
 "weyl_shift" -> maxabs[Table[
  ker[[x + 1, Mod[y - 1, dim] + 1]] -
   rt[dim, 12 (x + hf 17)] ker[[Mod[x + 17, dim] + 1, y + 1]],
  {x, 0, dim - 1}, {y, 0, dim - 1}]],
 "weyl_modulation" -> maxabs[Table[
  rt[dim, y] ker[[x + 1, y + 1]] -
   rt[dim, 17 (x + hf 24)] ker[[Mod[x + 24, dim] + 1, y + 1]],
  {x, 0, dim - 1}, {y, 0, dim - 1}]],
 "period_x" -> maxabs[(ki[#[[1]] + dim, #[[2]]] - ki @@ # &) /@
                    {{-2, -1}, {0, 0}, {1, dim - 1}, {dim + 2, 2 dim + 1}}],
 "period_y" -> maxabs[(ki[#[[1]], #[[2]] + dim] - ki @@ # &) /@
                    {{-2, -1}, {0, 0}, {1, dim - 1}, {dim + 2, 2 dim + 1}}]
 |>;
 ys = DeleteDuplicates[{0, 1, Quotient[dim, 2], dim - 1}]; ce = 0; pe = 0;
 Do[
  ss = Table[Sqrt[dim] sq[[Mod[x, dim] + 1, y + 1]] rt[48 dim, qf[x, y]],
             {x, 0, 23}];
  Do[
   co = Total[Table[ss[[x + 1]] rt[24, -m x], {x, 0, 23}]]/24;
   pred = rt[48, -34 m y - 17 dim m^2]/(Sqrt[24] rho);
   ce = Max[ce, Abs[Abs[co] - 1/Sqrt[24]]]; pe = Max[pe, Abs[co - pred]],
   {m, 0, 23}], {y, ys}];
 errors["coefficient_modulus"] = ce; errors["coefficient_phase"] = pe;
 <|"N" -> dim, "gcd_N_24" -> gg, "matrix_entries" -> dim^2,
 "DFT_coefficients" -> 24 Length[ys],
 "passed" -> TrueQ[Max[Values[errors]] < 10^-65],
 "maximum_error" -> ToString[InputForm[N[Max[Values[errors]], 10]]],
 "errors" -> Map[ToString[InputForm[N[#, 10]]] &, errors]|>
];
results = checkOne /@ {3,5,7,9,11,15,21,25,27,33,45};
ExportString[<|"precision"->90,"all_passed"->And@@Lookup[results,"passed"],
 "total_matrix_entries"->Total[Lookup[results,"matrix_entries"]],
 "total_DFT_coefficients"->Total[Lookup[results,"DFT_coefficients"]],
 "results"->results|>,"JSON"]
