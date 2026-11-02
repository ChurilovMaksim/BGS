// Wave 26, task 2: exact PC check for one triple (m, p1, p2).
// Sequences: a_j = Tr(A alpha^j) mod p1, b_j = Tr(B alpha^j) mod p2,
// alpha = 3+2 sqrt2, A in R/p1, B in R/p2 (all p^2, since alpha^m = 1
// mod p for every odd p | D_m). d in D_m: d(j) = eps*j + k mod m.
// (*) : {(a_{d1(j)}, b_{d2(j)})} = {(a_j, b_j)} as multisets.
// Reduction: (*) iff for e = d2 o d1^{-1}, for every a-value v,
// {b_{e(j)} : a_j = v} = {b_j : a_j = v} (fibre condition).
// Pi_i: pi in D_t (functions, deduplicated) with class multisets matching.
// Usage: ./pc_check m p1 p2
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int mod_norm(int x, int p) { x %= p; if (x < 0) x += p; return x; }
// R/p element as (x, y) = x + y sqrt2
struct E { int x, y; };
E mulE(E a, E b, int p) {
    return {(int)(((ll)a.x * b.x + 2LL * a.y * b.y) % p),
            (int)(((ll)a.x * b.y + (ll)a.y * b.x) % p)};
}

int main(int argc, char** argv) {
    if (argc < 4) { cerr << "usage: pc_check m p1 p2\n"; return 1; }
    int m = atoi(argv[1]), p1 = atoi(argv[2]), p2 = atoi(argv[3]);
    int t = std::gcd(m, 4);
    // D_t as deduplicated functions r -> (eps*r + k) mod t
    vector<vector<int>> Dt;
    for (int eps : {1, -1}) for (int k = 0; k < t; k++) {
        vector<int> f(t);
        for (int r = 0; r < t; r++) f[r] = mod_norm(eps * r + k, t);
        if (find(Dt.begin(), Dt.end(), f) == Dt.end()) Dt.push_back(f);
    }
    int nDt = Dt.size();
    int fullMask = (1 << nDt) - 1;
    // map pi-function tuple -> index, for pi_d of d in D_m
    auto pi_index = [&](int eps, int k) {
        vector<int> f(t);
        for (int r = 0; r < t; r++) f[r] = mod_norm(eps * r + k, t);
        for (int i = 0; i < nDt; i++) if (Dt[i] == f) return i;
        return -1;
    };
    // D_m elements: (eps, k); pi index; composition table for e o d1
    struct Dd { int eps, k, pi; };
    vector<Dd> Dm;
    for (int eps : {1, -1}) for (int k = 0; k < m; k++)
        Dm.push_back({eps, k, pi_index(eps, k)});
    int nDm = Dm.size();
    // comp[e][d1] = index of e o d1 in Dm
    vector<vector<int>> comp(nDm, vector<int>(nDm, -1));
    for (int i = 0; i < nDm; i++) for (int j = 0; j < nDm; j++) {
        int eps = Dm[i].eps * Dm[j].eps;
        int k = mod_norm(Dm[i].eps * Dm[j].k + Dm[i].k, m);
        for (int q = 0; q < nDm; q++)
            if (Dm[q].eps == eps && Dm[q].k == k) { comp[i][j] = q; break; }
    }
    auto apply_d = [&](const Dd& d, int j) { return mod_norm(d.eps * j + d.k, m); };

    // sequences for all A in R/p1, B in R/p2
    auto all_seqs = [&](int p) {
        vector<vector<int>> seqs;
        vector<E> pw(m + 1);
        pw[0] = {1, 0};
        for (int j = 0; j < m; j++) pw[j + 1] = mulE(pw[j], {3, 2}, p);
        for (int ax = 0; ax < p; ax++) for (int ay = 0; ay < p; ay++) {
            vector<int> s(m);
            for (int j = 0; j < m; j++) {
                E c = mulE({ax, ay}, pw[j], p);
                s[j] = mod_norm(2 * c.x, p);
            }
            seqs.push_back(move(s));
        }
        return seqs;
    };
    vector<vector<int>> SA = all_seqs(p1), SB = all_seqs(p2);
    int nA = SA.size(), nB = SB.size();
    // class multisets: CM[seq][r] = sorted values on O_r
    auto class_multis = [&](const vector<int>& s) {
        vector<vector<int>> cm(t);
        for (int j = 0; j < m; j++) cm[j % t].push_back(s[j]);
        for (int r = 0; r < t; r++) sort(cm[r].begin(), cm[r].end());
        return cm;
    };
    vector<vector<vector<int>>> CMA(nA), CMB(nB);
    vector<char> allEqA(nA, 0), allEqB(nB, 0);
    for (int i = 0; i < nA; i++) {
        CMA[i] = class_multis(SA[i]);
        allEqA[i] = 1;
        for (int r = 1; r < t; r++) if (CMA[i][r] != CMA[i][0]) allEqA[i] = 0;
    }
    for (int i = 0; i < nB; i++) {
        CMB[i] = class_multis(SB[i]);
        allEqB[i] = 1;
        for (int r = 1; r < t; r++) if (CMB[i][r] != CMB[i][0]) allEqB[i] = 0;
    }
    // Pi masks: PiMask[seq][delta] over D_t functions, delta = pi_d index
    auto pi_masks = [&](const vector<vector<vector<int>>>& CM) {
        int n = CM.size();
        vector<vector<int>> masks(n, vector<int>(nDt, 0));
        for (int i = 0; i < n; i++) {
            for (int di = 0; di < nDt; di++) {
                int mask = 0;
                for (int pi = 0; pi < nDt; pi++) {
                    bool ok = true;
                    for (int r = 0; r < t; r++)
                        if (CM[i][Dt[di][r]] != CM[i][Dt[pi][r]]) { ok = false; break; }
                    if (ok) mask |= (1 << pi);
                }
                masks[i][di] = mask;
            }
        }
        return masks;
    };
    vector<vector<int>> PiA = pi_masks(CMA), PiB = pi_masks(CMB);
    bool side1_forced_full = true, side2_forced_full = true;
    for (int i = 0; i < nA; i++) if (!allEqA[i]) side1_forced_full = false;
    for (int i = 0; i < nB; i++) if (!allEqB[i]) side2_forced_full = false;

    // groups of positions by a-value (values < p1)
    long long nPairs = 0, nSkipped = 0, nPreserved = 0, nBad = 0;
    bool nondeg = false;
    int badA = -1, badB = -1, badE = -1, badD1 = -1, witA = -1, witB = -1, witE = -1, witD1 = -1;
    vector<int> tmp1, tmp2;
    for (int ia = 0; ia < nA; ia++) {
        const vector<int>& a = SA[ia];
        // positions by a-value
        vector<vector<int>> groups(p1);
        for (int j = 0; j < m; j++) groups[a[j]].push_back(j);
        for (int ib = 0; ib < nB; ib++) {
            nPairs++;
            bool skipPi = (allEqA[ia] || allEqB[ib]);
            if (skipPi) nSkipped++;
            const vector<int>& b = SB[ib];
            for (int ei = 0; ei < nDm; ei++) {
                const Dd& e = Dm[ei];
                bool fibre_ok = true;
                for (int v = 0; v < p1 && fibre_ok; v++) {
                    auto& g = groups[v];
                    if (g.empty()) continue;
                    tmp1.clear(); tmp2.clear();
                    for (int j : g) { tmp1.push_back(b[j]); tmp2.push_back(b[apply_d(e, j)]); }
                    sort(tmp1.begin(), tmp1.end());
                    sort(tmp2.begin(), tmp2.end());
                    if (tmp1 != tmp2) fibre_ok = false;
                }
                if (!fibre_ok) continue;
                // (*) holds for all d1 with d2 = e o d1
                for (int d1 = 0; d1 < nDm; d1++) {
                    nPreserved++;
                    if (skipPi) continue;
                    int d2 = comp[ei][d1];
                    int m1 = PiA[ia][Dm[d1].pi];
                    int m2 = PiB[ib][Dm[d2].pi];
                    if ((m1 & m2) == 0) {
                        if (nBad == 0) { badA = ia; badB = ib; badE = ei; badD1 = d1; }
                        nBad++;
                    } else if (!nondeg && m1 != fullMask && m2 != fullMask) {
                        nondeg = true; witA = ia; witB = ib; witE = ei; witD1 = d1;
                    }
                }
            }
        }
    }
    printf("m=%d p1=%d p2=%d t=%d |Dt|=%d nA=%d nB=%d pairs=%lld skipped=%lld preserved=%lld bad=%lld nondeg=%d side1_forced_full=%d side2_forced_full=%d\n",
           m, p1, p2, t, nDt, nA, nB, nPairs, nSkipped, nPreserved, nBad, (int)nondeg,
           (int)side1_forced_full, (int)side2_forced_full);
    auto show_seq = [&](const vector<vector<int>>& S, int idx) {
        printf("[");
        for (int j = 0; j < m; j++) printf("%d%s", S[idx][j], j + 1 < m ? "," : "");
        printf("]");
    };
    if (nBad > 0) {
        printf("FIRST BAD: A="); show_seq(SA, badA);
        printf(" B="); show_seq(SB, badB);
        printf(" d1=(eps=%d,k=%d) e=(eps=%d,k=%d) d2=(eps=%d,k=%d) Pi1mask=%d Pi2mask=%d\n",
               Dm[badD1].eps, Dm[badD1].k, Dm[badE].eps, Dm[badE].k,
               Dm[comp[badE][badD1]].eps, Dm[comp[badE][badD1]].k,
               PiA[badA][Dm[badD1].pi], PiB[badB][Dm[comp[badE][badD1]].pi]);
    }
    if (nondeg) {
        printf("NONDEG WITNESS: A="); show_seq(SA, witA);
        printf(" B="); show_seq(SB, witB);
        printf(" d1=(eps=%d,k=%d) e=(eps=%d,k=%d) Pi1mask=%d Pi2mask=%d full=%d\n",
               Dm[witD1].eps, Dm[witD1].k, Dm[witE].eps, Dm[witE].k,
               PiA[witA][Dm[witD1].pi], PiB[witB][Dm[comp[witE][witD1]].pi], fullMask);
    }
    return 0;
}
