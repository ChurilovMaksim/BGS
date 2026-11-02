// Wave 5 task 1: C++ gluing search for the remaining m=10 cases.
// Remaining set: q841 component non-distinct AND (q32 constant OR
// q1681 pattern (first 5 values, period 5) non-distinct).
// Tag A (q841 distinct) and Tag B (q32 non-const + pattern distinct)
// cover all other global vectors by short arguments (see note).
// Per-component separation holds and A(v)=D(v) for all components
// (verified in Python), so every candidate in the same global fiber is
// a dihedral-effect combination (w32, w841, w1681), w_i in D(v_i).
// Search is over global dihedral-orbit representatives only (canon in
// packed-triple order; the remaining set is dihedral-invariant).
// A hit = sorted(candidate triples) == sorted(base triples) AND
// affine canon(candidate) != affine canon(base) in packed order.
// Packing (injective): key = v32 + (v841<<5) + (v1681<<15)  (26 bits).
#include <bits/stdc++.h>
using namespace std;
const int M = 10;
using Vec = array<int, M>;
using Canon = array<uint32_t, M>;

struct CanonHash {
    size_t operator()(Canon const& c) const noexcept {
        uint64_t h = 1469598103934665603ULL;
        for (int i = 0; i < M; ++i) { h ^= c[i]; h *= 1099511628211ULL; }
        return (size_t)h;
    }
};

vector<Vec> read_vecs(const string& path) {
    vector<Vec> out;
    ifstream in(path);
    if (!in) { cerr << "cannot open " << path << "\n"; exit(2); }
    Vec v;
    while (true) {
        for (int j = 0; j < M; ++j) if (!(in >> v[j])) {
            if (j == 0) return out;
            cerr << "truncated line in " << path << "\n"; exit(2);
        }
        out.push_back(v);
    }
}

int distinct_count(const Vec& v) {
    int s[10]; for (int j = 0; j < M; ++j) s[j] = v[j];
    sort(s, s + M);
    int c = 1; for (int j = 1; j < M; ++j) if (s[j] != s[j-1]) ++c;
    return c;
}

vector<array<int, M>> dihedral_perms() {
    vector<array<int, M>> ps;
    for (int b = 0; b < M; ++b) {
        array<int, M> r, f;
        for (int j = 0; j < M; ++j) { r[j] = (j + b) % M; f[j] = (b - j + M) % M; }
        ps.push_back(r); ps.push_back(f);
    }
    sort(ps.begin(), ps.end());
    ps.erase(unique(ps.begin(), ps.end()), ps.end());
    return ps;
}

vector<array<int, M>> affine_perms() {
    vector<array<int, M>> ps;
    for (int a : {1, 3, 7, 9}) for (int b = 0; b < M; ++b) {
        array<int, M> p;
        for (int j = 0; j < M; ++j) p[j] = (a * j + b) % M;
        ps.push_back(p);
    }
    return ps;
}

Vec apply_perm(const Vec& v, const array<int, M>& p) {
    Vec w; for (int j = 0; j < M; ++j) w[j] = v[p[j]]; return w;
}

vector<Vec> D_list(const Vec& v, const vector<array<int, M>>& dperms) {
    vector<Vec> out;
    for (auto& p : dperms) {
        Vec w = apply_perm(v, p);
        if (find(out.begin(), out.end(), w) == out.end()) out.push_back(w);
    }
    return out;
}

Canon canon_of(const array<uint32_t, M>& triples,
               const vector<array<int, M>>& perms) {
    Canon best; bool first = true;
    for (auto& p : perms) {
        Canon cand;
        for (int j = 0; j < M; ++j) cand[j] = triples[p[j]];
        if (first || cand < best) { best = cand; first = false; }
    }
    return best;
}

void isort10(array<uint32_t, M>& a) {
    for (int i = 1; i < M; ++i) {
        uint32_t x = a[i]; int j = i - 1;
        while (j >= 0 && a[j] > x) { a[j+1] = a[j]; --j; }
        a[j+1] = x;
    }
}

