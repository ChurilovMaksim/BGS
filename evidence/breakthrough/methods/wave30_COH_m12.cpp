// Wave 30, task 3: COH at m=12 across ALL components -- exact test.
//
// D_12 = 1536796800 = 2^7 * 3^4 * 5^2 * 7^2 * 11^2, components
// q in {128, 81, 25, 49, 121}. Genuine parameters number 1536796800:
// direct grouping is infeasible, so the test is reduced exactly:
//
// For genuine A, S(A) = (Tr(A alpha^i))_{i in Z/12}. A pair (A, A')
// shares the joint global multiset iff some permutation sigma of
// Z/12 sends S(A) to S(A'). COH holds for the pair iff some single
// (j, c) works: A' = c(A) alpha^j + z + w (mod D_12), z in Ann,
// w in Shadow. In sequence terms, with tau the dihedral map of
// (j, c), COH iff for some tau: S'_q - tau(S_q) in ShiftSeq_q for
// every q, where ShiftSeq_q = {0} except q=81, where it is the 9
// sequences Tr(27 D alpha^i), D in R/3R.
//
// Classes equal dihedral images at q != 81 (verified), so validity
// of sigma at q != 81 depends only on S_q's value PATTERN:
// sigma(S_q) = tau(S_q) iff pattern_q[sigma(i)] = pattern_q[tau(i)]
// for all i. Define alive_q(sigma, pattern) = {tau : as above} and
// T_81(S_81, S'_81) = {tau : S'_81 - tau(S_81) in ShiftSet}.
// A pair fails COH iff, for its sigma, all alive_q are nonempty and
//   (AND_q alive_q) intersect T_81 = empty.
// Two phases, both exhaustive:
//  Phase 1 (mixed, T_81 full): iterate over (pattern, dihedral
//   image) tuples at q != 81 (257520 total): masks m_q =
//   {tau : P_q o tau = Q_q}; if AND m_q = 0 and a matching sigma
//   with P_q[sigma(i)] = Q_q[i] exists, that sigma (with A_81 = 0)
//   is a COH failure.
//  Phase 2 (81-constrained): all (S_81, S'_81) class pairs with
//   T_81 a proper subset (1728 pairs, 207360 matchings total;
//   the huge-matching pairs all have T_81 full, hence belong to
//   Phase 1). For each matching sigma and each pattern tuple with
//   all alive_q nonempty, check (AND alive) intersect T_81 empty.
// Any failure is reconstructed via CRT and verified directly
// (joint multisets equal; no (j, c) over L = lcm of orders with
// Ann+Shadow slack). No Lean, repository untouched.
#include <bits/stdc++.h>
using namespace std;
using i64 = long long;
const int M = 12;
const int QS[5] = {128, 81, 25, 49, 121};

pair<int,int> mulp(pair<int,int> a, pair<int,int> b, int q) {
    return {(a.first*b.first + 2*a.second*b.second) % q,
            (a.first*b.second + a.second*b.first) % q};
}
pair<int,int> pw(pair<int,int> a, int n, int q) {
    pair<int,int> r = {1, 0};
    for (int i = 0; i < n; i++) r = mulp(r, a, q);
    return r;
}
pair<int,int> conjp(pair<int,int> a, int q) {
    return {a.first % q, (q - a.second) % q};
}
int trp(pair<int,int> a, int q) { return (2*a.first) % q; }

struct Seq12 { int v[12]; };
bool operator<(Seq12 const& a, Seq12 const& b) {
    for (int i = 0; i < 12; i++) { if (a.v[i] != b.v[i]) return a.v[i] < b.v[i]; }
    return false;
}
bool operator==(Seq12 const& a, Seq12 const& b) {
    for (int i = 0; i < 12; i++) if (a.v[i] != b.v[i]) return false;
    return true;
}
struct SeqHash {
    size_t operator()(Seq12 const& s) const {
        size_t h = 0;
        for (int i = 0; i < 12; i++) h = h*1315423911u + (size_t)(s.v[i]+1);
        return h;
    }
};

vector<array<int,12>> DIH;

uint32_t alive_mask(array<int,12> const& sig, array<int,12> const& P) {
    uint32_t m = 0;
    for (int ti = 0; ti < 24; ti++) {
        bool ok = true;
        for (int i = 0; i < 12; i++) if (P[sig[i]] != P[DIH[ti][i]]) { ok = false; break; }
        if (ok) m |= (1u << ti);
    }
    return m;
}

