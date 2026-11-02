// Wave 18, task 1 (follow-up): Gamma-orbit census over supp at m=12.
// Same CRT enumeration as wave18_bsymw.cpp. For each point computes
// its Gamma-orbit size via the dihedral stabilizer (24 perms), and
// aggregates per fiber (key sorted y) a histogram of orbit sizes.
// Cross-checks sum_y |Gamma y| against wave 17's Bsym_Gamma numerator
// 2,302,601,802, and measures split-fiber mass for bounding the
// pair-sum ratio R. No Lean, no repo access.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <chrono>
#include <set>

using u32 = uint32_t;
using u64 = uint64_t;
using i64 = int64_t;
static const int M = 12;

static u64 splitmix64(u64 x) {
    x += 0x9e3779b97f4a7c15ULL;
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
    x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
    return x ^ (x >> 31);
}
static u64 hash_key(const u32* y) {
    u64 h = 1469598103934665603ULL;
    for (int j = 0; j < M; j++) { h ^= y[j]; h *= 1099511628211ULL; }
    return splitmix64(h);
}
static std::string to_string128(unsigned __int128 x) {
    if (x == 0) return "0";
    std::string s;
    while (x > 0) { int d = (int)(x % 10); s.push_back('0' + d); x /= 10; }
    std::reverse(s.begin(), s.end());
    return s;
}

// orbit sizes possible: divisors from D12 subgroups: 1,2,3,4,6,8,12,24
static const int OSIZES[8] = {1, 2, 3, 4, 6, 8, 12, 24};
static int bin_of(int s) {
    for (int i = 0; i < 8; i++) if (OSIZES[i] == s) return i;
    return -1;
}

struct FSlot {
    u64 h = 0;
    u32 y[M];
    u64 cnt = 0;
    u32 hist[8] = {0, 0, 0, 0, 0, 0, 0, 0};
    bool occ = false;
};
struct FTable {
    std::vector<FSlot> t;
    size_t mask = 0, distinct = 0;
    explicit FTable(int pw) { t.resize((size_t)1 << pw); mask = t.size() - 1; }
    void grow() {
        std::vector<FSlot> old = std::move(t);
        t.resize(old.size() * 2); mask = t.size() - 1; distinct = 0;
        for (auto& s : old) if (s.occ) insert_raw(s.h, s.y, s.cnt, s.hist);
    }
    void insert_raw(u64 h, const u32* y, u64 c, const u32* hist) {
        size_t i = h & mask;
        while (t[i].occ) {
            if (t[i].h == h && memcmp(t[i].y, y, sizeof(u32) * M) == 0) {
                t[i].cnt += c;
                for (int b = 0; b < 8; b++) t[i].hist[b] += hist[b];
                return;
            }
            i = (i + 1) & mask;
        }
        t[i].occ = true; t[i].h = h; memcpy(t[i].y, y, sizeof(u32) * M);
        t[i].cnt = c; memcpy(t[i].hist, hist, sizeof(u32) * 8); distinct++;
    }
    void add(const u32* y, int obin) {
        if (distinct * 10 > t.size() * 7) grow();
        u64 h = hash_key(y);
        size_t i = h & mask;
        while (t[i].occ) {
            if (t[i].h == h && memcmp(t[i].y, y, sizeof(u32) * M) == 0) {
                t[i].cnt++; t[i].hist[obin]++; return;
            }
            i = (i + 1) & mask;
        }
        t[i].occ = true; t[i].h = h; memcpy(t[i].y, y, sizeof(u32) * M);
        t[i].cnt = 1; t[i].hist[obin] = 1; distinct++;
    }
};

static i64 egcd(i64 a, i64 b, i64& x, i64& y) {
    if (b == 0) { x = 1; y = 0; return a; }
    i64 x1, y1; i64 g = egcd(b, a % b, x1, y1); x = y1; y = x1 - (a / b) * y1; return g;
}

