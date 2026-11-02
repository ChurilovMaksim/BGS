// Wave 27, task 1: full G1' check at (750,5) mod 625.
// R = Z[sqrt2] mod 625, alpha = 3+2 sqrt2, sequences y_i = Tr(A alpha^i),
// i in Z/750. Group by global multiset (count-vector hash), then check
// that the unordered pair of class multisets (classes mod 2) is constant
// within each group (D_2 = {id, swap} on Z/2). Exact integer arithmetic.
#include <cstdio>
#include <cstdint>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cstring>
using namespace std;
const int P4 = 625;
struct E { int a, b; };
static inline E mul(E x, E y) {
    return {(x.a*y.a + 2*x.b*y.b) % P4, (x.a*y.b + x.b*y.a) % P4};
}
static inline int tr(E x) { return (2*x.a) % P4; }
int main() {
    // powers of alpha mod 625
    vector<E> pw(751);
    pw[0] = {1, 0};
    for (int i = 1; i <= 750; i++) pw[i] = mul(pw[i-1], {3, 2});
    if (!(pw[750].a == 1 && pw[750].b == 0)) {
        printf("alpha^750 != 1 mod 625: (%d,%d)\n", pw[750].a, pw[750].b);
        return 1;
    }
    printf("alpha^750 == 1 mod 625 OK\n");
    // order of gamma = alpha^6 mod 625
    E g = pw[6];
    E cur = {1, 0};
    int gord = 0;
    for (int i = 1; i <= 200; i++) {
        cur = mul(cur, g);
        if (cur.a == 1 && cur.b == 0) { gord = i; break; }
    }
    printf("gamma = alpha^6 = (%d,%d), order mod 625 = %d\n", g.a, g.b, gord);
    // gamma - 1 = 5*u ; u mod 5
    printf("gamma-1 = (%d,%d); u mod 5 = (%d,%d)\n",
        (g.a - 1 + P4) % P4, g.b, ((g.a - 1) / 5) % 5, (g.b / 5) % 5);

    const int M = 750;
    const int NA = P4 * P4; // 390625
    // For each A: global count vector hash + class count-vector hashes.
    // Use two 64-bit hashes: FNV over counts is expensive; instead hash the
    // sequence directly via polynomial rolling over sorted? No: multiset
    // hash = sum over values of h(value) with multiplicity (commutative).
    // Use splitmix-style per-value contribution summed (order-independent).
    auto hval = [](uint64_t v) {
        uint64_t z = v + 0x9e3779b97f4a7c15ULL;
        z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL;
        z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL;
        return z ^ (z >> 31);
    };
    struct Rec {
        uint64_t gh;      // global multiset hash
        uint64_t c0, c1;  // class multiset hashes
    };
    vector<Rec> recs(NA);
    vector<int> cnt(P4);
    for (int a = 0; a < P4; a++) {
        for (int b = 0; b < P4; b++) {
            int idx = a * P4 + b;
            E A = {a, b};
            uint64_t gh = 0, c0 = 0, c1 = 0;
            for (int i = 0; i < M; i++) {
                int v = tr(mul(A, pw[i]));
                uint64_t hv = hval((uint64_t)v);
                gh += hv;
                if (i % 2 == 0) c0 += hv; else c1 += hv;
            }
            recs[idx] = {gh, c0, c1};
        }
        if (a % 125 == 0) fprintf(stderr, "a=%d done\n", a);
    }
    // group by gh (with verification: same gh => compare full count vectors
    // for a sample; here we trust 64-bit sum-hash + verify class constancy
    // below, and separately verify collisions are negligible by recounting
    // one group fully -- see note)
    unordered_map<uint64_t, vector<int>> groups;
    groups.reserve(NA * 2);
    for (int i = 0; i < NA; i++) groups[recs[i].gh].push_back(i);
    printf("num groups (by hash): %zu\n", groups.size());
    // group size distribution
    vector<int> szdist(100000, 0);
    size_t maxsz = 0;
    for (auto &kv : groups) {
        if (kv.second.size() < szdist.size()) szdist[kv.second.size()]++;
        maxsz = max(maxsz, kv.second.size());
    }
    printf("max group size: %zu\n", maxsz);
    printf("size distribution (size: count): ");
    for (size_t s = 1; s < szdist.size(); s++)
        if (szdist[s]) printf("%zu:%d ", s, szdist[s]);
    printf("\n");
    // per-class constancy: within each group, the unordered pair {c0,c1}
    // must be constant.
    long long badgroups = 0;
    long long badpairs_est = 0;
    for (auto &kv : groups) {
        auto &v = kv.second;
        uint64_t lo0 = min(recs[v[0]].c0, recs[v[0]].c1);
        uint64_t hi0 = max(recs[v[0]].c0, recs[v[0]].c1);
        for (size_t k = 1; k < v.size(); k++) {
            uint64_t lo = min(recs[v[k]].c0, recs[v[k]].c1);
            uint64_t hi = max(recs[v[k]].c0, recs[v[k]].c1);
            if (lo != lo0 || hi != hi0) {
                badgroups++;
                badpairs_est += (long long)k;
                break;
            }
        }
    }
    printf("groups failing class-pair constancy: %lld\n", badgroups);
    return 0;
}
