(* Exact symbolic cross-checks over Q(t,s,k,l), not finite-N experiments.
   Stateless Wolfram Language evaluator; no external packages. *)
Clear[t, s, k, l, z, pp];
a[tt_, kk_, ll_] := tt ll^2/2 + tt^2 kk ll/2 + tt^3 kk^2/6;
h = {{t^3/3, t^2/2}, {t^2/2, t}};
y = {{1, t}, {0, 1}};
g = Together[Inverse[h]];
c = Together[g.y];
skew = Together[c - Transpose[c]];
cocycle = Expand[a[t, k, l] + a[s, k, l + t k] - a[t + s, k, l]];
diagAction = Factor[-{t z, 0}.g.{t z, 0}/2];
returnJ = Factor[1 - 1/(1/(1-z))];
returnOrthogonal = Factor[1 - 1/(1/(1-z^pp))];
<|"kernel_version" -> $Version, "cocycle" -> cocycle,
  "hessian_determinant" -> Factor[Det[h]], "inverse" -> g,
  "mixed_coefficient" -> c, "alternating_determinant" -> Factor[Det[skew]],
  "diagonal_action" -> diagAction,
  "return_on_constants" -> returnJ,
  "return_on_orthogonal_complement" -> returnOrthogonal|>
