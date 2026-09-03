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
    std::vector<int> factors;
    for (int candidate = 2; candidate * candidate <= value; ++candidate) {
        if (value % candidate != 0) {
            continue;
        }
        factors.push_back(candidate);
        while (value % candidate == 0) {
            value /= candidate;
        }
    }
    if (value > 1) {
        factors.push_back(value);
    }
    return factors;
}

int primitive_root(int prime) {
    const auto factors = prime_divisors(prime - 1);
    for (int generator = 2; generator < prime; ++generator) {
        bool ok = true;
        for (int factor : factors) {
            if (mod_pow(generator, (prime - 1) / factor, prime) == 1) {
                ok = false;
                break;
            }
        }
        if (ok) {
            return generator;
        }
    }
    throw std::runtime_error("primitive root not found");
}

std::vector<int> subgroup_elements(int prime, int generator, int order) {
    if ((prime - 1) % order != 0) {
        throw std::runtime_error("K must divide N-1");
    }
    std::vector<int> values;
    values.reserve(order);
    int value = 1;
    for (int step = 0; step < order; ++step) {
        if (std::find(values.begin(), values.end(), value) != values.end()) {
            throw std::runtime_error("subgroup generator has order smaller than K");
        }
        values.push_back(value);
        value = static_cast<int>(1LL * value * generator % prime);
    }
    if (value != 1) {
        throw std::runtime_error("subgroup generator does not have exact order K");
    }
    std::sort(values.begin(), values.end());
    return values;
}

std::vector<int> inverse_table(int prime) {
    std::vector<int> inverse(prime, 0);
    for (int value = 1; value < prime; ++value) {
        inverse[value] = static_cast<int>(mod_pow(value, prime - 2, prime));
    }
    return inverse;
}

struct KeyRecord {
    int u;
    int v;
    int difference;
    long long multiplicity;

    bool is_diagonal() const {
        return u == 1 && v == 1;
    }

    bool operator==(const KeyRecord&) const = default;
};

struct CouplingClasses {
    long long off_to_off = 0;
    long long diagonal_to_off = 0;
    long long off_to_diagonal = 0;
    long long diagonal_to_diagonal = 0;

    bool operator==(const CouplingClasses&) const = default;
};

struct DistributionResult {
    std::vector<long long> distribution;
    CouplingClasses classes;
};

int key_difference(int prime, int u, int v) {
    if (u == v || u == 0 || v == 0 || u == 1 || v == 1) {
        throw std::runtime_error("invalid off-diagonal key");
    }
    const long long numerator = 1LL * (u - 1) * (v - 1) % prime;
    const int denominator = (v - u + prime) % prime;
    return static_cast<int>(
        numerator * mod_pow(denominator, prime - 2, prime) % prime
    );
}

std::vector<KeyRecord> explicit_key_table(int prime) {
    std::vector<KeyRecord> records;
    records.reserve(1 + (prime - 2) * (prime - 3));
    records.push_back({1, 1, 0, prime - 2});
    for (int u = 2; u < prime; ++u) {
        for (int v = 2; v < prime; ++v) {
            if (u == v) {
                continue;
            }
            records.push_back({u, v, key_difference(prime, u, v), 1});
        }
    }
    return records;
}

std::vector<KeyRecord> original_pair_key_table(int prime) {
    std::map<std::pair<int, int>, KeyRecord> table;
    for (int x = 2; x < prime; ++x) {
        for (int y = 2; y < prime; ++y) {
            const int u = static_cast<int>(
                1LL * x * mod_pow(y, prime - 2, prime) % prime
            );
            const int v = static_cast<int>(
                1LL * (x - 1) * mod_pow(y - 1, prime - 2, prime) % prime
            );
            const int difference = (x - y + prime) % prime;
            const std::pair<int, int> key{u, v};
            auto [it, inserted] = table.emplace(
                key, KeyRecord{u, v, difference, 1}
            );
            if (inserted) {
                continue;
            }
            if (key != std::pair<int, int>{1, 1}
                || it->second.difference != 0
                || difference != 0) {
                throw std::runtime_error("unexpected repeated off-diagonal key");
            }
            it->second.multiplicity += 1;
        }
    }

    std::vector<KeyRecord> records;
    records.reserve(table.size());
    for (const auto& [key, record] : table) {
        (void)key;
        records.push_back(record);
    }
    return records;
}

