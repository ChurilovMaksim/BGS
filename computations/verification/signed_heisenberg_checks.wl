Clear[mm, nn, dm, dn, ds, pp, qq, hh, aa, bb];
z = -1/2 + I Sqrt[3]/2;
t = {3, z, Sqrt[2] z, Sqrt[3]};
moment = Table[If[j >= k, t[[j-k+1]], Conjugate[t[[k-j+1]]]], {j,0,3}, {k,0,3}];
out = <|"CubicDiscrepancy" -> ToString[Expand[pp-(mm+dm)-(nn+dn)-(mm+nn+ds)+2 n0-(2 n0-2(mm+nn))],InputForm], "QuadraticTracePhase" -> ToString[Expand[mm^2+nn^2-(mm+nn)^2],InputForm], "ConeConstant" -> ToString[((bb-aa)^2 aa Sqrt[2 aa])/.{aa->1/8,bb->1/4},InputForm], "TwoBlockCoefficientChecks" -> Table[Sum[Binomial[qq-1,hh-1] Factorial[hh-1] Factorial[qq-hh],{hh,1,qq}]==Factorial[qq],{qq,1,10}], "ToeplitzDeterminantN3" -> ToString[FullSimplify[Det[moment]],InputForm]|>;
ExportString[out,"RawJSON"]
