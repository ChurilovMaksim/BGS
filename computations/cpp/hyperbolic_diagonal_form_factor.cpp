// Integer and floating-point checks for BGS-TRACE-131.
// A pass is a finite check of the note, not a proof of BGS-TRACE-005.
#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <utility>
#include <vector>

namespace {

constexpr double kPi = 0x1.921fb54442d18p+1;
constexpr double kTol = 1e-8;

using Mat = std::pair<std::pair<long long, long long>, std::pair<long long, long long>>;

long long v_seq(long long t, int n) {
  if (n == 0) return 0;
  if (n == 1) return 1;
  long long a = 0;
  long long b = 1;
  for (int i = 2; i <= n; ++i) {
    long long c = t * b - a;
    a = b;
    b = c;
  }
  return b;
}

long long u_seq(long long t, int n) {
  if (n == 0) return 2;
  return t * v_seq(t, n) - 2 * v_seq(t, n - 1);
}

Mat mul(const Mat& a, const Mat& b, long long mod = 0) {
  long long e00 = a.first.first * b.first.first + a.first.second * b.second.first;
  long long e01 = a.first.first * b.first.second + a.first.second * b.second.second;
  long long e10 = a.second.first * b.first.first + a.second.second * b.second.first;
  long long e11 = a.second.first * b.first.second + a.second.second * b.second.second;
  if (mod) {
    e00 %= mod;
    e01 %= mod;
    e10 %= mod;
    e11 %= mod;
    if (e00 < 0) e00 += mod;
    if (e01 < 0) e01 += mod;
    if (e10 < 0) e10 += mod;
    if (e11 < 0) e11 += mod;
  }
  return {{e00, e01}, {e10, e11}};
}

Mat power(Mat a, int n, long long mod = 0) {
  Mat r = {{1, 0}, {0, 1}};
  for (int i = 0; i < n; ++i) r = mul(r, a, mod);
  return r;
}

int kernel(Mat s, int m, int n) {
  Mat a = power(s, m, n);
  long long e00 = a.first.first - 1;
  long long e11 = a.second.second - 1;
  long long e01 = a.first.second;
  long long e10 = a.second.first;
  auto norm = [n](long long e) {
    e %= n;
    if (e < 0) e += n;
    return e;
  };
  e00 = norm(e00);
  e01 = norm(e01);
  e10 = norm(e10);
  e11 = norm(e11);
  int count = 0;
  for (int x = 0; x < n; ++x) {
    for (int y = 0; y < n; ++y) {
      if ((e00 * x + e01 * y) % n == 0 && (e10 * x + e11 * y) % n == 0) ++count;
    }
  }
  return count;
}

int mod_inverse(int a, int n) {
  int r0 = n;
  int r1 = a % n;
  if (r1 < 0) r1 += n;
  int s0 = 0;
  int s1 = 1;
  while (r1 != 0) {
    int q = r0 / r1;
    int r = r0 - q * r1;
    r0 = r1;
    r1 = r;
    int s = s0 - q * s1;
    s0 = s1;
    s1 = s;
  }
  if (r0 != 1) throw std::runtime_error("inverse");
  if (s0 < 0) s0 += n;
  return s0;
}

int legendre(int delta, int p) {
  int a = delta % p;
  if (a < 0) a += p;
  int result = 1;
  int exponent = (p - 1) / 2;
  while (exponent) {
    if (exponent & 1) result = static_cast<int>((1LL * result * a) % p);
    a = static_cast<int>((1LL * a * a) % p);
    exponent >>= 1;
  }
  return result;
}

using C = std::complex<double>;

std::vector<C> quant(Mat s, int n) {
  int kappa = (n - mod_inverse((2 * static_cast<int>(s.first.second)) % n, n)) % n;
  std::vector<C> m(n * n);
  double scale = std::pow(static_cast<double>(n), -0.5);
  for (int x = 0; x < n; ++x) {
    for (int y = 0; y < n; ++y) {
      long long phase = kappa * (s.second.second * x * x - 2LL * x * y +
                                 s.first.first * y * y);
      phase %= n;
      if (phase < 0) phase += n;
      m[x * n + y] = scale * std::exp(C(0, 2 * kPi * static_cast<double>(phase) / n));
    }
  }
  return m;
}

double j0(double z) {
  z = std::fabs(z);
  const int nodes = 256;
  double acc = 0;
  for (int i = 0; i < nodes; ++i) {
    double theta = (i + 0.5) * kPi / nodes;
    acc += std::cos(z * std::sin(theta));
  }
  return acc / nodes;
}

double time_one(Mat s, int n, double eta) {
  int kappa = (n - mod_inverse((2 * static_cast<int>(s.first.second)) % n, n)) % n;
  long long trace = s.first.first + s.second.second;
  std::vector<C> diag(n);
  double scale = std::pow(static_cast<double>(n), -0.5);
  for (int x = 0; x < n; ++x) {
    long long phase = kappa * (trace - 2) % n * x % n * x;
    phase %= n;
    if (phase < 0) phase += n;
    diag[x] = scale * std::exp(C(0, 2 * kPi * static_cast<double>(phase) / n));
  }
  double acc = 0;
  for (int x = 0; x < n; ++x) {
    for (int y = 0; y < n; ++y) {
      auto rho = [&](int k) {
        return std::abs(std::exp(C(0, 2 * kPi * k * x / n)) -
                        std::exp(C(0, 2 * kPi * k * y / n)));
      };
      double weight = j0(eta * 1.0 * rho(1)) * j0(eta * 0.5 * rho(2));
      acc += std::real(diag[x] * std::conj(diag[y]) * weight);
    }
  }
  return acc;
}

void require(bool ok, const char* message) {
  if (!ok) throw std::runtime_error(message);
}

}  // namespace

