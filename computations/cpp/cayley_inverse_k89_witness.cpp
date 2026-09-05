#include <algorithm>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <utility>
#include <vector>

using u64 = std::uint64_t;

static u64 mul_mod(u64 a, u64 b, u64 p) {
    // The maintained modulus is < 1.5e8, so (a mod p)(b mod p) fits u64.
    return (a % p) * (b % p) % p;
}

static u64 pow_mod(u64 a, u64 e, u64 p) {
    u64 r = 1 % p;
    a %= p;
    while (e) {
        if (e & 1U) r = mul_mod(r, a, p);
        a = mul_mod(a, a, p);
        e >>= 1U;
    }
    return r;
}

static bool is_prime(u64 n) {
    if (n < 2) return false;
    if ((n & 1U) == 0) return n == 2;
    for (u64 d = 3; d <= n / d; d += 2) {
        if (n % d == 0) return false;
    }
    return true;
}

static u64 add_mod(u64 a, u64 b, u64 p) {
    a %= p;
    b %= p;
    return a >= p - b ? a - (p - b) : a + b;
}

static u64 sub_mod(u64 a, u64 b, u64 p) {
    a %= p;
    b %= p;
    return a >= b ? a - b : p - (b - a);
}

int main() {
    constexpr u64 K = 89;
    constexpr u64 p = 143207231;
    constexpr u64 h = 28905841;
    const u64 K4 = K * K * K * K;

    if (!is_prime(p)) throw std::runtime_error("p is not prime");
    if ((p - 1) % K != 0) throw std::runtime_error("p is not split modulo K");
    if (p <= K4) throw std::runtime_error("expected p>K^4");
    if (pow_mod(h, K, p) != 1 || h == 1) {
        throw std::runtime_error("h does not have exact prime order K");
    }

    std::vector<u64> hp(K);
    hp[0] = 1;
    for (u64 a = 1; a < K; ++a) hp[a] = mul_mod(hp[a - 1], h, p);

    const u64 m = (K - 1) / 2;
    std::vector<u64> trace(m + 1);
    for (u64 a = 0; a <= m; ++a) {
        const u64 hinv = (a == 0 ? 1 : hp[K - a]);
        trace[a] = add_mod(hp[a], hinv, p);
    }
    for (u64 a = 0; a <= m; ++a) {
        for (u64 b = a + 1; b <= m; ++b) {
            if (trace[a] == trace[b]) {
                throw std::runtime_error("trace classes are not distinct");
            }
        }
    }

    const u64 tau = trace[1];
    std::vector<u64> centered(m + 1);
    for (u64 a = 0; a <= m; ++a) centered[a] = sub_mod(trace[a], tau, p);
    if (centered[1] != 0) throw std::runtime_error("centering failed");

    std::vector<std::pair<u64, u64>> zero_edges;
    for (u64 a = 0; a <= m; ++a) {
        if (a == 1) continue;
        if (centered[a] == 0) throw std::runtime_error("unexpected valid zero root");
        for (u64 b = a + 1; b <= m; ++b) {
            if (b == 1) continue;
            if (add_mod(centered[a], centered[b], p) == 0) {
                zero_edges.emplace_back(a, b);
            }
        }
    }

    const std::vector<std::pair<u64, u64>> expected{{16, 35}, {20, 33}};
    if (zero_edges != expected) {
        std::cerr << "observed zero edges:";
        for (auto [a, b] : zero_edges) std::cerr << " (" << a << "," << b << ")";
        std::cerr << "\n";
        return 1;
    }

    const std::vector<u64> idx{16, 35, 20, 33};
    u64 e1 = 0;
    for (u64 a : idx) e1 = add_mod(e1, centered[a], p);

    u64 e3 = 0;
    for (int i = 0; i < 4; ++i) {
        for (int j = i + 1; j < 4; ++j) {
            for (int k = j + 1; k < 4; ++k) {
                const u64 term = mul_mod(
                    mul_mod(centered[idx[i]], centered[idx[j]], p),
                    centered[idx[k]], p);
                e3 = add_mod(e3, term, p);
            }
        }
    }
    if (e1 != 0 || e3 != 0) {
        throw std::runtime_error("quartic e1=e3 certificate failed");
    }

    const u64 I_inverse = 2 * zero_edges.size();
    if (I_inverse != 4) throw std::runtime_error("inverse intersection count mismatch");

    if (centered[16] != 49215600ULL || centered[35] != 93991631ULL ||
        centered[20] != 74755068ULL || centered[33] != 68452163ULL) {
        throw std::runtime_error("recorded centered-root values changed");
    }

    std::cout << "PASS K=" << K
              << " p=" << p
              << " h=" << h
              << " p/K^4="
              << static_cast<long double>(p) / static_cast<long double>(K4)
              << " zero_edges=(16,35),(20,33)"
              << " I_inverse=" << I_inverse
              << " e1=e3=0\n";
    return 0;
}
