// Wave 45, task 7 — W2 sweep to 1e10: for each odd prime p in [LO, HI),
//   d = ord_p(alpha) in (R/pR)^x, R = Z[sqrt(2)], alpha = 3+2*sqrt(2),
//   and test whether alpha^d == 1 mod p^2 (i.e. e = v_p(alpha^d - 1) >= 2).
// d divides N = p - (2/p): p-1 if p = +-1 mod 8 (split), p+1 if p = +-3 mod 8.
// Differences from wave 40: p^2 is NEVER formed (it overflows u64 for
// p > 2^32 -- the first version of this file did form it and produced
// a false positive at p = 4318272001, caught by the Python verifier;
// that run was discarded). Mod-p^2 arithmetic uses the p-part
// representation (A + pB, components mod p, products in __int128),
// validated by --selftest against plain mod-p^2 arithmetic for
// p <= 1e9. The sieve is segmented per thread (no 5 GB table).
// Usage: ./wave45_W2_sweep10 LO HI NTHREADS   (LO odd, HI exclusive)
//        ./wave45_W2_sweep10 --selftest
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <cstring>
#include <cmath>
#include <vector>
#include <thread>
#include <mutex>
using i128 = __int128_t;
using u128 = __uint128_t;
using u64 = uint64_t;

struct Elem { u64 a, b; };

// Plain multiplication mod m (valid when 3*m^2 < 2^127, i.e. m <= 1e18).
static inline Elem mul_plain(Elem x, Elem y, u64 m) {
    i128 a = (i128)x.a * y.a + (i128)2 * x.b * y.b;
    i128 b = (i128)x.a * y.b + (i128)x.b * y.a;
    return {(u64)(a % m), (u64)(b % m)};
}

// Mod-p^2 arithmetic WITHOUT ever storing p^2 in u64 (it overflows for
// p > 2^32 -- the bug that invalidated the first decade run, producing
// a false positive at p = 4318272001). Element of R/p^2R written in
// base p: (a0 + b0*sqrt2) + p*(a1 + b1*sqrt2), all components mod p
// (fit u64 for p <= 1e10). (A + pB)(C + pD) = AC + p(AD + BC) mod p^2,
// where AC must be taken mod p^2 EXACTLY (its base-p high digit folds
// into the p-part); AD, BC only mod p. All wide products are in
// __int128 (max here 3e20), p^2 itself only as u128.
struct E2 { u64 a0, b0, a1, b1; };
static inline E2 mul_e2(E2 x, E2 y, u64 p) {
    u128 p2 = (u128)p * p;
    u128 fam = ((u128)x.a0 * y.a0 + (u128)2 * x.b0 * y.b0) % p2;
    u128 fbm = ((u128)x.a0 * y.b0 + (u128)x.b0 * y.a0) % p2;
    u64 a0 = (u64)(fam % p), b0 = (u64)(fbm % p);
    u64 fa1 = (u64)(fam / p), fb1 = (u64)(fbm / p);
    u64 ad_a = (u64)(((i128)x.a0 * y.a1 + (i128)2 * x.b0 * y.b1) % p);
    u64 ad_b = (u64)(((i128)x.a0 * y.b1 + (i128)x.b0 * y.a1) % p);
    u64 bc_a = (u64)(((i128)x.a1 * y.a0 + (i128)2 * x.b1 * y.b0) % p);
    u64 bc_b = (u64)(((i128)x.a1 * y.b0 + (i128)x.b1 * y.a0) % p);
    u64 a1 = (fa1 + ad_a + bc_a) % p;
    u64 b1 = (fb1 + ad_b + bc_b) % p;
    return {a0, b0, a1, b1};
}
static inline E2 sqr_e2(E2 x, u64 p) {
    u128 p2 = (u128)p * p;
    u128 fam = ((u128)x.a0 * x.a0 + (u128)2 * x.b0 * x.b0) % p2;
    u128 fbm = ((u128)2 * x.a0 * x.b0) % p2;
    u64 a0 = (u64)(fam % p), b0 = (u64)(fbm % p);
    u64 fa1 = (u64)(fam / p), fb1 = (u64)(fbm / p);
    u64 ab_a = (u64)(((i128)x.a0 * x.a1 + (i128)2 * x.b0 * x.b1) % p);
    u64 ab_b = (u64)(((i128)x.a0 * x.b1 + (i128)x.b0 * x.a1) % p);
    u64 a1 = (fa1 + 2 * ab_a) % p;
    u64 b1 = (fb1 + 2 * ab_b) % p;
    return {a0, b0, a1, b1};
}
static Elem pw_plain(Elem base, u64 exp, u64 m) {
    Elem r{1 % m, 0};
    while (exp) {
        if (exp & 1) r = mul_plain(r, base, m);
        base = mul_plain(base, base, m);
        exp >>= 1;
    }
    return r;
}
static E2 pw_e2(E2 base, u64 exp, u64 p) {
    E2 r{1 % p, 0, 0, 0};
    while (exp) {
        if (exp & 1) r = mul_e2(r, base, p);
        base = sqr_e2(base, p);
        exp >>= 1;
    }
    return r;
}