int main(int argc, char** argv) {
    string dir = (argc > 1) ? argv[1] : ".";
    auto v32s = read_vecs(dir + "/m10_q32.txt");
    auto v841s = read_vecs(dir + "/m10_q841.txt");
    auto v1681s = read_vecs(dir + "/m10_q1681.txt");
    cerr << "loaded " << v32s.size() << " " << v841s.size() << " " << v1681s.size() << "\n";
    // sanity: periods
    for (auto& v : v32s) for (int j = 0; j < M; ++j)
        if (v[j] != v[(j + 2) % M]) { cerr << "q32 not period2\n"; return 2; }
    for (auto& v : v1681s) for (int j = 0; j < M; ++j)
        if (v[j] != v[(j + 5) % M]) { cerr << "q1681 not period5\n"; return 2; }
    auto dperms = dihedral_perms();
    auto aperms = affine_perms();
    cerr << "dihedral perms=" << dperms.size() << " affine perms=" << aperms.size() << "\n";
    // per-vector data
    vector<vector<Vec>> D32(v32s.size()), D841(v841s.size()), D1681(v1681s.size());
    vector<int> dist32(v32s.size()), dist841(v841s.size()), pat1681(v1681s.size());
    for (size_t i = 0; i < v32s.size(); ++i) { D32[i] = D_list(v32s[i], dperms); dist32[i] = distinct_count(v32s[i]); }
    for (size_t i = 0; i < v841s.size(); ++i) { D841[i] = D_list(v841s[i], dperms); dist841[i] = distinct_count(v841s[i]); }
    for (size_t i = 0; i < v1681s.size(); ++i) {
        D1681[i] = D_list(v1681s[i], dperms);
        int s[5]; for (int j = 0; j < 5; ++j) s[j] = v1681s[i][j];
        sort(s, s + 5); int c = 1; for (int j = 1; j < 5; ++j) if (s[j] != s[j-1]) ++c;
        pat1681[i] = c;
    }
    struct Rep {
        int i32, i841, i1681;
        array<uint32_t, M> base_sorted;
        Canon base_aff_canon;
        array<uint32_t, M> base_triples;
    };
    vector<Rep> reps;
    unordered_map<Canon, int, CanonHash> seen;
    seen.reserve(4000000);
    long long remaining = 0;
    auto t0 = chrono::steady_clock::now();
    for (size_t i32 = 0; i32 < v32s.size(); ++i32) {
        bool const32 = (dist32[i32] == 1);
        for (size_t i841 = 0; i841 < v841s.size(); ++i841) {
            if (dist841[i841] == M) continue; // Tag A covers
            for (size_t i1681 = 0; i1681 < v1681s.size(); ++i1681) {
                if (!const32 && pat1681[i1681] == 5) continue; // Tag B covers
                ++remaining;
                array<uint32_t, M> trip;
                for (int j = 0; j < M; ++j)
                    trip[j] = (uint32_t)v32s[i32][j] | ((uint32_t)v841s[i841][j] << 5) | ((uint32_t)v1681s[i1681][j] << 15);
                Canon dc = canon_of(trip, dperms);
                auto it = seen.find(dc);
                if (it != seen.end()) continue;
                seen.emplace(dc, (int)reps.size());
                Rep r; r.i32 = (int)i32; r.i841 = (int)i841; r.i1681 = (int)i1681; r.base_triples = trip;
                r.base_sorted = trip; isort10(r.base_sorted);
                r.base_aff_canon = canon_of(trip, aperms);
                reps.push_back(r);
            }
        }
        if (i32 % 8 == 0) {
            auto t1 = chrono::steady_clock::now();
            cerr << "i32=" << i32 << " remaining=" << remaining << " reps=" << reps.size()
                 << " elapsed=" << chrono::duration_cast<chrono::seconds>(t1 - t0).count() << "s\n";
        }
    }
    cerr << "remaining=" << remaining << " representatives=" << reps.size() << "\n";
    long long combos = 0;
    struct Hit { Rep rep; Vec w32, w841, w1681; Canon cand_aff_canon; array<uint32_t, M> cand_sorted; };
    vector<Hit> hits;
    bool done = false;
    for (auto& r : reps) {
        if (done) break;
        for (auto& w32 : D32[r.i32]) {
            if (done) break;
            for (auto& w841 : D841[r.i841]) {
                if (done) break;
                for (auto& w1681 : D1681[r.i1681]) {
                    ++combos;
                    array<uint32_t, M> cand;
                    for (int j = 0; j < M; ++j)
                        cand[j] = (uint32_t)w32[j] | ((uint32_t)w841[j] << 5) | ((uint32_t)w1681[j] << 15);
                    array<uint32_t, M> srt = cand; isort10(srt);
                    if (srt != r.base_sorted) continue;
                    Canon cc = canon_of(cand, aperms);
                    if (cc == r.base_aff_canon) continue;
                    Hit h; h.rep = r; h.w32 = w32; h.w841 = w841; h.w1681 = w1681; h.cand_aff_canon = cc; h.cand_sorted = srt;
                    hits.push_back(h);
                    cerr << "HIT rep=(" << r.i32 << "," << r.i841 << "," << r.i1681 << ")\n";
                    if (hits.size() >= 3) { done = true; break; }
                }
            }
        }
    }
    auto t1 = chrono::steady_clock::now();
    cout << "{\n  \"m\": 10, \"remaining_y\": " << remaining
         << ", \"representatives\": " << reps.size()
         << ", \"combos_checked\": " << combos
         << ", \"hits\": " << hits.size()
         << ", \"seconds\": " << chrono::duration_cast<chrono::seconds>(t1 - t0).count() << "\n";
    for (size_t k = 0; k < hits.size(); ++k) {
        auto& h = hits[k];
        cout << "  ,\"hit" << k << "\": {\"rep\": [" << h.rep.i32 << "," << h.rep.i841 << "," << h.rep.i1681 << "]"
             << ", \"w32\": ["; for (int j = 0; j < M; ++j) cout << h.w32[j] << (j+1<M?",":"");
        cout << "], \"w841\": ["; for (int j = 0; j < M; ++j) cout << h.w841[j] << (j+1<M?",":"");
        cout << "], \"w1681\": ["; for (int j = 0; j < M; ++j) cout << h.w1681[j] << (j+1<M?",":"");
        cout << "], \"cand_aff_canon\": ["; for (int j = 0; j < M; ++j) cout << h.cand_aff_canon[j] << (j+1<M?",":"");
        cout << "], \"base_aff_canon\": ["; for (int j = 0; j < M; ++j) cout << h.rep.base_aff_canon[j] << (j+1<M?",":"");
        cout << "]}\n";
    }
    cout << "}\n";
    return 0;
}
