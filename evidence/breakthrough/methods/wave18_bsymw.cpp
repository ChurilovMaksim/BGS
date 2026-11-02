// Wave 18, task 1: exact Bsym_w(supp) and Bsym_fiber(supp) at m=12.
// Enumerates global Fix_12 points in support via CRT over component
// seeds (only supported component seeds: 8 x 81 x 25 x 49 x 121 =
// 96,049,800 points). For each point computes sorted(y) (fiber key)
// and sorted(w), w = (H y)/D, and aggregates sum of squares of class
// sizes for fibers (key sorted y) and (fiber,w)-classes (key sorted y
// + sorted w). No Lean, no repo access.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <chrono>
#include <map>

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
static u64 hash_key(const u32* y, const int8_t* w) {
    u64 h = 1469598103934665603ULL;
    for (int j = 0; j < M; j++) { h ^= y[j]; h *= 1099511628211ULL; }
    if (w) for (int j = 0; j < M; j++) { h ^= (u64)(uint8_t)w[j]; h *= 1099511628211ULL; }
    return splitmix64(h);
}
static std::string to_string128(unsigned __int128 x) {
    if (x == 0) return "0";
    std::string s;
    while (x > 0) { int d = (int)(x % 10); s.push_back('0' + d); x /= 10; }
    std::reverse(s.begin(), s.end());
    return s;
}
static u64 ugcd(u64 a, u64 b) { while (b) { u64 t = a % b; a = b; b = t; } return a; }
static u64 gcd128_64(unsigned __int128 a, u64 b) {
    u64 r = (u64)(a % b);
    return ugcd(b, r);
}

// ---------- fiber table: key sorted y ----------
struct FSlot {
    u64 h = 0;
    u32 y[M];
    u64 cnt = 0;
    bool occ = false;
};
struct FTable {
    std::vector<FSlot> t;
    size_t mask = 0, distinct = 0;
    explicit FTable(int pw) { t.resize((size_t)1 << pw); mask = t.size() - 1; }
    void grow() {
        std::vector<FSlot> old = std::move(t);
        t.resize(old.size() * 2); mask = t.size() - 1; distinct = 0;
        for (auto& s : old) if (s.occ) insert_raw(s.h, s.y, s.cnt);
    }
    void insert_raw(u64 h, const u32* y, u64 c) {
        size_t i = h & mask;
        while (t[i].occ) {
            if (t[i].h == h && memcmp(t[i].y, y, sizeof(u32) * M) == 0) { t[i].cnt += c; return; }
            i = (i + 1) & mask;
        }
        t[i].occ = true; t[i].h = h; memcpy(t[i].y, y, sizeof(u32) * M); t[i].cnt = c; distinct++;
    }
    void add(const u32* y) {
        if (distinct * 10 > t.size() * 7) grow();
        u64 h = hash_key(y, nullptr);
        size_t i = h & mask;
        while (t[i].occ) {
            if (t[i].h == h && memcmp(t[i].y, y, sizeof(u32) * M) == 0) { t[i].cnt++; return; }
            i = (i + 1) & mask;
        }
        t[i].occ = true; t[i].h = h; memcpy(t[i].y, y, sizeof(u32) * M); t[i].cnt = 1; distinct++;
    }
    const FSlot* find(const u32* y, u64 h) const {
        size_t i = h & mask;
        while (t[i].occ) {
            if (t[i].h == h && memcmp(t[i].y, y, sizeof(u32) * M) == 0) return &t[i];
            i = (i + 1) & mask;
        }
        return nullptr;
    }
};

// ---------- (fiber,w) table: key sorted y + sorted w ----------
struct WSlot {
    u64 h = 0;
    u32 y[M];
    int8_t w[M];
    u64 cnt = 0;
    bool occ = false;
};
struct WTable {
    std::vector<WSlot> t;
    size_t mask = 0, distinct = 0;
    explicit WTable(int pw) { t.resize((size_t)1 << pw); mask = t.size() - 1; }
    void grow() {
        std::vector<WSlot> old = std::move(t);
        t.resize(old.size() * 2); mask = t.size() - 1; distinct = 0;
        for (auto& s : old) if (s.occ) insert_raw(s.h, s.y, s.w, s.cnt);
    }
    void insert_raw(u64 h, const u32* y, const int8_t* w, u64 c) {
        size_t i = h & mask;
        while (t[i].occ) {
            if (t[i].h == h && memcmp(t[i].y, y, sizeof(u32) * M) == 0 && memcmp(t[i].w, w, M) == 0) { t[i].cnt += c; return; }
            i = (i + 1) & mask;
        }
        t[i].occ = true; t[i].h = h; memcpy(t[i].y, y, sizeof(u32) * M); memcpy(t[i].w, w, M); t[i].cnt = c; distinct++;
    }
    void add(const u32* y, const int8_t* w) {
        if (distinct * 10 > t.size() * 7) grow();
        u64 h = hash_key(y, w);
        size_t i = h & mask;
        while (t[i].occ) {
            if (t[i].h == h && memcmp(t[i].y, y, sizeof(u32) * M) == 0 && memcmp(t[i].w, w, M) == 0) { t[i].cnt++; return; }
            i = (i + 1) & mask;
        }
        t[i].occ = true; t[i].h = h; memcpy(t[i].y, y, sizeof(u32) * M); memcpy(t[i].w, w, M); t[i].cnt = 1; distinct++;
    }
};

