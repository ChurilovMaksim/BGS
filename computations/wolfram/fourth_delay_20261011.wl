(* Exact finite check on one noncommuting 3-by-3 Gaussian-rational fixture.
   Circle means are residues at 0 and Conjugate[a]; no quadrature.
   The asymptotic fourth-delay theorem is not certified by this computation. *)
ClearAll[w];
skew = {{0,1/3,-1/4},{-1/3,0,1/5},{1/4,-1/5,0}};
s = DiagonalMatrix[{1,I,-1}] . Inverse[IdentityMatrix[3]-skew] .
    (IdentityMatrix[3]+skew);
x = {{1,I,2},{-I,2,1},{2,1,-1}};
tmat = IdentityMatrix[3] + ConjugateTranspose[x] . x;
a = s[[1,1]]; d = 1-Abs[a]^2;
q = w/(1-a w); qb = 1/(w-Conjugate[a]);
k = {{q s[[1,2]],q s[[1,3]]},{1,0},{0,1}};
kh = {{qb Conjugate[s[[1,2]]],1,0},
      {qb Conjugate[s[[1,3]]],0,1}};
tp = kh . tmat . k;
sp = s[[2;;3,2;;3]] + q Outer[Times,s[[2;;3,1]],s[[1,2;;3]]];
mean[z_] := Module[{v=Together[z/w]},
  Simplify[Residue[v,{w,0}]+Residue[v,{w,Conjugate[a]}]]];
qmat = s . tmat . ConjugateTranspose[s];
gamma = s . tmat; beta = s . MatrixPower[tmat,2];
t = tmat[[1,1]]; ss = qmat[[1,1]]; g = gamma[[1,1]];
t2 = MatrixPower[tmat,2]; t3 = MatrixPower[tmat,3];
q2 = MatrixPower[qmat,2]; q3 = MatrixPower[qmat,3];
quartic = Tr[MatrixPower[tmat,4]] +
  4(t q3[[1,1]]+t2[[1,1]]q2[[1,1]]+ss t3[[1,1]])/d +
  8 Re[Conjugate[a](g(ss t2[[1,1]]+t q2[[1,1]])+t ss beta[[1,1]])]/d^2 +
  (1+Abs[a]^2)(2 t^2 ss^2+4 t ss Abs[g]^2)/d^3 +
  8 t ss Re[Conjugate[a]^2 g^2]/d^3;
(* An independent two-dimensional Cayley-Hamilton representation of Tr tp^4. *)
trace4 = Tr[tp]^4-4 Det[tp] Tr[tp]^2+2 Det[tp]^2;
checks = {
  Simplify[s . ConjugateTranspose[s] == IdentityMatrix[3] && 0<Abs[a]^2<1],
  Simplify[Map[mean,sp . tp,{2}] == gamma[[2;;3,2;;3]]],
  And@@Table[mean[(tp . tp)[[j-1,j-1]]] ==
    t2[[j,j]]+(Abs[s[[1,j]]]^2 t2[[1,1]]+
    2 t Re[Conjugate[s[[1,j]]]gamma[[1,j]]])/d+
    2 Abs[s[[1,j]]]^2 t Re[Conjugate[a]g]/d^2,{j,2,3}],
  mean[trace4] == quartic
};
{a, Simplify[checks]}
