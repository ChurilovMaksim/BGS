// Wave 17, task 2: exact PC check for (m,3,17) with 8|m.
// Enumerates ALL recurrence sequences mod 3 and mod 17, ALL (d1,d2) in D_m x D_m,
// tests pair-multiset preservation (*), and Pi1 cap Pi2 != empty for preserved cases.
// Also asserts the structural pillars: mod-3 sequences 4-periodic, mod-17
// sequences 4-antiperiodic, and m-periodicity of every enumerated sequence.
#include <bits/stdc++.h>
using namespace std;

int main(int argc, char** argv) {
  int m = atoi(argv[1]); // expect 16 or 24 (8|m)
  const int p1 = 3, p2 = 17;
  assert(m % 8 == 0);
  auto seqs = [&](int p) {
    vector<vector<int>> out;
    for (int y0 = 0; y0 < p; y0++)
      for (int y1 = 0; y1 < p; y1++) {
        vector<int> s(2 * m + 2);
        s[0] = y0; s[1] = y1;
        for (int j = 1; j <= 2 * m; j++)
          s[j + 1] = ((6 * s[j] - s[j - 1]) % p + p) % p;
        // m-periodicity must hold for every (y0,y1): alpha^m = 1 mod p
        assert(s[m] == y0 && s[m + 1] == y1);
        // structural pillars
        for (int j = 0; j < m; j++) {
          if (p == 3) assert(s[j + 4] == s[j]);                 // 4-periodic
          if (p == 17) assert(s[j + 4] == (p - s[j]) % p);       // 4-antiperiodic
        }
        s.resize(m);
        out.push_back(s);
      }
    return out;
  };
  auto A = seqs(p1), B = seqs(p2);
  int nA = A.size(), nB = B.size();
  // dihedral maps d(j) = (eps*j + k) mod m
  struct D { int eps, k; };
  vector<D> Ds;
  for (int e : {1, -1}) for (int k = 0; k < m; k++) Ds.push_back({e, k});
  int nD = Ds.size();
  auto apply = [&](const vector<int>& s, D d) {
    vector<int> t(m);
    for (int j = 0; j < m; j++) {
      int src = (d.eps * j + d.k) % m; if (src < 0) src += m;
      t[j] = s[src];
    }
    return t;
  };
  // permuted sequences
  vector<vector<vector<int>>> Ap(nA, vector<vector<int>>(nD)), Bp(nB, vector<vector<int>>(nD));
  for (int i = 0; i < nA; i++) for (int d = 0; d < nD; d++) Ap[i][d] = apply(A[i], Ds[d]);
  for (int i = 0; i < nB; i++) for (int d = 0; d < nD; d++) Bp[i][d] = apply(B[i], Ds[d]);
  // class-count vectors: [4 classes][p values]
  auto classcounts = [&](const vector<int>& s, int p) {
    array<array<int,17>,4> out{};
    for (int j = 0; j < m; j++) out[j % 4][s[j]]++;
    return out;
  };
  vector<array<array<int,17>,4>> ccA(nA), ccB(nB);
  vector<vector<array<array<int,17>,4>>> ccAp(nA, vector<array<array<int,17>,4>>(nD)),
      ccBp(nB, vector<array<array<int,17>,4>>(nD));
  for (int i = 0; i < nA; i++) { ccA[i] = classcounts(A[i], p1); for (int d = 0; d < nD; d++) ccAp[i][d] = classcounts(Ap[i][d], p1); }
  for (int i = 0; i < nB; i++) { ccB[i] = classcounts(B[i], p2); for (int d = 0; d < nD; d++) ccBp[i][d] = classcounts(Bp[i][d], p2); }
  // D4 elements pi(r) = (eps*r + k) mod 4
  struct P4 { int eps, k; };
  vector<P4> P4s;
  for (int e : {1, -1}) for (int k = 0; k < 4; k++) P4s.push_back({e, k});
  long long total = 0, preserved = 0, bad = 0;
  // pair counts: code = a*p2 + b in [0, 51)
  for (int ia = 0; ia < nA; ia++) for (int ib = 0; ib < nB; ib++) {
    int orig[51] = {};
    for (int j = 0; j < m; j++) orig[A[ia][j] * p2 + B[ib][j]]++;
    for (int d1 = 0; d1 < nD; d1++) for (int d2 = 0; d2 < nD; d2++) {
      total++;
      int cnt[51] = {};
      for (int j = 0; j < m; j++) cnt[Ap[ia][d1][j] * p2 + Bp[ib][d2][j]]++;
      bool same = true;
      for (int c = 0; c < 51; c++) if (cnt[c] != orig[c]) { same = false; break; }
      if (!same) continue;
      preserved++;
      // Pi1, Pi2
      bool in1[8] = {}, in2[8] = {};
      for (int q = 0; q < 8; q++) {
        int e = P4s[q].eps, k = P4s[q].k;
        bool ok1 = true, ok2 = true;
        for (int r = 0; r < 4; r++) {
          int pr = (e * r + k) % 4; if (pr < 0) pr += 4;
          for (int v = 0; v < p1; v++) if (ccAp[ia][d1][r][v] != ccA[ia][pr][v]) ok1 = false;
          for (int v = 0; v < p2; v++) if (ccBp[ib][d2][r][v] != ccB[ib][pr][v]) ok2 = false;
        }
        in1[q] = ok1; in2[q] = ok2;
      }
      bool inter = false;
      for (int q = 0; q < 8; q++) if (in1[q] && in2[q]) inter = true;
      if (!inter) { bad++; if (bad <= 3) printf("BAD ia=%d ib=%d d1=%d d2=%d\n", ia, ib, d1, d2); }
    }
  }
  printf("m=%d pairs=%d dmaps=%d total=%lld preserved=%lld bad=%lld\n", m, nA * nB, nD * nD, total, preserved, bad);
  return bad == 0 ? 0 : 1;
}
