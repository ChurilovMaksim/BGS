#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
int md(int n,int p){n%=p;return n<0?n+p:n;}
void need(bool b,const string&s){if(!b)throw runtime_error(s);}
int main(int argc,char**argv){
 try {
 bool inject=argc>1 && string(argv[1])=="--inject-bad-carry";
 auto started=chrono::steady_clock::now();
 cout << "{\"arithmetic\":\"exact signed integer residues and root-of-unity histograms\",\"runs\":[";
 bool first=true;
 for(int p: {5,11,17}){
  int N=p*p; vector<int>cu(p),iv(p),xx(N),yy(N),phase(N*N);
  for(int t=0;t<p;t++){cu[t]=md(t*t*t,p);iv[cu[t]]=t;}
  auto sorted=cu;sort(sorted.begin(),sorted.end());for(int t=0;t<p;t++)need(sorted[t]==t,"cube bijection");
  for(int j=0;j<N;j++){xx[j]=cu[j%p];yy[j]=cu[j/p];}
  for(int j=0;j<N;j++)for(int k=0;k<N;k++)phase[j*N+k]=md(xx[j]*xx[k]+2*xx[j]*yy[k]+yy[j]*yy[k],p);
  uint64_t carries=0,gram_entries=0,hist_identities=0,classifications=0;int wrong_orientation=0;
  for(int c=1;c<N;c++)for(int j=0;j<N;j++){
   int xp=(j%p+c%p)%p, eps=(j%p+c%p)/p;
   int yp=md(j/p+c/p+(inject?0:eps),p);
   need(xp+p*yp==(j+c)%N,"literal cyclic carry identity");carries++;
  }
  // Orthogonality is exact in Q[zeta_p]: off-diagonal histograms must be constant.
  for(int j=0;j<N;j++)for(int l=0;l<N;l++){
   vector<int>unit(p),square(p),rev(p);
   for(int k=0;k<N;k++){
    unit[md(phase[j*N+k]-phase[l*N+k],p)]++;
    square[md(phase[j*N+k]+phase[k*N+l],p)]++;
    rev[md(phase[j*N+k]-phase[k*N+j]-phase[l*N+k]+phase[k*N+l],p)]++;
   }
   int cx=md(3*xx[j]+2*yy[j],p),cy=md(-2*xx[j]-yy[j],p), row=iv[cx]+p*iv[cy];
   int kx=md(-xx[j]-2*yy[j],p),ky=md(2*xx[j]+3*yy[j],p),wrong=iv[kx]+p*iv[ky];
   if((l==row)!=(l==wrong))wrong_orientation++;
   for(int t=0;t<p;t++){
    need(unit[t]==(j==l?(t==0?N:0):p),"unitarity histogram");
    need(rev[t]==(j==l?(t==0?N:0):p),"reverse orthogonality histogram");
    need(square[t]==(l==row?(t==0?N:0):p),"squared row permutation histogram");
   }
   int tx=xx[j],ty=yy[j];for(int n=0;n<p;n++){int oldx=tx,oldy=ty;tx=md(3*oldx+2*oldy,p);ty=md(-2*oldx-oldy,p);}need(tx==xx[j]&&ty==yy[j],"row map order p");
   gram_entries++;
  }
  int d00=1,d01=0,d10=0,d11=1,period_found=0;
  uint64_t power_cases=0,odd_trace_cases=0,even_trace_cases=0;
  for(int k=0;k<2*p;k++){
   need(d00==md(1+2*k,p)&&d01==md(2*k,p)&&d10==md(-2*k,p)&&d11==md(1-2*k,p),"unipotent power identity");
   int fixed=0;vector<int>actual(p),quadratic(p);
   for(int x=0;x<p;x++)for(int y=0;y<p;y++){
    int nx=md(d00*x+d01*y,p),ny=md(d10*x+d11*y,p);
    if(nx==x&&ny==y)fixed++;
    actual[md(nx*x+2*nx*y+ny*y,p)]++;
   }
   for(int t=0;t<p;t++)quadratic[md((2*k+1)*t*t,p)]+=p;
   need(actual==quadratic,"odd trace exact quadratic histogram");
   need(fixed==(k%p==0?N:p),"even trace fixed-space count");
   if(k>0&&fixed==N&&period_found==0)period_found=k;
   vector<int>normhist(p);for(int x=0;x<p;x++)for(int y=0;y<p;y++)normhist[md((2*k+1)*(x*x-y*y),p)]++;
   bool odddiv=((2*k+1)%p==0);
   for(int t=0;t<p;t++)need(normhist[t]==(odddiv?(t==0?N:0):(t==0?2*p-1:p-1)),"odd Gauss squared modulus histogram");
   int odd_norm2=odddiv?N:p;
   if(2*k+1<2*p)need(odd_norm2<=N,"uniform normalized odd trace bound");
   if(k>0&&2*k<2*p)need(fixed*fixed<=N,"uniform normalized even trace bound");
   if(2*k+1==p)need(odd_norm2==N&&N!=N*N,"H^p is not identity");
   power_cases++;odd_trace_cases++;even_trace_cases++;
   int old00=d00,old01=d01,old10=d10,old11=d11;
   d00=md(3*old00-2*old01,p);d01=md(2*old00-old01,p);
   d10=md(3*old10-2*old11,p);d11=md(2*old10-old11,p);
  }
  need(period_found==p,"unipotent permutation exact period");
  int maxexc=0,maxdiv=0,maxc10=0,maxc1neg=0,maxrestricted=0,special_restricted=-1;
  uint64_t nonempty_branches=0, formal_constant_u=0,formal_constant_v=0;
  for(int c=1;c<N;c++){
   int c0=c%p,c1=c/p; vector<int>be(N*N);
   if(p<=11)for(int j=0;j<N;j++)for(int k=0;k<N;k++)be[j*N+k]=md(phase[j*N+k]-phase[((j+c)%N)*N+(k+c)%N],p);
   for(int j=0;j<N;j++){
    int exceptions=0, restricted_exceptions=0;
    for(int l=0;l<N;l++){
     int ap=md(xx[j]-xx[l],p),aq=md(2*xx[j]+yy[j]-2*xx[l]-yy[l],p);
     int bp=md(xx[(j+c)%N]-xx[(l+c)%N],p);
     int bq=md(2*xx[(j+c)%N]+yy[(j+c)%N]-2*xx[(l+c)%N]-yy[(l+c)%N],p);
     bool exceptional=false,restricted=false;vector<int>factor_hist(p);
     for(int e=0;e<2;e++){
      int lo=e?p-c0:0,hi=e?p:p-c0;if(lo==hi)continue;
      int d=md(c1+e,p);vector<int>uv(p),vv(p),hu(p),hv(p);
      for(int t=0;t<p;t++){uv[t]=md(ap*cu[t]-bp*cu[(t+c0)%p],p);vv[t]=md(aq*cu[t]-bq*cu[(t+d)%p],p);}
      bool uc=all_of(uv.begin(),uv.end(),[&](int v){return v==uv[0];});
      bool vc=all_of(vv.begin(),vv.end(),[&](int v){return v==vv[0];});
      bool ur=all_of(uv.begin()+lo,uv.begin()+hi,[&](int v){return v==uv[lo];});
      need(uc==(c0==0?ap==bp:(ap==0&&bp==0)),"u polynomial constant criterion");
      need(vc==(d==0?aq==bq:(aq==0&&bq==0)),"v polynomial constant criterion");
      exceptional|=uc&&vc;restricted|=ur&&vc;
      formal_constant_u+=uc;formal_constant_v+=vc;nonempty_branches++;
      if(p<=11){
       for(int u=lo;u<hi;u++)hu[uv[u]]++;
       for(int v=0;v<p;v++)hv[vv[v]]++;
       for(int a=0;a<p;a++)for(int b=0;b<p;b++)factor_hist[(a+b)%p]+=hu[a]*hv[b];
      }
     }
     exceptions+=exceptional;restricted_exceptions+=restricted;classifications++;
     if(exceptional){
      if(c0)need(j%p==l%p,"nonzero low digit necessary exceptional condition");
      else need(md(2*xx[j]+yy[j]-2*xx[l]-yy[l],p)==0,"p-divisible necessary exceptional condition");
     }
     if(p<=11){vector<int>direct_hist(p);for(int k=0;k<N;k++)direct_hist[md(be[j*N+k]-be[l*N+k],p)]++;need(direct_hist==factor_hist,"independent Gram histogram factorization");hist_identities++;}
    }
    need(exceptions<=p,"exception count");maxexc=max(maxexc,exceptions);maxrestricted=max(maxrestricted,restricted_exceptions);
    if(c0==0)maxdiv=max(maxdiv,exceptions);
    if(c1==0)maxc10=max(maxc10,exceptions);
    if(c1==p-1)maxc1neg=max(maxc1neg,exceptions);
    if(p==5&&c==21&&j==4)special_restricted=restricted_exceptions;
   }
  }
  if(!first)cout<<",";
  first=false;
  cout<<"{\"p\":"<<p<<",\"N\":"<<N<<",\"unipotent_power_cases\":"<<power_cases<<",\"odd_trace_cases\":"<<odd_trace_cases<<",\"even_trace_cases\":"<<even_trace_cases<<",\"carry_cases\":"<<carries<<",\"gram_entries_each_kind\":"<<gram_entries<<",\"classification_triples\":"<<classifications<<",\"branch_cases\":"<<nonempty_branches<<",\"exact_gram_factorizations\":"<<hist_identities<<",\"max_formal_exceptional\":"<<maxexc<<",\"max_p_divisible_exceptional\":"<<maxdiv<<",\"max_c1_zero_exceptional\":"<<maxc10<<",\"max_c1_minus_one_exceptional\":"<<maxc1neg<<",\"max_restricted_constant_partners\":"<<maxrestricted<<",\"p5_c21_j4_restricted_constant_partners\":"<<special_restricted<<",\"wrong_row_ket_orientation_disagreements\":"<<wrong_orientation<<"}";
 }
 cout<<"],\"status\":\"passed\",\"runtime_seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-started).count()<<"}\n";
 } catch (const exception& e) { cerr << e.what() << endl; return 2; }
}
