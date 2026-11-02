// Wave 45, task 3: exact Lemma U census at m=110, components (29,1)x(109,1).
// u=55, beta=alpha^2. block0={(t_k,s_k)}, block1=-block0, P=block0 U block1.
// Groups by multiset hash of P (sum of per-pair splitmix hashes, order-free),
// then exact verification within hash groups. Within each true P-group:
//   - block-pair constancy (unordered {B0,-B0})
//   - dihedral-orbit count (D = <simultaneous rot, conj, neg>)
//   - connectivity of orbits via partial moves J_a, J_b, N_a, N_b
//     (f=1: no genuine scaling edges; no kernel, p != 3)
// Reports: conflicts (Lemma U counterexample), multi-orbit groups and
// whether all are J/N-connected (else UNKNOWN = candidate fourth kind).
#include <cstdio>
#include <cstdint>
#include <cstring>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <functional>
using namespace std;
typedef uint64_t u64;
static u64 splitmix(u64 x){ x+=0x9e3779b97f4a7c15ULL; x=(x^(x>>30))*0xbf58476d1ce4e5b9ULL; x=(x^(x>>27))*0x94d049bb133111ebULL; return x^(x>>31); }

// R = Z[sqrt2] mod mod
struct Comp{
  int p, mod, na; // na = #params = mod^2
  vector<int> rot, conj, neg; // param-index maps
  vector<vector<short>> cyc; // cycles of trace values, length u
  vector<int> period; vector<char> distinct, negfree, nonzero;
};
static pair<int,int> rmul(pair<int,int> x, pair<int,int> y, int mod){
  return {(int)(((long long)x.first*y.first + 2LL*x.second*y.second)%mod),
          (int)(((long long)x.first*y.second + (long long)x.second*y.first)%mod)};
}
static pair<int,int> rpow(pair<int,int> x, long long n, int mod){
  pair<int,int> r={1%mod,0};
  while(n){ if(n&1) r=rmul(r,x,mod); x=rmul(x,x,mod); n>>=1; }
  return r;
}
static Comp build(int p, int u){
  Comp C; C.p=p; C.mod=p; C.na=p*p;
  pair<int,int> alpha={3%p,2%p};
  auto au=rpow(alpha,u,p);
  if(au!=make_pair(p-1,0)){ fprintf(stderr,"not constraining %d\n",p); exit(1); }
  auto beta=rmul(alpha,alpha,p);
  vector<pair<int,int>> bp(u); bp[0]={1,0};
  for(int k=1;k<u;k++) bp[k]=rmul(bp[k-1],beta,p);
  vector<pair<int,int>> Cs; Cs.reserve(C.na);
  for(int a=0;a<p;a++) for(int b=0;b<p;b++) Cs.push_back({a,b});
  unordered_map<int,int> idx; idx.reserve(C.na*2);
  for(int i=0;i<C.na;i++) idx[Cs[i].first*p+Cs[i].second]=i;
  C.rot.assign(C.na,0); C.conj.assign(C.na,0); C.neg.assign(C.na,0);
  for(int i=0;i<C.na;i++){
    auto Cr=rmul(beta,Cs[i],p); C.rot[i]=idx[Cr.first*p+Cr.second];
    C.conj[i]=idx[Cs[i].first*p+((-Cs[i].second)%p+p)%p];
    C.neg[i]=idx[((-Cs[i].first)%p+p)%p*p+((-Cs[i].second)%p+p)%p];
  }
  C.cyc.assign(C.na, vector<short>(u));
  C.period.assign(C.na,0); C.distinct.assign(C.na,0); C.negfree.assign(C.na,0); C.nonzero.assign(C.na,0);
  for(int i=0;i<C.na;i++){
    auto &cy=C.cyc[i];
    for(int k=0;k<u;k++){ auto v=rmul(Cs[i],bp[k],p); cy[k]=(short)((2*v.first)%p); }
    int T=u;
    for(int d=1;d<=u;d++) if(u%d==0){ bool ok=true; for(int k=0;k<u;k++) if(cy[k]!=cy[k%d]){ok=false;break;} if(ok){T=d;break;} }
    C.period[i]=T;
    vector<short> vals(cy.begin(), cy.begin()+T);
    sort(vals.begin(), vals.end()); vals.erase(unique(vals.begin(), vals.end()), vals.end());
    C.distinct[i]=(int)vals.size()==T;
    unordered_set<int> vs(vals.begin(), vals.end());
    bool nf=true, nz=true;
    for(int v: vals){ if(v==0) nz=false; if(vs.count((p-v)%p)) nf=false; }
    C.negfree[i]=nf; C.nonzero[i]=nz;
  }
  return C;
}
int main(){
  const int u=55;
  Comp A=build(29,u), B=build(109,u);
  const int na=A.na, nb=B.na;
  printf("params: na=%d nb=%d points=%lld\n", na, nb, (long long)na*nb);
  // generic counts
  long long genA=0, genB=0;
  for(int i=0;i<na;i++) if(A.distinct[i]&&A.negfree[i]&&A.nonzero[i]) genA++;
  for(int i=0;i<nb;i++) if(B.distinct[i]&&B.negfree[i]&&B.nonzero[i]) genB++;
  printf("generic params: A %lld/%d  B %lld/%d\n", genA, na, genB, nb);
  // pair-code hash table: code = a*109+b in [0,3161)
  static u64 H[3161];
  for(int c=0;c<3161;c++) H[c]=splitmix(0x1234567ULL+c*2654435761ULL);
  vector<u64> ph; ph.reserve((size_t)na*nb);
  vector<int> pt; pt.reserve((size_t)na*nb);
  vector<u64> pairhash; // per-point block0 hash for canonical block compare (sorted not needed: use sum too, plus exact check later)
  // We store per point: hashP (multiset hash of P) and also multiset hash of block0 alone (for block-pair compare, need exact; do exact on groups)
  for(int ia=0; ia<na; ia++){
    auto &ta=A.cyc[ia];
    for(int ib=0; ib<nb; ib++){
      auto &sb=B.cyc[ib];
      u64 h=0;
      for(int k=0;k<u;k++){
        int c0=ta[k]*109+sb[k];
        int c1=((29-ta[k])%29)*109+((109-sb[k])%109);
        h+=H[c0]+H[c1];
      }
      ph.push_back(h); pt.push_back(ia*nb+ib);
    }
  }
  printf("hashes done\n"); fflush(stdout);
  vector<int> order(pt.size());
  for(size_t i=0;i<order.size();i++) order[i]=(int)i;
  sort(order.begin(), order.end(), [&](int x,int y){ return ph[x]<ph[y]; });
  long long ngroups=0, nconflict=0, nmulti=0, nunknown=0, ngeneric_multi=0;
  long long totpts=0;
  // iterate hash groups
  size_t i=0;
  vector<short> codes; codes.reserve(2*u);
  vector<short> b0; b0.reserve(u);
  while(i<order.size()){
    size_t j=i+1;
    while(j<order.size() && ph[order[j]]==ph[order[i]]) j++;
    // exact split of [i,j) by full sorted P
    // build sorted P for each point in range (only if range>1 or check anyway)
    // group by exact P via map from string key
    unordered_map<string, vector<int>> ex;
    for(size_t t=i;t<j;t++){
      int id=pt[order[t]]; int ia=id/nb, ib=id%nb;
      codes.clear();
      for(int k=0;k<u;k++){ codes.push_back((short)(A.cyc[ia][k]*109+B.cyc[ib][k])); codes.push_back((short)(((29-A.cyc[ia][k])%29)*109+((109-B.cyc[ib][k])%109))); }
      sort(codes.begin(), codes.end());
      string key((char*)codes.data(), codes.size()*sizeof(short));
      ex[key].push_back(id);
    }
    for(auto &kv: ex){
      auto &pts=kv.second; ngroups++; totpts+=pts.size();
      // block-pair canonical: sorted block0, and sorted -block0; unordered pair -> min/max
      string canon0; bool first=true; string ref;
      bool conflict=false;
      for(int id: pts){
        int ia=id/nb, ib=id%nb;
        vector<pair<short,short>> pairs;
        for(int k=0;k<u;k++) pairs.push_back({A.cyc[ia][k], B.cyc[ib][k]});
        sort(pairs.begin(), pairs.end());
        string s0((char*)pairs.data(), pairs.size()*sizeof(pair<short,short>));
        vector<pair<short,short>> pairsN;
        for(auto &pr: pairs) pairsN.push_back({(short)((29-pr.first)%29),(short)((109-pr.second)%109)});
        sort(pairsN.begin(), pairsN.end());
        string s1((char*)pairsN.data(), pairsN.size()*sizeof(pair<short,short>));
        string can = (s0<s1)? (s0+"|"+s1) : (s1+"|"+s0);
        if(first){ ref=can; first=false; } else if(can!=ref) conflict=true;
      }
      if(conflict){ nconflict++; if(nconflict<=5){ printf("CONFLICT group size %zu first pt %d\n", pts.size(), pts[0]); } continue; }
      // dihedral orbits within group: D generated by (rot,rot),(conj,conj),(neg,neg)
      unordered_set<int> inG(pts.begin(), pts.end());
      unordered_set<int> seen;
      int norb=0; vector<vector<int>> orbits;
      for(int id: pts){
        if(seen.count(id)) continue;
        norb++;
        vector<int> orb; vector<int> stack={id}; seen.insert(id);
        while(!stack.empty()){
          int cur=stack.back(); stack.pop_back(); orb.push_back(cur);
          int ca=cur/nb, cb=cur%nb;
          int nxt[3]={A.rot[ca]*nb+B.rot[cb], A.conj[ca]*nb+B.conj[cb], A.neg[ca]*nb+B.neg[cb]};
          for(int q=0;q<3;q++) if(inG.count(nxt[q]) && !seen.count(nxt[q])){ seen.insert(nxt[q]); stack.push_back(nxt[q]); }
        }
        orbits.push_back(orb);
      }
      if(norb>1){
        nmulti++;
        // generic? any point generic on both sides?
        bool gen=false;
        for(int id: pts){ int ia=id/nb, ib=id%nb; if(A.distinct[ia]&&A.negfree[ia]&&A.nonzero[ia]&&B.distinct[ib]&&B.negfree[ib]&&B.nonzero[ib]) gen=true; }
        if(gen) ngeneric_multi++;
        // connectivity via J_a=(conj,id), J_b=(id,conj), N_a=(neg,id), N_b=(id,neg)
        // build orbit graph: orbit index per point
        unordered_map<int,int> orbidx;
        for(int o=0;o<(int)orbits.size();o++) for(int id: orbits[o]) orbidx[id]=o;
        vector<int> parent(norb); for(int o=0;o<norb;o++) parent[o]=o;
        function<int(int)> find=[&](int x){ return parent[x]==x?x:(parent[x]=find(parent[x])); };
        auto uni=[&](int x,int y){ x=find(x); y=find(y); if(x!=y) parent[x]=y; };
        for(int id: pts){
          int ia=id/nb, ib=id%nb; int o0=orbidx[id];
          int ms[4]={A.conj[ia]*nb+ib, ia*nb+B.conj[ib], A.neg[ia]*nb+ib, ia*nb+B.neg[ib]};
          for(int q=0;q<4;q++) if(inG.count(ms[q])) uni(o0, orbidx[ms[q]]);
        }
        int comp=find(0); bool conn=true;
        for(int o=0;o<norb;o++) if(find(o)!=comp) conn=false;
        if(!conn){ nunknown++; if(nunknown<=10) printf("UNKNOWN group size %zu orbits %d pts0 %d\n", pts.size(), norb, pts[0]); }
      }
    }
    i=j;
  }
  printf("RESULT groups=%lld points=%lld conflicts=%lld multi-orbit=%lld generic-multi=%lld unknown=%lld\n",
         ngroups, totpts, nconflict, nmulti, ngeneric_multi, nunknown);
  return 0;
}
