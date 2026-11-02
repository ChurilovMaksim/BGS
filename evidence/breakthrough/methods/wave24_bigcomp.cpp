// Wave 24, task 4: streaming census of the q = 13729^2 component at m = 48.
//
// Kernel points mod q are p * t with t = (i*Up + j*Vp) mod p,
// i, j in [0, p), p = 13729 (validated against the SNF construction:
// formula == direct seed construction, H*seq == 0 mod q).
// Fiber/orbit structure mod q equals that of t mod p (scaling by p is
// injective and dihedral-equivariant), so this enumerates fibers and
// Gamma-orbits (dihedral, 96 perms) of the big component exactly.
// Streaming: no point array is stored; a hash table maps the 128-bit
// hash of the sorted multiset to (count, up to 2 distinct orbit-canon
// hashes, split flag). Memory scales with #fibers, not #points.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <iostream>
#include <string>
#include <thread>
#include <vector>

static const int M = 48;
static const int P = 13729;

struct Hash128 {
    uint64_t h1, h2;
    bool operator==(const Hash128 &o) const { return h1 == o.h1 && h2 == o.h2; }
};

static inline Hash128 hash_arr(const uint16_t *a, int n) {
    uint64_t h1 = 1469598103934665603ULL;
    for (int i = 0; i < n; i++) {
        h1 ^= (uint64_t)a[i];
        h1 *= 1099511628211ULL;
    }
    uint64_t h2 = 0;
    for (int i = 0; i < n; i++) h2 = h2 * 1000003ULL + (uint64_t)(a[i] + 1);
    return {h1, h2};
}

// Open-addressing table: key -> count, canon hashes, split flag.
struct Entry {
    Hash128 key{};
    uint32_t count = 0;
    Hash128 canon1{};
    Hash128 canon2{};
    uint8_t ncanon = 0;
    uint8_t used = 0;
};

struct Table {
    std::vector<Entry> t;
    size_t mask = 0;
    size_t n = 0;
    Table() { init(1 << 20); }
    void init(size_t cap) {
        t.assign(cap, Entry());
        mask = cap - 1;
        n = 0;
    }
    void grow() {
        std::vector<Entry> old = std::move(t);
        init((mask + 1) * 2);
        for (auto &e : old)
            if (e.used) insert_entry(e);
    }
    void insert_entry(const Entry &e) {
        size_t idx = (e.key.h1 ^ (e.key.h2 * 0x9E3779B97F4A7C15ULL)) & mask;
        while (t[idx].used) idx = (idx + 1) & mask;
        t[idx] = e;
        n++;
    }
    // Insert one point; returns false if table exceeded the entry cap.
    bool insert_point(const Hash128 &key, const Hash128 &canon, size_t cap_entries) {
        if ((n + 1) * 10 > (mask + 1) * 7) grow();
        if (n >= cap_entries) return false;
        size_t idx = (key.h1 ^ (key.h2 * 0x9E3779B97F4A7C15ULL)) & mask;
        while (true) {
            Entry &e = t[idx];
            if (!e.used) {
                e.used = 1;
                e.key = key;
                e.count = 1;
                e.canon1 = canon;
                e.ncanon = 1;
                n++;
                return true;
            }
            if (e.key == key) {
                e.count++;
                if (!(e.canon1 == canon)) {
                    if (e.ncanon == 1) {
                        e.canon2 = canon;
                        e.ncanon = 2;
                    } else if (!(e.canon2 == canon)) {
                        e.ncanon = 3;  // >=3 distinct orbits (capped)
                    }
                }
                return true;
            }
            idx = (idx + 1) & mask;
        }
    }
    void merge_from(const Table &o) {
        for (auto &e : o.t) {
            if (!e.used) continue;
            if ((n + 1) * 10 > (mask + 1) * 7) grow();
            size_t idx = (e.key.h1 ^ (e.key.h2 * 0x9E3779B97F4A7C15ULL)) & mask;
            while (true) {
                Entry &d = t[idx];
                if (!d.used) {
                    d = e;
                    n++;
                    break;
                }
                if (d.key == e.key) {
                    d.count += e.count;
                    // merge canon sets (cap at 3 distinct)
                    int nc = (int)d.ncanon;
                    auto add = [&](const Hash128 &c) {
                        if (nc >= 3) return;
                        if (nc == 0) { d.canon1 = c; nc = 1; return; }
                        if (d.canon1 == c) return;
                        if (nc == 1) { d.canon2 = c; nc = 2; return; }
                        if (d.canon2 == c) return;
                        nc = 3;
                    };
                    if (e.ncanon >= 1) add(e.canon1);
                    if (e.ncanon >= 2) add(e.canon2);
                    if (e.ncanon >= 3) nc = 3;
                    d.ncanon = (uint8_t)nc;
                    break;
                }
                idx = (idx + 1) & mask;
            }
        }
    }
};

static int Up[M], Vp[M];

// Lex-min dihedral canon of t[0..47]. Shifts: new[j]=t[(j+k)%48];
// reflections: new[j]=t[(k-j+48)%48]. Only perms starting at a minimal
// value can attain the lex-min.
static void canon(const uint16_t *t, uint16_t *best) {
    uint16_t mn = t[0];
    for (int i = 1; i < M; i++) mn = std::min(mn, t[i]);
    bool first = true;
    uint16_t cand[M];
    for (int k = 0; k < M; k++) {
        if (t[k] != mn) continue;
        for (int kind = 0; kind < 2; kind++) {
            for (int j = 0; j < M; j++)
                cand[j] = (kind == 0) ? t[(j + k) % M] : t[(k - j + M) % M];
            if (first || std::lexicographical_compare(cand, cand + M, best, best + M)) {
                std::memcpy(best, cand, sizeof(cand));
                first = false;
            }
        }
    }
}

