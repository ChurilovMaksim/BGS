// Integer kernels and floating occupation sums for BGS-TRACE-127.
// The sixteen-phase block repeats the Python splitmix sample. It is not a
// limit theorem.
#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

namespace {

constexpr double kPi = 0x1.921fb54442d18p+1;
constexpr double kTol = 1e-6;
constexpr int kCert[] = {3, 5, 7, 9, 11, 15, 21, 25, 27, 35, 45, 49, 63, 105};
constexpr int kSampleN[] = {3, 5, 7, 11, 31};
constexpr int kDraws = 24;
constexpr int kMmax = 6;
constexpr uint64_t kSeed = 20261029ULL;

using C = std::complex<double>;
using Mat = std::vector<C>;

int r_num(int k) {
  switch (k) {
    case 0:
      return 4;
    case 1:
    case -1:
      return 2;
    case 7:
    case -7:
      return -2;
    case 6:
    case -6:
    case 8:
    case -8:
      return -1;
    default:
      return 0;
  }
}

std::pair<long long, long long> coeff(int k, int ell) {
  if (ell == 0) {
    long long re = (k == 7 || k == -7 ? 2000LL : 0LL) + 100LL * r_num(k) - (k == 0 ? 400LL : 0LL);
    long long im = -5LL * (r_num(k - 1) - r_num(k + 1));
    return {re, im};
  }
  if (ell == 1) return {-3LL * r_num(k), -4LL * r_num(k)};
  if (ell == -1) return {-3LL * r_num(k), 4LL * r_num(k)};
  return {0, 0};
}

struct Mode {
  int a, b;
  long long re, im;
};

std::vector<Mode> modes() {
  std::vector<Mode> out;
  for (int k = -9; k <= 9; ++k) {
    for (int ell = -1; ell <= 1; ++ell) {
      auto c = coeff(k, ell);
      if (c.first == 0 && c.second == 0) continue;
      out.push_back(Mode{ell, k, c.first, c.second});
    }
  }
  return out;
}

struct Pair {
  int ra, rb;
  long long rre, rim;
  int oa, ob;
  long long ore, oim;
};

std::vector<Pair> pairs_of(const std::vector<Mode>& ms) {
  std::vector<Mode> left = ms;
  std::sort(left.begin(), left.end(), [](const Mode& u, const Mode& v) {
    return u.a < v.a || (u.a == v.a && u.b < v.b);
  });
  std::vector<Pair> out;
  std::vector<char> used(left.size(), 0);
  for (size_t i = 0; i < left.size(); ++i) {
    if (used[i]) continue;
    int wa = -left[i].a, wb = -left[i].b;
    size_t j = left.size();
    for (size_t t = 0; t < left.size(); ++t) {
      if (!used[t] && left[t].a == wa && left[t].b == wb) {
        j = t;
        break;
      }
    }
    if (j == left.size() || j == i) throw std::runtime_error("pair missing");
    const Mode* rep = &left[i];
    const Mode* other = &left[j];
    if (std::make_pair(other->a, other->b) > std::make_pair(rep->a, rep->b)) std::swap(rep, other);
    out.push_back(Pair{rep->a, rep->b, rep->re, rep->im, other->a, other->b, other->re, other->im});
    used[i] = used[j] = 1;
  }
  if (out.size() != 16) throw std::runtime_error("pair count");
  return out;
}

long long symbol_energy(const std::vector<Mode>& ms) {
  long long s = 0;
  for (const auto& m : ms) s += m.re * m.re + m.im * m.im;
  return s;
}

struct M2 {
  long long a, b, c, d;
};

M2 pow_s(int m) {
  M2 acc{1, 0, 0, 1};
  M2 base{3, 4, 2, 3};
  while (m) {
    if (m & 1) {
      acc = M2{acc.a * base.a + acc.b * base.c, acc.a * base.b + acc.b * base.d,
               acc.c * base.a + acc.d * base.c, acc.c * base.b + acc.d * base.d};
    }
    base = M2{base.a * base.a + base.b * base.c, base.a * base.b + base.b * base.d,
              base.c * base.a + base.d * base.c, base.c * base.b + base.d * base.d};
    m >>= 1;
  }
  return acc;
}

int ker(int n, int m) {
  M2 A = pow_s(m);
  long long a = A.a - 1, b = A.b, c = A.c, d = A.d - 1;
  int cnt = 0;
  for (int x = 0; x < n; ++x) {
    for (int y = 0; y < n; ++y) {
      if ((a * x + b * y) % n == 0 && (c * x + d * y) % n == 0) ++cnt;
    }
  }
  return cnt;
}

long long qpoly(long long x, long long y) { return 3 * x * x - 2 * x * y + 3 * y * y; }

void phase_identity(int n) {
  for (int a = 0; a < n; ++a) {
    for (int b = 0; b < n; ++b) {
      for (int c = 0; c < n; ++c) {
        long long left = qpoly(a, b) + qpoly(b, c) + qpoly(c, a);
        long long right = qpoly(a, c) + qpoly(c, b) + qpoly(b, a);
        if (left != right) throw std::runtime_error("phase identity");
      }
    }
  }
}

long long mod_inv(long long a, long long mod) {
  long long t = 0, nt = 1, r = mod, nr = a % mod;
  if (nr < 0) nr += mod;
  while (nr) {
    long long q = r / nr;
    long long tmp = nt;
    nt = t - q * nt;
    t = tmp;
    tmp = nr;
    nr = r - q * nr;
    r = tmp;
  }
  if (r != 1 && r != -1) throw std::runtime_error("inverse");
  if (t < 0) t += mod;
  return t;
}

Mat cat(int n) {
  long long inv8 = mod_inv(8, n);
  Mat M(static_cast<size_t>(n * n));
  const double scale = 1.0 / std::sqrt(static_cast<double>(n));
  for (int x = 0; x < n; ++x) {
    for (int y = 0; y < n; ++y) {
      long long quad = (3LL * x * x - 2LL * x * y + 3LL * y * y) % n;
      if (quad < 0) quad += n;
      long long phase = (n - inv8) % n;
      phase = phase * quad % n;
      double ang = 2.0 * kPi * static_cast<double>(phase) / static_cast<double>(n);
      M[static_cast<size_t>(x * n + y)] = std::polar(scale, ang);
    }
  }
  return M;
}

uint32_t pack_sorted(int m, int a, int b, int c) {
  int v[3] = {a, b, c};
  std::sort(v, v + m);
  uint32_t key = 0;
  for (int i = 0; i < m; ++i) key = (key << 8) | static_cast<uint32_t>(v[i]);
  return key;
}

double occupation_sum(const Mat& M, int n, int m) {
  std::unordered_map<uint32_t, C> buckets;
  auto add = [&](uint32_t key, C amp) { buckets[key] += amp; };
  if (m == 1) {
    for (int a = 0; a < n; ++a) add(pack_sorted(1, a, 0, 0), M[static_cast<size_t>(a * n + a)]);
  } else if (m == 2) {
    for (int a = 0; a < n; ++a) {
      for (int b = 0; b < n; ++b) {
        add(pack_sorted(2, a, b, 0), M[static_cast<size_t>(a * n + b)] * M[static_cast<size_t>(b * n + a)]);
      }
    }
  } else if (m == 3) {
    for (int a = 0; a < n; ++a) {
      for (int b = 0; b < n; ++b) {
        C mab = M[static_cast<size_t>(a * n + b)];
        for (int c = 0; c < n; ++c) {
          add(pack_sorted(3, a, b, c),
              mab * M[static_cast<size_t>(b * n + c)] * M[static_cast<size_t>(c * n + a)]);
        }
      }
    }
  } else {
    throw std::runtime_error("m");
  }
  double s = 0;
  for (const auto& kv : buckets) s += std::norm(kv.second);
  return s;
}

double closed_form(int n, int m) {
  if (m == 1) return 1.0;
  if (m == 2) return static_cast<double>(2 * n - 1) / static_cast<double>(n);
  if (m == 3)
    return static_cast<double>(6 * n * n - 9 * n + 4) / static_cast<double>(n * n);
  throw std::runtime_error("closed");
}

Mat weyl(int n, int a, int b) {
  a %= n;
  if (a < 0) a += n;
  b %= n;
  if (b < 0) b += n;
  long long inv2 = 0;
  {
    long long t = 0, nt = 1, r = n, nr = 2;
    while (nr) {
      long long q = r / nr;
      long long tmp = nt;
      nt = t - q * nt;
      t = tmp;
      tmp = nr;
      nr = r - q * nr;
      r = tmp;
    }
    if (t < 0) t += n;
    inv2 = t;
  }
  Mat T(static_cast<size_t>(n * n), C(0, 0));
  for (int x = 0; x < n; ++x) {
    int y = (x + a) % n;
    long long phase = (static_cast<long long>(b) * (x + inv2 * a)) % n;
    if (phase < 0) phase += n;
    double ang = 2.0 * kPi * static_cast<double>(phase) / static_cast<double>(n);
    T[static_cast<size_t>(x * n + y)] = std::polar(1.0, ang);
  }
  return T;
}

double col_norm(const Mat& A, int n) {
  double best = 0;
  for (int j = 0; j < n; ++j) {
    double s = 0;
    for (int i = 0; i < n; ++i) s += std::abs(A[static_cast<size_t>(i * n + j)]);
    if (s > best) best = s;
  }
  return best;
}

Mat matmul(const Mat& A, const Mat& B, int n) {
  Mat out(static_cast<size_t>(n * n), C(0.0, 0.0));
  for (int i = 0; i < n; ++i) {
    for (int k = 0; k < n; ++k) {
      C aik = A[static_cast<size_t>(i * n + k)];
      for (int j = 0; j < n; ++j) {
        out[static_cast<size_t>(i * n + j)] += aik * B[static_cast<size_t>(k * n + j)];
      }
    }
  }
  return out;
}

Mat expm(const Mat& B, int n) {
  double norm = col_norm(B, n);
  int s = 0;
  if (norm > 1.0) s = static_cast<int>(std::ceil(std::log2(norm)));
  double scale = s ? 1.0 / static_cast<double>(1 << s) : 1.0;
  Mat Bs(B.size());
  for (size_t i = 0; i < B.size(); ++i) Bs[i] = B[i] * scale;
  Mat acc(static_cast<size_t>(n * n), C(0, 0));
  Mat term(static_cast<size_t>(n * n), C(0, 0));
  for (int i = 0; i < n; ++i) {
    acc[static_cast<size_t>(i * n + i)] = 1;
    term[static_cast<size_t>(i * n + i)] = 1;
  }
  for (int k = 1; k < 100; ++k) {
    term = matmul(term, Bs, n);
    for (auto& z : term) z /= static_cast<double>(k);
    for (size_t i = 0; i < acc.size(); ++i) acc[i] += term[i];
    if (col_norm(term, n) < 1e-16) break;
  }
  for (int i = 0; i < s; ++i) acc = matmul(acc, acc, n);
  return acc;
}

C trace(const Mat& A, int n) {
  C s = 0;
  for (int i = 0; i < n; ++i) s += A[static_cast<size_t>(i * n + i)];
  return s;
}

uint64_t splitmix(uint64_t& x) {
  x += 0x9E3779B97F4A7C15ULL;
  uint64_t z = x;
  z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL;
  z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL;
  return z ^ (z >> 31);
}

std::vector<double> sample_means(int n, const std::vector<Pair>& ps) {
  uint64_t state = kSeed;
  std::unordered_map<int, Mat> cache;
  auto at = [&](int a, int b) -> const Mat& {
    int aa = a % n;
    if (aa < 0) aa += n;
    int bb = b % n;
    if (bb < 0) bb += n;
    int key = aa * n + bb;
    auto it = cache.find(key);
    if (it == cache.end()) it = cache.emplace(key, weyl(n, aa, bb)).first;
    return it->second;
  };
  Mat M = cat(n);
  std::vector<double> acc(kMmax, 0.0);
  for (int draw = 0; draw < kDraws; ++draw) {
    double phis[16];
    for (int r = 0; r < 16; ++r) {
      uint64_t z = splitmix(state);
      phis[r] = static_cast<double>(z >> 11) * (1.0 / 9007199254740992.0) * 2.0 * kPi;
    }
    Mat A(static_cast<size_t>(n * n), C(0, 0));
    for (int r = 0; r < 16; ++r) {
      C e = std::polar(1.0, phis[r]);
      C crep(ps[r].rre / 4000.0, ps[r].rim / 4000.0);
      C cother(ps[r].ore / 4000.0, ps[r].oim / 4000.0);
      const Mat& Tr = at(ps[r].ra, ps[r].rb);
      const Mat& To = at(ps[r].oa, ps[r].ob);
      for (size_t i = 0; i < A.size(); ++i) {
        A[i] += crep * e * Tr[i];
        A[i] += cother / e * To[i];
      }
    }
    Mat H = A;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        C zij = A[static_cast<size_t>(i * n + j)];
        C zji = A[static_cast<size_t>(j * n + i)];
        H[static_cast<size_t>(i * n + j)] = 0.5 * (zij + std::conj(zji));
      }
    }
    A.swap(H);
    Mat scaled(A.size());
    for (size_t i = 0; i < A.size(); ++i) scaled[i] = C(0, 1) * 2.0 * A[i];
    Mat K = expm(scaled, n);
    Mat U = matmul(K, M, n);
    Mat T = U;
    for (int m = 0; m < kMmax; ++m) {
      acc[static_cast<size_t>(m)] += std::norm(trace(T, n));
      T = matmul(T, U, n);
    }
  }
  for (double& v : acc) v /= static_cast<double>(kDraws);
  return acc;
}

