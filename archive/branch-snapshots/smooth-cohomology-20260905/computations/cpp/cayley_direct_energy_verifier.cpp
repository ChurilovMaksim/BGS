#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <stdexcept>
#include <vector>

using u64 = std::uint64_t;

static u64 mul_mod(u64 a, u64 b, u64 p) {
    u64 out = 0;
    a %= p;
    while (b) {
        if (b & 1U) out = (out >= p - a) ? out - (p - a) : out + a;
        b >>= 1U;
        if (b) a = (a >= p - a) ? a - (p - a) : a + a;
    }
    return out;
}

static u64 pow_mod(u64 a, u64 e, u64 p) {
    u64 out = 1;
    while (e) {
        if (e & 1U) out = mul_mod(out, a, p);
        a = mul_mod(a, a, p);
        e >>= 1U;
    }
    return out;
}

static u64 inv_mod(u64 a, u64 p) {
    if (a % p == 0) throw std::runtime_error("division by zero");
    return pow_mod(a, p - 2, p);
}

static u64 cayley(u64 h, u64 p) {
    if (h == 1) throw std::runtime_error("Cayley singularity");
    return mul_mod((h + 1) % p, inv_mod((h + p - 1) % p, p), p);
}

static bool is_prime(u64 n) {
    if (n < 2) return false;
    if ((n & 1U) == 0) return n == 2;
    for (u64 d = 3; d <= n / d; d += 2)
        if (n % d == 0) return false;
    return true;
}

static u64 primitive_root(u64 p) {
    u64 n = p - 1;
    std::vector<u64> factors;
    for (u64 q = 2; q <= n / q; ++q) {
        if (n % q != 0) continue;
        factors.push_back(q);
        while (n % q == 0) n /= q;
    }
    if (n > 1) factors.push_back(n);
    for (u64 g = 2; g < p; ++g) {
        bool good = true;
        for (u64 q : factors) {
            if (pow_mod(g, (p - 1) / q, p) == 1) {
                good = false;
                break;
            }
        }
        if (good) return g;
    }
    throw std::runtime_error("primitive root not found");
}

struct Expected {
    u64 k, p, energy, max_generic, zero_bin, minus_two_bin, sum_bins;
};

static void verify_design(const Expected& e) {
    if (!is_prime(e.p) || (e.p - 1) % e.k != 0)
        throw std::runtime_error("invalid prime/subgroup design");

    // Exact form of K < p^(3/4)/3: (3K)^4 < p^3.
    const u64 lhs_base = 3 * e.k;
    const u64 lhs = lhs_base * lhs_base * lhs_base * lhs_base;
    const u64 rhs = e.p * e.p * e.p;
    if (!(100 < e.k && lhs < rhs))
        throw std::runtime_error("design outside Stepanov range");

    const u64 g = primitive_root(e.p);
    const u64 generator = pow_mod(g, (e.p - 1) / e.k, e.p);
    if (pow_mod(generator, e.k, e.p) != 1 || generator == 1)
        throw std::runtime_error("subgroup generator order failure");

    std::vector<u64> H(e.k);
    H[0] = 1;
    for (u64 j = 1; j < e.k; ++j)
        H[j] = mul_mod(H[j - 1], generator, e.p);

    std::vector<u64> A;
    A.reserve(e.k - 1);
    for (u64 h : H)
        if (h != 1) A.push_back(cayley(h, e.p));

    std::map<u64, u64> counts;
    for (u64 a : A)
        for (u64 b : A)
            ++counts[(a + b) % e.p];

    u64 energy = 0;
    u64 max_generic = 0;
    for (const auto& [t, multiplicity] : counts) {
        energy += multiplicity * multiplicity;
        if (t != 0 && t != e.p - 2)
            max_generic = std::max(max_generic, multiplicity);
    }

    const u64 zero_bin = counts[0];
    const u64 minus_two_bin = counts[e.p - 2];
    if (energy != e.energy || max_generic != e.max_generic ||
        zero_bin != e.zero_bin || minus_two_bin != e.minus_two_bin ||
        counts.size() != e.sum_bins) {
        throw std::runtime_error("stored direct-energy anchor changed");
    }

    // Exact integer form of max_generic <= 32 K^(2/3).
    const u64 max_cube = max_generic * max_generic * max_generic;
    const u64 source_bound_cube = 32ULL * 32ULL * 32ULL * e.k * e.k;
    if (max_cube > source_bound_cube)
        throw std::runtime_error("generic fiber exceeds Stepanov source bound");

    // Independently verify the bilinear fiber identity on every admissible pair.
    for (u64 x : H) {
        if (x == 1) continue;
        for (u64 y : H) {
            if (y == 1) continue;
            const u64 t = (cayley(x, e.p) + cayley(y, e.p)) % e.p;
            const u64 a = (2 + e.p - t) % e.p;
            const u64 term_xy = mul_mod(a, mul_mod(x, y, e.p), e.p);
            const u64 term_x = mul_mod(t, x, e.p);
            const u64 term_y = mul_mod(t, y, e.p);
            const u64 constant = (e.p - ((2 + t) % e.p)) % e.p;
            if ((term_xy + term_x + term_y + constant) % e.p != 0)
                throw std::runtime_error("bilinear Cayley fiber identity failed");

            // For a xy+b x+c y+d, ad-bc=-4, hence irreducible in odd char.
            const u64 d = constant;
            const u64 determinant =
                (mul_mod(a, d, e.p) + e.p - mul_mod(t, t, e.p)) % e.p;
            if (determinant != (e.p - 4) % e.p)
                throw std::runtime_error("bilinear determinant identity failed");
        }
    }

    std::cout << "PASS direct-energy K=" << e.k
              << " p=" << e.p
              << " energy=" << energy
              << " maxGeneric=" << max_generic
              << " r0=" << zero_bin
              << " rMinus2=" << minus_two_bin
              << " sumBins=" << counts.size() << "\n";
}

int main() {
    // Generated independently from the proof constants; all designs satisfy
    // K>100 and K<p^(3/4)/3.  These are regression anchors, not proof cases.
    const std::vector<Expected> designs = {
        {101, 3637, 55204, 14, 100, 2, 2787},
        {103, 2267, 75418, 17, 102, 8, 2073},
        {109, 2399, 86508, 17, 108, 4, 2237},
        {127, 3049, 127554, 18, 126, 6, 2863},
        {131, 3407, 128934, 18, 130, 6, 3183},
    };
    try {
        for (const auto& e : designs) verify_design(e);
    } catch (const std::exception& ex) {
        std::cerr << "FAIL: " << ex.what() << "\n";
        return 1;
    }
    return 0;
}
