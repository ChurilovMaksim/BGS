(* Executed independently in Wolfram. *)
{
 TrigReduce[(1-Cos[7 x])(1+Cos[x]) Sin[x]],
 TrigReduce[Cos[7 x]+(1-Cos[7 x])(1+Cos[x])/10],
 Module[{r=2 ConstantArray[1/3,{3,3}]-IdentityMatrix[3],k},
  k=r^2; {r.r,k,Eigenvalues[k]}]
}
Table[
 Module[{n,f,d,b},
  {n,f}=MatrixPower[{{1,2},{1,1}},k].{1,0};
  d=127 n/(100 10^80);
  b=n/(k (1+n d/3))-1;
  {k,n,n^2-2 f^2,Mod[MatrixPower[{{3,4},{2,3}},k],n],d<1,b>3,N[b,24]}],
 {k,{105,201,203}}]
