#include <bits/stdc++.h>
using namespace std;
// Per-class pattern lemma check for blocks: r_s = T*c_s + D*e_s mod Q', Q'=2^(L+3), P=2^L
// D multiple of 8. Group blocks by sorted multiset, check per-class multisets lie in one D4 orbit.
int main(int argc,char**argv){
  int L = argc>1 ? atoi(argv[1]) : 6;
  int P = 1<<L;
  int Q = 1<<(L+3);
  vector<int> cs(P+2), es(P+2);
  cs[0]=1; cs[1]=3; es[0]=0; es[1]=1;
  for(int i=2;i<P+2;i++){ cs[i]=(6*cs[i-1]-cs[i-2])%Q; if(cs[i]<0)cs[i]+=Q; es[i]=(6*es[i-1]-es[i-2])%Q; if(es[i]<0)es[i]+=Q; }
  auto d4_orbit = [](array<vector<int>,4> pc){
    set<array<vector<int>,4>> s;
    auto a=pc[0],b=pc[1],c=pc[2],d=pc[3];
    array<array<vector<int>,4>,8> cand = {{{a,b,c,d},{b,c,d,a},{c,d,a,b},{d,a,b,c},{a,d,c,b},{b,a,d,c},{c,b,a,d},{d,c,b,a}}};
    for(auto &x: cand) s.insert(x);
    return s;
  };
  map<vector<int>, vector<array<vector<int>,4>>> groups;
  vector<int> blk(P);
  long long nblocks=0;
  for(int T=0;T<Q;T++){
    for(int D=0;D<Q;D+=8){
      for(int s=0;s<P;s++) blk[s]=(T*cs[s]+D*es[s])%Q;
      vector<int> ms=blk; sort(ms.begin(), ms.end());
      array<vector<int>,4> pc;
      for(int r=0;r<4;r++){ for(int s=r;s<P;s+=4) pc[r].push_back(blk[s]); sort(pc[r].begin(), pc[r].end()); }
      groups[ms].push_back(pc);
      nblocks++;
    }
  }
  long long bad=0, ngroups=0, npairs=0;
  for(auto &kv: groups){
    ngroups++;
    auto &lst=kv.second;
    npairs += (long long)lst.size()*(lst.size()-1)/2;
    auto orb = d4_orbit(lst[0]);
    for(auto &pc: lst) if(!orb.count(pc)){ bad++; break; }
  }
  cout<<"L="<<L<<" P="<<P<<" Q="<<Q<<" blocks="<<nblocks<<" groups="<<ngroups<<" pairs="<<npairs<<" bad_groups="<<bad<<"\n";
  return 0;
}
