#include <bits/stdc++.h>
using namespace std;
int main(){
    vector<int> ms = {2,6,10,12,14,18,20,22,24,26,28,30,32,34,36,38,40,44,48,52,56,60};
    for(int m: ms){
        int L=0, tmp=m; while(tmp%2==0){tmp/=2; L++;}
        int a = (L==0?2:2*L+3);
        int q = 1<<a;
        int P = 1<<L;
        int t = std::gcd(m,4);
        // enumerate Fix_m mod q by brute force over (y0,y1)
        vector<vector<int>> seqs;
        vector<int> s(m+2);
        for(int y0=0;y0<q;y0++) for(int y1=0;y1<q;y1++){
            s[0]=y0; s[1]=y1;
            for(int i=2;i<m+2;i++) s[i]=(6*s[i-1]-s[i-2])%q, s[i]=(s[i]+q)%q;
            if(s[m]==y0 && s[m+1]==y1) seqs.emplace_back(s.begin(), s.begin()+m);
        }
        int nonP=0;
        for(auto &y: seqs) for(int i=0;i<m;i++) if(y[i]!=y[i%P]){nonP++; break;}
        // group by sorted multiset
        map<vector<int>, vector<int>> groups; // key -> indices
        for(int i=0;i<(int)seqs.size();i++){
            vector<int> key=seqs[i]; sort(key.begin(), key.end());
            groups[key].push_back(i);
        }
        // D_t canonical form of per-class tuple
        auto canon = [&](const vector<int>& y){
            vector<vector<int>> cls(t);
            for(int i=0;i<m;i++) cls[i%t].push_back(y[i]);
            for(auto &c: cls) sort(c.begin(), c.end());
            vector<vector<int>> best; bool first=true;
            vector<vector<int>> cur(t);
            for(int b=0;b<t;b++){
                // shift
                for(int sgn:{1,-1}){
                    for(int r=0;r<t;r++) cur[r]=cls[(sgn*r+b)%t <0 ? (sgn*r+b)%t+t : (sgn*r+b)%t];
                    // careful with negative mod: compute properly
                    for(int r=0;r<t;r++){ int idx=(sgn*r+b)%t; if(idx<0) idx+=t; cur[r]=cls[idx]; }
                    if(first || cur<best) {best=cur; first=false;}
                }
            }
            return best;
        };
        int bad=0, ngroups=0;
        for(auto &kv: groups){
            ngroups++;
            auto c0 = canon(seqs[kv.second[0]]);
            for(int idx: kv.second) if(canon(seqs[idx])!=c0){bad++; break;}
        }
        printf("m=%d L=%d a=%d q=%d P=%d t=%d |Fix|=%d expect=%d nonPperiodic=%d groups=%d BAD=%d\n",
            m,L,a,q,P,t,(int)seqs.size(),1<<a,nonP,ngroups,bad);
        fflush(stdout);
    }
    return 0;
}
