// Wave 32, task 5: unified COH DFS at m=60.
// Components: pattern components (classes = dihedral images, verified in
// step A) contribute collapsed (mask, allow) options; collapse components
// (81, 625) contribute (T, Allow) keys from class pairs, with ShiftSet
// read from an optional file (default: {zero sequence} = exact equality).
// A leaf with empty mask + a full matching = a COH failure (Stage 1:
// modulo shadow; 0 failures with ShiftSet={0} implies COH outright).
// Search is parallel over first-component options; memo keys are
// (level, mask, 256-bit allow hash) -- collision risk ~2^-256.
#include <bits/stdc++.h>
using namespace std;
const int M = 60, NT = 120;
struct Mask120 { uint64_t lo=0, hi=0;
    bool zero() const { return lo==0 && hi==0; }
    bool operator==(const Mask120& o) const { return lo==o.lo && hi==o.hi; }
};
static inline Mask120 mand(Mask120 a, Mask120 b){ return {a.lo&b.lo, a.hi&b.hi}; }
struct Option { Mask120 mask; array<uint64_t,60> allow; };
struct CompOpts { int q; vector<Option> opts; string kind; };
static vector<array<int,60>> DIH;
static bool has_match(const array<uint64_t,60>& allow){
    int matchR[60]; fill(begin(matchR), end(matchR), -1);
    function<bool(int, bool*)> bpm = [&](int u, bool* seen)->bool{
        uint64_t bits = allow[u];
        for(int v=0; v<60; v++) if(bits>>v & 1ULL){
            if(seen[v]) continue; seen[v]=true;
            if(matchR[v]<0 || bpm(matchR[v], seen)){ matchR[v]=u; return true; }
        }
        return false;
    };
    for(int u=0; u<60; u++){ bool seen[60]={0}; if(!bpm(u, seen)) return false; }
    return true;
}
static uint64_t mix64(uint64_t x){
    x += 0x9e3779b97f4a7c15ULL; x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
    x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL; return x ^ (x >> 31);
}
struct MemoKey { int lvl; uint64_t mlo, mhi, h1, h2;
    bool operator==(const MemoKey& o) const { return lvl==o.lvl && mlo==o.mlo && mhi==o.mhi && h1==o.h1 && h2==o.h2; }
};
struct MemoHash { size_t operator()(MemoKey const& k) const {
    uint64_t h = mix64((uint64_t)k.lvl ^ k.mlo ^ (k.h1<<1)); h ^= mix64(k.mhi + k.h2);
    return (size_t)h; } };
