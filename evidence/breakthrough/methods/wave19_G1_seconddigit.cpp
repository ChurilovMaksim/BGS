// Wave 19, task 3: second-digit twist invariant at p=31 (generalising wave 18, p=13).
// (v2: fixed rho = Abar^{-1} * A = A^2 / N(A); earlier version used Abar/N, wrong.)
//
// Setup: R = Z[sqrt2], p odd, modulus p^2. alpha = 3+2*sqrt2, order L0 mod p
// and mod p^2 (k = 2, s = 0). G = <alpha> mod p^2, |G| = L0.
// Twist: A' = A*(1 + p*c*sqrt2), c = 1..p-1 (purely imaginary twists;
// zeta in G is irrelevant: it permutes the orbit).
// Orbit values v_z = Tr(Az) mod p^2, z in G. Write v_z = v0_z + p*v1_z.
// Twisted second digit: v1'_z = (v1_z + c*t_z) mod p, t_z = Tr(A*sqrt2*z) mod p.
// Statistics: v1-marginal (sorted v1 list); joint (sorted (v0,v1) pairs),
// which equals conditional-on-v0 (v0 multiset is unchanged by the twist).
// Genuine twist: A' not in A*G union Abar*G.
//   A' in A*G  <=> (1+p*c*sqrt2) in G (never for c != 0: reduction mod p injective on G).
//   A' in Abar*G <=> rho*(1+p*c*sqrt2) in G, rho = Abar^{-1}*A = A^2/N(A).
// Gap case: B = A^L0 real mod p.
// Exact integer arithmetic; single-threaded; no external deps.
// Compile-time parameters P, M (= P^2), ORB (= L0); p=13 version via sed.
#include <bits/stdc++.h>
using namespace std;
const int P = 31, M = 961, ORB = 15;

struct E { int a, b; };
bool eqE(E x, E y) { return x.a == y.a && x.b == y.b; }
E mulE(E x, E y, int m) {
  long long a = (long long)x.a * y.a + 2LL * x.b * y.b;
  long long b = (long long)x.a * y.b + (long long)x.b * y.a;
  return {(int)(a % m), (int)(b % m)};
}
E pwE(E x, int n, int m) {
  E r{1, 0};
  while (n) { if (n & 1) r = mulE(r, x, m); x = mulE(x, x, m); n >>= 1; }
  return r;
}
int modinv(int a, int m) {
  int t = 0, nt = 1, r = m, nr = (a % m + m) % m;
  while (nr) { int q = r / nr; int tmp = nt; nt = t - q * nt; t = tmp; tmp = nr; nr = r - q * nr; r = tmp; }
  return (t % m + m) % m;
}

struct Example {
  bool set = false;
  int a = 0, b = 0, c = 0;
};