std::map<std::pair<int, int>, KeyRecord> record_map(
    const std::vector<KeyRecord>& records
) {
    std::map<std::pair<int, int>, KeyRecord> result;
    for (const KeyRecord& record : records) {
        result[{record.u, record.v}] = record;
    }
    return result;
}

DistributionResult direct_distribution(
    int prime,
    const std::vector<int>& subgroup,
    const std::vector<KeyRecord>& records
) {
    std::vector<char> in_subgroup(prime, 0);
    for (int value : subgroup) {
        in_subgroup[value] = 1;
    }

    DistributionResult result{std::vector<long long>(prime, 0), {}};
    for (const KeyRecord& left : records) {
        for (const KeyRecord& right : records) {
            if (!in_subgroup[1LL * left.u * right.u % prime]
                || !in_subgroup[1LL * left.v * right.v % prime]) {
                continue;
            }
            const long long weight = left.multiplicity * right.multiplicity;
            result.distribution[(left.difference + right.difference) % prime]
                += weight;
            if (left.is_diagonal() && right.is_diagonal()) {
                result.classes.diagonal_to_diagonal += weight;
            } else if (left.is_diagonal()) {
                result.classes.diagonal_to_off += weight;
            } else if (right.is_diagonal()) {
                result.classes.off_to_diagonal += weight;
            } else {
                result.classes.off_to_off += weight;
            }
        }
    }
    return result;
}

DistributionResult fast_distribution(
    int prime,
    const std::vector<int>& subgroup
) {
    const auto inverse = inverse_table(prime);
    const int side = prime - 2;

    std::vector<std::vector<int>> difference(side, std::vector<int>(side, -1));
    std::vector<std::vector<int>> lookup(prime, std::vector<int>(prime, -1));
    for (int i = 0; i < side; ++i) {
        const int u = i + 2;
        for (int j = 0; j < side; ++j) {
            const int v = j + 2;
            if (u == v) {
                continue;
            }
            const int d = key_difference(prime, u, v);
            difference[i][j] = d;
            lookup[u][v] = d;
        }
    }

    DistributionResult result{std::vector<long long>(prime, 0), {}};
    for (int h1 : subgroup) {
        for (int h2 : subgroup) {
            for (int i = 0; i < side; ++i) {
                const int u = i + 2;
                const int partner_u = static_cast<int>(1LL * h1 * inverse[u] % prime);
                for (int j = 0; j < side; ++j) {
                    const int d1 = difference[i][j];
                    if (d1 < 0) {
                        continue;
                    }
                    const int v = j + 2;
                    const int partner_v = static_cast<int>(
                        1LL * h2 * inverse[v] % prime
                    );
                    const int d2 = lookup[partner_u][partner_v];
                    if (d2 < 0) {
                        continue;
                    }
                    result.distribution[(d1 + d2) % prime] += 1;
                    result.classes.off_to_off += 1;
                }
            }
        }
    }

    std::vector<long long> mixed(prime, 0);
    for (int u : subgroup) {
        if (u == 1) {
            continue;
        }
        for (int v : subgroup) {
            if (v == 1 || u == v) {
                continue;
            }
            mixed[key_difference(prime, u, v)] += 1;
        }
    }

    const long long diagonal_weight = prime - 2;
    long long mixed_total = 0;
    for (int t = 0; t < prime; ++t) {
        result.distribution[t] += 2 * diagonal_weight * mixed[t];
        mixed_total += mixed[t];
    }
    result.distribution[0] += diagonal_weight * diagonal_weight;
    result.classes.diagonal_to_off = diagonal_weight * mixed_total;
    result.classes.off_to_diagonal = diagonal_weight * mixed_total;
    result.classes.diagonal_to_diagonal = diagonal_weight * diagonal_weight;
    return result;
}

long long expected_off_total(int prime, int order) {
    return 1LL * order * order * (prime - 2) * (prime - 3)
        - 3LL * order * (order - 1) * (prime - 3)
        + 2LL * (order - 1) * (order - 2);
}

long long variety_count_formula(int prime, int order) {
    return 1LL * (order * order + 1) * prime * prime
        - 1LL * (6 * order * order + 3 * order) * prime
        + 13LL * order * order
        - 3LL * order;
}

