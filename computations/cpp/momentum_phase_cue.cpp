// Bucket checks for BGS-TRACE-140.
// Recomputes the Haar reduced-phase form factor at primes 5, 7 and 11.
#include <cmath>
#include <complex>
#include <iostream>
#include <stdexcept>
#include <vector>

namespace {
constexpr double kPi = 0x1.921fb54442d18p+1;

int mod_pow(int a, int e, int p) {
  int r = 1;
  a %= p;
  while (e > 0) {
    if (e & 1) r = static_cast<int>((static_cast<long long>(r) * a) % p);
    a = static_cast<int>((static_cast<long long>(a) * a) % p);
    e >>= 1;
  }
  return r;
}

int mod_inv(int a, int p) {
  return mod_pow(a, p - 2, p);
}

bool admissible(int p, int m, int delta = 3) {
  // Theorem 1 needs only lambda not congruent to -1.
  (void)m;
  const int lam = mod_inv(delta, p);
  return lam != p - 1;
}

long long falling(int p, int m) {
  long long out = 1;
  for (int i = 0; i < m; ++i) out *= (p - i);
  return out;
}

long long factorial(int m) {
  long long out = 1;
  for (int i = 1; i <= m; ++i) out *= i;
  return out;
}

// Occupation key for m <= 4: sort the m letters into base-p digits.
int occ_key(const std::vector<int>& w, int p) {
  std::vector<int> s = w;
  for (int i = 1; i < static_cast<int>(s.size()); ++i) {
    int v = s[i];
    int j = i;
    while (j > 0 && s[j - 1] > v) {
      s[j] = s[j - 1];
      --j;
    }
    s[j] = v;
  }
  int key = 0;
  for (int v : s) key = key * p + v;
  return key;
}

double bucket(int p, int m, int lam) {
  const int nwords = static_cast<int>(std::pow(p, m));
  std::vector<std::complex<double>> acc(static_cast<size_t>(nwords) * nwords);
  std::vector<int> x(m), s(m);
  const double scale = 2.0 * kPi / static_cast<double>(p);
  for (int X = 0; X < nwords; ++X) {
    int tmp = X;
    for (int t = 0; t < m; ++t) {
      x[t] = tmp % p;
      tmp /= p;
    }
    const int ox = occ_key(x, p);
    for (int S = 0; S < nwords; ++S) {
      tmp = S;
      int phase = 0;
      for (int t = 0; t < m; ++t) {
        s[t] = tmp % p;
        tmp /= p;
        const int nxt = x[(t + 1) % m];
        phase += s[t] * (x[t] - lam * nxt);
      }
      phase %= p;
      if (phase < 0) phase += p;
      const int os = occ_key(s, p);
      acc[static_cast<size_t>(ox) * nwords + os] +=
          std::exp(std::complex<double>(0.0, scale * phase));
    }
  }
  double total = 0.0;
  for (const auto& z : acc) total += std::norm(z);
  double denom = 1.0;
  for (int i = 0; i < 2 * m; ++i) denom *= p;
  return total / denom;
}

}  // namespace

int main() {
  // 16/25 * 9/80000 = 9/125000, cross-multiplied.
  const long long left = 16LL * 9 * 125000;
  const long long right = 25LL * 80000 * 9;
  if (left != right) {
    std::cerr << "odd energy cross-multiplication failed\n";
    return 1;
  }
  if (mod_pow(3, 3, 13) != 1) {
    std::cerr << "13 should divide 3^3-1\n";
    return 1;
  }
  for (int p : {5, 7, 11, 13}) {
    for (int m : {2, 3}) {
      if (!admissible(p, m)) {
        std::cerr << "unexpected exclusion " << p << " " << m << "\n";
        return 1;
      }
      const int lam = mod_inv(3, p);
      const double val = bucket(p, m, lam);
      double gap = 0.0;
      double bound = 0.0;
      if (m == 2) {
        gap = std::abs(val - 2.0);
        bound = 20.0 / p;
      } else {
        const double main_term =
            static_cast<double>(m) * static_cast<double>(falling(p, m)) /
            std::pow(static_cast<double>(p), m);
        gap = std::abs(val - main_term);
        bound = static_cast<double>(factorial(m) * factorial(m)) *
                (1.0 + 2.0 * m * (m - 1)) / p;
      }
      std::cout << "p=" << p << " m=" << m << " value=" << val
                << " gap=" << gap << " bound=" << bound << "\n";
      if (gap > bound + 1e-8) {
        std::cerr << "bound failed\n";
        return 1;
      }
    }
  }
  std::cout << "momentum_phase_cue cpp ok\n";
  return 0;
}
