#include <algorithm>
#include <cmath>
#include <complex>
#include <iomanip>
#include <iostream>
#include <map>
#include <stdexcept>
#include <tuple>
#include <utility>
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
    int difference;
};

struct KeyRecord {
    int first_key;
    int second_key;
    int difference;
    long long multiplicity;

    bool is_diagonal() const {
        return first_key == 1 && second_key == 1;
    }
};

struct CouplingClasses {
    long long off_to_off = 0;
    long long diagonal_to_off = 0;
    long long off_to_diagonal = 0;
    long long diagonal_to_diagonal = 0;
};

struct GeometryResult {
    std::vector<long long> distribution;
    std::vector<long long> key_distribution;
    CouplingClasses classes;
    std::size_t collapsed_key_count;
};

std::vector<char> subgroup_indicator(
    int prime,
    int subgroup_generator,
    int subgroup_order
) {
    std::vector<char> in_subgroup(prime, 0);
    int value = 1;
    for (int exponent = 0; exponent < subgroup_order; ++exponent) {
        if (in_subgroup[value]) {
            throw std::runtime_error("subgroup generator has order smaller than K");
        }
        in_subgroup[value] = 1;
        value = static_cast<int>(1LL * value * subgroup_generator % prime);
    }
    if (value != 1) {
        throw std::runtime_error("subgroup generator does not close after K steps");
    }
    return in_subgroup;
}

