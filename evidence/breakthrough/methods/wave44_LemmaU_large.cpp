// Wave 44, task 2 — Lemma U at m=60, large pairs involving 601^2 / 2281^2.
// Conventions (wave 43): u=30, beta=alpha^2, cycles s_k of length 30 over Z/m,
// s_0 = 2a, s_1 = 34a+48b, s_{k+1} = 34 s_k - s_{k-1} (mod m).
// block0 = {(s_k, t_k)}, block1 = {(-s_k, -t_k)}, P = block0 + block1 (sorted).
// G = <simultaneous shift, simultaneous reversal, simultaneous negation>.
// H = <shift, reversal> on single cycles.
// Modes: struct m | l1 m | reps ma mb [degenA] [degenB] | brute ma mb
#include <bits/stdc++.h>
using namespace std;
using u64 = unsigned long long;
using i64 = long long;

static inline u64 splitmix64(u64 x) {
    x += 0x9e3779b97f4a7c15ULL;
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
    x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
    return x ^ (x >> 31);
}
static u64 fnv_arr(const int* v, int n) {
    u64 h = 1469598103934665603ULL;
    for (int i = 0; i < n; i++) { h ^= (u64)(v[i] + 0x9e3779b9); h *= 1099511628211ULL; }
    return h;
}
static int modnorm(int v, int m) { v %= m; if (v < 0) v += m; return v; }

struct Cyc { array<int,30> v; };

static Cyc cycle_from_ab(int a, int b, int m) {
    Cyc c;
    c.v[0] = (2 * a) % m;
    c.v[1] = (34 * a + 48 * b) % m;
    for (int k = 2; k < 30; k++) c.v[k] = modnorm(34 * c.v[k-1] - c.v[k-2], m);
    return c;
}
static int min_period(const Cyc& c) {
    for (int d : {1,2,3,5,6,10,15,30}) {
        bool ok = true;
        for (int k = 0; k < 30; k++) if (c.v[k] != c.v[(k+d)%30]) { ok = false; break; }
        if (ok) return d;
    }
    return 30;
}
// H-canonical: min over shifts j and reversal e of t_k = s[(e ? -k+j : k+j) mod 30]
static array<int,30> hcanon(const Cyc& c) {
    array<int,30> best; bool first = true;
    for (int e = 0; e < 2; e++) for (int j = 0; j < 30; j++) {
        array<int,30> t;
        for (int k = 0; k < 30; k++) {
            int idx = e ? (-k + j) : (k + j);
            idx %= 30; if (idx < 0) idx += 30;
            t[k] = c.v[idx];
        }
        if (first || t < best) { best = t; first = false; }
    }
    return best;
}
// G-canonical of pair (A,B): min over shift m, reversal e, negation n of
// the 30-tuple of encoded pairs (A'_k * mb + B'_k). Early-exit lexicographic
// comparison: most transforms differ from the incumbent best at position 0-2.
static array<int,30> gcanon(const Cyc& A, const Cyc& B, int ma, int mb) {
    array<int,30> best; bool first = true;
    for (int e = 0; e < 2; e++) for (int n = 0; n < 2; n++) for (int j = 0; j < 30; j++) {
        // compare transform tuple with best element by element
        int cmp = 0; // -1: transform smaller, +1: larger, 0: equal so far
        int firstdiff = -1;
        for (int k = 0; k < 30; k++) {
            int idx = e ? (-k + j) : (k + j);
            idx %= 30; if (idx < 0) idx += 30;
            int av = A.v[idx], bv = B.v[idx];
            if (n) { av = (ma - av) % ma; bv = (mb - bv) % mb; }
            int v = av * mb + bv;
            if (first) break; // first transform: materialize below
            if (v < best[k]) { cmp = -1; firstdiff = k; break; }
            if (v > best[k]) { cmp = 1; break; }
        }
        if (first || cmp < 0) {
            array<int,30> t;
            for (int k = 0; k < 30; k++) {
                int idx = e ? (-k + j) : (k + j);
                idx %= 30; if (idx < 0) idx += 30;
                int av = A.v[idx], bv = B.v[idx];
                if (n) { av = (ma - av) % ma; bv = (mb - bv) % mb; }
                t[k] = av * mb + bv;
            }
            (void)firstdiff;
            best = t; first = false;
        }
    }
    return best;
}
static string key_of(const array<int,30>& t) {
    string s; s.resize(60);
    for (int k = 0; k < 30; k++) { s[2*k] = char(t[k] & 255); s[2*k+1] = char((t[k] >> 8) & 255); }
    return s;
}

