// Wave 17, task 3: mod-p^3 e-test scan for k>=3 primes below 2e6.
// For odd prime p, e = p - (2/p): alpha^e == 1 mod p^t  <=>  k >= t
// (proved in wave17_G1_k3.md; here t = 2, 3). Arithmetic in R = Z[sqrt2]
// with unsigned __int128 and per-term reduction: mod = p^3 <= 8e18,
// single products <= 6.4e37 < 2^128, doubled products <= 1.28e38 < 2^128.
// Compile: g++ -O2 wave17_G1_k3_scan.cpp -o wave17_G1_k3_scan
#include <cstdio>
#include <cstdint>
#include <vector>
using u64 = uint64_t;
using u128 = __uint128_t;

struct Elem { u64 a, b; };
static inline Elem mulR(Elem x, Elem y, u64 mod) {
    u128 t1 = (u128)x.a * y.a % mod;
    u128 t2 = (u128)2 * x.b * y.b % mod;
    u128 t3 = (u128)x.a * y.b % mod;
    u128 t4 = (u128)x.b * y.a % mod;
    return {(u64)((t1 + t2) % mod), (u64)((t3 + t4) % mod)};
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

int main() {
    const u64 N = 2000000;
    std::vector<bool> comp(N + 1, false);
    for (u64 i = 2; i * i <= N; ++i) if (!comp[i])
        for (u64 j = i * i; j <= N; j += i) comp[j] = true;
    long long nprimes = 0, nk2 = 0, nk3 = 0;
    for (u64 p = 3; p <= N; p += 2) {
        if (comp[p]) continue;
        ++nprimes;
        int eps = (p % 8 == 1 || p % 8 == 7) ? 1 : -1;
        u64 e = (u64)((int64_t)p - eps);
        u64 mod2 = p * p;
        Elem v2 = powR({3 % mod2, 2 % mod2}, e, mod2);
        bool k2 = (v2.a == 1 % mod2 && v2.b == 0);
        u64 mod3 = p * p * p;
        Elem v3 = powR({3 % mod3, 2 % mod3}, e, mod3);
        bool k3 = (v3.a == 1 % mod3 && v3.b == 0);
        if (k2) { ++nk2; printf("k>=2 prime p=%llu\n", (unsigned long long)p); }
        if (k3) { ++nk3; printf("k>=3 prime p=%llu\n", (unsigned long long)p); }
    }
    fprintf(stderr, "done: odd primes=%lld k>=2=%lld k>=3=%lld\n", nprimes, nk2, nk3);
    return 0;
}