struct CharacterData {
    int primitive;
    std::vector<int> exponents;
    std::vector<std::vector<Complex>> characters;
};

CharacterData character_table(int prime, int subgroup_order) {
    const int generator = primitive_root(prime);
    std::vector<int> dlog(prime, -1);
    int value = 1;
    for (int exponent = 0; exponent < prime - 1; ++exponent) {
        dlog[value] = exponent;
        value = static_cast<int>(1LL * value * generator % prime);
    }

    std::vector<int> exponents;
    for (int exponent = 0; exponent < prime - 1; exponent += subgroup_order) {
        exponents.push_back(exponent);
    }

    std::vector<std::vector<Complex>> characters(
        exponents.size(), std::vector<Complex>(prime, Complex{0.0, 0.0})
    );
    for (std::size_t row = 0; row < exponents.size(); ++row) {
        for (int x = 1; x < prime; ++x) {
            const double angle = 2.0 * PI * exponents[row] * dlog[x] / (prime - 1);
            characters[row][x] = std::polar(1.0, angle);
        }
    }
    return {generator, exponents, characters};
}

struct TwistCollapseResult {
    double frequency_max_relative_deviation;
    double time_max_relative_deviation;
};

TwistCollapseResult verify_twist_collapse(
    int prime,
    int subgroup_order,
    const std::vector<KeyRecord>& records,
    const std::vector<long long>& distribution
) {
    const CharacterData data = character_table(prime, subgroup_order);
    const int dimension = static_cast<int>(data.exponents.size());
    const int twist_count = dimension * dimension;

    std::vector<std::vector<Complex>> amplitude(
        twist_count, std::vector<Complex>(prime, Complex{0.0, 0.0})
    );
    for (const KeyRecord& record : records) {
        for (int first = 0; first < dimension; ++first) {
            for (int second = 0; second < dimension; ++second) {
                const int twist = first * dimension + second;
                amplitude[twist][record.difference] += static_cast<double>(record.multiplicity)
                    * data.characters[first][record.u]
                    * data.characters[second][record.v];
            }
        }
    }

    std::vector<std::vector<Complex>> transform(
        twist_count, std::vector<Complex>(prime, Complex{0.0, 0.0})
    );
    for (int twist = 0; twist < twist_count; ++twist) {
        for (int xi = 0; xi < prime; ++xi) {
            Complex sum = 0.0;
            for (int d = 0; d < prime; ++d) {
                sum += amplitude[twist][d]
                    * std::polar(1.0, -2.0 * PI * xi * d / prime);
            }
            transform[twist][xi] = sum;
        }
    }

    double frequency_max = 0.0;
    double frequency_scale = 1.0;
    for (int xi = 0; xi < prime; ++xi) {
        Complex left = 0.0;
        Complex b_hat = 0.0;
        for (int twist = 0; twist < twist_count; ++twist) {
            left += transform[twist][xi] * transform[twist][xi];
        }
        for (int t = 0; t < prime; ++t) {
            b_hat += static_cast<double>(distribution[t])
                * std::polar(1.0, -2.0 * PI * xi * t / prime);
        }
        const Complex right = static_cast<double>(dimension * dimension) * b_hat;
        frequency_max = std::max(frequency_max, std::abs(left - right));
        frequency_scale = std::max(frequency_scale, std::abs(right));
    }

    std::vector<Complex> time_left(prime, Complex{0.0, 0.0});
    for (int twist = 0; twist < twist_count; ++twist) {
        for (int d1 = 0; d1 < prime; ++d1) {
            for (int d2 = 0; d2 < prime; ++d2) {
                time_left[(d1 + d2) % prime] +=
                    amplitude[twist][d1] * amplitude[twist][d2];
            }
        }
    }

    double time_max = 0.0;
    double time_scale = 1.0;
    for (int t = 0; t < prime; ++t) {
        const Complex right = static_cast<double>(dimension * dimension)
            * distribution[t];
        time_max = std::max(time_max, std::abs(time_left[t] - right));
        time_scale = std::max(time_scale, std::abs(right));
    }

    return {frequency_max / frequency_scale, time_max / time_scale};
}