int main() {
  E alpha{3, 2};
  E aL0_P = pwE(alpha, ORB, P);
  E aL0_M = pwE(alpha, ORB, M);
  E aL0_P3 = pwE(alpha, ORB, P * P * P);
  printf("alpha^L0 mod p = (%d,%d); mod p^2 = (%d,%d); mod p^3 = (%d,%d)\n",
         aL0_P.a, aL0_P.b, aL0_M.a, aL0_M.b, aL0_P3.a, aL0_P3.b);
  E x{1, 0};
  int ordP = 0;
  do { x = mulE(x, alpha, P); ordP++; } while (!eqE(x, E{1, 0}));
  printf("order of alpha mod p = %d\n", ordP);
  vector<E> G;
  x = {1, 0};
  do { G.push_back(x); x = mulE(x, alpha, M); } while (!eqE(x, E{1, 0}));
  printf("|G| mod p^2 = %zu\n", G.size());
  vector<char> Gset((size_t)M * M, 0);
  for (auto z : G) Gset[(size_t)z.a * M + z.b] = 1;
  // H0 = <alpha^2>; equals G iff gcd(2,ORB)=1
  vector<E> H0;
  x = {1, 0};
  E a2 = mulE(alpha, alpha, M);
  do { H0.push_back(x); x = mulE(x, a2, M); } while (!eqE(x, E{1, 0}));
  bool h0eq = (H0.size() == G.size());
  if (h0eq) for (auto z : H0) if (!Gset[(size_t)z.a * M + z.b]) h0eq = false;
  printf("|H0| = %zu, H0 == G as sets: %d\n", H0.size(), (int)h0eq);
  bool twInG[64] = {false};
  for (int c = 1; c < P; c++) { E tw{1, (P * c) % M}; twInG[c] = Gset[(size_t)tw.a * M + tw.b]; }
  printf("twist (1+p*c*sqrt2) in G for some c=1..p-1: %d\n",
         (int)any_of(begin(twInG) + 1, begin(twInG) + P, [](bool v) { return v; }));

  long long n_units = 0, n_breal = 0;
  // counts: [0] = all units, [1] = B-real units
  long long pairs[2] = {0, 0}, genuine[2] = {0, 0}, trivial[2] = {0, 0};
  long long marg_coinc_gen[2] = {0, 0}, marg_coinc_triv[2] = {0, 0};
  long long joint_pres_gen[2] = {0, 0}, joint_pres_triv[2] = {0, 0};
  Example ex_triv_joint, ex_gen_margdiff, ex_gen_margcoinc, ex_gen_jointpres;

  vector<int> v0(ORB), v1(ORB), tt(ORB), bk(ORB), v1p(ORB), tk(ORB);
  vector<int> basefreq(P), f2(P);
  for (int a = 0; a < M; a++) {
    int aP = a % P;
    for (int b = 0; b < M; b++) {
      int bP = b % P;
      int normP = (aP * aP - 2 * bP * bP) % P;
      if (normP < 0) normP += P;
      if (normP == 0) continue;  // not a unit mod p^2
      n_units++;
      // B-real: B = A^L0 mod p has b-component 0
      E BP = pwE(E{aP, bP}, ORB, P);
      bool breal = (BP.b == 0);
      if (breal) n_breal++;
      // base orbit digits
      for (int i = 0; i < ORB; i++) {
        int z0 = G[i].a, z1 = G[i].b;
        int v = (2 * (a * z0 + 2 * b * z1)) % M;
        v0[i] = v % P;
        v1[i] = (v - v0[i]) / P;
        bk[i] = v0[i] * P + v1[i];
        int t = (4 * (bP * (z0 % P) + aP * (z1 % P))) % P;
        tt[i] = t;
      }
      sort(bk.begin(), bk.end());
      fill(basefreq.begin(), basefreq.end(), 0);
      for (int i = 0; i < ORB; i++) basefreq[v1[i]]++;
      // rho = Abar^{-1} * A = A^2 / N(A)  (Abar^{-1} = A / N(A))
      int N = (a * a - 2 * b * b) % M;
      if (N < 0) N += M;
      int Ninv = modinv(N, M);
      E Asq = mulE(E{a, b}, E{a, b}, M);
      E rho{(Asq.a * Ninv) % M, (Asq.b * Ninv) % M};
      for (int c = 1; c < P; c++) {
        E tw{1, (P * c) % M};
        E rtw = mulE(rho, tw, M);
        bool gen = !(twInG[c] || Gset[(size_t)rtw.a * M + rtw.b]);
        int idx[2] = {0, breal ? 1 : -1};
        for (int k = 0; k < 2; k++) {
          int id = idx[k];
          if (id < 0) continue;
          pairs[id]++;
          if (gen) genuine[id]++; else trivial[id]++;
        }
        // second digits under twist
        for (int i = 0; i < ORB; i++) {
          int s = (c * tt[i]) % P;
          int np = v1[i] + s;
          if (np >= P) np -= P;
          v1p[i] = np;
        }
        fill(f2.begin(), f2.end(), 0);
        for (int i = 0; i < ORB; i++) f2[v1p[i]]++;
        bool marg_eq = true;
        for (int d = 0; d < P; d++) if (f2[d] != basefreq[d]) { marg_eq = false; break; }
        if (!marg_eq) {
          if (gen && !ex_gen_margdiff.set) { ex_gen_margdiff = {true, a, b, c}; }
          continue;  // joint differs automatically
        }
        // marginal coincides: classify, then joint check
        for (int k = 0; k < 2; k++) {
          int id = idx[k];
          if (id < 0) continue;
          if (gen) marg_coinc_gen[id]++; else marg_coinc_triv[id]++;
        }
        if (gen && !ex_gen_margcoinc.set) { ex_gen_margcoinc = {true, a, b, c}; }
        for (int i = 0; i < ORB; i++) tk[i] = v0[i] * P + v1p[i];
        sort(tk.begin(), tk.end());
        bool joint_eq = true;
        for (int i = 0; i < ORB; i++) if (tk[i] != bk[i]) { joint_eq = false; break; }
        if (!joint_eq) continue;
        for (int k = 0; k < 2; k++) {
          int id = idx[k];
          if (id < 0) continue;
          if (gen) joint_pres_gen[id]++; else joint_pres_triv[id]++;
        }
        if (gen && !ex_gen_jointpres.set) { ex_gen_jointpres = {true, a, b, c}; }
        if (!gen && !ex_triv_joint.set) { ex_triv_joint = {true, a, b, c}; }
      }
    }
  }
  printf("\nunits mod p^2: %lld\n", n_units);
  printf("B-real units: %lld\n", n_breal);
  const char* lbl[2] = {"all units", "B-real units"};
  for (int id = 0; id < 2; id++) {
    printf("\n[%s] pairs=%lld genuine=%lld trivial=%lld\n", lbl[id], pairs[id], genuine[id], trivial[id]);
    printf("  marginal coincidences: genuine=%lld trivial=%lld\n", marg_coinc_gen[id], marg_coinc_triv[id]);
    printf("  joint preservations:   genuine=%lld trivial=%lld\n", joint_pres_gen[id], joint_pres_triv[id]);
  }
  auto show = [&](const char* name, Example ex) {
    if (!ex.set) { printf("\n%s: none\n", name); return; }
    int a = ex.a, b = ex.b, c = ex.c, aP = a % P, bP = b % P;
    vector<int> base, tw;
    for (int i = 0; i < ORB; i++) {
      int v = (2 * (a * G[i].a + 2 * b * G[i].b)) % M;
      base.push_back(v);
      int t = (4 * (bP * (G[i].a % P) + aP * (G[i].b % P))) % P;
      int v0i = v % P, v1i = (v - v0i) / P;
      int np = v1i + (c * t) % P; if (np >= P) np -= P;
      tw.push_back(v0i + P * np);
    }
    sort(base.begin(), base.end());
    sort(tw.begin(), tw.end());
    printf("\n%s: A=(%d,%d) c=%d\n  base orbit:   ", name, a, b, c);
    for (int v : base) printf("%d ", v);
    printf("\n  twisted orbit:");
    for (int v : tw) printf("%d ", v);
    printf("\n");
  };
  show("first trivial joint-preserving", ex_triv_joint);
  show("first genuine twist, marginals differ", ex_gen_margdiff);
  show("first genuine marginal coincidence (COUNTEREXAMPLE if present)", ex_gen_margcoinc);
  show("first genuine joint preservation (COUNTEREXAMPLE if present)", ex_gen_jointpres);
  return 0;
}
