// Full census at j = 13 (m = p = 8192) for the Gap G ladder prediction:
// exactly two step-64 chains of 8 with contribution +-16 per point.
// Grid: t odd in [1,65536), u = (11t + 16*U0) mod 65536, U0 in [0,4096).
// Q = 2^29, so all mod-Q arithmetic is masking; 6*y fits in uint32.
// NOTE vs j=12: the shift-8 digit here is mod 256 (diff divisible by
// Q/256 = 2^21, not Q/128); B2 is E mod 4 == phi mod 4 with that digit.
// OpenMP-parallel over t. argv[1] optionally limits NT (smoke tests).
#include <cstdio>
#include <cstdint>
#include <cstdlib>
#include <cstring>
#include <map>
#include <string>
#include <algorithm>
#include <omp.h>

static const uint32_t Q = 1u << 29;
static const uint32_t MASK = Q - 1;
static const uint32_t STEP0 = 8192;
static const int P = 8192;
static const int QQ = 1024;  // p/8 quarter indices
static const int PJ = 512;   // p/16 pair indices
static const uint32_t MU = 1u << 21; // Q/256

struct Stats {
    long npoints = 0, valid = 0, bad_period = 0, bad_min = 0, bad_nu = 0;
    long D_nondiv = 0, eps_non01 = 0, phi_nondiv = 0, B2_bad = 0;
    long reps_bad = 0, spacing_bad = 0, ap_bad = 0, diff_non4 = 0, delta_even = 0;
    long E_non0mod4 = 0;
    long cond64_total = 0, cond64_class_const = 0, nonzero_not_cond64 = 0;
    long chain_pos = 0, chain_neg = 0;
    std::map<std::string, long> sizes_hist, contribs_hist, wit_hist, share_hist;
    std::map<std::string, long> witclass_hist, nonzero_hist, chainpair_hist;
    void merge(const Stats &o) {
        npoints += o.npoints; valid += o.valid;
        bad_period += o.bad_period; bad_min += o.bad_min; bad_nu += o.bad_nu;
        D_nondiv += o.D_nondiv; eps_non01 += o.eps_non01;
        phi_nondiv += o.phi_nondiv; B2_bad += o.B2_bad;
        reps_bad += o.reps_bad; spacing_bad += o.spacing_bad; ap_bad += o.ap_bad;
        diff_non4 += o.diff_non4; delta_even += o.delta_even; E_non0mod4 += o.E_non0mod4;
        cond64_total += o.cond64_total; cond64_class_const += o.cond64_class_const;
        nonzero_not_cond64 += o.nonzero_not_cond64;
        chain_pos += o.chain_pos; chain_neg += o.chain_neg;
        for (auto &kv : o.sizes_hist) sizes_hist[kv.first] += kv.second;
        for (auto &kv : o.contribs_hist) contribs_hist[kv.first] += kv.second;
        for (auto &kv : o.wit_hist) wit_hist[kv.first] += kv.second;
        for (auto &kv : o.share_hist) share_hist[kv.first] += kv.second;
        for (auto &kv : o.witclass_hist) witclass_hist[kv.first] += kv.second;
        for (auto &kv : o.nonzero_hist) nonzero_hist[kv.first] += kv.second;
        for (auto &kv : o.chainpair_hist) chainpair_hist[kv.first] += kv.second;
    }
};

