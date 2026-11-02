// Wave 16, task 1: search for primes p with k=2 and 4|L0, where
// L0 = ord_p(alpha), alpha = 3+2*sqrt(2), k = v_p(alpha^L0 - 1).
// E-test lemma: for odd prime p, eps = (2/p), e = p - eps (the order of
// the norm-1 group). Then alpha^e == 1 mod p^2  <=>  k >= 2.
// Proof: e = L0*q with q = e/L0; L0 >= 3 for odd p (alpha-1 = 2+2*sqrt2,
// alpha^2-1 = 16+12*sqrt2, so L0=1 forces p|2, L0=2 forces p|4), hence
// 1 <= q <= (p+1)/3 < p, so p does not divide q. If k>=2, alpha^e =
// (1+p^k u)^q == 1 mod p^2. If k=1, alpha^e == 1 + p*q*u mod p^2 with
// u a unit mod p and p not dividing q, so != 1 mod p^2.
// Arithmetic in R = Z[sqrt2]: (a,b) = a + b*sqrt2, product
// (a1a2+2*b1b2, a1b2+a2b1). All __int128: p <= 2e9 => p^2 <= 4e18,
// products <= ~5e37 < 2^127 ~ 1.7e38. Safe.
// Modes: validate <bound> : for p < bound, compute L0, k directly and
//   check e-test <=> k>=2; print all k>=2 primes.
//   scan <bound> : print all e-test candidates (k>=2 primes) <= bound.
// Compile: g++ -O2 -fopenmp wave16_search.cpp -o wave16_search
#include <cstdio>
#include <cstdint>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>
using u64 = uint64_t;
using u128 = __uint128_t;

static inline u64 mulmod(u128 a, u128 b, u64 mod) {
    return (u64)((a * b) % mod);
}

// (a,b) in R/mod, returns pair
struct Elem { u64 a, b; };
static inline Elem mulR(Elem x, Elem y, u64 mod) {
    u128 a = (u128)x.a * y.a + (u128)2 * x.b * y.b;
    u128 b = (u128)x.a * y.b + (u128)x.b * y.a;
    return {(u64)(a % mod), (u64)(b % mod)};
}
static Elem powR(Elem base, u64 exp, u64 mod) {
    Elem r{1 % mod, 0};
    while (exp) {
        if (exp & 1) r = mulR(r, base, mod);
        base = mulR(base, base, mod);
        exp >>= 1;
    }
    return r;
}

// small primes up to n by simple sieve
static std::vector<u64> small_primes(u64 n) {
    std::vector<bool> comp(n + 1, false);
    std::vector<u64> ps;
    for (u64 i = 2; i <= n; ++i) if (!comp[i]) {
        ps.push_back(i);
        if (i * i <= n) for (u64 j = i * i; j <= n; j += i) comp[j] = true;
    }
    return ps;
}

// distinct prime factors of n (trial division by small primes)
static std::vector<u64> distinct_factors(u64 n, const std::vector<u64>& ps) {
    std::vector<u64> fs;
    for (u64 p : ps) {
        if (p * p > n) break;
        if (n % p == 0) { fs.push_back(p); while (n % p == 0) n /= p; }
    }
    if (n > 1) fs.push_back(n);
    return fs;
}

// order of alpha mod p (p odd prime): factor e = p - (2/p), reduce.
static u64 order_mod_p(u64 p, const std::vector<u64>& ps) {
    u64 r = p & 7;
    int eps = (r == 1 || r == 7) ? 1 : -1;
    u64 e = (u64)((int64_t)p - eps);
    Elem alpha{3 % p, 2 % p};
    u64 ord = e;
    for (u64 q : distinct_factors(e, ps)) {
        while (ord % q == 0) {
            Elem t = powR(alpha, ord / q, p);
            if (t.a == 1 % p && t.b == 0) ord /= q;
            else break;
        }
    }
    return ord;
}

