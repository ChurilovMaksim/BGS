// Wave 45, task 2 — JBL-grade pairing at m=32, (8192,577), by sampling.
// Definitions follow wave44_GPL_test.py exactly:
//   genuine B in ker(alpha^32 - 1) in R/M (R = Z[sqrt(2)]);
//   sequence s_i = Tr(B alpha^i) mod M; classes r = i mod 4 (t=4);
//   joints per class r = sorted pairs (p_i, o_i), i = r mod 4;
//   global = sorted pairs over all i;
//   JBL check: exists pi in D_4 with j[r] == j0[pi(r)] for all r.
// Sampling design (exhaustive census, 8192 x 332929 pairs, is infeasible):
//   A. Per-B2 slices: for a stratified sample of B2, ALL Bq are enumerated
//      and globals hashed; every exact collision is JBL-checked.
//   B. Random full pairs: random (B2, Bq), globals hashed across the sample
//      (catches cross-B2 collisions).
//   C. Structured siblings: for random (B2, Bq), siblings -Bq, conj(Bq),
//      Bq*beta^k are tested for global equality + JBL check.
#include <bits/stdc++.h>
using namespace std;
using u64 = uint64_t;
const int M2 = 8192, MQ = 577, m = 32, t = 4;

static pair<int,int> mulM(pair<int,int> a, pair<int,int> b, int M){
    return {(int)(((long)a.first*b.first + 2L*a.second*b.second) % M),
            (int)(((long)a.first*b.second + (long)a.second*b.first) % M)};
}
static pair<int,int> pwM(pair<int,int> a, int n, int M){
    pair<int,int> r = {1, 0};
    for (int i = 0; i < n; i++) r = mulM(r, a, M);
    return r;
}
static int gg(int a, int b){ return std::gcd(a, b); }

// genuine(M, m): replicate wave44 solver exactly.
static vector<pair<int,int>> genuine(int M){
    auto d0d1 = pwM({3,2}, m, M);
    int d0 = (d0d1.first - 1 + M) % M, d1 = d0d1.second;
    vector<pair<int,int>> sols;
    for (int x = 0; x < M; x++){
        int rhs = ((-d1 * x) % M + M) % M;
        int g = gg(d0, M);
        if (rhs % g) continue;
        int d0p = d0 / g, Mp = M / g, rhsp = rhs / g;
        int y0 = (int)((long)rhsp * ([](int a, int mod){ // inverse via extended Eucldiean
            long t = 0, nt = 1, r = mod, nr = a % mod;
            while (nr){ long q = r / nr; long tmp = t - q*nt; t = nt; nt = tmp; tmp = r - q*nr; r = nr; nr = tmp; }
            if (r > 1) return -1L; if (t < 0) t += mod; return t; })(d0p, Mp)) % Mp;
        for (int k = 0; k < g; k++){
            int y = y0 + k * Mp;
            if ((d0*x + 2*d1*y) % M == 0 && (d1*x + d0*y) % M == 0) sols.push_back({x, y});
        }
    }
    return sols;
}

static vector<array<int,4>> PERMS;
static void build_perms(){
    // NOTE: C++ % on negatives differs from Python %: must normalize.
    for (int eps : {1, -1}) for (int b = 0; b < t; b++){
        array<int,4> pp;
        for (int r = 0; r < t; r++) pp[r] = ((eps*r + b) % t + t) % t;
        PERMS.push_back(pp);
    }
    // self-test: 8 distinct permutations of {0,1,2,3}
    sort(PERMS.begin(), PERMS.end());
    PERMS.erase(unique(PERMS.begin(), PERMS.end()), PERMS.end());
    if (PERMS.size() != 8){ fprintf(stderr, "PERM SELF-TEST FAILED: %zu perms\n", PERMS.size()); exit(1); }
    for (auto& pp : PERMS){
        array<int,4> s = pp; sort(s.begin(), s.end());
        if (s != array<int,4>{0,1,2,3}){ fprintf(stderr, "PERM SELF-TEST FAILED: not a permutation\n"); exit(1); }
    }
    fprintf(stderr, "perm self-test OK: 8 perms\n");
}

