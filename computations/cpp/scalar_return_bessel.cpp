// Integer orbit counts and floating Bessel sums for BGS-TRACE-129.
#include <cmath>
#include <complex>
#include <cstdint>
#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
#include <utility>
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
    int im = -5 * (r_num(k - 1) - r_num(k + 1));
    return {re, im};
  }
  if (ell == 1) return {-3 * r_num(k), -4 * r_num(k)};
  if (ell == -1) return {-3 * r_num(k), 4 * r_num(k)};
  return {0, 0};
}

struct Mode { int ell, k, re, im; };

std::vector<Mode> modes() {
  std::vector<Mode> out;
  for (int k = -9; k <= 9; ++k)
    for (int ell = -1; ell <= 1; ++ell) {
      auto c = coeff(k, ell);
      if (c.first || c.second) out.push_back(Mode{ell, k, c.first, c.second});
    }
  return out;
}

void require(bool ok, const std::string& msg) {
  if (!ok) throw std::runtime_error(msg);
}

struct Orbit {
  int m;
  std::vector<std::pair<int, int>> rows;
};

Orbit order_and_rows(int n) {
  int aa = 1, bb = 0, cc = 0, dd = 1;
  Orbit out;
  for (int t = 0; t < n * n + 3; ++t) {
    out.rows.push_back({aa % n, bb % n});
    if (t > 0 && aa % n == 1 && bb % n == 0 && cc % n == 0 && dd % n == 1) {
      out.m = t;
      out.rows.pop_back();
      return out;
    }
    int na = (3 * aa + 2 * bb) % n;
    int nb = (4 * aa + 3 * bb) % n;
    int nc = (3 * cc + 2 * dd) % n;
    int nd = (4 * cc + 3 * dd) % n;
    aa = na; bb = nb; cc = nc; dd = nd;
  }
  throw std::runtime_error("order not found");
}

long long quadruples(const std::vector<std::pair<int, int>>& rows, int n) {
  std::map<std::pair<int, int>, int> sums;
  for (auto u : rows)
    for (auto v : rows) {
      auto key = std::make_pair((u.first + v.first) % n, (u.second + v.second) % n);
      sums[key] += 1;
    }
  long long total = 0;
  for (auto& item : sums) total += 1LL * item.second * item.second;
  return total;
}

double bessel_j0(double z) {
  double term = 1.0, total = 1.0, y = (z / 2.0) * (z / 2.0);
  for (int k = 1; k < 40; ++k) {
    term *= -y / (k * k);
    total += term;
  }
  return total;
}

struct Pair { int k; double amp; };

std::vector<Pair> diagonal_pairs(const std::vector<Mode>& all) {
  std::map<int, double> found;
  for (auto m : all) {
    if (m.ell != 0) continue;
    int rep = m.k > -m.k ? m.k : -m.k;
    if (!found.count(rep)) {
      double re = m.re / 4000.0, im = m.im / 4000.0;
      found[rep] = std::sqrt(re * re + im * im);
    }
  }
  std::vector<Pair> out;
  for (auto& item : found) out.push_back(Pair{item.first, item.second});
  return out;
}

std::vector<std::complex<double>> phasors(int n, int m, int k) {
  std::vector<std::complex<double>> out(static_cast<size_t>(n) * n);
  size_t idx = 0;
  for (int q = 0; q < n; ++q)
    for (int p = 0; p < n; ++p) {
      std::complex<double> acc = 0;
      int qq = q, pp = p;
      for (int j = 0; j < m; ++j) {
        acc += std::exp(std::complex<double>(0.0, 2.0 * kPi * ((k % n) * qq % n) / n));
        int nq = (3 * qq + 4 * pp) % n;
        int np = (2 * qq + 3 * pp) % n;
        qq = nq; pp = np;
      }
      out[idx++] = acc;
    }
  return out;
}

double bessel_average(int n, int m, double eta, const std::vector<Pair>& pairs) {
  std::vector<std::pair<double, std::vector<std::complex<double>>>> vs;
  for (auto pr : pairs)
    if (pr.k % n != 0) vs.push_back({pr.amp, phasors(n, m, pr.k)});
  const int N2 = n * n;
  double total = 0.0;
  for (int i = 0; i < N2; ++i) {
    for (int j = 0; j < N2; ++j) {
      double prod = 1.0;
      for (auto& item : vs) {
        double diff = std::abs(item.second[i] - item.second[j]);
        prod *= bessel_j0(2.0 * eta * item.first * diff);
      }
      total += prod;
    }
  }
  return total / (static_cast<double>(N2) * N2);
}

double sigma_diag(int n, const std::vector<Pair>& pairs) {
  double s = 0.0;
  for (auto pr : pairs)
    if (pr.k % n != 0) s += 2.0 * pr.amp * pr.amp;
  return s;
}

uint64_t splitmix(uint64_t& x) {
  x += 0x9E3779B97F4A7C15ULL;
  uint64_t z = x;
  z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL;
  z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL;
  return z ^ (z >> 31);
}

