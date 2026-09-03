#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

using Complex = std::complex<long double>;
using Matrix = std::vector<std::vector<Complex>>;

std::vector<int> prime_divisors(int value) {
    std::vector<int> divisors;
    for (int candidate = 2; candidate * candidate <= value; ++candidate) {
        if (value % candidate == 0) {
            divisors.push_back(candidate);
            while (value % candidate == 0) value /= candidate;
        }
    }
    if (value > 1) divisors.push_back(value);
    return divisors;
}

std::int64_t mod_pow(std::int64_t base, std::int64_t exponent, std::int64_t mod) {
    // This executable accepts an int prime, so products of residues fit int64_t.
    std::int64_t result = 1;
    base %= mod;
    while (exponent > 0) {
        if (exponent & 1) result = (result * base) % mod;
        base = (base * base) % mod;
        exponent >>= 1;
    }
    return result;
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
        if (ok) return generator;
    }
    throw std::runtime_error("primitive root not found");
}

struct CharacterData {
    int generator{};
    int dimension{};
    std::vector<int> dlog;
    Matrix chars;
};

CharacterData character_table(int prime, int subgroup_order) {
    CharacterData data;
    data.generator = primitive_root(prime);
    data.dimension = (prime - 1) / subgroup_order;
    data.dlog.assign(prime, -1);
    int value = 1;
    for (int exponent = 0; exponent < prime - 1; ++exponent) {
        data.dlog[value] = exponent;
        value = static_cast<int>((static_cast<std::int64_t>(value) * data.generator) % prime);
    }

    data.chars.assign(data.dimension, std::vector<Complex>(prime));
    const long double tau = 2.0L * std::acos(-1.0L);
    for (int j = 0; j < data.dimension; ++j) {
        for (int x = 1; x < prime; ++x) {
            const long double angle = tau * static_cast<long double>(j * data.dlog[x]) /
                                      static_cast<long double>(data.dimension);
            data.chars[j][x] = std::polar(1.0L, angle);
        }
    }
    return data;
}

std::vector<int> inverses(int prime) {
    std::vector<int> inv(prime, 0);
    for (int x = 1; x < prime; ++x) inv[x] = static_cast<int>(mod_pow(x, prime - 2, prime));
    return inv;
}

Matrix historical_mobius_amplitudes(int prime, const Matrix& chars, const std::vector<int>& inv) {
    const int m = static_cast<int>(chars.size());
    Matrix amplitudes(m * m, std::vector<Complex>(prime));
    for (int d = 0; d < prime; ++d) {
        for (int u = 1; u < prime; ++u) {
            int denominator = (d + 1 - u) % prime;
            if (denominator < 0) denominator += prime;
            if (denominator == 0) continue;
            int numerator = static_cast<int>((static_cast<std::int64_t>(d - 1) * u + 1) % prime);
            if (numerator < 0) numerator += prime;
            const int v = static_cast<int>((static_cast<std::int64_t>(numerator) * inv[denominator]) % prime);
            if (v == 0) continue;
            for (int a = 0; a < m; ++a) {
                const Complex cu = chars[a][u];
                for (int b = 0; b < m; ++b) {
                    amplitudes[a * m + b][d] += cu * chars[b][v];
                }
            }
        }
    }
    return amplitudes;
}

Matrix correct_key_amplitudes(int prime, const Matrix& chars, const std::vector<int>& inv) {
    const int m = static_cast<int>(chars.size());
    Matrix amplitudes(m * m, std::vector<Complex>(prime));
    for (int x = 2; x < prime; ++x) {
        for (int y = 2; y < prime; ++y) {
            const int u = static_cast<int>((static_cast<std::int64_t>(x) * inv[y]) % prime);
            const int v = static_cast<int>((static_cast<std::int64_t>(x - 1) * inv[y - 1]) % prime);
            int d = x - y;
            if (d < 0) d += prime;
            for (int a = 0; a < m; ++a) {
                const Complex cu = chars[a][u];
                for (int b = 0; b < m; ++b) {
                    amplitudes[a * m + b][d] += cu * chars[b][v];
                }
            }
        }
    }
    return amplitudes;
}

