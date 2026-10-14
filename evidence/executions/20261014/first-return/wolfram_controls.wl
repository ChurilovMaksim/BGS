Module[{w,h,k,n=4,p=5,jn,jp,pin,pip,m,projector,traces,expected},
 w={{1,1,1,1},{1,-1,-1,1},{1,1,-1,-1},{1,-1,1,-1}};
 h=w/2;k=MatrixPower[h,2];
 jn=ConstantArray[1/n,{n,n}];jp=ConstantArray[1/p,{p,p}];
 pin=IdentityMatrix[n]-jn;pip=IdentityMatrix[p]-jp;
 m=KroneckerProduct[MatrixPower[k,p]-jn,pip];
 projector=KroneckerProduct[pin,pip];
 traces=Table[Tr[MatrixPower[m,q]],{q,1,9}];
 expected=Table[If[Mod[q,3]==0,(n-1)(p-1),0],{q,1,9}];
 <|"arithmetic"->"exact integers and rationals",
   "n"->n,"p"->p,"ambientDiagonalDimension"->n p,
   "centeredDiagonalDimension"->n p-1,
   "pulseRank"->Tr[projector],
   "coreSixPeriod"->(MatrixPower[h,6]==IdentityMatrix[4]),
   "coreCycleTraces"->{Tr[k],Tr[MatrixPower[k,2]],Tr[MatrixPower[k,3]]},
   "powersOneThroughNineTraces"->traces,
   "expectedTraces"->expected,
   "traceReplayPass"->(traces==expected),
   "cubeIsProjection"->(MatrixPower[m,3]==projector),
   "gramIsProjection"->(m.Transpose[m]==projector),
   "scope"->"Finite n=4,p=5 memory-operator replay only; no asymptotic, perturbation, BGS or formal certification"|>
]