double orbit_mc(int n, int m, double eta, int draws, uint64_t seed, const std::vector<Pair>& pairs) {
  std::vector<Pair> active;
  for (auto pr : pairs)
    if (pr.k % n != 0) active.push_back(pr);
  double acc = 0.0;
  for (int draw = 0; draw < draws; ++draw) {
    std::vector<double> phases(active.size());
    for (double& phi : phases) phi = (splitmix(seed) >> 11) * (2.0 * kPi) / 9007199254740992.0;
    std::complex<double> total = 0;
    for (int q = 0; q < n; ++q)
      for (int p = 0; p < n; ++p) {
        std::vector<int> pos(m);
        int qq = q, pp = p;
        for (int j = 0; j < m; ++j) {
          pos[j] = qq;
          int nq = (3 * qq + 4 * pp) % n;
          int np = (2 * qq + 3 * pp) % n;
          qq = nq; pp = np;
        }
        double phase_sum = 0.0;
        for (size_t r = 0; r < active.size(); ++r) {
          double acc_c = 0.0;
          for (int x : pos)
            acc_c += std::cos(phases[r] + 2.0 * kPi * ((active[r].k % n) * x % n) / n);
          phase_sum += 2.0 * active[r].amp * acc_c;
        }
        total += std::exp(std::complex<double>(0.0, eta * phase_sum));
      }
    double norm = std::abs(total / static_cast<double>(n * n));
    acc += norm * norm;
  }
  return acc / draws;
}

}  // namespace

int main() {
  try {
    auto all = modes();
    require(all.size() == 32, "mode count");
    long long energy = 0, odd = 0;
    for (auto m : all) {
      energy += 1LL * m.re * m.re + 1LL * m.im * m.im;
      if (m.ell == 1) odd += 1LL * m.re * m.re + 1LL * m.im * m.im;
    }
    require(energy == 6603300, "energy");
    require(odd == 900, "odd energy");
    require(odd * 160000 == 9 * 16000000LL, "9/160000");
    require(2 * 2 - 4 * 2 == -4, "det");
    auto pairs = diagonal_pairs(all);
    const int primes[] = {5, 7, 11, 13, 17, 19, 31, 41, 47};
    const int expect_n[] = {5, 7, 11, 31, 41, 47};
    const int expect_m[] = {6, 3, 12, 15, 5, 23};
    const int expect_q[] = {90, 15, 396, 435, 45, 1035};
    const int expect_p[] = {66, 15, 276, 435, 45, 1035};
    for (int n : primes) {
      auto orb = order_and_rows(n);
      require(static_cast<int>(orb.rows.size()) == orb.m, "row count");
      long long quads = quadruples(orb.rows, n);
      long long perm = 2LL * orb.m * orb.m - orb.m;
      std::cout << "quad N=" << n << " m=" << orb.m << " quads=" << quads
                << " perm=" << perm << " excess=" << (quads - perm) << "\n";
      for (int i = 0; i < 6; ++i)
        if (expect_n[i] == n)
          require(orb.m == expect_m[i] && quads == expect_q[i] && perm == expect_p[i], "quad table");
      if (n == 7 || n == 31 || n == 41 || n == 47) require(quads == perm, "excess");
      if (n >= 11)
        for (auto pr : pairs) require(pr.k % n != 0, "sigma0");
    }
    auto check = [&](int n, double lam, double lo, double hi) {
      auto orb = order_and_rows(n);
      double sig = sigma_diag(n, pairs);
      double eta = std::sqrt(lam / (sig * orb.m));
      double avg = bessel_average(n, orb.m, eta, pairs);
      double ratio = avg / std::exp(-lam);
      std::cout << "bessel N=" << n << " m=" << orb.m << " lam=" << lam
                << " avg=" << avg << " ratio=" << ratio << "\n";
      require(ratio > lo && ratio < hi, "ratio window");
    };
    check(11, 1.0, 1.10, 10.0);
    check(31, 0.3, 0.99, 1.01);
    check(31, 1.0, 0.97, 1.03);
    check(47, 1.0, 0.97, 1.03);
    for (int n : {7, 11}) {
      auto orb = order_and_rows(n);
      double sig = sigma_diag(n, pairs);
      double eta = std::sqrt(0.3 / (sig * orb.m));
      double exact = bessel_average(n, orb.m, eta, pairs);
      double sample = orbit_mc(n, orb.m, eta, n == 7 ? 400 : 200, 1000u + n, pairs);
      std::cout << "orbit N=" << n << " eta=" << eta << " bessel=" << exact << " mc=" << sample << "\n";
      require(std::abs(exact - sample) < 0.02, "orbit monte carlo");
    }
    std::cout << "PASS\n";
  } catch (const std::exception& ex) {
    std::cerr << ex.what() << "\n";
    return 1;
  }
  return 0;
}
