// Wave 47, task 4: triple Pi intersections for PC at m=24.
// Modes:
//   pairs qa qb     -- joint pairs at (qa,qb)
//   triple qa qb qc src -- joint triples at (qa,qb,qc); src = preferred
//                          sigma-source component (must be one of qa,qb,qc)
// Method: for a base tuple, pick the first non-constant component as the
// sigma-source (all-constant bases have only the diagonal mate). Loop over
// mates at the source; enumerate value-preserving bijections sigma by
// backtracking, recurrence-pruned for the other components. mate =
// base o sigma componentwise, so the joint condition (equal multiset of
// value-tuples) holds by construction, and every joint tuple arises this
// way. Pi masks are precomputed per fiber pair; a joint tuple fails iff
// the AND of its Pi masks is 0. Node cap + exact direct fallback covers
// highly symmetric sources.
#include <algorithm>
#include <array>
#include <atomic>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <mutex>
#include <string>
#include <thread>
#include <vector>
using std::array;
using std::vector;
using Seq = array<short, 24>;
using Prof = array<array<short, 6>, 4>;

static vector<array<int, 4>> D4maps() {
    vector<array<int, 4>> v;
    for (int b = 0; b < 4; b++) {
        array<int, 4> s, f;
        for (int r = 0; r < 4; r++) { s[r] = (r + b) % 4; f[r] = ((-r + b) % 4 + 4) % 4; }
        v.push_back(s); v.push_back(f);
    }
    std::sort(v.begin(), v.end());
    v.erase(std::unique(v.begin(), v.end()), v.end());
    return v;
}
static vector<array<int, 4>> D4;

struct Comp {
    int q = 0;
    vector<Seq> K;
    vector<int> fib;
    vector<vector<int>> fibers;
    vector<Prof> P;
    vector<vector<unsigned char>> mask;  // mask[i][j], 0 if different fiber
    std::map<Seq, int> idx;
    vector<vector<int>> head;            // per element: size q, first pos of value v
    vector<array<int, 24>> nxt;          // per element: next pos with same value
};

static Comp build_comp(int q) {
    Comp C; C.q = q;
    for (int y0 = 0; y0 < q; y0++) for (int y1 = 0; y1 < q; y1++) {
        int y[26]; y[0] = y0; y[1] = y1;
        for (int n = 0; n < 24; n++) y[n + 2] = ((6 * y[n + 1] - y[n]) % q + q) % q;
        if (y[24] == y0 && y[25] == y1) {
            Seq s; for (int i = 0; i < 24; i++) s[i] = (short)y[i];
            C.K.push_back(s);
        }
    }
    int n = (int)C.K.size();
    std::map<Seq, int> fmap;
    C.fib.assign(n, -1);
    for (int i = 0; i < n; i++) {
        Seq s = C.K[i]; std::sort(s.begin(), s.end());
        auto it = fmap.find(s);
        if (it == fmap.end()) {
            int id = (int)C.fibers.size();
            fmap[s] = id; C.fibers.push_back({i}); C.fib[i] = id;
        } else { C.fibers[it->second].push_back(i); C.fib[i] = it->second; }
    }
    C.P.resize(n);
    for (int i = 0; i < n; i++)
        for (int r = 0; r < 4; r++) {
            array<short, 6> c; int k = 0;
            for (int j = r; j < 24; j += 4) c[k++] = C.K[i][j];
            std::sort(c.begin(), c.end()); C.P[i][r] = c;
        }
    C.mask.assign(n, vector<unsigned char>(n, 0));
    for (auto &f : C.fibers)
        for (int i : f) for (int j : f) {
            unsigned m = 0;
            for (int k = 0; k < 8; k++) {
                bool ok = true;
                for (int r = 0; r < 4; r++) if (C.P[j][r] != C.P[i][D4[k][r]]) ok = false;
                if (ok) m |= (1u << k);
            }
            C.mask[i][j] = (unsigned char)m;
        }
    for (int i = 0; i < n; i++) C.idx[C.K[i]] = i;
    C.head.assign(n, vector<int>(q, -1));
    C.nxt.assign(n, {});
    for (int i = 0; i < n; i++) {
        C.nxt[i].fill(-1);
        for (int j = 23; j >= 0; j--) {
            int v = C.K[i][j];
            C.nxt[i][j] = C.head[i][v];
            C.head[i][v] = j;
        }
    }
    return C;
}

