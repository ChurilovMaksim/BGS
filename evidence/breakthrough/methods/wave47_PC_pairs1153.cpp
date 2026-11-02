// Wave 47, task 4: pair PC at (q, 1153^2) and single-component 1153^2.
// Modes:
//   pair q      -- q in {25,49,81,121,512}: every joint pair at (q,1153^2)
//                  has Pi_q & Pi_1153 != 0.
//   single1153  -- every fiber pair at 1153^2 alone has Pi_1153 != 0.
// Method (wave-44 cell method, generalized): points (yq, s) with s a trace
// sequence mod 1153; cells = (q-marginal group x s-marginal group); in a
// cell, group by pair-multiset hash, split exactly by sorted pair keys.
// In a fiber, points with identical profile-pairs share pi = s0, so only
// distinct profile-pairs are checked pairwise (exact: Pi depends only on
// profiles). Profiles at 1153^2 are mod 1153 (x -> 1153x injective).
#include <algorithm>
#include <array>
#include <atomic>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <mutex>
#include <string>
#include <thread>
#include <vector>
using std::array;
using std::vector;
static const int M = 24, P1153 = 1153;

static uint64_t sm_state = 0x9e3779b97f4a7c15ULL;
static uint64_t rnd64() {
    uint64_t z = (sm_state += 0x9e3779b97f4a7c15ULL);
    z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL;
    z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL;
    return z ^ (z >> 31);
}
static int pi_map[8][4];
static void init_pi() {
    for (int b = 0; b < 4; b++) {
        for (int r = 0; r < 4; r++) pi_map[b][r] = (r + b) % 4;
        for (int r = 0; r < 4; r++) pi_map[4 + b][r] = (4 + b - r) % 4;
    }
}
using Seq24 = array<uint16_t, M>;   // values < 1153 or < q (q<=512)
using Prof24 = array<uint16_t, M>;  // 4 classes x 6 sorted values

static vector<array<uint16_t, M>> kernel_small(int q) {
    vector<array<uint16_t, M>> out;
    for (int y0 = 0; y0 < q; y0++) for (int y1 = 0; y1 < q; y1++) {
        int y[26]; y[0] = y0; y[1] = y1;
        for (int n = 0; n < 24; n++) y[n + 2] = ((6 * y[n + 1] - y[n]) % q + q) % q;
        if (y[24] == y0 && y[25] == y1) {
            array<uint16_t, M> s; for (int i = 0; i < M; i++) s[i] = (uint16_t)y[i];
            out.push_back(s);
        }
    }
    return out;
}
static void marg_prof(const vector<array<uint16_t, M>> &seq, int p,
                      vector<array<uint16_t, M>> &marg, vector<Prof24> &prof) {
    int n = (int)seq.size();
    marg.resize(n); prof.resize(n);
    for (int k = 0; k < n; k++) {
        uint16_t v[M];
        for (int i = 0; i < M; i++) v[i] = seq[k][i];
        std::sort(v, v + M);
        for (int i = 0; i < M; i++) marg[k][i] = v[i];
        for (int r = 0; r < 4; r++) {
            uint16_t c[6]; int t = 0;
            for (int j = r; j < M; j += 4) c[t++] = seq[k][j];
            std::sort(c, c + 6);
            for (int j = 0; j < 6; j++) prof[k][r * 6 + j] = c[j];
        }
    }
}
static vector<vector<int>> group_by_marg(const vector<array<uint16_t, M>> &marg) {
    int n = (int)marg.size();
    vector<uint64_t> h(n);
    for (int k = 0; k < n; k++) {
        uint64_t x = 1469598103934665603ULL;
        for (int i = 0; i < M; i++) { x ^= marg[k][i]; x *= 1099511628211ULL; }
        h[k] = x;
    }
    vector<int> idx(n);
    for (int k = 0; k < n; k++) idx[k] = k;
    std::sort(idx.begin(), idx.end(), [&](int a, int b) { return h[a] < h[b]; });
    vector<vector<int>> groups;
    for (int i = 0; i < n;) {
        int j = i;
        while (j < n && h[idx[j]] == h[idx[i]]) j++;
        std::sort(idx.begin() + i, idx.begin() + j, [&](int a, int b) {
            return std::memcmp(marg[a].data(), marg[b].data(), sizeof(uint16_t) * M) < 0;
        });
        int k = i;
        while (k < j) {
            int l = k + 1;
            while (l < j && std::memcmp(marg[idx[k]].data(), marg[idx[l]].data(),
                                        sizeof(uint16_t) * M) == 0) l++;
            groups.push_back(vector<int>(idx.begin() + k, idx.begin() + l));
            k = l;
        }
        i = j;
    }
    return groups;
}
// Pi mask between two points given their profiles (both components if two)
static unsigned pi_mask2(const Prof24 &p1, const Prof24 &p1p,
                         const Prof24 *p2, const Prof24 *p2p) {
    unsigned m = 0;
    for (int pi = 0; pi < 8; pi++) {
        bool good = true;
        for (int r = 0; r < 4 && good; r++) {
            int pr = pi_map[pi][r];
            for (int v = 0; v < 6; v++)
                if (p1p[r * 6 + v] != p1[pr * 6 + v]) { good = false; break; }
            if (good && p2)
                for (int v = 0; v < 6; v++)
                    if ((*p2p)[r * 6 + v] != (*p2)[pr * 6 + v]) { good = false; break; }
        }
        if (good) m |= (1u << pi);
    }
    return m;
}

