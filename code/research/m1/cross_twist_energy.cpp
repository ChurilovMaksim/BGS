// Independent C++17 implementation of the finite-N M1 cross-twist audit.
// Research diagnostic only: this does not prove an asymptotic theorem.
#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using i64 = std::int64_t;
using cd = std::complex<double>;

static i64 mod_pow(i64 a, i64 e, i64 p) {
    i64 r = 1;
    while (e) {
        if (e & 1) r = r * a % p;
        a = a * a % p;
        e >>= 1;
    }
    return r;
}

static std::vector<int> prime_factors(int n) {
    std::vector<int> out;
    for (int d = 2; 1LL * d * d <= n; ++d) {
        if (n % d == 0) {
            out.push_back(d);
            while (n % d == 0) n /= d;
        }
    }
    if (n > 1) out.push_back(n);
    return out;
}

static int primitive_root(int p) {
    const auto fs = prime_factors(p - 1);
    for (int g = 2; g < p; ++g) {
        bool ok = true;
        for (int q : fs) {
            if (mod_pow(g, (p - 1) / q, p) == 1) {
                ok = false;
                break;
            }
        }
        if (ok) return g;
    }
    throw std::runtime_error("no primitive root");
}

static int multiplicative_order(int a, int p) {
    int x = 1;
    for (int k = 1; k < p; ++k) {
        x = (i64)x * a % p;
        if (x == 1) return k;
    }
    throw std::runtime_error("non-unit");
}

struct KeyTensor {
    int N, a, K, m, g;
    std::vector<i64> W;  // [m,m,N]

    std::size_t idx(int cu, int cv, int d) const {
        return (static_cast<std::size_t>(cu) * m + cv) * N + d;
    }
};

static KeyTensor build_key_tensor(int N, int a, int K) {
    if (multiplicative_order(a, N) != K) throw std::runtime_error("wrong K");
    if ((N - 1) % K) throw std::runtime_error("K does not divide N-1");
    const int m = (N - 1) / K;
    const int g = primitive_root(N);
    std::vector<int> dl(N, -1), inv(N, 0);
    int z = 1;
    for (int e = 0; e < N - 1; ++e) {
        dl[z] = e;
        z = (i64)z * g % N;
    }
    if (dl[a] % m != 0) throw std::runtime_error("H coset convention mismatch");
    for (int x = 1; x < N; ++x) inv[x] = static_cast<int>(mod_pow(x, N - 2, N));

    KeyTensor kt{N, a, K, m, g, std::vector<i64>(static_cast<std::size_t>(m) * m * N, 0)};
    for (int x = 2; x < N; ++x) {
        for (int y = 2; y < N; ++y) {
            const int u = (i64)x * inv[y] % N;
            const int v = (i64)(x - 1) * inv[y - 1] % N;
            const int d = (x - y + N) % N;
            ++kt.W[kt.idx(dl[u] % m, dl[v] % m, d)];
        }
    }
    i64 mass = 0;
    for (i64 w : kt.W) mass += w;
    if (mass != 1LL * (N - 2) * (N - 2)) throw std::runtime_error("wrong key mass");
    if (kt.W[kt.idx(0, 0, 0)] != N - 2) throw std::runtime_error("wrong singular multiplicity");
    return kt;
}

static std::vector<i64> exact_direct_B(const KeyTensor& kt) {
    const int N = kt.N, m = kt.m;
    std::vector<i64> B(N, 0);
    for (int cu = 0; cu < m; ++cu) {
        for (int cv = 0; cv < m; ++cv) {
            const int du = (m - cu) % m, dv = (m - cv) % m;
            std::vector<std::pair<int, i64>> left, right;
            for (int d = 0; d < N; ++d) {
                const i64 a = kt.W[kt.idx(cu, cv, d)];
                const i64 b = kt.W[kt.idx(du, dv, d)];
                if (a) left.push_back({d, a});
                if (b) right.push_back({d, b});
            }
            for (auto [d1, a] : left) {
                for (auto [d2, b] : right) {
                    B[(d1 + d2) % N] += a * b;
                }
            }
        }
    }
    return B;
}

struct TwistSummary {
    double reconstruction_error = 0.0;
    long double full_energy = 0.0L;
    long double trivial_energy = 0.0L;
    long double diagonal_energy = 0.0L;
    long double cross_energy = 0.0L;
    double max_nontriv_A_all = 0.0;
    double max_nontriv_A_regular = 0.0;
};

