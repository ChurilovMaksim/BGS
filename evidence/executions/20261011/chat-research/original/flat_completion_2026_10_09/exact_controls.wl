(* Exact finite controls; not a proof certificate for all dimensions. *)
ClearAll["Global`*"];
ad[x_] := ConjugateTranspose[x];
id = IdentityMatrix[2];
left = {{3/5, -4/5}, {4/5, 3/5}};
right = {{1, 0}, {0, I}};
values = DiagonalMatrix[{3/5, 4/5}];
defects = DiagonalMatrix[{4/5, 3/5}];
g = left.values.ad[right];
gamma = left.defects.ad[left];
delta = right.defects.ad[right];
julia = ArrayFlatten[{{g, -gamma}, {delta, ad[g]}}];
juliaTests = {ad[julia].julia == IdentityMatrix[4],
  julia.ad[julia] == IdentityMatrix[4], g.delta == gamma.g,
  g.ad[g] != ad[g].g};
a = {{1/8, I/16}, {1/32, 1/8}};
b = {{1/16, 1/32}, {I/64, 1/16}};
center = 1/4 + I/8;
f[x_] := (x - center id).Inverse[id - Conjugate[center] x];
fa = f[a]; fb = f[b];
mobiusRight = (1 - Abs[center]^2) Inverse[id - Conjugate[center] b].
  (id - b.ad[a]).Inverse[id - center ad[a]];
ratio[x_, y_] := Abs[Det[id - y.ad[x]]]^2/
  (Det[id - x.ad[x]] Det[id - y.ad[y]]);
mobiusTests = {id - fb.ad[fa] == mobiusRight,
  ratio[fa, fb] == ratio[a, b]};
(* The normalization failure from Zirnbauer 2109.10272v1, Eq. (4.21). *)
bulkPrimitive = t/(1 + t)^2;
badMomentPrimitive = Log[1 + t] + 3/(1 + t) - 1/(1 + t)^2 - 2;
primitiveTests = {Together[D[bulkPrimitive, t] - (1 - t)/(1 + t)^3] == 0,
  Together[D[badMomentPrimitive, t] - (t^2 - t)/(1 + t)^3] == 0,
  (bulkPrimitive /. t -> 0) == 0, (badMomentPrimitive /. t -> 0) == 0};
bulkNormalization = Normal[Series[bulkPrimitive /. t -> 1/eps, {eps, 0, 0}]] /. eps -> 0;
normalizationCheck = bulkNormalization == 0;
badMomentCutoff = badMomentPrimitive /. t -> cutoff;
badMomentRemainder = Together[badMomentCutoff - Log[1 + cutoff]];
badMomentRemainderLimit = Normal[Series[badMomentRemainder /. cutoff -> 1/eps,
  {eps, 0, 0}]] /. eps -> 0;
(* Log[1+cutoff] is unbounded, while the rational remainder tends to -2. *)
badMomentCheck = badMomentRemainderLimit == -2;
boundaryTests = Table[Module[{u, vars, aa, bb, body, mixed},
  u = If[n == 2, left, 2 ConstantArray[1/n, {n, n}] - IdentityMatrix[n]];
  vars = Table[Symbol["r" <> ToString[j]], {j, n}];
  aa = DiagonalMatrix[vars]; bb = u.aa.Transpose[u];
  body = Det[IdentityMatrix[n] - aa.aa]/
    Det[IdentityMatrix[n] - zeta bb.aa];
  mixed = Together[D[body, Sequence @@ ({#, 1} & /@ vars)]] /. Thread[vars -> 1];
  Together[mixed - (-2)^n/(1 - zeta)^n] == 0], {n, {2, 3}}];
result = <|"JuliaChecks" -> juliaTests, "MobiusChecks" -> mobiusTests,
 "UncorrectedBulkNormalization" -> bulkNormalization,
 "NormalizationFailureVerified" -> normalizationCheck,
 "WrongFermionicMomentDiverges" -> badMomentCheck,
 "BoundaryJetChecksN2N3" -> boundaryTests,
 "PrimitiveChecks" -> primitiveTests,
 "AllChecksPassed" -> And @@ Join[juliaTests, mobiusTests, primitiveTests,
   {normalizationCheck, badMomentCheck}, boundaryTests],
 "Scope" -> "Exact finite controls and two source diagnostics; no full BGS proof"|>;
ExportString[result, "RawJSON"]
