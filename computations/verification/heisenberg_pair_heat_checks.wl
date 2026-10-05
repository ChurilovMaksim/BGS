ClearAll[p, q, x, u, y, n, z, cut, wick, hooks, m, k];
hooks[k_] := Module[{rr},
 rr = Normal[Series[Exp[Sum[(1-y^j) p[j] x^j/j,{j,1,k}]],{x,0,k}]];
 Table[Expand[Cancel[Coefficient[rr,x,j]/(1-y)]],{j,1,k}]
];
wick[expr_,k_] := Fold[Function[{cur,j}, Sum[(-j)^r D[cur,{p[j],r},{q[j],r}]/r!,{r,0,k}]],expr,Range[k]]//Expand;
contractions = Table[Module[{hh, left,right},
 hh=hooks[k]; left=wick[hh[[k]] (hh[[k]]/.p[j_]:>q[j]),k];
 right=hh[[k]] (hh[[k]]/.p[j_]:>q[j])-k y^(k-1)-(1-y)^2 Sum[(k-j)y^(k-j-1)hh[[j]](hh[[j]]/.p[a_]:>q[a]),{j,1,k-1}];
 TrueQ[Expand[left-right]===0]],{k,1,4}];
factor = Together[(1-z)(1-y^2 z)/(1-y z)^2-(1-(1-y)^2 z/(1-y z)^2)]===0;
linear = Table[Together[(k-1)(1-y^k)/2+k y^k-y(1-y^k)/(1-y)-Sum[(1-y^a)(1-y^(k-a)),{a,1,k-1}]/2]===0,{k,1,12}];
contour1 = Together[-m-m(m-1)/n+2(n(m/n)/4+3m(m/n)/4)+n(m/n)(1-m/n)/2-m/n]===0;
contour2 = Together[-m-m(m-1)/n+(m/n)(m-k-1)+2(n(m/n)/4+3k(m/n)/4)+n(m/n)(1-k/n)/2]===0;
<|"ContourUncontractedExponent"->contour1,"ContourContractedExponent"->contour2,"ContractionDegrees1to4"->contractions,"RationalWickFactor"->factor,"LinearCutJoinDegrees1to12"->linear|>
