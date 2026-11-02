// Wave 44, task 5: slice PC at m=24.
//
// Slice: ker_289 x ker_1153^2, all other components zero.
//   D_24 = 2^9 * 3^4 * 5^2 * 7^2 * 11^2 * 17^2 * 1153^2.
//   Constraining odd primes: 17, 1153 (Tr(a^6) = 39202 = 2*17*1153,
//   so a^12 = -1 mod pR for p in {17,1153}).
//   Kernel mod p^2 = { p*Tr(C a^i) mod p^2 : C in R/p }  (p split, e=1,
//   so |ker| = p^2; verified by brute force at 289, by distinctness +
//   counting at 1153^2).
// Points are (C,D) with C in R/17, D in R/1153:
//   t_i = Tr(C a^i) mod 17, s_i = Tr(D a^i) mod 1153, i<24,
//   antiperiodic: t_{i+12} = -t_i, s_{i+12} = -s_i.
// Fiber key = multiset of the 24 pairs (t_i, s_i)  (== global multiset
//   of the slice point, by CRT + injectivity of x -> p*x mod p^2).
// Class profile at a component: 4 sorted 6-multisets of values at
//   positions i = r mod 4 (values are negation-symmetric triples).
// PC on the slice: every fiber pair has a common pi in D_4, where
//   pi in Pi  iff  prof'[r] == prof[pi(r)] for all r, at both
//   constraining components.
// Algorithm: fiber pairs must share marginal multisets, so process
//   cells (t-marginal group x s-marginal group) independently; inside
//   a cell group by a 128-bit pair-multiset hash, then split hash
//   groups by exact sorted-pair keys. Base-vs-other checks suffice
//   by transitivity of the common-pi relation.

#include <algorithm>
#include <array>
#include <atomic>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <mutex>
#include <string>
#include <thread>
#include <unordered_map>
#include <utility>
#include <vector>

using std::array;
using std::vector;

static const int M = 24, H = 12;
static const int P1 = 17, P2 = 1153, Q2 = 1153 * 1153;

// splitmix64
static uint64_t sm_state = 0x9e3779b97f4a7c15ULL;
static uint64_t rnd64() {
  uint64_t z = (sm_state += 0x9e3779b97f4a7c15ULL);
  z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL;
  z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL;
  return z ^ (z >> 31);
}

