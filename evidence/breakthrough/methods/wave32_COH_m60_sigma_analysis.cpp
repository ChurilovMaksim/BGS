// Wave 32, task 5: value-level analysis of the DFS failure candidate.
// sigma(i) = 11*i+9 mod 60 (affine multiplier map from the DFS failure).
// For each component q: enumerate genuine sequences S, compute S' = sigma(S)
// (S'[i] = S[sigma(i)]), test S' genuine (solver for odd q, brute force for
// 128), and record the tau-mask of each compatible pair:
//   pattern components: {tau : S' = tau(S)} exactly;
//   collapse components: {tau : S' - tau(S) in ShiftSet} for the validated
//   shadow AND for the superset shadow (robustness).
// Then search combinations of per-component masks with empty intersection.
#include <bits/stdc++.h>
using namespace std;
const int M = 60, NT = 120;
static vector<array<int,60>> DIH;
static inline pair<int,int> mulp(pair<int,int> a, pair<int,int> b, int q){
    return {(int)(((long long)a.first*b.first + 2LL*a.second*b.second)%q),
            (int)(((long long)a.first*b.second + (long long)a.second*b.first)%q)};
}
static int modinv(int a, int q){ // q odd prime power here; brute force
    a%=q; for(int x=1;x<q;x++) if((a*x)%q==1) return x; return -1;
}
struct Mask120 { uint64_t lo=0, hi=0;
    bool zero() const { return lo==0 && hi==0; }
    bool has(int ti) const { return ti<64 ? (lo>>ti & 1ULL) : (hi>>(ti-64) & 1ULL); }
    string str() const { char b[64]; snprintf(b,64,"%llx:%llx",(unsigned long long)lo,(unsigned long long)hi); return b; }
};
int main(){
    for(int k=0;k<60;k++){
        array<int,60> sh, rf;
        for(int i=0;i<60;i++){ sh[i]=(i+k)%60; rf[i]=(((-i+k)%60)+60)%60; }
        DIH.push_back(sh); DIH.push_back(rf);
    }
    sort(DIH.begin(), DIH.end()); DIH.erase(unique(DIH.begin(), DIH.end()), DIH.end());
    assert(DIH.size()==120);
    int sigma[60];
    for(int i=0;i<60;i++) sigma[i]=(11*i+9)%60;
    // shift sets: validated (file) and superset (computed inline)
    auto load_shiftfile = [](const string& fn){
        unordered_set<string> ss; FILE* f=fopen(fn.c_str(),"rb");
        if(!f){ printf("cannot open %s\n", fn.c_str()); exit(1); }
        array<int,60> buf;
        while(fread(buf.data(),sizeof(int),60,f)==60){ string k; k.resize(240); memcpy(&k[0], buf.data(), 240); ss.insert(k); }
        fclose(f); return ss;
    };
    unordered_map<int, unordered_set<string>> shift_val, shift_super;
    shift_val[81] = load_shiftfile("wave32_shift81.bin");
    shift_val[625] = load_shiftfile("wave32_shift625.bin");
    // superset shadows: multiples of 9 at 81, multiples of 25 at 625
    for(auto [q, step, lim] : vector<tuple<int,int,int>>{{81,9,9},{625,25,25}}){
        unordered_set<string> ss;
        for(int a=0;a<lim;a++) for(int b=0;b<lim;b++){
            pair<int,int> cur{(step*a)%q,(step*b)%q}; array<int,60> v;
            for(int i=0;i<60;i++){ v[i]=(2*cur.first)%q; cur=mulp(cur,{3,2},q); }
            string k; k.resize(240); memcpy(&k[0], v.data(), 240); ss.insert(k);
        }
        shift_super[q]=move(ss);
        printf("q=%d validated shifts=%zu superset shifts=%zu\n", q, shift_val[q].size(), shift_super[q].size()); fflush(stdout);
    }
    struct CompRes { int q; long long compat=0; map<string, long long> maskcount_val, maskcount_super;
                     map<string, pair<array<int,60>,array<int,60>>> ex_val;
                     map<string, pair<pair<int,int>,pair<int,int>>> exA_val; };
    vector<CompRes> results;
    vector<tuple<int,int>> comps = {{128,0},{81,9},{625,25},{49,7},{121,11},{361,19},{841,29},{923521,961},{1681,41},{3481,59},{72361,269},{361201,601},{5202961,2281}};
    // precompute 128 genuine sequences set
    unordered_set<string> seq128;
    {
        for(int a=0;a<8;a++) for(int b=0;b<16;b++){
            pair<int,int> A{16*a,8*b}; array<int,60> v; auto cur=A;
            for(int i=0;i<60;i++){ v[i]=(2*cur.first)%128; cur=mulp(cur,{3,2},128); }
            string k; k.resize(240); memcpy(&k[0], v.data(), 240); seq128.insert(k);
        }
    }
    for(auto [q, pe] : comps){
        CompRes R; R.q=q;
        vector<pair<int,int>> G;
        if(q==128){ for(int a=0;a<8;a++) for(int b=0;b<16;b++) G.push_back({16*a,8*b}); }
        else { for(int a=0;a<pe;a++) for(int b=0;b<pe;b++) G.push_back({pe*a,pe*b}); }
        int inv2 = (q==128? -1 : modinv(2,q));
        int inv4 = (q==128? -1 : modinv(4,q));
        bool collapse = (q==81 || q==625);
        for(auto A : G){
            array<int,60> S; auto cur=A;
            for(int i=0;i<60;i++){ S[i]=(2*cur.first)%q; cur=mulp(cur,{3,2},q); }
            array<int,60> Sp;
            for(int i=0;i<60;i++) Sp[i]=S[sigma[i]];
            // genuineness of Sp
            bool genuine=false;
            if(q==128){ string k; k.resize(240); memcpy(&k[0], Sp.data(), 240); genuine = seq128.count(k); }
            else {
                int ap = (Sp[0]*inv2)%q;
                int bp = (((Sp[1]*inv2)%q - (3*ap)%q)%q+q)%q; bp=(bp*inv4)%q;
                pair<int,int> Ap{ap,bp}; auto cur2=Ap; genuine=true;
                for(int i=0;i<60;i++){ if((2*cur2.first)%q != Sp[i]){ genuine=false; break; } cur2=mulp(cur2,{3,2},q); }
            }
            if(!genuine) continue;
            R.compat++;
            Mask120 mv{0,0}, ms{0,0};
            for(int ti=0; ti<120; ti++){
                if(collapse){
                    array<int,60> diff;
                    for(int i=0;i<60;i++){ diff[i]=((Sp[i]-S[DIH[ti][i]])%q+q)%q; }
                    string dk; dk.resize(240); memcpy(&dk[0], diff.data(), 240);
                    if(shift_val[q].count(dk)){ if(ti<64) mv.lo|=(1ULL<<ti); else mv.hi|=(1ULL<<(ti-64)); }
                    if(shift_super[q].count(dk)){ if(ti<64) ms.lo|=(1ULL<<ti); else ms.hi|=(1ULL<<(ti-64)); }
                } else {
                    bool eq=true; for(int i=0;i<60;i++) if(Sp[i]!=S[DIH[ti][i]]){ eq=false; break; }
                    if(eq){ if(ti<64) mv.lo|=(1ULL<<ti); else mv.hi|=(1ULL<<(ti-64)); }
                }
            }
            if(!collapse) ms=mv;
            R.maskcount_val[mv.str()]++;
            if(!R.ex_val.count(mv.str())){
                R.ex_val[mv.str()]={S,Sp};
                // recover Ap from Sp
                pair<int,int> Ap{0,0};
                if(q==128){
                    for(auto A2 : G){ array<int,60> v; auto cu=A2;
                        for(int i=0;i<60;i++){ v[i]=(2*cu.first)%128; cu=mulp(cu,{3,2},128); }
                        if(v==Sp){ Ap=A2; break; } }
                } else {
                    int ap = (Sp[0]*inv2)%q;
                    int bp = (((Sp[1]*inv2)%q - (3*ap)%q)%q+q)%q; bp=(bp*inv4)%q;
                    Ap={ap,bp};
                }
                R.exA_val[mv.str()]={A,Ap};
            }
            if(collapse) R.maskcount_super[ms.str()]++;
        }
        printf("q=%d compat_pairs=%lld distinct_masks_val=%zu", q, R.compat, R.maskcount_val.size());
        if(collapse) printf(" distinct_masks_super=%zu", R.maskcount_super.size());
        printf("\n"); fflush(stdout);
        results.push_back(move(R));
    }
    // dump example pairs per (component, validated mask)
    for(auto& R : results){
        string fn = "wave32_COH_m60_sigma_examples_q"+to_string(R.q)+".txt";
        FILE* f=fopen(fn.c_str(),"w");
        for(auto& kv : R.exA_val){
            fprintf(f, "%s %d %d %d %d\n", kv.first.c_str(), kv.second.first.first, kv.second.first.second, kv.second.second.first, kv.second.second.second);
        }
        fclose(f);
        printf("dumped %zu example pairs for q=%d to %s\n", R.exA_val.size(), R.q, fn.c_str()); fflush(stdout);
    }
    // search combinations with empty intersection, for validated and superset masks
    for(int mode=0; mode<2; mode++){
        vector<map<string,long long>*> mcs;
        for(auto& R : results) mcs.push_back(mode==0 ? &R.maskcount_val : &R.maskcount_super);
        // branch and bound over components (order: fewest masks first)
        vector<int> ord(results.size()); iota(ord.begin(), ord.end(), 0);
        sort(ord.begin(), ord.end(), [&](int a, int b){ return mcs[a]->size() < mcs[b]->size(); });
        vector<string> choice(results.size());
        unordered_set<string> dead;
        function<bool(int, Mask120)> dfs = [&](int lvl, Mask120 cur)->bool{
            if(cur.zero()) return true;
            if(lvl==(int)ord.size()) return false;
            string dk = to_string(lvl)+":"+to_string(cur.lo)+":"+to_string(cur.hi);
            if(dead.count(dk)) return false;
            int ci = ord[lvl];
            for(auto& kv : *mcs[ci]){
                unsigned long long lo, hi; sscanf(kv.first.c_str(), "%llx:%llx", &lo, &hi);
                Mask120 nm{cur.lo & lo, cur.hi & hi};
                choice[ci]=kv.first;
                if(dfs(lvl+1, nm)) return true;
            }
            dead.insert(dk);
            return false;
        };
        Mask120 full{0xFFFFFFFFFFFFFFFFULL, 0x00FFFFFFFFFFFFFFULL};
        bool ok = dfs(0, full);
        printf("mode %s: empty-intersection combination %s\n", mode==0?"validated":"superset", ok?"FOUND":"none");
        if(ok){ for(size_t i=0;i<results.size();i++) printf("  q=%d mask=%s\n", results[i].q, choice[i].c_str()); }
        fflush(stdout);
    }
    return 0;
}
