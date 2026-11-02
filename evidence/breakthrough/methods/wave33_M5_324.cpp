// Wave 33, task 3 (retry): verify M5 at (324,3) mod 243 only.
// (V1) level-5 vertex/block decomposition: for every collapsed unit base
//      point C (C real mod 3, C != 0 mod 3), the 81 orbit values grouped by
//      j mod 9 (9 blocks x 9 values) are each rigid (1 value) or a full
//      line (3 values, same mod 81, each mult 3); anything else is OTHER.
// (V2) coefficient vanishing: for every unit A' in the global group of a
//      unit rep A0, for every fit A' = A0^eps * alpha^s * (1+9*eta1+27*eta2
//      +81*eta3) mod 243 with Tr(eta1)=Tr(eta2)=0 mod 3, and every collapsed
//      orbit C of B = A0^eps*alpha^s, check
//      delta(a,C) = Tr(C*eta3) + a*Tr(C*eta2*u) + C(a,2)*Tr(C*eta1*u^2)
//      == 0 mod 3 for all a in F3 (all traces computed directly mod 3).
// Divisible A go by induction (as in M4 s7); only units are checked.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;
const int P = 243, M = 324;
struct E { int a, b; };
static inline E mul(E x, E y) {
    return {(x.a*y.a + 2*x.b*y.b) % P, (x.a*y.b + x.b*y.a) % P};
}
static inline int tr(E x) { return (2*x.a) % P; }
static inline E conjE(E x) { return {x.a, (P - x.b) % P}; }
static E inv(E x) {
    int n = (x.a*x.a - 2*x.b*x.b) % P; if (n < 0) n += P;
    int t = 0, nt = 1, r = P, nr = n;
    while (nr) { int q = r / nr, tmp = nt; nt = t - q*nt; t = tmp; tmp = nr; nr = r - q*nr; r = tmp; }
    if (t < 0) t += P;
    return {(x.a*t) % P, (P - (x.b*t) % P) % P};
}
// mod-3 arithmetic for delta: elements as (a3,b3)
struct E3 { int a, b; };
static inline E3 mul3(E3 x, E3 y) {
    return {(x.a*y.a + 2*x.b*y.b) % 3, (x.a*y.b + x.b*y.a) % 3};
}
static inline int tr3(E3 x) { return (2*x.a) % 3; }
struct Rec { array<uint16_t, P> g{}; int idx; };
int main() {
    const E ALPHA{3, 2};
    E cur{1, 0};
    for (int i = 0; i < M; i++) cur = mul(cur, ALPHA);
    printf("alpha^324 mod 243 = (%d,%d) (need (1,0))\n", cur.a, cur.b);
    if (cur.a != 1 || cur.b != 0) return 1;
    // alpha powers mod 243
    vector<E> ap(M + 1); ap[0] = {1, 0};
    for (int i = 1; i <= M; i++) ap[i] = mul(ap[i-1], ALPHA);
    E gamma = ap[4];
    printf("gamma = alpha^4 = (%d,%d)\n", gamma.a, gamma.b);
    // gamma = 1 + 3u, u mod 81
    if ((gamma.a - 1) % 3 != 0 || gamma.b % 3 != 0) { printf("gamma != 1 mod 3!\n"); return 1; }
    E u81{(gamma.a - 1) / 3 % 81, gamma.b / 3 % 81};
    printf("u mod 81 = (%d,%d); u mod 3 = (%d,%d) (need (0,1), mu=1)\n",
           u81.a, u81.b, u81.a % 3, u81.b % 3);
    E gpow{1, 0}; for (int i = 0; i < 81; i++) gpow = mul(gpow, gamma);
    printf("gamma^81 = (%d,%d) (need (1,0))\n", gpow.a, gpow.b);
    E3 u3{u81.a % 3, u81.b % 3};
    E3 u3sq = mul3(u3, u3);
    printf("u^2 mod 3 = (%d,%d) (expect (2,0))\n", u3sq.a, u3sq.b);
    // ---- (V1) block census over collapsed unit base points ----
    long nColl = 0, nBlocks = 0, nRigid = 0, nLine = 0, nOther = 0, nFiberBad = 0;
    int shown = 0;
    for (int ca = 0; ca < P; ca++) for (int cb = 0; cb < P; cb++) {
        if (ca % 3 == 0 && cb % 3 == 0) continue; // non-unit
        if (!(cb % 3 == 0 && ca % 3 != 0)) continue; // not collapsed
        nColl++;
        E c{ca, cb};
        int vals[81];
        E cc = c;
        for (int j = 0; j < 81; j++) { vals[j] = tr(cc); cc = mul(cc, gamma); }
        for (int bl = 0; bl < 9; bl++) {
            nBlocks++;
            int bv[9], nb = 0;
            for (int j = bl; j < 81; j += 9) bv[nb++] = vals[j];
            int m81 = bv[0] % 81, ok81 = 1;
            for (int k = 0; k < 9; k++) if (bv[k] % 81 != m81) ok81 = 0;
            if (!ok81) nFiberBad++;
            sort(bv, bv + 9);
            int nd = 1; for (int k = 1; k < 9; k++) if (bv[k] != bv[k-1]) nd++;
            if (nd == 1) nRigid++;
            else if (nd == 3 && bv[0] == bv[1] && bv[1] == bv[2] && bv[3] == bv[4] &&
                     bv[4] == bv[5] && bv[6] == bv[7] && bv[7] == bv[8] && ok81) nLine++;
            else {
                nOther++;
                if (shown < 5) {
                    shown++;
                    printf("OTHER block: C=(%d,%d) block=%d vals=", ca, cb, bl);
                    for (int k = 0; k < 9; k++) printf("%d ", bv[k]);
                    printf("(fiber81 ok=%d)\n", ok81);
                }
            }
        }
    }
    printf("V1: collapsed base points=%ld blocks=%ld rigid=%ld fullline=%ld OTHER=%ld fiber81bad=%ld\n",
           nColl, nBlocks, nRigid, nLine, nOther, nFiberBad);
    // ---- groups by global multiset ----
    vector<Rec> recs; recs.reserve(P*P);
    for (int a = 0; a < P; a++) for (int b = 0; b < P; b++) {
        Rec r; r.g.fill(0); r.idx = a*P + b;
        E c{a, b};
        for (int i = 0; i < M; i++) { r.g[tr(c)]++; c = mul(c, ALPHA); }
        recs.push_back(r);
    }
    sort(recs.begin(), recs.end(), [](const Rec& x, const Rec& y) {
        return memcmp(x.g.data(), y.g.data(), sizeof(x.g)) < 0;
    });
    // alpha^s mod 9 lookup, s in 0..11
    int amod9[12][2];
    E cc9{1, 0};
    for (int s = 0; s < 12; s++) { amod9[s][0] = cc9.a % 9; amod9[s][1] = cc9.b % 9; cc9 = mul(cc9, ALPHA); }
    // ---- (V2) fits and delta ----
    long nGroups = 0, nGroupsUnit = 0, nApr = 0, nFits = 0, nValid = 0, nNoFit = 0;
    long nDelta = 0, nDeltaBad = 0;
    int dshown = 0;
    size_t i = 0;
    while (i < recs.size()) {
        size_t j = i;
        while (j < recs.size() && memcmp(recs[j].g.data(), recs[i].g.data(), sizeof(recs[i].g)) == 0) j++;
        nGroups++;
        int rep = -1;
        for (size_t k = i; k < j; k++) {
            int A = recs[k].idx, a = A / P, b = A % P;
            if (a % 3 != 0 || b % 3 != 0) { rep = A; break; }
        }
        if (rep < 0) { i = j; continue; }
        nGroupsUnit++;
        E A0{rep / P, rep % P};
        for (size_t k = i; k < j; k++) {
            int A = recs[k].idx, a = A / P, b = A % P;
            if (a % 3 == 0 && b % 3 == 0) continue; // divisible: induction case
            nApr++;
            E Apr{a, b};
            int nValidHere = 0;
            for (int eps = 0; eps < 2; eps++) {
                E base = eps ? conjE(A0) : A0;
                E T = mul(Apr, inv(base));
                int t9a = T.a % 9, t9b = T.b % 9, s0 = -1;
                for (int s = 0; s < 12; s++)
                    if (amod9[s][0] == t9a && amod9[s][1] == t9b) s0 = s;
                if (s0 < 0) continue;
                for (int kk = 0; kk < 27; kk++) {
                    int s = s0 + 12*kk;
                    E Bs = mul(base, ap[s]);
                    E R = mul(Apr, inv(Bs));
                    nFits++;
                    if (R.a % 9 != 1 || R.b % 9 != 0) continue; // cannot happen; guard
                    int ea = ((R.a - 1) / 9) % 27, eb = (R.b / 9) % 27;
                    E3 e1{ea % 3, eb % 3}, e2{(ea / 3) % 3, (eb / 3) % 3}, e3{(ea / 9) % 3, (eb / 9) % 3};
                    if (tr3(e1) != 0 || tr3(e2) != 0) continue; // not a level-4 fit
                    nValid++; nValidHere++;
                    // collapsed orbits of B
                    for (int ci = 0; ci < 4; ci++) {
                        E C = mul(Bs, ap[ci]);
                        if (!(C.b % 3 == 0 && C.a % 3 != 0)) continue;
                        E3 C3{C.a % 3, C.b % 3};
                        int tCe3 = tr3(mul3(C3, e3));
                        int tCe2u = tr3(mul3(mul3(C3, e2), u3));
                        int tCe1u2 = tr3(mul3(mul3(C3, e1), u3sq));
                        for (int av = 0; av < 3; av++) {
                            int comb = av*(av - 1) / 2;
                            int d = (tCe3 + av*tCe2u + comb*tCe1u2) % 3;
                            nDelta++;
                            if (d != 0) {
                                nDeltaBad++;
                                if (dshown < 10) {
                                    dshown++;
                                    printf("DELTA!=0: rep=(%d,%d) Apr=(%d,%d) eps=%d s=%d eta=(%d,%d)|(%d,%d)|(%d,%d) C=(%d,%d) a=%d delta=%d\n",
                                           A0.a, A0.b, Apr.a, Apr.b, eps ? -1 : 1, s,
                                           e1.a, e1.b, e2.a, e2.b, e3.a, e3.b, C.a, C.b, av, d);
                                }
                            }
                        }
                    }
                }
            }
            if (nValidHere == 0) nNoFit++;
        }
        i = j;
    }
    printf("V2: groups=%ld unitGroups=%ld unitApr=%ld fits=%ld validFits=%ld AprWithNoValidFit=%ld deltaEvals=%ld deltaBad=%ld\n",
           nGroups, nGroupsUnit, nApr, nFits, nValid, nNoFit, nDelta, nDeltaBad);
    return 0;
}
