#include <cmath>
#include <complex>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <tuple>
#include <vector>

using Complex = std::complex<double>;
constexpr double PI = 3.141592653589793238462643383279502884;

long long mod_pow(long long base, long long exponent, long long modulus) {
    long long result = 1 % modulus;
    base %= modulus;
    while (exponent > 0) {
        if (exponent & 1LL) {
            result = result * base % modulus;
        }
        base = base * base % modulus;
        exponent >>= 1;
    }
    return result;
}

std::vector<int> prime_divisors(int value) {
    std::vector<int> divisors;
    for (int candidate = 2; candidate * candidate <= value; ++candidate) {
        if (value % candidate != 0) {
            continue;
        }
        divisors.push_back(candidate);
        while (value % candidate == 0) {
            value /= candidate;
        }
    }
    if (value > 1) {
        divisors.push_back(value);
    }
    return divisors;
}

int primitive_root(int prime) {
    const auto divisors = prime_divisors(prime - 1);
    for (int generator = 2; generator < prime; ++generator) {
        bool primitive = true;
        for (int divisor : divisors) {
            if (mod_pow(generator, (prime - 1) / divisor, prime) == 1) {
                primitive = false;
                break;
            }
        }
        if (primitive) {
            return generator;
        }
    }
    throw std::runtime_error("primitive root not found");
}

struct PairData {
    int first_key;
    int second_key;
    int phase_difference;
};

struct VerificationResult {
    int primitive_root;
    int dimension;
    double left_side;
    Complex sigma_four;
    long long constraint_variety_count;
};

VerificationResult verify_case(
    int prime,
    int subgroup_generator,
    int subgroup_order,
    int q
) {
    const int generator = primitive_root(prime);
    std::vector<int> dlog(prime, -1);
    int value = 1;
    for (int exponent = 0; exponent < prime - 1; ++exponent) {
        dlog[value] = exponent;
        value = static_cast<int>(1LL * value * generator % prime);
    }

    std::vector<int> character_indices;
    for (int k = 0; k < prime - 1; k += subgroup_order) {
        character_indices.push_back(k);
    }
    const int dimension = static_cast<int>(character_indices.size());

    std::vector<int> x_values;
    for (int x = 2; x < prime; ++x) {
        x_values.push_back(x);
    }

    double left_side = 0.0;
    for (int first_index : character_indices) {
        for (int second_index : character_indices) {
            Complex jacobi_sum = 0.0;
            for (int x : x_values) {
                const double angle = 2.0 * PI * (
                    static_cast<double>(q * x) / prime
                    - static_cast<double>(first_index * dlog[x]) / (prime - 1)
                    + static_cast<double>(second_index * dlog[x - 1]) / (prime - 1)
                );
                jacobi_sum += std::polar(1.0, angle);
            }
            const double squared_norm = std::norm(jacobi_sum);
            left_side += squared_norm * squared_norm;
        }
    }

    std::vector<char> in_subgroup(prime, 0);
    value = 1;
    for (int exponent = 0; exponent < subgroup_order; ++exponent) {
        in_subgroup[value] = 1;
        value = static_cast<int>(1LL * value * subgroup_generator % prime);
    }

    std::vector<PairData> pairs;
    pairs.reserve(x_values.size() * x_values.size());
    for (int x : x_values) {
        for (int y : x_values) {
            const int first_key = static_cast<int>(
                1LL * x * mod_pow(y, prime - 2, prime) % prime
            );
            const int second_key = static_cast<int>(
                1LL * (x - 1) * mod_pow(y - 1, prime - 2, prime) % prime
            );
            int difference = (x - y) % prime;
            if (difference < 0) {
                difference += prime;
            }
            pairs.push_back({first_key, second_key, difference});
        }
    }

    Complex sigma_four = 0.0;
    long long constraint_variety_count = 0;
    for (const PairData& left_pair : pairs) {
        const Complex left_phase = std::polar(
            1.0,
            2.0 * PI * q * left_pair.phase_difference / prime
        );
        for (const PairData& right_pair : pairs) {
            const int first_product = static_cast<int>(
                1LL * left_pair.first_key * right_pair.first_key % prime
            );
            const int second_product = static_cast<int>(
                1LL * left_pair.second_key * right_pair.second_key % prime
            );
            if (!in_subgroup[first_product] || !in_subgroup[second_product]) {
                continue;
            }
            ++constraint_variety_count;
            const Complex right_phase = std::polar(
                1.0,
                2.0 * PI * q * right_pair.phase_difference / prime
            );
            sigma_four += left_phase * right_phase;
        }
    }

    return {generator, dimension, left_side, sigma_four, constraint_variety_count};
}

int main() {
    const std::vector<std::tuple<int, int, int, int>> cases = {
        {23, 2, 11, 1},
        {53, 10, 13, 1},
        {53, 10, 13, 7},
    };

    std::cout << std::setprecision(17);
    for (const auto& [prime, subgroup_generator, subgroup_order, q] : cases) {
        const auto result = verify_case(prime, subgroup_generator, subgroup_order, q);
        const Complex right_side =
            static_cast<double>(result.dimension * result.dimension)
            * result.sigma_four;
        std::cout
            << "N=" << prime
            << " K=" << subgroup_order
            << " q=" << q
            << " primitive_root=" << result.primitive_root
            << " m=" << result.dimension
            << " lhs=" << result.left_side
            << " rhs_real=" << right_side.real()
            << " rhs_imag=" << right_side.imag()
            << " abs_deviation=" << std::abs(result.left_side - right_side)
            << " variety_count=" << result.constraint_variety_count
            << '\n';
    }
}