struct Side {
    int m = 0;
    vector<Cyc> reps;      // H-orbit representative cycles
    vector<int> per;       // minimal periods
    vector<long> cnt;      // #params (or distinct cycles) in orbit
};

// sqrt(2) mod p by scan (p <= 2281 here)
static int sqrt2mod(int p) {
    for (int r = 0; r < p; r++) if ((r * r) % p == 2 % p) return r;
    return -1;
}

// Build side. If degen_only (large prime only), restrict to degenerate cycles:
// torsion (c1=0 or c2=0) or repeated values (c2/c1 in <beta1>), in split coords.
static Side build_side(int m, bool degen_only = false) {
    Side S; S.m = m;
    map<string, int> idx;
    auto add_cycle = [&](const Cyc& c) {
        array<int,30> hc = hcanon(c);
        string key = key_of(hc);
        auto it = idx.find(key);
        if (it == idx.end()) {
            int id = (int)S.reps.size();
            idx[key] = id;
            Cyc rep; rep.v = hc;
            S.reps.push_back(rep);
            S.per.push_back(min_period(c));
            S.cnt.push_back(1);
        } else S.cnt[it->second]++;
    };
    if (degen_only) {
        int p = m;
        int r = sqrt2mod(p);
        if (r < 0) { fprintf(stderr, "no sqrt2 mod %d\n", p); exit(1); }
        int b1 = (int)((1LL*(3+2*r)*(3+2*r)) % p);
        // powers of b1
        int pw[31]; pw[0] = 1;
        for (int k = 1; k <= 30; k++) pw[k] = (int)(1LL*pw[k-1]*b1 % p);
        int b1inv = 1; // b1^29 since ord 30
        for (int k = 0; k < 29; k++) b1inv = (int)(1LL*b1inv*b1 % p);
        // torsion: (0, c2), (c1, 0)
        for (int c = 0; c < p; c++) {
            Cyc cy;
            for (int k = 0; k < 30; k++) cy.v[k] = (int)(1LL*c*pw[k] % p); // (c,0): s_k = c*b1^k
            add_cycle(cy);
            Cyc cy2;
            // (0, c): s_k = c*b2^k, b2 = b1^{-1}
            int v = c;
            for (int k = 0; k < 30; k++) { cy2.v[k] = v; v = (int)(1LL*v*b1inv % p); }
            add_cycle(cy2);
        }
        // repeated values: c2 = c1 * b1^m, c1 != 0
        for (int c1 = 1; c1 < p; c1++) {
            for (int mm = 0; mm < 30; mm++) {
                int c2 = (int)(1LL*c1*pw[mm] % p);
                Cyc cy;
                int p1 = 1, p2 = 1; // b1^k, b2^k = b1^{-k}
                for (int k = 0; k < 30; k++) {
                    cy.v[k] = (int)((1LL*c1*p1 + 1LL*c2*p2) % p);
                    p1 = (int)(1LL*p1*b1 % p);
                    p2 = (int)(1LL*p2*b1inv % p);
                }
                add_cycle(cy);
            }
        }
        return S;
    }
    if (m == 9) {
        set<array<int,30>> seen;
        for (int a = 0; a < 9; a++) for (int b = 0; b < 9; b++) {
            Cyc c = cycle_from_ab(a, b, 9);
            if (seen.insert(c.v).second) add_cycle(c);
        }
        return S;
    }
    for (int a = 0; a < m; a++) for (int b = 0; b < m; b++)
        add_cycle(cycle_from_ab(a, b, m));
    return S;
}

