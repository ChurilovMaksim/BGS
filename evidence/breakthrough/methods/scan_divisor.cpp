// Wave 7 task 4: for given (m, d), enumerate ker(H_m mod d) and report
// the worst fiber splitting under dihedral and affine canons.
// Enumeration: (v0,v1) = (a,b) with (A^m - I)(a,b)^T = 0 mod d, A=[[0,1],[-1,6]],
// iterating a and solving the linear congruence for b (no d^2 scan).
// H = 6I - C - C^T, i.e. v_{i+1} = 6 v_i - v_{i-1} cyclically.
// Action convention: (p.y)_j = y_{p(j)}, p(j) = a*j + b (affine) or +-j + b (dihedral).
#include <bits/stdc++.h>
using namespace std;
using i128 = __int128_t;
int main(int argc, char** argv) {
    if (argc < 3) { cerr << "usage: scan_divisor m d\n"; return 2; }
    int m = atoi(argv[1]);
    long long d = atoll(argv[2]);
    if (m < 1 || d < 2) { cerr << "bad args\n"; return 2; }
    // A^m mod d
    long long A00 = 1, A01 = 0, A10 = 0, A11 = 1; // result
    long long B00 = 0, B01 = 1, B10 = -1, B11 = 6; // base, mod d handled below
    auto modnorm = [&](long long x) { long long r = x % d; return r < 0 ? r + d : r; };
    B00 = modnorm(B00); B01 = modnorm(B01); B10 = modnorm(B10); B11 = modnorm(B11);
    int n = m;
    while (n) {
        if (n & 1) {
            long long N00 = (long long)((i128)A00 * B00 + (i128)A01 * B10) % d;
            long long N01 = (long long)((i128)A00 * B01 + (i128)A01 * B11) % d;
            long long N10 = (long long)((i128)A10 * B00 + (i128)A11 * B10) % d;
            long long N11 = (long long)((i128)A10 * B01 + (i128)A11 * B11) % d;
            A00 = N00; A01 = N01; A10 = N10; A11 = N11;
        }
        long long N00 = (long long)((i128)B00 * B00 + (i128)B01 * B10) % d;
        long long N01 = (long long)((i128)B00 * B01 + (i128)B01 * B11) % d;
        long long N10 = (long long)((i128)B10 * B00 + (i128)B11 * B10) % d;
        long long N11 = (long long)((i128)B10 * B01 + (i128)B11 * B11) % d;
        B00 = N00; B01 = N01; B10 = N10; B11 = N11;
        n >>= 1;
    }
    long long P = modnorm(A00 - 1), Q = A01, R = A10, S = modnorm(A11 - 1);
    vector<vector<int>> vecs;
    for (long long a = 0; a < d; ++a) {
        long long rhs = modnorm(-P * (a % d));
        long long g = std::gcd(Q, d);
        if (rhs % g != 0) continue;
        long long Qr = Q / g, qr = d / g;
        long long b0 = 0;
        if (qr > 1) {
            long long inv = 0;
            // inverse of Qr mod qr (coprime)
            long long t = 0, nt = 1, r = qr, nr = modnorm(Qr);
            while (nr != 0) {
                long long qq = r / nr;
                long long tt = t - qq * nt; t = nt; nt = tt;
                long long rr = r - qq * nr; r = nr; nr = rr;
            }
            inv = modnorm(t);
            b0 = (long long)((i128)(rhs / g) * inv) % qr;
        }
        for (long long k = 0; k < g; ++k) {
            long long b = b0 + k * qr;
            if (modnorm(R * a + S * b) != 0) continue;
            vector<int> y(m);
            if (m >= 1) y[0] = (int)a;
            if (m >= 2) y[1] = (int)b;
            for (int i = 1; i < m - 1; ++i)
                y[i + 1] = (int)modnorm(6LL * y[i] - y[i - 1]);
            // verify Hv = 0 mod d
            bool ok = true;
            for (int i = 0; i < m; ++i) {
                if (modnorm(6LL * y[i] - y[(i - 1 + m) % m] - y[(i + 1) % m]) != 0) { ok = false; break; }
            }
            if (!ok) { cerr << "H-check failed\n"; return 3; }
            vecs.push_back(move(y));
            if (vecs.size() > 3000000) { cout << "{\"m\":" << m << ",\"d\":" << d << ",\"skipped\":\"too_many_vectors\"}\n"; return 0; }
        }
    }
    // perms
    vector<vector<int>> dperms, aperms;
    for (int b = 0; b < m; ++b) {
        vector<int> r(m), f(m);
        for (int j = 0; j < m; ++j) { r[j] = (j + b) % m; f[j] = (b - j + m) % m; }
        dperms.push_back(r); dperms.push_back(f);
    }
    sort(dperms.begin(), dperms.end());
    dperms.erase(unique(dperms.begin(), dperms.end()), dperms.end());
    for (int a = 0; a < m; ++a) if (std::gcd(a, m) == 1)
        for (int b = 0; b < m; ++b) {
            vector<int> p(m);
            for (int j = 0; j < m; ++j) p[j] = (a * j + b) % m;
            aperms.push_back(p);
        }
    auto canon = [&](const vector<int>& v, const vector<vector<int>>& perms) {
        vector<int> best;
        bool first = true;
        for (auto& p : perms) {
            vector<int> cand(m);
            for (int j = 0; j < m; ++j) cand[j] = v[p[j]];
            if (first || cand < best) { best = cand; first = false; }
        }
        return best;
    };
    struct KeyHash {
        size_t operator()(vector<int> const& c) const noexcept {
            uint64_t h = 1469598103934665603ULL;
            for (int x : c) { h ^= (uint64_t)(x + 1000003); h *= 1099511628211ULL; }
            return (size_t)h;
        }
    };
    unordered_map<vector<int>, vector<vector<int>>, KeyHash> fib_d;
    unordered_map<vector<int>, vector<vector<int>>, KeyHash> fib_a;
    unordered_map<vector<int>, int, KeyHash> fib_size;
    for (auto& v : vecs) {
        vector<int> s = v;
        sort(s.begin(), s.end());
        fib_size[s]++;
        auto dc = canon(v, dperms);
        auto& ld = fib_d[s];
        if (find(ld.begin(), ld.end(), dc) == ld.end()) ld.push_back(dc);
        auto ac = canon(v, aperms);
        auto& la = fib_a[s];
        if (find(la.begin(), la.end(), ac) == la.end()) la.push_back(ac);
    }
    int maxd = 0, maxa = 0, nbad_d = 0, nbad_a = 0;
    vector<int> worst_s;
    for (auto& kv : fib_d) {
        int kd = (int)kv.second.size();
        int ka = (int)fib_a[kv.first].size();
        if (kd > 1) ++nbad_d;
        if (ka > 1) ++nbad_a;
        if (kd > maxd) { maxd = kd; worst_s = kv.first; }
        if (ka > maxa) maxa = ka;
    }
    cout << "{\"m\":" << m << ",\"d\":" << d << ",\"n_fix\":" << vecs.size()
         << ",\"n_fibers\":" << fib_d.size()
         << ",\"max_dih_canons\":" << maxd << ",\"max_aff_canons\":" << maxa
         << ",\"bad_dih_fibers\":" << nbad_d << ",\"bad_aff_fibers\":" << nbad_a;
    if (maxd > 1) {
        cout << ",\"worst_sorted\":[";
        for (int i = 0; i < m; ++i) cout << worst_s[i] << (i + 1 < m ? "," : "");
        cout << "],\"worst_fiber_size\":" << fib_size[worst_s];
    }
    cout << "}\n";
    return 0;
}
