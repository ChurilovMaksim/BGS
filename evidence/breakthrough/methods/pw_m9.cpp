// P_w kill-test at m=9, exhaustive over Fix_9 (D = 7761796 = 4*49*39601).
// Fix = ker(H mod D), H = 6I - C - C^T, i.e. y_{i+1} = 6 y_i - y_{i-1}, period 9.
// Gamma = dihedral perms p[j] = (j+k) % 9 or (k-j) % 9, acting (p.y)_j = y_{p[j]}.
// Fiber = sorted(y) class. w = (H y)/D (integer, entries in -1..5).
// P_w FAILS on a fiber iff two distinct Gamma-orbits in it share sorted(w).
// Output: JSON summary + first kill examples (orbit canons, themselves Fix points).
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using namespace std;
using i64 = int64_t;
static const int M = 9;
static const int64_t D = 7761796;
static const int64_t MODS[3] = {4, 49, 39601};

static i64 egcd(i64 a, i64 b, i64 &x, i64 &y) {
    if (b == 0) { x = 1; y = 0; return a; }
    i64 x1, y1; i64 g = egcd(b, a % b, x1, y1); x = y1; y = x1 - (a / b) * y1; return g;
}
static i64 modinv(i64 a, i64 mod) {
    if (mod == 1) return 0;
    i64 x, y; egcd((a % mod + mod) % mod, mod, x, y);
    return (x % mod + mod) % mod;
}

// fix_mod via (A^9 - I) v = 0, A = [[0,1],[-1,6]] mod q (cf. gluing_components.py)
static vector<array<uint32_t, M>> fix_mod(int64_t q) {
    using Mat = array<array<i64, 2>, 2>;
    auto mul = [&](const Mat &A, const Mat &B) {
        Mat R{};
        for (int i = 0; i < 2; i++)
            for (int j = 0; j < 2; j++)
                R[i][j] = (A[i][0] * B[0][j] + A[i][1] * B[1][j]) % q;
        return R;
    };
    Mat base{{{0, 1}, {(q - 1) % q, 6 % q}}};
    Mat res{{{1, 0}, {0, 1}}};
    int n = M;
    while (n) {
        if (n & 1) res = mul(res, base);
        base = mul(base, base);
        n >>= 1;
    }
    i64 P = (res[0][0] - 1 + q) % q, Q = res[0][1];
    i64 R = res[1][0], S = (res[1][1] - 1 + q) % q;
    vector<array<uint32_t, M>> out;
    for (i64 a = 0; a < q; a++) {
        i64 rhs = (q - (P * a) % q) % q;
        i64 g = std::gcd(Q, q);
        if (rhs % g != 0) continue;
        i64 Qr = Q / g, qr = q / g;
        i64 b0 = qr > 1 ? ((rhs / g) * modinv(Qr % qr, qr)) % qr : 0;
        for (i64 k = 0; k < g; k++) {
            i64 b = b0 + k * qr;
            if ((R * a + S * b) % q != 0) continue;
            array<uint32_t, M> y{};
            y[0] = (uint32_t)a; y[1] = (uint32_t)b;
            for (int i = 1; i < M - 1; i++) {
                i64 v = (6 * (i64)y[i] - (i64)y[i - 1]) % q;
                y[i + 1] = (uint32_t)((v + q) % q);
            }
            i64 y9 = ((6 * (i64)y[M - 1] - (i64)y[M - 2]) % q + q) % q;
            i64 y10 = ((6 * y9 - (i64)y[M - 1]) % q + q) % q;
            if (y9 != a || y10 != b) continue;
            bool ok = true;
            for (int i = 0; i < M; i++) {
                i64 v = 6 * (i64)y[i] - (i64)y[(i + M - 1) % M] - (i64)y[(i + 1) % M];
                if (((v % q) + q) % q != 0) { ok = false; break; }
            }
            if (ok) out.push_back(y);
        }
    }
    return out;
}

struct Record {
    uint32_t s[M];
    uint32_t o[M];
    int8_t ws[M];
    int8_t pad[3];
};

static bool rec_less(const Record &A, const Record &B) {
    int c = memcmp(A.s, B.s, sizeof(A.s));
    if (c) return c < 0;
    c = memcmp(A.o, B.o, sizeof(A.o));
    if (c) return c < 0;
    return memcmp(A.ws, B.ws, sizeof(A.ws)) < 0;
}
static bool eq_u32(const uint32_t *a, const uint32_t *b) {
    return memcmp(a, b, M * sizeof(uint32_t)) == 0;
}
static bool eq_i8(const int8_t *a, const int8_t *b) {
    return memcmp(a, b, M * sizeof(int8_t)) == 0;
}
static string arr_str_u32(const uint32_t *a) {
    string s = "[";
    for (int i = 0; i < M; i++) { if (i) s += ","; s += to_string(a[i]); }
    return s + "]";
}
static string arr_str_i8(const int8_t *a) {
    string s = "[";
    for (int i = 0; i < M; i++) { if (i) s += ","; s += to_string((int)a[i]); }
    return s + "]";
}