// Small primes up to 100000 by simple sieve.
static std::vector<u64> small_primes() {
    const int LIM = 100000;
    std::vector<char> comp(LIM + 1, 0);
    for (int i = 2; 1LL * i * i <= LIM; i++)
        if (!comp[i])
            for (int j = i * i; j <= LIM; j += i) comp[j] = 1;
    std::vector<u64> pr;
    for (int i = 2; i <= LIM; i++)
        if (!comp[i]) pr.push_back(i);
    return pr;
}

static std::mutex out_mu;

struct Worker {
    u64 lo, hi;                 // odd range [lo, hi)
    const std::vector<u64>* small;
    long nprimes = 0, ne2 = 0;
    std::vector<std::pair<u64,u64>> hits;
    void run(int tid) {
        static const u64 SEG_ODDS = 1ULL << 26;   // 67.1M odds per segment
        std::vector<unsigned char> seg;
        for (u64 s = lo; s < hi; s += 2 * SEG_ODDS) {
            u64 send = s + 2 * SEG_ODDS;
            if (send > hi) send = hi;
            u64 n_odds = (send - s + 1) / 2;
            seg.assign(n_odds, 0);
            for (u64 q : *small) {
                if (q == 2) continue;
                u64 q2 = q * q;
                if (q2 > send && q > send) break;
                u64 m0 = q2 > s ? q2 : ((s + q - 1) / q) * q;
                if ((m0 & 1) == 0) m0 += q;
                if (m0 < q2) m0 = q2 + ((q2 - m0 + 2 * q - 1) / (2 * q)) * 2 * q;
                for (u64 n = m0; n < send; n += 2 * q)
                    seg[(n - s) / 2] = 1;
            }
            for (u64 i = 0; i < n_odds; i++) {
                if (seg[i]) continue;
                u64 p = s + 2 * i;
                if (p < 3) continue;
                nprimes++;
                u64 r8 = p % 8;
                u64 N = (r8 == 1 || r8 == 7) ? p - 1 : p + 1;
                u64 tmp = N;
                std::vector<u64> fac;
                for (u64 q : *small) {
                    if (q * q > tmp) break;
                    if (tmp % q == 0) {
                        fac.push_back(q);
                        while (tmp % q == 0) tmp /= q;
                    }
                }
                if (tmp > 1) fac.push_back(tmp);
                Elem alpha{3 % p, 2 % p};
                u64 d = N;
                for (u64 q : fac) {
                    while (d % q == 0) {
                        Elem t = pw_plain(alpha, d / q, p);
                        if (t.a == 1 % p && t.b == 0) d /= q;
                        else break;
                    }
                }
                // alpha in base p: A = (3%p, 2%p), B = ((3-A.a)/p, (2-A.b)/p);
                // B = 0 for p > 3, but B = (1, 0) at p = 3 (else p = 3 is a
                // false positive: (2*sqrt2)^4 = 64 == 1 mod 9).
                E2 alpha2{3 % p, 2 % p, (3 - 3 % p) / p, (2 - 2 % p) / p};
                E2 t2 = pw_e2(alpha2, d, p);
                if (t2.a0 == 1 % p && t2.b0 == 0 && t2.a1 == 0 && t2.b1 == 0) {
                    ne2++;
                    hits.push_back({p, d});
                }
            }
        }
        std::lock_guard<std::mutex> lk(out_mu);
        for (auto& h : hits)
            std::printf("E2 p=%llu d=%llu\n",
                        (unsigned long long)h.first, (unsigned long long)h.second);
        std::fprintf(stderr, "thread %d range [%llu,%llu): primes=%ld e>=2=%ld\n",
                     tid, (unsigned long long)lo, (unsigned long long)hi,
                     nprimes, ne2);
    }
};

