#pragma once
// Shared helpers for revival_closure_law.cpp and revival_half_period_parity.cpp.

#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

namespace revival {

constexpr double kPi = 0x1.921fb54442d18p+1;
constexpr double kLam = 3.0 + 2.0 * std::sqrt(2.0);

using C = std::complex<double>;
using Mat = std::vector<C>;

inline void require(bool cond, const std::string& msg) {
  if (!cond) {
    std::cout << "FAIL: " << msg << "\n";
    std::exit(1);
  }
}

inline double r_coeff(int k) {
  switch (k) {
    case 0:
      return 1.0;
    case 1:
    case -1:
      return 0.5;
    case 7:
    case -7:
      return -0.5;
    case 6:
    case -6:
    case 8:
    case -8:
      return -0.25;
    default:
      return 0.0;
  }
}

inline std::pair<double, double> diag_coeff(int k) {
  const double re =
      (std::abs(k) == 7 ? 0.5 : 0.0) + r_coeff(k) / 10.0 - (k == 0 ? 0.1 : 0.0);
  const double im = -(r_coeff(k - 1) - r_coeff(k + 1)) / 200.0;
  return {re, im};
}

struct DiagMode {
  int k;
  C c;
};

inline std::vector<DiagMode> build_diag() {
  std::vector<DiagMode> out;
  for (int k = 1; k < 10; ++k) {
    auto dc = diag_coeff(k);
    if (dc.first == 0.0 && dc.second == 0.0) continue;
    out.push_back(DiagMode{k, C(dc.first, dc.second)});
  }
  return out;
}

inline const std::vector<DiagMode>& diag_modes() {
  static const std::vector<DiagMode> modes = build_diag();
  return modes;
}

inline double sigma_d() {
  double s = 0.0;
  for (int k = 1; k < 10; ++k) {
    auto dc = diag_coeff(k);
    if (dc.first == 0.0 && dc.second == 0.0) continue;
    s += 2.0 * (dc.first * dc.first + dc.second * dc.second);
  }
  return s;
}

inline int k_max() {
  int km = 0;
  for (const auto& m : diag_modes()) km = std::max(km, m.k);
  return km;
}

inline long long mod_ll(long long x, long long n) {
  long long r = x % n;
  if (r < 0) r += n;
  return r;
}

inline long long mod_inv(long long a, long long n) {
  long long t = 0, nt = 1, r = n, nr = mod_ll(a, n);
  while (nr != 0) {
    const long long q = r / nr;
    const long long tmp = nt;
    nt = t - q * nt;
    t = tmp;
    const long long tmp2 = nr;
    nr = r - q * nr;
    r = tmp2;
  }
  require(r == 1, "mod_inv");
  if (t < 0) t += n;
  return t;
}

inline C e_n(int n, long long t) {
  const long long r = mod_ll(t, n);
  return std::polar(1.0, 2.0 * kPi * static_cast<double>(r) / static_cast<double>(n));
}

inline std::tuple<long long, long long, long long, long long> spow(int d) {
  long long a = 1, b = 0, c = 0, e = 1;
  for (int i = 0; i < d; ++i) {
    const long long na = 3 * a + 2 * b;
    const long long nb = 4 * a + 3 * b;
    const long long nc = 3 * c + 2 * e;
    const long long ne = 4 * c + 3 * e;
    a = na;
    b = nb;
    c = nc;
    e = ne;
  }
  return {a, b, c, e};
}

inline std::tuple<int, int, int, int> spow_mod(int d, int n) {
  long long a = 1, b = 0, c = 0, e = 1;
  for (int i = 0; i < d; ++i) {
    const long long na = mod_ll(3 * a + 2 * b, n);
    const long long nb = mod_ll(4 * a + 3 * b, n);
    const long long nc = mod_ll(3 * c + 2 * e, n);
    const long long ne = mod_ll(4 * c + 3 * e, n);
    a = na;
    b = nb;
    c = nc;
    e = ne;
  }
  return {static_cast<int>(a), static_cast<int>(b), static_cast<int>(c), static_cast<int>(e)};
}

inline int order(int n) {
  long long a = 1, b = 0, c = 0, e = 1;
  for (int t = 1; t < 6 * n * n; ++t) {
    const long long na = mod_ll(3 * a + 2 * b, n);
    const long long nb = mod_ll(4 * a + 3 * b, n);
    const long long nc = mod_ll(3 * c + 2 * e, n);
    const long long ne = mod_ll(4 * c + 3 * e, n);
    a = na;
    b = nb;
    c = nc;
    e = ne;
    if (a == 1 && b == 0 && c == 0 && e == 1) return t;
  }
  throw std::runtime_error("order not found");
}

class Pcg64 {
 public:
  explicit Pcg64(uint64_t seed) {
#if defined(__SIZEOF_INT128__)
    const uint64_t* words = seed_words(seed);
    const u128 initstate = (static_cast<u128>(words[0]) << 64) | words[1];
    const u128 initseq = (static_cast<u128>(words[2]) << 64) | words[3];
    state_ = 0;
    inc_ = (initseq << 1) | 1;
    step();
    state_ += initstate;
    step();
#else
    require(false, "Pcg64 requires 128-bit integer support");
#endif
  }