// k = v_p(alpha^L0 - 1): largest t with alpha^L0 == 1 mod p^t.
// Only called in validate mode (p < 10000), so p^4 fits u64; if the
// value passes every checkable t, return 99 (flags "very large k").
static int kval(u64 p, u64 L0) {
    u128 mod = (u128)p * p; // p^2
    int t = 2;
    for (;;) {
        if (mod >= ((u128)1 << 64)) return 99;
        u64 m = (u64)mod;
        Elem alpha{3 % m, 2 % m};
        Elem v = powR(alpha, L0, m);
        if (!(v.a == 1 % m && v.b == 0)) return t - 1;
        mod *= p; ++t;
    }
}

int main(int argc, char** argv) {
    if (argc < 3) { fprintf(stderr, "usage: %s validate|scan bound\n", argv[0]); return 2; }
    bool validate = strcmp(argv[1], "validate") == 0;
    u64 N = strtoull(argv[2], nullptr, 10);
    u64 sq = (u64)sqrt((long double)N) + 1;
    std::vector<u64> ps = small_primes(sq);
    const u64 SEG = 1 << 20; // odds per segment
    std::vector<u64> all_candidates;
    long long nprimes = 0, mismatch = 0;
    // collect per-thread candidate lists
    int nthreads = 4;
#pragma omp parallel num_threads(nthreads)
    {
        std::vector<u64> local;
        long long lprimes = 0, lmismatch = 0;
#pragma omp for schedule(dynamic, 1)
        for (u64 lo = 3; lo <= N; lo += 2 * SEG) {
            u64 hi = std::min(lo + 2 * SEG, N + 1);
            // sieve odds in [lo, hi)
            std::vector<char> comp(SEG, 0);
            for (u64 pr : ps) {
                if (pr == 2) continue;
                u64 start = (lo + pr - 1) / pr * pr;
                if (start < pr * pr) start = pr * pr;
                if ((start & 1) == 0) start += pr;
                for (u64 j = start; j < hi; j += 2 * pr) comp[(j - lo) / 2] = 1;
            }
            for (u64 j = lo; j < hi; j += 2) {
                if (comp[(j - lo) / 2]) continue;
                u64 p = j;
                ++lprimes;
                u64 r = p & 7;
                int eps = (r == 1 || r == 7) ? 1 : -1;
                u64 e = (u64)((int64_t)p - eps);
                u128 p2 = (u128)p * p;
                u64 mod = (u64)p2; // p <= 2e9 => p^2 < 2^63
                Elem alpha{3 % mod, 2 % mod};
                Elem v = powR(alpha, e, mod);
                bool etest = (v.a == 1 % mod && v.b == 0);
                if (validate) {
                    u64 L0 = order_mod_p(p, ps);
                    int k = kval(p, L0);
                    bool kk = (k >= 2);
                    if (kk != etest) {
                        ++lmismatch;
#pragma omp critical
                        fprintf(stderr, "MISMATCH p=%llu L0=%llu k=%d etest=%d\n",
                                (unsigned long long)p, (unsigned long long)L0, k, (int)etest);
                    }
                    if (kk) {
#pragma omp critical
                        printf("k>=2 prime p=%llu L0=%llu k=%d 4|L0=%d\n",
                               (unsigned long long)p, (unsigned long long)L0, k, (int)(L0 % 4 == 0));
                    }
                } else {
                    if (etest) local.push_back(p);
                }
            }
        }
#pragma omp critical
        {
            all_candidates.insert(all_candidates.end(), local.begin(), local.end());
            nprimes += lprimes; mismatch += lmismatch;
        }
    }
    if (!validate) {
        std::sort(all_candidates.begin(), all_candidates.end());
        for (u64 p : all_candidates) printf("candidate p=%llu\n", (unsigned long long)p);
    }
    fprintf(stderr, "done: primes=%lld candidates=%zu mismatch=%lld\n",
            nprimes, all_candidates.size(), mismatch);
    return 0;
}
