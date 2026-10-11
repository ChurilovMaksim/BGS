// Independent exact rational control of the harmonic-lift energy identity.
// This checks finite instances, not singular-value min-max or a BGS limit.
#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <iostream>
#include <stdexcept>
#include <vector>

using R = boost::multiprecision::cpp_rational;
using V = std::vector<R>;
using M = std::vector<V>;

void require(bool value) {
    if (!value) throw std::runtime_error("Exact censoring control failed");
}
R dot(const V& a, const V& b) {
    require(a.size() == b.size());
    R result = 0;
    for (std::size_t i = 0; i < a.size(); ++i) result += a[i] * b[i];
    return result;
}
V multiply(const M& a, const V& x) {
    V y(a.size());
    for (std::size_t i = 0; i < a.size(); ++i) y[i] = dot(a[i], x);
    return y;
}
R sum(const V& a) {
    R result = 0;
    for (const auto& value : a) result += value;
    return result;
}
V solve(M a, V b) {
    const std::size_t n = a.size();
    for (std::size_t col = 0; col < n; ++col) {
        std::size_t pivot = col;
        while (pivot < n && a[pivot][col] == 0) ++pivot;
        require(pivot < n);
        std::swap(a[col], a[pivot]); std::swap(b[col], b[pivot]);
        const R scale = a[col][col];
        for (auto& value : a[col]) value /= scale;
        b[col] /= scale;
        for (std::size_t row = 0; row < n; ++row) {
            if (row == col) continue;
            const R factor = a[row][col];
            for (std::size_t k = 0; k < n; ++k) a[row][k] -= factor * a[col][k];
            b[row] -= factor * b[col];
        }
    }
    return b;
}
M mix(int n, int trial) {
    M p(n, V(n, R(1) / n));
    R total = 1;
    for (int shift = 0; shift < n; ++shift) {
        const int weight = 1 + ((trial + 1) * (shift + 4)) % 9;
        total += weight;
        for (int i = 0; i < n; ++i) {
            int j = (i + shift) % n;
            if ((trial + shift) % 2) j = n - 1 - j;
            p[i][j] += weight;
        }
    }
    for (auto& row : p) for (auto& value : row) value /= total;
    for (int j = 0; j < n; ++j) {
        require(sum(p[j]) == 1);
        R column = 0;
        for (int i = 0; i < n; ++i) column += p[i][j];
        require(column == 1);
    }
    return p;
}
int main() {
    try {
        int cases = 0, identities = 0;
        for (int n = 2; n <= 9; ++n) for (int trial = 0; trial < 4; ++trial) {
            const M p = mix(n, trial);
            for (int retained = 1; retained < n; ++retained) {
                const int deleted = n - retained;
                V x(retained);
                for (int i = 0; i < retained; ++i) x[i] = (i * i + 2 * trial + i) % 7 - 3;
                const R mean_x = sum(x) / retained;
                for (auto& value : x) value -= mean_x;
                M system(deleted, V(deleted));
                V rhs(deleted);
                for (int i = 0; i < deleted; ++i) {
                    for (int j = 0; j < deleted; ++j)
                        system[i][j] = R(i == j ? 1 : 0) - p[retained + i][retained + j];
                    for (int j = 0; j < retained; ++j) rhs[i] += p[retained + i][j] * x[j];
                }
                const V t = solve(system, rhs);
                V lifted = x;
                lifted.insert(lifted.end(), t.begin(), t.end());
                const V plift = multiply(p, lifted);
                for (int i = 0; i < deleted; ++i) require(plift[retained + i] == t[i]);
                V pcx(plift.begin(), plift.begin() + retained);
                require(sum(pcx) == 0);
                const R full_mean = sum(lifted) / n;
                for (auto& value : lifted) value -= full_mean;
                const V centered_output = multiply(p, lifted);
                const R correction = dot(t, t) - sum(t) * sum(t) / n;
                require(correction >= 0);
                for (const R& s2 : V{R(0), R(1) / 16, R(1) / 4, R(9) / 16, R(1)}) {
                    const R left = dot(centered_output, centered_output) - s2 * dot(lifted, lifted);
                    const R right = dot(pcx, pcx) - s2 * dot(x, x) + (1 - s2) * correction;
                    require(left == right);
                    ++identities;
                }
                ++cases;
            }
        }
        std::cout << "{\"status\":\"PASS\",\"exact_rational_cases\":" << cases
                  << ",\"exact_energy_identities\":" << identities
                  << ",\"dimension_range\":[2,9],\"non_claims\":[\"asymptotic gap bound\",\"BGS\"]}\n";
    } catch (const std::exception& error) {
        std::cerr << error.what() << '\n';
        return 1;
    }
}
