ClearAll[z, q, p, aa, xx, yy, th];
sc = {{3, 4}, {2, 3}};
bb = sc - IdentityMatrix[2];
rr = Inverse[bb].sc;
jj = {{0, 1}, {-1, 0}};
yyv = rr.jj.{D[aa[q,p],p],0};
grad = {D[aa[q,p],q],D[aa[q,p],p]};
vec = rr.jj.grad;
divCheck = FullSimplify[D[vec[[1]],q]+D[vec[[2]],p]+D[aa[q,p],{q,2}]-D[aa[q,p],{p,2}]/2];
rpol = 1+(z+z^-1)/2-(z^7+z^-7)/2-(z^8+z^-8+z^6+z^-6)/4;
vpol = Expand[(z^7+z^-7)/2+rpol/10+rpol*(z-z^-1)/(200 I)-1/10];
cf[k_] := Coefficient[Expand[z^9 vpol],z,k+9];
coeffs = Table[{k,cf[k]}, {k,{2,6,8}}];
modePi2 = Table[{m,-16 m^2 cf[-2 m]}, {m,{1,3,4}}];
normSquared = FullSimplify[Abs[#[[2]]]^2]& /@ modePi2;
phaseCheck = FullSimplify[TrigExpand[Total[((1+Cos[xx+#]) (1+Cos[xx+yy+#]))& /@ {0,Pi/2,Pi,3Pi/2}]/4-(1+Cos[yy]/2)]];
{Det[bb],rr,divCheck,coeffs,modePi2,normSquared,phaseCheck}
