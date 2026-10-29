// Independent engine: E|Tr U^m|^2 = p^{-m} sum_rho W(rho) s(rho) sum_{w in Arr(rho)} G(rho,w)
// (Prop. 2 re-derived; s(rho)=prod|B|!, Arr = distinct block words with rho's block multiplicities).
// Rotation reduction of words: sum_w f(w) = (m/mult(b)) sum_{w: w_0=b} f(w)  (f rotation invariant).
// mode 0 (symbolic): rank over Q by exact int64/int128 Bareiss; I = pivot rows (row basis) => B_II nonsingular;
//                    D = squarefree(2^r det B_II); Gauss sum = p^{n-r/2} eps^r (D/p) for p not dividing minors.
// mode P (prime):    rank over F_P; Legendre symbol (2^r det B_II / P).
// usage: engine m mode maxk2 nthreads < list of rho (comma separated RGS), output keys (k2=2d+r, r, D|leg, count)
#include <vector>
#include <algorithm>
#include <thread>
#include <atomic>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <tuple>
#include <iostream>
#include <sstream>
using namespace std;
typedef long long ll;
int m, P, maxk2, nth;
ll sqfree(ll v){ if(v==0) return 0; ll s = v<0?-1:1; v = v<0?-v:v; ll r=1;
  for(ll q=2;q*q<=v;q++){ int e=0; while(v%q==0){v/=q;e++;} if(e&1) r*=q; } r*=v; return s*r; }
ll pw(ll a, ll e, ll md){ ll r=1; a%=md; if(a<0)a+=md; while(e){ if(e&1) r=(__int128)r*a%md; a=(__int128)a*a%md; e>>=1;} return r; }
int rankQ(vector<ll> A, int n, int lim, vector<int>& rows){
  vector<int> rid(n); for(int i=0;i<n;i++) rid[i]=i; int r=0; ll prev=1; rows.clear();
  for(int c=0;c<n && r<n;c++){
    int piv=-1; for(int i=r;i<n;i++) if(A[i*n+c]!=0){piv=i;break;}
    if(piv<0) continue;
    if(piv!=r){ for(int k=0;k<n;k++) swap(A[piv*n+k],A[r*n+k]); swap(rid[piv],rid[r]); }
    for(int i=r+1;i<n;i++){
      for(int k=c+1;k<n;k++){ __int128 t=(__int128)A[r*n+c]*A[i*n+k]-(__int128)A[i*n+c]*A[r*n+k];
        if(t%prev!=0){ fprintf(stderr,"Bareiss inexact\n"); exit(2);} A[i*n+k]=(ll)(t/prev); }
      A[i*n+c]=0; }
    prev=A[r*n+c]; rows.push_back(rid[r]); r++;
    if(r>lim) return r; }
  return r; }
ll detQ(vector<ll> A,int n){ ll prev=1; int sg=1;
  for(int c=0;c<n;c++){ int piv=-1; for(int i=c;i<n;i++) if(A[i*n+c]){piv=i;break;} if(piv<0) return 0;
    if(piv!=c){ for(int k=0;k<n;k++) swap(A[piv*n+k],A[c*n+k]); sg=-sg; }
    for(int i=c+1;i<n;i++){ for(int k=c+1;k<n;k++){ __int128 t=(__int128)A[c*n+c]*A[i*n+k]-(__int128)A[i*n+c]*A[c*n+k]; A[i*n+k]=(ll)(t/prev);} A[i*n+c]=0; }
    prev=A[c*n+c]; }
  return sg*A[(n-1)*n+(n-1)]; }
int rankP(vector<ll> A,int n,int lim, vector<int>&rows){
  for(auto&v:A){ v%=P; if(v<0) v+=P; }
  vector<int> rid(n); for(int i=0;i<n;i++) rid[i]=i; int r=0; rows.clear();
  for(int c=0;c<n&&r<n;c++){ int piv=-1; for(int i=r;i<n;i++) if(A[i*n+c]){piv=i;break;} if(piv<0) continue;
    if(piv!=r){ for(int k=0;k<n;k++) swap(A[piv*n+k],A[r*n+k]); swap(rid[piv],rid[r]); }
    ll inv=pw(A[r*n+c],P-2,P);
    for(int i=r+1;i<n;i++){ if(!A[i*n+c]) continue; ll f=A[i*n+c]*inv%P; for(int k=c;k<n;k++){ A[i*n+k]=(A[i*n+k]-f*A[r*n+k])%P; if(A[i*n+k]<0)A[i*n+k]+=P; } }
    rows.push_back(rid[r]); r++; if(r>lim) return r; }
  return r; }
