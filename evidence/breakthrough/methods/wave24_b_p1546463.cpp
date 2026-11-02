// Wave 24, task 5 probe 4: second-digit lemma (b2) at p = 1546463 (k=2, L0=773231).
// Random A mod p^2, random c: check v1-marginal change for genuine twists,
// preservation for trivial controls (gap + c = -2b), and K == 0 for gap A
// (symmetry-lemma check at a third prime). Exact __int128 arithmetic.
#include <bits/stdc++.h>
using namespace std;
using i128 = __int128_t;
using i64 = long long;
static i64 P;
static i64 MOD; // p^2

struct E { i64 x, y; };
static inline i64 mm(i128 a) { i64 r = (i64)(a % MOD); if (r < 0) r += MOD; return r; }
static E mul(E a, E b) {
    return {mm((i128)a.x*b.x + (i128)2*a.y*b.y), mm((i128)a.x*b.y + (i128)a.y*b.x)};
}
static E pw(E a, i64 n) {
    E r{1, 0};
    while (n) { if (n & 1) r = mul(r, a); a = mul(a, a); n >>= 1; }
    return r;
}
static i64 normmod(E a) { return mm((i128)a.x*a.x - (i128)2*a.y*a.y); }
static i64 egcd_inv(i128 a, i128 mod, bool &ok) {
    // returns inverse of a mod mod (a, mod coprime), values fit in i128
    i128 old_r = a, r = mod, old_s = 1, s = 0;
    while (r != 0) {
        i128 q = old_r / r;
        i128 t = r; r = old_r - q*r; old_r = t;
        t = s; s = old_s - q*s; old_s = t;
    }
    if (old_r != 1 && old_r != -1) { ok = false; return 0; }
    ok = true;
    i128 inv = old_s % mod; if (inv < 0) inv += mod;
    return (i64)inv;
}
static E invE(E a) {
    i64 n = normmod(a);
    bool ok; i64 ni = egcd_inv(n, MOD, ok); assert(ok);
    return {mm((i128)a.x*ni), mm(-(i128)a.y*ni)};
}
int main() {
    P = 1546463; MOD = P*P;
    E alpha{3, 2};
    // order of alpha mod p
    E cur{1, 0}; i64 L0 = -1;
    for (i64 j = 1; j <= 2*P; j++) {
        cur = mul(cur, E{3 % P, 2}); // careful: mul is mod MOD; do mod-p separately below
        break;
    }
    // mod-p order via separate mod-p arithmetic
    auto mulp = [&](E a, E b) {
        return E{(i64)(((i128)a.x*b.x + (i128)2*a.y*b.y) % P),
                 (i64)(((i128)a.x*b.y + (i128)a.y*b.x) % P)};
    };
    cur = {1, 0};
    for (i64 j = 1; j <= P; j++) {
        cur = mulp(cur, alpha);
        if (cur.x == 1 && cur.y == 0) { L0 = j; break; }
    }
    printf("order of alpha mod p: %lld (expect 773231)\n", (long long)L0);
    E chk = pw(alpha, L0);
    printf("alpha^L0 mod p^2: (%lld,%lld) (expect (1,0))\n", (long long)chk.x, (long long)chk.y);
    assert(L0 == 773231 && chk.x == 1 && chk.y == 0);
    // Teichmuller: m = (p-1)^2, m = 1 mod p so m^{-1} = 1 mod p
    i64 m = (P-1)*(P-1);
    mt19937_64 rng(12345);
    uniform_int_distribution<i64> uni(0, MOD-1);
    vector<int> f1(P, 0), f2(P, 0);
    int n_gap_gen = 0, n_gap_gen_pres = 0, n_nongap_gen = 0, n_nongap_gen_pres = 0;
    int n_triv = 0, n_triv_pres = 0, n_K = 0, n_K_nonzero = 0;
    int tried = 0;
    while ((n_gap_gen < 20 || n_nongap_gen < 20 || n_triv < 5) && tried < 300) {
        tried++;
        E A{uni(rng), uni(rng)};
        if (((((i128)A.x*A.x - (i128)2*A.y*A.y) % P) + P) % P == 0) continue;
        // Teichmuller tau of A
        E wm = pw(A, m);
        // wm = 1 + p*u
        assert(wm.x % P == 1 && wm.y % P == 0);
        i64 ux = (wm.x - 1) / P % P, uy = wm.y / P % P;
        E adj{(1 - P*(ux % P)) % MOD, (-P*(uy % P)) % MOD};
        adj.x = (adj.x % MOD + MOD) % MOD; adj.y = (adj.y % MOD + MOD) % MOD;
        E tau = mul(A, adj);
        E lamq = mul(A, invE(tau));
        assert(lamq.x % P == 1 && lamq.y % P == 0);
        i64 b = (lamq.y - 1*0) ; // lam = (lamq-1)/p
        i64 lamx = (lamq.x - 1) / P % P, lamy = lamq.y / P % P;
        b = lamy;
        // gap?
        E B = pw(A, L0);
        bool gap = (B.y % P == 0);
        // choose c: mostly random; for trivial controls use c = -2b (gap only)
        i64 c;
        bool want_triv = gap && (n_triv < 5) && (tried % 3 == 0);
        if (want_triv) c = ((-2*b) % P + P) % P;
        else c = 1 + (rng() % (P-1));
        if (c == 0) continue;
        bool trivial = gap && (c == ((-2*b) % P + P) % P);
        // orbit marginals
        fill(f1.begin(), f1.end(), 0);
        fill(f2.begin(), f2.end(), 0);
        E w = A;
        for (i64 j = 0; j < L0; j++) {
            i64 Tr = (2*w.x) % MOD;
            i64 v0 = Tr % P;
            i64 v1 = (Tr - v0) / P;
            i64 t = (4*w.y) % P;
            f1[(size_t)v1]++;
            f2[(size_t)((v1 + c*t) % P)]++;
            w = mul(w, alpha);
        }
        bool pres = (f1 == f2);
        if (trivial) { n_triv++; if (pres) n_triv_pres++; }
        else if (gap) { n_gap_gen++; if (pres) { n_gap_gen_pres++; printf("PRESERVED gap genuine! c=%lld b=%lld\n", (long long)c, (long long)b); } }
        else { n_nongap_gen++; if (pres) { n_nongap_gen_pres++; printf("PRESERVED nongap genuine! c=%lld b=%lld\n", (long long)c, (long long)b); } }
        // K check for gap A: K = -2*S/(L0*N(tau)) mod p, S = sum d1*eta over tau-orbit
        if (gap) {
            i128 S = 0;
            E u = tau;
            for (i64 j = 0; j < L0; j++) {
                i64 Tru = (2*u.x) % MOD;
                i64 d1 = (Tru - Tru % P) / P;
                i64 eta = u.y % P;
                S += (i128)d1 * eta;
                u = mul(u, alpha);
            }
            i64 Smod = (i64)(S % P);
            i64 Ntau = (i64)(((i128)tau.x*tau.x - (i128)2*tau.y*tau.y) % P);
            if (Ntau < 0) Ntau += P;
            bool ok; i64 den = egcd_inv((i128)((L0 % P) * Ntau % P), P, ok); assert(ok);
            i64 K = (i64)((-(i128)2 * Smod * den) % P); if (K < 0) K += P;
            n_K++;
            if (K != 0) { n_K_nonzero++; printf("K NONZERO for gap A: K=%lld\n", (long long)K); }
        }
    }
    printf("tried=%d gap_genuine=%d preserved=%d | nongap_genuine=%d preserved=%d | trivial=%d preserved=%d | K checked=%d nonzero=%d\n",
        tried, n_gap_gen, n_gap_gen_pres, n_nongap_gen, n_nongap_gen_pres, n_triv, n_triv_pres, n_K, n_K_nonzero);
    return 0;
}
