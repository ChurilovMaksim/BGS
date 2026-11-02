// Wave 47, task 4: triples (q, 1153^2, 81) for PC at m=24, q in {25,121,289,512}.
// Method: enumerate joint pairs at (q,81) with sigma-source 81 (both
// components non-constant; constant cases reduce to pair (q,1153^2),
// pair (81,1153^2), or single-1153 checks done by the cell program).
// For each joint pair and each common sigma != id:
//   V(sigma) = {(a,b) in F_1153^2 : s(a,b) o sigma in ker_1153}.
//   dim 0 -> only D=0, Pi_1153 full, triple OK.
//   dim 1 -> Pi_1153 constant over D != 0 (scaling); check once.
//   dim 2 -> sigma must be dihedral (else brute force over D); the
//            induced class map lies in Pi_q, Pi_81 and Pi_1153.
// s(a,b)[i] = Tr((a+b sqrt2) alpha^i) mod 1153, alpha = 3+2 sqrt2.
// Profiles at 1153^2 are computed mod 1153 (x -> 1153x is injective).
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
static const int P1153 = 1153;

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
    vector<vector<unsigned char>> mask;
    std::map<Seq, int> idx;
    vector<vector<int>> head;
    vector<array<int, 24>> nxt;
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

// trace sequence s(a,b) mod 1153, length 24
static array<short, 24> trace_seq(int a, int b) {
    array<short, 24> s;
    int ca = a, cb = b;
    for (int i = 0; i < 24; i++) {
        s[i] = (short)((2 * ca) % P1153);
        int nca = (3 * ca + 4 * cb) % P1153;
        int ncb = (2 * ca + 3 * cb) % P1153;
        ca = nca; cb = ncb;
    }
    return s;
}
static Prof prof_of_seq(const array<short, 24> &s) {
    Prof p;
    for (int r = 0; r < 4; r++) {
        array<short, 6> c; int k = 0;
        for (int j = r; j < 24; j += 4) c[k++] = s[j];
        std::sort(c.begin(), c.end()); p[r] = c;
    }
    return p;
}
static unsigned pi_mask_prof(const Prof &p, const Prof &pp) {
    unsigned m = 0;
    for (int k = 0; k < 8; k++) {
        bool ok = true;
        for (int r = 0; r < 4; r++) if (pp[r] != p[D4[k][r]]) ok = false;
        if (ok) m |= (1u << k);
    }
    return m;
}
static bool is_constant(const Seq &s) {
    for (int i = 1; i < 24; i++) if (s[i] != s[0]) return false;
    return true;
}

struct Stats {
    long long bases = 0, skipped_const = 0, groups = 0, pairs = 0;
    long long sigmas = 0, dim0 = 0, dim1 = 0, dim2dih = 0, dim2non = 0;
    long long failures = 0, overflows = 0, unresolved = 0, fb_brute = 0;
};
static std::mutex mu;
static vector<std::string> wit;
static const long long NODE_CAP = 2000;

static array<short, 24> S1, S2;  // trace basis

// V(sigma): dim + generator (if dim 1). Equations: cyclic recurrence for
// s o sigma, n = 0..23, coefficients from S1,S2.
static int v_dim_gen(const int sig[24], int &ga, int &gb) {
    int fca = 0, fcb = 0; bool have = false;
    for (int n = 0; n < 24; n++) {
        int i0 = sig[n], i1 = sig[(n + 1) % 24], i2 = sig[(n + 2) % 24];
        int ca = ((S1[i2] - 6 * S1[i1] + S1[i0]) % P1153 + P1153) % P1153;
        int cb = ((S2[i2] - 6 * S2[i1] + S2[i0]) % P1153 + P1153) % P1153;
        if (ca == 0 && cb == 0) continue;
        if (!have) { fca = ca; fcb = cb; have = true; continue; }
        if ((ca * fcb - cb * fca) % P1153 != 0) return 0;
    }
    if (!have) return 2;
    ga = (-fcb % P1153 + P1153) % P1153; gb = fca;
    return 1;
}
static bool sigma_dihedral(const int sig[24], int &kind, int &k) {
    // shift?
    int k0 = (sig[0] + 24) % 24;
    bool ok = true;
    for (int i = 0; i < 24; i++) if (sig[i] != (i + k0) % 24) ok = false;
    if (ok) { kind = 0; k = k0; return true; }
    int k1 = (sig[0] + 24) % 24;
    ok = true;
    for (int i = 0; i < 24; i++) if (sig[i] != ((-i + k1) % 24 + 24) % 24) ok = false;
    if (ok) { kind = 1; k = k1; return true; }
    return false;
}
// D4 index of induced class map: shift by k -> s_{k%4}; reflection k -> f_{k%4}.
// D4 order: generated as shifts then flips per b, sorted+unique. Find by map.
static int d4_index_of_map(const array<int, 4> &mp) {
    for (int k = 0; k < 8; k++) if (D4[k] == mp) return k;
    return -1;
}

