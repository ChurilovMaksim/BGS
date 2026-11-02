#include <bits/stdc++.h>
using namespace std;
const int M=36, NT=72;
pair<int,int> mulp(pair<int,int> a, pair<int,int> b, int q){
    return {(int)(((long long)a.first*b.first + 2LL*a.second*b.second)%q),
            (int)(((long long)a.first*b.second + (long long)a.second*b.first)%q)};
}
int trp(pair<int,int> a, int q){ return (2*a.first)%q; }
struct Seq { array<int,36> v; };
bool operator<(Seq const& a, Seq const& b){ return a.v<b.v; }
bool operator==(Seq const& a, Seq const& b){ return a.v==b.v; }
using Mask72 = pair<unsigned long long, unsigned long long>; // bits 0..71 (lo:0..63, hi:64..71)
Mask72 mask_and(Mask72 a, Mask72 b){ return {a.first&b.first, a.second&b.second}; }
bool mask_zero(Mask72 a){ return a.first==0 && a.second==0; }
struct PQE { array<int,36> P, Q; Mask72 mask; array<unsigned long long,36> allow; }; // allow[i]: bitmask over j (36 bits) with P[j]==Q[i]
// bipartite matching: left i (0..35) -> allowed j bits
bool has_match(const array<unsigned long long,36>& allow){
    int matchR[36]; fill(begin(matchR), end(matchR), -1);
    function<bool(int, bool*)> bpm = [&](int u, bool* seen)->bool{
        unsigned long long bits = allow[u];
        for(int v=0; v<36; v++) if(bits>>v & 1ULL){
            if(seen[v]) continue; seen[v]=true;
            if(matchR[v]<0 || bpm(matchR[v], seen)){ matchR[v]=u; return true; }
        }
        return false;
    };
    for(int u=0; u<36; u++){ bool seen[36]={0}; if(!bpm(u, seen)) return false; }
    return true;
}
int main(){
    vector<array<int,36>> DIH;
    for(int k=0;k<36;k++){
        array<int,36> sh, rf;
        for(int i=0;i<36;i++){ sh[i]=(i+k)%36; rf[i]=((-i+k)%36+36)%36; }
        DIH.push_back(sh); DIH.push_back(rf);
    }
    sort(DIH.begin(), DIH.end()); DIH.erase(unique(DIH.begin(), DIH.end()), DIH.end());
    assert(DIH.size()==72);
    // component order: ascending PQ (128,49,25,39601,121,38809,5329,32041)
    vector<int> QS={128,49,25,39601,121,38809,5329,32041};
    vector<vector<PQE>> comps;
    for(int qi=0; qi<(int)QS.size(); qi++){
        int q=QS[qi];
        vector<pair<int,int>> G;
        if(q==128){ for(int a=0;a<8;a++) for(int b=0;b<16;b++) G.push_back({16*a,8*b}); }
        else { int p=(int)round(sqrt((double)q)); for(int a=0;a<p;a++) for(int b=0;b<p;b++) G.push_back({p*a,p*b}); }
        set<array<int,36>> patterns;
        for(auto A:G){
            Seq s; auto cur=A;
            for(int i=0;i<36;i++){ s.v[i]=trp(cur,q); cur=mulp(cur,{3,2},q); }
            array<int,36> pat; map<int,int> lab;
            for(int i=0;i<36;i++){ if(!lab.count(s.v[i])) lab[s.v[i]]=(int)lab.size(); pat[i]=lab[s.v[i]]; }
            patterns.insert(pat);
        }
        vector<PQE> pq;
        for(auto &P: patterns){
            map<array<int,36>, Mask72> m;
            for(int ti=0; ti<72; ti++){
                array<int,36> Q; for(int i=0;i<36;i++) Q[i]=P[DIH[ti][i]];
                m[Q].first |= (ti<64 ? (1ULL<<ti) : 0);
                if(ti>=64) m[Q].second |= (1ULL<<(ti-64));
            }
            for(auto &kv: m){
                PQE e; e.P=P; e.Q=kv.first; e.mask=kv.second;
                for(int i=0;i<36;i++){ unsigned long long bits=0; for(int j=0;j<36;j++) if(P[j]==kv.first[i]) bits|=(1ULL<<j); e.allow[i]=bits; }
                pq.push_back(e);
            }
        }
        printf("q=%d patterns=%zu PQ=%zu\n", q, patterns.size(), pq.size());
        comps.push_back(move(pq));
    }
    int NC=comps.size();
    long long nodes=0, pruned=0;
    vector<int> choice(NC,-1);
    set<tuple<int,unsigned long long,unsigned long long,string>> dead;
    auto start = chrono::steady_clock::now();
    function<bool(int, Mask72, array<unsigned long long,36>)> dfs = [&](int k, Mask72 curMask, array<unsigned long long,36> allow)->bool{
        nodes++;
        if(nodes%1000000==0){
            auto now=chrono::steady_clock::now();
            printf("... nodes=%lld level=%d elapsed=%.0fs\n", nodes, k, chrono::duration<double>(now-start).count());
            fflush(stdout);
        }
        if(k==NC){
            if(mask_zero(curMask)){
                printf("*** PHASE1 FAILURE *** choices:"); for(int c: choice) printf(" %d", c); printf("\n");
                return true;
            }
            return false;
        }
        // memo dead
        string key; key.reserve(36*8);
        for(int i=0;i<36;i++){ unsigned long long x=allow[i]; for(int b=0;b<8;b++) key.push_back(char(x>>(8*b))); }
        auto tk = make_tuple(k, curMask.first, curMask.second, key);
        if(dead.count(tk)){ pruned++; return false; }
        for(int ei=0; ei<(int)comps[k].size(); ei++){
            auto &e = comps[k][ei];
            Mask72 nm = mask_and(curMask, e.mask);
            array<unsigned long long,36> na;
            bool ok=true;
            for(int i=0;i<36;i++){ na[i]=allow[i]&e.allow[i]; if(!na[i]){ ok=false; break; } }
            if(!ok) continue;
            if(!has_match(na)) continue;
            choice[k]=ei;
            if(dfs(k+1, nm, na)) return true;
        }
        dead.insert(tk);
        return false;
    };
    Mask72 full{0xFFFFFFFFFFFFFFFFULL, 0xFFULL};
    array<unsigned long long,36> allow0; allow0.fill((36==64?~0ULL: ((1ULL<<36)-1)));
    bool found = dfs(0, full, allow0);
    auto now=chrono::steady_clock::now();
    printf("Phase1 done: found=%d nodes=%lld pruned_memo=%lld dead_states=%zu elapsed=%.0fs\n",
           (int)found, nodes, pruned, dead.size(), chrono::duration<double>(now-start).count());
    return 0;
}
