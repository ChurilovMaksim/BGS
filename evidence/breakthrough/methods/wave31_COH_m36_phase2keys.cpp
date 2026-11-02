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
struct SeqHash{ size_t operator()(Seq const& s) const { size_t h=0; for(int i=0;i<36;i++) h=h*1315423911u+(size_t)(s.v[i]+1); return h; } };
int main(){
    vector<array<int,36>> DIH;
    for(int k=0;k<36;k++){
        array<int,36> sh, rf;
        for(int i=0;i<36;i++){ sh[i]=(i+k)%36; rf[i]=((-i+k)%36+36)%36; }
        DIH.push_back(sh); DIH.push_back(rf);
    }
    sort(DIH.begin(), DIH.end()); DIH.erase(unique(DIH.begin(), DIH.end()), DIH.end());
    int q=729;
    vector<pair<int,int>> G;
    for(int a=0;a<27;a++) for(int b=0;b<27;b++) G.push_back({27*a,27*b});
    map<Seq, vector<pair<int,int>>> seqdict;
    map<Seq, vector<Seq>> classes;
    for(auto A:G){
        Seq s; auto cur=A;
        for(int i=0;i<36;i++){ s.v[i]=trp(cur,q); cur=mulp(cur,{3,2},q); }
        seqdict[s].push_back(A);
        Seq ss=s; sort(ss.v.begin(), ss.v.end()); classes[ss].push_back(s);
    }
    for(auto &kv: classes){ auto &vec=kv.second; sort(vec.begin(), vec.end()); vec.erase(unique(vec.begin(), vec.end()), vec.end()); }
    unordered_set<Seq, SeqHash> shifts;
    for(int a=0;a<9;a++) for(int b=0;b<9;b++){
        pair<int,int> D={(81*a)%729,(81*b)%729};
        Seq s; auto cur=D;
        for(int i=0;i<36;i++){ s.v[i]=trp(cur,729); cur=mulp(cur,{3,2},729); }
        shifts.insert(s);
    }
    printf("ShiftSet81 size=%zu\n", shifts.size());
    map<tuple<unsigned long long,unsigned long long,string>, long long> keycount;
    long long total=0, fullT=0, proper=0;
    map<int,int> tsize_dist;
    for(auto &kv: classes){
        auto &vec=kv.second;
        for(auto &S: vec) for(auto &Sp: vec){
            total++;
            unsigned long long tlo=0, thi=0;
            for(int ti=0; ti<72; ti++){
                Seq diff; for(int i=0;i<36;i++) diff.v[i]=(Sp.v[i]-S.v[DIH[ti][i]]%729+729)%729;
                if(shifts.count(diff)){ if(ti<64) tlo|=(1ULL<<ti); else thi|=(1ULL<<(ti-64)); }
            }
            int tsize=__builtin_popcountll(tlo)+__builtin_popcountll(thi);
            tsize_dist[tsize]++;
            bool full = (tlo==0xFFFFFFFFFFFFFFFFULL && thi==0xFFULL);
            if(full) fullT++; else proper++;
            array<unsigned long long,36> allow;
            for(int i=0;i<36;i++){ unsigned long long bits=0; for(int j=0;j<36;j++) if(S.v[j]==Sp.v[i]) bits|=(1ULL<<j); allow[i]=bits; }
            string key; for(int i=0;i<36;i++){ unsigned long long x=allow[i]; for(int b=0;b<8;b++) key.push_back(char(x>>(8*b))); }
            keycount[make_tuple(tlo,thi,key)]++;
        }
    }
    printf("pairs=%lld fullT=%lld proper=%lld distinct_keys=%zu\n", total, fullT, proper, keycount.size());
    printf("T-size dist:"); for(auto &pr: tsize_dist) printf(" %d:%d", pr.first, pr.second); printf("\n");
    set<tuple<unsigned long long,unsigned long long,string>> properkeys;
    for(auto &kv: keycount){
        auto [tlo,thi,key]=kv.first;
        if(!(tlo==0xFFFFFFFFFFFFFFFFULL && thi==0xFFULL)) properkeys.insert(kv.first);
    }
    printf("distinct proper keys=%zu\n", properkeys.size());
    FILE* f=fopen("/tmp/coh36_properkeys2.bin","wb");
    for(auto &k: properkeys){
        auto [tlo,thi,key]=k;
        fwrite(&tlo,8,1,f); fwrite(&thi,8,1,f); fwrite(key.data(),1,288,f);
    }
    fclose(f);
    printf("wrote %zu proper keys\n", properkeys.size());
    return 0;
}