std::vector<Complex> circular_convolution(const std::vector<Complex>& a) {
    const int n = static_cast<int>(a.size());
    std::vector<Complex> out(n);
    for (int d = 0; d < n; ++d) {
        Complex sum{};
        for (int s = 0; s < n; ++s) {
            int other = d - s;
            if (other < 0) other += n;
            sum += a[s] * a[other];
        }
        out[d] = sum;
    }
    return out;
}

struct Energy {
    long double total_raw{};
    long double diagonal_raw{};
    long double cross_raw{};
    long double cross_over_diagonal{};
    long double normalized_energy{};
};

Energy assembly_energy(const Matrix& amplitudes, int dimension) {
    const int prime = static_cast<int>(amplitudes.front().size());
    std::vector<Complex> summed(prime);
    long double diagonal = 0.0L;
    for (const auto& row : amplitudes) {
        auto convolution = circular_convolution(row);
        for (int d = 0; d < prime; ++d) {
            diagonal += std::norm(convolution[d]);
            summed[d] += convolution[d];
        }
    }
    long double total = 0.0L;
    for (const Complex& value : summed) total += std::norm(value);
    const long double dim = static_cast<long double>(dimension);
    const long double dim4 = dim * dim * dim * dim;
    Energy energy;
    energy.total_raw = total;
    energy.diagonal_raw = diagonal;
    energy.cross_raw = total - diagonal;
    energy.cross_over_diagonal = energy.cross_raw / diagonal;
    energy.normalized_energy = total / dim4;
    return energy;
}

struct Correction {
    long double time_residual{};
    long double fourier_residual{};
    bool pass{};
};

Correction verify_correction(int prime, int dimension, const Matrix& historical, const Matrix& correct) {
    long double max_time = 0.0L;
    for (int a = 0; a < dimension; ++a) {
        for (int b = 0; b < dimension; ++b) {
            const int flat = a * dimension + b;
            for (int d = 0; d < prime; ++d) {
                Complex expected = 1.0L;
                if (d == 0) expected = (a == 0) ? 0.0L : -static_cast<long double>(prime - 1);
                max_time = std::max(max_time, std::abs((historical[flat][d] - correct[flat][d]) - expected));
            }
        }
    }

    const long double tau = 2.0L * std::acos(-1.0L);
    long double max_fourier = 0.0L;
    for (int a = 0; a < dimension; ++a) {
        for (int b = 0; b < dimension; ++b) {
            const int flat = a * dimension + b;
            for (int xi = 0; xi < prime; ++xi) {
                Complex observed{};
                for (int d = 0; d < prime; ++d) {
                    const long double angle = -tau * static_cast<long double>(xi * d) /
                                              static_cast<long double>(prime);
                    observed += (historical[flat][d] - correct[flat][d]) * std::polar(1.0L, angle);
                }
                Complex expected{};
                if (a == 0) {
                    expected = (xi == 0) ? static_cast<long double>(prime - 1) : -1.0L;
                } else {
                    expected = (xi == 0) ? 0.0L : -static_cast<long double>(prime);
                }
                max_fourier = std::max(max_fourier, std::abs(observed - expected));
            }
        }
    }
    return {max_time, max_fourier, max_time < 1e-10L && max_fourier < 1e-8L};
}

struct Result {
    int prime{};
    int subgroup_order{};
    int dimension{};
    int generator{};
    Correction correction;
    Energy historical;
    Energy correct;
    std::uint64_t correct_integer{};
    long double correct_integer_residual{};
    bool pass{};
};

Result analyse_design(int prime, int subgroup_order) {
    if ((prime - 1) % subgroup_order != 0) throw std::invalid_argument("K must divide N-1");
    auto data = character_table(prime, subgroup_order);
    auto inv = inverses(prime);
    auto historical = historical_mobius_amplitudes(prime, data.chars, inv);
    auto correct = correct_key_amplitudes(prime, data.chars, inv);
    auto correction = verify_correction(prime, data.dimension, historical, correct);
    auto historical_energy = assembly_energy(historical, data.dimension);
    auto correct_energy = assembly_energy(correct, data.dimension);
    const auto rounded = static_cast<std::uint64_t>(std::llround(correct_energy.normalized_energy));
    const long double residual = std::abs(correct_energy.normalized_energy - static_cast<long double>(rounded));
    return {prime, subgroup_order, data.dimension, data.generator, correction,
            historical_energy, correct_energy, rounded, residual,
            correction.pass && residual < 1e-3L};
}