int main(int argc, char **argv) {
    Stats total;
    const int NT = (argc > 1) ? atoi(argv[1]) : 32768; // t = 2*ti+1
    #pragma omp parallel
    {
        Stats st;
        uint32_t W[2048];
        int E[PJ], eps[PJ], phi[PJ], vv[PJ], tt[PJ];
        #pragma omp for schedule(dynamic, 64)
        for (int ti = 0; ti < NT; ++ti) {
            if (ti % 8192 == 0) {
                #pragma omp critical
                fprintf(stderr, "ti %d\n", ti);
            }
            int t = 2 * ti + 1;
            for (int U0 = 0; U0 < 4096; ++U0) {
                ++st.npoints;
                uint32_t u = (11u * (uint32_t)t + 16u * (uint32_t)U0) % 65536u;
                uint32_t y0 = STEP0 * (uint32_t)t;
                uint32_t y1 = STEP0 * u;
                uint32_t y_prev = y0, y_curr = y1;
                uint32_t s4096 = 0, s4097 = 0, s8192 = 0, s8193 = 0;
                W[0] = y_curr;
                for (int nn = 1; nn <= P + 1; ++nn) {
                    uint32_t y_next = (6u * y_curr - y_prev) & MASK;
                    y_prev = y_curr; y_curr = y_next;
                    if ((nn % 2) == 0 && nn / 2 < 2048) W[nn / 2] = y_curr;
                    if (nn + 1 == 4096) s4096 = y_curr;
                    if (nn + 1 == 4097) s4097 = y_curr;
                    if (nn + 1 == 8192) s8192 = y_curr;
                    if (nn + 1 == 8193) s8193 = y_curr;
                }
                bool per_ok = (s8192 == y0) && (s8193 == y1);
                bool min_ok = !((s4096 == y0) && (s4097 == y1));
                bool nu_ok = (((s4096 - y0) & MASK) == Q / 2) && (((s4097 - y1) & MASK) == 0);
                if (!per_ok) { ++st.bad_period; continue; }
                if (!min_ok) { ++st.bad_min; continue; }
                if (!nu_ok) { ++st.bad_nu; continue; }
                ++st.valid;
                for (int j = 0; j < PJ; ++j) {
                    uint32_t diff = (W[j + 8] - W[j]) & MASK;
                    if (diff & (MU - 1)) ++st.D_nondiv;
                    E[j] = (int)(diff >> 21); // mod 256
                    uint32_t de = (W[j + QQ] - W[j]) & MASK;
                    if (de & (Q / 2 - 1)) ++st.eps_non01;
                    eps[j] = (int)(de / (Q / 2));
                    uint32_t dp = (W[j + PJ] - W[j]) & MASK;
                    if (dp & (Q / 4 - 1)) ++st.phi_nondiv;
                    phi[j] = (int)((dp / (Q / 4)) % 4);
                    vv[j] = (int)(W[j] & (Q / 2 - 1));
                    tt[j] = (int)(W[j] / (Q / 2));
                    if ((E[j] & 3) != (phi[j] & 3)) ++st.B2_bad;
                }
                int reps[PJ], nr = 0;
                for (int j = 0; j < PJ; ++j)
                    if (eps[j] == 0 && phi[j] == 0) reps[nr++] = j;
                if (nr != 128) { ++st.reps_bad; continue; }
                bool sp = true;
                for (int i = 0; i + 1 < nr; ++i) if (reps[i + 1] - reps[i] != 4) sp = false;
                if (!sp) { ++st.spacing_bad; continue; }
                int d = (E[reps[1]] - E[reps[0]] + 256) % 256;
                bool ap = true;
                for (int i = 0; i + 1 < nr; ++i)
                    if ((E[reps[i + 1]] - E[reps[i]] + 256) % 256 != d) ap = false;
                if (!ap) { ++st.ap_bad; continue; }
                if (d % 4 != 0) { ++st.diff_non4; continue; }
                int dE = (d / 4) % 64; // delta_E mod 64
                if (dE % 2 == 0) ++st.delta_even;
                bool e4 = true;
                for (int i = 0; i < nr; ++i) if (E[reps[i]] % 4 != 0) e4 = false;
                if (!e4) ++st.E_non0mod4;
                int dE32 = dE % 32, dE8 = dE % 8;
                int wit = 0, share = 0;
                int S[128];
                for (int i = 0; i < nr; ++i) {
                    S[i] = (E[reps[i]] + 4 * dE32) % 128;
                    if (S[i] == 0) ++wit;
                    if (S[i] % 64 == 0) ++share;
                }
                st.wit_hist["wit_" + std::to_string(wit)]++;
                st.share_hist["share_" + std::to_string(share)]++;
                // classes by v
                int cls[128][128], clen[128], nc = 0;
                for (int i = 0; i < nr; ++i) {
                    int c = -1;
                    for (int k = 0; k < nc; ++k)
                        if (vv[reps[cls[k][0]]] == vv[reps[i]]) { c = k; break; }
                    if (c < 0) { c = nc++; clen[c] = 0; }
                    cls[c][clen[c]++] = i;
                }
                int sizes[128]; for (int k = 0; k < nc; ++k) sizes[k] = clen[k];
                std::sort(sizes, sizes + nc);
                std::string sk = "sizes";
                for (int k = 0; k < nc; ++k) sk += "_" + std::to_string(sizes[k]);
                st.sizes_hist[sk]++;
                int contribs[128], nnonzero = 0;
                for (int k = 0; k < nc; ++k) {
                    int s = 0;
                    for (int a = 0; a < clen[k]; ++a) s += 2 * (1 - 2 * tt[reps[cls[k][a]]]);
                    contribs[k] = s;
                    if (s != 0) ++nnonzero;
                }
                st.nonzero_hist["nonzero_" + std::to_string(nnonzero)]++;
                std::sort(contribs, contribs + nc);
                std::string ck = "contribs";
                for (int k = 0; k < nc; ++k) ck += "_" + std::to_string(contribs[k]);
                st.contribs_hist[ck]++;
                // witness reps' class: size + contribution (informational)
                {
                    int wi = -1;
                    for (int i = 0; i < nr; ++i) if (S[i] == 0) { wi = i; break; }
                    if (wi >= 0) {
                        for (int k = 0; k < nc; ++k) {
                            bool has = false;
                            for (int a = 0; a < clen[k]; ++a) if (cls[k][a] == wi) has = true;
                            if (has) {
                                int s = 0;
                                for (int a = 0; a < clen[k]; ++a) s += 2 * (1 - 2 * tt[reps[cls[k][a]]]);
                                st.witclass_hist["witclass_size_" + std::to_string(clen[k])
                                    + "_contrib_" + std::to_string(s)]++;
                                break;
                            }
                        }
                    }
                }
                // step-64 chains (ordinals mod 8 -> two chains spaced 16):
                // condition E + 28*delta_E == 0 mod 32
                int chain_signs[2], nchains = 0;
                for (int c = 0; c < 8; ++c) {
                    int cond = (E[reps[c]] + 28 * dE8) % 32;
                    if (cond != 0) continue;
                    for (int baseoff = 0; baseoff < 2; ++baseoff) {
                        int base = c + 8 * baseoff;
                        ++st.cond64_total;
                        // members ordinals base+16a (a<8): exactly one class? constant t?
                        int k0 = -1;
                        for (int k = 0; k < nc; ++k) {
                            bool has = false;
                            for (int a = 0; a < clen[k]; ++a) if (cls[k][a] == base) has = true;
                            if (has) { k0 = k; break; }
                        }
                        bool exact = (k0 >= 0 && clen[k0] == 8);
                        if (exact) {
                            for (int a = 0; a < 8; ++a) {
                                bool member = false;
                                for (int b = 0; b < clen[k0]; ++b) if (cls[k0][b] == base + 16 * a) member = true;
                                if (!member) exact = false;
                            }
                            int t0 = tt[reps[cls[k0][0]]];
                            for (int a = 0; a < clen[k0]; ++a)
                                if (tt[reps[cls[k0][a]]] != t0) exact = false;
                        }
                        if (exact) {
                            ++st.cond64_class_const;
                            int s = 0;
                            for (int a = 0; a < clen[k0]; ++a) s += 2 * (1 - 2 * tt[reps[cls[k0][a]]]);
                            if (s == 16) { ++st.chain_pos; chain_signs[nchains++] = 1; }
                            else if (s == -16) { ++st.chain_neg; chain_signs[nchains++] = -1; }
                            else nchains = -100; // unexpected contribution
                        }
                    }
                }
                if (nchains == 2) {
                    std::string pk = (chain_signs[0] > 0 && chain_signs[1] > 0) ? "pair_pp"
                        : (chain_signs[0] < 0 && chain_signs[1] < 0) ? "pair_nn" : "pair_pn";
                    st.chainpair_hist[pk]++;
                } else {
                    st.chainpair_hist["pair_other"]++;
                }
                // nonzero classes that are not cond-64 chains
                for (int k = 0; k < nc; ++k) {
                    int s = 0;
                    for (int a = 0; a < clen[k]; ++a) s += 2 * (1 - 2 * tt[reps[cls[k][a]]]);
                    if (s == 0) continue;
                    bool iscond = false;
                    if (clen[k] == 8) {
                        int ords[8];
                        for (int a = 0; a < 8; ++a) ords[a] = cls[k][a];
                        std::sort(ords, ords + 8);
                        if (ords[0] % 8 == ords[1] % 8) {
                            bool spaced = true;
                            for (int a = 0; a + 1 < 8; ++a) if (ords[a + 1] - ords[a] != 16) spaced = false;
                            if (spaced && (E[reps[ords[0]]] + 28 * dE8) % 32 == 0) iscond = true;
                        }
                    }
                    if (!iscond) ++st.nonzero_not_cond64;
                }
            }
        }
        #pragma omp critical
        total.merge(st);
    }
    printf("npoints %ld\nvalid %ld\nbad_period %ld\nbad_min %ld\nbad_nu %ld\n",
           total.npoints, total.valid, total.bad_period, total.bad_min, total.bad_nu);
    printf("D_nondiv %ld\neps_non01 %ld\nphi_nondiv %ld\nB2_bad %ld\n",
           total.D_nondiv, total.eps_non01, total.phi_nondiv, total.B2_bad);
    printf("reps_bad %ld\nspacing_bad %ld\nap_bad %ld\ndiff_non4 %ld\ndelta_even %ld\nE_non0mod4 %ld\n",
           total.reps_bad, total.spacing_bad, total.ap_bad, total.diff_non4, total.delta_even, total.E_non0mod4);
    printf("cond64_total %ld\ncond64_class_const %ld\nnonzero_not_cond64 %ld\n",
           total.cond64_total, total.cond64_class_const, total.nonzero_not_cond64);
    printf("chain_pos %ld\nchain_neg %ld\n", total.chain_pos, total.chain_neg);
    for (auto &kv : total.wit_hist) printf("%s %ld\n", kv.first.c_str(), kv.second);
    for (auto &kv : total.share_hist) printf("%s %ld\n", kv.first.c_str(), kv.second);
    for (auto &kv : total.sizes_hist) printf("%s %ld\n", kv.first.c_str(), kv.second);
    for (auto &kv : total.contribs_hist) printf("%s %ld\n", kv.first.c_str(), kv.second);
    for (auto &kv : total.witclass_hist) printf("%s %ld\n", kv.first.c_str(), kv.second);
    for (auto &kv : total.nonzero_hist) printf("%s %ld\n", kv.first.c_str(), kv.second);
    for (auto &kv : total.chainpair_hist) printf("%s %ld\n", kv.first.c_str(), kv.second);
    return 0;
}
