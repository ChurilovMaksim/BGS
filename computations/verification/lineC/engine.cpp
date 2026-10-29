// Exact (n, rank r, square class D) histogram over all words y (distinct rearrangements of the
// block-label word x of a set partition rho) of the quadratic form
//   z^T B z,  B = adj-multigraph(x-walk) - adj-multigraph(y-walk)  (cyclic walks of length m).
// rank via elimination mod P=2^61-1 (exact: all minors < P by Hadamard, asserted);
// D = exact integer pivot product = det of principal minor of the unimodularly transformed B.
// Input (stdin): lines "idx m n l_0 ... l_{m-1}".  Output: "idx r D count" (count = #words).
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <unordered_map>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;
typedef unsigned long long u64; typedef __int128 i128; typedef long long ll;
static const u64 P = (1ULL<<61)-1;
static inline u64 mulm(u64 a, u64 b){ __uint128_t c=(__uint128_t)a*b; u64 lo=(u64)(c&P), hi=(u64)(c>>61); u64 s=lo+hi; if(s>=P) s-=P; return s; }
static inline u64 addm(u64 a,u64 b){ u64 s=a+b; if(s>=P) s-=P; return s;}
static inline u64 subm(u64 a,u64 b){ return a>=b? a-b : a+P-b;}
static inline u64 tom(ll x){ ll r = x % (ll)P; if(r<0) r+=P; return (u64)r; }
u64 powm(u64 a,u64 e){u64 r=1;while(e){if(e&1)r=mulm(r,a);a=mulm(a,a);e>>=1;}return r;}
u64 invm(u64 a){return powm(a,P-2);}
ll sqfree(ll D){ // signed squarefree part
  static unordered_map<ll,ll> cache; auto it=cache.find(D); if(it!=cache.end()) return it->second;
  ll s = D<0?-1:1; ll x = D<0?-D:D; ll out=1;
  for(ll d=2; d*d<=x; d++){ while(x%(d*d)==0) x/=d*d; if(x%d==0){out*=d; x/=d;} }
  ll res = s*out*x; cache[D]=res; return res;
}
i128 bareiss_det(vector<vector<ll>> A){
  int n=A.size(); if(n==0) return 1; vector<vector<i128>> M(n, vector<i128>(n));
  for(int i=0;i<n;i++)for(int j=0;j<n;j++) M[i][j]=A[i][j];
  i128 prev=1; int sign=1;
  for(int k=0;k<n-1;k++){
    if(M[k][k]==0){ int sw=-1; for(int i=k+1;i<n;i++) if(M[i][k]!=0){sw=i;break;} if(sw<0) return 0; swap(M[k],M[sw]); sign=-sign; }
    for(int i=k+1;i<n;i++) for(int j=k+1;j<n;j++){ M[i][j]=(M[i][j]*M[k][k]-M[i][k]*M[k][j])/prev; }
    prev=M[k][k];
  }
  return sign*M[n-1][n-1];
}
int main(int argc,char**argv){
  int SH = argc>2? atoi(argv[1]):0, NS = argc>2? atoi(argv[2]):1;
  ios::sync_with_stdio(false);
  vector<pair<int,vector<int>>> jobs; int idx,m,n;
  vector<int> ns;
  while(cin>>idx>>m>>n){ vector<int> l(m); for(auto&v:l) cin>>v; jobs.push_back({idx,l}); ns.push_back(n);}
  int J=jobs.size();
  vector<map<pair<int,ll>,ll>> res(J);
  #pragma omp parallel for schedule(dynamic,1)
  for(int t=0;t<J;t++){
    if(t%NS!=SH) continue;
    const vector<int>& L=jobs[t].second; int m=L.size(), n=ns[t];
    vector<ll> Bx(n*n,0);
    for(int j=0;j<m;j++){int a=L[j],b=L[(j+1)%m]; Bx[a*n+b]++; Bx[b*n+a]++;}
    vector<int> w(L.begin(),L.end()); sort(w.begin(),w.end());
    // rotation reduction: fix y_0 = 0 (label of block of position 0); total = (m/s0) * count
    int s0=0; for(int v: L) if(v==0) s0++;
    w.erase(w.begin()); // remove one 0; w is sorted so w[0]==0 was first
    vector<int> full(m);
    map<pair<int,ll>,ll> hist;
    unordered_map<string,pair<int,ll>> cache;
    vector<ll> B(n*n); string key(n*n,'\0');
    do{
      full[0]=0; for(int j=1;j<m;j++) full[j]=w[j-1];
      for(int i=0;i<n*n;i++) B[i]=Bx[i];
      for(int j=0;j<m;j++){int a=full[j],b=full[(j+1)%m]; B[a*n+b]--; B[b*n+a]--;}
      for(int i=0;i<n*n;i++) key[i]=(char)(B[i]+64);
      auto it=cache.find(key); pair<int,ll> rv;
      if(it!=cache.end()) rv=it->second; else {
        // elimination
        vector<ll> Bi(B); vector<u64> S(n*n); for(int i=0;i<n*n;i++) S[i]=tom(B[i]);
        vector<char> rem(n,1); vector<int> piv; 
        while(true){
          int pi=-1; for(int i=0;i<n;i++) if(rem[i]&&S[i*n+i]){pi=i;break;}
          if(pi<0){ int ii=-1,jj=-1; for(int i=0;i<n&&ii<0;i++) if(rem[i]) for(int j=0;j<n;j++) if(rem[j]&&j!=i&&S[i*n+j]){ii=i;jj=j;break;}
            if(ii<0) break;
            for(int k=0;k<n;k++){ Bi[ii*n+k]+=Bi[jj*n+k]; } for(int k=0;k<n;k++){ Bi[k*n+ii]+=Bi[k*n+jj]; }
            for(int k=0;k<n;k++){ S[ii*n+k]=addm(S[ii*n+k],S[jj*n+k]); } for(int k=0;k<n;k++){ S[k*n+ii]=addm(S[k*n+ii],S[k*n+jj]); }
            pi=ii; }
          u64 a=S[pi*n+pi], ai=invm(a);
          vector<u64> col(n); for(int i=0;i<n;i++) col[i]=S[i*n+pi];
          for(int i=0;i<n;i++) if(rem[i]&&i!=pi&&col[i]){ u64 f=mulm(col[i],ai);
              for(int k=0;k<n;k++) if(rem[k]&&k!=pi) S[i*n+k]=subm(S[i*n+k],mulm(f,col[k])); }
          for(int i=0;i<n;i++){ S[i*n+pi]=0; S[pi*n+i]=0; }
          rem[pi]=0; piv.push_back(pi);
        }
        int r=piv.size();
        vector<vector<ll>> A(r, vector<ll>(r)); double had=0;
        for(int a=0;a<r;a++){ double rn=0; for(int b=0;b<r;b++){A[a][b]=Bi[piv[a]*n+piv[b]]; rn+= (double)A[a][b]*A[a][b];} had+=0.5*log2(rn+1e-300);}        
        if(had>60){ fprintf(stderr,"Hadamard bound too big %f\n",had); exit(1);} 
        // rank check of original B: Hadamard on B rows
        double hb=0; for(int a=0;a<n;a++){double rn=0; for(int b=0;b<n;b++) rn+=(double)B[a*n+b]*B[a*n+b]; if(rn>0) hb+=0.5*log2(rn);} if(hb>60){fprintf(stderr,"rank Hadamard too big\n"); exit(1);} 
        i128 D=bareiss_det(A); if(D==0){fprintf(stderr,"zero det?\n"); exit(1);} 
        ll Ds = (ll)D; if((i128)Ds!=D){fprintf(stderr,"overflow\n"); exit(1);} 
        rv={r, r? sqfree(Ds):1}; cache[key]=rv;
      }
      hist[rv]++;
    }while(next_permutation(w.begin(),w.end()));
    res[t]=hist;
  }
  for(int t=0;t<J;t++) for(auto&kv:res[t]) { int s0=0; for(int v: jobs[t].second) if(v==0) s0++; printf("%d %d %lld %lld %d\n", jobs[t].first, kv.first.first, kv.first.second, kv.second*(long long)jobs[t].second.size(), s0);}
}