struct Stats {
    long long bases = 0, auto_ok = 0, groups = 0, joint = 0, failures = 0;
    long long overflows = 0, fb_groups = 0, fb_joint = 0, lookup_err = 0;
};
static std::mutex fail_mu;
static vector<std::string> fail_wit;
static const long long NODE_CAP = 2000;

struct Searcher {
    const vector<Comp> *comps;
    int s;                    // source index
    vector<int> bi;           // base indices per component
    int msrc;                 // source mate index
    vector<int> others;       // component indices != s
    bool used[24];
    int sig[24];
    long long nodes = 0;
    bool overflow = false;
    long long lookup_err = 0;
    vector<vector<int>> mates;  // mate indices for others, deduped by caller

    bool rec(int npos) {
        if (overflow) return false;
        if (++nodes > NODE_CAP) { overflow = true; return false; }
        const Comp &S = (*comps)[s];
        const Seq &mat = S.K[msrc];
        if (npos == 24) {
            for (int oi : others) {
                const Comp &C = (*comps)[oi];
                const Seq &B = C.K[bi[oi]];
                int q = C.q;
                int y24 = ((6 * B[sig[23]] - B[sig[22]]) % q + q) % q;
                int y25 = ((6 * y24 - B[sig[23]]) % q + q) % q;
                if (y24 != B[sig[0]] || y25 != B[sig[1]]) return true;
            }
            vector<int> mt;
            for (int oi : others) {
                const Comp &C = (*comps)[oi];
                Seq o; for (int i = 0; i < 24; i++) o[i] = C.K[bi[oi]][sig[i]];
                auto it = C.idx.find(o);
                if (it == C.idx.end()) { lookup_err++; return true; }
                if (C.fib[it->second] != C.fib[bi[oi]]) return true;
                mt.push_back(it->second);
            }
            bool diag = (msrc == bi[s]);
            for (size_t t = 0; t < others.size(); t++)
                if (mt[t] != bi[others[t]]) diag = false;
            if (!diag) mates.push_back(mt);
            return true;
        }
        int v = mat[npos];
        for (int j = S.head[bi[s]][v]; j != -1; j = S.nxt[bi[s]][j]) {
            if (used[j]) continue;
            bool ok = true;
            if (npos >= 2) {
                for (int oi : others) {
                    const Comp &C = (*comps)[oi];
                    const Seq &B = C.K[bi[oi]];
                    int q = C.q;
                    int need = ((6 * B[sig[npos - 1]] - B[sig[npos - 2]]) % q + q) % q;
                    if (B[j] != need) { ok = false; break; }
                }
            }
            if (!ok) continue;
            used[j] = true; sig[npos] = j;
            if (!rec(npos + 1)) { used[j] = false; return false; }
            used[j] = false;
        }
        return true;
    }
};

