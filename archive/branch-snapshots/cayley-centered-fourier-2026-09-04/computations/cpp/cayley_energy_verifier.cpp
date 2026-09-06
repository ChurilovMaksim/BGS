#include <algorithm>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <vector>

using u64 = std::uint64_t;
static u64 mul_mod(u64 a, u64 b, u64 p) {
    u64 result = 0;
    a %= p;
    while (b) {
        if (b & 1U) {
            // All active designs are far below uint64_t overflow, but this
            // branch-safe form also avoids relying on non-standard __int128.
            result = (result >= p - a) ? result - (p - a) : result + a;
        }
        b >>= 1U;
        if (b) a = (a >= p - a) ? a - (p - a) : a + a;
    }
    return result;
}

static u64 pow_mod(u64 base, u64 exp, u64 p) {
    u64 result = 1 % p;
    base %= p;
    while (exp) {
        if (exp & 1U) result = mul_mod(result, base, p);
        base = mul_mod(base, base, p);
        exp >>= 1U;
    }
    return result;
}

static std::vector<u64> prime_divisors(u64 n) {
    std::vector<u64> out;
    for (u64 d = 2; d * d <= n; ++d) {
        if (n % d != 0) continue;
        out.push_back(d);
        while (n % d == 0) n /= d;
    }
    if (n > 1) out.push_back(n);
    return out;
}

static bool has_exact_order(u64 a, u64 order, u64 p) {
    if (pow_mod(a, order, p) != 1) return false;
    for (u64 q : prime_divisors(order)) {
        if (pow_mod(a, order / q, p) == 1) return false;
    }
    return true;
}

static u64 inv_mod(u64 x, u64 p) {
    if (x % p == 0) throw std::invalid_argument("division by zero in F_p");
    return pow_mod(x, p - 2, p);
}

static u64 cayley(u64 h, u64 p) {
    if (h % p == 1) throw std::invalid_argument("Cayley transform singular at h=1");
    return mul_mod((h + 1) % p, inv_mod((h + p - 1) % p, p), p);
}

struct Audit {
    u64 p;
    u64 k;
    u64 a;
    u64 pair_count;
    u64 energy;
    u64 baseline;
    u64 excess;
    u64 max_multiplicity;
};

static Audit audit_design(u64 p, u64 a, u64 k) {
    if (p < 3 || (p % 2) == 0) throw std::invalid_argument("p must be an odd prime design");
    if ((p - 1) % k != 0) throw std::invalid_argument("K must divide p-1");
    if (!has_exact_order(a, k, p)) throw std::invalid_argument("generator does not have exact order K");

    std::vector<u64> subgroup;
    subgroup.reserve(k);
    u64 h = 1;
    for (u64 i = 0; i < k; ++i) {
        subgroup.push_back(h);
        h = mul_mod(h, a, p);
    }
    if (h != 1) throw std::runtime_error("subgroup did not close");

    std::vector<u64> A;
    A.reserve(k - 1);
    for (u64 x : subgroup) {
        if (x != 1) A.push_back(cayley(x, p));
    }
    std::vector<bool> in_A(p, false);
    for (u64 x : A) {
        if (in_A[x]) throw std::runtime_error("Cayley transform not injective on H\\{1}");
        in_A[x] = true;
    }
    if (in_A[0]) throw std::runtime_error("0 unexpectedly lies in Cayley set");
    for (u64 x : A) {
        if (!in_A[(p - x) % p]) throw std::runtime_error("A != -A");
    }

    std::vector<u64> difference_counts(p, 0);
    for (u64 x : A) {
        for (u64 y : A) {
            if (x == y) continue;
            ++difference_counts[(x + p - y) % p];
        }
    }

    std::vector<u64> collision_counts(p, 0);
    for (u64 u : subgroup) {
        if (u == 1) continue;
        for (u64 v : subgroup) {
            if (v == 1 || u == v) continue;
            const u64 cu = cayley(u, p);
            const u64 cv = cayley(v, p);
            const u64 delta = (cu + p - cv) % p;
            const u64 t = mul_mod(2, inv_mod(delta, p), p);
            ++collision_counts[t];
        }
    }

    u64 pair_count = 0;
    u64 difference_energy = 0;
    u64 collision_energy = 0;
    u64 max_multiplicity = 0;
    for (u64 t = 1; t < p; ++t) {
        pair_count += collision_counts[t];
        difference_energy += difference_counts[t] * difference_counts[t];
        collision_energy += collision_counts[t] * collision_counts[t];
        max_multiplicity = std::max(max_multiplicity, difference_counts[t]);
    }
    if (difference_energy != collision_energy) {
        throw std::runtime_error("Cayley difference energy and mixed collision energy disagree");
    }
    const u64 expected_pairs = (k - 1) * (k - 2);
    if (pair_count != expected_pairs) throw std::runtime_error("admissible pair count mismatch");

    const u64 baseline = (k - 1) * (2 * k - 5);
    if (collision_energy < baseline) throw std::runtime_error("energy below forced baseline");

    return {p, k, a, pair_count, collision_energy, baseline,
            collision_energy - baseline, max_multiplicity};
}

struct Expected {
    u64 p, a, k, energy, max_multiplicity;
    const char* role;
};

int main() {
    const std::vector<Expected> designs = {
        {199, 139, 11, 170, 2, "generic K=11 control"},
        {67, 64, 11, 218, 4, "exceptional K=11 control"},
        {521, 101, 13, 252, 2, "generic K=13 control"},
        {53, 10, 13, 460, 6, "exceptional K=13 control"},
        {461, 23, 23, 1190, 6, "K=23 non-uniformity witness"},
    };

    for (const auto& expected : designs) {
        const Audit a = audit_design(expected.p, expected.a, expected.k);
        if (a.energy != expected.energy || a.max_multiplicity != expected.max_multiplicity) {
            std::cerr << "FAIL N=" << a.p << " K=" << a.k
                      << ": energy=" << a.energy << " maxMultiplicity=" << a.max_multiplicity << "\n";
            return 1;
        }
        std::cout << "PASS N=" << a.p
                  << " K=" << a.k
                  << " role=\"" << expected.role << "\""
                  << " pairs=" << a.pair_count
                  << " energy=" << a.energy
                  << " baseline=" << a.baseline
                  << " excess=" << a.excess
                  << " maxMultiplicity=" << a.max_multiplicity
                  << "\n";
    }
    return 0;
}