// ---------- per-fiber aggregation of w-classes ----------
struct ASlot {
    u64 h = 0;
    u32 y[M];
    u32 nw = 0;
    u64 sumsq = 0;
    bool occ = false;
};
struct ATable {
    std::vector<ASlot> t;
    size_t mask = 0, distinct = 0;
    explicit ATable(int pw) { t.resize((size_t)1 << pw); mask = t.size() - 1; }
    void grow() {
        std::vector<ASlot> old = std::move(t);
        t.resize(old.size() * 2); mask = t.size() - 1; distinct = 0;
        for (auto& s : old) if (s.occ) insert_raw(s.h, s.y, s.nw, s.sumsq);
    }
    void insert_raw(u64 h, const u32* y, u32 nw, u64 sumsq) {
        size_t i = h & mask;
        while (t[i].occ) {
            if (t[i].h == h && memcmp(t[i].y, y, sizeof(u32) * M) == 0) { t[i].nw += nw; t[i].sumsq += sumsq; return; }
            i = (i + 1) & mask;
        }
        t[i].occ = true; t[i].h = h; memcpy(t[i].y, y, sizeof(u32) * M); t[i].nw = nw; t[i].sumsq = sumsq; distinct++;
    }
    void add(const u32* y, u64 wcnt) {
        if (distinct * 10 > t.size() * 7) grow();
        u64 h = hash_key(y, nullptr);
        size_t i = h & mask;
        while (t[i].occ) {
            if (t[i].h == h && memcmp(t[i].y, y, sizeof(u32) * M) == 0) { t[i].nw++; t[i].sumsq += wcnt * wcnt; return; }
            i = (i + 1) & mask;
        }
        t[i].occ = true; t[i].h = h; memcpy(t[i].y, y, sizeof(u32) * M); t[i].nw = 1; t[i].sumsq = wcnt * wcnt; distinct++;
    }
    const ASlot* find(const u32* y, u64 h) const {
        size_t i = h & mask;
        while (t[i].occ) {
            if (t[i].h == h && memcmp(t[i].y, y, sizeof(u32) * M) == 0) return &t[i];
            i = (i + 1) & mask;
        }
        return nullptr;
    }
};

static i64 egcd(i64 a, i64 b, i64& x, i64& y) {
    if (b == 0) { x = 1; y = 0; return a; }
    i64 x1, y1; i64 g = egcd(b, a % b, x1, y1); x = y1; y = x1 - (a / b) * y1; return g;
}

