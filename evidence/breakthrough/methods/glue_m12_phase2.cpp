#include <bits/stdc++.h>
using namespace std;
const int M=12;
using Vec=array<int,12>;
int main(){
  vector<int> QS={128,81,25,49,121};
  map<int, vector<Vec>> FIX;
  map<int, set<Vec>> FIXSET;
  for(int q: QS){
    vector<Vec> F;
    for(int a=0;a<q;a++) for(int b=0;b<q;b++){
      int seq[14]; seq[0]=a; seq[1]=b;
      for(int i=0;i<M;i++) seq[i+2]=((6*seq[i+1]-seq[i])%q+q)%q;
      if(seq[M]==a && seq[M+1]==b){
        Vec v; for(int i=0;i<M;i++) v[i]=seq[i];
        bool ok=true;
        for(int i=0;i<M;i++){ int s=6*v[i]-v[(i+M-1)%M]-v[(i+1)%M]; if(((s%q)+q)%q!=0) ok=false; }
        if(ok) F.push_back(v);
      }
    }
    FIX[q]=F; FIXSET[q]=set<Vec>(F.begin(),F.end());
    cerr<<"q="<<q<<" |Fix|="<<F.size()<<endl;
  }
  // dihedral perms: p[j] as index into v: (v∘p)[j]=v[p[j]]
  vector<Vec> DIH;
  {
    set<Vec> s;
    for(int k=0;k<M;k++){
      Vec r,t;
      for(int j=0;j<M;j++){ r[j]=(j+k)%M; t[j]=((k-j)%M+M)%M; }
      s.insert(r); s.insert(t);
    }
    DIH.assign(s.begin(),s.end());
  }
  cerr<<"dihedral="<<DIH.size()<<endl;
  auto apply_perm=[&](const Vec& v, const Vec& p){ Vec w; for(int j=0;j<M;j++) w[j]=v[p[j]]; return w; };
  auto tau_count=[&](const Vec& v){ long long prod=1; map<int,int> c; for(int x:v) c[x]++; for(auto &kv:c){ long long f=1; for(int i=2;i<=kv.second;i++) f*=i; prod*=f; if(prod>20000) return prod; } return prod; };
  auto encode=[&](const Vec& t){ uint64_t e=0; for(int i=M-1;i>=0;i--) e=e*12+t[i]; return e; };
  auto decode=[&](uint64_t e){ Vec t; for(int i=0;i<M;i++){ t[i]=e%12; e/=12; } return t; };
  function<unordered_set<uint64_t>(int)> gen_taus = [&](int q){
    unordered_set<uint64_t> S;
    map<Vec, vector<Vec>> fib;
    for(auto &v: FIX[q]){ Vec s=v; sort(s.begin(),s.end()); fib[s].push_back(v); }
    for(auto &kv: fib){
      auto &vs=kv.second;
      for(auto &v: vs){
        if(tau_count(v)>20000) continue;
        map<int, vector<int>> pos;
        for(int i=0;i<M;i++) pos[v[i]].push_back(i);
        for(auto &w: vs){
          vector<vector<int>> cand(M);
          for(int j=0;j<M;j++) cand[j]=pos[w[j]];
          Vec tau; vector<int> used(M,0);
          function<void(int)> bt=[&](int j){
            if(j==M){ S.insert(encode(tau)); return; }
            for(int i: cand[j]) if(!used[i]){ used[i]=1; tau[j]=i; bt(j+1); used[i]=0; }
          };
          bt(0);
        }
      }
    }
    return S;
  };
  auto taus121=gen_taus(121);
  auto taus25=gen_taus(25);
  cerr<<"taus121="<<taus121.size()<<" taus25="<<taus25.size()<<endl;
  vector<uint64_t> cand;
  for(auto e: taus25) if(!taus121.count(e)) cand.push_back(e);
  cerr<<"phase2 tau candidates (25\\121): "<<cand.size()<<endl;
  // dihedral encoded set
  unordered_set<uint64_t> dihset; for(auto &d: DIH) dihset.insert(encode(d));
  // components for phase2: 25,49,81,128 (121 fixed zero)
  vector<int> Q2={25,49,81,128};
  auto in_fix=[&](const Vec& w, int q){ for(int i=0;i<M;i++){ int s=6*w[i]-w[(i+M-1)%M]-w[(i+1)%M]; if(((s%q)+q)%q!=0) return false; } return true; };
  long long processed=0, found=0;
  for(uint64_t e: cand){
    if(dihset.count(e)) continue;
    Vec tau=decode(e);
    processed++;
    // S lists per component
    struct Comp{ int q; vector<Vec> S; vector<Vec> W; vector<uint32_t> dmask; };
    vector<Comp> comps;
    bool bad=false;
    for(int q: Q2){
      Comp c; c.q=q;
      for(auto &v: FIX[q]){
        Vec w=apply_perm(v,tau);
        if(in_fix(w,q)){ c.S.push_back(v); c.W.push_back(w); }
      }
      comps.push_back(move(c));
    }
    // order by S size ascending
    sort(comps.begin(), comps.end(), [](const Comp& a, const Comp& b){ return a.S.size()<b.S.size(); });
    // precompute dmask per comp (only for v in S)
    for(auto &c: comps){
      c.dmask.assign(c.S.size(),0);
      for(size_t i=0;i<c.S.size();i++){
        uint32_t mask=0;
        for(int di=0;di<(int)DIH.size();di++){
          if(apply_perm(c.S[i], DIH[di])==c.W[i]) mask|=(1u<<di);
        }
        c.dmask[i]=mask;
      }
    }
    // backtrack over comps to empty possible mask
    uint32_t ALL=(DIH.size()==32?0xFFFFFFFFu:((1u<<DIH.size())-1));
    vector<Vec> chosen(Q2.size());
    function<bool(int,uint32_t)> bt=[&](int idx, uint32_t possible)->bool{
      if(possible==0) return true;
      if(idx==(int)comps.size()) return false;
      auto &c=comps[idx];
      for(size_t i=0;i<c.S.size();i++){
        uint32_t np=possible & c.dmask[i];
        if(bt(idx+1, np)) return true;
      }
      return false;
    };
    // need chosen values on success: rerun with tracking
    vector<int> choice_idx;
    function<bool(int,uint32_t)> bt2=[&](int idx, uint32_t possible)->bool{
      if(possible==0) return true;
      if(idx==(int)comps.size()) return false;
      auto &c=comps[idx];
      for(size_t i=0;i<c.S.size();i++){
        uint32_t np=possible & c.dmask[i];
        choice_idx.push_back((int)i);
        if(bt2(idx+1, np)) return true;
        choice_idx.pop_back();
      }
      return false;
    };
    bool ok=bt2(0, ALL);
    if(ok){
      // reconstruct chosen comp vectors in original Q order
      map<int,Vec> compmap; compmap[121]=Vec{0,0,0,0,0,0,0,0,0,0,0,0};
      for(size_t i=0;i<comps.size();i++) compmap[comps[i].q]=comps[i].S[choice_idx[i]];
      // global y via CRT
      const long long Dd=1536796800LL;
      Vec y{}; // values mod D, use long long array separately
      long long yg[12]={0};
      for(int j=0;j<M;j++){
        long long x=0;
        for(int q: QS){
          long long Mq=Dd/q;
          // inverse of Mq mod q
          long long inv=1; // pow
          long long base=Mq%q, exp=q-1; // not prime; use extended gcd
          // extended gcd
          long long a=Mq, b=q, x0=1, x1=0;
          // use std extended euclid for inverse (gcd=1 since coprime)
          long long old_r=Mq, r=q, old_s=1, s=0;
          while(r){ long long qq=old_r/r; long long tr=old_r-qq*r; old_r=r; r=tr; long long ts=old_s-qq*s; old_s=s; s=ts; }
          inv=((old_s%q)+q)%q;
          x=(x+compmap[q][j]*Mq*inv)%Dd;
        }
        yg[j]=x;
      }
      // gamma canon check: compare canonical forms of y and y∘tau
      auto canon=[&](long long* arr){
        long long best[12]; bool first=true;
        for(auto &d: DIH){
          long long candv[12]; for(int j=0;j<M;j++) candv[j]=arr[d[j]];
          if(first || lexicographical_compare(candv,candv+12,best,best+12)){ memcpy(best,candv,sizeof(best)); first=false; }
        }
        return array<long long,12>{best[0],best[1],best[2],best[3],best[4],best[5],best[6],best[7],best[8],best[9],best[10],best[11]};
      };
      long long y2g[12]; for(int j=0;j<M;j++) y2g[j]=yg[tau[j]];
      auto c1=canon(yg), c2=canon(y2g);
      // w vectors
      long long w1[12], w2[12];
      for(int i=0;i<M;i++){ w1[i]=(6*yg[i]-yg[(i+M-1)%M]-yg[(i+1)%M])/Dd; w2[i]=(6*y2g[i]-y2g[(i+M-1)%M]-y2g[(i+1)%M])/Dd; }
      sort(w1,w1+12); sort(w2,w2+12);
      cout<<"FOUND tau="; for(int j=0;j<M;j++) cout<<tau[j]<<(j+1==M?'\n':' ');
      cout<<"comp:"; for(int q: QS){ cout<<" q"<<q<<"="; for(int j=0;j<M;j++) cout<<compmap[q][j]<<(j+1==M?';':' '); }
      cout<<"\ny="; for(int j=0;j<M;j++) cout<<yg[j]<<(j+1==M?'\n':' ');
      cout<<"y2="; for(int j=0;j<M;j++) cout<<y2g[j]<<(j+1==M?'\n':' ');
      cout<<"canon_equal="<<(c1==c2)<<" pw_separates="<<(!equal(w1,w1+12,w2))<<"\n";
      cout<<"w_sorted="; for(int j=0;j<M;j++) cout<<w1[j]<<(j+1==M?'\n':' ');
      cout<<"w2_sorted="; for(int j=0;j<M;j++) cout<<w2[j]<<(j+1==M?'\n':' ');
      cout.flush();
      found++;
      if(found>=5) break;
    }
    if(processed%50000==0) cerr<<"processed "<<processed<<" found "<<found<<endl;
  }
  cerr<<"DONE processed="<<processed<<" found="<<found<<endl;
  return 0;
}
