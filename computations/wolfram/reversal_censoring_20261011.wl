h={{1,1+I,0},{1-I,0,1},{0,1,-1}};
s=Simplify[(IdentityMatrix[3]+I h).Inverse[IdentityMatrix[3]-I h]];
rev[m_]:=Table[m[[i,j]] Conjugate[m[[j,i]]],{i,Length[m]},{j,Length[m]}];
r=Simplify[rev[s]]; a=s[[3,3]]; aa=s[[1;;2,1;;2]];
c=s[[1;;2,3]]; b=s[[3,1;;2]]; d=1-Abs[a]^2;
ass=Element[{y,x1,x2,x3,x4,t2},Reals];
w=(1+I y)/(1-I y); q=w/(1-a w);
sp=aa+q Outer[Times,c,b];
cc=DiagonalMatrix[c].Transpose[Conjugate[aa]].DiagonalMatrix[b];
v=c Conjugate[b]; vv=Outer[Times,v,Conjugate[v]];
noiseFormula=FullSimplify[rev[sp]-r[[1;;2,1;;2]]-q cc-Conjugate[q] ConjugateTranspose[cc]-q Conjugate[q] vv,ass];
x={x1+I x2,x3+I x4}; t=(r[[3,1;;2]].x)/(1-r[[3,3]]);
z=Join[x,{t}]; rc=r[[1;;2,1;;2]]+Outer[Times,r[[1;;2,3]],r[[3,1;;2]]]/(1-r[[3,3]]);
norm2[vv_]:=Conjugate[vv].vv;
energy=FullSimplify[norm2[r.z]-t2 norm2[z]-norm2[rc.x]+t2 norm2[x]-(1-t2)Abs[t]^2,ass];
<|"Unitary"->(Simplify[s.ConjugateTranspose[s]]===IdentityMatrix[3]),
"HermitianReversal"->(r===ConjugateTranspose[r]),
"ExactPhaseExpansion"->(noiseFormula===ConstantArray[0,{2,2}]),
"GeneralComplexLift"->(energy===0)|>
