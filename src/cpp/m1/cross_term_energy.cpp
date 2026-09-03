#include <algorithm>
#include <cmath>
#include <complex>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <utility>
#include <vector>

using cd = std::complex<double>;
static const double PI = std::acos(-1.0);

long long modpow(long long a, long long e, long long p) {
    long long r = 1 % p;
    for (a %= p; e; e >>= 1, a = a * a % p) {
        if (e & 1) r = r * a % p;
    }
    return r;
}

std::vector<int> prime_factors(int n) {
    std::vector<int> out;
    for (int d = 2; d * d <= n; ++d) {
        if (n % d == 0) {
            out.push_back(d);
            while (n % d == 0) n /= d;
        }
    }
    if (n > 1) out.push_back(n);
    return out;
}

int primitive_root(int p) {
    const auto factors = prime_factors(p - 1);
    for (int g = 2; g < p; ++g) {
        bool ok = true;
        for (int q : factors) {
            if (modpow(g, (p - 1) / q, p) == 1) {
                ok = false;
                break;
            }
        }
        if (ok) return g;
    }
    throw std::runtime_error("primitive root not found");
}

struct Result {
    int N, K, m, primitiveRoot, violations;
    double totalRaw, diagRaw, crossRaw, trivialNontrivialCrossRaw,
           nontrivialCrossRaw, maxAbsNontrivialA, weilBound;
};

Result analyse(int N, int K) {
    if ((N - 1) % K != 0) throw std::runtime_error("K must divide N-1");
    const int g = primitive_root(N);
    std::vector<int> dlog(N, -1);
    long long x = 1;
    for (int s = 0; s < N - 1; ++s) {
        dlog[x] = s;
        x = x * g % N;
    }

    std::vector<int> ks;
    for (int k = 0; k < N - 1; k += K) ks.push_back(k);
    const int m = static_cast<int>(ks.size());
    const int P = m * m;

    std::vector<std::vector<cd>> psi(m, std::vector<cd>(N));
    for (int r = 0; r < m; ++r) {
        for (int u = 1; u < N; ++u) {
            const double theta = 2.0 * PI * ks[r] * dlog[u] / double(N - 1);
            psi[r][u] = cd(std::cos(theta), std::sin(theta));
        }
    }

    std::vector<std::vector<cd>> A(P, std::vector<cd>(N));
    for (int d = 0; d < N; ++d) {
        for (int u = 1; u < N; ++u) {
            int den = (d - u + 1) % N;
            if (den < 0) den += N;
            if (den == 0) continue;
            const int num = int((1LL * u * ((d - 1 + N) % N) + 1) % N);
            const int v = int(1LL * num * modpow(den, N - 2, N) % N);
            if (v == 0) continue;
            for (int r = 0; r < m; ++r) {
                for (int s = 0; s < m; ++s) {
                    A[r * m + s][d] += psi[r][u] * psi[s][v];
                }
            }
        }
    }

    const double weil = 4.0 * std::sqrt(double(N));
    double maxA = 0.0;
    int violations = 0;
    for (int t = 1; t < P; ++t) {
        for (int d = 0; d < N; ++d) {
            const double z = std::abs(A[t][d]);
            maxA = std::max(maxA, z);
            if (z > weil + 1e-8) ++violations;
        }
    }

    std::vector<std::vector<cd>> F(P, std::vector<cd>(N));
    for (int t = 0; t < P; ++t) {
        for (int z = 0; z < N; ++z) {
            cd acc = 0.0;
            for (int d = 0; d < N; ++d) acc += A[t][d] * A[t][(z - d + N) % N];
            F[t][z] = acc;
        }
    }

    std::vector<cd> totalVector(N), nontrivialVector(N);
    double diag = 0.0, nontrivialDiag = 0.0;
    for (int t = 0; t < P; ++t) {
        double e = 0.0;
        for (int z = 0; z < N; ++z) {
            totalVector[z] += F[t][z];
            if (t != 0) nontrivialVector[z] += F[t][z];
            e += std::norm(F[t][z]);
        }
        diag += e;
        if (t != 0) nontrivialDiag += e;
    }

    double total = 0.0, nontrivialTotal = 0.0;
    cd trivialCoupling = 0.0;
    for (int z = 0; z < N; ++z) {
        total += std::norm(totalVector[z]);
        nontrivialTotal += std::norm(nontrivialVector[z]);
        trivialCoupling += std::conj(F[0][z]) * nontrivialVector[z];
    }

    return {N, K, m, g, violations, total, diag, total - diag,
            2.0 * trivialCoupling.real(), nontrivialTotal - nontrivialDiag,
            maxA, weil};
}

int main() {
    const std::vector<std::pair<int, int>> designs{{53, 13}, {199, 11}};
    std::cout << std::setprecision(17);
    for (auto [N, K] : designs) {
        const Result r = analyse(N, K);
        std::cout << "N=" << r.N << " K=" << r.K << " m=" << r.m
                  << " total_raw=" << r.totalRaw
                  << " diag_raw=" << r.diagRaw
                  << " cross_raw=" << r.crossRaw
                  << " cross_over_diag=" << r.crossRaw / r.diagRaw
                  << " trivial_nontrivial_cross_raw=" << r.trivialNontrivialCrossRaw
                  << " nontrivial_cross_raw=" << r.nontrivialCrossRaw
                  << " max_abs_nontrivial_A=" << r.maxAbsNontrivialA
                  << " weil_4sqrtN=" << r.weilBound
                  << " violations=" << r.violations << '\n';
    }
}
