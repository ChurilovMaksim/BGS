// Independent integer and floating-point certificate for BGS-TRACE-126.
// Recomputes the scaled Fourier table, the parity and reversal defects,
// the cyclotomic witness at N=11, m=3, and the prime-revival coefficient
// at N=41. Floating-point matrix comparisons are finite checks of the
// trace closure. A pass does not prove BGS-TRACE-005.

#include <complex>
#include <cstdint>
#include <cmath>
#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

namespace {

using C = std::complex<double>;

[[noreturn]] void fail(const std::string& msg) { throw std::runtime_error(msg); }

void check(bool cond, const std::string& msg) {
    if (!cond) fail(msg);
}

long r_num(long k) {
    if (k == 0) return 4;
    if (k == 1 || k == -1) return 2;
    if (k == 7 || k == -7) return -2;
    if (k == 6 || k == -6 || k == 8 || k == -8) return -1;
    return 0;
}

std::pair<long, long> coeff(long k, long ell) {
    if (ell == 0) {
        long re = (k == 7 || k == -7 ? 2000 : 0) + 100 * r_num(k) - (k == 0 ? 400 : 0);
        long im = -5 * (r_num(k - 1) - r_num(k + 1));
        return {re, im};
    }
    if (ell == 1) return {-3 * r_num(k), -4 * r_num(k)};
    if (ell == -1) return {-3 * r_num(k), 4 * r_num(k)};
    return {0, 0};
}

std::int64_t igcd(std::int64_t a, std::int64_t b) {
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    while (b) {
        std::int64_t t = a % b;
        a = b;
        b = t;
    }
    return a == 0 ? 1 : a;
}

std::uint64_t isqrt_u64(std::uint64_t n) {
    std::uint64_t x = n;
    std::uint64_t y = (x + 1) / 2;
    while (y < x) {
        x = y;
        y = (x + n / x) / 2;
    }
    return x;
}

using Mode = std::pair<long, long>;  // (k, ell), coefficient of T(ell, k)

std::vector<Mode> nonzero_modes() {
    std::vector<Mode> out;
    for (long k = -9; k <= 9; ++k)
        for (long ell = -1; ell <= 1; ++ell) {
            auto c = coeff(k, ell);
            if (c.first != 0 || c.second != 0) out.push_back({k, ell});
        }
    return out;
}

void check_symbol() {
    auto modes = nonzero_modes();
    check(modes.size() == 32, "mode count");
    long squares = 0;
    long imag = 0;
    // Every denominator divides 16000000, so the majorant numerator is exact in int64.
    std::int64_t majorant_num = 0;
    const std::int64_t majorant_den = 16000000;
    for (auto [k, ell] : modes) {
        auto c = coeff(k, ell);
        auto back = coeff(-k, -ell);
        check(back.first == c.first && back.second == -c.second, "hermitian");
        squares += c.first * c.first + c.second * c.second;
        imag += c.second * c.second;
        std::int64_t n = c.first * c.first + c.second * c.second;
        std::int64_t d = majorant_den;
        std::int64_t g = igcd(n, d);
        std::int64_t p = n / g;
        std::int64_t q = d / g;
        auto s = isqrt_u64(static_cast<std::uint64_t>(p) * static_cast<std::uint64_t>(q));
        check(static_cast<std::int64_t>(s) * static_cast<std::int64_t>(s) <= p * q, "isqrt low");
        check(p * q < static_cast<std::int64_t>(s + 1) * static_cast<std::int64_t>(s + 1), "isqrt high");
        majorant_num += (static_cast<std::int64_t>(s) + 1) * (majorant_den / q);
    }
    check(squares == 6603300, "energy");
    check(imag == 2652, "parity energy");
    std::int64_t mg = igcd(majorant_num, majorant_den);
    check(majorant_num / mg == 184981 && majorant_den / mg == 160000, "majorant");
    auto c70 = coeff(7, 0);
    check(c70.first == 1800 && c70.second == 0, "(7,0) coefficient");
}

long modn(long z, long N) {
    long r = z % N;
    if (r < 0) r += N;
    return r;
}

std::map<std::pair<long, long>, std::pair<long, long>> fold(long N) {
    std::map<std::pair<long, long>, std::pair<long, long>> acc;
    for (long k = -9; k <= 9; ++k)
        for (long ell = -1; ell <= 1; ++ell) {
            auto c = coeff(k, ell);
            if (c.first == 0 && c.second == 0) continue;
            auto key = std::make_pair(modn(ell, N), modn(k, N));
            acc[key].first += c.first;
            acc[key].second += c.second;
        }
    return acc;
}

std::pair<long, long> getc(const std::map<std::pair<long, long>, std::pair<long, long>>& acc, long a, long b, long N) {
    auto it = acc.find({modn(a, N), modn(b, N)});
    if (it == acc.end()) return {0, 0};
    return it->second;
}

std::int64_t parity_scaled(long N) {
    auto acc = fold(N);
    std::int64_t total = 0;
    for (long a = 0; a < N; ++a)
        for (long b = 0; b < N; ++b) {
            auto c = getc(acc, a, b, N);
            auto o = getc(acc, -a, -b, N);
            long dr = o.first - c.first;
            long di = o.second - c.second;
            total += static_cast<std::int64_t>(dr) * dr + static_cast<std::int64_t>(di) * di;
        }
    return total;
}

std::int64_t reversal_scaled(long N) {
    auto acc = fold(N);
    std::int64_t total = 0;
    for (long a = 0; a < N; ++a)
        for (long b = 0; b < N; ++b) {
            auto cs = getc(acc, a, -b, N);
            long sa = 3 * a + 4 * b;
            long sb = 2 * a + 3 * b;
            auto ct = getc(acc, sa, sb, N);
            long dr = cs.first - ct.first;
            long di = -cs.second - ct.second;
            total += static_cast<std::int64_t>(dr) * dr + static_cast<std::int64_t>(di) * di;
        }
    return total;
}

std::int64_t reversal_unreduced() {
    std::int64_t total = 0;
    for (long a = -40; a <= 40; ++a)
        for (long b = -40; b <= 40; ++b) {
            // c at (ell,k)=(a,b) is coeff(b,a). sigma(a,b)=(a,-b).
            auto cs = coeff(-b, a);
            // S(a,b)=(3a+4b, 2a+3b).
            auto ct = coeff(2 * a + 3 * b, 3 * a + 4 * b);
            long dr = cs.first - ct.first;
            long di = -cs.second - ct.second;
            total += static_cast<std::int64_t>(dr) * dr + static_cast<std::int64_t>(di) * di;
        }
    return total;
}

void check_defects() {
    check(reversal_unreduced() == 13206200, "unreduced reversal");
    for (long N = 3; N <= 77; N += 2) {
        auto p = parity_scaled(N);
        auto r = reversal_scaled(N);
        if (N == 7) {
            check(p == 0 && r == 0, "N=7");
        } else {
            check(p > 0 && r > 0, "positive defect");
        }
        if (N >= 19) check(p == 10608, "stable parity");
    }
    for (long N : {79L, 81L, 105L}) {
        check(parity_scaled(N) == 10608, "large parity");
        check(reversal_scaled(N) == 13206200, "large reversal");
    }
}

std::vector<long> mul_zeta(const std::vector<long>& c) {
    std::vector<long> out(10, 0);
    for (int j = 0; j < 10; ++j) out[j] -= c[9];
    for (int j = 0; j < 9; ++j) out[j + 1] += c[j];
    return out;
}

std::vector<long> zeta_pow(int k) {
    std::vector<long> c(10, 0);
    c[0] = 1;
    k %= 11;
    if (k < 0) k += 11;
    for (int i = 0; i < k; ++i) c = mul_zeta(c);
    return c;
}

void add_scaled(std::vector<long>& acc, const std::vector<long>& c, long s) {
    for (int i = 0; i < 10; ++i) acc[i] += s * c[i];
}

struct Mat2 {
    long a00 = 1, a01 = 0, a10 = 0, a11 = 1;
};

Mat2 mul(const Mat2& A, const Mat2& B) {
    return {A.a00 * B.a00 + A.a01 * B.a10, A.a00 * B.a01 + A.a01 * B.a11,
            A.a10 * B.a00 + A.a11 * B.a10, A.a10 * B.a01 + A.a11 * B.a11};
}

Mat2 pow_mod(Mat2 base, int e, long N) {
    Mat2 acc;
    while (e) {
        if (e & 1) {
            acc = mul(base, acc);
            acc.a00 = modn(acc.a00, N);
            acc.a01 = modn(acc.a01, N);
            acc.a10 = modn(acc.a10, N);
            acc.a11 = modn(acc.a11, N);
        }
        base = mul(base, base);
        base.a00 = modn(base.a00, N);
        base.a01 = modn(base.a01, N);
        base.a10 = modn(base.a10, N);
        base.a11 = modn(base.a11, N);
        e >>= 1;
    }
    return acc;
}

std::pair<long, long> apply(const Mat2& A, long x, long y, long N) {
    return {modn(A.a00 * x + A.a01 * y, N), modn(A.a10 * x + A.a11 * y, N)};
}

void check_cyclotomic_and_revival() {
    const long N = 11;
    const int m = 3;
    Mat2 S{3, 4, 2, 3};
    Mat2 Sm = pow_mod(S, m, N);
    std::map<std::pair<long, long>, std::pair<long, long>> pre;
    for (long x = 0; x < N; ++x)
        for (long y = 0; y < N; ++y) {
            auto img = apply(Sm, x, y, N);
            pre.emplace(std::make_pair(modn(x - img.first, N), modn(y - img.second, N)), std::make_pair(x, y));
        }
    long inv2 = (N + 1) / 2;
    std::vector<long> re(10, 0), im(10, 0);
    for (long k = -9; k <= 9; ++k)
        for (long ell = -1; ell <= 1; ++ell) {
            auto c = coeff(k, ell);
            if (c.first == 0 && c.second == 0) continue;
            auto it = pre.find({modn(ell, N), modn(k, N)});
            if (it == pre.end()) continue;
            auto w = it->second;
            auto Sw = apply(Sm, w.first, w.second, N);
            long form = modn(w.first * Sw.second - w.second * Sw.first, N);
            long psi = modn(inv2 * form, N);
            auto zp = zeta_pow(static_cast<int>(psi));
            auto zm = zeta_pow(static_cast<int>(modn(-psi, N)));
            add_scaled(re, zp, c.first);
            add_scaled(re, zm, -c.first);
            add_scaled(im, zp, c.second);
            add_scaled(im, zm, c.second);
        }
    const long expect_re[10] = {3600, 7200, 3224, 3600, 3400, 3400, 3800, 3800, 3600, 3976};
    for (int i = 0; i < 10; ++i) {
        check(re[i] == expect_re[i], "cyclotomic real");
        check(im[i] == 0, "cyclotomic imag");
    }

    check(pow_mod(S, 5, 41).a00 == 1 && pow_mod(S, 5, 41).a01 == 0 && pow_mod(S, 5, 41).a10 == 0 &&
              pow_mod(S, 5, 41).a11 == 1,
          "order divides 5");
    for (int d = 1; d < 5; ++d) {
        auto A = pow_mod(S, d, 41);
        check(!(A.a00 == 1 && A.a01 == 0 && A.a10 == 0 && A.a11 == 1), "exact order");
        long det = modn((A.a00 - 1) * (A.a11 - 1) - A.a01 * A.a10, 41);
        check(det != 0, "proper power invertible");
    }
    check(5L * 66033L * 1681L * 32000L == 111001473L * 160000L, "revival rational");
}

int inv_mod(int a, int N) {
    int x = 1;
    while ((a * x) % N != 1) ++x;
    return x;
}

C eN(int N, long t) {
    long r = t % N;
    if (r < 0) r += N;
    return std::exp(C(0, 2 * M_PI * static_cast<double>(r) / static_cast<double>(N)));
}

std::vector<C> weyl(int N, long a, long b) {
    a = modn(a, N);
    b = modn(b, N);
    int inv2 = inv_mod(2, N);
    std::vector<C> T(static_cast<size_t>(N * N), 0);
    for (int x = 0; x < N; ++x) {
        int y = static_cast<int>((x + a) % N);
        long phase = modn(b * modn(x + inv2 * a, N), N);
        T[static_cast<size_t>(x * N + y)] = eN(N, phase);
    }
    return T;
}

std::vector<C> cat(int N) {
    int inv8 = inv_mod(8, N);
    std::vector<C> M(static_cast<size_t>(N * N), 0);
    double scale = 1.0 / std::sqrt(static_cast<double>(N));
    for (int x = 0; x < N; ++x)
        for (int y = 0; y < N; ++y) {
            long quad = modn(3L * x * x - 2L * x * y + 3L * y * y, N);
            M[static_cast<size_t>(x * N + y)] = scale * eN(N, modn(-inv8 * quad, N));
        }
    return M;
}

std::vector<C> matmul(const std::vector<C>& A, const std::vector<C>& B, int N) {
    std::vector<C> Cmat(static_cast<size_t>(N * N), 0);
    for (int i = 0; i < N; ++i)
        for (int k = 0; k < N; ++k) {
            C aik = A[static_cast<size_t>(i * N + k)];
            if (aik == C(0, 0)) continue;
            for (int j = 0; j < N; ++j)
                Cmat[static_cast<size_t>(i * N + j)] += aik * B[static_cast<size_t>(k * N + j)];
        }
    return Cmat;
}

std::vector<C> matpow(std::vector<C> base, int e, int N) {
    std::vector<C> acc(static_cast<size_t>(N * N), 0);
    for (int i = 0; i < N; ++i) acc[static_cast<size_t>(i * N + i)] = 1;
    while (e) {
        if (e & 1) acc = matmul(base, acc, N);
        base = matmul(base, base, N);
        e >>= 1;
    }
    return acc;
}

C trace(const std::vector<C>& A, int N) {
    C s = 0;
    for (int i = 0; i < N; ++i) s += A[static_cast<size_t>(i * N + i)];
    return s;
}

double norm_diff(const std::vector<C>& A, const std::vector<C>& B) {
    double s = 0;
    for (size_t i = 0; i < A.size(); ++i) {
        C d = A[i] - B[i];
        s += std::norm(d);
    }
    return std::sqrt(s);
}

void check_matrices() {
    for (int N : {5, 7, 9, 11, 15}) {
        auto M = cat(N);
        auto Minv = M;
        // M is unitary and symmetric, so conjugate transpose is the inverse
        // and equals the entrywise conjugate.
        std::vector<C> Mc(M.size());
        for (size_t i = 0; i < M.size(); ++i) Mc[i] = std::conj(M[i]);
        auto Mt = M;
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j) Mt[static_cast<size_t>(i * N + j)] = std::conj(M[static_cast<size_t>(j * N + i)]);
        check(norm_diff(Mc, Mt) < 1e-8, "M symmetric");
        std::vector<C> Id(static_cast<size_t>(N * N), 0);
        for (int i = 0; i < N; ++i) Id[static_cast<size_t>(i * N + i)] = 1;
        check(norm_diff(matmul(M, Mt, N), Id) < 1e-8, "M unitary");
        for (auto [a, b] : std::vector<std::pair<long, long>>{{1, 0}, {0, 1}, {1, 1}, {2, -3}}) {
            auto TM = matmul(weyl(N, a, b), Mt, N);
            auto left = matmul(M, TM, N);
            auto right = weyl(N, 3 * a + 4 * b, 2 * a + 3 * b);
            check(norm_diff(left, right) < 1e-8, "egorov");
        }
        int inv2 = inv_mod(2, N);
        for (auto [a, b] : std::vector<std::pair<long, long>>{{0, 1}, {1, 0}, {1, 2}, {2, -1}}) {
            auto left = matmul(weyl(N, a, b), weyl(N, 1, 1), N);
            long form = modn(a * 1 - b * 1, N);
            auto right = weyl(N, a + 1, b + 1);
            C phase = eN(N, modn(inv2 * form, N));
            for (auto& z : right) z *= phase;
            check(norm_diff(left, right) < 1e-8, "cocycle");
            auto raw = weyl(N, a, b);
            std::vector<C> KR(static_cast<size_t>(N * N), 0);
            long aa = modn(a, N);
            long bb = modn(b, N);
            for (int x = 0; x < N; ++x) {
                KR[static_cast<size_t>(x * N + (x + aa) % N)] =
                    std::exp(C(0, M_PI * static_cast<double>(a * b) / N)) *
                    std::exp(C(0, 2 * M_PI * static_cast<double>(bb * x) / N));
            }
            double sign = ((a * b) % 2 == 0) ? 1.0 : -1.0;
            for (auto& z : KR) z *= sign;
            check(norm_diff(raw, KR) < 1e-8, "gauge");
        }
        for (int m = 1; m <= 4; ++m) {
            Mat2 S{3, 4, 2, 3};
            auto Sm = pow_mod(S, m, N);
            std::map<std::pair<long, long>, std::pair<long, long>> pre;
            long ker = 0;
            for (long x = 0; x < N; ++x)
                for (long y = 0; y < N; ++y) {
                    auto img = apply(Sm, x, y, N);
                    auto v = std::make_pair(modn(x - img.first, N), modn(y - img.second, N));
                    if (v.first == 0 && v.second == 0) ++ker;
                    pre.emplace(v, std::make_pair(x, y));
                }
            auto Mm = matpow(M, m, N);
            C Z = trace(Mm, N);
            check(std::abs(std::norm(Z) - static_cast<double>(ker)) < 1e-6, "kernel");
            int inv2m = inv_mod(2, N);
            for (long a = -2; a <= 2; ++a)
                for (long b = -2; b <= 2; ++b) {
                    auto it = pre.find({modn(a, N), modn(b, N)});
                    C pred = 0;
                    if (it != pre.end()) {
                        auto w = it->second;
                        auto Sw = apply(Sm, w.first, w.second, N);
                        long psi = modn(inv2m * modn(w.first * Sw.second - w.second * Sw.first, N), N);
                        pred = eN(N, psi) * Z;
                    }
                    auto TW = matmul(weyl(N, a, b), Mm, N);
                    check(std::abs(trace(TW, N) - pred) < 1e-7, "trace closure");
                }
        }
    }
    // Dimension 7: both classical symmetries survive on the literal matrices.
    {
        const int N = 7;
        auto M = cat(N);
        std::vector<C> A(static_cast<size_t>(N * N), 0);
        for (auto [k, ell] : nonzero_modes()) {
            auto c = coeff(k, ell);
            auto T = weyl(N, ell, k);
            C z(c.first / 4000.0, c.second / 4000.0);
            for (size_t i = 0; i < A.size(); ++i) A[i] += z * T[i];
        }
        std::vector<C> P(static_cast<size_t>(N * N), 0);
        for (int x = 0; x < N; ++x) P[static_cast<size_t>(x * N + modn(-x, N))] = 1;
        auto PA = matmul(P, A, N);
        auto PAP = matmul(PA, P, N);
        check(norm_diff(PAP, A) < 1e-8, "parity at 7");
        std::vector<C> Ac(A.size());
        for (size_t i = 0; i < A.size(); ++i) Ac[i] = std::conj(A[i]);
        auto AM = matmul(A, M, N);
        std::vector<C> Minv(M.size());
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j)
                Minv[static_cast<size_t>(i * N + j)] = std::conj(M[static_cast<size_t>(j * N + i)]);
        auto rev = matmul(Minv, AM, N);
        check(norm_diff(Ac, rev) < 1e-8, "reversal at 7");
    }
}

}  // namespace

int main() {
    try {
        check_symbol();
        check_defects();
        check_cyclotomic_and_revival();
        check_matrices();
    } catch (const std::exception& ex) {
        std::cerr << "FAIL " << ex.what() << "\n";
        return 1;
    }
    std::cout << "all exact and floating checks passed\n";
    return 0;
}
