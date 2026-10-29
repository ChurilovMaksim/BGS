// C++ twin of computations/verification/revival_closure_law.py (BGS-TRACE-133/134).

#include "revival_closure_common.hpp"

#include <boost/multiprecision/cpp_int.hpp>

#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <sstream>
#include <unordered_set>

namespace {

constexpr uint64_t kSeed = 20261029ULL;
using namespace revival;

std::vector<std::pair<int, int>> orbit_vectors(int n, int m) {
  std::vector<std::pair<int, int>> out;
  out.reserve(static_cast<size_t>(m));
  for (int j = 0; j < m; ++j) {
    auto s = spow(j);
    out.push_back({static_cast<int>(mod_ll(std::get<1>(s), n)), static_cast<int>(mod_ll(std::get<3>(s), n))});
  }
  return out;
}

using LambdaTuple = std::vector<int>;

std::vector<LambdaTuple> lambda_set(int n, int m) {
  const auto v = orbit_vectors(n, m);
  const auto p = v[static_cast<size_t>(m - 2)];
  const auto q = v[static_cast<size_t>(m - 1)];
  const long long det = mod_ll(static_cast<long long>(p.first) * q.second - static_cast<long long>(p.second) * q.first, n);
  const long long det_inv = mod_inv(det, n);
  std::vector<LambdaTuple> out;
  std::vector<int> head(static_cast<size_t>(std::max(0, m - 2)), 0);
  const auto go = [&](auto&& self, int depth) -> void {
    if (depth == m - 2) {
      long long r0 = 0, r1 = 0;
      for (int j = 0; j < m - 2; ++j) {
        r0 = mod_ll(r0 + static_cast<long long>(head[static_cast<size_t>(j)]) * v[static_cast<size_t>(j)].first, n);
        r1 = mod_ll(r1 + static_cast<long long>(head[static_cast<size_t>(j)]) * v[static_cast<size_t>(j)].second, n);
      }
      r0 = mod_ll(-r0, n);
      r1 = mod_ll(-r1, n);
      long long x = mod_ll(det_inv * (r0 * q.second - r1 * q.first), n);
      long long y = mod_ll(det_inv * (static_cast<long long>(p.first) * r1 - static_cast<long long>(p.second) * r0), n);
      LambdaTuple tup = head;
      tup.push_back(static_cast<int>(x));
      tup.push_back(static_cast<int>(y));
      out.push_back(std::move(tup));
      return;
    }
    for (int a = 0; a < n; ++a) {
      head[static_cast<size_t>(depth)] = a;
      self(self, depth + 1);
    }
  };
  if (m - 2 > 0) go(go, 0);
  else {
    LambdaTuple tup;
    long long r0 = 0, r1 = 0;
    long long x = mod_ll(det_inv * (r0 * q.second - r1 * q.first), n);
    long long y = mod_ll(det_inv * (static_cast<long long>(p.first) * r1 - static_cast<long long>(p.second) * r0), n);
    tup.push_back(static_cast<int>(x));
    tup.push_back(static_cast<int>(y));
    out.push_back(tup);
  }
  return out;
}

int beta(const LambdaTuple& a, int n) {
  std::vector<long long> y;
  y.reserve(a.size());
  for (size_t d = 0; d < a.size(); ++d) y.push_back(std::get<2>(spow(static_cast<int>(d))) / 2);
  long long s = 0;
  for (size_t i = 0; i < a.size(); ++i) {
    for (size_t j = i + 1; j < a.size(); ++j) {
      s += static_cast<long long>(a[i]) * a[j] * y[j - i];
    }
  }
  return static_cast<int>(mod_ll(-2 * s, n));
}

bool is_relation(const std::vector<int>& c) {
  long long a = 0, b = 0;
  long long pa = 1, pb = 0;
  for (int cj : c) {
    a += static_cast<long long>(cj) * pa;
    b += static_cast<long long>(cj) * pb;
    const long long npa = -pb;
    const long long npb = pa + 6 * pb;
    pa = npa;
    pb = npb;
  }
  return a == 0 && b == 0;
}

bool closes_mod(const std::vector<int>& c, int n) {
  long long a = 0, b = 0;
  long long pa = 1, pb = 0;
  for (int cj : c) {
    a += static_cast<long long>(cj) * pa;
    b += static_cast<long long>(cj) * pb;
    const long long npa = -pb;
    const long long npb = pa + 6 * pb;
    pa = npa;
    pb = npb;
  }
  return mod_ll(a, n) == 0 && mod_ll(b, n) == 0;
}

void check_conventions() {
  Pcg64 rng(kSeed);
  for (int n : {5, 7, 11}) {
    const Mat m = cat(n);
    const Mat mct = conj_transpose(m, n);
    for (int t = 0; t < 4; ++t) {
      const int a = static_cast<int>(rng.integers(0, n));
      const int b = static_cast<int>(rng.integers(0, n));
      const int sv0 = static_cast<int>(mod_ll(3 * a + 4 * b, n));
      const int sv1 = static_cast<int>(mod_ll(2 * a + 3 * b, n));
      Mat left = matmul(m, weyl(n, a, b), n);
      left = matmul(left, mct, n);
      const Mat right = weyl(n, sv0, sv1);
      require(norm_max_diff(left, right) < 1e-12, "Egorov N=" + std::to_string(n));
    }
  }
  std::cout << "conventions: Egorov M T(v) M^-1 = T(Sv) at N=5,7,11  ok\n";
}

void check_theorem_a() {
  Pcg64 rng(kSeed + 1);
  double worst = 0.0;
  const std::vector<std::pair<int, int>> cases = {{5, 3},  {7, 3},  {7, 4},  {9, 3},  {11, 3}, {11, 4},
                                                  {13, 3}, {15, 3}, {25, 3}, {41, 3}, {5, 5},  {41, 4}};
  for (auto [n, m] : cases) {
    const auto lam = lambda_set(n, m);
    std::unordered_set<std::string> seen;
    for (const auto& tup : lam) {
      std::ostringstream oss;
      for (int x : tup) oss << x << ',';
      seen.insert(oss.str());
    }
    size_t pow_nm2 = 1;
    for (int i = 0; i < m - 2; ++i) pow_nm2 *= static_cast<size_t>(n);
    require(lam.size() == pow_nm2 && seen.size() == lam.size(),
            "|Lambda| N=" + std::to_string(n) + " m=" + std::to_string(m));

    std::vector<C> d(static_cast<size_t>(n));
    for (int i = 0; i < n; ++i) d[static_cast<size_t>(i)] = std::polar(1.0, rng.uniform(0, 2 * kPi));
    auto dh = fft(d);
    for (auto& z : dh) z /= static_cast<double>(n);
    const Mat mm = cat(n);
    C lhs = trace_kicked_product(n, m, d, mm);

    C rhs(0, 0);
    for (const auto& a : lam) {
      C prod(1, 0);
      for (int x : a) prod *= dh[static_cast<size_t>(x)];
      rhs += static_cast<double>(n) * e_n(n, beta(a, n)) * prod;
    }
    const double rel = std::abs(lhs - rhs) / std::max(std::abs(lhs), 1e-300);
    worst = std::max(worst, rel);
    require(rel < 1e-10, "Theorem A N=" + std::to_string(n) + " m=" + std::to_string(m) + " rel=" + std::to_string(rel));

    std::vector<C> pr(static_cast<size_t>(n * n), C(1, 0));
    std::vector<int> z0(static_cast<size_t>(n * n)), z1(static_cast<size_t>(n * n));
    for (int q = 0; q < n; ++q) {
      for (int p = 0; p < n; ++p) {
        const size_t idx = static_cast<size_t>(q * n + p);
        z0[idx] = q;
        z1[idx] = p;
      }
    }
    for (int t = 0; t < m; ++t) {
      for (size_t idx = 0; idx < pr.size(); ++idx) pr[idx] *= d[static_cast<size_t>(z0[idx])];
      for (size_t idx = 0; idx < pr.size(); ++idx) {
        const int qq = z0[idx], pp = z1[idx];
        z0[idx] = static_cast<int>(mod_ll(3 * qq + 4 * pp, n));
        z1[idx] = static_cast<int>(mod_ll(2 * qq + 3 * pp, n));
      }
    }
    C sum_pr(0, 0);
    for (const C& z : pr) sum_pr += z;
    C cl(0, 0);
    for (const auto& a : lam) {
      C prod(1, 0);
      for (int x : a) prod *= dh[static_cast<size_t>(x)];
      cl += prod;
    }
    require(std::abs(sum_pr / static_cast<double>(n * n) - cl) < 1e-10,
            "classical counterpart N=" + std::to_string(n) + " m=" + std::to_string(m));
  }
  std::cout << std::scientific << std::setprecision(1);
  std::cout << "Theorem A: 12 (N,m) cases, |Lambda_m|=N^(m-2), max rel err " << worst << "  ok\n";
  std::cout << std::defaultfloat;

  for (int n : {7, 41, 35, 239}) {
    const int t = order(n);
    const Mat mm = cat(n);
    const C trmt = trace(matpow(mm, t, n), n);
    require(std::abs(std::abs(trmt) - static_cast<double>(n)) < 1e-8, "|Tr M^t|=N at " + std::to_string(n));
    std::vector<double> phi(diag_modes().size());
    for (double& p : phi) p = rng.uniform(0, 2 * kPi);
    const auto d = diag_kick(n, phi, 0.7);
    const Mat U0 = scale_rows(mm, d, n);
    const C u_tr = trace(matpow(U0, t, n), n);
    const C prod_tr = trace_kicked_product(n, t, d, mm);
    require(std::abs(u_tr - trmt / static_cast<double>(n) * prod_tr) < 1e-8 * n,
            "scalar return " + std::to_string(n));
  }
  std::cout << "scalar return: |Tr M^t| = N and Tr U^t = (Tr M^t/N) Tr(prod D_j) at N=7,41,35,239  ok\n";
}

void check_phase_average() {
  const auto& modes = diag_modes();
  const DiagMode pick[2] = {modes[4], modes[0]};
  const std::pair<int, C> mode_pair[2] = {{pick[0].k, pick[0].c}, {pick[1].k, pick[1].c}};
  for (auto [n, m, eta] : std::vector<std::tuple<int, int, double>>{{7, 2, 1.3}, {7, 3, 1.3}, {11, 2, 2.0}}) {
    const Mat mm = cat(n);
    std::vector<std::vector<int>> xs;
    std::vector<int> cur(static_cast<size_t>(m), 0);
    const auto gen = [&](auto&& self, int d) -> void {
      if (d == m) {
        xs.push_back(cur);
        return;
      }
      for (int v = 0; v < n; ++v) {
        cur[static_cast<size_t>(d)] = v;
        self(self, d + 1);
      }
    };
    gen(gen, 0);
    std::vector<C> kern(xs.size(), C(0, 0));
    for (size_t i = 0; i < xs.size(); ++i) {
      C p(1, 0);
      for (int j = 0; j < m; ++j) {
        p *= mm[static_cast<size_t>(xs[i][static_cast<size_t>(j)] * n + xs[i][static_cast<size_t>((j + 1) % m)])];
      }
      kern[i] = p;
    }
    std::vector<std::vector<C>> vr(2);
    for (int mi = 0; mi < 2; ++mi) {
      vr[static_cast<size_t>(mi)].resize(xs.size());
      for (size_t i = 0; i < xs.size(); ++i) {
        C acc(0, 0);
        for (const auto& x : xs[i]) acc += e_n(n, static_cast<long long>(mode_pair[mi].first) * x);
        vr[static_cast<size_t>(mi)][i] = acc;
      }
    }
    C tot(0, 0);
    for (size_t i = 0; i < xs.size(); ++i) {
      std::vector<double> w(xs.size(), 1.0);
      for (int mi = 0; mi < 2; ++mi) {
        const double wc = 2.0 * eta * std::abs(mode_pair[mi].second);
        for (size_t j = 0; j < xs.size(); ++j) {
          w[j] *= bessel_j0(wc * std::abs(vr[static_cast<size_t>(mi)][i] - vr[static_cast<size_t>(mi)][j]));
        }
      }
      C inner(0, 0);
      for (size_t j = 0; j < xs.size(); ++j) inner += std::conj(kern[j]) * w[j];
      tot += kern[i] * inner;
    }
    const int g = 64;
    double quad = 0.0;
    for (int i1 = 0; i1 < g; ++i1) {
      const double p1 = 2.0 * kPi * i1 / g;
      for (int i2 = 0; i2 < g; ++i2) {
        const double p2 = 2.0 * kPi * i2 / g;
        std::vector<double> f(static_cast<size_t>(n), 0.0);
        const double ph[2] = {p1, p2};
        for (int mi = 0; mi < 2; ++mi) {
          for (int x = 0; x < n; ++x) {
            f[static_cast<size_t>(x)] +=
                2.0 * std::real(mode_pair[mi].second * std::polar(1.0, ph[mi]) * e_n(n, static_cast<long long>(mode_pair[mi].first) * x));
          }
        }
        std::vector<C> dd(static_cast<size_t>(n));
        for (int x = 0; x < n; ++x) dd[static_cast<size_t>(x)] = std::polar(1.0, eta * f[static_cast<size_t>(x)]);
        const Mat U0 = scale_rows(mm, dd, n);
        const C trm = trace(matpow(U0, m, n), n);
        quad += std::norm(trm);
      }
    }
    quad /= static_cast<double>(g * g);
    require(std::abs(tot.real() - quad) < 1e-9 * std::max(1.0, quad), "J0 identity N=" + std::to_string(n) + " m=" + std::to_string(m));
  }
  std::cout << "phase average: J0 path sum = trapezoid quadrature (N=7 m=2,3; N=11 m=2)  ok\n";
}

void check_norm_lemma() {
  struct Row {
    int n, length, amax, nz;
  };
  std::vector<Row> rows;
  for (auto [n, length, amax] : std::vector<std::tuple<int, int, int>>{{41, 3, 5}, {239, 4, 6}, {239, 5, 5}, {1189, 5, 8}}) {
    require(static_cast<double>(amax * amax) * std::pow(kLam, length) <= 4.0 * n * n, "window hypothesis " + std::to_string(n));
    int nz = 0;
    std::vector<int> c(static_cast<size_t>(length), 0);
    const auto go = [&](auto&& self, int d) -> void {
      if (d == length) {
        if (std::any_of(c.begin(), c.end(), [](int v) { return v != 0; }) && closes_mod(c, n)) {
          ++nz;
          require(is_relation(c), "Lemma 1 violated at N=" + std::to_string(n));
        }
        return;
      }
      for (int v = -amax; v <= amax; ++v) {
        c[static_cast<size_t>(d)] = v;
        self(self, d + 1);
      }
    };
    go(go, 0);
    rows.push_back({n, length, amax, nz});
  }
  require(!is_relation({-7, 1, -7}) && closes_mod({-7, 1, -7}, 41), "near-sharpness witness");
  std::cout << "Lemma 1 exhaustive (N,L,A,closures): [";
  for (size_t i = 0; i < rows.size(); ++i) {
    if (i) std::cout << ", ";
    std::cout << "(" << rows[i].n << ", " << rows[i].length << ", " << rows[i].amax << ", " << rows[i].nz << ")";
  }
  std::cout << "]  ok; witness (-7,1,-7) at N=41 outside the window\n";
}

void check_dichotomy(int n, int amax, int expect_case1) {
  const int t = order(n);
  const auto v = orbit_vectors(n, t);
  const double gthr = t - std::log(4.0 * n * n / static_cast<double>(amax * amax)) / std::log(kLam);
  const int ga = amax > 2 ? static_cast<int>(std::floor(2.0 * std::log(amax / 2.0) / std::log(kLam))) : 0;
  const auto p = v[static_cast<size_t>(t - 2)];
  const auto q = v[static_cast<size_t>(t - 1)];
  const long long det = mod_ll(static_cast<long long>(p.first) * q.second - static_cast<long long>(p.second) * q.first, n);
  const long long det_inv = mod_inv(det, n);
  int case1 = 0, total = 0;
  std::vector<int> head(static_cast<size_t>(std::max(0, t - 2)), 0);
  const auto go = [&](auto&& self, int depth) -> void {
    if (depth == t - 2) {
      long long r0 = 0, r1 = 0;
      for (int j = 0; j < t - 2; ++j) {
        r0 = mod_ll(r0 + static_cast<long long>(head[static_cast<size_t>(j)]) * v[static_cast<size_t>(j)].first, n);
        r1 = mod_ll(r1 + static_cast<long long>(head[static_cast<size_t>(j)]) * v[static_cast<size_t>(j)].second, n);
      }
      r0 = mod_ll(-r0, n);
      r1 = mod_ll(-r1, n);
      long long x = mod_ll(det_inv * (r0 * q.second - r1 * q.first), n);
      long long y = mod_ll(det_inv * (static_cast<long long>(p.first) * r1 - static_cast<long long>(p.second) * r0), n);
      int xi = static_cast<int>(x);
      int yi = static_cast<int>(y);
      if (xi > n / 2) xi -= n;
      if (yi > n / 2) yi -= n;
      if (std::abs(xi) > amax || std::abs(yi) > amax) return;
      std::vector<int> a = head;
      a.push_back(xi);
      a.push_back(yi);
      if (!std::any_of(a.begin(), a.end(), [](int z) { return z != 0; })) return;
      ++total;
      std::vector<int> nzi;
      for (int j = 0; j < t; ++j) {
        if (a[static_cast<size_t>(j)]) nzi.push_back(j);
      }
      std::vector<int> gaps(nzi.size());
      for (size_t i = 0; i < nzi.size(); ++i) {
        gaps[i] = nzi.size() > 1 ? (nzi[(i + 1) % nzi.size()] - nzi[i] - 1 + t) % t : t - 1;
      }
      size_t gi = 0;
      for (size_t i = 1; i < gaps.size(); ++i) {
        if (gaps[i] > gaps[gi]) gi = i;
      }
      if (static_cast<double>(gaps[gi]) < gthr) return;
      ++case1;
      const int start = nzi[(gi + 1) % nzi.size()];
      std::vector<int> rot(static_cast<size_t>(t));
      for (int j = 0; j < t; ++j) rot[static_cast<size_t>(j)] = a[static_cast<size_t>((start + j) % t)];
      require(is_relation(rot), "Case 1 not a relation");
      std::vector<int> nzr;
      for (int j = 0; j < t; ++j) {
        if (rot[static_cast<size_t>(j)]) nzr.push_back(j);
      }
      std::vector<std::vector<int>> blocks;
      blocks.push_back({nzr[0]});
      for (size_t j = 1; j < nzr.size(); ++j) {
        if (nzr[j] - blocks.back().back() - 1 <= ga) {
          blocks.back().push_back(nzr[j]);
        } else {
          blocks.push_back({nzr[j]});
        }
      }
      for (const auto& b : blocks) {
        std::vector<int> seg(static_cast<size_t>(b.back() + 1), 0);
        for (int j : b) seg[static_cast<size_t>(j)] = rot[static_cast<size_t>(j)];
        require(static_cast<int>(b.size()) >= 3 && is_relation(seg), "run lemma");
      }
      return;
    }
    for (int val = -amax; val <= amax; ++val) {
      head[static_cast<size_t>(depth)] = val;
      self(self, depth + 1);
    }
  };
  if (t - 2 > 0) go(go, 0);
  require(case1 == expect_case1, "Case-1 count N=" + std::to_string(n) + " A=" + std::to_string(amax) + ": " + std::to_string(case1));
  std::cout << "dichotomy N=" << n << " t=" << t << " A=" << amax << ": elements=" << total << " case1=" << case1
            << " (runs checked) case2=" << (total - case1) << "  ok\n";
}

boost::multiprecision::cpp_int family_member_cpp(int t, int kappa) {
  using boost::multiprecision::cpp_int;
  auto spow_a = [](int d) {
    cpp_int a = 1, b = 0, c = 0, e = 1;
    for (int i = 0; i < d; ++i) {
      const cpp_int na = 3 * a + 2 * b;
      const cpp_int nb = 4 * a + 3 * b;
      const cpp_int nc = 3 * c + 2 * e;
      const cpp_int ne = 4 * c + 3 * e;
      a = na;
      b = nb;
      c = nc;
      e = ne;
    }
    return a;
  };
  auto isqrt = [](cpp_int n) {
    cpp_int x = n;
    cpp_int y = (x + 1) / 2;
    while (y < x) {
      x = y;
      y = (x + n / x) / 2;
    }
    return x;
  };
  const cpp_int x = spow_a(t);
  const cpp_int num = 2 * x - 2;
  require(num % kappa == 0, "family t=" + std::to_string(t));
  const cpp_int n2 = num / kappa;
  const cpp_int n = isqrt(n2);
  require(n * n == n2, "family t=" + std::to_string(t));
  return n;
}

int family_member(int t, int kappa) {
  const boost::multiprecision::cpp_int n = family_member_cpp(t, kappa);
  require(n <= std::numeric_limits<int>::max(), "family t=" + std::to_string(t));
  return static_cast<int>(n);
}

double log10_cpp_int(const boost::multiprecision::cpp_int& n) {
  const std::string s = n.convert_to<std::string>();
  if (s.empty()) return 0.0;
  if (static_cast<int>(s.size()) == 1) return std::log10(std::stod(s));
  const double lead = std::stod(s.substr(0, 4));
  return std::log10(lead) + static_cast<double>(s.size() - 4);
}

double explicit_bound(double log_n, int a_limit, int t, double eta) {
  const auto& modes = diag_modes();
  std::vector<double> w_r;
  for (const auto& m : modes) w_r.push_back(2.0 * eta * std::abs(m.c));
  double big_w = 0.0;
  for (double w : w_r) big_w += w;
  double jprod = 1.0;
  for (double w : w_r) jprod *= bessel_j0(w);
  const double rho = std::expm1(big_w);
  double best = std::numeric_limits<double>::infinity();
  std::vector<double> tail(6002, 0.0);
  std::vector<double> terms(6001);
  for (int d = 0; d <= 6000; ++d) terms[static_cast<size_t>(d)] = std::exp(d * std::log(big_w) - std::lgamma(d + 1));
  for (int d = 6000; d >= 0; --d) tail[static_cast<size_t>(d)] = tail[static_cast<size_t>(d + 1)] + terms[static_cast<size_t>(d)];
  const int kmax = k_max();
  int a = 2;
  while (a <= a_limit) {
    const double tau = tail[static_cast<size_t>(std::min(a / kmax + 1, 6000))];
    const double e_t = t * tau * std::exp(big_w * (t - 1));
    const double thr = t - (std::log(4.0) + 2.0 * log_n - 2.0 * std::log(a)) / std::log(kLam);
    const int gstar = std::max(static_cast<int>(std::ceil(thr)) - 1, 0);
    const int s0 = std::max(static_cast<int>(std::ceil(static_cast<double>(t) / (gstar + 1))), 1);
    double e_d = 0.0;
    for (int s = s0; s <= t; ++s) {
      e_d += std::exp(std::lgamma(t + 1) - std::lgamma(s + 1) - std::lgamma(t - s + 1) + s * std::log(rho));
    }
    const int ga = a > 2 ? static_cast<int>(std::floor(2.0 * std::log(a / 2.0) / std::log(kLam))) : 0;
    const double q = (ga + 1) * rho;
    const double e_r = q >= 1.0 ? std::numeric_limits<double>::infinity()
                                : std::expm1(t * std::log1p(std::pow(ga + 1, 2) * std::pow(rho, 3) / (1.0 - q)));
    best = std::min(best, e_t + e_d + e_r);
    a = a < 64 ? a + 1 : static_cast<int>(a * 1.1);
  }
  require(jprod > 0, "J positive");
  return best;
}

void check_theorem_c() {
  const double sig = sigma_d();
  require(std::abs(sig - 13203.0 / 32000.0) < 1e-15, "sigma_d");
  const std::vector<int> fam4 = {family_member(3, 4), family_member(5, 4), family_member(7, 4), family_member(9, 4),
                                 family_member(11, 4), family_member(13, 4), family_member(15, 4)};
  const std::vector<int> fam32 = {family_member(6, 32), family_member(10, 32), family_member(14, 32)};
  const std::vector<int> want4 = {7, 41, 239, 1393, 8119, 47321, 275807};
  const std::vector<int> want32 = {35, 1189, 40391};
  require(fam4 == want4 && fam32 == want32, "families");
  const std::vector<int> ns = {fam4[0], fam4[1], fam4[2], fam4[3], fam4[4], fam32[0], fam32[1]};
  const std::vector<int> ts = {3, 5, 7, 9, 11, 6, 10};
  for (size_t i = 0; i < ns.size(); ++i) require(order(ns[i]) == ts[i], "order " + std::to_string(ns[i]));
  std::cout << "families (kappa=4): [";
  for (size_t i = 0; i < fam4.size(); ++i) std::cout << (i ? ", " : "") << fam4[i];
  std::cout << "]  (kappa=32): [";
  for (size_t i = 0; i < fam32.size(); ++i) std::cout << (i ? ", " : "") << fam32[i];
  std::cout << "]  orders ok; sigma_d = 13203/32000\n";
  const double b41 = explicit_bound(std::log(41.0), std::min(41 / 2 - 1, 9 * 5000), 5,
                                    std::sqrt(0.25 / (sig * 5)));
  const boost::multiprecision::cpp_int n501 = family_member_cpp(501, 4);
  const double log_n501 = log10_cpp_int(n501) * std::log(10.0);
  const double b501 = explicit_bound(log_n501, 9 * 5000, 501, std::sqrt(0.25 / (sig * 501)));
  std::cout << std::setprecision(3) << std::fixed;
  std::cout << "explicit bound lam=1/4: N=41 -> " << b41 << " (no information); t=501, log10 N="
            << static_cast<int>(std::lround(log10_cpp_int(n501))) << " -> " << b501 << "\n";
  require(b41 > 1 && b501 < 1, "bound regime");
  Pcg64 rng(kSeed + 2);
  double prev = std::numeric_limits<double>::infinity();
  for (int n : {41, 239}) {
    const int t = order(n);
    const double eta = std::sqrt(1.0 / (sig * t));
    const Mat mm = cat(n);
    const C trmt = trace(matpow(mm, t, n), n);
    double dev = 0.0;
    for (int draw = 0; draw < 100; ++draw) {
      std::vector<double> phi(diag_modes().size());
      for (double& p : phi) p = rng.uniform(0, 2 * kPi);
      const auto d = diag_kick(n, phi, eta);
      const Mat U0 = scale_rows(mm, d, n);
      const C r = trace(matpow(U0, t, n), n) / trmt;
      C mean(0, 0);
      for (const C& z : d) mean += z;
      mean /= static_cast<double>(n);
      dev = std::max(dev, std::abs(r - std::pow(mean, t)));
    }
    std::cout << std::scientific << std::setprecision(3);
    std::cout << "diagnostic N=" << n << " t=" << t << " lam=1: max_phi |R - dhat0^t| = " << dev << " (100 draws)\n";
    require(dev < prev, "deviation should decrease along the family (diagnostic)");
    prev = dev;
  }
}

}  // namespace

int main() {
  try {
    check_conventions();
    check_theorem_a();
    check_phase_average();
    check_norm_lemma();
    check_dichotomy(239, 5, 28);
    check_dichotomy(1393, 5, 108);
    check_theorem_c();
    std::cout << "PASS\n";
  } catch (const std::exception& ex) {
    std::cout << "FAIL: " << ex.what() << "\n";
    return 1;
  }
  return 0;
}
