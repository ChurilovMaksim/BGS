// Full census at j = 12 (m = p = 4096) for the Gap G ladder prediction:
// exactly one step-32 chain of 8 with contribution +-16 per point.
// Grid: t odd in [1,32768), u = (11t + 16*U0) mod 32768, U0 in [0,2048).
// Q = 2^27, so all mod-Q arithmetic is masking; 6*y fits in uint32.
// OpenMP-parallel over t.
#include <cstdio>
#include <cstdint>
#include <cstring>
#include <map>
#include <string>
#include <algorithm>
#include <omp.h>

static const uint32_t Q = 1u << 27;
static const uint32_t MASK = Q - 1;
static const uint32_t STEP0 = 4096;
static const int P = 4096;
static const int QQ = 512;   // p/8 quarter indices
static const int PJ = 256;   // p/16 pair indices
static const uint32_t MU = 1u << 20; // Q/128

struct Stats {
    long npoints = 0, valid = 0, bad_period = 0, bad_min = 0, bad_nu = 0;
    long D_nondiv = 0, eps_non01 = 0, phi_nondiv = 0, B2_bad = 0;
    long reps_bad = 0, spacing_bad = 0, ap_bad = 0, diff_non4 = 0, delta_even = 0;
    long E_non0mod4 = 0;
    long cond32_total = 0, cond32_class_const = 0, nonzero_not_cond32 = 0;
    long chain_pos = 0, chain_neg = 0;
    std::map<std::string, long> sizes_hist, contribs_hist, wit_hist, share_hist;
    std::map<std::string, long> witclass_hist, nonzero_hist;
    void merge(const Stats &o) {
        npoints += o.npoints; valid += o.valid;
        bad_period += o.bad_period; bad_min += o.bad_min; bad_nu += o.bad_nu;
        D_nondiv += o.D_nondiv; eps_non01 += o.eps_non01;
        phi_nondiv += o.phi_nondiv; B2_bad += o.B2_bad;
        reps_bad += o.reps_bad; spacing_bad += o.spacing_bad; ap_bad += o.ap_bad;
        diff_non4 += o.diff_non4; delta_even += o.delta_even; E_non0mod4 += o.E_non0mod4;
        cond32_total += o.cond32_total; cond32_class_const += o.cond32_class_const;
        nonzero_not_cond32 += o.nonzero_not_cond32;
        chain_pos += o.chain_pos; chain_neg += o.chain_neg;
        for (auto &kv : o.sizes_hist) sizes_hist[kv.first] += kv.second;
        for (auto &kv : o.contribs_hist) contribs_hist[kv.first] += kv.second;
        for (auto &kv : o.wit_hist) wit_hist[kv.first] += kv.second;
        for (auto &kv : o.share_hist) share_hist[kv.first] += kv.second;
        for (auto &kv : o.witclass_hist) witclass_hist[kv.first] += kv.second;
        for (auto &kv : o.nonzero_hist) nonzero_hist[kv.first] += kv.second;
    }
};