// sequences
static vector<pair<int,int>> POW2, POWQ;
static void seq_of(pair<int,int> B, const vector<pair<int,int>>& pw, int M, int out[32]){
    for (int i = 0; i < m; i++)
        out[i] = (int)((2L * (B.first * pw[i].first + 2L * B.second * pw[i].second)) % M);
}
static int class_period(const int s[32], int r){
    int seq[8];
    for (int k = 0; k < 8; k++) seq[k] = s[r + 4*k];
    for (int p = 1; p <= 8; p++)
        if (8 % p == 0){
            bool ok = true;
            for (int k = 0; k < 8; k++) if (seq[k] != seq[k % p]) ok = false;
            if (ok) return p;
        }
    return 8;
}
struct Joints { // 4 classes x 8 sorted pairs
    array<array<pair<short,short>,8>,4> c;
};
static Joints joints_of(const int p[32], const int o[32]){
    Joints J;
    for (int r = 0; r < t; r++){
        array<pair<short,short>,8> v;
        for (int k = 0; k < 8; k++) v[k] = {(short)p[r+4*k], (short)o[r+4*k]};
        sort(v.begin(), v.end());
        J.c[r] = v;
    }
    return J;
}
static bool jbl_ok(const Joints& J, const Joints& J0){
    for (auto& pp : PERMS){
        bool ok = true;
        for (int r = 0; r < t; r++) if (J.c[r] != J0.c[pp[r]]) ok = false;
        if (ok) return true;
    }
    return false;
}
static bool jbl_ok_id(const Joints& J, const Joints& J0){
    for (int r = 0; r < t; r++) if (J.c[r] != J0.c[r]) return false;
    return true;
}
// global hash: sum of per-position hashes (order-independent), verified exactly on match.
static inline u64 pair_hash(int p, int o){
    u64 z = (u64)(p + 1) * 1000003ULL + (u64)(o + 1) * 9176ULL + 0x9E3779B97F4A7C15ULL;
    z ^= z >> 33; z *= 0xFF51AFD7ED558CCDULL; z ^= z >> 33;
    return z;
}
static bool global_equal(const int p[32], const int o1[32], const int o2[32]){
    pair<short,short> a[32], b[32];
    for (int i = 0; i < 32; i++){ a[i] = {(short)p[i], (short)o1[i]}; b[i] = {(short)p[i], (short)o2[i]}; }
    sort(a, a+32); sort(b, b+32);
    for (int i = 0; i < 32; i++) if (a[i] != b[i]) return false;
    return true;
}
static bool global_equal_cross(const int p1[32], const int o1[32], const int p2[32], const int o2[32]){
    pair<short,short> a[32], b[32];
    for (int i = 0; i < 32; i++){ a[i] = {(short)p1[i], (short)o1[i]}; b[i] = {(short)p2[i], (short)o2[i]}; }
    sort(a, a+32); sort(b, b+32);
    for (int i = 0; i < 32; i++) if (a[i] != b[i]) return false;
    return true;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    build_perms();
    for (int i = 0; i < m; i++){ POW2.push_back(pwM({3,2}, i, M2)); POWQ.push_back(pwM({3,2}, i, MQ)); }
    auto G2 = genuine(M2);
    printf("|G2| = %zu (expect 8192)\n", G2.size());
    // sanity: wave43 witness pattern side must be genuine
    bool w = false;
    for (auto& B : G2) if (B.first == 0 && B.second == 128) w = true;
    printf("witness B2=(0,128) genuine: %d\n", (int)w);
    // alpha^32 mod 577R
    auto a32 = pwM({3,2}, 32, MQ);
    printf("alpha^32 mod 577R = (%d,%d) (expect (1,0): all Bq genuine)\n", a32.first, a32.second);
    // all Bq
    vector<pair<int,int>> GQ;
    for (int x = 0; x < MQ; x++) for (int y = 0; y < MQ; y++) GQ.push_back({x, y});
    printf("|Gq| = %zu\n", GQ.size());

    mt19937_64 rng(20261102ULL);
    // ---- Phase A: stratified per-B2 slices, ALL Bq ----
    // classify B2 by profile
    vector<pair<int,int>> prof1, prof2, prof4;
    vector<int> ptmp(32);
    for (auto& B : G2){
        int s[32]; seq_of(B, POW2, M2, s);
        int p0 = class_period(s, 0);
        if (p0 == 1) prof1.push_back(B); else if (p0 == 2) prof2.push_back(B); else prof4.push_back(B);
    }
    printf("profiles: (1)x%zu (2)x%zu (4)x%zu\n", prof1.size(), prof2.size(), prof4.size());
    vector<pair<int,int>> slices;
    auto pick = [&](vector<pair<int,int>>& v, int n){
        shuffle(v.begin(), v.end(), rng);
        for (int i = 0; i < n && i < (int)v.size(); i++) slices.push_back(v[i]);
    };
    pick(prof1, 100); pick(prof2, 100); pick(prof4, 100);
    slices.push_back({0,128}); slices.push_back({0,64});
    printf("Phase A slices: %zu B2\n", slices.size());
    long long tot_pairs = 0, tot_coll = 0, tot_jblbad = 0, tot_id = 0, tot_nonid = 0, tot_hashfalse = 0;
    vector<tuple<pair<int,int>,pair<int,int>,pair<int,int>>> bad; // (B2, Bq1, Bq2)
    int si = 0;
    for (auto& B2 : slices){
        long long sc = 0, sid = 0, snon = 0, sbad = 0;
        int p[32]; seq_of(B2, POW2, M2, p);
        int prof = class_period(p, 0);
        // per-position hash table: htab[i][o]
        static u64 htab[32][577];
        for (int i = 0; i < 32; i++) for (int o = 0; o < MQ; o++) htab[i][o] = pair_hash(p[i], o);
        unordered_map<u64, pair<int,int>> first;
        first.reserve(1<<20); first.max_load_factor(0.7);
        for (auto& Bq : GQ){
            int o[32]; seq_of(Bq, POWQ, MQ, o);
            u64 gh = 0;
            for (int i = 0; i < 32; i++) gh += htab[i][o[i]];
            auto it = first.find(gh);
            if (it == first.end()){ first[gh] = Bq; continue; }
            int o0[32]; seq_of(it->second, POWQ, MQ, o0);
            if (!global_equal(p, o0, o)){ tot_hashfalse++; continue; }
            tot_coll++; sc++;
            Joints J0 = joints_of(p, o0), J = joints_of(p, o);
            if (jbl_ok(J, J0)){
                if (jbl_ok_id(J, J0)) tot_id++, sid++; else tot_nonid++, snon++;
            } else {
                tot_jblbad++; sbad++;
                if (bad.size() < 5) bad.push_back({B2, it->second, Bq});
            }
        }
        tot_pairs += (long long)GQ.size();
        printf("  slice %d/%zu B2=(%d,%d) prof=%d coll=%lld id=%lld nonid=%lld jblbad=%lld\n",
               ++si, slices.size(), B2.first, B2.second, prof, sc, sid, snon, sbad), fflush(stdout);
    }
    printf("Phase A: pairs=%lld exact_collisions=%lld (id=%lld nonid_pi=%lld) JBL_BAD=%lld hash_false_alarms=%lld\n",
           tot_pairs, tot_coll, tot_id, tot_nonid, tot_jblbad, tot_hashfalse);
    for (auto& b : bad) printf("JBL-BAD slice: B2=(%d,%d) Bq1=(%d,%d) Bq2=(%d,%d)\n",
        get<0>(b).first, get<0>(b).second, get<1>(b).first, get<1>(b).second, get<2>(b).first, get<2>(b).second);

    // ---- Phase B: random full pairs, global hashing across sample ----
    {
        const int N = 3000000;
        unordered_map<u64, tuple<pair<int,int>,pair<int,int>>> first;
        first.reserve(1<<22); first.max_load_factor(0.7);
        long long coll = 0, jblbad = 0, idc = 0, nonid = 0, hfalse = 0;
        uniform_int_distribution<size_t> d2(0, G2.size()-1), dq(0, GQ.size()-1);
        for (int n = 0; n < N; n++){
            auto B2 = G2[d2(rng)], Bq = GQ[dq(rng)];
            int p[32], o[32]; seq_of(B2, POW2, M2, p); seq_of(Bq, POWQ, MQ, o);
            u64 gh = 0; for (int i = 0; i < 32; i++) gh += pair_hash(p[i], o[i]);
            auto it = first.find(gh);
            if (it == first.end()){ first[gh] = {B2, Bq}; continue; }
            auto [B20, Bq0] = it->second;
            int p0[32], o0[32]; seq_of(B20, POW2, M2, p0); seq_of(Bq0, POWQ, MQ, o0);
            if (!global_equal_cross(p0, o0, p, o)){ hfalse++; continue; }
            coll++;
            Joints J0 = joints_of(p0, o0), J = joints_of(p, o);
            if (jbl_ok(J, J0)){ if (jbl_ok_id(J, J0)) idc++; else nonid++; }
            else { jblbad++; if (jblbad <= 5) printf("PhaseB JBL-BAD: (%d,%d)x(%d,%d) vs (%d,%d)x(%d,%d)\n",
                B20.first,B20.second,Bq0.first,Bq0.second,B2.first,B2.second,Bq.first,Bq.second); }
        }
        printf("Phase B: N=%d exact_collisions=%lld (id=%lld nonid_pi=%lld) JBL_BAD=%lld hash_false=%lld\n",
               N, coll, idc, nonid, jblbad, hfalse);
    }

    // ---- Phase C: structured siblings ----
    {
        auto beta = pwM({3,2}, 4, MQ);
        auto beta2 = mulM(beta, beta, MQ), beta3 = mulM(beta2, beta, MQ);
        pair<int,int> betas[4] = {{1,0}, beta, beta2, beta3};
        long long tested = 0, geq = 0, jblbad = 0;
        uniform_int_distribution<size_t> d2(0, G2.size()-1), dq(0, GQ.size()-1);
        for (int n = 0; n < 2000; n++){
            auto B2 = G2[d2(rng)], Bq = GQ[dq(rng)];
            int p[32], o[32]; seq_of(B2, POW2, M2, p); seq_of(Bq, POWQ, MQ, o);
            vector<pair<int,int>> sibs;
            sibs.push_back({(MQ - Bq.first) % MQ, (MQ - Bq.second) % MQ}); // -Bq
            sibs.push_back({Bq.first, (MQ - Bq.second) % MQ});              // conj
            for (int k = 1; k < 4; k++) sibs.push_back(mulM(Bq, betas[k], MQ));
            for (auto& S : sibs){
                tested++;
                int o2[32]; seq_of(S, POWQ, MQ, o2);
                if (!global_equal(p, o, o2)) continue;
                geq++;
                Joints J0 = joints_of(p, o), J = joints_of(p, o2);
                if (!jbl_ok(J, J0)){ jblbad++; printf("PhaseC JBL-BAD: B2=(%d,%d) Bq=(%d,%d) sib=(%d,%d)\n",
                    B2.first,B2.second,Bq.first,Bq.second,S.first,S.second); }
            }
        }
        printf("Phase C: sibling_tests=%lld global_equal=%lld JBL_BAD=%lld\n", tested, geq, jblbad);
    }

    // ---- Odd-period stats on a random sample ----
    {
        int cnt1 = 0, cnt2 = 0, cnt4 = 0, cntother = 0;
        uniform_int_distribution<size_t> dq(0, GQ.size()-1);
        for (int n = 0; n < 20000; n++){
            auto Bq = GQ[dq(rng)];
            int o[32]; seq_of(Bq, POWQ, MQ, o);
            // per-class period profile: use class 0..3, count Bq by max period? report class-0 period
            int per = class_period(o, 0);
            if (per == 1) cnt1++; else if (per == 2) cnt2++; else if (per == 4) cnt4++; else cntother++;
        }
        printf("Odd class-0 periods over 20000 random Bq: 1:%d 2:%d 4:%d other:%d\n", cnt1, cnt2, cnt4, cntother);
    }
    printf("DONE\n");
    return 0;
}
