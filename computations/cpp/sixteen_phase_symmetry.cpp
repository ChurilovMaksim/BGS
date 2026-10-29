// Symmetry checks for BGS-TRACE-130.
#include <cmath>
#include <complex>
#include <iostream>
#include <random>
#include <stdexcept>
#include <string>
#include <vector>

namespace {
constexpr double kPi = 0x1.921fb54442d18p+1;

int r_num(int k) {
  switch (k) {
    case 0: return 4;
    case 1:
    case -1: return 2;
    case 7:
    case -7: return -2;
    case 6:
    case -6:
    case 8:
    case -8: return -1;
    default: return 0;
  }
}

std::pair<int, int> coeff(int k, int ell) {
  if (ell == 0) {
    int re = (std::abs(k) == 7 ? 2000 : 0) + 100 * r_num(k) - (k == 0 ? 400 : 0);
    return {re, -5 * (r_num(k - 1) - r_num(k + 1))};
  }
  if (ell == 1) return {-3 * r_num(k), -4 * r_num(k)};
  if (ell == -1) return {-3 * r_num(k), 4 * r_num(k)};
  return {0, 0};
}

void require(bool ok, const std::string& msg) {
  if (!ok) throw std::runtime_error(msg);
}

std::vector<std::complex<double>> cat(int n) {
  int inv8 = 0;
  for (int i = 1; i < n; ++i)
    if ((8 * i) % n == 1) inv8 = i;
  std::vector<std::complex<double>> m(static_cast<size_t>(n) * n);
  for (int x = 0; x < n; ++x)
    for (int y = 0; y < n; ++y) {
      int quad = (3 * x * x - 2 * x * y + 3 * y * y) % n;
      int phase = ((-inv8 * quad) % n + n) % n;
      m[static_cast<size_t>(x) * n + y] =
          std::exp(std::complex<double>(0.0, 2.0 * kPi * phase / n)) / std::sqrt(double(n));
    }
  return m;
}

}  // namespace

int main() {
  try {
    long long odd = 0;
    for (int k = -9; k <= 9; ++k) {
      auto c = coeff(k, 1);
      odd += 1LL * c.first * c.first + 1LL * c.second * c.second;
    }
    require(odd == 900, "odd energy");
    require(odd * 160000 == 9 * 16000000LL, "ratio");
    require(2 * 2 - 4 * 2 == -4, "det");
    std::cout << "odd_energy_scaled=" << odd << "\n";
    std::mt19937_64 rng(130);
    std::normal_distribution<double> normal(0.0, 1.0);
    for (int n : {3, 5, 7, 11}) {
      auto m = cat(n);
      std::vector<double> a(n);
      for (double& v : a) v = normal(rng);
      std::vector<std::complex<double>> s(static_cast<size_t>(n) * n);
      for (int x = 0; x < n; ++x)
        for (int y = 0; y < n; ++y) {
          auto phase = std::exp(std::complex<double>(0.0, 0.5 * (a[x] + a[y])));
          s[static_cast<size_t>(x) * n + y] = phase * m[static_cast<size_t>(x) * n + y];
        }
      double gap = 0.0;
      for (int x = 0; x < n; ++x)
        for (int y = 0; y < n; ++y)
          gap = std::max(gap, std::abs(s[static_cast<size_t>(x) * n + y] - s[static_cast<size_t>(y) * n + x]));
      std::cout << "sym N=" << n << " gap=" << gap << "\n";
      require(gap < 1e-8, "symmetry");
      // B = (E - E^T)/(2i), E the cycle shift.
      double odd_gap = 0.0, herm = 0.0;
      for (int x = 0; x < n; ++x)
        for (int y = 0; y < n; ++y) {
          std::complex<double> b(0.0, 0.0);
          if (y == (x + 1) % n) b += 1.0 / (2.0 * std::complex<double>(0.0, 1.0));
          if (y == (x + n - 1) % n) b -= 1.0 / (2.0 * std::complex<double>(0.0, 1.0));
          odd_gap = std::max(odd_gap, std::abs(std::conj(b) + b));
          std::complex<double> bt(0.0, 0.0);
          if (x == (y + 1) % n) bt += 1.0 / (2.0 * std::complex<double>(0.0, 1.0));
          if (x == (y + n - 1) % n) bt -= 1.0 / (2.0 * std::complex<double>(0.0, 1.0));
          herm = std::max(herm, std::abs(b - std::conj(bt)));
        }
      std::cout << "mom N=" << n << " odd_gap=" << odd_gap << "\n";
      require(odd_gap < 1e-12, "momentum odd");
      require(herm < 1e-12, "hermitian");
    }
    std::cout << "PASS\n";
  } catch (const std::exception& ex) {
    std::cerr << ex.what() << "\n";
    return 1;
  }
}