int main() {
    Stats total;
    const int NT = 16384; // t = 2*ti+1
    #pragma omp parallel
    {
        Stats st;
        uint32_t W[1024];
        int E[PJ], eps[PJ], phi[PJ], vv[PJ], tt[PJ];
        #pragma omp for schedule(dynamic, 64)
        for (int ti = 0; ti < NT; ++ti) {
            int t = 2 * ti + 1;
            for (int U0 = 0; U0 < 2048; ++U0) {
                ++st.npoints;
                uint32_t u = (11u * (uint32_t)t + 16u * (uint32_t)U0) % 32768u;
                uint32_t y0 = STEP0 * (uint32_t)t;
                uint32_t y1 = STEP0 * u;
                uint32_t y_prev = y0, y_curr = y1;
                uint32_t s2048 = 0, s2049 = 0, s4096 = 0, s4097 = 0;
                W[0] = y_curr;
                for (int nn = 1; nn <= P + 1; ++nn) {
                    uint32_t y_next = (6u * y_curr - y_prev) & MASK;
                    y_prev = y_curr; y_curr = y_next;
                    if ((nn % 2) == 0 && nn / 2 < 1024) W[nn / 2] = y_curr;
                    if (nn + 1 == 2048) s2048 = y_curr;
                    if (nn + 1 == 2049) s2049 = y_curr;
                    if (nn + 1 == 4096) s4096 = y_curr;
                    if (nn + 1 == 4097) s4097 = y_curr;
                }
                bool per_ok = (s4096 == y0) && (s4097 == y1);
                bool min_ok = !((s2048 == y0) && (s2049 == y1));
                bool nu_ok = (((s2048 - y0) & MASK) == Q / 2) && (((s2049 - y1) & MASK) == 0);
                if (!per_ok) { ++st.bad_period; continue; }
                if (!min_ok) { ++st.bad_min; continue; }
                if (!nu_ok) { ++st.bad_nu; continue; }
                ++st.valid;
                for (int j = 0; j < PJ; ++j) {
                    uint32_t diff = (W[j + 8] - W[j]) & MASK;
                    if (diff & (MU - 1)) ++st.D_nondiv;
                    E[j] = (int)(diff >> 20); // mod 128
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
                if (nr != 64) { ++st.reps_bad; continue; }
                bool sp = true;
                for (int i = 0; i + 1 < nr; ++i) if (reps[i + 1] - reps[i] != 4) sp = false;
                if (!sp) { ++st.spacing_bad; continue; }
                int d = (E[reps[1]] - E[reps[0]] + 128) % 128;
                bool ap = true;
                for (int i = 0; i + 1 < nr; ++i)
                    if ((E[reps[i + 1]] - E[reps[i]] + 128) % 128 != d) ap = false;
                if (!ap) { ++st.ap_bad; continue; }
                if (d % 4 != 0) { ++st.diff_non4; continue; }
                int dE = d / 4; // delta_E mod 32
                if (dE % 2 == 0) ++st.delta_even;
                bool e4 = true;
                for (int i = 0; i < nr; ++i) if (E[reps[i]] % 4 != 0) e4 = false;
                if (!e4) ++st.E_non0mod4;
                int dE16 = dE % 16, dE8 = dE % 8;
                int wit = 0, share = 0;
                int S[64];
                for (int i = 0; i < nr; ++i) {
                    S[i] = (E[reps[i]] + 4 * dE16) % 64;
                    if (S[i] == 0) ++wit;
                    if (S[i] % 32 == 0) ++share;
                }
                st.wit_hist["wit_" + std::to_string(wit)]++;
                st.share_hist["share_" + std::to_string(share)]++;
                // classes by v
                int cls[64][64], clen[64], nc = 0;
                for (int i = 0; i < nr; ++i) {
                    int c = -1;
                    for (int k = 0; k < nc; ++k)
                        if (vv[reps[cls[k][0]]] == vv[reps[i]]) { c = k; break; }
                    if (c < 0) { c = nc++; clen[c] = 0; }
                    cls[c][clen[c]++] = i;
                }
                int sizes[64]; for (int k = 0; k < nc; ++k) sizes[k] = clen[k];
                std::sort(sizes, sizes + nc);
                std::string sk = "sizes";
                for (int k = 0; k < nc; ++k) sk += "_" + std::to_string(sizes[k]);
                st.sizes_hist[sk]++;
                int contribs[64], nnonzero = 0;
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
                // step-32 chains (ordinals mod 8): condition E + 12*delta_E == 0 mod 32
                for (int c = 0; c < 8; ++c) {
                    int cond = (E[reps[c]] + 12 * dE8) % 32;
                    if (cond != 0) continue;
                    ++st.cond32_total;
                    // members ordinals c+8a (a<8): exactly one class? constant t?
                    int k0 = -1;
                    for (int k = 0; k < nc; ++k) {
                        bool has = false;
                        for (int a = 0; a < clen[k]; ++a) if (cls[k][a] == c) has = true;
                        if (has) { k0 = k; break; }
                    }
                    bool exact = (k0 >= 0 && clen[k0] == 8);
                    if (exact) {
                        for (int a = 0; a < 8; ++a) {
                            bool member = false;
                            for (int b = 0; b < clen[k0]; ++b) if (cls[k0][b] == c + 8 * a) member = true;
                            if (!member) exact = false;
                        }
                        int t0 = tt[reps[cls[k0][0]]];
                        for (int a = 0; a < clen[k0]; ++a)
                            if (tt[reps[cls[k0][a]]] != t0) exact = false;
                    }
                    if (exact) {
                        ++st.cond32_class_const;
                        int s = 0;
                        for (int a = 0; a < clen[k0]; ++a) s += 2 * (1 - 2 * tt[reps[cls[k0][a]]]);
                        if (s == 16) ++st.chain_pos; else if (s == -16) ++st.chain_neg;
                    }
                }
                // nonzero classes that are not cond-32 chains
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
                            for (int a = 0; a + 1 < 8; ++a) if (ords[a + 1] - ords[a] != 8) spaced = false;
                            if (spaced && (E[reps[ords[0]]] + 12 * dE8) % 32 == 0) iscond = true;
                        }
                    }
                    if (!iscond) ++st.nonzero_not_cond32;
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
    printf("cond32_total %ld\ncond32_class_const %ld\nnonzero_not_cond32 %ld\n",
           total.cond32_total, total.cond32_class_const, total.nonzero_not_cond32);
    printf("chain_pos %ld\nchain_neg %ld\n", total.chain_pos, total.chain_neg);
    for (auto &kv : total.wit_hist) printf("%s %ld\n", kv.first.c_str(), kv.second);
    for (auto &kv : total.share_hist) printf("%s %ld\n", kv.first.c_str(), kv.second);
    for (auto &kv : total.sizes_hist) printf("%s %ld\n", kv.first.c_str(), kv.second);
    for (auto &kv : total.contribs_hist) printf("%s %ld\n", kv.first.c_str(), kv.second);
    for (auto &kv : total.witclass_hist) printf("%s %ld\n", kv.first.c_str(), kv.second);
    for (auto &kv : total.nonzero_hist) printf("%s %ld\n", kv.first.c_str(), kv.second);
    return 0;
}