int main(int argc, char** argv) {
    const char* datafile = argv[1];
    const char* splitfile = argc > 2 ? argv[2] : nullptr;
    FILE* f = fopen(datafile, "r");
    if (!f) { fprintf(stderr, "cannot open %s\n", datafile); return 1; }
    int m; i64 D;
    if (fscanf(f, "%d %lld", &m, (long long*)&D) != 2) return 1;
    struct Comp { int q; std::vector<std::array<u32, M>> contrib; };
    std::vector<Comp> comps;
    while (true) {
        char tag; int q, nsup;
        if (fscanf(f, " %c %d %d", &tag, &q, &nsup) != 3) break;
        Comp c; c.q = q;
        i64 dq = D / q;
        i64 x, yv; egcd(dq % q, q, x, yv);
        i64 inv = ((x % q) + q) % q;
        i64 e = (dq * inv) % D;
        for (int i = 0; i < q; i++) {
            std::array<u32, M> row; int s;
            for (int j = 0; j < M; j++) if (fscanf(f, "%u", &row[j]) != 1) return 1;
            if (fscanf(f, "%d", &s) != 1) return 1;
            if (s) {
                std::array<u32, M> cr;
                for (int j = 0; j < M; j++) cr[j] = (u32)((e * (i64)row[j]) % D);
                c.contrib.push_back(cr);
            }
        }
        comps.push_back(std::move(c));
    }
    fclose(f);
    // dihedral perms (gamma_perms logic)
    std::vector<std::array<int, M>> perms;
    {
        std::set<std::array<int, M>> seen;
        for (int k = 0; k < M; k++) {
            std::array<int, M> r, fl;
            for (int j = 0; j < M; j++) { r[j] = (j + k) % M; fl[j] = (k - j + M) % M; }
            if (seen.insert(r).second) perms.push_back(r);
            if (seen.insert(fl).second) perms.push_back(fl);
        }
    }
    fprintf(stderr, "n_perms=%zu\n", perms.size());
    int K = comps.size();
    std::vector<std::vector<std::array<i64, M>>> delta(K);
    std::vector<int> n(K);
    for (int k = 0; k < K; k++) {
        n[k] = comps[k].contrib.size();
        delta[k].resize(n[k]);
        for (int s = 0; s < n[k]; s++) {
            int ns = (s + 1) % n[k];
            for (int j = 0; j < M; j++)
                delta[k][s][j] = (i64)comps[k].contrib[ns][j] - (i64)comps[k].contrib[s][j];
        }
    }
    u64 N = 1;
    for (int k = 0; k < K; k++) N *= (u64)n[k];
    fprintf(stderr, "total points: %llu\n", (unsigned long long)N);
    std::array<i64, M> y{};
    y.fill(0);
    for (int k = 0; k < K; k++)
        for (int j = 0; j < M; j++) y[j] += comps[k].contrib[0][j];
    for (int j = 0; j < M; j++) y[j] %= D;

    FTable ft(24);
    auto t0 = std::chrono::steady_clock::now();
    std::vector<int> idx(K, 0);
    u64 sum_orbitsq = 0;
    std::array<u32, M> sy;
    for (u64 count = 0; count < N; count++) {
        // stabilizer size
        int stab = 0;
        for (auto& p : perms) {
            bool same = true;
            for (int j = 0; j < M; j++) if (y[p[j]] != y[j]) { same = false; break; }
            if (same) stab++;
        }
        int osize = (int)perms.size() / stab;
        int obin = bin_of(osize);
        if (obin < 0) { fprintf(stderr, "BAD orbit size %d\n", osize); return 1; }
        sum_orbitsq += (u64)osize;
        for (int j = 0; j < M; j++) sy[j] = (u32)y[j];
        std::sort(sy.begin(), sy.end());
        ft.add(sy.data(), obin);
        if (count + 1 < N) {
            int k = K - 1;
            while (true) {
                int s = idx[k];
                for (int j = 0; j < M; j++) {
                    y[j] += delta[k][s][j];
                    if (y[j] < 0) y[j] += D;
                    else if (y[j] >= D) y[j] -= D;
                }
                if (s + 1 < n[k]) { idx[k] = s + 1; break; }
                idx[k] = 0;
                k--;
            }
        }
        if ((count + 1) % 20000000ULL == 0) {
            auto t1 = std::chrono::steady_clock::now();
            double el = std::chrono::duration<double>(t1 - t0).count();
            fprintf(stderr, "  %llu pts (%.1fs) fibers=%zu\n",
                    (unsigned long long)(count + 1), el, ft.distinct);
        }
    }
    // split stats
    u64 n_split = 0, n_nonsplit = 0, n_orbits = 0;
    unsigned __int128 mass_split = 0, sq_split = 0, osq_split = 0, tot = 0, sumF = 0;
    for (auto& s : ft.t) if (s.occ) {
        tot += s.cnt; sumF += (unsigned __int128)s.cnt * s.cnt;
        int b = bin_of((int)s.cnt);
        bool split = (b < 0) || (s.hist[b] < s.cnt);
        unsigned __int128 osq = 0;
        for (int i = 0; i < 8; i++) {
            osq += (unsigned __int128)OSIZES[i] * s.hist[i];
            n_orbits += s.hist[i] / (u64)OSIZES[i];
        }
        if (split) { n_split++; mass_split += s.cnt; sq_split += (unsigned __int128)s.cnt * s.cnt; osq_split += osq; }
        else n_nonsplit++;
    }
    u64 supp = (u64)tot;
    if (splitfile) {
        FILE* sf = fopen(splitfile, "wb");
        if (!sf) { fprintf(stderr, "cannot open splitfile\n"); return 1; }
        for (auto& s : ft.t) if (s.occ) {
            int b = bin_of((int)s.cnt);
            bool split = (b < 0) || (s.hist[b] < s.cnt);
            if (split) fwrite(s.y, sizeof(u32), M, sf);
        }
        fclose(sf);
        fprintf(stderr, "split keys dumped\n");
    }
    printf("{\n");
    printf("  \"points\": %llu,\n", (unsigned long long)supp);
    printf("  \"n_fibers\": %zu,\n", ft.distinct);
    printf("  \"n_orbits\": %llu,\n", (unsigned long long)n_orbits);
    printf("  \"sum_orbitsq\": %llu,\n", (unsigned long long)sum_orbitsq);
    printf("  \"sum_sq_fiber_check\": %s,\n", to_string128(sumF).c_str());
    printf("  \"n_split_fibers\": %llu,\n", (unsigned long long)n_split);
    printf("  \"n_nonsplit_fibers\": %llu,\n", (unsigned long long)n_nonsplit);
    printf("  \"mass_split_fibers\": %s,\n", to_string128(mass_split).c_str());
    printf("  \"sumsq_split_fibers\": %s,\n", to_string128(sq_split).c_str());
    printf("  \"orbitsq_split_fibers\": %s\n", to_string128(osq_split).c_str());
    printf("}\n");
    // R bounds (phi constant on orbits assumed): R in
    // [(sumF - sq_split)/supp, sumF/supp]; R - BsymG in
    // [-osq_split/supp, (sq_split - osq_split)/supp]
    {
        unsigned __int128 lo = sumF - sq_split;
        // print floats via long double
        long double Rlo = (long double)lo / (long double)supp;
        long double Rhi = (long double)sumF / (long double)supp;
        long double dlo = -(long double)osq_split / (long double)supp;
        long double dhi = (long double)(sq_split - osq_split) / (long double)supp;
        fprintf(stderr, "R in [%.12Lf, %.12Lf]; R-BsymG in [%.12Lf, %.12Lf]\n", Rlo, Rhi, dlo, dhi);
    }
    return 0;
}