std::vector<PairData> build_pairs(int prime) {
    std::vector<PairData> pairs;
    pairs.reserve(static_cast<std::size_t>(prime - 2) * (prime - 2));
    for (int x = 2; x < prime; ++x) {
        for (int y = 2; y < prime; ++y) {
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
    return pairs;
}

GeometryResult build_geometry(
    int prime,
    int subgroup_generator,
    int subgroup_order
) {
    const auto in_subgroup = subgroup_indicator(
        prime, subgroup_generator, subgroup_order
    );
    const auto pairs = build_pairs(prime);

    std::vector<long long> direct(prime, 0);
    for (const PairData& left : pairs) {
        for (const PairData& right : pairs) {
            const int first_product = static_cast<int>(
                1LL * left.first_key * right.first_key % prime
            );
            const int second_product = static_cast<int>(
                1LL * left.second_key * right.second_key % prime
            );
            if (!in_subgroup[first_product] || !in_subgroup[second_product]) {
                continue;
            }
            direct[(left.difference + right.difference) % prime] += 1;
        }
    }

    std::map<std::pair<int, int>, KeyRecord> table;
    for (const PairData& pair : pairs) {
        const std::pair<int, int> key = {pair.first_key, pair.second_key};
        auto [it, inserted] = table.emplace(
            key,
            KeyRecord{pair.first_key, pair.second_key, pair.difference, 1}
        );
        if (inserted) {
            continue;
        }
        if (key != std::pair<int, int>{1, 1}
            || it->second.difference != 0
            || pair.difference != 0) {
            throw std::runtime_error("unexpected repeated off-diagonal key");
        }
        it->second.multiplicity += 1;
    }

    const auto diagonal_it = table.find({1, 1});
    if (diagonal_it == table.end()
        || diagonal_it->second.multiplicity != prime - 2) {
        throw std::runtime_error("incorrect diagonal key multiplicity");
    }

    std::vector<KeyRecord> records;
    records.reserve(table.size());
    for (const auto& [key, record] : table) {
        (void)key;
        records.push_back(record);
    }

    std::vector<long long> collapsed(prime, 0);
    CouplingClasses classes;
    for (const KeyRecord& left : records) {
        for (const KeyRecord& right : records) {
            const int first_product = static_cast<int>(
                1LL * left.first_key * right.first_key % prime
            );
            const int second_product = static_cast<int>(
                1LL * left.second_key * right.second_key % prime
            );
            if (!in_subgroup[first_product] || !in_subgroup[second_product]) {
                continue;
            }

            const long long weight = left.multiplicity * right.multiplicity;
            collapsed[(left.difference + right.difference) % prime] += weight;

            if (left.is_diagonal() && right.is_diagonal()) {
                classes.diagonal_to_diagonal += weight;
            } else if (left.is_diagonal()) {
                classes.diagonal_to_off += weight;
            } else if (right.is_diagonal()) {
                classes.off_to_diagonal += weight;
            } else {
                classes.off_to_off += weight;
            }
        }
    }

    if (direct != collapsed) {
        throw std::runtime_error("direct B(t) and collapsed key-table B(t) disagree");
    }

    return {direct, collapsed, classes, records.size()};
}

std::tuple<int, int, double> jacobi_fourth(
    int prime,
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

    double fourth = 0.0;
    for (int first_index : character_indices) {
        for (int second_index : character_indices) {
            Complex jacobi_sum = 0.0;
            for (int x = 2; x < prime; ++x) {
                const double angle = 2.0 * PI * (
                    static_cast<double>(q * x) / prime
                    - static_cast<double>(first_index * dlog[x]) / (prime - 1)
                    + static_cast<double>(second_index * dlog[x - 1]) / (prime - 1)
                );
                jacobi_sum += std::polar(1.0, angle);
            }
            const double squared_norm = std::norm(jacobi_sum);
            fourth += squared_norm * squared_norm;
        }
    }

    return {generator, static_cast<int>(character_indices.size()), fourth};
}

long long sum_values(const std::vector<long long>& values) {
    long long result = 0;
    for (long long value : values) {
        result += value;
    }
    return result;
}

long long squared_energy(const std::vector<long long>& values) {
    long long result = 0;
    for (long long value : values) {
        result += value * value;
    }
    return result;
}

Complex sigma_from_distribution(
    const std::vector<long long>& distribution,
    int prime,
    int q
) {
    Complex sigma = 0.0;
    for (int t = 0; t < prime; ++t) {
        sigma += static_cast<double>(distribution[t])
            * std::polar(1.0, 2.0 * PI * q * t / prime);
    }
    return sigma;
}

int main() {
    const std::vector<std::tuple<int, int, int, std::vector<int>>> designs = {
        {23, 2, 11, {1}},
        {53, 10, 13, {1, 7}},
    };

    std::cout << std::setprecision(17);
    for (const auto& [prime, subgroup_generator, subgroup_order, q_values] : designs) {
        const GeometryResult geometry = build_geometry(
            prime, subgroup_generator, subgroup_order
        );
        const long long variety_count = sum_values(geometry.distribution);
        const long long energy = squared_energy(geometry.distribution);
        const long long expected_mixed =
            1LL * (prime - 2) * (subgroup_order - 1) * (subgroup_order - 2);

        std::cout
            << "N=" << prime
            << " K=" << subgroup_order
            << " keys=" << geometry.collapsed_key_count
            << " V4=" << variety_count
            << " Z0=" << geometry.distribution[0]
            << " energy=" << energy
            << " diag_to_off=" << geometry.classes.diagonal_to_off
            << " off_to_diag=" << geometry.classes.off_to_diagonal
            << " diag_to_diag=" << geometry.classes.diagonal_to_diagonal
            << " expected_each_mixed=" << expected_mixed
            << '\n';

        if (geometry.classes.diagonal_to_off != expected_mixed
            || geometry.classes.off_to_diagonal != expected_mixed
            || geometry.classes.diagonal_to_diagonal != 1LL * (prime - 2) * (prime - 2)) {
            throw std::runtime_error("ordered diagonal coupling class check failed");
        }

        for (int q : q_values) {
            const auto [generator, dimension, left_side] = jacobi_fourth(
                prime, subgroup_order, q
            );
            const Complex sigma = sigma_from_distribution(
                geometry.distribution, prime, q
            );
            const Complex right_side = static_cast<double>(dimension * dimension) * sigma;
            const double relative_deviation =
                std::abs(left_side - right_side) / std::max(std::abs(left_side), 1.0);
            std::cout
                << "  q=" << q
                << " primitive_root=" << generator
                << " m=" << dimension
                << " lhs=" << left_side
                << " rhs_real=" << right_side.real()
                << " rhs_imag=" << right_side.imag()
                << " relative_deviation=" << relative_deviation
                << '\n';
            if (relative_deviation >= 1e-11) {
                throw std::runtime_error("fourth-moment factorization regression");
            }
        }
    }
    return 0;
}
