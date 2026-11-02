// Wave 10, task 2: P=32 pattern affine test + m=32 joint-lift exact search.
// (A) Enumerate Fix_32 mod 8192 by seed scan, group by sorted multiset,
//     check per ordered pair: dihedral tau exists? affine tau exists?
//     class sums (mod 4) in single D4 orbit?
// (B) Joint lifts at m=32 with other components zero: q2=8192, q3=9,
//     CRT to D32 ( __int128 ), group by sorted multiset, check exact Y
//     in single D4 orbit.
#include <bits/stdc++.h>
using namespace std;
using i128 = __int128_t;
using u128 = __uint128_t;

string toString(i128 v) {
    if (v == 0) return "0";
    bool neg = v < 0; if (neg) v = -v;
    string s; while (v > 0) { s.push_back('0' + int(v % 10)); v /= 10; }
    if (neg) s.push_back('-');
    reverse(s.begin(), s.end()); return s;
}

int main() {
    const int P = 32;
    const int q = 8192;
    // ---- (A) seed scan ----
    vector<vector<int>> vecs;
    vecs.reserve(q);
    for (int y0 = 0; y0 < q; ++y0) {
        for (int y1 = 0; y1 < q; ++y1) {
            int a = y0, b = y1;
            int seq[34];
            seq[0] = y0; seq[1] = y1;
            for (int k = 2; k <= P+1; ++k) {
                int c = (6*b - a) % q; if (c < 0) c += q;
                seq[k] = c; a = b; b = c;
            }
            if (seq[P] == y0 && seq[P+1] == y1) {
                vector<int> v(P);
                for (int k = 0; k < P; ++k) v[k] = seq[k];
                vecs.push_back(move(v));
            }
        }
    }
    printf("(A) P=%d q=%d |Fix|=%zu (expect %d)\n", P, q, vecs.size(), q);
    // group by sorted multiset
    map<vector<int>, vector<int>> groups; // sorted -> indices
    for (int i = 0; i < (int)vecs.size(); ++i) {
        vector<int> s = vecs[i];
        sort(s.begin(), s.end());
        groups[s].push_back(i);
    }
    printf("    groups=%zu\n", groups.size());
    auto classSums = [&](const vector<int>& v) {
        array<int,4> Y = {0,0,0,0};
        for (int j = 0; j < P; ++j) Y[j%4] += v[j];
        return Y;
    };
    auto d4orbit = [&](array<int,4> v) {
        set<array<int,4>> out;
        for (int b = 0; b < 4; ++b) {
            array<int,4> r, f;
            for (int i = 0; i < 4; ++i) { r[i] = v[(i+b)%4]; f[i] = v[(-i+b+8)%4]; }
            out.insert(r); out.insert(f);
        }
        return out;
    };
    // tau existence via first-two-position candidates
    auto exists_map = [&](const vector<int>& p, const vector<int>& pp,
                          const vector<pair<int,int>>& maps) {
        // maps: list of (a,b) with tau(j)=(a*j+b)%P ; caller gives full list
        for (auto [a,b] : maps) {
            bool ok = true;
            for (int j = 0; j < P; ++j) if (pp[j] != p[(a*j+b)%P]) { ok = false; break; }
            if (ok) return true;
        }
        return false;
    };
    vector<pair<int,int>> dih, aff;
    for (int b = 0; b < P; ++b) { dih.push_back({1,b}); dih.push_back({P-1,b}); }
    for (int a = 1; a < P; a += 2) for (int b = 0; b < P; ++b) aff.push_back({a,b});
    long long total_pairs = 0, dih_fail = 0, aff_fail = 0, weak_fail = 0;
    for (auto& [ms, idxs] : groups) {
        // weak: class sums single D4 orbit?
        auto Y0 = classSums(vecs[idxs[0]]);
        auto orb = d4orbit(Y0);
        for (int id : idxs) if (!orb.count(classSums(vecs[id]))) { weak_fail++; break; }
        for (int ii : idxs) for (int jj : idxs) {
            if (ii == jj) continue;
            total_pairs++;
            const auto& p = vecs[ii]; const auto& pp = vecs[jj];
            if (!exists_map(p, pp, dih)) dih_fail++;
            if (!exists_map(p, pp, aff)) aff_fail++;
        }
    }
    printf("    ordered distinct pairs=%lld dihedral-fail=%lld affine-fail=%lld weak-fail-groups=%lld\n",
           total_pairs, dih_fail, aff_fail, weak_fail);

    // ---- (B) joint lifts m=32, q2=8192, q3=9, other components 0 ----
    // D32 = 3145168096065837266706432 ; factor 2^13 * 3^2 * 17^2 * 577^2 * 665857^2
    i128 D32 = 0;
    { const char* s = "3145168096065837266706432"; for (const char* p = s; *p; ++p) D32 = D32*10 + (*p - '0'); }
    // Fix mod 9, m=32, by seed scan
    vector<vector<int>> v9;
    for (int y0 = 0; y0 < 9; ++y0) for (int y1 = 0; y1 < 9; ++y1) {
        int a = y0, b = y1, seq[34]; seq[0]=y0; seq[1]=y1;
        for (int k = 2; k <= 33; ++k) { int c = (6*b - a) % 9; if (c<0) c+=9; seq[k]=c; a=b; b=c; }
        if (seq[32]==y0 && seq[33]==y1) { vector<int> v(32); for (int k=0;k<32;++k) v[k]=seq[k]; v9.push_back(v); }
    }
    printf("(B) Fix mod 9: %zu (expect 9)\n", v9.size());
    auto crt_coeff = [&](long long qq) -> i128 {
        i128 Dj = D32 / qq;
        // inverse of Dj mod qq (qq small)
        long long Djmod = (long long)(Dj % qq);
        long long inv = 1; for (long long x = 1; x < qq; ++x) if ((Djmod*x)%qq==1) { inv=x; break; }
        return (Dj * (i128)inv) % D32;
    };
    i128 c2 = crt_coeff(8192), c3 = crt_coeff(9);
    struct Lift { vector<i128> sorted; array<i128,4> Y; };
    vector<Lift> lifts;
    lifts.reserve(vecs.size()*v9.size());
    for (auto& z2 : vecs) for (auto& z3 : v9) {
        vector<i128> y(32);
        for (int i = 0; i < 32; ++i) y[i] = (c2*(i128)z2[i] + c3*(i128)z3[i]) % D32;
        vector<i128> s = y; sort(s.begin(), s.end());
        array<i128,4> Y = {0,0,0,0};
        for (int i = 0; i < 32; ++i) Y[i%4] += y[i];
        lifts.push_back({move(s), Y});
    }
    sort(lifts.begin(), lifts.end(), [](const Lift& A, const Lift& B){ return A.sorted < B.sorted; });
    long long ngroups = 0, npairs = 0, fails = 0;
    for (size_t i = 0; i < lifts.size(); ) {
        size_t j = i;
        while (j < lifts.size() && lifts[j].sorted == lifts[i].sorted) ++j;
        ngroups++;
        // D4 orbit of first Y
        set<array<i128,4>> orb;
        auto Y0 = lifts[i].Y;
        for (int b = 0; b < 4; ++b) {
            array<i128,4> r, f;
            for (int k = 0; k < 4; ++k) { r[k] = Y0[(k+b)%4]; f[k] = Y0[(-k+b+8)%4]; }
            orb.insert(r); orb.insert(f);
        }
        for (size_t k = i+1; k < j; ++k) {
            npairs++;
            if (!orb.count(lifts[k].Y)) fails++;
        }
        i = j;
    }
    printf("    lifts=%zu groups=%lld pairs=%lld EXACT FAILURES=%lld\n", lifts.size(), ngroups, npairs, fails);
    return 0;
}
