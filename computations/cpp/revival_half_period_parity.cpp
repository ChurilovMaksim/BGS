// C++ twin of computations/verification/revival_half_period_parity.py (BGS-TRACE-135).

#include "revival_closure_common.hpp"

#include <cmath>
#include <iostream>
#include <iomanip>
#include <numeric>
#include <vector>

namespace {

constexpr uint64_t kSeed = 20261030ULL;
using namespace revival;

bool is_prime(int n) {
  if (n <= 1) return false;
  for (int p = 2; p * p <= n; ++p) {
    if (n % p == 0) return false;
  }
  return true;
}

void check_half_period() {
  int even = 0;
  for (int p = 3; p < 400; ++p) {
    if (!is_prime(p)) continue;
    const int t = order(p);
    if (t % 2 == 0) {
      ++even;
      const auto h = spow_mod(t / 2, p);
      require(h == std::make_tuple(p - 1, 0, 0, p - 1), "S^(t/2) = -I at p=" + std::to_string(p));
    }
  }
  std::cout << "S^(t/2) = -I at all " << even << " odd primes < 400 with even order  ok\n";
  const std::vector<std::pair<int, int>> expect = {{201, 200}, {401, 400}, {801, 800}, {203, 57}, {205, 124}, {1001, 274}};
  for (auto [n, h] : expect) {
    const int t = order(n);
    require(t % 2 == 0, "half return parity " + std::to_string(n));
    require(spow_mod(t / 2, n) == std::make_tuple(h, 0, 0, h), "half return at " + std::to_string(n));
  }
  std::cout << "composite half returns: {201: 200, 401: 400, 801: 800, 203: 57, 205: 124, 1001: 274}  ok\n";
}

void check_parity_reduction() {
  Pcg64 rng(kSeed);
  for (int n : {61, 101}) {
    const int t = order(n);
    const Mat mm = cat(n);
    Mat par(static_cast<size_t>(n * n), C(0, 0));
    for (int x = 0; x < n; ++x) par[static_cast<size_t>(x * n + ((n - x) % n))] = 1;
    const Mat half = matpow(mm, t / 2, n);
    const C c = half[0];
    require(std::abs(std::abs(c) - 1.0) < 1e-9, "M^(t/2)=cP at " + std::to_string(n));
    double md = 0.0;
    for (size_t i = 0; i < half.size(); ++i) md = std::max(md, std::abs(half[i] - c * par[i]));
    require(md < 1e-9, "M^(t/2)=cP at " + std::to_string(n));
    require(norm_max_diff(matmul(par, mm, n), matmul(mm, par, n)) < 1e-12, "[P,M]=0 at " + std::to_string(n));

    std::vector<double> phi(diag_modes().size());
    for (double& p : phi) p = rng.uniform(0, 2 * kPi);
    const auto d = diag_kick(n, phi, 0.6);
    const C trmt = trace(matpow(mm, t, n), n);
    const Mat U0 = scale_rows(mm, d, n);
    const C r = trace(matpow(U0, t, n), n) / trmt;

    Mat a(static_cast<size_t>(n * n), C(0, 0));
    for (int i = 0; i < n; ++i) a[static_cast<size_t>(i * n + i)] = 1;
    Mat mj = a;
    const Mat D = diag_matrix(d, n);
    for (int k = 0; k < t / 2; ++k) {
      const Mat mct = conj_transpose(mj, n);
      Mat step = matmul(mj, D, n);
      step = matmul(step, mct, n);
      a = matmul(a, step, n);
      mj = matmul(mm, mj, n);
    }
    const Mat apa = matmul(matmul(a, par, n), a, n);
    const Mat apap = matmul(apa, par, n);
    const C red2 = trace(apap, n) / static_cast<double>(n);
    require(std::abs(r - red2) < 1e-9, "parity reduction at " + std::to_string(n));
  }
  std::cout << "M^(t/2) = cP, [P,M] = 0 and R = N^-1 Tr(A P A P) at N=61, 101  ok\n";
}

void diagnostics() {
  double c4 = 0.0;
  for (const auto& m : diag_modes()) c4 += std::norm(m.c) * std::norm(m.c);
  const double sig = sigma_d();
  const double coef = c4 / (2.0 * sig * sig);
  std::cout << std::fixed << std::setprecision(7);
  std::cout << "derived constant sum|c|^4/(2 sigma_d^2) = " << coef << " (from the heuristic F2)\n";
  require(std::abs(coef - 0.1204622) < 1e-6, "constant");
  Pcg64 rng(kSeed + 1);
  std::cout << "diagnostic (open conjecture): N t lam | E|R|^2 +- se | F2 | classical orbit | e^-lam  free-parity limit  classical limit\n";
  for (int n : {61, 101}) {
    const int t = order(n);
    const int nh = t / 2;
    const Mat mm = cat(n);
    const C trmt = trace(matpow(mm, t, n), n);
    for (double lam : {1.0, 2.0, 3.0}) {
      const double eta = std::sqrt(lam / (sig * t));
      std::vector<double> r2, f2, cl;
      r2.reserve(1000);
      f2.reserve(1000);
      cl.reserve(1000);
      for (int draw = 0; draw < 1000; ++draw) {
        std::vector<double> phi(diag_modes().size());
        for (double& p : phi) p = rng.uniform(0, 2 * kPi);
        const auto d = diag_kick(n, phi, eta);
        const Mat U0 = scale_rows(mm, d, n);
        const C rval = trace(matpow(U0, t, n), n) / trmt;
        C mu(0, 0);
        for (const C& z : d) mu += z;
        mu /= static_cast<double>(n);
        std::vector<C> dp(static_cast<size_t>(n));
        for (int x = 0; x < n; ++x) dp[static_cast<size_t>(x)] = d[static_cast<size_t>((n - x) % n)];
        C mup(0, 0);
        for (const C& z : dp) mup += z;
        mup /= static_cast<double>(n);
        C dprod(0, 0);
        for (int x = 0; x < n; ++x) dprod += d[static_cast<size_t>(x)] * dp[static_cast<size_t>(x)];
        dprod /= static_cast<double>(n);
        const C f = std::pow(mu * mup, nh - 1) * (mu * mup + static_cast<double>(nh) * (dprod - mu * mup));
        std::vector<int> z0(static_cast<size_t>(n * n)), z1(static_cast<size_t>(n * n));
        for (int q = 0; q < n; ++q) {
          for (int p = 0; p < n; ++p) {
            const size_t idx = static_cast<size_t>(q * n + p);
            z0[idx] = q;
            z1[idx] = p;
          }
        }
        std::vector<C> pr(static_cast<size_t>(n * n), C(1, 0));
        for (int step = 0; step < t; ++step) {
          for (size_t idx = 0; idx < pr.size(); ++idx) pr[idx] *= d[static_cast<size_t>(z0[idx])];
          for (size_t idx = 0; idx < pr.size(); ++idx) {
            const int qq = z0[idx], pp = z1[idx];
            z0[idx] = static_cast<int>(mod_ll(3 * qq + 4 * pp, n));
            z1[idx] = static_cast<int>(mod_ll(2 * qq + 3 * pp, n));
          }
        }
        C pm(0, 0);
        for (const C& z : pr) pm += z;
        r2.push_back(std::norm(rval));
        f2.push_back(std::norm(f));
        cl.push_back(std::norm(pm / static_cast<double>(n * n)));
      }
      const double mean_r2 = std::accumulate(r2.begin(), r2.end(), 0.0) / r2.size();
      const double mean_f2 = std::accumulate(f2.begin(), f2.end(), 0.0) / f2.size();
      const double mean_cl = std::accumulate(cl.begin(), cl.end(), 0.0) / cl.size();
      double var = 0.0;
      for (double v : r2) var += (v - mean_r2) * (v - mean_r2);
      var /= static_cast<double>(r2.size());
      const double se = std::sqrt(var) / std::sqrt(static_cast<double>(r2.size()));
      double lim = std::exp(-lam) * (1.0 + coef * lam * lam);
      double clim = std::exp(-lam);
      for (const auto& m : diag_modes()) clim *= bessel_i0(2.0 * lam * std::norm(m.c) / sig);
      std::cout << std::fixed << std::setprecision(4);
      std::cout << "  " << n << " " << t << " " << lam << " | " << mean_r2 << " +- " << se << " | " << mean_f2 << " | "
                << mean_cl << " | " << std::exp(-lam) << " " << lim << " " << clim << "\n";
      require(std::abs(mean_r2 - mean_f2) < 4.0 * se, "diagnostic: F2 within 4 se");
      if (lam >= 2.0) require(mean_cl - mean_r2 > 5.0 * se, "diagnostic: classical orbit law above data by > 5 se");
    }
  }
}

}  // namespace

int main() {
  try {
    check_half_period();
    check_parity_reduction();
    diagnostics();
    std::cout << "PASS\n";
  } catch (const std::exception& ex) {
    std::cout << "FAIL: " << ex.what() << "\n";
    return 1;
  }
  return 0;
}
