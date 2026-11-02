// Wave 40, task 4 — W2 sweep: for each odd prime p <= LIMIT, compute
//   d = ord_p(alpha) in (R/pR)^x, R = Z[sqrt(2)], alpha = 3+2*sqrt(2),
//   and test whether alpha^d == 1 mod p^2 (i.e. e = v_p(alpha^d - 1) >= 2).
// d divides N = p - (2/p): p-1 if p = +-1 mod 8 (split), p+1 if p = +-3 mod 8 (inert).
// Exact integer arithmetic: __int128 suffices (p <= 1e8 => p^2 <= 1e16,
// products <= 2e32 < 2^127). Candidates with e >= 2 are re-checked exactly
// in Python (mod p^3, p^4, ...) since p^3 arithmetic overflows __int128.
// Output: primes with e >= 2, plus counts. Usage: ./wave40_W2_sweep LIMIT
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <vector>
#include <algorithm>
using i128 = __int128_t;
using u64 = uint64_t;

// (a + b*sqrt2) mod m, m up to 1e16; products fit in __int128.
struct Elem { u64 a, b; };
static inline Elem mul(Elem x, Elem y, u64 m) {
    i128 a = (i128)x.a * y.a + (i128)2 * x.b * y.b;
    i128 b = (i128)x.a * y.b + (i128)x.b * y.a;
    return {(u64)(a % m), (u64)(b % m)};
}
static Elem pw(Elem base, u64 exp, u64 m) {
    Elem r{1 % m, 0};
    while (exp) {
        if (exp & 1) r = mul(r, base, m);
        base = mul(base, base, m);
        exp >>= 1;
    }
    return r;
}

int main(int argc, char** argv) {
    u64 LIMIT = argc > 1 ? strtoull(argv[1], nullptr, 10) : 100000000ULL;
    // Odd-only Eratosthenes sieve.
    std::vector<char> is_composite(LIMIT / 2 + 1, 0);
    for (u64 i = 3; i * i <= LIMIT; i += 2) {
        if (!is_composite[i / 2]) {
            for (u64 j = i * i; j <= LIMIT; j += 2 * i) is_composite[j / 2] = 1;
        }
    }
    // Small primes for trial division (up to sqrt(LIMIT+1)), collected
    // during a streaming pass so no full prime list is stored.
    std::vector<u64> small;
    small.push_back(2);
    for (u64 i = 3; i * i <= LIMIT + 1; i += 2)
        if (!is_composite[i / 2]) small.push_back(i);
    long nprimes = 0, ne2 = 0;
    for (u64 pi = 3; pi <= LIMIT; pi += 2) {
        if (is_composite[pi / 2]) continue;
        u64 p = pi;
        nprimes++;
        // N = p - (2/p).
        u64 r8 = p % 8;
        u64 N = (r8 == 1 || r8 == 7) ? p - 1 : p + 1;
        // Factor N by trial division.
        u64 tmp = N;
        std::vector<u64> fac;
        for (u64 q : small) {
            if (q * q > tmp) break;
            if (tmp % q == 0) {
                fac.push_back(q);
                while (tmp % q == 0) tmp /= q;
            }
        }
        if (tmp > 1) fac.push_back(tmp);
        // Order d of alpha mod p: reduce N by prime factors.
        Elem alpha{(3 % p), (2 % p)};
        u64 d = N;
        for (u64 q : fac) {
            while (d % q == 0) {
                Elem t = pw(alpha, d / q, p);
                if (t.a == 1 % p && t.b == 0) d /= q;
                else break;
            }
        }
        // e >= 2 iff alpha^d == 1 mod p^2.
        u64 p2 = p * p;
        Elem t2 = pw(Elem{3 % p2, 2 % p2}, d, p2);
        if (t2.a == 1 % p2 && t2.b == 0) {
            ne2++;
            std::printf("E2 p=%llu d=%llu\n",
                        (unsigned long long)p, (unsigned long long)d);
            std::fflush(stdout);
        }
    }
    std::fprintf(stderr, "primes=%ld e>=2 count=%ld LIMIT=%llu\n",
                 nprimes, ne2, (unsigned long long)LIMIT);
    return 0;
}