int main() {
  // ---- alpha powers mod p (i < 12) ----
  auto alpha_pow = [](int p) {
    vector<int> X(H), Y(H);
    X[0] = 1 % p; Y[0] = 0;
    if (H > 1) { X[1] = 3 % p; Y[1] = 2 % p; }
    for (int i = 2; i < H; i++) {
      int x0 = X[i - 1], y0 = Y[i - 1];
      X[i] = (3 * x0 + 4 * y0) % p;
      Y[i] = (2 * x0 + 3 * y0) % p;
    }
    return std::make_pair(X, Y);
  };
  auto [X1, Y1] = alpha_pow(P1);
  auto [X2, Y2] = alpha_pow(P2);
  // sanity: a^12 = -1 mod pR
  {
    auto ap = [](int p, int n) {
      int x = 1 % p, y = 0;
      for (int i = 0; i < n; i++) {
        int nx = (3 * x + 4 * y) % p, ny = (2 * x + 3 * y) % p;
        x = nx; y = ny;
      }
      return std::make_pair(x, y);
    };
    auto a12 = ap(P1, 12), b12 = ap(P2, 12);
    if (a12 != std::make_pair(P1 - 1, 0) || b12 != std::make_pair(P2 - 1, 0)) {
      printf("FATAL: a^12 != -1\n"); return 1;
    }
  }

  // ---- t-sequences for C in R/17 (289 x 12) ----
  const int NC = P1 * P1;
  vector<array<uint16_t, H>> tseq(NC);
  for (int a = 0; a < P1; a++)
    for (int b = 0; b < P1; b++) {
      int c = a * P1 + b;
      for (int i = 0; i < H; i++)
        tseq[c][i] = (uint16_t)((2 * (a * X1[i] + 2 * b * Y1[i])) % P1);
    }
  // ---- s-sequences for D in R/1153 (1153^2 x 12) ----
  const int ND = P2 * P2;
  vector<array<uint16_t, H>> sseq(ND);
  for (int x = 0; x < P2; x++) {
    for (int y = 0; y < P2; y++) {
      int d = x * P2 + y;
      for (int i = 0; i < H; i++)
        sseq[d][i] = (uint16_t)((2 * (x * X2[i] + 2 * y * Y2[i])) % P2);
    }
  }
  printf("seqs built: NC=%d ND=%d\n", NC, ND); fflush(stdout);

  // ---- marginal multisets (sorted 24 values) + class profiles ----
  // marginal: sorted concat(seq, -seq mod p). profile: 4 x sorted 6.
  auto build_marg_prof = [](const vector<array<uint16_t, H>> &seq, int p,
                            vector<array<uint16_t, M>> &marg,
                            vector<array<uint16_t, M>> &prof) {
    int n = (int)seq.size();
    marg.resize(n); prof.resize(n);
    for (int k = 0; k < n; k++) {
      uint16_t v[M];
      for (int i = 0; i < H; i++) { v[i] = seq[k][i]; v[H + i] = (p - seq[k][i]) % p; }
      std::sort(v, v + M);
      for (int i = 0; i < M; i++) marg[k][i] = v[i];
      // class r: indices r, r+4, r+8 and negations
      for (int r = 0; r < 4; r++) {
        uint16_t c[6] = {seq[k][r], seq[k][r + 4], seq[k][r + 8],
                         (uint16_t)((p - seq[k][r]) % p),
                         (uint16_t)((p - seq[k][r + 4]) % p),
                         (uint16_t)((p - seq[k][r + 8]) % p)};
        std::sort(c, c + 6);
        for (int j = 0; j < 6; j++) prof[k][r * 6 + j] = c[j];
      }
    }
  };
  vector<array<uint16_t, M>> tmarg, tprof, smarg, sprof;
  build_marg_prof(tseq, P1, tmarg, tprof);
  printf("t marginals/profiles done\n"); fflush(stdout);
  build_marg_prof(sseq, P2, smarg, sprof);
  printf("s marginals/profiles done\n"); fflush(stdout);

  // ---- group by marginal multiset (hash + exact verify) ----
  auto group_by_marg = [](const vector<array<uint16_t, M>> &marg) {
    int n = (int)marg.size();
    vector<uint64_t> h(n);
    for (int k = 0; k < n; k++) {
      uint64_t x = 1469598103934665603ULL;
      for (int i = 0; i < M; i++) { x ^= marg[k][i]; x *= 1099511628211ULL; }
      h[k] = x;
    }
    vector<int> idx(n);
    for (int k = 0; k < n; k++) idx[k] = k;
    std::sort(idx.begin(), idx.end(), [&](int a, int b) { return h[a] < h[b]; });
    vector<vector<int>> groups;
    for (int i = 0; i < n;) {
      int j = i;
      // exact split within hash run
      while (j < n && h[idx[j]] == h[idx[i]]) j++;
      // split [i,j) by exact marginal equality
      std::sort(idx.begin() + i, idx.begin() + j, [&](int a, int b) {
        return std::memcmp(marg[a].data(), marg[b].data(), sizeof(uint16_t) * M) < 0;
      });
      int k = i;
      while (k < j) {
        int l = k + 1;
        while (l < j && std::memcmp(marg[idx[k]].data(), marg[idx[l]].data(),
                                    sizeof(uint16_t) * M) == 0) l++;
        groups.push_back(vector<int>(idx.begin() + k, idx.begin() + l));
        k = l;
      }
      i = j;
    }
    return groups;
  };
  vector<vector<int>> tgroups = group_by_marg(tmarg);
  printf("t-marginal groups: %zu\n", tgroups.size()); fflush(stdout);
  vector<vector<int>> sgroups = group_by_marg(smarg);
  printf("s-marginal groups: %zu\n", sgroups.size()); fflush(stdout);
  size_t maxsg = 0; for (auto &g : sgroups) maxsg = std::max(maxsg, g.size());
  size_t maxtg = 0; for (auto &g : tgroups) maxtg = std::max(maxtg, g.size());
  printf("max t-group %zu, max s-group %zu\n", maxtg, maxsg); fflush(stdout);

  // ---- random pair-hash tables (17 x 1153) ----
  const int NP = P1 * P2;
  vector<uint64_t> R1(NP), R2(NP);
  for (int i = 0; i < NP; i++) { R1[i] = rnd64(); R2[i] = rnd64(); }

  // ---- D_4 permutations of classes {0,1,2,3}: pi(r) ----
  // rotations r -> r+b; reflections r -> -r+b
  int pi_map[8][4];
  for (int b = 0; b < 4; b++) {
    for (int r = 0; r < 4; r++) pi_map[b][r] = (r + b) % 4;
    for (int r = 0; r < 4; r++) pi_map[4 + b][r] = (4 + b - r) % 4;
  }

  // ---- cells ----
  struct Cell { int tg, sg; };
  vector<Cell> cells;
  for (int i = 0; i < (int)tgroups.size(); i++)
    for (int j = 0; j < (int)sgroups.size(); j++) cells.push_back({i, j});
  printf("cells: %zu\n", cells.size()); fflush(stdout);

  struct Stats {
    uint64_t points = 0, fibers = 0, multifibers = 0, pairs = 0, failures = 0;
  };
  std::atomic<size_t> next_cell{0};
  std::mutex fail_mu;
  vector<std::string> fail_witnesses;
  vector<Stats> tstats(4);

  auto worker = [&](int tid) {
    Stats st;
    vector<std::tuple<uint64_t, uint64_t, int, int>> items;
    vector<array<int, M>> keys;
    vector<int> order;
    while (true) {
      size_t ci = next_cell.fetch_add(1);
      if (ci >= cells.size()) break;
      const vector<int> &tg = tgroups[cells[ci].tg];
      const vector<int> &sg = sgroups[cells[ci].sg];
      items.clear();
      items.reserve(tg.size() * sg.size());
      for (int c : tg) {
        for (int d : sg) {
          uint64_t h1 = 0, h2 = 0;
          for (int i = 0; i < H; i++) {
            int t = tseq[c][i], s = sseq[d][i];
            int tn = (P1 - t) % P1, sn = (P2 - s) % P2;
            h1 += R1[t * P2 + s] + R1[tn * P2 + sn];
            h2 += R2[t * P2 + s] + R2[tn * P2 + sn];
          }
          items.emplace_back(h1, h2, c, d);
        }
      }
      st.points += items.size();
      std::sort(items.begin(), items.end(), [](const auto &a, const auto &b) {
        if (std::get<0>(a) != std::get<0>(b)) return std::get<0>(a) < std::get<0>(b);
        return std::get<1>(a) < std::get<1>(b);
      });
      size_t i = 0;
      while (i < items.size()) {
        size_t j = i + 1;
        while (j < items.size() && std::get<0>(items[j]) == std::get<0>(items[i]) &&
               std::get<1>(items[j]) == std::get<1>(items[i])) j++;
        // exact split of hash group [i,j) by sorted 24-pair key
        keys.assign(j - i, {});
        for (size_t k = i; k < j; k++) {
          int c = std::get<2>(items[k]), d = std::get<3>(items[k]);
          array<int, M> &ky = keys[k - i];
          for (int q = 0; q < H; q++) {
            ky[q] = tseq[c][q] * P2 + sseq[d][q];
            ky[H + q] = ((P1 - tseq[c][q]) % P1) * P2 + ((P2 - sseq[d][q]) % P2);
          }
          std::sort(ky.begin(), ky.end());
        }
        order.resize(j - i);
        for (size_t k = 0; k < j - i; k++) order[k] = (int)k;
        std::sort(order.begin(), order.end(), [&](int a, int b) {
          return keys[a] < keys[b];
        });
        size_t a = 0;
        while (a < order.size()) {
          size_t b = a + 1;
          while (b < order.size() && keys[order[b]] == keys[order[a]]) b++;
          st.fibers++;
          if (b - a >= 2) {
            st.multifibers++;
            int bc = std::get<2>(items[i + order[a]]);
            int bd = std::get<3>(items[i + order[a]]);
            for (size_t k = a + 1; k < b; k++) {
              int oc = std::get<2>(items[i + order[k]]);
              int od = std::get<3>(items[i + order[k]]);
              st.pairs++;
              bool ok = false;
              for (int pi = 0; pi < 8 && !ok; pi++) {
                bool good = true;
                for (int r = 0; r < 4 && good; r++) {
                  int pr = pi_map[pi][r];
                  for (int v = 0; v < 6; v++) {
                    if (tprof[oc][r * 6 + v] != tprof[bc][pr * 6 + v] ||
                        sprof[od][r * 6 + v] != sprof[bd][pr * 6 + v]) { good = false; break; }
                  }
                }
                if (good) ok = true;
              }
              if (!ok) {
                st.failures++;
                std::lock_guard<std::mutex> lk(fail_mu);
                if (fail_witnesses.size() < 5) {
                  char buf[256];
                  snprintf(buf, sizeof(buf),
                           "FAIL cell(tg=%d,sg=%d) base(C=%d,D=%d) other(C=%d,D=%d)",
                           cells[ci].tg, cells[ci].sg, bc, bd, oc, od);
                  fail_witnesses.push_back(buf);
                }
              }
            }
          }
          a = b;
        }
        i = j;
      }
    }
    tstats[tid] = st;
  };

  int nthreads = 4;
  vector<std::thread> th;
  for (int t = 0; t < nthreads; t++) th.emplace_back(worker, t);
  for (auto &t : th) t.join();

  Stats tot;
  for (auto &s : tstats) {
    tot.points += s.points; tot.fibers += s.fibers;
    tot.multifibers += s.multifibers; tot.pairs += s.pairs;
    tot.failures += s.failures;
  }
  printf("POINTS %llu (expect 384199201)\n", (unsigned long long)tot.points);
  printf("FIBERS %llu  MULTIFIBERS %llu  PAIRS %llu  FAILURES %llu\n",
         (unsigned long long)tot.fibers, (unsigned long long)tot.multifibers,
         (unsigned long long)tot.pairs, (unsigned long long)tot.failures);
  for (auto &w : fail_witnesses) printf("%s\n", w.c_str());
  printf("DONE\n");
  return tot.failures == 0 ? 0 : 2;
}
