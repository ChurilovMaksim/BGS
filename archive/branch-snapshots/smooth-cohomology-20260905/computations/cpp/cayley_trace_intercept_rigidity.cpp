#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

struct Signature {
    std::array<std::uint32_t, 8> entries{};
    bool operator==(const Signature& other) const noexcept {
        return entries == other.entries;
    }
};

struct SignatureHash {
    std::size_t operator()(const Signature& s) const noexcept {
        std::uint64_t h = 1469598103934665603ULL;
        for (std::uint32_t v : s.entries) {
            h ^= v;
            h *= 1099511628211ULL;
        }
        return static_cast<std::size_t>(h);
    }
};

static int mod_k(int x, int K) {
    x %= K;
    if (x < 0) x += K;
    return x;
}

static int fold_class(int x, int K) {
    x = mod_k(x, K);
    return std::min(x, K - x);
}

static bool is_prime(int n) {
    if (n < 2) return false;
    for (int d = 2; 1LL * d * d <= n; ++d) {
        if (n % d == 0) return false;
    }
    return true;
}

// Exact coefficient signature in Z[C_K] for
//   s_1 t_b - s_r t_a,
// where s_n=zeta^n-zeta^-n and t_n=zeta^n+zeta^-n.
// For prime K, equality of two such signatures is equivalent to equality
// in Q(zeta): any rational relation among 1,zeta,...,zeta^(K-1) is a
// multiple of Phi_K, while every signature here has coefficient sum zero.
static Signature intercept_signature(int K, int r, int a, int b) {
    std::array<std::pair<int, int>, 8> terms{{
        {mod_k(1 + b, K), +1},
        {mod_k(1 - b, K), +1},
        {mod_k(-1 + b, K), -1},
        {mod_k(-1 - b, K), -1},
        {mod_k(r + a, K), -1},
        {mod_k(r - a, K), -1},
        {mod_k(-r + a, K), +1},
        {mod_k(-r - a, K), +1},
    }};
    std::sort(terms.begin(), terms.end(),
              [](auto x, auto y) { return x.first < y.first; });

    Signature out;
    int slot = 0;
    for (int i = 0; i < 8;) {
        const int exponent = terms[i].first;
        int coefficient = 0;
        while (i < 8 && terms[i].first == exponent) {
            coefficient += terms[i].second;
            ++i;
        }
        if (coefficient != 0) {
            // exponent in [0,K-1], coefficient in [-2,2].
            out.entries[slot++] =
                static_cast<std::uint32_t>((exponent + 1) * 8 + (coefficient + 3));
        }
    }
    return out;
}

struct FiberData {
    int count = 0;
    std::array<int, 4> first_two{{-1, -1, -1, -1}};
};

static bool step_two_class(int a, int c, int K) {
    return c == fold_class(a + 2, K) || c == fold_class(a - 2, K);
}

static bool predicted_target_pair(
    int K, int r, int a, int c, int b, int d) {
    // Search the two signed representatives of source class a. The theorem
    // predicts c=[x+2 eps] and
    // {b,d}={[x+eps-r],[x+eps+r]}.
    const std::array<int, 2> reps{{a, mod_k(-a, K)}};
    for (int x : reps) {
        for (int eps : {-1, +1}) {
            const int y = mod_k(x + 2 * eps, K);
            if (fold_class(y, K) != c) continue;
            const int center = mod_k(x + eps, K);
            std::array<int, 2> predicted{{
                fold_class(center - r, K),
                fold_class(center + r, K),
            }};
            std::array<int, 2> observed{{b, d}};
            std::sort(predicted.begin(), predicted.end());
            std::sort(observed.begin(), observed.end());
            if (predicted == observed) return true;
        }
    }
    return false;
}

struct AuditResult {
    int K = 0;
    int max_fiber = 0;
    std::uint64_t double_fibers = 0;
};

static AuditResult audit_prime(int K) {
    if (!is_prime(K) || K < 7 || K % 2 == 0) {
        throw std::invalid_argument("K must be an odd prime >= 7");
    }
    const int m = (K - 1) / 2;
    AuditResult result{K, 0, 0};

    // r=1 is the same normalized row and is excluded. r=-1 is included:
    // it is the inverse-row reflection class and has a separate exact
    // swap classification.
    for (int r = 2; r < K; ++r) {
        std::unordered_map<Signature, FiberData, SignatureHash> fibers;
        fibers.reserve(static_cast<std::size_t>(m + 1) * (m + 1) * 2);

        for (int a = 0; a <= m; ++a) {
            for (int b = 0; b <= m; ++b) {
                auto& f = fibers[intercept_signature(K, r, a, b)];
                if (f.count < 2) {
                    f.first_two[2 * f.count] = a;
                    f.first_two[2 * f.count + 1] = b;
                }
                ++f.count;
                result.max_fiber = std::max(result.max_fiber, f.count);
                if (f.count > 2) {
                    std::cerr << "counterexample K=" << K << " r=" << r
                              << " fiber_size=" << f.count << "\n";
                    throw std::runtime_error("intercept fiber exceeds two");
                }
            }
        }

        for (const auto& [signature, f] : fibers) {
            (void)signature;
            if (f.count != 2) continue;
            ++result.double_fibers;
            const int a = f.first_two[0];
            const int b = f.first_two[1];
            const int c = f.first_two[2];
            const int d = f.first_two[3];

            if (r == K - 1) {
                // alpha=-1, so the intercept is s_1(t_a+t_b);
                // the only doubleton is the swap.
                if (!(a == d && b == c)) {
                    throw std::runtime_error("inverse-row doubleton is not a swap");
                }
            } else {
                if (!step_two_class(a, c, K)) {
                    throw std::runtime_error(
                        "non-inverse source classes are not step-two adjacent");
                }
                if (!predicted_target_pair(K, r, a, c, b, d)) {
                    throw std::runtime_error(
                        "non-inverse target pair violates exact classification");
                }
            }
        }
    }
    return result;
}

int main(int argc, char** argv) {
    bool extended = false;
    std::vector<int> requested;
    for (int i = 1; i < argc; ++i) {
        const std::string arg = argv[i];
        if (arg == "--extended") {
            extended = true;
        } else {
            requested.push_back(std::stoi(arg));
        }
    }

    std::vector<int> tests;
    if (!requested.empty()) {
        tests = requested;
    } else {
        tests = {7, 11, 13, 17, 23, 31, 47, 79, 101, 127, 151, 181, 199};
        if (extended) {
            const std::vector<int> extra{251, 307, 401, 503, 601, 701, 809};
            tests.insert(tests.end(), extra.begin(), extra.end());
        }
    }

    for (int K : tests) {
        const auto start = std::chrono::steady_clock::now();
        const AuditResult result = audit_prime(K);
        const double sec =
            std::chrono::duration<double>(std::chrono::steady_clock::now() - start)
                .count();
        std::cout << "PASS K=" << K
                  << " maxFiber=" << result.max_fiber
                  << " doubleFibers=" << result.double_fibers
                  << " seconds=" << sec << "\n";
    }
    std::cout << "cayley trace-intercept rigidity regression: OK\n";
    return 0;
}