// ---------- radix sort by 64-bit key (LSD, 4x16-bit) ----------
struct Rec { u64 ph; u64 bh; int ia, ib, eps, r; };
static void radix_sort_rec(vector<Rec>& a) {
    int n = (int)a.size();
    vector<Rec> b(n);
    vector<int> cnt(65536);
    for (int pass = 0; pass < 4; pass++) {
        fill(cnt.begin(), cnt.end(), 0);
        int sh = 16 * pass;
        for (auto& x : a) cnt[(x.ph >> sh) & 0xFFFF]++;
        int sum = 0;
        for (int i = 0; i < 65536; i++) { int t = cnt[i]; cnt[i] = sum; sum += t; }
        for (auto& x : a) b[cnt[(x.ph >> sh) & 0xFFFF]++] = x;
        a.swap(b);
    }
}

struct PairInfo {
    array<int,30> A, B; // pair sequences
};

// exact P (sorted 60 pairs) and exact block pair (sorted b0, sorted b1) for a rep
static void exact_blocks(const Cyc& sa, const Cyc& sb, int ma, int mb, int eps, int rr,
                         array<int,60>& P, array<int,30>& b0, array<int,30>& b1) {
    for (int k = 0; k < 30; k++) {
        int idx = eps ? (-k - rr) : (k + rr);
        idx %= 30; if (idx < 0) idx += 30;
        int av = sa.v[idx], bv = sb.v[k];
        b0[k] = av * mb + bv;
        b1[k] = ((ma - av) % ma) * mb + ((mb - bv) % mb);
    }
    sort(b0.begin(), b0.end());
    sort(b1.begin(), b1.end());
    merge(b0.begin(), b0.end(), b1.begin(), b1.end(), P.begin());
}

