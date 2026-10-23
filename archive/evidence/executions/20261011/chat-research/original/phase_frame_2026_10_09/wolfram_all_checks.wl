jacobianJSON=(
records=Table[
 n=m^2; e=n-m; ell=ConstantArray[0,{e,m}]; row=1;
 Do[ell[[row,a]]=1;ell[[row,b]]=1;row++;
    ell[[row,a]]=1;ell[[row,b]]=I;row++,{a,1,m},{b,a+1,m}];
 k=Join[ell,IdentityMatrix[m]]; t=ConjugateTranspose[k].k;
 u=2 k.Inverse[t].ConjugateTranspose[k]-IdentityMatrix[n];
 If[e==0,s=u;ll=ell,
  inv=Inverse[IdentityMatrix[e]-u[[1;;e,1;;e]]];
  ll=inv.u[[1;;e,e+1;;n]];
  s=u[[e+1;;n,e+1;;n]]+u[[e+1;;n,1;;e]].ll];
 hh=Table[
  du=ConstantArray[0,{n,n}];du[[phase]]=I u[[phase]];
  If[e==0,ds=du,
   dl=inv.(du[[1;;e,e+1;;n]]+du[[1;;e,1;;e]].ll);
   ds=du[[e+1;;n,e+1;;n]]+du[[e+1;;n,1;;e]].ll+
       u[[e+1;;n,1;;e]].dl];
  Simplify[-I ConjugateTranspose[s].ds],{phase,1,n}];
 coords[h_]:=Join[Re[Diagonal[h]],
  Flatten[Table[{Re[h[[a,b]]],Im[h[[a,b]]]},{a,1,m},{b,a+1,m}]]];
 selected=Join[Range[e+1,n],Range[1,e]];
 jac=Transpose[coords/@hh[[selected]]];
 proj=k.Inverse[t].ConjugateTranspose[k];
 energy=Sum[Abs[proj[[a,b]]]^4/(proj[[a,a]]proj[[b,b]]),
            {a,1,n},{b,1,n}];
 <|"m"->m,"N"->n,
   "unitarity"->(Simplify[ConjugateTranspose[u].u]==IdentityMatrix[n]),
   "recoveredL"->(ll==ell),"cavityIdentity"->(s==IdentityMatrix[m]),
   "phaseDerivatives"->And@@Table[hh[[a]]==Outer[Times,Conjugate[k[[a]]],k[[a]]],{a,1,n}],
   "JacobianDeterminant"->Det[jac],
   "projectionCheck"->(Simplify[proj.proj]==proj),
   "frameEnergyExact"->ToString[energy,InputForm],"WelchBoundCheck"->(energy>=2m/(m+1))|>,
 {m,1,4}];
ExportString[records,"RawJSON"]

);
finiteBoundsJSON=(
(* Exact symbolic identities behind both finite-N inequalities.
   No claim of formal proof of Haar conditional distributions. *)
Clear[m,n];
cc=m^2(m-1)/(m+2); cr=m(m^2-1)/(m+4);
bc=m(m-1)/(n+1); br=m(m-1)/(n+2);
maxc=2m(m-1)/((m+2)(n+1));
minc=maxc(n-m)/(n+2);
maxr=3m(m-1)/((m+4)(n+2));
minr=maxr(n-m)/(n+4);
checks=<|
 "complexLower"->Together[bc-maxc-cc/(n+1)],
 "complexUpper"->Together[bc-minc-cc/(n+1)-2m(m-1)/((n+1)(n+2))],
 "realLower"->Together[br-maxr-cr/(n+2)],
 "realUpper"->Together[br-minr-cr/(n+2)-3m(m-1)/((n+2)(n+4))],
 "complexInfluence"->Together[
  m(m+1)(m^4+2(m-1)m^2+m(m-2))/((m+1)^2(m+2)^2)-cc],
 "realInfluence"->Together[
  m(m+2)(m^2(m+1)^2+4(m-1)(m+1)^2+2(m+1)(m-2))/((m+2)^2(m+4)^2)-cr]
|>;
ExportString[<|"checks"->checks,"allZero"->And@@(#==0&/@Values[checks])|>,"RawJSON"]

);
ExportString[<|"jacobian"->ImportString[jacobianJSON,"RawJSON"],"finiteBounds"->ImportString[finiteBoundsJSON,"RawJSON"]|>,"RawJSON"]