// Exact direct fallback for an overflowed group: enumerate fiber mates of
// the other components and compare sorted value-tuples.
static long long fallback_group(const vector<Comp> &comps, int s,
                                const vector<int> &bi, int msrc, Stats &st) {
    int k = (int)comps.size();
    vector<int> others;
    for (int i = 0; i < k; i++) if (i != s) others.push_back(i);
    vector<vector<short>> bt(24, vector<short>(k)), mt2(24, vector<short>(k));
    for (int i = 0; i < 24; i++)
        for (int c = 0; c < k; c++) bt[i][c] = comps[c].K[bi[c]][i];
    std::sort(bt.begin(), bt.end());
    vector<vector<int>> flist;
    for (int o : others) flist.push_back(comps[o].fibers[comps[o].fib[bi[o]]]);
    vector<size_t> pos(others.size(), 0);
    long long joint = 0;
    while (true) {
        vector<int> mt(k, -1);
        mt[s] = msrc;
        for (size_t t = 0; t < others.size(); t++) mt[others[t]] = flist[t][pos[t]];
        bool diag = true;
        for (int c = 0; c < k; c++) if (mt[c] != bi[c]) diag = false;
        if (!diag) {
            for (int i = 0; i < 24; i++)
                for (int c = 0; c < k; c++) mt2[i][c] = comps[c].K[mt[c]][i];
            std::sort(mt2.begin(), mt2.end());
            if (mt2 == bt) {
                joint++;
                unsigned all = 0xFF;
                for (int c = 0; c < k; c++) all &= comps[c].mask[bi[c]][mt[c]];
                if (!all) {
                    st.failures++;
                    std::lock_guard<std::mutex> lk(fail_mu);
                    if (fail_wit.size() < 5) fail_wit.push_back("FAIL(fallback)");
                }
            }
        }
        size_t t = 0;
        while (t < pos.size()) {
            if (++pos[t] < flist[t].size()) break;
            pos[t] = 0; t++;
        }
        if (t == pos.size()) break;
    }
    return joint;
}

static bool is_constant(const Seq &s) {
    for (int i = 1; i < 24; i++) if (s[i] != s[0]) return false;
    return true;
}