ll detP(vector<ll> A,int n){ for(auto&v:A){v%=P; if(v<0)v+=P;} ll d=1;
  for(int c=0;c<n;c++){ int piv=-1; for(int i=c;i<n;i++) if(A[i*n+c]){piv=i;break;} if(piv<0) return 0;
    if(piv!=c){ for(int k=0;k<n;k++) swap(A[piv*n+k],A[c*n+k]); d=(P-d)%P; }
    d=d*A[c*n+c]%P; ll inv=pw(A[c*n+c],P-2,P);
    for(int i=c+1;i<n;i++){ ll f=A[i*n+c]*inv%P; for(int k=c;k<n;k++){ A[i*n+k]=(A[i*n+k]-f*A[c*n+k])%P; if(A[i*n+k]<0)A[i*n+k]+=P;} } }
  return d%P; }
typedef tuple<int,int,ll> Key;
int main(int argc,char**argv){
  m=atoi(argv[1]); P=atoi(argv[2]); maxk2=atoi(argv[3]); nth=atoi(argv[4]);
  string line;
  while(getline(cin,line)){
    if(line.empty()) continue;
    vector<int> x; { stringstream ss(line); string t; while(getline(ss,t,',')) x.push_back(stoi(t)); }
    int n=*max_element(x.begin(),x.end())+1; int d=m-n;
    vector<int> mult(n,0); for(int v:x) mult[v]++;
    int b=0; for(int v=0;v<n;v++) if(mult[v]<mult[b]) b=v;
    vector<int> rest; for(int v=0;v<n;v++) for(int k=0;k<mult[v]-(v==b);k++) rest.push_back(v);
    sort(rest.begin(),rest.end());
    int lim = maxk2-2*d; if(lim<0) continue;
    vector<ll> Bx(n*n,0);
    for(int j=0;j<m;j++){ int a=x[j], c=x[(j+1)%m]; if(a==c) Bx[a*n+a]+=2; else { Bx[a*n+c]++; Bx[c*n+a]++; } }
    vector<vector<int>> tasks;
    { vector<int> r1=rest; r1.erase(unique(r1.begin(),r1.end()),r1.end());
      for(int a:r1){ vector<int> rr=rest; rr.erase(find(rr.begin(),rr.end(),a));
        if(rr.empty()){ tasks.push_back({a}); continue; }
        vector<int> r2=rr; r2.erase(unique(r2.begin(),r2.end()),r2.end());
        for(int c:r2) tasks.push_back({a,c}); } }
    if(rest.empty()) tasks.push_back({});
    atomic<size_t> nxt(0); vector<map<Key,ll>> res(nth); vector<ll> skipped(nth,0);
    auto worker=[&](int id){ vector<int> rows; vector<ll> B(n*n); vector<int> w(m);
      while(true){ size_t t=nxt++; if(t>=tasks.size()) break; auto pre=tasks[t];
        vector<int> rr=rest; for(int v:pre) rr.erase(find(rr.begin(),rr.end(),v)); sort(rr.begin(),rr.end());
        do{
          w[0]=b; int pos=1; for(int v:pre) w[pos++]=v; for(int v:rr) w[pos++]=v;
          B=Bx; for(int j=0;j<m;j++){ int a=w[j], c=w[(j+1)%m]; if(a==c) B[a*n+a]-=2; else { B[a*n+c]--; B[c*n+a]--; } }
          int r; ll D;
          if(P==0){ r=rankQ(B,n,lim,rows); if(r>lim){skipped[id]++; continue;}
            if(r==0) D=1; else { vector<ll> S(r*r); for(int i=0;i<r;i++) for(int k=0;k<r;k++) S[i*r+k]=B[rows[i]*n+rows[k]]; ll dt=detQ(S,r); if(dt==0){fprintf(stderr,"singular principal block!\n"); exit(1);} D=sqfree((r&1)?2*dt:dt); } }
          else { r=rankP(B,n,lim,rows); if(r>lim){skipped[id]++; continue;}
            if(r==0) D=1; else { vector<ll> S(r*r); for(int i=0;i<r;i++) for(int k=0;k<r;k++) S[i*r+k]=B[rows[i]*n+rows[k]]; ll dt=detP(S,r); if(dt==0){fprintf(stderr,"singular mod P!\n"); exit(1);} ll v=(r&1)? 2*dt%P : dt; ll lg=pw(v,(P-1)/2,P); D = (lg==1)?1:-1; } }
          res[id][Key(2*d+r,r,D)]++;
        } while(next_permutation(rr.begin(),rr.end()));
      } };
    vector<thread> T; for(int i=0;i<nth;i++) T.emplace_back(worker,i); for(auto&t:T) t.join();
    map<Key,ll> tot; for(auto&mm:res) for(auto&kv:mm) tot[kv.first]+=kv.second;
    printf("RHO %s n=%d d=%d multb=%d\n",line.c_str(),n,d,mult[b]);
    for(auto&kv:tot) printf("T %d %d %lld %lld\n",get<0>(kv.first),get<1>(kv.first),get<2>(kv.first),kv.second);
    fflush(stdout);
  }
}