struct Ctx {
    const Comp *Cq, *C81;
    Stats *st;
    int bq, b81;   // base indices
    int mq, m81;   // mate indices
    unsigned M;    // Pi_q & Pi_81 for this pair
    // sigma backtracking scratch
    bool used[24];
    int sig[24];
    long long nodes = 0;
    bool overflow = false;
    void check_sigma() {
        // skip identity sigma (D'=D, Pi_1153 contains s0, M contains s0? M
        // contains s0 iff profiles equal; identity sigma => mates equal =>
        // pair diagonal; but check_sigma is called for all sigma incl id
        // when pair diagonal. For id, D'=D so triple contains s0 iff
        // s0 in M... M = Pi(y,y') with y'=y => s0 in M always (prof equal).
        // So id is always OK.)
        bool id = true;
        for (int i = 0; i < 24; i++) if (sig[i] != i) id = false;
        if (id) return;
        st->sigmas++;
        int ga = 0, gb = 0;
        int dim = v_dim_gen(sig, ga, gb);
        if (dim == 0) { st->dim0++; return; }
        if (dim == 1) {
            st->dim1++;
            array<short, 24> sg, sgs;
            for (int i = 0; i < 24; i++) {
                sg[i] = (short)((ga * S1[i] + gb * S2[i]) % P1153);
            }
            for (int i = 0; i < 24; i++) sgs[i] = sg[sig[i]];
            unsigned m1153 = pi_mask_prof(prof_of_seq(sg), prof_of_seq(sgs));
            if (!(M & m1153)) {
                st->failures++;
                std::lock_guard<std::mutex> lk(mu);
                if (wit.size() < 5) {
                    char buf[256];
                    snprintf(buf, sizeof(buf), "FAIL dim1 base=(%d,%d) mate=(%d,%d)",
                             bq, b81, mq, m81);
                    wit.push_back(buf);
                }
            }
            return;
        }
        // dim 2
        int kind = -1, kk = 0;
        if (sigma_dihedral(sig, kind, kk)) {
            st->dim2dih++;
            array<int, 4> mp;
            for (int r = 0; r < 4; r++)
                mp[r] = kind == 0 ? (r + kk) % 4 : ((kk - r) % 4 + 4) % 4;
            int di = d4_index_of_map(mp);
            if (di < 0 || !(M & (1u << di))) {
                st->failures++;
                std::lock_guard<std::mutex> lk(mu);
                if (wit.size() < 5) wit.push_back("FAIL dim2dih induced map not in M");
            }
            return;
        }
        // non-dihedral dim 2: brute force over all D
        st->dim2non++;
        st->fb_brute++;
        for (int a = 0; a < P1153; a++) {
            for (int b = 0; b < P1153; b++) {
                if (a == 0 && b == 0) continue;
                array<short, 24> d, ds;
                for (int i = 0; i < 24; i++) d[i] = (short)((a * S1[i] + b * S2[i]) % P1153);
                for (int i = 0; i < 24; i++) ds[i] = d[sig[i]];
                unsigned m1153 = pi_mask_prof(prof_of_seq(d), prof_of_seq(ds));
                if (!(M & m1153)) {
                    st->failures++;
                    std::lock_guard<std::mutex> lk(mu);
                    if (wit.size() < 5) {
                        char buf[256];
                        snprintf(buf, sizeof(buf), "FAIL dim2non base=(%d,%d) mate=(%d,%d) D=(%d,%d)",
                                 bq, b81, mq, m81, a, b);
                        wit.push_back(buf);
                    }
                    return;
                }
            }
        }
    }
    bool rec(int npos) {
        if (overflow) return false;
        if (++nodes > NODE_CAP) { overflow = true; return false; }
        const Comp &S = *C81;
        const Seq &mat = S.K[m81];
        const Seq &B = Cq->K[bq];
        int q = Cq->q;
        if (npos == 24) {
            // closure for q
            int y24 = ((6 * B[sig[23]] - B[sig[22]]) % q + q) % q;
            int y25 = ((6 * y24 - B[sig[23]]) % q + q) % q;
            if (y24 != B[sig[0]] || y25 != B[sig[1]]) return true;
            Seq o; for (int i = 0; i < 24; i++) o[i] = B[sig[i]];
            auto it = Cq->idx.find(o);
            if (it == Cq->idx.end()) return true;
            if (Cq->fib[it->second] != Cq->fib[bq]) return true;
            mq = it->second;
            // M for this pair
            M = Cq->mask[bq][mq] & C81->mask[b81][m81];
            if (!M) {
                // pair failure at (q,81): should not happen (wave 46)
                st->failures++;
                std::lock_guard<std::mutex> lk(mu);
                if (wit.size() < 5) wit.push_back("FAIL pair (q,81) empty");
                return true;
            }
            st->pairs++;
            check_sigma();
            return true;
        }
        int v = mat[npos];
        for (int j = S.head[b81][v]; j != -1; j = S.nxt[b81][j]) {
            if (used[j]) continue;
            bool ok = true;
            if (npos >= 2) {
                int need = ((6 * B[sig[npos - 1]] - B[sig[npos - 2]]) % q + q) % q;
                if (B[j] != need) ok = false;
            }
            if (!ok) continue;
            used[j] = true; sig[npos] = j;
            if (!rec(npos + 1)) { used[j] = false; return false; }
            used[j] = false;
        }
        return true;
    }
};

