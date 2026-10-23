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
