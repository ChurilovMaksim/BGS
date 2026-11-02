// Wave 32, task 5, step A: per-component classes/patterns at m=60.
// For each prime-power component q of D_60, enumerate genuine sequences
// S(A) = (Tr(A*alpha^i))_{i in Z/60}, alpha = 3+2*sqrt2, Tr(a+b*sqrt2)=2a,
// and check: every sequence in a value-multiset class is a dihedral image
// of the class representative (the property the COH reduction needs).
// Also dumps distinct patterns per component for the DFS stage.
#include <bits/stdc++.h>
using namespace std;
const int M = 60, NT = 120;
using Seq = array<int,60>;
using Pat = array<unsigned char,60>;
struct Mask120 { uint64_t lo=0, hi=0; };
static inline pair<int,int> mulp(pair<int,int> a, pair<int,int> b, int q){
    return {(int)(((long long)a.first*b.first + 2LL*a.second*b.second)%q),
            (int)(((long long)a.first*b.second + (long long)a.second*b.first)%q)};
}
static inline string seqkey(const Seq& s){
    string k; k.resize(60*sizeof(int));
    memcpy(&k[0], s.data(), 60*sizeof(int));
    return k;
}
static inline string patkey(const Pat& p){
    string k; k.resize(60);
    for(int i=0;i<60;i++) k[i]=char(p[i]);
    return k;
}
int main(){
    vector<array<int,60>> DIH;
    for(int k=0;k<60;k++){
        array<int,60> sh, rf;
        for(int i=0;i<60;i++){ sh[i]=(i+k)%60; rf[i]=(((-i+k)%60)+60)%60; }
        DIH.push_back(sh); DIH.push_back(rf);
    }
    sort(DIH.begin(), DIH.end()); DIH.erase(unique(DIH.begin(), DIH.end()), DIH.end());
    printf("dihedral maps: %zu (expect 120)\n", DIH.size()); fflush(stdout);
    // (q, pe) with G = pe*(R/peR); 128 handled specially
    struct Comp{int q; int pe;};
    vector<Comp> comps = {{128,0},{81,9},{625,25},{49,7},{121,11},{361,19},
                          {841,29},{923521,961},{1681,41},{3481,59},{72361,269},
                          {361201,601},{5202961,2281}};
    for(auto [q, pe] : comps){
        auto t0 = chrono::steady_clock::now();
        vector<pair<int,int>> G;
        if(q==128){ for(int a=0;a<8;a++) for(int b=0;b<16;b++) G.push_back({16*a,8*b}); }
        else { for(int a=0;a<pe;a++) for(int b=0;b<pe;b++) G.push_back({pe*a,pe*b}); }
        struct ClassInfo{
            Seq rep; Pat reppat; Seq sorted;
            unordered_map<string, Mask120> img; // image pattern -> tau mask
            long long size=0;
        };
        vector<ClassInfo> classes;
        unordered_map<string,int> classBySorted;
        unordered_set<string> patterns;
        long long nondih=0, nondih_patmiss=0;
        vector<Seq> nondih_examples;
        vector<int> nondih_class;
        long long done=0;
        for(auto A : G){
            Seq v; auto cur=A;
            for(int i=0;i<60;i++){ v[i]=(2*cur.first)%q; cur=mulp(cur,{3,2},q); }
            // sort pairs (value, index) -> sorted values + pattern labels
            array<pair<int,int>,60> vp;
            for(int i=0;i<60;i++) vp[i]={v[i],i};
            sort(vp.begin(), vp.end());
            Seq sorted; Pat pat; int lab=0;
            for(int k=0;k<60;k++){
                sorted[k]=vp[k].first;
                if(k>0 && vp[k].first!=vp[k-1].first) lab++;
                pat[vp[k].second]=(unsigned char)lab;
            }
            patterns.insert(patkey(pat));
            string sk = seqkey(sorted);
            auto it = classBySorted.find(sk);
            int ci;
            if(it==classBySorted.end()){
                ci = (int)classes.size();
                classBySorted[sk]=ci;
                ClassInfo C; C.rep=v; C.reppat=pat; C.sorted=sorted; C.size=0;
                // image-pattern map for representative: canonical pattern of
                // the transported sequence tau(R) (labels recomputed on the
                // transported values, NOT transported labels)
                for(int ti=0; ti<120; ti++){
                    Seq tv; for(int i=0;i<60;i++) tv[i]=v[DIH[ti][i]];
                    array<pair<int,int>,60> tp;
                    for(int i=0;i<60;i++) tp[i]={tv[i],i};
                    sort(tp.begin(), tp.end());
                    Pat Q; int lb=0;
                    for(int k=0;k<60;k++){
                        if(k>0 && tp[k].first!=tp[k-1].first) lb++;
                        Q[tp[k].second]=(unsigned char)lb;
                    }
                    string qk = patkey(Q);
                    auto &mk = C.img[qk];
                    if(ti<64) mk.lo |= (1ULL<<ti); else mk.hi |= (1ULL<<(ti-64));
                }
                classes.push_back(move(C));
            } else ci = it->second;
            ClassInfo &C = classes[ci];
            C.size++;
            if(!(v==C.rep)){
                // dihedral membership via pattern-image map + value check
                auto itm = C.img.find(patkey(pat));
                bool ok=false;
                if(itm!=C.img.end()){
                    Mask120 mk = itm->second;
                    for(int ti=0; ti<120 && !ok; ti++){
                        bool has = (ti<64) ? (mk.lo>>ti & 1ULL) : (mk.hi>>(ti-64) & 1ULL);
                        if(!has) continue;
                        bool eq=true;
                        for(int i=0;i<60;i++) if(v[i]!=C.rep[DIH[ti][i]]){ eq=false; break; }
                        if(eq) ok=true;
                    }
                } else nondih_patmiss++;
                if(!ok){
                    nondih++;
                    if(nondih_examples.size()<3){ nondih_examples.push_back(v); nondih_class.push_back(ci); }
                }
            }
            if(++done % 1000000 == 0){ printf("  q=%d ... %lld/%zu\n", q, done, G.size()); fflush(stdout); }
        }
        // PQ count from distinct patterns
        long long pq=0;
        for(auto &pk : patterns){
            Pat P; for(int i=0;i<60;i++) P[i]=(unsigned char)pk[i];
            unordered_set<string> imgs;
            for(int ti=0; ti<120; ti++){
                Pat Q; for(int i=0;i<60;i++) Q[i]=P[DIH[ti][i]];
                imgs.insert(patkey(Q));
            }
            pq += (long long)imgs.size();
        }
        // class size distribution (top sizes)
        vector<long long> sizes;
        for(auto &C: classes) sizes.push_back(C.size);
        sort(sizes.begin(), sizes.end(), greater<long long>());
        auto t1 = chrono::steady_clock::now();
        printf("q=%d |G|=%zu patterns=%zu classes=%zu PQ=%lld nondih=%lld (patmiss=%lld) elapsed=%.0fs\n",
               q, G.size(), patterns.size(), classes.size(), pq, nondih, nondih_patmiss,
               chrono::duration<double>(t1-t0).count());
        printf("   class sizes (top 12):");
        for(size_t i=0;i<sizes.size() && i<12;i++) printf(" %lld", sizes[i]);
        printf("\n");
        for(size_t e=0;e<nondih_examples.size();e++){
            printf("   nondih ex class=%d seq:", nondih_class[e]);
            for(int i=0;i<60;i++) printf(" %d", nondih_examples[e][i]);
            printf("\n   rep seq:");
            for(int i=0;i<60;i++) printf(" %d", classes[nondih_class[e]].rep[i]);
            printf("\n");
        }
        fflush(stdout);
        // dump patterns
        string fn = "wave32_COH_m60_patterns_q" + to_string(q) + ".bin";
        FILE* f = fopen(fn.c_str(), "wb");
        for(auto &pk : patterns) fwrite(pk.data(), 1, 60, f);
        fclose(f);
        printf("   dumped %zu patterns to %s\n", patterns.size(), fn.c_str()); fflush(stdout);
    }
    return 0;
}