static TwistSummary analyze_twists(const KeyTensor& kt, const std::vector<i64>& B) {
    const int N = kt.N, m = kt.m;
    const int T = m * m;
    const double pi = std::acos(-1.0);
    std::vector<cd> root(m);
    for (int k = 0; k < m; ++k) root[k] = std::polar(1.0, -2.0 * pi * k / m);

    std::vector<cd> A(static_cast<std::size_t>(T) * N);
    auto tidx = [N](int tau, int d) { return static_cast<std::size_t>(tau) * N + d; };
    for (int r = 0; r < m; ++r) {
        for (int s = 0; s < m; ++s) {
            const int tau = r * m + s;
            for (int d = 0; d < N; ++d) {
                cd sum = 0.0;
                for (int cu = 0; cu < m; ++cu) {
                    for (int cv = 0; cv < m; ++cv) {
                        const i64 w = kt.W[kt.idx(cu, cv, d)];
                        if (!w) continue;
                        sum += static_cast<double>(w) * root[(r * cu + s * cv) % m];
                    }
                }
                A[tidx(tau, d)] = sum;
            }
        }
    }

    std::vector<cd> F(static_cast<std::size_t>(T) * N, 0.0);
    for (int tau = 0; tau < T; ++tau) {
        for (int d1 = 0; d1 < N; ++d1) {
            const cd z1 = A[tidx(tau, d1)];
            for (int d2 = 0; d2 < N; ++d2) {
                F[tidx(tau, (d1 + d2) % N)] += z1 * A[tidx(tau, d2)];
            }
        }
    }

    TwistSummary out;
    std::vector<cd> Btw(N, 0.0);
    const double m2 = static_cast<double>(m) * m;
    const long double m4 = static_cast<long double>(m2) * m2;
    for (int tau = 0; tau < T; ++tau) {
        for (int d = 0; d < N; ++d) {
            Btw[d] += F[tidx(tau, d)] / m2;
            out.diagonal_energy += std::norm(F[tidx(tau, d)]) / m4;
        }
    }
    for (int d = 0; d < N; ++d) {
        out.reconstruction_error = std::max(out.reconstruction_error, std::abs(Btw[d] - static_cast<double>(B[d])));
        out.full_energy += static_cast<long double>(B[d]) * B[d];
        out.trivial_energy += std::norm(F[tidx(0, d)] / m2);
    }
    out.cross_energy = out.full_energy - out.diagonal_energy;
    for (int tau = 1; tau < T; ++tau) {
        for (int d = 0; d < N; ++d) {
            const double a = std::abs(A[tidx(tau, d)]);
            out.max_nontriv_A_all = std::max(out.max_nontriv_A_all, a);
            if (d != 0) out.max_nontriv_A_regular = std::max(out.max_nontriv_A_regular, a);
        }
    }
    return out;
}

int main(int argc, char** argv) {
    if (argc != 4) {
        std::cerr << "usage: " << argv[0] << " N a K\n";
        return 2;
    }
    const int N = std::stoi(argv[1]), a = std::stoi(argv[2]), K = std::stoi(argv[3]);
    try {
        const auto kt = build_key_tensor(N, a, K);
        const auto B = exact_direct_B(kt);
        const auto s = analyze_twists(kt, B);
        i64 V4 = 0;
        for (i64 x : B) V4 += x;
        std::cout << std::setprecision(17);
        std::cout << "{\n"
                  << "  \"status\": \"RESEARCH_DIAGNOSTIC_NOT_A_PROOF\",\n"
                  << "  \"N\": " << N << ", \"a\": " << a << ", \"K\": " << K << ", \"m\": " << kt.m << ",\n"
                  << "  \"V4_count\": " << V4 << ",\n"
                  << "  \"projector_max_abs_error\": " << s.reconstruction_error << ",\n"
                  << "  \"full_energy\": " << static_cast<double>(s.full_energy) << ",\n"
                  << "  \"trivial_energy\": " << static_cast<double>(s.trivial_energy) << ",\n"
                  << "  \"delta_vs_trivial\": " << static_cast<double>((s.full_energy - s.trivial_energy) / s.trivial_energy) << ",\n"
                  << "  \"diagonal_twist_energy\": " << static_cast<double>(s.diagonal_energy) << ",\n"
                  << "  \"cross_twist_energy\": " << static_cast<double>(s.cross_energy) << ",\n"
                  << "  \"cross_fraction_of_full\": " << static_cast<double>(s.cross_energy / s.full_energy) << ",\n"
                  << "  \"max_nontrivial_abs_A_including_d0\": " << s.max_nontriv_A_all << ",\n"
                  << "  \"max_nontrivial_abs_A_regular_d_nonzero\": " << s.max_nontriv_A_regular << ",\n"
                  << "  \"A_tau_d0_expected\": " << (N - 2) << "\n"
                  << "}\n";
    } catch (const std::exception& e) {
        std::cerr << "error: " << e.what() << "\n";
        return 1;
    }
    return 0;
}