void print_energy(const char* name, const Energy& e) {
    std::cout << "    \"" << name << "\": {\n"
              << "      \"total_raw\": " << static_cast<double>(e.total_raw) << ",\n"
              << "      \"diagonal_raw\": " << static_cast<double>(e.diagonal_raw) << ",\n"
              << "      \"cross_raw\": " << static_cast<double>(e.cross_raw) << ",\n"
              << "      \"cross_over_diagonal\": " << static_cast<double>(e.cross_over_diagonal) << ",\n"
              << "      \"normalized_energy\": " << static_cast<double>(e.normalized_energy) << "\n"
              << "    }";
}

void print_result(const Result& r) {
    std::cout << std::setprecision(17);
    std::cout << "{\n"
              << "  \"producer\": \"src/cpp/m1/cross_term_energy.cpp\",\n"
              << "  \"status\": \"FINITE DIAGNOSTIC; HISTORICAL ASSEMBLY RETRACTED\",\n"
              << "  \"N\": " << r.prime << ",\n"
              << "  \"K\": " << r.subgroup_order << ",\n"
              << "  \"m\": " << r.dimension << ",\n"
              << "  \"primitive_root\": " << r.generator << ",\n"
              << "  \"correction_identity\": {\n"
              << "    \"time_domain_max_abs_residual\": " << static_cast<double>(r.correction.time_residual) << ",\n"
              << "    \"fourier_domain_max_abs_residual\": " << static_cast<double>(r.correction.fourier_residual) << ",\n"
              << "    \"pass\": " << (r.correction.pass ? "true" : "false") << "\n"
              << "  },\n";
    print_energy("historical_mobius_energy", r.historical);
    std::cout << ",\n";
    print_energy("correct_key_table_energy", r.correct);
    std::cout << ",\n"
              << "  \"correct_energy_integer_sum_B_squared\": " << r.correct_integer << ",\n"
              << "  \"correct_energy_integer_residual\": " << static_cast<double>(r.correct_integer_residual) << ",\n"
              << "  \"pass\": " << (r.pass ? "true" : "false") << "\n"
              << "}\n";
}

bool close_relative(long double observed, long double expected, long double rel_tol = 1e-11L) {
    const long double scale = std::max(1.0L, std::abs(expected));
    return std::abs(observed - expected) <= rel_tol * scale;
}

bool verify_anchor(const Result& r, std::uint64_t correct_integer,
                   long double historical_normalized, int expected_generator) {
    bool ok = r.pass;
    ok = ok && r.correct_integer == correct_integer;
    ok = ok && r.generator == expected_generator;
    ok = ok && close_relative(r.historical.normalized_energy, historical_normalized, 1e-10L);
    return ok;
}

int verify() {
    const Result r53 = analyse_design(53, 13);
    const Result r199 = analyse_design(199, 11);
    const bool ok53 = verify_anchor(r53, 3410502105ULL, 3682650293.0L, 2);
    const bool ok199 = verify_anchor(r199, 115589503389ULL, 113859701371.0L, 3);
    std::cout << std::setprecision(18)
              << "N=53 K=13 correct=" << r53.correct_integer
              << " hist=" << static_cast<double>(r53.historical.normalized_energy)
              << " time_res=" << static_cast<double>(r53.correction.time_residual)
              << " fourier_res=" << static_cast<double>(r53.correction.fourier_residual)
              << " status=" << (ok53 ? "PASS" : "FAIL") << "\n"
              << "N=199 K=11 correct=" << r199.correct_integer
              << " hist=" << static_cast<double>(r199.historical.normalized_energy)
              << " time_res=" << static_cast<double>(r199.correction.time_residual)
              << " fourier_res=" << static_cast<double>(r199.correction.fourier_residual)
              << " status=" << (ok199 ? "PASS" : "FAIL") << "\n";
    return (ok53 && ok199) ? 0 : 1;
}

}  // namespace

int main(int argc, char** argv) {
    try {
        if (argc == 2 && std::string(argv[1]) == "verify") return verify();
        if (argc == 3) {
            print_result(analyse_design(std::stoi(argv[1]), std::stoi(argv[2])));
            return 0;
        }
        std::cerr << "usage: cross_term_energy verify | cross_term_energy N K\n";
        return 2;
    } catch (const std::exception& exc) {
        std::cerr << "error: " << exc.what() << "\n";
        return 2;
    }
}