int main(int argc, char** argv) {
    setvbuf(stdout, NULL, _IONBF, 0);
    if (argc < 3) { fprintf(stderr, "usage: struct m | l1 m | reps ma mb [dA] [dB] | brute ma mb\n"); return 1; }
    string mode = argv[1];
    if (mode == "struct") {
        int m = atoi(argv[2]);
        Side S = build_side(m);
        map<int,long> per; long anti = 0, tot = 0;
        // need per-cycle stats: recompute over params (cheap for small; for large use split? just params)
        if (m == 9) {
            set<array<int,30>> seen;
            for (int a = 0; a < 9; a++) for (int b = 0; b < 9; b++) {
                Cyc c = cycle_from_ab(a, b, 9);
                if (!seen.insert(c.v).second) continue;
                tot++; per[min_period(c)]++;
                bool ok = true;
                for (int k = 0; k < 30; k++) if (c.v[(k+15)%30] != (m - c.v[k]) % m) ok = false;
                if (ok) anti++;
            }
        } else {
            for (int a = 0; a < m; a++) for (int b = 0; b < m; b++) {
                Cyc c = cycle_from_ab(a, b, m);
                tot++; per[min_period(c)]++;
                bool ok = true;
                for (int k = 0; k < 30; k++) if (c.v[(k+15)%30] != (m - c.v[k]) % m) ok = false;
                if (ok) anti++;
            }
        }
        printf("side m=%d: cycles=%ld H-orbits=%zu periods:", m, tot, S.reps.size());
        for (auto& kv : per) printf(" %d:%ld", kv.first, kv.second);
        printf(" antiperiod15=%ld\n", anti);
        return 0;
    }
    if (mode == "l1") {
        int m = atoi(argv[2]);
        // group cycles by sorted value multiset; check dihedral equivalence within group
        map<array<int,30>, vector<Cyc>> groups;
        auto add = [&](const Cyc& c) {
            array<int,30> s = c.v;
            sort(s.begin(), s.end());
            groups[s].push_back(c);
        };
        if (m == 9) {
            set<array<int,30>> seen;
            for (int a = 0; a < 9; a++) for (int b = 0; b < 9; b++) {
                Cyc c = cycle_from_ab(a, b, 9);
                if (seen.insert(c.v).second) add(c);
            }
        } else {
            for (int a = 0; a < m; a++) for (int b = 0; b < m; b++) add(cycle_from_ab(a, b, m));
        }
        long bad = 0, ngroups = 0;
        for (auto& kv : groups) {
            ngroups++;
            // dihedral canonical under <shift, reversal, negation>
            set<array<int,30>> classes;
            for (auto& c : kv.second) {
                array<int,30> best; bool first = true;
                for (int e = 0; e < 2; e++) for (int n = 0; n < 2; n++) for (int j = 0; j < 30; j++) {
                    array<int,30> t;
                    for (int k = 0; k < 30; k++) {
                        int idx = e ? (-k + j) : (k + j);
                        idx %= 30; if (idx < 0) idx += 30;
                        int v = c.v[idx];
                        if (n) v = (m - v) % m;
                        t[k] = v;
                    }
                    if (first || t < best) { best = t; first = false; }
                }
                classes.insert(best);
            }
            if (classes.size() > 1) {
                bad++;
                if (bad <= 3) printf("  L1 VIOLATION group size %zu, %zu dihedral classes\n", kv.second.size(), classes.size());
            }
        }
        printf("L1 side m=%d: value-multiset groups=%ld violations=%ld\n", m, ngroups, bad);
        return 0;
    }
    if (mode == "reps") {
        int ma = atoi(argv[2]), mb = atoi(argv[3]);
        bool dA = argc > 4 && atoi(argv[4]) != 0;
        bool dB = argc > 5 && atoi(argv[5]) != 0;
        Side A = build_side(ma, dA), B = build_side(mb, dB);
        printf("reps pair (%d,%d) degen=(%d,%d): H-orbits A=%zu B=%zu\n", ma, mb, (int)dA, (int)dB, A.reps.size(), B.reps.size());
        fflush(stdout);
        vector<Rec> recs;
        recs.reserve(1 << 20);
        for (int ia = 0; ia < (int)A.reps.size(); ia++) {
            for (int ib = 0; ib < (int)B.reps.size(); ib++) {
                int Ta = A.per[ia], Tb = B.per[ib];
                int g = std::gcd(Ta, Tb);
                for (int eps = 0; eps < 2; eps++) for (int rr = 0; rr < g; rr++) {
                    array<int,30> b0, b1;
                    for (int k = 0; k < 30; k++) {
                        int idx = eps ? (-k - rr) : (k + rr);
                        idx %= 30; if (idx < 0) idx += 30;
                        int av = A.reps[ia].v[idx], bv = B.reps[ib].v[k];
                        b0[k] = av * mb + bv;
                        b1[k] = ((ma - av) % ma) * mb + ((mb - bv) % mb);
                    }
                    sort(b0.begin(), b0.end());
                    sort(b1.begin(), b1.end());
                    array<int,60> P;
                    merge(b0.begin(), b0.end(), b1.begin(), b1.end(), P.begin());
                    u64 ph = fnv_arr(P.data(), 60);
                    u64 bh = fnv_arr(b0.data(), 30) ^ fnv_arr(b1.data(), 30);
                    recs.push_back({ph, bh, ia, ib, eps, rr});
                }
            }
            if (ia % 2000 == 0 && ia > 0) { fprintf(stderr, "  ia=%d recs=%zu\n", ia, recs.size()); }
        }
        printf("reps total=%zu; sorting...\n", recs.size()); fflush(stdout);
        radix_sort_rec(recs);
        long ngroups = 0, nmulti = 0, nconf_cand = 0;
        struct Cand { vector<Rec> rs; };
        vector<Cand> cands;
        for (size_t i = 0; i < recs.size();) {
            size_t j = i;
            while (j < recs.size() && recs[j].ph == recs[i].ph) j++;
            ngroups++;
            if (j - i > 1) nmulti++;
            // distinct block hashes?
            bool multi_bh = false;
            for (size_t k = i + 1; k < j; k++) if (recs[k].bh != recs[i].bh) { multi_bh = true; break; }
            if (multi_bh) {
                nconf_cand++;
                Cand c;
                for (size_t k = i; k < j; k++) c.rs.push_back(recs[k]);
                cands.push_back(std::move(c));
            }
            i = j;
        }
        printf("groups=%ld multi-rep groups=%ld conflict-candidates=%ld\n", ngroups, nmulti, nconf_cand);
        // exact verification of candidates
        long true_conf = 0;
        for (auto& c : cands) {
            // group reps by exact P
            map<array<int,60>, vector<array<int,30>>> byP; // P -> list of (b0,b1) as unordered pair key
            map<array<int,60>, vector<pair<array<int,30>,array<int,30>>>> det;
            for (auto& rc : c.rs) {
                array<int,60> P; array<int,30> b0, b1;
                exact_blocks(A.reps[rc.ia], B.reps[rc.ib], ma, mb, rc.eps, rc.r, P, b0, b1);
                det[P].push_back({b0, b1});
            }
            for (auto& kv : det) {
                auto& lst = kv.second;
                // unordered block pair equality: {b0,b1} as set (b0 vs b1 swap allowed)
                bool allsame = true;
                for (size_t k = 1; k < lst.size(); k++) {
                    bool eq = (lst[k].first == lst[0].first && lst[k].second == lst[0].second) ||
                              (lst[k].first == lst[0].second && lst[k].second == lst[0].first);
                    if (!eq) allsame = false;
                }
                if (!allsame) {
                    true_conf++;
                    printf("  TRUE CONFLICT: exact-P group with %zu reps, differing block pairs\n", lst.size());
                }
            }
        }
        printf("TRUE CONFLICTS=%ld\n", true_conf);
        // multi-orbit analysis: for groups with >1 rep (by hash), dedupe by G-canon and
        // check partial-relatedness. To bound cost, do it for all groups but report totals.
        // Rebuild groups (by exact P) from recs: second pass over sorted recs is expensive;
        // instead do it only for candidate-free multi groups via a fresh grouping on phash
        // with G-canon computed per rep in multi groups.
        long morbits_groups = 0, explained = 0, unexplained = 0, morbit_reps = 0;
        for (size_t i = 0; i < recs.size();) {
            size_t j = i;
            while (j < recs.size() && recs[j].ph == recs[i].ph) j++;
            if (j - i > 1) {
                // dedupe by G-canon (exact P first: reps with different exact P are different groups;
                // hash collisions merged them -- handle by exact P grouping)
                map<array<int,60>, vector<Rec>> byP;
                for (size_t k = i; k < j; k++) {
                    array<int,60> P; array<int,30> b0, b1;
                    exact_blocks(A.reps[recs[k].ia], B.reps[recs[k].ib], ma, mb, recs[k].eps, recs[k].r, P, b0, b1);
                    byP[P].push_back(recs[k]);
                }
                for (auto& kv : byP) {
                    auto& lst = kv.second;
                    // G-canonical forms
                    vector<array<int,30>> gc;
                    vector<Rec> greps;
                    for (auto& rc : lst) {
                        // pair sequences for this rep
                        Cyc PA, PB;
                        for (int k = 0; k < 30; k++) {
                            int idx = rc.eps ? (-k - rc.r) : (k + rc.r);
                            idx %= 30; if (idx < 0) idx += 30;
                            PA.v[k] = A.reps[rc.ia].v[idx];
                            PB.v[k] = B.reps[rc.ib].v[k];
                        }
                        array<int,30> g = gcanon(PA, PB, ma, mb);
                        bool dup = false;
                        for (auto& h : gc) if (h == g) { dup = true; break; }
                        if (!dup) { gc.push_back(g); greps.push_back(rc); }
                    }
                    if (gc.size() > 1) {
                        morbits_groups++;
                        morbit_reps += (long)gc.size();
                        // check partial-relatedness: each other orbit vs first
                        bool allok = true;
                        // reconstruct first orbit pair sequences
                        auto getpair = [&](const Rec& rc, Cyc& PA, Cyc& PB) {
                            for (int k = 0; k < 30; k++) {
                                int idx = rc.eps ? (-k - rc.r) : (k + rc.r);
                                idx %= 30; if (idx < 0) idx += 30;
                                PA.v[k] = A.reps[rc.ia].v[idx];
                                PB.v[k] = B.reps[rc.ib].v[k];
                            }
                        };
                        Cyc pA, pB; getpair(greps[0], pA, pB);
                        array<int,30> g0 = gc[0];
                        for (size_t q = 1; q < greps.size(); q++) {
                            Cyc qA, qB; getpair(greps[q], qA, qB);
                            array<int,30> gq = gc[q];
                            bool rel = false;
                            // partial on A side: transforms of pA only
                            for (int e = 0; e < 2 && !rel; e++) for (int n = 0; n < 2 && !rel; n++) for (int s = 0; s < 30 && !rel; s++) {
                                Cyc DA, DB = pB;
                                for (int k = 0; k < 30; k++) {
                                    int idx = e ? (-k + s) : (k + s);
                                    idx %= 30; if (idx < 0) idx += 30;
                                    int v = pA.v[idx];
                                    if (n) v = (ma - v) % ma;
                                    DA.v[k] = v;
                                }
                                if (gcanon(DA, DB, ma, mb) == gq) rel = true;
                            }
                            // partial on B side
                            for (int e = 0; e < 2 && !rel; e++) for (int n = 0; n < 2 && !rel; n++) for (int s = 0; s < 30 && !rel; s++) {
                                Cyc DA = pA, DB;
                                for (int k = 0; k < 30; k++) {
                                    int idx = e ? (-k + s) : (k + s);
                                    idx %= 30; if (idx < 0) idx += 30;
                                    int v = pB.v[idx];
                                    if (n) v = (mb - v) % mb;
                                    DB.v[k] = v;
                                }
                                if (gcanon(DA, DB, ma, mb) == gq) rel = true;
                            }
                            if (!rel) allok = false;
                        }
                        if (allok) explained++; else {
                            unexplained++;
                            printf("  UNEXPLAINED multi-orbit group: %zu orbits\n", gc.size());
                        }
                    }
                }
            }
            i = j;
        }
        printf("multi-orbit groups=%ld (reps in them=%ld) explained=%ld unexplained=%ld\n",
               morbits_groups, morbit_reps, explained, unexplained);
        return 0;
    }
    if (mode == "brute") {
        int ma = atoi(argv[2]), mb = atoi(argv[3]);
        // precompute cycles per param
        vector<Cyc> CA, CB;
        if (ma == 9) {
            set<array<int,30>> seen;
            for (int a = 0; a < 9; a++) for (int b = 0; b < 9; b++) {
                Cyc c = cycle_from_ab(a, b, 9);
                if (seen.insert(c.v).second) CA.push_back(c);
            }
        } else for (int a = 0; a < ma; a++) for (int b = 0; b < ma; b++) CA.push_back(cycle_from_ab(a, b, ma));
        if (mb == 9) {
            set<array<int,30>> seen;
            for (int a = 0; a < 9; a++) for (int b = 0; b < 9; b++) {
                Cyc c = cycle_from_ab(a, b, 9);
                if (seen.insert(c.v).second) CB.push_back(c);
            }
        } else for (int a = 0; a < mb; a++) for (int b = 0; b < mb; b++) CB.push_back(cycle_from_ab(a, b, mb));
        printf("brute pair (%d,%d): cycles A=%zu B=%zu points=%lld\n", ma, mb, CA.size(), CB.size(),
               (long long)CA.size() * (long long)CB.size());
        fflush(stdout);
        struct BRec { u64 ph, bh; int ia, ib; };
        vector<BRec> recs;
        recs.reserve(CA.size() * CB.size());
        for (int ia = 0; ia < (int)CA.size(); ia++) {
            for (int ib = 0; ib < (int)CB.size(); ib++) {
                array<int,30> b0, b1;
                for (int k = 0; k < 30; k++) {
                    int av = CA[ia].v[k], bv = CB[ib].v[k];
                    b0[k] = av * mb + bv;
                    b1[k] = ((ma - av) % ma) * mb + ((mb - bv) % mb);
                }
                sort(b0.begin(), b0.end());
                sort(b1.begin(), b1.end());
                array<int,60> P;
                merge(b0.begin(), b0.end(), b1.begin(), b1.end(), P.begin());
                u64 ph = fnv_arr(P.data(), 60);
                u64 bh = fnv_arr(b0.data(), 30) ^ fnv_arr(b1.data(), 30);
                recs.push_back({ph, bh, ia, ib});
            }
            if (ia % 50000 == 0 && ia > 0) fprintf(stderr, "  ia=%d recs=%zu\n", ia, recs.size());
        }
        printf("brute total=%zu; sorting...\n", recs.size()); fflush(stdout);
        // radix sort by ph (LSD 16-bit x4) on BRec: reuse generic approach
        vector<BRec> tmp(recs.size());
        vector<int> cnt(65536);
        for (int pass = 0; pass < 4; pass++) {
            fill(cnt.begin(), cnt.end(), 0);
            int sh = 16 * pass;
            for (auto& x : recs) cnt[(x.ph >> sh) & 0xFFFF]++;
            int sum = 0;
            for (int i = 0; i < 65536; i++) { int t = cnt[i]; cnt[i] = sum; sum += t; }
            for (auto& x : recs) tmp[cnt[(x.ph >> sh) & 0xFFFF]++] = x;
            recs.swap(tmp);
        }
        long ngroups = 0, nconf_cand = 0, true_conf = 0;
        for (size_t i = 0; i < recs.size();) {
            size_t j = i;
            while (j < recs.size() && recs[j].ph == recs[i].ph) j++;
            ngroups++;
            bool multi_bh = false;
            for (size_t k = i + 1; k < j; k++) if (recs[k].bh != recs[i].bh) { multi_bh = true; break; }
            if (multi_bh) {
                nconf_cand++;
                // exact verify: group by exact P
                map<array<int,60>, vector<pair<array<int,30>,array<int,30>>>> det;
                for (size_t k = i; k < j; k++) {
                    array<int,30> b0, b1;
                    for (int t = 0; t < 30; t++) {
                        int av = CA[recs[k].ia].v[t], bv = CB[recs[k].ib].v[t];
                        b0[t] = av * mb + bv;
                        b1[t] = ((ma - av) % ma) * mb + ((mb - bv) % mb);
                    }
                    sort(b0.begin(), b0.end());
                    sort(b1.begin(), b1.end());
                    array<int,60> P;
                    merge(b0.begin(), b0.end(), b1.begin(), b1.end(), P.begin());
                    det[P].push_back({b0, b1});
                }
                for (auto& kv : det) {
                    auto& lst = kv.second;
                    bool allsame = true;
                    for (size_t k = 1; k < lst.size(); k++) {
                        bool eq = (lst[k].first == lst[0].first && lst[k].second == lst[0].second) ||
                                  (lst[k].first == lst[0].second && lst[k].second == lst[0].first);
                        if (!eq) allsame = false;
                    }
                    if (!allsame) { true_conf++; printf("  TRUE CONFLICT in brute group\n"); }
                }
            }
            i = j;
        }
        printf("brute groups=%ld conflict-candidates=%ld TRUE CONFLICTS=%ld\n", ngroups, nconf_cand, true_conf);
        return 0;
    }
    fprintf(stderr, "unknown mode\n");
    return 1;
}