int main(int argc, char** argv) {
    const char* datafile = argv[1];
    int limit_last = argc > 2 ? atoi(argv[2]) : -1; // restrict innermost comp seeds (validation)
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
        if ((int)c.contrib.size() != nsup) { fprintf(stderr, "nsup mismatch q=%d\n", q); return 1; }
        comps.push_back(std::move(c));
    }
    fclose(f);
    int K = comps.size();
    fprintf(stderr, "components:");
    for (auto& c : comps) fprintf(stderr, " q=%d n=%zu", c.q, c.contrib.size());
    fprintf(stderr, "\n");
    if (limit_last > 0) comps.back().contrib.resize(limit_last);
    // delta vectors: delta[k][s] = contrib[k][(s+1)%n] - contrib[k][s]
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
    fprintf(stderr, "total points to enumerate: %llu\n", (unsigned long long)N);
    // initial y = sum of contrib[*][0] mod D
    std::array<i64, M> y{};
    y.fill(0);
    for (int k = 0; k < K; k++)
        for (int j = 0; j < M; j++) y[j] += comps[k].contrib[0][j];
    for (int j = 0; j < M; j++) y[j] %= D;

    FTable ft(24);
    WTable wt(24);
    auto t0 = std::chrono::steady_clock::now();
    std::vector<int> idx(K, 0);
    u64 bad = 0;
    std::array<u32, M> sy;
    std::array<int8_t, M> sw;
    for (u64 count = 0; count < N; count++) {
        for (int j = 0; j < M; j++) sy[j] = (u32)y[j];
        std::sort(sy.begin(), sy.end());
        bool ok = true;
        for (int j = 0; j < M; j++) {
            i64 hy = 6 * y[j] - y[(j - 1 + M) % M] - y[(j + 1) % M];
            if (hy % D != 0) { ok = false; }
            sw[j] = (int8_t)(hy / D);
        }
        if (!ok) bad++;
        std::sort(sw.begin(), sw.end());
        ft.add(sy.data());
        wt.add(sy.data(), sw.data());
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
        if ((count + 1) % 10000000ULL == 0) {
            auto t1 = std::chrono::steady_clock::now();
            double el = std::chrono::duration<double>(t1 - t0).count();
            fprintf(stderr, "  %llu pts (%.1fs, %.0f pts/s) fibers=%zu wclasses=%zu bad=%llu\n",
                    (unsigned long long)(count + 1), el, (count + 1) / el,
                    ft.distinct, wt.distinct, (unsigned long long)bad);
        }
    }
    fprintf(stderr, "enumeration done, bad=%llu\n", (unsigned long long)bad);
    // stats
    unsigned __int128 sumF = 0, sumW = 0, totF = 0, totW = 0;
    u64 maxF = 0, maxW = 0;
    std::map<u64, u64> histF, histW;
    for (auto& s : ft.t) if (s.occ) {
        totF += s.cnt; sumF += (unsigned __int128)s.cnt * s.cnt;
        if (s.cnt > maxF) maxF = s.cnt;
        histF[s.cnt]++;
    }
    for (auto& s : wt.t) if (s.occ) {
        totW += s.cnt; sumW += (unsigned __int128)s.cnt * s.cnt;
        if (s.cnt > maxW) maxW = s.cnt;
        histW[s.cnt]++;
    }
    // per-fiber w-class aggregation
    ATable at(24);
    for (auto& s : wt.t) if (s.occ) at.add(s.y, s.cnt);
    u64 fib_multi_w = 0, fib_single_w = 0;
    unsigned __int128 mass_multi_w = 0, mass_single_w = 0, sq_multi_w = 0;
    for (auto& s : ft.t) if (s.occ) {
        u64 h = hash_key(s.y, nullptr);
        const ASlot* a = at.find(s.y, h);
        if (!a) { fprintf(stderr, "AGGREGATION BUG: fiber missing\n"); return 1; }
        if (a->nw > 1) { fib_multi_w++; mass_multi_w += s.cnt; sq_multi_w += (unsigned __int128)s.cnt * s.cnt; }
        else { fib_single_w++; mass_single_w += s.cnt; }
        if (a->sumsq > (unsigned __int128)s.cnt * s.cnt) { fprintf(stderr, "AGGREGATION BUG sumsq\n"); return 1; }
    }
    u64 supp = (u64)totF;
    printf("{\n");
    printf("  \"points\": %llu,\n", (unsigned long long)supp);
    printf("  \"points_w\": %llu,\n", (unsigned long long)(u64)totW);
    printf("  \"bad_nondivisible\": %llu,\n", (unsigned long long)bad);
    printf("  \"n_fibers\": %zu,\n", ft.distinct);
    printf("  \"n_wclasses\": %zu,\n", wt.distinct);
    printf("  \"sum_sq_fiber\": %s,\n", to_string128(sumF).c_str());
    printf("  \"sum_sq_w\": %s,\n", to_string128(sumW).c_str());
    // reduced fractions sum/|supp|
    {
        u64 g = gcd128_64(sumF, supp);
        unsigned __int128 num = sumF / g; u64 den = supp / g;
        printf("  \"Bsym_fiber\": \"%s/%llu\",\n", to_string128(num).c_str(), (unsigned long long)den);
        printf("  \"Bsym_fiber_float\": %.12f,\n", (double)num / (double)den);
    }
    {
        u64 g = gcd128_64(sumW, supp);
        unsigned __int128 num = sumW / g; u64 den = supp / g;
        printf("  \"Bsym_w\": \"%s/%llu\",\n", to_string128(num).c_str(), (unsigned long long)den);
        printf("  \"Bsym_w_float\": %.12f,\n", (double)num / (double)den);
    }
    printf("  \"max_fiber\": %llu,\n", (unsigned long long)maxF);
    printf("  \"max_wclass\": %llu,\n", (unsigned long long)maxW);
    printf("  \"fibers_multi_wclass\": %llu,\n", (unsigned long long)fib_multi_w);
    printf("  \"fibers_single_wclass\": %llu,\n", (unsigned long long)fib_single_w);
    printf("  \"mass_multi_wclass_fibers\": %s,\n", to_string128(mass_multi_w).c_str());
    printf("  \"mass_single_wclass_fibers\": %s,\n", to_string128(mass_single_w).c_str());
    printf("  \"sumsq_multi_wclass_fibers\": %s\n", to_string128(sq_multi_w).c_str());
    printf("}\n");
    fprintf(stderr, "fiber size histogram (size:count):");
    for (auto& kv : histF) fprintf(stderr, " %llu:%llu", (unsigned long long)kv.first, (unsigned long long)kv.second);
    fprintf(stderr, "\nwclass size histogram (size:count):");
    for (auto& kv : histW) fprintf(stderr, " %llu:%llu", (unsigned long long)kv.first, (unsigned long long)kv.second);
    fprintf(stderr, "\n");
    return 0;
}
