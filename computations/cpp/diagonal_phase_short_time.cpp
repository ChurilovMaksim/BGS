// Floating-point checks for BGS-TRACE-128.
// The inequalities are a finite check of the counting argument, not a proof.
// The quadruple count is an integer census at the primes 5 and 7.
#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

namespace {

constexpr double kPi = 0x1.921fb54442d18p+1;
constexpr double kAbsTol = 1e-8;
constexpr double kUnitTol = 1e-8;

using C = std::complex<double>;

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
  if (r0 != 1) throw std::runtime_error("inverse failed");
  if (s0 < 0) s0 += n;
  return s0;
}

long long factorial(int m) {
  long long out = 1;
  for (int k = 2; k <= m; ++k) out *= k;
  return out;
}

long long falling(int n, int m) {
  if (m > n) return 0;
  long long out = 1;
  for (int k = 0; k < m; ++k) out *= n - k;
  return out;
}

std::vector<int> pi_table(int n, bool invert) {
  std::vector<int> table(n);
  for (int x = 0; x < n; ++x) table[x] = x;
  if (invert) {
    for (int x = 1; x < n; ++x) table[x] = mod_inverse(x, n);
  }
  return table;
}

uint64_t pack_sorted(const std::vector<int>& xs) {
  std::vector<int> sorted = xs;
  std::sort(sorted.begin(), sorted.end());
  uint64_t key = 0;
  for (int value : sorted) key = (key << 6) | static_cast<uint64_t>(value);
  return key;
}

double occupation(int n, int m, bool invert) {
  const int inv8 = mod_inverse(8, n);
  const std::vector<int> pi = pi_table(n, invert);
  std::unordered_map<uint64_t, C> buckets;
  std::vector<int> xs(m, 0);
  const double scale = std::pow(static_cast<double>(n), -0.5 * m);
  const double twopi = 2.0 * kPi;
  auto step = [&]() {
    for (int i = 0; i < m; ++i) {
      xs[i] += 1;
      if (xs[i] < n) return true;
      xs[i] = 0;
    }
    return false;
  };
  while (true) {
    int phase = 0;
    for (int t = 0; t < m; ++t) {
      const int u = pi[xs[t]];
      const int v = (t + 1 == m) ? xs[0] : xs[t + 1];
      const int quad = (3 * u * u - 2 * u * v + 3 * v * v) % n;
      phase += ((-inv8 * quad) % n + n) % n;
    }
    phase %= n;
    const C amp = std::exp(C(0.0, twopi * static_cast<double>(phase) / n)) * scale;
    buckets[pack_sorted(xs)] += amp;
    if (!step()) break;
  }
  double sum = 0.0;
  for (const auto& item : buckets) sum += std::norm(item.second);
  return sum;
}

int entry_phase(int n, int x, int y, bool invert) {
  const int inv8 = mod_inverse(8, n);
  const int u = (invert && x != 0) ? mod_inverse(x, n) : x;
  const int quad = (3 * u * u - 2 * u * y + 3 * y * y) % n;
  return ((-inv8 * quad) % n + n) % n;
}

double unitary_deviation(int n, bool invert) {
  const int inv8 = mod_inverse(8, n);
  const std::vector<int> pi = pi_table(n, invert);
  const double scale = std::pow(static_cast<double>(n), -0.5);
  const double twopi = 2.0 * kPi;
  std::vector<C> mat(static_cast<size_t>(n) * n);
  for (int x = 0; x < n; ++x) {
    for (int y = 0; y < n; ++y) {
      const int u = pi[x];
      const int quad = (3 * u * u - 2 * u * y + 3 * y * y) % n;
      const int phase = ((-inv8 * quad) % n + n) % n;
      mat[static_cast<size_t>(x) * n + y] =
          std::exp(C(0.0, twopi * static_cast<double>(phase) / n)) * scale;
    }
  }
  double worst = 0.0;
  for (int i = 0; i < n; ++i) {
    for (int j = i; j < n; ++j) {
      C inner = 0.0;
      for (int y = 0; y < n; ++y) {
        inner += mat[static_cast<size_t>(i) * n + y] * std::conj(mat[static_cast<size_t>(j) * n + y]);
      }
      const double target = (i == j) ? 1.0 : 0.0;
      worst = std::max(worst, std::abs(inner - target));
    }
  }
  return worst;
}

int quad_count(int p) {
  int count = 0;
  for (int n1 = 1; n1 < p; ++n1) {
    const int inv1 = mod_inverse(n1, p);
    for (int n2 = 1; n2 < p; ++n2) {
      const int sum12 = (n1 + n2) % p;
      const int inv12 = (inv1 + mod_inverse(n2, p)) % p;
      for (int n3 = 1; n3 < p; ++n3) {
        const int inv3 = mod_inverse(n3, p);
        for (int n4 = 1; n4 < p; ++n4) {
          if ((sum12 - n3 - n4) % p != 0) continue;
          if ((inv12 - inv3 - mod_inverse(n4, p)) % p != 0) continue;
          ++count;
        }
      }
    }
  }
  return count;
}

void require(bool condition, const std::string& message) {
  if (!condition) throw std::runtime_error(message);
}

