// Wave 18, task 1: extract raw global points whose fiber is split.
// Reads split fiber keys (sorted y, binary) dumped by wave18_orbits,
// re-enumerates all support points, and writes raw y vectors of
// points in split fibers to a binary file (12 x uint32 per point).
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
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
struct Slot { u64 h = 0; u32 y[M]; bool occ = false; };
static i64 egcd(i64 a, i64 b, i64& x, i64& y) {
    if (b == 0) { x = 1; y = 0; return a; }
    i64 x1, y1; i64 g = egcd(b, a % b, x1, y1); x = y1; y = x1 - (a / b) * y1; return g;
}
int main(int argc, char** argv) {
    const char* datafile = argv[1];
    const char* splitfile = argv[2];
    const char* outfile = argv[3];
    // load split keys into small hash set
    std::vector<Slot> set(4096);
    size_t mask = set.size() - 1;
    size_t nkeys = 0;
    {
        FILE* sf = fopen(splitfile, "rb");
        if (!sf) { fprintf(stderr, "cannot open splitfile\n"); return 1; }
        u32 key[M];
        while (fread(key, sizeof(u32), M, sf) == M) {
            u64 h = hash_key(key);
            size_t i = h & mask;
            while (set[i].occ) i = (i + 1) & mask;
            set[i].occ = true; set[i].h = h; memcpy(set[i].y, key, sizeof(u32) * M);
            nkeys++;
        }
        fclose(sf);
    }
    fprintf(stderr, "split keys loaded: %zu\n", nkeys);
    FILE* f = fopen(datafile, "r");
    if (!f) return 1;
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
    std::array<i64, M> y{};
    y.fill(0);
    for (int k = 0; k < K; k++)
        for (int j = 0; j < M; j++) y[j] += comps[k].contrib[0][j];
    for (int j = 0; j < M; j++) y[j] %= D;
    FILE* out = fopen(outfile, "wb");
    if (!out) return 1;
    std::vector<int> idx(K, 0);
    std::array<u32, M> sy;
    u64 written = 0;
    for (u64 count = 0; count < N; count++) {
        for (int j = 0; j < M; j++) sy[j] = (u32)y[j];
        std::sort(sy.begin(), sy.end());
        u64 h = hash_key(sy.data());
        size_t i = h & mask;
        bool found = false;
        while (set[i].occ) {
            if (set[i].h == h && memcmp(set[i].y, sy.data(), sizeof(u32) * M) == 0) { found = true; break; }
            i = (i + 1) & mask;
        }
        if (found) {
            u32 raw[M];
            for (int j = 0; j < M; j++) raw[j] = (u32)y[j];
            fwrite(raw, sizeof(u32), M, out);
            written++;
        }
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
    }
    fclose(out);
    fprintf(stderr, "split-fiber points written: %llu (expected 35952)\n", (unsigned long long)written);
    return 0;
}
