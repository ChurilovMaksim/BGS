// Occupation checks for BGS-TRACE-132.
// A pass checks the inequalities. It does not prove BGS-TRACE-005.
#include <algorithm>
#include <cmath>
#include <complex>
#include <iostream>
#include <map>
#include <stdexcept>
#include <vector>

namespace {

constexpr double kPi = 0x1.921fb54442d18p+1;
using C = std::complex<double>;
using MatI = std::vector<long long>;

int mod_inverse(int a, int n) {
  int r0 = n, r1 = a % n;
  if (r1 < 0) r1 += n;
  int s0 = 0, s1 = 1;
  while (r1) {
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

std::vector<C> quant(long long alpha, long long beta, long long delta, int n, bool invert) {
  int kappa = (n - mod_inverse(static_cast<int>((2 * beta) % n), n)) % n;
  std::vector<int> pi(n);
  for (int x = 0; x < n; ++x) pi[x] = x;
  if (invert) {
    for (int x = 1; x < n; ++x) pi[x] = mod_inverse(x, n);
  }
  std::vector<C> m(n * n);
  double scale = std::pow(static_cast<double>(n), -0.5);
  for (int x = 0; x < n; ++x) {
    int xx = pi[x];
    for (int y = 0; y < n; ++y) {
      long long phase = kappa * (delta * xx * xx - 2LL * xx * y + alpha * y * y);
      phase %= n;
      if (phase < 0) phase += n;
      m[x * n + y] = scale * std::exp(C(0, 2 * kPi * static_cast<double>(phase) / n));
    }
  }
  return m;
}

double occupation(const std::vector<C>& m, int n, int len) {
  std::map<std::vector<int>, C> buckets;
  std::vector<int> word(len, 0);
  auto rec = [&](auto&& self, int pos) -> void {
    if (pos == len) {
      C amp = 1;
      for (int t = 0; t < len; ++t) amp *= m[word[t] * n + word[(t + 1) % len]];
      auto key = word;
      std::sort(key.begin(), key.end());
      buckets[key] += amp;
      return;
    }
    for (int x = 0; x < n; ++x) {
      word[pos] = x;
      self(self, pos + 1);
    }
  };
  rec(rec, 0);
  double acc = 0;
  for (const auto& item : buckets) acc += std::norm(item.second);
  return acc;
}

long long falling(int n, int m) {
  long long out = 1;
  for (int k = 0; k < m; ++k) out *= n - k;
  return out;
}

long long fact(int m) {
  long long out = 1;
  for (int k = 2; k <= m; ++k) out *= k;
  return out;
}

void require(bool ok, const char* message) {
  if (!ok) throw std::runtime_error(message);
}

}  // namespace

int main() {
  try {
    struct Row { long long a, b, d; };
    std::vector<Row> matrices = {{3, 4, 3}, {2, 1, 1}, {5, 2, 1}};
    int rows = 0;
    for (Row s : matrices) {
      for (int n : {5, 7, 9, 11, 15}) {
        if (s.b % n == 0) continue;
        auto m = quant(s.a, s.b, s.d, n, false);
        if (n <= 7) {
          require(std::abs(occupation(m, n, 1) - 1.0) < 1e-6, "time1");
          require(std::abs(occupation(m, n, 2) - (2.0 * n - 1) / n) < 1e-6, "time2");
        }
        for (int len : {3, 4}) {
          double got = occupation(m, n, len);
          double main = 2.0 * len * static_cast<double>(falling(n, len)) / std::pow(n, len);
          double bound = static_cast<double>(fact(len) * (1 + len * (len - 1))) / n;
          require(std::abs(got - main) <= bound + 1e-8, "haar");
          ++rows;
        }
      }
      for (int p : {5, 7, 11}) {
        if (s.b % p == 0) continue;
        auto m = quant(s.a, s.b, s.d, p, true);
        for (int len : {3, 4}) {
          double got = occupation(m, p, len);
          double main = 1.0 * len * static_cast<double>(falling(p, len)) / std::pow(p, len);
          double bound = static_cast<double>(fact(len)) *
                         (std::pow(3.0, 0.25) * std::pow(p, -0.25) +
                          (len * (len - 1) + 2.0) / p);
          require(std::abs(got - main) <= bound + 1e-6, "inv");
          ++rows;
        }
      }
    }
    auto plain = quant(3, 4, 3, 3, false);
    auto inv = quant(3, 4, 3, 3, true);
    double p3 = occupation(plain, 3, 3);
    require(std::abs(p3 - occupation(inv, 3, 3)) < 1e-8, "p3");
    require(121 * 11 > 6 * 18, "majorant");
    std::cout << "BGS-TRACE-132 ok\n";
    std::cout << "inequality_rows " << rows << "\n";
    std::cout.setf(std::ios::fixed);
    std::cout.precision(12);
    std::cout << "p3_time3 " << p3 << "\n";
  } catch (const std::exception& ex) {
    std::cerr << ex.what() << "\n";
    return 1;
  }
  return 0;
}