void check_low_times(int n, bool invert, const char* label) {
  const double closed[3] = {0.0, 1.0, (2.0 * n - 1.0) / n};
  for (int m = 1; m <= 2; ++m) {
    const double got = occupation(n, m, invert);
    const double err = std::abs(got - closed[m]);
    std::cout << std::fixed << std::setprecision(12) << label << " N=" << n << " m=" << m << " E=" << got
              << " closed=" << closed[m] << " err=" << std::scientific << std::setprecision(3) << err << "\n";
    require(err <= kAbsTol, "low time failed");
  }
}

double check_symmetric(int n, int m) {
  const double got = occupation(n, m, false);
  const double main = 2.0 * m * static_cast<double>(falling(n, m)) / std::pow(static_cast<double>(n), m);
  const double bound = static_cast<double>(factorial(m)) * (1.0 + m * (m - 1)) / n;
  const double diff = std::abs(got - main);
  const double slack = bound - diff;
  std::cout << std::fixed << std::setprecision(12) << "sym N=" << n << " m=" << m << " E=" << got << " D=" << main
            << " diff=" << std::scientific << std::setprecision(6) << diff << " bound=" << std::fixed << bound
            << " slack=" << std::scientific << slack << "\n";
  require(slack >= -kAbsTol, "symmetric inequality failed");
  if (m == 3) {
    const double closed = (6.0 * n * n - 9.0 * n + 4.0) / (n * n);
    const double exact = (9.0 * n - 8.0) / (n * n);
    require(std::abs(got - closed) <= kAbsTol, "time-three closed form failed");
    require(std::abs((got - main) - exact) <= kAbsTol, "time-three gap failed");
  }
  return got;
}

double check_inversion(int p, int m) {
  const double got = occupation(p, m, true);
  const double main = m * static_cast<double>(falling(p, m)) / std::pow(static_cast<double>(p), m);
  const double bound =
      static_cast<double>(factorial(m)) * (std::pow(3.0, 0.25) * std::pow(static_cast<double>(p), -0.25) +
                                            (m * (m - 1) + 2.0) / p);
  const double diff = std::abs(got - main);
  const double slack = bound - diff;
  std::cout << std::fixed << std::setprecision(12) << "inv p=" << p << " m=" << m << " E=" << got << " main=" << main
            << " diff=" << std::scientific << std::setprecision(6) << diff << " bound=" << std::fixed << bound
            << " slack=" << std::scientific << slack << "\n";
  require(slack >= -kAbsTol, "inversion inequality failed");
  return got;
}

}  // namespace

int main() {
  try {
    const int sym_odd[] = {3, 5, 7, 9, 11, 13, 15};
    const int sym_m4[] = {21, 31, 41, 49};
    const int primes[] = {3, 5, 7, 11, 13, 17, 19, 23, 29, 31};
    for (int n : sym_odd) {
      check_low_times(n, false, "sym");
      for (int m = 3; m <= 5; ++m) check_symmetric(n, m);
      const double dev = unitary_deviation(n, false);
      std::cout << "unit sym N=" << n << " dev=" << std::scientific << dev << "\n";
      require(dev <= kUnitTol, "symmetric unitarity failed");
    }
    for (int n : sym_m4) {
      check_symmetric(n, 4);
      const double dev = unitary_deviation(n, false);
      std::cout << "unit sym N=" << n << " dev=" << std::scientific << dev << "\n";
      require(dev <= kUnitTol, "symmetric unitarity failed");
    }
    for (int p : primes) {
      check_low_times(p, true, "inv");
      double sym3 = 0.0;
      double sym4 = 0.0;
      if (p == 3) {
        sym3 = occupation(3, 3, false);
        sym4 = occupation(3, 4, false);
      }
      for (int m = 3; m <= 4; ++m) {
        const double got = check_inversion(p, m);
        if (p == 3) {
          const double err = std::abs(got - (m == 3 ? sym3 : sym4));
          std::cout << "id p=3 m=" << m << " err=" << std::scientific << err << "\n";
          require(err <= kAbsTol, "p=3 identity failed");
        }
      }
      if (p >= 5) {
        const int x = (p == 11) ? 2 : 1;
        const int y = (p == 11) ? 0 : 2;
        const int delta = (entry_phase(p, x, y, true) - entry_phase(p, y, x, true) + 2 * p) % p;
        std::cout << std::defaultfloat << "nonsym p=" << p << " pair=" << x << "," << y << " delta=" << delta << "\n";
        require(delta != 0, "inversion still symmetric");
      }
      const double dev = unitary_deviation(p, true);
      std::cout << "unit inv p=" << p << " dev=" << std::scientific << dev << "\n";
      require(dev <= kUnitTol, "inversion unitarity failed");
    }
    const int expected[] = {36, 90};
    const int caps[] = {48, 108};
    const int ps[] = {5, 7};
    for (int i = 0; i < 2; ++i) {
      const int got = quad_count(ps[i]);
      std::cout << "kloosterman p=" << ps[i] << " count=" << got << " cap=" << caps[i] << "\n";
      require(got == expected[i], "quadruple census failed");
      require(got <= caps[i], "quadruple cap failed");
    }
    std::cout << "PASS\n";
  } catch (const std::exception& ex) {
    std::cerr << ex.what() << "\n";
    return 1;
  }
  return 0;
}
