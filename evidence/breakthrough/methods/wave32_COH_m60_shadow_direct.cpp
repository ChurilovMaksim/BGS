// Wave 32, task 5: direct shadow test at q=81 and q=625 (m=60).
// w is shadow iff sig_q(A+w) == sig_q(A) for every genuine A, where
// sig_q(A) = (sorted multiset over s in Z/15 of Tr(A*alpha^r*beta^s))_{r in Z/4},
// beta = alpha^4, alpha = 3+2*sqrt2.
#include <bits/stdc++.h>
using namespace std;
static inline pair<int,int> mulp(pair<int,int> a, pair<int,int> b, int q){
    return {(int)(((long long)a.first*b.first + 2LL*a.second*b.second)%q),
            (int)(((long long)a.first*b.second + (long long)a.second*b.first)%q)};
}
static inline int trp(pair<int,int> a, int q){ return (2*a.first)%q; }
static string sig_of(pair<int,int> A, int q, const vector<pair<int,int>>& alphas,
                     const vector<pair<int,int>>& betas){
    array<int,60> out; int k=0;
    for(int r=0;r<4;r++){
        auto base = mulp(A, alphas[r], q);
        array<int,15> vals;
        for(int s=0;s<15;s++) vals[s]=trp(mulp(base, betas[s], q), q);
        sort(vals.begin(), vals.end());
        for(int s=0;s<15;s++) out[k++]=vals[s];
    }
    string key; key.resize(60*sizeof(int)); memcpy(&key[0], out.data(), 60*sizeof(int));
    return key;
}
int main(){
    vector<pair<int,int>> alphas, betas;
    // alphas/betas depend on q; compute per q inside loop via powers
    struct Cand { string label; vector<pair<int,int>> ws; };
    vector<pair<int, vector<Cand>>> jobs;
    {
        vector<Cand> c81;
        vector<pair<int,int>> w1, w2;
        for(int a=0;a<3;a++) for(int b=0;b<3;b++) w1.push_back({(27*a)%81,(27*b)%81});
        for(int a=0;a<9;a++) for(int b=0;b<9;b++) w2.push_back({(9*a)%81,(9*b)%81});
        c81.push_back({"27D:R/3R", w1}); c81.push_back({"9D:R/9R", w2});
        jobs.push_back({81, c81});
    }
    {
        vector<Cand> c625;
        vector<pair<int,int>> w1, w2, w3;
        for(int a=0;a<5;a++) for(int b=0;b<5;b++) w1.push_back({(125*a)%625,(125*b)%625});
        for(int a=0;a<25;a++) for(int b=0;b<25;b++) w2.push_back({(125*a)%625,(125*b)%625});
        for(int a=0;a<5;a++) for(int b=0;b<5;b++) w3.push_back({(25*a)%625,(25*b)%625});
        c625.push_back({"125D:R/5R", w1}); c625.push_back({"125D:R/25R", w2}); c625.push_back({"25D:R/5R", w3});
        jobs.push_back({625, c625});
    }
    for(auto& [q, cands] : jobs){
        int pe = (q==81?9:25);
        vector<pair<int,int>> G;
        for(int a=0;a<pe;a++) for(int b=0;b<pe;b++) G.push_back({pe*a,pe*b});
        vector<pair<int,int>> al(4), be(15);
        al[0]={1,0}; for(int r=1;r<4;r++) al[r]=mulp(al[r-1],{3,2},q);
        be[0]={1,0}; auto beta=mulp(mulp(mulp({3,2},{3,2},q),{3,2},q),{3,2},q);
        for(int s=1;s<15;s++) be[s]=mulp(be[s-1],beta,q);
        unordered_map<string,string> sigG; // A-key -> sig
        for(auto A : G){
            string ak; ak.resize(8); memcpy(&ak[0], &A.first, 4); memcpy(&ak[4], &A.second, 4);
            sigG[ak]=sig_of(A,q,al,be);
        }
        printf("q=%d |G|=%zu\n", q, G.size()); fflush(stdout);
        for(auto& cd : cands){
            int pass=0; vector<pair<int,int>> failw; pair<int,int> failA{0,0}; bool haveFailA=false;
            for(auto w : cd.ws){
                bool ok=true;
                for(auto A : G){
                    pair<int,int> Aw{ (A.first+w.first)%q, (A.second+w.second)%q };
                    string ak; ak.resize(8); memcpy(&ak[0], &A.first, 4); memcpy(&ak[4], &A.second, 4);
                    if(sig_of(Aw,q,al,be)!=sigG[ak]){ ok=false; if(!haveFailA){ failA=A; haveFailA=true; } break; }
                }
                if(ok) pass++; else failw.push_back(w);
            }
            printf("  %s: pass %d/%zu", cd.label.c_str(), pass, cd.ws.size());
            if(!failw.empty()){ printf(" fail e.g. w=(%d,%d) at A=(%d,%d)", failw[0].first, failw[0].second, failA.first, failA.second); }
            printf("\n"); fflush(stdout);
        }
    }
    return 0;
}
