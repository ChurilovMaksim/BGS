// Dump first affine-fail pairs at P=32, q=8192, with periods.
#include <bits/stdc++.h>
using namespace std;
int main() {
    const int P = 32, q = 8192;
    vector<vector<int>> vecs; vecs.reserve(q);
    for (int y0 = 0; y0 < q; ++y0) for (int y1 = 0; y1 < q; ++y1) {
        int a = y0, b = y1, seq[34]; seq[0]=y0; seq[1]=y1;
        for (int k = 2; k <= 33; ++k) { int c = (6*b-a)%q; if (c<0) c+=q; seq[k]=c; a=b; b=c; }
        if (seq[32]==y0 && seq[33]==y1) { vector<int> v(32); for (int k=0;k<32;++k) v[k]=seq[k]; vecs.push_back(v); }
    }
    map<vector<int>, vector<int>> groups;
    for (int i = 0; i < (int)vecs.size(); ++i) { vector<int> s = vecs[i]; sort(s.begin(), s.end()); groups[s].push_back(i); }
    vector<pair<int,int>> aff;
    for (int a = 1; a < P; a += 2) for (int b = 0; b < P; ++b) aff.push_back({a,b});
    auto exists_aff = [&](const vector<int>& p, const vector<int>& pp) {
        for (auto [a,b] : aff) { bool ok=true; for (int j=0;j<P;++j) if (pp[j]!=p[(a*j+b)%P]) { ok=false; break; } if (ok) return true; }
        return false;
    };
    auto period = [&](const vector<int>& v) {
        for (int d = 1; d <= P; ++d) if (P%d==0) { bool ok=true; for (int j=0;j<P;++j) if (v[j]!=v[j%d]) ok=false; if (ok) return d; }
        return P;
    };
    auto classSums = [&](const vector<int>& v) { array<int,4> Y={0,0,0,0}; for (int j=0;j<P;++j) Y[j%4]+=v[j]; return Y; };
    int dumped = 0;
    for (auto& [ms, idxs] : groups) {
        for (int ii : idxs) for (int jj : idxs) {
            if (ii==jj) continue;
            if (!exists_aff(vecs[ii], vecs[jj])) {
                printf("PAIR %d:\n p  =", dumped); for (int x : vecs[ii]) printf(" %d", x); printf("\n pp ="); for (int x : vecs[jj]) printf(" %d", x); printf("\n");
                printf("  period p=%d pp=%d  Yp=", period(vecs[ii]), period(vecs[jj]));
                auto Y = classSums(vecs[ii]); auto Yp = classSums(vecs[jj]);
                for (int k=0;k<4;++k) printf(" %d", Y[k]); printf("  Ypp="); for (int k=0;k<4;++k) printf(" %d", Yp[k]); printf("\n");
                if (++dumped >= 8) return 0;
                goto next_group;
            }
        }
        next_group:;
    }
    return 0;
}