double pure_trace_square(const Mat& M, int n, int m) {
  Mat P(static_cast<size_t>(n * n), C(0, 0));
  for (int i = 0; i < n; ++i) P[static_cast<size_t>(i * n + i)] = 1;
  for (int k = 0; k < m; ++k) P = matmul(P, M, n);
  return std::norm(trace(P, n));
}

}  // namespace

int main() {
  try {
    auto ms = modes();
    if (ms.size() != 32 || symbol_energy(ms) != 6603300LL) {
      throw std::runtime_error("symbol");
    }
    auto ps = pairs_of(ms);
    for (int n : {3, 5, 7, 9, 11, 15}) phase_identity(n);
    double max_err = 0;
    for (int n : kCert) {
      Mat M = cat(n);
      double scale = 1.0 / std::sqrt(static_cast<double>(n));
      for (const auto& z : M) {
        if (std::abs(std::abs(z) - scale) > 1e-12) throw std::runtime_error("flat");
      }
      int k2 = ker(n, 2);
      int k3 = ker(n, 3);
      int expect3 = (n % 7 == 0) ? 49 : 1;
      int g = std::gcd(14, n);
      if (k2 != 1 || k3 != expect3 || expect3 != g * g) throw std::runtime_error("kernel");
      if (std::abs(pure_trace_square(M, n, 2) - k2) > kTol) throw std::runtime_error("trace2");
      if (std::abs(pure_trace_square(M, n, 3) - k3) > kTol) throw std::runtime_error("trace3");
      for (int m = 1; m <= 3; ++m) {
        double err = std::abs(occupation_sum(M, n, m) - closed_form(n, m));
        if (err > max_err) max_err = err;
        if (err > kTol) throw std::runtime_error("form");
      }
    }
    std::cout << "occupation-max-abs-err " << max_err << "\n";
    if (ker(31, 5) != 1) throw std::runtime_error("ker 31,5");
    std::cout << "kernels-ok odd-N 14 including 3,5,7\n";
    for (int n : kSampleN) {
      auto means = sample_means(n, ps);
      for (int m = 1; m <= kMmax; ++m) {
        std::cout.setf(std::ios::fixed);
        std::cout.precision(12);
        std::cout << "sample N=" << n << " eta=2 m=" << m << " mean=" << means[static_cast<size_t>(m - 1)]
                  << "\n";
      }
    }
    std::cout << "diagonal-phase-form-factor: OK\n";
  } catch (const std::exception& ex) {
    std::cerr << ex.what() << "\n";
    return 1;
  }
  return 0;
}
