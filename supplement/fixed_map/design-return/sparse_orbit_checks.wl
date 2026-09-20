(* Independent symbolic check, executed 18 September 2026. *)
Clear[x,y];
r=(1-(x^7+x^-7)/2)(1+(x+x^-1)/2);
f=(x^7+x^-7)/2+r/10+r(x-x^-1)/(200 I)+
  r((-3-4 I)y+(-3+4 I)/y)/1000-1/10;
ct[z_]:=Coefficient[Coefficient[Expand[z],x,0],y,0];
s={{3,4},{2,3}};
cov[j_]:=With[{a=MatrixPower[s,j]},ct[f (f/.{
  x->x^a[[2,2]] y^a[[1,2]],y->x^a[[2,1]] y^a[[1,1]]})]];
{ct[f^2],cov[1],cov[2],ct[f^2]+2cov[1],
 MatrixPower[s,3]-IdentityMatrix[2],2*7*{{7,10},{5,7}},
 423859315570607>270^6}
(* Returned exactly:
{66033/160000,-7/2000000,0,1650797/4000000,
 {{98,140},{70,98}},{{98,140},{70,98}},True}
*)
