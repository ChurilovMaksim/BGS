// Wave 32, task 1: full G1' check at (324,3) mod 243 (f=5, k=1, s=4).
// Mirrors wave26_G1_f4_checks.py full_G1_check: A over R/243,
// y_i = Tr(A*alpha^i) mod 243, i in [0,324); global = sorted multiset;
// per-class: i mod t, t = gcd(324,4) = 4; D_4-relatedness via 8 perms.
// Pass 1: global count vectors, sort, group. Pass 2: per-class canonical
// forms (min over 8 dihedral perms of concatenated class count vectors)
// must agree within each global group.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
using namespace std;
const int P = 243, M = 324, T = 4;
struct Elem { int a, b; };
static inline Elem mul(Elem x, Elem y) {
    return {(x.a*y.a + 2*x.b*y.b) % P, (x.a*y.b + x.b*y.a) % P};
}
static inline int tr(Elem x) { return (2*x.a) % P; }
struct Rec {
    array<uint16_t, P> g{};
    int idx;
};
int main() {
    const Elem ALPHA{3, 2};
    Elem cur{1, 0};
    for (int i = 0; i < M; i++) cur = mul(cur, ALPHA);
    printf("alpha^%d mod %d = (%d,%d) (need (1,0))\n", M, P, cur.a, cur.b);
    if (cur.a != 1 || cur.b != 0) return 1;
    vector<Rec> recs;
    recs.reserve(P*P);
    for (int a = 0; a < P; a++) for (int b = 0; b < P; b++) {
        Rec r; r.g.fill(0); r.idx = a*P + b;
        Elem c{a, b};
        for (int i = 0; i < M; i++) {
            r.g[tr(c)]++;
            c = mul(c, ALPHA);
        }
        recs.push_back(r);
    }
    sort(recs.begin(), recs.end(), [](const Rec& x, const Rec& y){
        return memcmp(x.g.data(), y.g.data(), sizeof(x.g)) < 0;
    });
    int perms[8][4], np = 0;
    for (int eps : {1, -1}) for (int bb = 0; bb < 4; bb++) {
        for (int r = 0; r < 4; r++) perms[np][r] = ((eps*r + bb) % 4 + 4) % 4;
        np++;
    }
    long ngroups = 0, maxsize = 0, bad = 0;
    size_t i = 0;
    while (i < recs.size()) {
        size_t j = i;
        while (j < recs.size() && memcmp(recs[j].g.data(), recs[i].g.data(), sizeof(recs[i].g)) == 0) j++;
        ngroups++;
        maxsize = max(maxsize, (long)(j - i));
        vector<string> cans;
        for (size_t k = i; k < j; k++) {
            int A = recs[k].idx;
            Elem c{A / P, A % P};
            array<array<uint16_t, P>, 4> pc{};
            for (auto& v : pc) v.fill(0);
            for (int s = 0; s < M; s++) {
                pc[s % T][tr(c)]++;
                c = mul(c, ALPHA);
            }
            string best;
            bool f2 = true;
            for (int pi = 0; pi < 8; pi++) {
                string cand;
                cand.resize(4*P*sizeof(uint16_t));
                for (int r = 0; r < 4; r++)
                    memcpy(&cand[r*P*sizeof(uint16_t)], pc[perms[pi][r]].data(), sizeof(uint16_t)*P);
                if (f2 || cand < best) { best = cand; f2 = false; }
            }
            cans.push_back(best);
        }
        for (size_t k = 1; k < cans.size(); k++)
            if (cans[k] != cans[0]) {
                bad++;
                if (bad <= 3) printf("  BAD in group starting idx %d\n", recs[i].idx);
            }
        i = j;
    }
    printf("full G1' (m=%d,p=3,P=%d,t=%d): A-values=%d groups=%ld maxgroup=%ld bad=%ld\n",
           M, P, T, P*P, ngroups, maxsize, bad);
    return 0;
}