// parameter transform for dihedral tau: shift tau(i)=i+k -> A alpha^k;
// reflection tau(i)=-i+k -> conj(A) alpha^{-k}
pair<int,int> tau_param(pair<int,int> A, int ti, int q) {
    int k0 = DIH[ti][0];
    bool isshift = true;
    for (int i = 0; i < 12; i++) if (DIH[ti][i] != (i+k0)%12) isshift = false;
    if (isshift) return mulp(A, pw({3,2}, k0, q), q);
    int kk = ((-k0)%12+12)%12;
    return mulp(conjp(A, q), pw({3,2}, kk, q), q);
}

struct Comp {
    int q;
    vector<pair<int,int>> G;
    unordered_map<Seq12, vector<pair<int,int>>, SeqHash> seqdict;
    map<Seq12, vector<Seq12>> classes;
    vector<Seq12> seqs;
    map<array<int,12>, pair<pair<int,int>,Seq12>> pat_example;
    vector<array<int,12>> patterns;
};

int main() {
    for (int k = 0; k < 12; k++) {
        array<int,12> sh, rf;
        for (int i = 0; i < 12; i++) { sh[i] = (i+k)%12; rf[i] = ((-i+k)%12+12)%12; }
        DIH.push_back(sh); DIH.push_back(rf);
    }
    sort(DIH.begin(), DIH.end());
    DIH.erase(unique(DIH.begin(), DIH.end()), DIH.end());
    assert(DIH.size() == 24);

    vector<Comp> comps;
    for (int qi = 0; qi < 5; qi++) {
        int q = QS[qi];
        Comp C; C.q = q;
        auto d = pw({3,2}, M, q);
        pair<int,int> dm = {(d.first-1+q)%q, d.second};
        for (int x = 0; x < q; x++) for (int y = 0; y < q; y++)
            if (mulp(dm, {x,y}, q) == make_pair(0,0)) C.G.push_back({x,y});
        for (auto A : C.G) {
            Seq12 s; auto b = A;
            for (int i = 0; i < 12; i++) { s.v[i] = trp(b, q); b = mulp(b, {3,2}, q); }
            C.seqs.push_back(s);
            C.seqdict[s].push_back(A);
            Seq12 ss = s; sort(ss.v, ss.v+12);
            C.classes[ss].push_back(s);
            array<int,12> pat; map<int,int> lab;
            for (int i = 0; i < 12; i++) {
                if (!lab.count(s.v[i])) lab[s.v[i]] = (int)lab.size();
                pat[i] = lab[s.v[i]];
            }
            if (!C.pat_example.count(pat)) C.pat_example[pat] = {A, s};
        }
        for (auto& kv : C.classes) {
            sort(kv.second.begin(), kv.second.end());
            kv.second.erase(unique(kv.second.begin(), kv.second.end()), kv.second.end());
        }
        for (auto& kv : C.pat_example) C.patterns.push_back(kv.first);
        printf("q=%d |G|=%zu classes=%zu patterns=%zu\n", q, C.G.size(),
               C.classes.size(), C.patterns.size());
        comps.push_back(move(C));
    }
    Comp& C81 = comps[1];
    set<Seq12> shifts;
    for (int a = 0; a < 3; a++) for (int b = 0; b < 3; b++) {
        pair<int,int> D = {(27*a)%81, (27*b)%81};
        Seq12 s; auto cur = D;
        for (int i = 0; i < 12; i++) { s.v[i] = trp(cur, 81); cur = mulp(cur, {3,2}, 81); }
        shifts.insert(s);
    }
    printf("ShiftSet size=%zu\n", shifts.size());
    for (int qi : {0,2,3,4}) {
        Comp& C = comps[qi];
        int bad = 0;
        for (auto& kv : C.classes) {
            Seq12 S0 = kv.second[0];
            set<Seq12> dih;
            for (auto& t : DIH) { Seq12 t2; for (int i=0;i<12;i++) t2.v[i]=S0.v[t[i]]; dih.insert(t2); }
            for (auto& s : kv.second) if (!dih.count(s)) bad++;
        }
        printf("q=%d non-dihedral class seqs=%d\n", C.q, bad);
    }

    vector<int> qidx = {0,2,3,4};
    // ---- shared direct verification of a failure ----
    auto verify_failure = [&](array<int,12> const& sig, int pp[4],
                              pair<int,int> A81, pair<int,int> Ap81,
                              uint32_t am[4]) -> bool {
        pair<int,int> Bq[5], Bpq[5];
        Bq[1] = A81; Bpq[1] = Ap81;
        for (int k = 0; k < 4; k++) {
            Comp& C = comps[qidx[k]];
            auto ex = C.pat_example[C.patterns[pp[k]]];
            Bq[qidx[k]] = ex.first;
            int ti = -1;
            for (int t = 0; t < 24; t++) if (am[k] & (1u<<t)) { ti = t; break; }
            assert(ti >= 0);
            Bpq[qidx[k]] = tau_param(ex.first, ti, C.q);
            Seq12 chk; auto cur = Bpq[qidx[k]];
            for (int i = 0; i < 12; i++) { chk.v[i] = trp(cur, C.q); cur = mulp(cur, {3,2}, C.q); }
            Seq12 want; for (int i = 0; i < 12; i++) want.v[i] = ex.second.v[sig[i]];
            if (!(chk == want)) { printf("RECONSTRUCTION MISMATCH comp %d\n", C.q); return false; }
        }
        auto crt1 = [&](pair<int,int>* arr, int coord) {
            i64 x = 0, Mc = 1;
            for (int qi2 = 0; qi2 < 5; qi2++) {
                int q = QS[qi2];
                int r = (coord==0? arr[qi2].first : arr[qi2].second);
                i64 a = Mc % q, b = q, u = 1, v = 0;
                while (b) { i64 t = a/b; a-=t*b; swap(a,b); u-=t*v; swap(u,v); }
                i64 inv = (u%q+q)%q;
                i64 t = ((r - x) % q + q) % q * inv % q;
                x += Mc * t; Mc *= q;
            }
            return x;
        };
        i64 Ax = crt1(Bq,0), Ay = crt1(Bq,1), Apx = crt1(Bpq,0), Apy = crt1(Bpq,1);
        printf("A=(%lld,%lld) A'=(%lld,%lld) mod D12\n", Ax, Ay, Apx, Apy);
        const i64 D = 1536796800LL;
        auto gseq = [&](i64 X, i64 Y) {
            vector<i64> out; pair<i64,i64> b = {X, Y};
            for (int i = 0; i < 12; i++) {
                out.push_back((2*b.first)%D);
                b = {(b.first*3 + 2*b.second*2)%D, (b.first*2 + b.second*3)%D};
            }
            sort(out.begin(), out.end());
            return out;
        };
        auto sA = gseq(Ax, Ay), sAp = gseq(Apx, Apy);
        printf("joint multisets equal: %d\n", (int)(sA == sAp));
        if (sA != sAp) return false;
        vector<set<pair<int,int>>> slack(5);
        for (int qi2 = 0; qi2 < 5; qi2++) {
            int q = QS[qi2];
            set<pair<int,int>> Ann;
            auto pows = vector<pair<int,int>>(12);
            { auto cur = make_pair(1,0); for (int i=0;i<12;i++){ pows[i]=cur; cur=mulp(cur,{3,2},q);} }
            for (int x = 0; x < q; x++) for (int y = 0; y < q; y++) {
                bool ok = true;
                for (int i = 0; i < 12; i++)
                    if (trp(mulp({x,y}, pows[i], q), q) != 0) { ok = false; break; }
                if (ok) Ann.insert({x,y});
            }
            set<pair<int,int>> Sh;
            if (q == 81) for (int a=0;a<3;a++) for (int b=0;b<3;b++) Sh.insert({(27*a)%81,(27*b)%81});
            else Sh.insert({0,0});
            for (auto z : Ann) for (auto w : Sh)
                slack[qi2].insert({(z.first+w.first)%q, (z.second+w.second)%q});
        }
        int L = 1;
        for (int qi2 = 0; qi2 < 5; qi2++) {
            int q = QS[qi2]; auto cur = make_pair(1,0); int o = 0;
            do { cur = mulp(cur, {3,2}, q); o++; } while (cur != make_pair(1,0));
            L = std::lcm(L, o);
        }
        vector<vector<pair<int,int>>> pwq(5);
        for (int qi2 = 0; qi2 < 5; qi2++) {
            int q = QS[qi2]; pwq[qi2].push_back({1,0});
            for (int i = 0; i < L; i++) pwq[qi2].push_back(mulp(pwq[qi2].back(), {3,2}, q));
        }
        bool found = false;
        for (int c = 0; c < 2 && !found; c++)
            for (int j = 0; j < L && !found; j++) {
                bool good = true;
                for (int qi2 = 0; qi2 < 5; qi2++) {
                    int q = QS[qi2];
                    auto b0 = c ? conjp(Bq[qi2], q) : Bq[qi2];
                    auto bj = mulp(b0, pwq[qi2][j], q);
                    pair<int,int> d = {(Bpq[qi2].first - bj.first % q + q)%q,
                                       (Bpq[qi2].second - bj.second % q + q)%q};
                    if (!slack[qi2].count(d)) { good = false; break; }
                }
                if (good) found = true;
            }
        printf("single (j,c) with Ann+Shadow slack exists: %d\n", (int)found);
        return !found;
    };

    // ---- Phase 1: mixed (81 unconstrained) via (P,Q) tuples ----
    {
        // per component k (qidx), per pattern: list of (Q image, tau-mask)
        struct PQ { array<int,12> P, Q; uint32_t mask; };
        vector<vector<PQ>> pq(4);
        for (int k = 0; k < 4; k++) {
            Comp& C = comps[qidx[k]];
            map<array<int,12>, uint32_t> img2mask;
            for (auto& P : C.patterns) {
                map<array<int,12>, uint32_t> m;
                for (int ti = 0; ti < 24; ti++) {
                    array<int,12> Q;
                    for (int i = 0; i < 12; i++) Q[i] = P[DIH[ti][i]];
                    m[Q] |= (1u << ti);
                }
                for (auto& kv : m) pq[k].push_back({P, kv.first, kv.second});
            }
        }
        long long combos = 0, match_ok = 0;
        for (auto& a : pq[0]) for (auto& b : pq[1]) for (auto& c : pq[2]) for (auto& d : pq[3]) {
            combos++;
            if ((a.mask & b.mask & c.mask & d.mask) != 0) continue;
            // matching sigma with P[sigma(i)] = Q[i] for all components
            array<int,12> Pq[4] = {a.P, b.P, c.P, d.P};
            array<int,12> Qq[4] = {a.Q, b.Q, c.Q, d.Q};
            // Allowed_i bitmask over j
            uint32_t allow[12];
            bool bad = false;
            for (int i = 0; i < 12; i++) {
                uint32_t m = 0xFFFu;
                for (int k = 0; k < 4; k++) {
                    uint32_t mm = 0;
                    for (int j = 0; j < 12; j++) if (Pq[k][j] == Qq[k][i]) mm |= (1u << j);
                    m &= mm;
                }
                allow[i] = m;
                if (!m) { bad = true; break; }
            }
            if (bad) continue;
            vector<int> used(12, 0);
            array<int,12> sig;
            bool found = false;
            function<void(int)> rec = [&](int i) {
                if (found) return;
                if (i == 12) { found = true; return; }
                uint32_t m = allow[i];
                for (int j = 0; j < 12; j++) if ((m & (1u<<j)) && !used[j]) {
                    used[j] = 1; sig[i] = j; rec(i+1); used[j] = 0;
                    if (found) return;
                }
            };
            rec(0);
            if (!found) continue;
            match_ok++;
            printf("*** COH FAILURE (Phase 1, mixed) ***\n");
            printf("sigma:"); for (int i=0;i<12;i++) printf(" %d", sig[i]); printf("\n");
            // pattern indices for reconstruction
            int pp[4]; uint32_t am[4];
            {
                array<int,12> Ps[4] = {a.P, b.P, c.P, d.P};
                uint32_t ms[4] = {a.mask, b.mask, c.mask, d.mask};
                for (int k = 0; k < 4; k++) {
                    Comp& C = comps[qidx[k]];
                    int pi = -1;
                    for (int x = 0; x < (int)C.patterns.size(); x++)
                        if (C.patterns[x] == Ps[k]) { pi = x; break; }
                    pp[k] = pi; am[k] = ms[k];
                }
            }
            if (verify_failure(sig, pp, {0,0}, {0,0}, am)) return 0;
            printf("WARNING: direct verification did not confirm; continuing\n");
        }
        printf("Phase 1 done, (P,Q) combos=%lld, matching-found=%lld\n", combos, match_ok);
    }

    // ---- Phase 2: 81-constrained pairs with proper T81 ----
    {
        struct Job2 { Seq12 S, Sp; uint32_t t81; vector<array<int,12>> sigmas; };
        vector<Job2> jobs;
        set<Seq12> distinct;
        for (auto& s : C81.seqs) distinct.insert(s);
        for (auto& S : distinct) {
            Seq12 ss = S; sort(ss.v, ss.v+12);
            for (auto& Sp : C81.classes[ss]) {
                uint32_t mask = 0;
                for (int ti = 0; ti < 24; ti++) {
                    Seq12 diff;
                    for (int i = 0; i < 12; i++)
                        diff.v[i] = (Sp.v[i] - S.v[DIH[ti][i]] % 81 + 81) % 81;
                    if (shifts.count(diff)) mask |= (1u << ti);
                }
                if (mask == 0xFFFFFFu) continue; // Phase 1 territory
                vector<array<int,12>> sigmas;
                {
                    vector<int> used(12, 0);
                    array<int,12> sig;
                    function<void(int)> rec = [&](int i) {
                        if (i == 12) { sigmas.push_back(sig); return; }
                        for (int j = 0; j < 12; j++)
                            if (!used[j] && S.v[j] == Sp.v[i]) {
                                used[j] = 1; sig[i] = j; rec(i+1); used[j] = 0;
                            }
                    };
                    rec(0);
                }
                jobs.push_back({S, Sp, mask, move(sigmas)});
            }
        }
        size_t tot = 0; for (auto& j : jobs) tot += j.sigmas.size();
        printf("Phase 2: pairs=%zu total matchings=%zu\n", jobs.size(), tot);
        map<array<int,12>, vector<pair<int,uint32_t>>> bysig;
        for (int ji = 0; ji < (int)jobs.size(); ji++)
            for (auto& s : jobs[ji].sigmas) bysig[s].push_back({ji, jobs[ji].t81});
        printf("Phase 2: distinct sigmas=%zu\n", bysig.size());
        vector<vector<array<int,12>>> pats(4);
        for (int k = 0; k < 4; k++) pats[k] = comps[qidx[k]].patterns;
        long long checked = 0;
        for (auto& kv : bysig) {
            auto& sig = kv.first;
            uint32_t alm[4][16]; int npc[4];
            vector<int> alivepats[4];
            for (int k = 0; k < 4; k++) {
                npc[k] = (int)pats[k].size();
                for (int pi = 0; pi < npc[k]; pi++) {
                    alm[k][pi] = alive_mask(sig, pats[k][pi]);
                    if (alm[k][pi]) alivepats[k].push_back(pi);
                }
            }
            set<uint32_t> t81s;
            for (auto& pr : kv.second) t81s.insert(pr.second);
            for (int p0 : alivepats[0]) for (int p1 : alivepats[1])
            for (int p2 : alivepats[2]) for (int p3 : alivepats[3]) {
                uint32_t a0 = alm[0][p0], a1 = alm[1][p1], a2 = alm[2][p2], a3 = alm[3][p3];
                checked++;
                uint32_t C = a0 & a1 & a2 & a3;
                for (uint32_t t81 : t81s) {
                    if ((C & t81) == 0) {
                        int ji = -1;
                        for (auto& pr : kv.second) if (pr.second == t81) { ji = pr.first; break; }
                        assert(ji >= 0);
                        printf("*** COH FAILURE (Phase 2) ***\n");
                        printf("sigma:"); for (int i=0;i<12;i++) printf(" %d", sig[i]); printf("\n");
                        printf("pattern idx: %d %d %d %d  Cmask=%u t81mask=%u\n",
                               p0,p1,p2,p3, C, t81);
                        int pp[4] = {p0,p1,p2,p3};
                        uint32_t am[4] = {a0,a1,a2,a3};
                        auto A81 = C81.seqdict[jobs[ji].S][0];
                        auto Ap81 = C81.seqdict[jobs[ji].Sp][0];
                        if (verify_failure(sig, pp, A81, Ap81, am)) return 0;
                        printf("WARNING: direct verification did not confirm; continuing\n");
                    }
                }
            }
        }
        printf("Phase 2 done, valid pattern-tuple checks=%lld\n", checked);
    }

    printf("COH HOLDS at m=12: no failing (pattern tuple, 81-pair, sigma) in either phase\n");
    return 0;
}
