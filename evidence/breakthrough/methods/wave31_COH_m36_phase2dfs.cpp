#include <bits/stdc++.h>
using namespace std;
const int M=36;
pair<int,int> mulp(pair<int,int> a, pair<int,int> b, int q){
    return {(int)(((long long)a.first*b.first + 2LL*a.second*b.second)%q),
            (int)(((long long)a.first*b.second + (long long)a.second*b.first)%q)};
}
int trp(pair<int,int> a, int q){ return (2*a.first)%q; }
struct Seq { array<int,36> v; };
bool operator<(Seq const& a, Seq const& b){ return a.v<b.v; }
bool operator==(Seq const& a, Seq const& b){ return a.v==b.v; }
using Mask72 = pair<unsigned long long, unsigned long long>;
Mask72 mask_and(Mask72 a, Mask72 b){ return {a.first&b.first, a.second&b.second}; }
bool mask_zero(Mask72 a){ return a.first==0 && a.second==0; }
struct PQE { array<int,36> P, Q; Mask72 mask; array<unsigned long long,36> allow; };
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
struct Key { unsigned long long tlo, thi; array<unsigned long long,36> allow; };
int main(int argc, char** argv){
    int nthreads = argc>1 ? atoi(argv[1]) : 4;
    int chunk_start = argc>2 ? atoi(argv[2]) : 0;
    int chunk_end = argc>3 ? atoi(argv[3]) : 1000000000;
    vector<array<int,36>> DIH;
    for(int k=0;k<36;k++){
        array<int,36> sh, rf;
        for(int i=0;i<36;i++){ sh[i]=(i+k)%36; rf[i]=((-i+k)%36+36)%36; }
        DIH.push_back(sh); DIH.push_back(rf);
    }
    sort(DIH.begin(), DIH.end()); DIH.erase(unique(DIH.begin(), DIH.end()), DIH.end());
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
                if(ti<64) m[Q].first |= (1ULL<<ti); else m[Q].second |= (1ULL<<(ti-64));
            }
            for(auto &kv: m){
                PQE e; e.P=P; e.Q=kv.first; e.mask=kv.second;
                for(int i=0;i<36;i++){ unsigned long long bits=0; for(int j=0;j<36;j++) if(P[j]==kv.first[i]) bits|=(1ULL<<j); e.allow[i]=bits; }
                pq.push_back(e);
            }
        }
        comps.push_back(move(pq));
    }
    // load keys
    vector<Key> keys;
    FILE* f=fopen("/tmp/coh36_properkeys2.bin","rb");
    if(!f){ printf("no keys file\n"); return 1; }
    while(true){
        Key k; if(fread(&k.tlo,8,1,f)!=1) break; if(fread(&k.thi,8,1,f)!=1) break;
        unsigned long long buf[36];
        if(fread(buf,8,36,f)!=36) break;
        for(int i=0;i<36;i++) k.allow[i]=buf[i];
        keys.push_back(k);
    }
    fclose(f);
    printf("keys=%zu range=[%d,%d) threads=%d\n", keys.size(), chunk_start, chunk_end, nthreads);
    int NC=comps.size();
    atomic<long long> total_nodes{0};
    atomic<int> found_flag{0};
    mutex print_mu;
    auto t0 = chrono::steady_clock::now();
    // per-thread worker over key indices
    vector<thread> ths;
    int lo = max(0, chunk_start), hi = min((int)keys.size(), chunk_end);
    for(int tid=0; tid<nthreads; tid++){
        ths.emplace_back([&, tid](){
            vector<int> choice(NC,-1);
            for(int ki=lo+tid; ki<hi; ki+=nthreads){
                if(found_flag) return;
                Key &K = keys[ki];
                Mask72 initT{K.tlo, K.thi};
                // quick check: initial Allow must have perfect matching (it does by construction: sigma exists)
                set<tuple<int,unsigned long long,unsigned long long,string>> dead;
                long long nodes=0;
                function<bool(int, Mask72, array<unsigned long long,36>)> dfs = [&](int k, Mask72 curMask, array<unsigned long long,36> allow)->bool{
                    nodes++;
                    if(k==NC){
                        if(mask_zero(curMask)) return true;
                        return false;
                    }
                    string keystr; keystr.reserve(288);
                    for(int i=0;i<36;i++){ unsigned long long x=allow[i]; for(int b=0;b<8;b++) keystr.push_back(char(x>>(8*b))); }
                    auto tk = make_tuple(k, curMask.first, curMask.second, keystr);
                    if(dead.count(tk)) return false;
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
                bool found = dfs(0, initT, K.allow);
                total_nodes += nodes;
                if(found){
                    lock_guard<mutex> lk(print_mu);
                    printf("*** PHASE2 FAILURE key=%d choices:", ki);
                    for(int c: choice) printf(" %d", c);
                    printf("\n"); fflush(stdout);
                    found_flag=1; return;
                }
            }
        });
    }
    for(auto &t: ths) t.join();
    auto t1 = chrono::steady_clock::now();
    printf("Phase2 DFS done: found=%d total_nodes=%lld elapsed=%.0fs\n", (int)found_flag.load(), total_nodes.load(), chrono::duration<double>(t1-t0).count());
    return 0;
}