int main() {
    vector<array<int, M>> perms;
    for (int k = 0; k < M; k++) {
        array<int, M> r{}, f{};
        for (int j = 0; j < M; j++) { r[j] = (j + k) % M; f[j] = (k - j + M) % M; }
        perms.push_back(r); perms.push_back(f);
    }
    sort(perms.begin(), perms.end());
    perms.erase(unique(perms.begin(), perms.end()), perms.end());
    fprintf(stderr, "perms=%zu\n", perms.size());
    if (perms.size() != 18) return 1;

    vector<vector<array<uint32_t, M>>> comp(3);
    for (int i = 0; i < 3; i++) {
        comp[i] = fix_mod(MODS[i]);
        fprintf(stderr, "q=%lld n_fix=%zu\n", (long long)MODS[i], comp[i].size());
        if ((int64_t)comp[i].size() != MODS[i]) return 1;
    }
    vector<vector<array<int64_t, M>>> contrib(3);
    for (int i = 0; i < 3; i++) {
        i64 Mi = D / MODS[i];
        i64 inv = modinv(Mi % MODS[i], MODS[i]);
        contrib[i].resize(comp[i].size());
        for (size_t t = 0; t < comp[i].size(); t++)
            for (int j = 0; j < M; j++)
                contrib[i][t][j] = (comp[i][t][j] * Mi % D) * inv % D;
    }

    size_t total = (size_t)MODS[0] * (size_t)MODS[1] * (size_t)MODS[2];
    fprintf(stderr, "total points=%zu\n", total);
    vector<Record> recs;
    recs.reserve(total);
    uint32_t y[M];
    for (size_t i2 = 0; i2 < comp[2].size(); i2++)
        for (size_t i1 = 0; i1 < comp[1].size(); i1++)
            for (size_t i0 = 0; i0 < comp[0].size(); i0++) {
                for (int j = 0; j < M; j++) {
                    i64 v = contrib[0][i0][j] + contrib[1][i1][j] + contrib[2][i2][j];
                    y[j] = (uint32_t)(v % D);
                }
                Record r{};
                array<uint32_t, M> sy;
                for (int j = 0; j < M; j++) sy[j] = y[j];
                sort(sy.begin(), sy.end());
                memcpy(r.s, sy.data(), sizeof(r.s));
                array<uint32_t, M> best{};
                bool first = true;
                for (auto &p : perms) {
                    array<uint32_t, M> t{};
                    for (int j = 0; j < M; j++) t[j] = y[p[j]];
                    if (first || t < best) { best = t; first = false; }
                }
                memcpy(r.o, best.data(), sizeof(r.o));
                array<int8_t, M> w{};
                for (int i = 0; i < M; i++) {
                    i64 num = 6 * (i64)y[i] - (i64)y[(i + M - 1) % M] - (i64)y[(i + 1) % M];
                    if (num % D != 0) { fprintf(stderr, "Hy NOT DIVISIBLE\n"); return 1; }
                    i64 wi = num / D;
                    if (wi < -1 || wi > 5) { fprintf(stderr, "w OUT OF RANGE\n"); return 1; }
                    w[i] = (int8_t)wi;
                }
                sort(w.begin(), w.end());
                memcpy(r.ws, w.data(), sizeof(r.ws));
                recs.push_back(r);
            }
    fprintf(stderr, "generated %zu, sorting...\n", recs.size());
    sort(recs.begin(), recs.end(), rec_less);
    fprintf(stderr, "sorted, scanning...\n");

    size_t n_fib = 0, n_orbits = 0, n_bad = 0, n_pw_fail = 0;
    size_t n_anomaly = 0;  // orbits with >1 distinct sorted(w) (should be 0)
    map<size_t, size_t> fiber_size_dist, orbits_per_fiber_dist;
    struct Kill { array<uint32_t, M> s, o1, o2; array<int8_t, M> ws; };
    vector<Kill> kills;
    struct BadEx { array<uint32_t, M> s; size_t sz, norb; bool pwfail; };
    vector<BadEx> badex;
    size_t i = 0;
    while (i < recs.size()) {
        size_t j = i;
        while (j < recs.size() && eq_u32(recs[j].s, recs[i].s)) j++;
        n_fib++;
        size_t fsize = j - i;
        fiber_size_dist[fsize]++;
        // split group into orbits (consecutive by o), each orbit into ws values
        struct OrbitInfo { array<uint32_t, M> canon; vector<array<int8_t, M>> wss; };
        vector<OrbitInfo> orbits;
        size_t k = i;
        while (k < j) {
            size_t k2 = k;
            while (k2 < j && eq_u32(recs[k2].o, recs[k].o)) k2++;
            OrbitInfo oi{};
            memcpy(oi.canon.data(), recs[k].o, sizeof(uint32_t) * M);
            size_t t = k;
            while (t < k2) {
                size_t t2 = t;
                while (t2 < k2 && eq_i8(recs[t2].ws, recs[t].ws)) t2++;
                array<int8_t, M> ws{};
                memcpy(ws.data(), recs[t].ws, sizeof(int8_t) * M);
                oi.wss.push_back(ws);
                t = t2;
            }
            if (oi.wss.size() > 1) n_anomaly++;
            orbits.push_back(oi);
            k = k2;
        }
        n_orbits += orbits.size();
        orbits_per_fiber_dist[orbits.size()]++;
        bool bad = orbits.size() > 1;
        if (bad) n_bad++;
        // P_w check: ws -> first orbit canon
        map<array<int8_t, M>, array<uint32_t, M>> ws_to_orbit;
        bool pwfail = false;
        for (auto &oi : orbits) {
            for (auto &ws : oi.wss) {
                auto it = ws_to_orbit.find(ws);
                if (it != ws_to_orbit.end()) {
                    if (memcmp(it->second.data(), oi.canon.data(),
                               sizeof(uint32_t) * M) != 0) {
                        pwfail = true;
                        if (kills.size() < 20) {
                            Kill kl{};
                            memcpy(kl.s.data(), recs[i].s, sizeof(uint32_t) * M);
                            kl.o1 = it->second;
                            kl.o2 = oi.canon;
                            kl.ws = ws;
                            kills.push_back(kl);
                        }
                    }
                } else {
                    ws_to_orbit[ws] = oi.canon;
                }
            }
        }
        if (pwfail) n_pw_fail++;
        if (bad && badex.size() < 20) {
            BadEx be{};
            memcpy(be.s.data(), recs[i].s, sizeof(uint32_t) * M);
            be.sz = fsize; be.norb = orbits.size(); be.pwfail = pwfail;
            badex.push_back(be);
        }
        i = j;
    }

    printf("{\n");
    printf("  \"m\": 9, \"D\": %lld, \"n_points\": %zu,\n", (long long)D, recs.size());
    printf("  \"n_fibers\": %zu, \"n_gamma_orbits\": %zu, \"n_bad_fibers\": %zu,\n",
           n_fib, n_orbits, n_bad);
    printf("  \"n_pw_fail_fibers\": %zu, \"n_orbits_with_multiple_ws\": %zu,\n",
           n_pw_fail, n_anomaly);
    printf("  \"pw_survives\": %s,\n", n_pw_fail == 0 ? "true" : "false");
    printf("  \"fiber_size_dist\": {");
    bool first = true;
    for (auto &kv : fiber_size_dist) {
        if (!first) printf(", ");
        first = false;
        printf("\"%zu\": %zu", kv.first, kv.second);
    }
    printf("},\n  \"orbits_per_fiber_dist\": {");
    first = true;
    for (auto &kv : orbits_per_fiber_dist) {
        if (!first) printf(", ");
        first = false;
        printf("\"%zu\": %zu", kv.first, kv.second);
    }
    printf("},\n  \"bad_examples\": [");
    for (size_t t = 0; t < badex.size(); t++) {
        if (t) printf(", ");
        printf("{\"sorted\": %s, \"size\": %zu, \"n_orbits\": %zu, \"pw_fail\": %s}",
               arr_str_u32(badex[t].s.data()).c_str(), badex[t].sz, badex[t].norb,
               badex[t].pwfail ? "true" : "false");
    }
    printf("],\n  \"kills\": [");
    for (size_t t = 0; t < kills.size(); t++) {
        if (t) printf(", ");
        printf("{\"sorted\": %s, \"w_sorted\": %s, \"orbit_canon_1\": %s, \"orbit_canon_2\": %s}",
               arr_str_u32(kills[t].s.data()).c_str(),
               arr_str_i8(kills[t].ws.data()).c_str(),
               arr_str_u32(kills[t].o1.data()).c_str(),
               arr_str_u32(kills[t].o2.data()).c_str());
    }
    printf("]\n}\n");
    return 0;
}