static bool run_range(int i0, int i1, Table &tab, size_t cap_entries, int tid) {
    std::array<uint16_t, M> base{}, cur{}, sorted{}, best{};
    // base = i0 * Up mod p
    for (int k = 0; k < M; k++) base[k] = (uint16_t)(((int64_t)i0 * Up[k]) % P);
    auto t_start = std::chrono::steady_clock::now();
    int64_t done = 0;
    for (int i = i0; i < i1; i++) {
        cur = base;
        for (int j = 0; j < P; j++) {
            sorted = cur;
            std::sort(sorted.begin(), sorted.end());
            Hash128 fk = hash_arr(sorted.data(), M);
            canon(cur.data(), best.data());
            Hash128 ck = hash_arr(best.data(), M);
            if (!tab.insert_point(fk, ck, cap_entries)) {
                std::fprintf(stderr, "[t%d] ENTRY CAP EXCEEDED at i=%d j=%d\n", tid, i, j);
                return false;
            }
            if (++done % 20000000 == 0) {
                double el = std::chrono::duration<double>(
                                std::chrono::steady_clock::now() - t_start).count();
                std::fprintf(stderr, "[t%d] %lldM pts, entries=%zu, %.1fs\n", tid,
                             (long long)(done / 1000000), tab.n, el);
            }
            for (int k = 0; k < M; k++) {
                int v = cur[k] + Vp[k];
                if (v >= P) v -= P;
                cur[k] = (uint16_t)v;
            }
        }
        for (int k = 0; k < M; k++) {
            int v = base[k] + Up[k];
            if (v >= P) v -= P;
            base[k] = (uint16_t)v;
        }
    }
    return true;
}

int main(int argc, char **argv) {
    // Test mode: ./prog test basis.txt < pairs(i j) -> sorted tuple | canon tuple.
    if (argc > 2 && std::strcmp(argv[1], "test") == 0) {
        std::ifstream in(argv[2]);
        if (!in) { std::fprintf(stderr, "cannot open basis file\n"); return 1; }
        for (int k = 0; k < M; k++) in >> Up[k];
        for (int k = 0; k < M; k++) in >> Vp[k];
        long long i, j;
        std::array<uint16_t, M> t{}, sorted{}, best{};
        while (std::cin >> i >> j) {
            for (int k = 0; k < M; k++)
                t[k] = (uint16_t)(((i * Up[k] + j * Vp[k]) % P + P) % P);
            sorted = t;
            std::sort(sorted.begin(), sorted.end());
            canon(t.data(), best.data());
            for (int k = 0; k < M; k++) std::printf("%d%c", sorted[k], k + 1 == M ? '|' : ' ');
            for (int k = 0; k < M; k++) std::printf("%s%d", k ? " " : "", best[k]);
            std::printf("\n");
        }
        return 0;
    }
    const char *basis_file = (argc > 1) ? argv[1] : "wave24_bigcomp_basis.txt";
    int nthreads = (argc > 2) ? std::atoi(argv[2]) : 2;
    size_t cap_entries = (argc > 3) ? (size_t)std::atoll(argv[3]) : 30000000ULL;
    std::ifstream in(basis_file);
    if (!in) { std::fprintf(stderr, "cannot open basis file\n"); return 1; }
    for (int k = 0; k < M; k++) in >> Up[k];
    for (int k = 0; k < M; k++) in >> Vp[k];
    std::vector<Table> tabs(nthreads);
    std::vector<std::thread> ths;
    std::vector<char> ok(nthreads, 1);
    for (int t = 0; t < nthreads; t++) {
        int i0 = (int64_t)P * t / nthreads;
        int i1 = (int64_t)P * (t + 1) / nthreads;
        ths.emplace_back([&, t, i0, i1]() {
            ok[t] = run_range(i0, i1, tabs[t], cap_entries, t) ? 1 : 0;
        });
    }
    for (auto &th : ths) th.join();
    for (int t = 0; t < nthreads; t++)
        if (!ok[t]) { std::fprintf(stderr, "thread %d failed\n", t); return 2; }
    Table all = std::move(tabs[0]);
    for (int t = 1; t < nthreads; t++) all.merge_from(tabs[t]);
    // Summarize.
    uint64_t total = 0, nfib = 0, nsplit = 0, over96 = 0, maxsize = 0;
    std::vector<std::string> splits;
    for (auto &e : all.t) {
        if (!e.used) continue;
        total += e.count;
        nfib++;
        maxsize = std::max<uint64_t>(maxsize, e.count);
        if (e.count > 96) over96++;
        if (e.ncanon >= 2) {
            nsplit++;
            char buf[256];
            std::snprintf(buf, sizeof(buf),
                          "  split h1=%016llx h2=%016llx size=%u ncanon=%d",
                          (unsigned long long)e.key.h1, (unsigned long long)e.key.h2,
                          e.count, (int)e.ncanon);
            splits.push_back(buf);
        }
    }
    std::printf("TOTAL_POINTS=%llu\n", (unsigned long long)total);
    std::printf("N_FIBERS=%llu\n", (unsigned long long)nfib);
    std::printf("N_SPLIT=%llu\n", (unsigned long long)nsplit);
    std::printf("N_OVER96=%llu\n", (unsigned long long)over96);
    std::printf("MAX_FIBER_SIZE=%llu\n", (unsigned long long)maxsize);
    for (auto &s : splits) std::printf("%s\n", s.c_str());
    std::printf("DONE\n");
    return 0;
}
