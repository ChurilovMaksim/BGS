// Wave 7 task 4: Gamma-orbits per fiber at m=9, global check.
// Global vector = pair (v49, v39601) (+ constant mod-4 component, fixed
// to 0: adding a constant to all packed keys preserves order, so the
// splitting counts are identical for every mod-4 constant).
// Packed key per position: v49 + 49*v39601 (injective).
// For every pair, compute sorted key and dihedral canon (lex min over
// the 18 dihedral perms); count distinct dihedral canons per sorted key.
#include <bits/stdc++.h>
using namespace std;
const int M = 9;
using Vec = array<int, M>;
struct KeyHash {
    size_t operator()(Vec const& c) const noexcept {
        uint64_t h = 1469598103934665603ULL;
        for (int i = 0; i < M; ++i) { h ^= (uint64_t)(c[i] + 1000003); h *= 1099511628211ULL; }
        return (size_t)h;
    }
};
vector<Vec> read_vecs(const string& path) {
    vector<Vec> out; ifstream in(path);
    if (!in) { cerr << "cannot open " << path << "\n"; exit(2); }
    Vec v;
    while (true) {
        for (int j = 0; j < M; ++j) if (!(in >> v[j])) {
            if (j == 0) return out;
            cerr << "truncated line\n"; exit(2);
        }
        out.push_back(v);
    }
}
void isort9(array<int, M>& a) {
    for (int i = 1; i < M; ++i) {
        int x = a[i], j = i - 1;
        while (j >= 0 && a[j] > x) { a[j+1] = a[j]; --j; }
        a[j+1] = x;
    }
}
int main(int argc, char** argv) {
    string dir = (argc > 1) ? argv[1] : ".";
    auto v49s = read_vecs(dir + "/m9_q49.txt");
    auto v39601s = read_vecs(dir + "/m9_q39601.txt");
    cerr << "loaded " << v49s.size() << " " << v39601s.size() << "\n";
    vector<array<int, M>> dperms;
    for (int b = 0; b < M; ++b) {
        array<int, M> r, f;
        for (int j = 0; j < M; ++j) { r[j] = (j + b) % M; f[j] = (b - j + M) % M; }
        dperms.push_back(r); dperms.push_back(f);
    }
    sort(dperms.begin(), dperms.end());
    dperms.erase(unique(dperms.begin(), dperms.end()), dperms.end());
    cerr << "dihedral perms=" << dperms.size() << "\n";
    unordered_map<Vec, vector<Vec>, KeyHash> fibers;
    fibers.reserve(1000000);
    long long pairs = 0;
    for (auto& v49 : v49s) {
        for (auto& v39 : v39601s) {
            ++pairs;
            Vec t;
            for (int j = 0; j < M; ++j) t[j] = v49[j] + 49 * v39[j];
            Vec s = t; isort9(s);
            Vec dc; bool first = true;
            for (auto& p : dperms) {
                Vec cand;
                for (int j = 0; j < M; ++j) cand[j] = t[p[j]];
                if (first || cand < dc) { dc = cand; first = false; }
            }
            auto& lst = fibers[s];
            if (find(lst.begin(), lst.end(), dc) == lst.end()) lst.push_back(dc);
        }
    }
    map<int, long long> dist;
    long long nfib = 0, maxcan = 0;
    for (auto& kv : fibers) {
        ++nfib;
        int k = (int)kv.second.size();
        dist[k]++;
        if (k > maxcan) maxcan = k;
    }
    cout << "{\n  \"m\": 9, \"pairs\": " << pairs << ", \"fibers\": " << nfib
         << ", \"max_dihedral_canons_per_fiber\": " << maxcan << "\n";
    for (auto& kv : dist) cout << "  ,\"fibers_with_" << kv.first << "_canons\": " << kv.second << "\n";
    cout << "}\n";
    return 0;
}