std::tuple<int, int, double> jacobi_fourth(
    int prime,
    int subgroup_order,
    int q
) {
    const CharacterData data = character_table(prime, subgroup_order);
    const int dimension = static_cast<int>(data.exponents.size());
    double total = 0.0;
    for (int first = 0; first < dimension; ++first) {
        for (int second = 0; second < dimension; ++second) {
            Complex sum = 0.0;
            for (int x = 2; x < prime; ++x) {
                sum += std::conj(data.characters[first][x])
                    * data.characters[second][x - 1]
                    * std::polar(1.0, 2.0 * PI * q * x / prime);
            }
            const double norm = std::norm(sum);
            total += norm * norm;
        }
    }
    return {data.primitive, dimension, total};
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

long long squared_energy(const std::vector<long long>& values) {
    long long result = 0;
    for (long long value : values) {
        result += value * value;
    }
    return result;
}

int main() {
    const std::vector<std::tuple<int, int, int, std::vector<int>>> designs = {
        {23, 2, 11, {1}},
        {53, 10, 13, {1, 7}},
        {199, 139, 11, {1, 7}},
        {461, 23, 23, {1}},
    };

    std::cout << std::setprecision(17);
    for (const auto& [prime, subgroup_generator, subgroup_order, q_values] : designs) {
        const auto subgroup = subgroup_elements(
            prime, subgroup_generator, subgroup_order
        );
        const auto records = explicit_key_table(prime);
        const DistributionResult fast = fast_distribution(prime, subgroup);

        if (prime <= 53) {
            const auto original = original_pair_key_table(prime);
            if (record_map(original) != record_map(records)) {
                throw std::runtime_error("original pair collapse disagrees with explicit keys");
            }
            const DistributionResult direct = direct_distribution(
                prime, subgroup, records
            );
            if (direct.distribution != fast.distribution
                || !(direct.classes == fast.classes)) {
                throw std::runtime_error("direct and H^2 geometry disagree");
            }
        }

        const long long expected_mixed =
            1LL * (prime - 2) * (subgroup_order - 1) * (subgroup_order - 2);
        const long long expected_off = expected_off_total(prime, subgroup_order);
        const long long expected_variety = variety_count_formula(prime, subgroup_order);
        long long variety = 0;
        for (long long value : fast.distribution) {
            variety += value;
        }

        if (fast.classes.diagonal_to_off != expected_mixed
            || fast.classes.off_to_diagonal != expected_mixed
            || fast.classes.diagonal_to_diagonal != 1LL * (prime - 2) * (prime - 2)
            || fast.classes.off_to_off != expected_off
            || variety != expected_variety) {
            throw std::runtime_error("closed coupling-count formula regression");
        }

        std::cout
            << "N=" << prime
            << " K=" << subgroup_order
            << " keys=" << records.size()
            << " V4=" << variety
            << " Z0=" << fast.distribution[0]
            << " energy=" << squared_energy(fast.distribution)
            << " diag_to_off=" << fast.classes.diagonal_to_off
            << " off_to_diag=" << fast.classes.off_to_diagonal
            << " diag_to_diag=" << fast.classes.diagonal_to_diagonal;

        if (prime <= 199) {
            const TwistCollapseResult collapse = verify_twist_collapse(
                prime, subgroup_order, records, fast.distribution
            );
            std::cout
                << " twist_freq_rel=" << collapse.frequency_max_relative_deviation
                << " twist_time_rel=" << collapse.time_max_relative_deviation;
            if (collapse.frequency_max_relative_deviation >= 1e-11
                || collapse.time_max_relative_deviation >= 1e-11) {
                throw std::runtime_error("twist-sum collapse regression");
            }
        }
        std::cout << '\n';

        for (int q : q_values) {
            const auto [generator, dimension, left] = jacobi_fourth(
                prime, subgroup_order, q
            );
            const Complex sigma = sigma_from_distribution(
                fast.distribution, prime, q
            );
            const Complex right = static_cast<double>(dimension * dimension) * sigma;
            const double relative =
                std::abs(left - right) / std::max(std::abs(left), 1.0);
            std::cout
                << "  q=" << q
                << " primitive_root=" << generator
                << " m=" << dimension
                << " lhs=" << left
                << " rhs_real=" << right.real()
                << " rhs_imag=" << right.imag()
                << " relative_deviation=" << relative
                << '\n';
            if (relative >= 1e-10) {
                throw std::runtime_error("fourth-moment factorization regression");
            }
        }
    }
    return 0;
}