static vector<CompOpts> comps;
static atomic<long long> nodes{0};
static atomic<bool> found{false};
static mutex print_mu;
static vector<int> fail_choice;
static array<uint64_t,60> fail_allow;
static string optkey(const Option& o){
    string k; k.resize(16+60*8);
    memcpy(&k[0], &o.mask.lo, 8); memcpy(&k[8], &o.mask.hi, 8);
    memcpy(&k[16], o.allow.data(), 60*8);
    return k;
}
static void dfs(int lvl, Mask120 mask, array<uint64_t,60> allow,
                vector<int>& choice, unordered_set<MemoKey,MemoHash>& dead){
    if(found.load()) return;
    long long n = ++nodes;
    if(n % 20000000 == 0){
        lock_guard<mutex> lk(print_mu);
        printf("... nodes=%lld\n", n); fflush(stdout);
    }
    if(lvl == (int)comps.size()){
        if(mask.zero()){
            lock_guard<mutex> lk(print_mu);
            if(!found.load()){
                found.store(true); fail_choice = choice; fail_allow = allow;
                printf("*** FAILURE *** choices:"); for(int c: choice) printf(" %d", c); printf("\n");
            }
        }
        return;
    }
    uint64_t h1=1469598103934665603ULL, h2=1099511628211ULL;
    for(int i=0;i<60;i++){ h1 ^= mix64(allow[i]+0x9e3779b97f4a7c15ULL+i); h1 *= 1099511628211ULL; h2 ^= mix64(allow[i]^0xdeadbeefdeadbeefULL); h2 *= 1469598103934665603ULL; }
    MemoKey mk{lvl, mask.lo, mask.hi, h1, h2};
    if(dead.count(mk)) return;
    for(int ei=0; ei<(int)comps[lvl].opts.size(); ei++){
        if(found.load()) return;
        const Option& o = comps[lvl].opts[ei];
        Mask120 nm = mand(mask, o.mask);
        array<uint64_t,60> na; bool ok=true;
        for(int i=0;i<60;i++){ na[i]=allow[i]&o.allow[i]; if(!na[i]){ ok=false; break; } }
        if(!ok) continue;
        if(!has_match(na)) continue;
        choice[lvl]=ei;
        dfs(lvl+1, nm, na, choice, dead);
        if(found.load()) return;
    }
    dead.insert(mk);
}
static vector<array<unsigned char,60>> read_patterns(const string& fn){
    FILE* f=fopen(fn.c_str(),"rb"); if(!f){ printf("cannot open %s\n", fn.c_str()); exit(1); }
    vector<array<unsigned char,60>> out;
    array<unsigned char,60> buf;
    while(fread(buf.data(),1,60,f)==60) out.push_back(buf);
    fclose(f); return out;
}
static bool injective_pat(const array<unsigned char,60>& P){
    bool seen[60]={0};
    for(int i=0;i<60;i++){ if(seen[P[i]]) return false; seen[P[i]]=true; }
    return true;
}
int main(int argc, char** argv){
    // usage: dfs [shiftfile81] [shiftfile625] [nthreads]
    string shiftfile81 = argc>1 ? argv[1] : "";
    string shiftfile625 = argc>2 ? argv[2] : "";
    int nthreads = argc>3 ? atoi(argv[3]) : 4;
    for(int k=0;k<60;k++){
        array<int,60> sh, rf;
        for(int i=0;i<60;i++){ sh[i]=(i+k)%60; rf[i]=(((-i+k)%60)+60)%60; }
        DIH.push_back(sh); DIH.push_back(rf);
    }
    sort(DIH.begin(), DIH.end()); DIH.erase(unique(DIH.begin(), DIH.end()), DIH.end());
    assert(DIH.size()==120);
    // ---- pattern components ----
    vector<int> pat_qs = {128,49,121,361,841,1681,3481,72361,361201,923521,5202961};
    for(int q : pat_qs){
        auto pats = read_patterns("wave32_COH_m60_patterns_q"+to_string(q)+".bin");
        unordered_map<string, Option> optmap;
        bool has_inj=false; long long ninj=0;
        for(auto& P : pats){
            if(injective_pat(P)){ has_inj=true; continue; }
            ninj++;
            map<string, Mask120> byQ;
            for(int ti=0; ti<120; ti++){
                array<unsigned char,60> Q; for(int i=0;i<60;i++) Q[i]=P[DIH[ti][i]];
                string qk; qk.resize(60); for(int i=0;i<60;i++) qk[i]=char(Q[i]);
                auto& mk = byQ[qk];
                if(ti<64) mk.lo |= (1ULL<<ti); else mk.hi |= (1ULL<<(ti-64));
            }
            for(auto& kv : byQ){
                Option o; o.mask = kv.second;
                for(int i=0;i<60;i++){ uint64_t bits=0;
                    for(int j=0;j<60;j++) if(P[j]==(unsigned char)kv.first[i]) bits|=(1ULL<<j);
                    o.allow[i]=bits; }
                optmap[optkey(o)] = o;
            }
        }
        if(has_inj){
            for(int ti=0; ti<120; ti++){
                Option o; o.mask = {ti<64 ? (1ULL<<ti) : 0ULL, ti>=64 ? (1ULL<<(ti-64)) : 0ULL};
                for(int i=0;i<60;i++) o.allow[i]=(1ULL<<DIH[ti][i]);
                optmap[optkey(o)] = o;
            }
        }
        CompOpts C; C.q=q; C.kind="pattern";
        for(auto& kv : optmap) C.opts.push_back(kv.second);
        printf("pattern q=%d pats=%zu noninj=%lld collapsed_opts=%zu\n", q, pats.size(), ninj, C.opts.size()); fflush(stdout);
        comps.push_back(move(C));
    }
    // ---- collapse components ----
    // Per-component ShiftSet: set of 60-int sequences (default: zero only)
    auto load_shifts = [](const string& fn){
        unordered_set<string> ss;
        array<int,60> z; z.fill(0);
        string k0; k0.resize(60*sizeof(int)); memcpy(&k0[0], z.data(), 60*sizeof(int)); ss.insert(k0);
        if(!fn.empty()){
            FILE* f=fopen(fn.c_str(),"rb"); if(!f){ printf("cannot open shiftfile %s\n", fn.c_str()); exit(1); }
            array<int,60> buf;
            while(fread(buf.data(),sizeof(int),60,f)==60){
                string k; k.resize(60*sizeof(int)); memcpy(&k[0], buf.data(), 60*sizeof(int)); ss.insert(k);
            }
            fclose(f);
        }
        return ss;
    };
    unordered_map<int, unordered_set<string>> shiftsets;
    shiftsets[81] = load_shifts(shiftfile81);
    shiftsets[625] = load_shifts(shiftfile625);
    printf("ShiftSet sizes: 81=%zu 625=%zu\n", shiftsets[81].size(), shiftsets[625].size()); fflush(stdout);
    auto mulp = [](pair<int,int> a, pair<int,int> b, int q){
        return pair<int,int>{(int)(((long long)a.first*b.first + 2LL*a.second*b.second)%q),
            (int)(((long long)a.first*b.second + (long long)a.second*b.first)%q)}; };
    vector<pair<int, vector<pair<int,int>>>> collapse = {{81, {}}, {625, {}}};
    // genuine sets
    vector<pair<int,int>> G81, G625;
    for(int a=0;a<9;a++) for(int b=0;b<9;b++) G81.push_back({9*a,9*b});
    for(int a=0;a<25;a++) for(int b=0;b<25;b++) G625.push_back({25*a,25*b});
    vector<vector<pair<int,int>>> Gs = {G81, G625};
    vector<int> qs = {81, 625};
    for(size_t ci=0; ci<qs.size(); ci++){
        int q = qs[ci];
        auto& G = Gs[ci];
        map<string, vector<array<int,60>>> classes;
        for(auto A : G){
            array<int,60> v; auto cur=A;
            for(int i=0;i<60;i++){ v[i]=(2*cur.first)%q; cur=mulp(cur,{3,2},q); }
            array<int,60> srt=v; sort(srt.begin(), srt.end());
            string k; k.resize(60*sizeof(int)); memcpy(&k[0], srt.data(), 60*sizeof(int));
            classes[k].push_back(v);
        }
        for(auto& kv : classes){ auto& vec=kv.second; sort(vec.begin(), vec.end()); vec.erase(unique(vec.begin(), vec.end()), vec.end()); }
        unordered_map<string, Option> optmap;
        unordered_map<string, pair<array<int,60>,array<int,60>>> optrep;
        long long pairs=0;
        auto& shiftset = shiftsets[q];
        for(auto& kv : classes){
            auto& vec = kv.second;
            for(auto& S : vec) for(auto& Sp : vec){
                pairs++;
                Mask120 T{0,0};
                for(int ti=0; ti<120; ti++){
                    array<int,60> diff;
                    for(int i=0;i<60;i++){ diff[i]=((Sp[i]-S[DIH[ti][i]])%q+q)%q; }
                    string dk; dk.resize(60*sizeof(int)); memcpy(&dk[0], diff.data(), 60*sizeof(int));
                    if(shiftset.count(dk)){ if(ti<64) T.lo|=(1ULL<<ti); else T.hi|=(1ULL<<(ti-64)); }
                }
                Option o; o.mask=T;
                for(int i=0;i<60;i++){ uint64_t bits=0; for(int j=0;j<60;j++) if(S[j]==Sp[i]) bits|=(1ULL<<j); o.allow[i]=bits; }
                string ok = optkey(o);
                if(!optmap.count(ok)){ optmap[ok]=o; optrep[ok]={S,Sp}; }
            }
        }
        CompOpts C; C.q=q; C.kind="collapse";
        for(auto& kv : optmap) C.opts.push_back(kv.second);
        printf("collapse q=%d classes=%zu pairs=%lld collapsed_keys=%zu\n", q, classes.size(), pairs, C.opts.size()); fflush(stdout);
        // save representative pairs for failure analysis
        string fn = "wave32_COH_m60_collapse_keys_q"+to_string(q)+".txt";
        FILE* f=fopen(fn.c_str(),"w");
        int idx=0;
        for(auto& kv : optmap){
            auto& pr = optrep[kv.first];
            fprintf(f, "key %d mask=%llx:%llx S=", idx, (unsigned long long)kv.second.mask.lo, (unsigned long long)kv.second.mask.hi);
            for(int i=0;i<60;i++) fprintf(f, " %d", pr.first[i]);
            fprintf(f, " Sp=");
            for(int i=0;i<60;i++) fprintf(f, " %d", pr.second[i]);
            fprintf(f, "\n"); idx++;
        }
        fclose(f);
        comps.push_back(move(C));
    }
    // order by option count ascending
    sort(comps.begin(), comps.end(), [](const CompOpts& a, const CompOpts& b){ return a.opts.size() < b.opts.size(); });
    printf("DFS order:"); for(auto& c : comps) printf(" %d(%s,%zu)", c.q, c.kind.c_str(), c.opts.size()); printf("\n"); fflush(stdout);
    // parallel over first-component options
    auto t0 = chrono::steady_clock::now();
    atomic<int> nextidx{0};
    int nfirst = comps[0].opts.size();
    vector<thread> workers;
    for(int w=0; w<nthreads; w++){
        workers.emplace_back([&](){
            unordered_set<MemoKey,MemoHash> dead;
            vector<int> choice(comps.size(), -1);
            while(!found.load()){
                int fi = nextidx.fetch_add(1);
                if(fi >= nfirst) break;
                const Option& o = comps[0].opts[fi];
                array<uint64_t,60> allow0; allow0.fill((60==64?~0ULL: ((1ULL<<60)-1)));
                // careful: (1ULL<<60)-1 fits; use explicit
                allow0.fill(0x0FFFFFFFFFFFFFFFULL);
                Mask120 m0{0xFFFFFFFFFFFFFFFFULL, 0x00FFFFFFFFFFFFFFULL};
                Mask120 nm = mand(m0, o.mask);
                array<uint64_t,60> na; bool ok=true;
                for(int i=0;i<60;i++){ na[i]=allow0[i]&o.allow[i]; if(!na[i]){ ok=false; break; } }
                if(!ok) continue;
                if(!has_match(na)) continue;
                choice[0]=fi;
                dfs(1, nm, na, choice, dead);
            }
        });
    }
    for(auto& th : workers) th.join();
    auto t1 = chrono::steady_clock::now();
    printf("DFS done: found=%d nodes=%lld elapsed=%.0fs\n", (int)found.load(), nodes.load(), chrono::duration<double>(t1-t0).count());
    if(found.load()){
        printf("fail choices per DFS order:"); for(int c: fail_choice) printf(" %d", c); printf("\n");
        printf("fail matching sigma (left i -> right matchR):\n");
        // reconstruct matching from fail_allow
        int matchR[60]; fill(begin(matchR), end(matchR), -1);
        function<bool(int, bool*)> bpm = [&](int u, bool* seen)->bool{
            uint64_t bits = fail_allow[u];
            for(int v=0; v<60; v++) if(bits>>v & 1ULL){
                if(seen[v]) continue; seen[v]=true;
                if(matchR[v]<0 || bpm(matchR[v], seen)){ matchR[v]=u; return true; }
            }
            return false;
        };
        for(int u=0; u<60; u++){ bool seen[60]={0}; bpm(u, seen); }
        for(int v=0; v<60; v++) printf(" %d", matchR[v]);
        printf("\n");
    }
    return 0;
}