int main(int argc, char** argv) {
    if (argc > 1 && std::strcmp(argv[1], "--selftest") == 0) {
        // Compare E2 (p-part) arithmetic against plain mod-p^2 arithmetic
        // for random odd p <= 1e9 (where p^2 fits u64 and plain products
        // fit __int128). Covers mul, sqr, and full powmod.
        u64 state = 0x9E3779B97F4A7C15ULL;
        auto rnd = [&]() { state ^= state << 13; state ^= state >> 7; state ^= state << 17; return state; };
        auto to_plain = [&](E2 e, u64 p, u64 p2) -> Elem {
            u64 a = (u64)(((u128)e.a0 + (u128)p * e.a1) % p2);
            u64 b = (u64)(((u128)e.b0 + (u128)p * e.b1) % p2);
            return {a, b};
        };
        for (int i = 0; i < 200000; i++) {
            u64 p = 3 + 2 * (rnd() % 500000000ULL);
            u64 p2 = p * p;
            E2 a{rnd() % p, rnd() % p, rnd() % p, rnd() % p};
            E2 b{rnd() % p, rnd() % p, rnd() % p, rnd() % p};
            Elem g = to_plain(mul_e2(a, b, p), p, p2);
            Elem w = mul_plain(to_plain(a, p, p2), to_plain(b, p, p2), p2);
            Elem gs = to_plain(sqr_e2(a, p), p, p2);
            Elem ws = mul_plain(to_plain(a, p, p2), to_plain(a, p, p2), p2);
            if (g.a != w.a || g.b != w.b || gs.a != ws.a || gs.b != ws.b) {
                std::fprintf(stderr, "E2 SELFTEST FAIL (mul/sqr)\n");
                return 1;
            }
            u64 e = rnd() % 100000;
            E2 gp = pw_e2(E2{3 % p, 2 % p, (3 - 3 % p) / p, (2 - 2 % p) / p}, e, p);
            Elem wp = pw_plain(Elem{3 % p2, 2 % p2}, e, p2);
            Elem gpc = to_plain(gp, p, p2);
            if (gpc.a != wp.a || gpc.b != wp.b) {
                std::fprintf(stderr, "E2 SELFTEST FAIL (pow)\n");
                return 1;
            }
        }
        // Deterministic small-p pow checks, including p = 3 (whose base
        // has nonzero p-part: alpha = (0 + 2*sqrt2) + 3*(1 + 0*sqrt2)).
        for (u64 p : {3ULL, 5ULL, 7ULL, 13ULL, 17ULL}) {
            u64 p2 = p * p;
            for (u64 e = 0; e < 40; e++) {
                E2 gp = pw_e2(E2{3 % p, 2 % p, (3 - 3 % p) / p, (2 - 2 % p) / p}, e, p);
                Elem wp = pw_plain(Elem{3 % p2, 2 % p2}, e, p2);
                Elem gpc = to_plain(gp, p, p2);
                if (gpc.a != wp.a || gpc.b != wp.b) {
                    std::fprintf(stderr, "E2 SELFTEST FAIL (small p=%llu e=%llu)\n",
                                 (unsigned long long)p, (unsigned long long)e);
                    return 1;
                }
            }
        }
        std::fprintf(stderr, "SELFTEST PASS\n");
        return 0;
    }
    if (argc < 4) {
        std::fprintf(stderr, "usage: %s LO HI NTHREADS\n", argv[0]);
        return 2;
    }
    u64 LO = strtoull(argv[1], nullptr, 10);
    u64 HI = strtoull(argv[2], nullptr, 10);
    int NT = atoi(argv[3]);
    if (LO % 2 == 0) LO++;
    std::vector<u64> small = small_primes();
    std::vector<std::thread> ths;
    std::vector<Worker> ws(NT);
    u64 span = (HI - LO + NT - 1) / NT;
    span = (span + 1) / 2 * 2;   // keep boundaries even-aligned
    for (int t = 0; t < NT; t++) {
        u64 lo = LO + span * t, hi = lo + span;
        if (hi > HI) hi = HI;
        if (lo >= HI) { ws[t].lo = ws[t].hi = HI; continue; }
        ws[t].lo = lo; ws[t].hi = hi; ws[t].small = &small;
        ths.emplace_back([&, t]() { ws[t].run(t); });
    }
    for (auto& th : ths) th.join();
    long tot_p = 0, tot_e = 0;
    for (auto& w : ws) { tot_p += w.nprimes; tot_e += w.ne2; }
    std::fprintf(stderr, "TOTAL primes=%ld e>=2=%ld range=[%llu,%llu)\n",
                 tot_p, tot_e, (unsigned long long)LO, (unsigned long long)HI);
    return 0;
}
