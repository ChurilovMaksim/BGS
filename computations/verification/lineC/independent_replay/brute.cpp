// Independent exact brute force for E|Tr (D_theta M_p)^m|^2, p odd prime.
// E p^m = sum over multisets M of |sum_{distinct arrangements x of M} zeta^{c P_x}|^2,
// P_x = sum_j x_j x_{j+1} (cyclic), c = 4^{-1}. Accumulate autocorrelation counts of
// Delta = P_x - P_y in classes 0 / nonzero square / nonsquare (class of c*Delta = class of Delta).
// Translation x->x+t leaves P_x-P_y invariant (same multiset); translation orbits of multisets have
// size p (m<p) and contain exactly k(M) members containing 0 (k = #distinct values).
// Output: N0 Nsq Nnsq with E p^m = N0 - (Nsq+Nnsq)/(p-1) + (Nsq-Nnsq) g/(p-1), g = quadratic Gauss sum.
#include <vector>
#include <algorithm>
#include <thread>
#include <atomic>
#include <functional>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <numeric>
using namespace std;
typedef __int128 i128;
int p,m; vector<int> issq; long long L;
struct Acc{ i128 n0=0,nsq=0,nns=0; };
void work(const vector<int>& ms, Acc&a, vector<long long>& h){
  int k=1; for(int i=1;i<m;i++) if(ms[i]!=ms[i-1]) k++;
  fill(h.begin(),h.end(),0);
  vector<int> x=ms;
  do{ long long s=0; for(int j=0;j<m;j++) s+= (long long)x[j]*x[(j+1)%m]; h[s%p]++; } while(next_permutation(x.begin(),x.end()));
  vector<int> nz; for(int v=0;v<p;v++) if(h[v]) nz.push_back(v);
  i128 w = (i128)(L/k) * p;
  for(int u: nz) for(int v: nz){ int d=((u-v)%p+p)%p; i128 t=(i128)h[u]*h[v]*w; if(d==0) a.n0+=t; else if(issq[d]) a.nsq+=t; else a.nns+=t; }
}
string s128(i128 v){ if(v==0) return "0"; bool neg=v<0; if(neg) v=-v; string s; while(v){ s+=char('0'+(int)(v%10)); v/=10;} if(neg) s+='-'; reverse(s.begin(),s.end()); return s; }
int main(int argc,char**argv){
  p=atoi(argv[1]); m=atoi(argv[2]); int nth = argc>3?atoi(argv[3]):8;
  if(m>=p){ fprintf(stderr,"need m<p\n"); return 1; }
  issq.assign(p,0); for(int t=1;t<p;t++) issq[(1LL*t*t)%p]=1;
  L=1; for(int i=1;i<=m;i++) L = L/std::gcd(L,(long long)i)*i;
  vector<Acc> accs(nth); atomic<int> next(0);
  vector<pair<int,int>> tasks; if(m>=3){ for(int a=0;a<p;a++) for(int b=a;b<p;b++) tasks.push_back({a,b}); } else if(m==2){ for(int a=0;a<p;a++) tasks.push_back({a,-1}); } else tasks.push_back({-1,-1});
  auto th=[&](int id){ vector<long long> h(p); while(true){ int t=next++; if(t>=(int)tasks.size()) break; auto [a,b]=tasks[t];
      vector<int> ms(m,0); if(a>=0) ms[1]=a; if(b>=0) ms[2]=b; int st = (a<0)?1:(b<0?2:3);
      function<void(int,int)> rec=[&](int pos,int lo){ if(pos==m){ work(ms,accs[id],h); return;} for(int v=lo;v<p;v++){ ms[pos]=v; rec(pos+1,v);} };
      int lo = st==1?0:(st==2?a:b); rec(st,lo); } };
  vector<thread> T; for(int i=0;i<nth;i++) T.emplace_back(th,i); for(auto&t:T) t.join();
  Acc tot; for(auto&a:accs){ tot.n0+=a.n0; tot.nsq+=a.nsq; tot.nns+=a.nns; }
  if(tot.n0%L||tot.nsq%L||tot.nns%L){ fprintf(stderr,"non-divisible!\n"); return 1; }
  printf("%d %d %s %s %s\n",p,m,s128(tot.n0/L).c_str(),s128(tot.nsq/L).c_str(),s128(tot.nns/L).c_str());
}