  uint64_t next_u64() {
#if defined(__SIZEOF_INT128__)
    step();
    const uint64_t hi = static_cast<uint64_t>(state_ >> 64);
    const uint64_t lo = static_cast<uint64_t>(state_);
    const unsigned rot = static_cast<unsigned>(hi >> 58);
    return rot64(hi ^ lo, rot);
#else
    return 0;
#endif
  }

  double uniform(double lo, double hi) {
    const double u = (next_u64() >> 11) * (1.0 / 9007199254740992.0);
    return lo + (hi - lo) * u;
  }

  int64_t integers(int64_t lo, int64_t hi) {
    require(hi > lo, "integers bounds");
    const uint64_t bound = static_cast<uint64_t>(hi - lo);
    if (bound == 0) return lo;
    const uint64_t threshold = static_cast<uint64_t>(-bound) % bound;
    while (true) {
      const uint64_t r = next_u64();
#if defined(__SIZEOF_INT128__)
      const u128 prod = static_cast<u128>(r) * bound;
      if (static_cast<uint64_t>(prod) < threshold) continue;
      return lo + static_cast<int64_t>(prod >> 64);
#else
      require(false, "Pcg64 requires 128-bit integer support");
#endif
    }
  }

 private:
#if defined(__SIZEOF_INT128__)
  using u128 = unsigned __int128;
  static constexpr u128 kMult =
      (static_cast<u128>(2549297995355413924ULL) << 64) | 4865540595714422341ULL;

  static uint64_t rot64(uint64_t value, unsigned rot) {
    return (value >> rot) | (value << ((-static_cast<int>(rot)) & 63));
  }

  static const uint64_t* seed_words(uint64_t seed) {
    static const uint64_t k20261029[4] = {12835132708468342910ULL, 2404563375907808236ULL,
                                          12362633101553468378ULL, 4941175820035702272ULL};
    static const uint64_t k20261030[4] = {5403144766159761753ULL, 3924840635982624126ULL,
                                          1918294424417117553ULL, 11856450935557650943ULL};
    static const uint64_t k20261031[4] = {11778827977017204989ULL, 503919316614023805ULL,
                                          5410581971906314141ULL, 16960120388897983934ULL};
    switch (seed) {
      case 20261029ULL:
        return k20261029;
      case 20261030ULL:
        return k20261030;
      case 20261031ULL:
        return k20261031;
      default:
        require(false, "unsupported PCG seed");
        return k20261029;
    }
  }

  void step() { state_ = state_ * kMult + inc_; }

  u128 state_{0};
  u128 inc_{0};
#endif
};

inline Mat cat(int n) {
  const long long inv8 = mod_inv(8, n);
  Mat M(static_cast<size_t>(n * n), C(0, 0));
  const double scale = 1.0 / std::sqrt(static_cast<double>(n));
  for (int x = 0; x < n; ++x) {
    for (int y = 0; y < n; ++y) {
      long long quad = mod_ll(3LL * x * x - 2LL * x * y + 3LL * y * y, n);
      long long phase = mod_ll(-inv8 * quad, n);
      M[static_cast<size_t>(x * n + y)] = scale * e_n(n, phase);
    }
  }
  return M;
}

inline Mat weyl(int n, int a, int b) {
  a = static_cast<int>(mod_ll(a, n));
  b = static_cast<int>(mod_ll(b, n));
  const int inv2 = static_cast<int>(mod_inv(2, n));
  Mat T(static_cast<size_t>(n * n), C(0, 0));
  for (int x = 0; x < n; ++x) {
    const int y = (x + a) % n;
    const long long phase = mod_ll(static_cast<long long>(b) * mod_ll(x + inv2 * a, n), n);
    T[static_cast<size_t>(x * n + y)] = e_n(n, phase);
  }
  return T;
}

inline Mat matmul(const Mat& A, const Mat& B, int n) {
  Mat out(static_cast<size_t>(n * n), C(0, 0));
  for (int i = 0; i < n; ++i) {
    for (int k = 0; k < n; ++k) {
      const C aik = A[static_cast<size_t>(i * n + k)];
      if (aik == C(0, 0)) continue;
      for (int j = 0; j < n; ++j) {
        out[static_cast<size_t>(i * n + j)] += aik * B[static_cast<size_t>(k * n + j)];
      }
    }
  }
  return out;
}

inline Mat matpow(Mat base, int e, int n) {
  Mat acc(static_cast<size_t>(n * n), C(0, 0));
  for (int i = 0; i < n; ++i) acc[static_cast<size_t>(i * n + i)] = 1;
  while (e > 0) {
    if (e & 1) acc = matmul(base, acc, n);
    base = matmul(base, base, n);
    e >>= 1;
  }
  return acc;
}

inline C trace(const Mat& A, int n) {
  C s(0, 0);
  for (int i = 0; i < n; ++i) s += A[static_cast<size_t>(i * n + i)];
  return s;
}

inline Mat conj_transpose(const Mat& A, int n) {
  Mat out(static_cast<size_t>(n * n));
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      out[static_cast<size_t>(i * n + j)] = std::conj(A[static_cast<size_t>(j * n + i)]);
    }
  }
  return out;
}