int main(int argc, char **argv) {
    D4 = D4maps();
    if (argc < 2) { printf("usage: pairs qa qb | triple qa qb qc src\n"); return 1; }
    bool pairmode = !strcmp(argv[1], "pairs");
    vector<int> qs;
    int pref = -1;
    if (pairmode) {
        if (argc != 4 && argc != 5) { printf("usage: pairs qa qb [src]\n"); return 1; }
        qs = {atoi(argv[2]), atoi(argv[3])};
        if (argc == 5) pref = atoi(argv[4]);
    } else {
        if (argc != 6) { printf("usage: triple qa qb qc src\n"); return 1; }
        qs = {atoi(argv[2]), atoi(argv[3]), atoi(argv[4])}; pref = atoi(argv[5]);
    }
    int k = (int)qs.size();
    vector<Comp> comps;
    for (int q : qs) comps.push_back(build_comp(q));
    for (int i = 0; i < k; i++)
        printf("q=%d |K|=%zu fibers=%zu\n", qs[i], comps[i].K.size(), comps[i].fibers.size());
    // Re-verification of wave 46 s3 facts used by the reduction lemma.
    long long zero_masks = 0;
    for (int i = 0; i < k; i++) {
        for (auto &f : comps[i].fibers)
            for (int a : f) for (int b : f) if (a != b && comps[i].mask[a][b] == 0) zero_masks++;
        if (qs[i] == 81) {
            long long n2 = 0, nother = 0;
            for (auto &f : comps[i].fibers)
                for (int a : f) for (int b : f) if (a != b) {
                    if (__builtin_popcount(comps[i].mask[a][b]) == 2) n2++; else nother++;
                }
            printf("Pi81 check: size2=%lld other=%lld\n", n2, nother);
        }
        if (qs[i] == 49) {
            long long nfull = 0, nother = 0;
            for (auto &f : comps[i].fibers)
                for (int a : f) for (int b : f) if (a != b) {
                    if (comps[i].mask[a][b] == 0xFF) nfull++; else nother++;
                }
            printf("Pi49 check: full=%lld other=%lld\n", nfull, nother);
        }
    }
    printf("zero Pi masks over fiber pairs: %lld (must be 0)\n", zero_masks);
    fflush(stdout);
    if (zero_masks) return 3;

    long long total = 1;
    vector<long long> stride(k);
    for (int i = k - 1; i >= 0; i--) { stride[i] = total; total *= (long long)comps[i].K.size(); }
    // preferred source order: pref first, then the rest in order
    vector<int> order;
    if (pref >= 0) for (int i = 0; i < k; i++) if (qs[i] == pref) order.push_back(i);
    for (int i = 0; i < k; i++) if (std::find(order.begin(), order.end(), i) == order.end()) order.push_back(i);

    int nthreads = 4;
    vector<Stats> tstats(nthreads);
    std::atomic<long long> next_base{0};
    auto worker = [&](int tid) {
        Stats &st = tstats[tid];
        vector<int> bi(k);
        while (true) {
            long long b = next_base.fetch_add(1);
            if (b >= total) break;
            st.bases++;
            long long rem = b;
            for (int i = 0; i < k; i++) { bi[i] = (int)(rem / stride[i]); rem %= stride[i]; }
            int eff = -1;
            for (int c : order) if (!is_constant(comps[c].K[bi[c]])) { eff = c; break; }
            if (eff < 0) { st.auto_ok++; continue; }  // all-constant base: diagonal only
            vector<int> others;
            for (int i = 0; i < k; i++) if (i != eff) others.push_back(i);
            const Comp &S = comps[eff];
            for (int msrc : S.fibers[S.fib[bi[eff]]]) {
                st.groups++;
                Searcher sch;
                sch.comps = &comps; sch.s = eff; sch.bi = bi;
                sch.msrc = msrc; sch.others = others;
                memset(sch.used, 0, sizeof(sch.used));
                sch.rec(0);
                st.lookup_err += sch.lookup_err;
                if (sch.overflow) {
                    st.overflows++;
                    st.fb_groups++;
                    long long fj = fallback_group(comps, eff, bi, msrc, st);
                    st.fb_joint += fj;
                    st.joint += fj;
                    continue;
                }
                std::sort(sch.mates.begin(), sch.mates.end());
                sch.mates.erase(std::unique(sch.mates.begin(), sch.mates.end()), sch.mates.end());
                for (auto &mt : sch.mates) {
                    st.joint++;
                    vector<int> full(k, -1);
                    full[eff] = msrc;
                    for (size_t t = 0; t < others.size(); t++) full[others[t]] = mt[t];
                    unsigned all = 0xFF;
                    for (int c = 0; c < k; c++) all &= comps[c].mask[bi[c]][full[c]];
                    if (!all) {
                        st.failures++;
                        std::lock_guard<std::mutex> lk(fail_mu);
                        if (fail_wit.size() < 5) {
                            char buf[256];
                            snprintf(buf, sizeof(buf), "FAIL base=(%d,%d) mate=(%d,%d)",
                                     bi[0], k > 1 ? bi[1] : -1, full[0], k > 1 ? full[1] : -1);
                            fail_wit.push_back(buf);
                        }
                    }
                }
            }
        }
    };
    vector<std::thread> th;
    for (int t = 0; t < nthreads; t++) th.emplace_back(worker, t);
    for (auto &t : th) t.join();
    Stats tot;
    for (auto &s : tstats) {
        tot.bases += s.bases; tot.auto_ok += s.auto_ok; tot.groups += s.groups;
        tot.joint += s.joint; tot.failures += s.failures;
        tot.overflows += s.overflows; tot.fb_groups += s.fb_groups;
        tot.fb_joint += s.fb_joint; tot.lookup_err += s.lookup_err;
    }
    printf("BASES %lld AUTO_OK %lld GROUPS %lld JOINT %lld FAILURES %lld "
           "OVERFLOWS %lld FB_GROUPS %lld FB_JOINT %lld LOOKUP_ERR %lld\n",
           tot.bases, tot.auto_ok, tot.groups, tot.joint, tot.failures,
           tot.overflows, tot.fb_groups, tot.fb_joint, tot.lookup_err);
    for (auto &w : fail_wit) printf("%s\n", w.c_str());
    printf("DONE\n");
    return tot.failures == 0 ? 0 : 2;
}
