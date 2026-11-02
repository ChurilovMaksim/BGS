// Wave 33, task 3 (retry, v2): gauge-free verification of M5 at (324,3).
// v1's delta-check was gauge-dependent (s=12 gauge fits of the identity
// pair give delta!=0 artifactually), so it is replaced by the physical
// content: rigid-block value multisets of corresponding classes match.
// (V1) block census for EVERY unit base point C: 81 orbit values grouped
//      by j mod 9; each block rigid (1 value), full line (3 values, same
//      mod 81, each mult 3), or OTHER. Report by collapsed-ness
//      (C real mod 3, C != 0 mod 3) and per-orbit rigid counts.
// (V2) for every unit pair (rep A0, A') in a global group, for every
//      pi in D4 matching A0's class multisets to A''s, compare the rigid
//      value multiset of A0's class r with A''s class pi(r), for all r.
//      Class reps are canonical: C_r = A0*alpha^r, C'_r = A'*alpha^r.
#include <algorithm>
#include <array>
#include <cstdio>
#include <cstring>
#include <cstdint>
#include <vector>
using namespace std;
const int P = 243, M = 324;
struct E { int a, b; };
static inline E mul(E x, E y) {
    return {(x.a*y.a + 2*x.b*y.b) % P, (x.a*y.b + x.b*y.a) % P};
}
static inline int tr(E x) { return (2*x.a) % P; }
struct Rec { array<uint16_t, P> g{}; int idx; };
// rigid values of the gamma-orbit with base point C (sorted list)
static vector<int> rigidOf(E C, E gamma) {
    int vals[81]; E cc = C;
    for (int j = 0; j < 81; j++) { vals[j] = tr(cc); cc = mul(cc, gamma); }
    vector<int> rig;
    for (int bl = 0; bl < 9; bl++) {
        int v = vals[bl]; bool same = true;
        for (int j = bl; j < 81; j += 9) if (vals[j] != v) same = false;
        if (same) rig.push_back(v);
    }
    sort(rig.begin(), rig.end());
    return rig;
}
int main() {
    const E ALPHA{3, 2};
    vector<E> ap(M + 1); ap[0] = {1, 0};
    for (int i = 1; i <= M; i++) ap[i] = mul(ap[i-1], ALPHA);
    E gamma = ap[4];
    // ---- (V1) block census, all units ----
    long nCU = 0, nNU = 0, blCU = 0, blNU = 0, rCU = 0, rNU = 0, lCU = 0, lNU = 0;
    long oCU = 0, oNU = 0, fbad = 0;
    long minRigC = 99, maxRigC = -1, minRigN = 99, maxRigN = -1;
    int oshown = 0;
    for (int ca = 0; ca < P; ca++) for (int cb = 0; cb < P; cb++) {
        if (ca % 3 == 0 && cb % 3 == 0) continue;
        bool coll = (cb % 3 == 0 && ca % 3 != 0);
        E c{ca, cb};
        int vals[81]; E cc = c;
        for (int j = 0; j < 81; j++) { vals[j] = tr(cc); cc = mul(cc, gamma); }
        int nr = 0;
        for (int bl = 0; bl < 9; bl++) {
            int bv[9], nb = 0;
            for (int j = bl; j < 81; j += 9) bv[nb++] = vals[j];
            int m81 = bv[0] % 81, ok81 = 1;
            for (int k = 0; k < 9; k++) if (bv[k] % 81 != m81) ok81 = 0;
            if (!ok81) fbad++;
            sort(bv, bv + 9);
            int nd = 1; for (int k = 1; k < 9; k++) if (bv[k] != bv[k-1]) nd++;
            bool isRig = (nd == 1);
            bool isLine = (nd == 3 && bv[0] == bv[1] && bv[1] == bv[2] && bv[3] == bv[4] &&
                           bv[4] == bv[5] && bv[6] == bv[7] && bv[7] == bv[8] && ok81);
            if (coll) { blCU++; if (isRig) { rCU++; nr++; } else if (isLine) lCU++; else { oCU++; if (oshown < 5) { oshown++; printf("OTHER collapsed C=(%d,%d) bl=%d\n", ca, cb, bl); } } }
            else { blNU++; if (isRig) { rNU++; nr++; } else if (isLine) lNU++; else { oNU++; if (oshown < 5) { oshown++; printf("OTHER noncoll C=(%d,%d) bl=%d\n", ca, cb, bl); } } }
        }
        if (coll) { minRigC = min(minRigC, (long)nr); maxRigC = max(maxRigC, (long)nr); }
        else { minRigN = min(minRigN, (long)nr); maxRigN = max(maxRigN, (long)nr); }
        if (coll) nCU++; else nNU++;
    }
    printf("V1: collapsedPts=%ld blocks=%ld rigid=%ld line=%ld OTHER=%ld rigidPerOrbit=[%ld,%ld]\n",
           nCU, blCU, rCU, lCU, oCU, minRigC, maxRigC);
    printf("V1: noncollPts=%ld blocks=%ld rigid=%ld line=%ld OTHER=%ld rigidPerOrbit=[%ld,%ld] fiber81bad=%ld\n",
           nNU, blNU, rNU, lNU, oNU, minRigN, maxRigN, fbad);
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
    int perms[8][4], np = 0;
    for (int eps : {1, -1}) for (int bb = 0; bb < 4; bb++) {
        for (int r = 0; r < 4; r++) perms[np][r] = ((eps*r + bb) % 4 + 4) % 4;
        np++;
    }
    long nGroups = 0, nPairs = 0, nNoPi = 0, nPi1 = 0, nPiMulti = 0;
    long nRigCmp = 0, nRigBad = 0, nRigNonVac = 0;
    int rshown = 0;
    size_t i = 0;
    while (i < recs.size()) {
        size_t j = i;
        while (j < recs.size() && memcmp(recs[j].g.data(), recs[i].g.data(), sizeof(recs[i].g)) == 0) j++;
        nGroups++;
        int rep = -1;
        for (size_t k = i; k < j; k++) {
            int A = recs[k].idx;
            if (A / P % 3 != 0 || A % P % 3 != 0) { rep = A; break; }
        }
        if (rep < 0) { i = j; continue; }
        E A0{rep / P, rep % P};
        // class count vectors + rigid multisets for rep
        array<array<uint16_t, P>, 4> pc0{}; for (auto& v : pc0) v.fill(0);
        E c0 = A0;
        for (int s = 0; s < M; s++) { pc0[s % 4][tr(c0)]++; c0 = mul(c0, ALPHA); }
        vector<int> rig0[4];
        for (int r = 0; r < 4; r++) rig0[r] = rigidOf(mul(A0, ap[r]), gamma);
        for (size_t k = i; k < j; k++) {
            int A = recs[k].idx, a = A / P, b = A % P;
            if (a % 3 == 0 && b % 3 == 0) continue;
            nPairs++;
            E Apr{a, b};
            array<array<uint16_t, P>, 4> pc1{}; for (auto& v : pc1) v.fill(0);
            E c1 = Apr;
            for (int s = 0; s < M; s++) { pc1[s % 4][tr(c1)]++; c1 = mul(c1, ALPHA); }
            int npi = 0;
            for (int pi = 0; pi < 8; pi++) {
                bool ok = true;
                for (int r = 0; r < 4; r++)
                    if (memcmp(pc0[r].data(), pc1[perms[pi][r]].data(), sizeof(uint16_t)*P) != 0) ok = false;
                if (!ok) continue;
                npi++;
                vector<int> rig1[4];
                for (int r = 0; r < 4; r++) rig1[r] = rigidOf(mul(Apr, ap[perms[pi][r]]), gamma);
                for (int r = 0; r < 4; r++) {
                    nRigCmp++;
                    if (!rig0[r].empty()) nRigNonVac++;
                    if (rig0[r] != rig1[r]) {
                        nRigBad++;
                        if (rshown < 10) {
                            rshown++;
                            printf("RIGID MISMATCH rep=(%d,%d) Apr=(%d,%d) pi=%d r=%d rig0=", A0.a, A0.b, Apr.a, Apr.b, pi, r);
                            for (int v : rig0[r]) printf("%d ", v);
                            printf(" rig1=");
                            for (int v : rig1[r]) printf("%d ", v);
                            printf("\n");
                        }
                    }
                }
            }
            if (npi == 0) nNoPi++;
            else if (npi == 1) nPi1++;
            else nPiMulti++;
        }
        i = j;
    }
    printf("V2: groups=%ld pairs=%ld noPi=%ld piUnique=%ld piMulti=%ld rigidCmp=%ld rigidNonVac=%ld rigidBad=%ld\n",
           nGroups, nPairs, nNoPi, nPi1, nPiMulti, nRigCmp, nRigNonVac, nRigBad);
    return 0;
}