inline double norm_max_diff(const Mat& A, const Mat& B) {
  double m = 0.0;
  for (size_t i = 0; i < A.size(); ++i) m = std::max(m, std::abs(A[i] - B[i]));
  return m;
}

inline std::vector<C> fft(const std::vector<C>& x) {
  const int n = static_cast<int>(x.size());
  std::vector<C> out(static_cast<size_t>(n), C(0, 0));
  for (int k = 0; k < n; ++k) {
    C sum(0, 0);
    for (int j = 0; j < n; ++j) {
      sum += x[static_cast<size_t>(j)] *
             std::polar(1.0, -2.0 * kPi * static_cast<double>(j * k) / static_cast<double>(n));
    }
    out[static_cast<size_t>(k)] = sum;
  }
  return out;
}

inline std::vector<C> diag_kick(int n, const std::vector<double>& phi, double eta) {
  std::vector<double> f(static_cast<size_t>(n), 0.0);
  const auto& modes = diag_modes();
  require(static_cast<int>(phi.size()) == static_cast<int>(modes.size()), "phi size");
  for (size_t r = 0; r < modes.size(); ++r) {
    const int k = modes[r].k;
    const C c = modes[r].c;
    const C phase = std::polar(1.0, phi[r]);
    for (int x = 0; x < n; ++x) {
      const C ex = e_n(n, static_cast<long long>(k) * x);
      f[static_cast<size_t>(x)] += 2.0 * std::real(c * phase * ex);
    }
  }
  std::vector<C> d(static_cast<size_t>(n));
  for (int x = 0; x < n; ++x) d[static_cast<size_t>(x)] = std::polar(1.0, eta * f[static_cast<size_t>(x)]);
  return d;
}

inline Mat diag_matrix(const std::vector<C>& d, int n) {
  Mat D(static_cast<size_t>(n * n), C(0, 0));
  for (int i = 0; i < n; ++i) D[static_cast<size_t>(i * n + i)] = d[static_cast<size_t>(i)];
  return D;
}

inline Mat scale_rows(const Mat& M, const std::vector<C>& d, int n) {
  Mat out = M;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      out[static_cast<size_t>(i * n + j)] *= d[static_cast<size_t>(i)];
    }
  }
  return out;
}

inline C trace_kicked_product(int n, int m, const std::vector<C>& d, const Mat& mm) {
  Mat prod(static_cast<size_t>(n * n), C(0, 0));
  for (int i = 0; i < n; ++i) prod[static_cast<size_t>(i * n + i)] = 1;
  Mat mj = prod;
  const Mat D = diag_matrix(d, n);
  for (int t = 0; t < m; ++t) {
    const Mat mct = conj_transpose(mj, n);
    Mat step = matmul(mj, D, n);
    step = matmul(step, mct, n);
    prod = matmul(prod, step, n);
    mj = matmul(mm, mj, n);
  }
  return trace(prod, n);
}

inline double bessel_j0(double z) {
  double term = 1.0, total = 1.0;
  const double y = (z / 2.0) * (z / 2.0);
  for (int k = 1; k < 80; ++k) {
    term *= -y / (static_cast<double>(k) * k);
    total += term;
    if (std::abs(term) < 1e-18 * std::max(1.0, std::abs(total))) break;
  }
  return total;
}

inline double bessel_i0(double z) {
  double term = 1.0, total = 1.0;
  const double y = (z / 2.0) * (z / 2.0);
  for (int k = 1; k < 80; ++k) {
    term *= y / (static_cast<double>(k) * k);
    total += term;
    if (std::abs(term) < 1e-18 * std::max(1.0, std::abs(total))) break;
  }
  return total;
}

}  // namespace revival
