#include <boost/multiprecision/cpp_int.hpp>

#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <utility>
#include <vector>

using boost::multiprecision::cpp_int;
using u64 = std::uint64_t;

static cpp_int mod_norm(cpp_int a, const cpp_int& p) {
    a %= p;
    if (a < 0) a += p;
    return a;
}

static cpp_int pow_mod(cpp_int base, cpp_int exp, const cpp_int& p) {
    cpp_int result = 1;
    base = mod_norm(base, p);
    while (exp > 0) {
        if ((exp & 1) != 0) result = (result * base) % p;
        base = (base * base) % p;
        exp >>= 1;
    }
    return result;
}

static cpp_int gcd_big(cpp_int a, cpp_int b) {
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    while (b != 0) {
        cpp_int r = a % b;
        a = b;
        b = r;
    }
    return a;
}

static bool trial_prime(u64 n) {
    if (n < 2) return false;
    if ((n & 1U) == 0) return n == 2;
    for (u64 d = 3; d <= n / d; d += 2) {
        if (n % d == 0) return false;
    }
    return true;
}

static cpp_int fibonacci(unsigned n) {
    cpp_int a = 0, b = 1;
    for (unsigned i = 0; i < n; ++i) {
        cpp_int next = a + b;
        a = b;
        b = next;
    }
    return a;
}

static cpp_int cayley(const cpp_int& z, const cpp_int& p) {
    const cpp_int numerator = mod_norm(z + 1, p);
    const cpp_int denominator = mod_norm(z - 1, p);
    if (denominator == 0) throw std::runtime_error("Cayley singularity");
    const cpp_int inverse = pow_mod(denominator, p - 2, p);
    return (numerator * inverse) % p;
}

static void verify_lucas_primality_certificate(const cpp_int& p) {
    const std::vector<std::pair<u64, unsigned>> factors = {
        {2, 3}, {11, 1}, {89, 1}, {131, 1}, {199, 1}, {521, 1},
        {2081, 1}, {9901, 1}, {19801, 1}, {24571, 1},
    };

    cpp_int product = 1;
    for (const auto& [q, exponent] : factors) {
        if (!trial_prime(q)) throw std::runtime_error("non-prime p-1 factor");
        for (unsigned e = 0; e < exponent; ++e) product *= q;
    }
    if (product != p - 1) throw std::runtime_error("incomplete p-1 factorization");

    const cpp_int base = 3;
    if (pow_mod(base, p - 1, p) != 1) {
        throw std::runtime_error("Lucas primality Fermat condition failed");
    }
    for (const auto& [q, exponent] : factors) {
        (void)exponent;
        const cpp_int residue = pow_mod(base, (p - 1) / q, p);
        if (gcd_big(residue - 1, p) != 1) {
            throw std::runtime_error("Lucas primality gcd condition failed");
        }
    }
}

int main() {
    constexpr unsigned K = 131;
    const cpp_int p("1066340417491710595814572169");
    const cpp_int h("188706367382658195937453923");

    if (fibonacci(K) != p) {
        std::cerr << "FAIL: F_131 literal mismatch\n";
        return 1;
    }

    // Together with the complete p-1 factorization, these are the hypotheses
    // of the Lucas primality criterion; this is a certificate check, not a
    // probable-prime test.
    verify_lucas_primality_certificate(p);

    if ((p - 1) % K != 0) {
        std::cerr << "FAIL: K does not divide p-1\n";
        return 1;
    }
    if (mod_norm(h * h + 3 * h + 1, p) != 0) {
        std::cerr << "FAIL: h^2+3h+1 != 0 mod p\n";
        return 1;
    }
    if (pow_mod(h, K, p) != 1 || h == 1) {
        std::cerr << "FAIL: h does not have exact prime order 131\n";
        return 1;
    }

    std::vector<cpp_int> powers(K);
    powers[0] = 1;
    for (unsigned e = 1; e < K; ++e) powers[e] = (powers[e - 1] * h) % p;

    std::vector<cpp_int> A;
    A.reserve(K - 1);
    std::vector<cpp_int> cayley_by_exp(K);
    for (unsigned e = 1; e < K; ++e) {
        cayley_by_exp[e] = cayley(powers[e], p);
        A.push_back(cayley_by_exp[e]);
    }
    const std::set<cpp_int> unique_A(A.begin(), A.end());
    if (unique_A.size() != K - 1) {
        std::cerr << "FAIL: Cayley set is not injective\n";
        return 1;
    }

    std::map<cpp_int, u64> counts;
    for (const cpp_int& x : A) {
        for (const cpp_int& y : A) {
            if (x == y) continue;
            ++counts[mod_norm(x - y, p)];
        }
    }

    u64 energy = 0;
    u64 max_multiplicity = 0;
    std::map<u64, u64> histogram;
    for (const auto& [difference, multiplicity] : counts) {
        (void)difference;
        energy += multiplicity * multiplicity;
        max_multiplicity = std::max(max_multiplicity, multiplicity);
        ++histogram[multiplicity];
    }

    const u64 baseline = static_cast<u64>(K - 1) * (2 * K - 5);
    if (energy != 33442 || baseline != 33410 || energy - baseline != 32 ||
        max_multiplicity != 4 || counts.size() != 8444 ||
        histogram[1] != 126 || histogram[2] != 8312 ||
        histogram[3] != 4 || histogram[4] != 2) {
        std::cerr << "FAIL: giant Fibonacci energy certificate changed\n";
        return 1;
    }

    const cpp_int target = mod_norm(cayley_by_exp[1] - cayley_by_exp[K - 1], p);
    std::vector<std::pair<unsigned, unsigned>> pairs;
    for (unsigned a = 1; a < K; ++a) {
        for (unsigned b = 1; b < K; ++b) {
            if (a == b) continue;
            if (mod_norm(cayley_by_exp[a] - cayley_by_exp[b], p) == target) {
                pairs.emplace_back(a, b);
            }
        }
    }
    const std::vector<std::pair<unsigned, unsigned>> expected_pairs = {
        {1, 130}, {2, 1}, {130, 129},
    };
    if (pairs != expected_pairs) {
        std::cerr << "FAIL: explicit Fibonacci collision class changed\n";
        return 1;
    }

    std::cout << "PASS K=131 p=" << p
              << " F_K=prime-by-Lucas-certificate"
              << " energy=" << energy
              << " baseline=" << baseline
              << " excess=" << (energy - baseline)
              << " maxMultiplicity=" << max_multiplicity
              << " differenceClasses=" << counts.size()
              << "\n";
    return 0;
}
