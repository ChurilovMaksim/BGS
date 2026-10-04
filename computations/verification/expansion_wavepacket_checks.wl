(* Exact algebra controls only, not uniform gaps or analytic trace proofs. *)
r = {{4, 9}, {19, 43}};
s = {{3, 2}, {1, 1}};
v = {{-5, 19}, {-24, 91}};
b = (r + 8 IdentityMatrix[2])/21;
lucas = LinearRecurrence[{3, -1}, {2, 3}, 10];
rank[k_] := Cancel[(2 ((p+1)/2)^(2 k)+(p-3) p (p+1)/2+
 (p^2-1) 2^(1-2 k) Sum[Binomial[2 k,2 l] p^l,{l,0,k}])/(p (p^2-1))];
checks = <|
 "matrixProduct" -> (v.s == r),
 "rationalFourthRoot" -> (MatrixPower[b,4] == r),
 "determinants" -> (Map[Det,{r,s,v}] == {1,1,1}),
 "resultant" -> Resultant[z^2-2 z-2,19 z^2+39 z-9,z],
 "commutatorTrace" -> Tr[s.v.Inverse[s].Inverse[v]],
 "normIdentity" -> (Expand[(10 x+75 t)^2-5 (21 t)^2-
   20 (5 x^2+75 x t+171 t^2)] == 0),
 "mod3" -> Mod[Take[lucas,4],3],
 "mod7" -> Mod[Take[lucas,8],7],
 "rank1" -> rank[1],
 "rank2Identity" -> (Cancel[rank[2]-(p+7)/4] == 0),
 "rank3Identity" -> (Cancel[rank[3]-(p+3)(p^2+4 p+19)/32] == 0)
|>;
ExportString[checks, "RawJSON"]
