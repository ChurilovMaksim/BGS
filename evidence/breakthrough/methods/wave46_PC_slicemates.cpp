// Wave 46, task 7, step 3: sample non-dihedral mates in the m=24 slice.
// Slice point: (C, D), C in R/17, D in R/1153; pairs (t_i, s_i),
// t_i = Tr(C alpha^i) mod 17, s_i = Tr(D alpha^i) mod 1153, i < 24.
// alpha = 3 + 2*sqrt(2); Tr(a + b sqrt2) = 2a.
// Finds mates of a fixed base point with the same sorted pair multiset
// that are NOT dihedral images of the base. Outputs mates as C,D pairs.
#include <cstdio>
#include <cstdint>
#include <cstdlib>
#include <algorithm>
#include <array>
#include <random>
#include <set>

typedef std::array<int, 24> Seq;
typedef std::array<std::pair<short, short>, 24> Pairs;

// multiply (a,b) by alpha=(3,2) mod p
static inline void mul_alpha(int &a, int &b, int p) {
    int na = (3 * a + 4 * b) % p;
    int nb = (2 * a + 3 * b) % p;
    a = na; b = nb;
}

static Seq trace_seq(int a, int b, int p) {
    Seq s;
    int ca = a, cb = b;
    for (int i = 0; i < 24; i++) {
        s[i] = (2 * ca) % p;
        mul_alpha(ca, cb, p);
    }
    return s;
}

static Pairs pairs_of(const Seq &t, const Seq &s) {
    Pairs pr;
    for (int i = 0; i < 24; i++) pr[i] = {(short)t[i], (short)s[i]};
    return pr;
}

static uint64_t hash_pairs(Pairs pr) {
    std::sort(pr.begin(), pr.end());
    uint64_t h = 1469598103934665603ULL;
    for (auto &pp : pr) {
        uint64_t v = (uint64_t)(pp.first + 1) * 1000003ULL + (uint64_t)(pp.second + 1);
        h ^= v;
        h *= 1099511628211ULL;
    }
    return h;
}

int main(int argc, char **argv) {
    int C0a = argc > 1 ? atoi(argv[1]) : 1;
    int C0b = argc > 2 ? atoi(argv[2]) : 2;
    int D0a = argc > 3 ? atoi(argv[3]) : 3;
    int D0b = argc > 4 ? atoi(argv[4]) : 5;
    int want = argc > 5 ? atoi(argv[5]) : 10;
    long long maxsamp = argc > 6 ? atoll(argv[6]) : 200000000LL;

    Seq t0 = trace_seq(C0a, C0b, 17);
    Seq s0 = trace_seq(D0a, D0b, 1153);
    Pairs base = pairs_of(t0, s0);
    Pairs base_sorted = base;
    std::sort(base_sorted.begin(), base_sorted.end());
    uint64_t base_hash = hash_pairs(base);

    // dihedral images of base (48 maps j -> j+k, j -> -j+k)
    std::set<Pairs> dihedral;
    for (int k = 0; k < 24; k++) {
        Pairs pr;
        for (int i = 0; i < 24; i++) pr[i] = base[(i + k) % 24];
        dihedral.insert(pr);
        Pairs pr2;
        for (int i = 0; i < 24; i++) pr2[i] = base[((-i + k) % 24 + 24) % 24];
        dihedral.insert(pr2);
    }

    std::mt19937_64 rng(12345);
    std::uniform_int_distribution<int> distC(0, 16);
    std::uniform_int_distribution<int> distD(0, 1152);
    int found = 0;
    long long samp = 0;
    std::set<std::pair<int, int>> seen; // (C,D) encoded to avoid dup mates
    for (samp = 0; samp < maxsamp && found < want; samp++) {
        int ca = distC(rng), cb = distC(rng);
        int da = distD(rng), db = distD(rng);
        if (ca == C0a && cb == C0b && da == D0a && db == D0b) continue;
        Seq t = trace_seq(ca, cb, 17);
        Seq s = trace_seq(da, db, 1153);
        Pairs pr = pairs_of(t, s);
        if (hash_pairs(pr) != base_hash) continue;
        Pairs pr_sorted = pr;
        std::sort(pr_sorted.begin(), pr_sorted.end());
        if (pr_sorted != base_sorted) continue; // hash collision
        if (dihedral.count(pr)) continue; // dihedral mate, skip
        int code = (ca * 17 + cb) * 2000000 + (da * 1153 + db);
        if (seen.count({ca * 17 + cb, da * 1153 + db})) continue;
        seen.insert({ca * 17 + cb, da * 1153 + db});
        printf("MATE C=(%d,%d) D=(%d,%d) samp=%lld\n", ca, cb, da, db, samp);
        fflush(stdout);
        found++;
    }
    printf("DONE found=%d samp=%lld\n", found, samp);
    return 0;
}
