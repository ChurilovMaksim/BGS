ClearAll[q,p,r,R,a,aa,bb,cc,dd,h];
r[q_]=(1-Cos[14 Pi q])(1+Cos[2 Pi q]);
R[q_]=(1+Cos[14 Pi q])(1-Cos[2 Pi q]);
a=Cos[14 Pi q]+r[q]/10+r[q] Sin[2 Pi q]/100-1/10+
 R[q](-3 Cos[2 Pi p]+4 Sin[2 Pi p])/500;
Z={D[a,p],-D[a,q]};
Pp={{1,0},{0,-1}}; Pq=-Pp;
fixed={{0,0},{0,1/2},{1/2,0},{1/2,1/2}};
hess=FullSimplify[(125/Pi^2)(D[a,{q,2}]/.Thread[{q,p}->#])&/@fixed];
zstar={1/4,0};
evenPp=FullSimplify[Pp.(Z/.Thread[{q,p}->Pp.zstar])+(Z/.Thread[{q,p}->zstar])];
evenPq=FullSimplify[Pq.(Z/.Thread[{q,p}->Pq.zstar])+(Z/.Thread[{q,p}->zstar])];
S={{3,4},{2,3}}; L={{aa,bb},{cc,dd}}; H={{1,0},{h,1}};
equations=Thread[Flatten[L.S.H-Inverse[S.H].L]==0];
solutions=Solve[Join[Thread[(Coefficient[Subtract@@@equations,h,0])==0],
 Thread[(Coefficient[Subtract@@@equations,h,1])==0],{Det[L]==-1}],
 {aa,bb,cc,dd},Reals];
{hess,evenPp,evenPq,solutions}
