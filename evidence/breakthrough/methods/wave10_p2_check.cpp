// Wave 10, task 1: direct finite check of the 2-primary component Lemma Y
// at level ell (v2). Model from wave9 vcheck_general.py:
//   Q = 2^(ell+3), N = 2^ell, c_0=1,c_1=3, e_0=0,e_1=1,
//   x_{n+1} = 6 x_n - x_{n-1} (mod Q).
//   Block(T,D)[s] = (T*c_s + D*e_s) mod Q, T in Z/Q, D in 8*Z/Q.
//   S_r = sum_{s<N, s%4==r} Block[s] mod Q.
// Check: blocks with equal sorted multiset have S in one D4 orbit
// (permutations r -> r+b and r -> -r+b on Z/4).
#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <vector>
#include <array>
using namespace std;
int main(int argc, char** argv) {
  int ell = argc > 1 ? atoi(argv[1]) : 7;
  int Q = 1 << (ell + 3);
  int N = 1 << ell;
  vector<int> c(N), e(N);
  c[0] = 1; e[0] = 0;
  if (N > 1) { c[1] = 3; e[1] = 1; }
  for (int i = 2; i < N; ++i) {
    c[i] = (6 * c[i-1] - c[i-2]) % Q; if (c[i] < 0) c[i] += Q;
    e[i] = (6 * e[i-1] - e[i-2]) % Q; if (e[i] < 0) e[i] += Q;
  }
  struct Rec {
    vector<uint16_t> ms; // sorted block
    array<uint16_t,4> S;
    int T, D;
  };
  vector<Rec> recs;
  recs.reserve((size_t)Q * (Q/8));
  vector<uint16_t> blk(N), srt(N);
  for (int T = 0; T < Q; ++T) {
    for (int D = 0; D < Q; D += 8) {
      for (int s = 0; s < N; ++s) blk[s] = (uint16_t)((T * c[s] + D * e[s]) % Q);
      srt = blk;
      sort(srt.begin(), srt.end());
      array<uint16_t,4> S = {0,0,0,0};
      for (int s = 0; s < N; ++s) S[s % 4] = (uint16_t)((S[s % 4] + blk[s]) % Q);
      recs.push_back({std::move(srt), S, T, D});
    }
  }
  printf("ell=%d Q=%d N=%d blocks=%zu\n", ell, Q, N, recs.size());
  sort(recs.begin(), recs.end(), [](const Rec& a, const Rec& b){ return a.ms < b.ms; });
  auto d4orbit = [](array<uint16_t,4> S) {
    vector<array<uint16_t,4>> orb;
    for (int b = 0; b < 4; ++b) {
      array<uint16_t,4> r1, r2;
      for (int i = 0; i < 4; ++i) { r1[i] = S[(i+b)%4]; r2[i] = S[(-i+b)%4 < 0 ? (-i+b)%4+4 : (-i+b)%4]; }
      orb.push_back(r1); orb.push_back(r2);
    }
    sort(orb.begin(), orb.end()); orb.erase(unique(orb.begin(), orb.end()), orb.end());
    return orb;
  };
  size_t groups = 0, bad = 0, maxgroup = 0;
  for (size_t i = 0; i < recs.size(); ) {
    size_t j = i;
    while (j < recs.size() && recs[j].ms == recs[i].ms) ++j;
    ++groups; maxgroup = max(maxgroup, j - i);
    auto orb = d4orbit(recs[i].S);
    for (size_t k = i; k < j; ++k) {
      if (!binary_search(orb.begin(), orb.end(), recs[k].S)) {
        ++bad;
        if (bad <= 5) {
          printf("BAD group %zu: T=%d D=%d S=(%d,%d,%d,%d) vs rep S=(%d,%d,%d,%d) groupsize=%zu\n",
                 groups, recs[k].T, recs[k].D,
                 recs[k].S[0], recs[k].S[1], recs[k].S[2], recs[k].S[3],
                 recs[i].S[0], recs[i].S[1], recs[i].S[2], recs[i].S[3], j-i);
          printf("  ms first 16:"); for (int t = 0; t < 16 && t < N; ++t) printf(" %d", recs[i].ms[t]); printf("\n");
        }
      }
    }
    i = j;
  }
  printf("groups=%zu bad_blocks=%zu maxgroup=%zu\n", groups, bad, maxgroup);
  printf(bad == 0 ? "PASS: component Lemma Y holds at ell=%d\n" : "FAIL: counterexample found at ell=%d\n", ell);
  return bad == 0 ? 0 : 1;
}