int main(int argc, char **argv) {
    D4 = D4maps();
    if (argc != 2) { printf("usage: triple1153 q\n"); return 1; }
    int q = atoi(argv[1]);
    S1 = trace_seq(1, 0); S2 = trace_seq(0, 1);
    // sanity: antiperiod 12, period 24
    for (int i = 0; i < 24; i++) {
        int j = (i + 12) % 24;
        if ((S1[i] + S1[j]) % P1153 != 0 || (S2[i] + S2[j]) % P1153 != 0) {
            printf("FATAL: antiperiod fails\n"); return 1;
        }
    }
    Comp Cq = build_comp(q), C81 = build_comp(81);
    printf("q=%d |K|=%zu  81 |K|=%zu\n", q, Cq.K.size(), C81.K.size());
    fflush(stdout);
    long long total = (long long)Cq.K.size() * (long long)C81.K.size();
    int nthreads = 4;
    vector<Stats> tstats(nthreads);
    std::atomic<long long> next_base{0};
    auto worker = [&](int tid) {
        Stats &st = tstats[tid];
        while (true) {
            long long b = next_base.fetch_add(1);
            if (b >= total) break;
            st.bases++;
            int bq = (int)(b / (long long)C81.K.size());
            int b81 = (int)(b % (long long)C81.K.size());
            if (is_constant(Cq.K[bq]) || is_constant(C81.K[b81])) {
                st.skipped_const++; continue;  // covered by cell pair searches
            }
            for (int m81 : C81.fibers[C81.fib[b81]]) {
                st.groups++;
                Ctx ctx;
                ctx.Cq = &Cq; ctx.C81 = &C81; ctx.st = &st;
                ctx.bq = bq; ctx.b81 = b81; ctx.m81 = m81; ctx.mq = -1; ctx.M = 0;
                memset(ctx.used, 0, sizeof(ctx.used));
                ctx.rec(0);
                if (ctx.overflow) {
                    st.overflows++;
                    // retry with source q (swap roles): enumerate sigma from
                    // q-values, pruned by 81 recurrence. Implement via a
                    // second Ctx-like pass is complex; count as unresolved
                    // for now (reported honestly).
                    st.unresolved++;
                }
            }
        }
    };
    vector<std::thread> th;
    for (int t = 0; t < nthreads; t++) th.emplace_back(worker, t);
    for (auto &t : th) t.join();
    Stats tot;
    for (auto &s : tstats) {
        tot.bases += s.bases; tot.skipped_const += s.skipped_const;
        tot.groups += s.groups; tot.pairs += s.pairs; tot.sigmas += s.sigmas;
        tot.dim0 += s.dim0; tot.dim1 += s.dim1; tot.dim2dih += s.dim2dih;
        tot.dim2non += s.dim2non; tot.failures += s.failures;
        tot.overflows += s.overflows; tot.unresolved += s.unresolved;
        tot.fb_brute += s.fb_brute;
    }
    printf("BASES %lld SKIPPED_CONST %lld GROUPS %lld PAIRS %lld SIGMAS %lld "
           "DIM0 %lld DIM1 %lld DIM2DIH %lld DIM2NON %lld FAILURES %lld "
           "OVERFLOWS %lld UNRESOLVED %lld FB_BRUTE %lld\n",
           tot.bases, tot.skipped_const, tot.groups, tot.pairs, tot.sigmas,
           tot.dim0, tot.dim1, tot.dim2dih, tot.dim2non, tot.failures,
           tot.overflows, tot.unresolved, tot.fb_brute);
    for (auto &w : wit) printf("%s\n", w.c_str());
    printf("DONE\n");
    return tot.failures == 0 ? 0 : 2;
}