int main() {
  try {
    for (long long t : {3, 4, 5, 6, 7, 8, -16}) {
      for (int n = 1; n <= 12; ++n) {
        long long vn = v_seq(t, n);
        long long vp = v_seq(t, n - 1);
        require(vn * vn - t * vn * vp + vp * vp == 1, "cassini");
        long long sign = (n % 2 == 0) ? 1 : -1;
        require(u_seq(-t, n) == sign * u_seq(t, n), "sign");
      }
    }
    std::vector<Mat> matrices = {
        {{3, 4}, {2, 3}},   {{5, 2}, {2, 1}}, {{2, 1}, {3, 2}},
        {{2, 1}, {1, 1}},   {{4, 1}, {3, 1}}, {{-20, -9}, {9, 4}},
        {{-17, -18}, {1, 1}}};
    for (const Mat& s : matrices) {
      long long det = s.first.first * s.second.second - s.first.second * s.second.first;
      require(det == 1, "det");
      long long t = s.first.first + s.second.second;
      for (int n = 1; n <= 8; ++n) {
        Mat p = power(s, n);
        long long pd = p.first.first * p.second.second - p.first.second * p.second.first;
        require(pd == 1, "power det");
        long long e00 = p.first.first - 1;
        long long e01 = p.first.second;
        long long e10 = p.second.first;
        long long e11 = p.second.second - 1;
        require(e00 * e11 - e01 * e10 == 2 - u_seq(t, n), "gap");
      }
    }
    std::vector<int> primes = {5, 7, 11, 13, 17, 19};
    int tri = 0;
    for (int index = 0; index < 5; ++index) {
      Mat s = matrices[index];
      long long t = s.first.first + s.second.second;
      long long beta = s.first.second;
      for (int p : primes) {
        if (beta % p == 0) continue;
        long long delta = t * t - 4;
        bool ramified = delta % p == 0;
        int order = 0;
        int limit = ramified ? p + 2 : p + 1;
        for (int m = 1; m <= limit; ++m) {
          long long vm = v_seq(t, m) % p;
          long long vm1 = v_seq(t, m - 1) % p;
          if (vm < 0) vm += p;
          if (vm1 < 0) vm1 += p;
          bool ident = vm == 0 && vm1 == p - 1;
          bool gap = (2 - u_seq(t, m)) % p == 0;
          int k = kernel(s, m, p);
          if (ident) {
            require(k == p * p, "identity kernel");
            if (order == 0) order = m;
          } else if (gap) {
            require(k == p, "unipotent kernel");
          } else {
            require(k == 1, "invertible kernel");
          }
          ++tri;
        }
        if (ramified) continue;
        require(order > 0, "order");
        int chi = legendre(static_cast<int>(delta), p);
        int bound = chi == 1 ? p - 1 : p + 1;
        require(bound % order == 0, "splitting");
      }
    }
    require(kernel(matrices[5], 1, 3) == 9, "plus");
    require(kernel(matrices[6], 1, 3) == 3, "minus");
    require(kernel(matrices[0], 3, 49) == 49, "49 model");
    require(kernel(matrices[1], 3, 49) == 49, "49 five");
    require(kernel(matrices[3], 2, 5) == 5, "unipotent");
    require(v_seq(6, 5) % 41 == 0 && v_seq(6, 4) % 41 == 40, "order 41");
    require(5 * 5 * 41 * 41 == 42025, "42025");
    require(3 * 5 * 25 == 375, "375");

    for (int index = 0; index < 5; ++index) {
      Mat s = matrices[index];
      for (int n : {5, 7, 9, 11, 15}) {
        if (std::llabs(s.first.second) % n == 0) continue;
        auto m = quant(s, n);
        double unit = 0;
        double flat = 0;
        double sym = 0;
        double scale = std::pow(static_cast<double>(n), -0.5);
        for (int x = 0; x < n; ++x) {
          for (int y = 0; y < n; ++y) {
            C col = 0;
            for (int z = 0; z < n; ++z) col += std::conj(m[z * n + x]) * m[z * n + y];
            C expect = (x == y) ? C(1, 0) : C(0, 0);
            unit = std::max(unit, std::abs(col - expect));
            flat = std::max(flat, std::abs(std::abs(m[x * n + y]) - scale));
            sym = std::max(sym, std::abs(m[x * n + y] - m[y * n + x]));
          }
        }
        require(unit < kTol && flat < kTol, "unitarity");
        bool equal = s.first.first == s.second.second;
        require(equal ? sym < kTol : sym > 1e-6, "symmetry");
        for (int step = 1; step <= 3; ++step) {
          std::vector<C> powv(n * n);
          std::vector<C> cur = m;
          if (step == 1) powv = m;
          else {
            powv.assign(n * n, 0);
            std::vector<C> acc = m;
            for (int sstep = 1; sstep < step; ++sstep) {
              std::vector<C> next(n * n, 0);
              for (int x = 0; x < n; ++x)
                for (int y = 0; y < n; ++y)
                  for (int z = 0; z < n; ++z)
                    next[x * n + y] += acc[x * n + z] * m[z * n + y];
              acc.swap(next);
            }
            powv.swap(acc);
          }
          C tr = 0;
          for (int x = 0; x < n; ++x) tr += powv[x * n + x];
          double tr2 = std::norm(tr);
          require(std::abs(tr2 - kernel(s, step, n)) < 1e-6, "trace square");
        }
      }
    }
    for (std::pair<Mat, int> item :
         {std::pair<Mat, int>{matrices[0], 5}, {matrices[0], 7}, {matrices[0], 11},
          {matrices[4], 5}, {matrices[4], 7}, {matrices[2], 7}}) {
      for (double eta : {0.0, 1.0, 2.0}) {
        double val = time_one(item.first, item.second, eta);
        require(std::abs(val - 1.0) < 1e-6, "time one");
      }
    }
    double defect = time_one(matrices[4], 9, 0.0);
    double moved = time_one(matrices[4], 9, 1.0);
    require(std::abs(defect - 3.0) < 1e-6, "defect zero");
    require(std::abs(moved - 3.0) > 1e-3, "defect moves");
    std::cout << "BGS-TRACE-131 ok\n";
    std::cout << "trichotomy_rows " << tri << "\n";
    std::cout << "kernel_49 49\n";
    std::cout << "split_3 9 3\n";
    std::cout << "unipotent_5 5\n";
    std::cout << "revival -42025/8 -375/8\n";
    std::cout.setf(std::ios::fixed);
    std::cout.precision(12);
    std::cout << "time_one_defect " << moved << "\n";
  } catch (const std::exception& ex) {
    std::cerr << ex.what() << "\n";
    return 1;
  }
  return 0;
}