struct Stats {
    uint64_t points = 0, fibers = 0, pairs = 0, failures = 0, bigfib = 0;
};
static std::mutex mu;
static vector<std::string> wit;

int main(int argc, char **argv) {
    init_pi();
    if (argc < 2) { printf("usage: pair q | single1153\n"); return 1; }
    bool single = !strcmp(argv[1], "single1153");
    int q = single ? 0 : atoi(argv[1]);
    // ---- s sequences (trace) mod 1153 ----
    const int ND = P1153 * P1153;
    vector<array<uint16_t, M>> sseq(ND);
    for (int x = 0; x < P1153; x++) for (int y = 0; y < P1153; y++) {
        int d = x * P1153 + y;
        int ca = x, cb = y;
        for (int i = 0; i < M; i++) {
            sseq[d][i] = (uint16_t)((2 * ca) % P1153);
            int nca = (3 * ca + 4 * cb) % P1153, ncb = (2 * ca + 3 * cb) % P1153;
            ca = nca; cb = ncb;
        }
    }
    printf("sseq built: %d\n", ND); fflush(stdout);
    vector<array<uint16_t, M>> smarg; vector<Prof24> sprof;
    marg_prof(sseq, P1153, smarg, sprof);
    printf("s marginals/profiles done\n"); fflush(stdout);
    vector<vector<int>> sgroups = group_by_marg(smarg);
    size_t maxsg = 0; for (auto &g : sgroups) maxsg = std::max(maxsg, g.size());
    printf("s-marginal groups: %zu max %zu\n", sgroups.size(), maxsg); fflush(stdout);

    vector<array<uint16_t, M>> qseq, qmarg; vector<Prof24> qprof;
    vector<vector<int>> qgroups;
    if (!single) {
        qseq = kernel_small(q);
        marg_prof(qseq, q, qmarg, qprof);
        qgroups = group_by_marg(qmarg);
        printf("q=%d |K|=%zu groups=%zu\n", q, qseq.size(), qgroups.size()); fflush(stdout);
    }

    int nthreads = 4;
    vector<Stats> tstats(nthreads);
    if (single) {
        // fibers = s-marginal groups; check distinct profiles pairwise
        std::atomic<size_t> next_g{0};
        auto worker = [&](int tid) {
            Stats &st = tstats[tid];
            vector<int> order;
            vector<int> reps;
            while (true) {
                size_t gi = next_g.fetch_add(1);
                if (gi >= sgroups.size()) break;
                const vector<int> &g = sgroups[gi];
                if (g.size() < 2) continue;
                st.fibers++;
                // distinct profiles: sort indices by profile bytes
                order.resize(g.size());
                for (size_t i = 0; i < g.size(); i++) order[i] = (int)i;
                std::sort(order.begin(), order.end(), [&](int a, int b) {
                    return std::memcmp(sprof[g[a]].data(), sprof[g[b]].data(),
                                       sizeof(uint16_t) * M) < 0;
                });
                reps.clear();
                for (size_t i = 0; i < order.size();) {
                    size_t j = i + 1;
                    while (j < order.size() &&
                           std::memcmp(sprof[g[order[i]]].data(), sprof[g[order[j]]].data(),
                                       sizeof(uint16_t) * M) == 0) j++;
                    reps.push_back(g[order[i]]);
                    i = j;
                }
                if (reps.size() > 64) st.bigfib++;
                for (size_t a = 0; a < reps.size(); a++)
                    for (size_t b = a + 1; b < reps.size(); b++) {
                        st.pairs++;
                        if (!pi_mask2(sprof[reps[a]], sprof[reps[b]], nullptr, nullptr)) {
                            st.failures++;
                            std::lock_guard<std::mutex> lk(mu);
                            if (wit.size() < 5) {
                                char buf[256];
                                snprintf(buf, sizeof(buf), "FAIL single1153 D=(%d,%d)",
                                         reps[a], reps[b]);
                                wit.push_back(buf);
                            }
                        }
                    }
            }
        };
        vector<std::thread> th;
        for (int t = 0; t < nthreads; t++) th.emplace_back(worker, t);
        for (auto &t : th) t.join();
    } else {
        // cells: (tg, sg)
        const int NP = q * P1153;
        vector<uint64_t> R1(NP), R2(NP);
        for (int i = 0; i < NP; i++) { R1[i] = rnd64(); R2[i] = rnd64(); }
        size_t ncells = qgroups.size() * sgroups.size();
        std::atomic<size_t> next_cell{0};
        auto worker = [&](int tid) {
            Stats &st = tstats[tid];
            vector<std::tuple<uint64_t, uint64_t, int, int>> items;
            vector<array<int, M>> keys;
            vector<int> order;
            while (true) {
                size_t ci = next_cell.fetch_add(1);
                if (ci >= ncells) break;
                size_t tg = ci / sgroups.size(), sg = ci % sgroups.size();
                const vector<int> &T = qgroups[tg], &S = sgroups[sg];
                items.clear();
                items.reserve(T.size() * S.size());
                for (int c : T) for (int d : S) {
                    uint64_t h1 = 0, h2 = 0;
                    for (int i = 0; i < M; i++) {
                        int key = (int)qseq[c][i] * P1153 + sseq[d][i];
                        h1 += R1[key]; h2 += R2[key];
                    }
                    items.emplace_back(h1, h2, c, d);
                }
                st.points += items.size();
                std::sort(items.begin(), items.end(), [](const auto &a, const auto &b) {
                    if (std::get<0>(a) != std::get<0>(b)) return std::get<0>(a) < std::get<0>(b);
                    return std::get<1>(a) < std::get<1>(b);
                });
                size_t i = 0;
                while (i < items.size()) {
                    size_t j = i + 1;
                    while (j < items.size() && std::get<0>(items[j]) == std::get<0>(items[i]) &&
                           std::get<1>(items[j]) == std::get<1>(items[i])) j++;
                    keys.assign(j - i, {});
                    for (size_t k = i; k < j; k++) {
                        int c = std::get<2>(items[k]), d = std::get<3>(items[k]);
                        array<int, M> &ky = keys[k - i];
                        for (int t = 0; t < M; t++) ky[t] = (int)qseq[c][t] * P1153 + sseq[d][t];
                        std::sort(ky.begin(), ky.end());
                    }
                    order.resize(j - i);
                    for (size_t k = 0; k < j - i; k++) order[k] = (int)k;
                    std::sort(order.begin(), order.end(), [&](int a, int b) { return keys[a] < keys[b]; });
                    size_t a = 0;
                    while (a < order.size()) {
                        size_t b = a + 1;
                        while (b < order.size() && keys[order[b]] == keys[order[a]]) b++;
                        if (b - a >= 2) {
                            st.fibers++;
                            // distinct profile-pairs
                            vector<int> reps;
                            vector<int> o2(order.begin() + a, order.begin() + b);
                            std::sort(o2.begin(), o2.end(), [&](int x, int y) {
                                int cx = std::get<2>(items[i + x]), dx = std::get<3>(items[i + x]);
                                int cy = std::get<2>(items[i + y]), dy = std::get<3>(items[i + y]);
                                int cq = std::memcmp(qprof[cx].data(), qprof[cy].data(), sizeof(uint16_t) * M);
                                if (cq) return cq < 0;
                                return std::memcmp(sprof[dx].data(), sprof[dy].data(), sizeof(uint16_t) * M) < 0;
                            });
                            for (size_t t = 0; t < o2.size();) {
                                size_t u = t + 1;
                                while (u < o2.size()) {
                                    int cx = std::get<2>(items[i + o2[t]]), dx = std::get<3>(items[i + o2[t]]);
                                    int cy = std::get<2>(items[i + o2[u]]), dy = std::get<3>(items[i + o2[u]]);
                                    if (std::memcmp(qprof[cx].data(), qprof[cy].data(), sizeof(uint16_t) * M) == 0 &&
                                        std::memcmp(sprof[dx].data(), sprof[dy].data(), sizeof(uint16_t) * M) == 0) u++;
                                    else break;
                                }
                                reps.push_back(o2[t]);
                                t = u;
                            }
                            if (reps.size() > 64) st.bigfib++;
                            for (size_t x = 0; x < reps.size(); x++)
                                for (size_t y = x + 1; y < reps.size(); y++) {
                                    int c1 = std::get<2>(items[i + reps[x]]), d1 = std::get<3>(items[i + reps[x]]);
                                    int c2 = std::get<2>(items[i + reps[y]]), d2 = std::get<3>(items[i + reps[y]]);
                                    st.pairs++;
                                    if (!pi_mask2(qprof[c1], qprof[c2], &sprof[d1], &sprof[d2])) {
                                        st.failures++;
                                        std::lock_guard<std::mutex> lk(mu);
                                        if (wit.size() < 5) {
                                            char buf[256];
                                            snprintf(buf, sizeof(buf),
                                                     "FAIL pair q=%d (c=%d,d=%d) vs (c=%d,d=%d)",
                                                     q, c1, d1, c2, d2);
                                            wit.push_back(buf);
                                        }
                                    }
                                }
                        }
                        a = b;
                    }
                    i = j;
                }
            }
        };
        vector<std::thread> th;
        for (int t = 0; t < nthreads; t++) th.emplace_back(worker, t);
        for (auto &t : th) t.join();
    }
    Stats tot;
    for (auto &s : tstats) {
        tot.points += s.points; tot.fibers += s.fibers; tot.pairs += s.pairs;
        tot.failures += s.failures; tot.bigfib += s.bigfib;
    }
    printf("POINTS %llu FIBERS %llu PAIRS %llu FAILURES %llu BIGFIB %llu\n",
           (unsigned long long)tot.points, (unsigned long long)tot.fibers,
           (unsigned long long)tot.pairs, (unsigned long long)tot.failures,
           (unsigned long long)tot.bigfib);
    for (auto &w : wit) printf("%s\n", w.c_str());
    printf("DONE\n");
    return tot.failures == 0 ? 0 : 2;
}
