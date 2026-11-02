// Full census at j = 11 (m = p = 2048) for the Gap G mod-16/step-32 analysis.
// Grid: t odd in [1,16384), u = (11t + 16*U0) mod 16384, U0 in [0,1024).
// Q = 2^25, so all mod-Q arithmetic is masking; 6*y fits in uint32.
#include <cstdio>
#include <cstdint>
#include <cstring>
#include <map>
#include <string>
#include <algorithm>

static const uint32_t Q = 1u << 25;
static const uint32_t MASK = Q - 1;
static const uint32_t STEP0 = 2048;
static const int P = 2048;
static const int QQ = 256;   // p/8 quarter indices
static const int PJ = 128;   // p/16 pair indices
static const uint32_t MU = 1u << 19; // Q/64

int main() {
    long npoints = 0, valid = 0, bad_period = 0, bad_min = 0, bad_nu = 0;
    long D_nondiv = 0, eps_non01 = 0, phi_nondiv = 0, B2_bad = 0;
    long reps_bad = 0, spacing_bad = 0, ap_bad = 0, diff_non4 = 0, delta_even = 0;
    long E_non0mod4 = 0, dd32_bad = 0;
    long wit_class_nonzero = 0, wit_class_notsize8 = 0;
    long cond32_total = 0, cond32_class_const = 0, nonzero_not_cond32 = 0;
    std::map<std::string, long> sizes_hist, contribs_hist, wit_hist, share_hist;
    uint32_t W[512];
    int E[PJ], eps[PJ], phi[PJ], vv[PJ], tt[PJ];
    for (int t = 1; t < 16384; t += 2) {
        for (int U0 = 0; U0 < 1024; ++U0) {
            ++npoints;
            if ((npoints % 1000000) == 0) fprintf(stderr, "progress %ld\n", npoints);
            uint32_t u = (11u * (uint32_t)t + 16u * (uint32_t)U0) % 16384u;
            uint32_t y0 = STEP0 * (uint32_t)t;
            uint32_t y1 = STEP0 * u;
            uint32_t y_prev = y0, y_curr = y1;
            uint32_t s1024 = 0, s1025 = 0, s2048 = 0, s2049 = 0;
            W[0] = y_curr;
            for (int nn = 1; nn <= P + 1; ++nn) {
                uint32_t y_next = (6u * y_curr - y_prev) & MASK;
                y_prev = y_curr; y_curr = y_next;
                if ((nn % 2) == 0 && nn / 2 < 512) W[nn / 2] = y_curr;
                if (nn + 1 == 1024) s1024 = y_curr;
                if (nn + 1 == 1025) s1025 = y_curr;
                if (nn + 1 == 2048) s2048 = y_curr;
                if (nn + 1 == 2049) s2049 = y_curr;
            }
            bool per_ok = (s2048 == y0) && (s2049 == y1);
            bool min_ok = !((s1024 == y0) && (s1025 == y1));
            bool nu_ok = (((s1024 - y0) & MASK) == Q / 2) && (((s1025 - y1) & MASK) == 0);
            if (!per_ok) { ++bad_period; continue; }
            if (!min_ok) { ++bad_min; continue; }
            if (!nu_ok) { ++bad_nu; continue; }
            ++valid;
            for (int j = 0; j < PJ; ++j) {
                uint32_t diff = (W[j + 8] - W[j]) & MASK;
                if (diff & (MU - 1)) ++D_nondiv;
                E[j] = (int)(diff >> 19); // mod 64
                uint32_t de = (W[j + QQ] - W[j]) & MASK;
                if (de & (Q / 2 - 1)) ++eps_non01;
                eps[j] = (int)(de / (Q / 2));
                uint32_t dp = (W[j + PJ] - W[j]) & MASK;
                if (dp & (Q / 4 - 1)) ++phi_nondiv;
                phi[j] = (int)((dp / (Q / 4)) % 4);
                vv[j] = (int)(W[j] & (Q / 2 - 1));
                tt[j] = (int)(W[j] / (Q / 2));
                if ((E[j] & 3) != (phi[j] & 3)) ++B2_bad;
            }
            // consecutive-diff mod 32 constancy (secondary observation)
            {
                int c0 = (E[1] - E[0]) & 31;
                bool ok = true;
                for (int j = 1; j + 1 < PJ; ++j)
                    if (((E[j + 1] - E[j]) & 31) != c0) { ok = false; break; }
                if (!ok) ++dd32_bad;
            }
            int reps[PJ], nr = 0;
            for (int j = 0; j < PJ; ++j)
                if (eps[j] == 0 && phi[j] == 0) reps[nr++] = j;
            if (nr != 32) { ++reps_bad; continue; }
            bool sp = true;
            for (int i = 0; i + 1 < nr; ++i) if (reps[i + 1] - reps[i] != 4) sp = false;
            if (!sp) { ++spacing_bad; continue; }
            int d = (E[reps[1]] - E[reps[0]] + 64) % 64;
            bool ap = true;
            for (int i = 0; i + 1 < nr; ++i)
                if ((E[reps[i + 1]] - E[reps[i]] + 64) % 64 != d) ap = false;
            if (!ap) { ++ap_bad; continue; }
            if (d % 4 != 0) { ++diff_non4; continue; }
            int dE16 = d / 4; // delta_E mod 16
            if (dE16 % 2 == 0) ++delta_even;
            bool e4 = true;
            for (int i = 0; i < nr; ++i) if (E[reps[i]] % 4 != 0) e4 = false;
            if (!e4) ++E_non0mod4;
            int dE8 = dE16 % 8, dE4 = dE16 % 4;
            int wit = 0, share = 0;
            int S[32];
            for (int i = 0; i < nr; ++i) {
                S[i] = (E[reps[i]] + 4 * dE8) % 32;
                if (S[i] == 0) ++wit;
                if (S[i] % 16 == 0) ++share;
            }
            wit_hist["wit_" + std::to_string(wit)]++;
            share_hist["share_" + std::to_string(share)]++;
            // classes by v
            int cls[32][32], clen[32], nc = 0;
            for (int i = 0; i < nr; ++i) {
                int c = -1;
                for (int k = 0; k < nc; ++k)
                    if (vv[reps[cls[k][0]]] == vv[reps[i]]) { c = k; break; }
                if (c < 0) { c = nc++; clen[c] = 0; }
                cls[c][clen[c]++] = i;
            }
            int sizes[32]; for (int k = 0; k < nc; ++k) sizes[k] = clen[k];
            std::sort(sizes, sizes + nc);
            std::string sk = "sizes";
            for (int k = 0; k < nc; ++k) sk += "_" + std::to_string(sizes[k]);
            sizes_hist[sk]++;
            int contribs[32], nnonzero = 0;
            for (int k = 0; k < nc; ++k) {
                int s = 0;
                for (int a = 0; a < clen[k]; ++a) s += 2 * (1 - 2 * tt[reps[cls[k][a]]]);
                contribs[k] = s;
                if (s != 0) ++nnonzero;
            }
            std::sort(contribs, contribs + nc);
            std::string ck = "contribs";
            for (int k = 0; k < nc; ++k) ck += "_" + std::to_string(contribs[k]);
            contribs_hist[ck]++;
            // witness reps' class: expect size 8, contrib 0
            {
                int wi = -1;
                for (int i = 0; i < nr; ++i) if (S[i] == 0) { wi = i; break; }
                if (wi >= 0) {
                    for (int k = 0; k < nc; ++k) {
                        bool has = false;
                        for (int a = 0; a < clen[k]; ++a) if (cls[k][a] == wi) has = true;
                        if (has) {
                            // contribs[] was sorted, so recompute this class's sum
                            int s = 0;
                            for (int a = 0; a < clen[k]; ++a) s += 2 * (1 - 2 * tt[reps[cls[k][a]]]);
                            if (s != 0) ++wit_class_nonzero;
                            if (clen[k] != 8) ++wit_class_notsize8;
                            break;
                        }
                    }
                }
            }
            // step-32 chains (ordinals mod 8): condition E + 12*delta_E == 0 mod 16
            for (int c = 0; c < 8; ++c) {
                int cond = (E[reps[c]] + 12 * dE4) % 16;
                if (cond != 0) continue;
                ++cond32_total;
                // members ordinals c, c+8, c+16, c+24: same class? constant t?
                int k0 = reps[c], v0 = vv[k0], t0 = tt[k0];
                bool same = true, tconst = true;
                for (int a = 1; a < 4; ++a) {
                    int kk = reps[c + 8 * a];
                    if (vv[kk] != v0) same = false;
                    if (tt[kk] != t0) tconst = false;
                }
                if (same && tconst) ++cond32_class_const;
            }
            // nonzero classes that are not cond-32 chains: check via membership
            for (int k = 0; k < nc; ++k) {
                int s = 0;
                for (int a = 0; a < clen[k]; ++a) s += 2 * (1 - 2 * tt[reps[cls[k][a]]]);
                if (s == 0) continue;
                // is this class exactly a cond-32 chain?
                bool iscond = false;
                if (clen[k] == 4) {
                    int ords[4];
                    for (int a = 0; a < 4; ++a) {
                        // find ordinal of member
                        for (int i = 0; i < nr; ++i) if (cls[k][a] == i) ords[a] = i;
                    }
                    std::sort(ords, ords + 4);
                    if (ords[1] - ords[0] == 8 && ords[2] - ords[1] == 8 && ords[3] - ords[2] == 8) {
                        int cond = (E[reps[ords[0]]] + 12 * dE4) % 16;
                        if (cond == 0) iscond = true;
                    }
                }
                if (!iscond) ++nonzero_not_cond32;
            }
        }
    }
    printf("npoints %ld\nvalid %ld\nbad_period %ld\nbad_min %ld\nbad_nu %ld\n",
           npoints, valid, bad_period, bad_min, bad_nu);
    printf("D_nondiv %ld\neps_non01 %ld\nphi_nondiv %ld\nB2_bad %ld\n",
           D_nondiv, eps_non01, phi_nondiv, B2_bad);
    printf("reps_bad %ld\nspacing_bad %ld\nap_bad %ld\ndiff_non4 %ld\ndelta_even %ld\nE_non0mod4 %ld\ndd32_bad %ld\n",
           reps_bad, spacing_bad, ap_bad, diff_non4, delta_even, E_non0mod4, dd32_bad);
    printf("wit_class_nonzero %ld\nwit_class_notsize8 %ld\n",
           wit_class_nonzero, wit_class_notsize8);
    printf("cond32_total %ld\ncond32_class_const %ld\nnonzero_not_cond32 %ld\n",
           cond32_total, cond32_class_const, nonzero_not_cond32);
    for (auto &kv : wit_hist) printf("%s %ld\n", kv.first.c_str(), kv.second);
    for (auto &kv : share_hist) printf("%s %ld\n", kv.first.c_str(), kv.second);
    for (auto &kv : sizes_hist) printf("%s %ld\n", kv.first.c_str(), kv.second);
    for (auto &kv : contribs_hist) printf("%s %ld\n", kv.first.c_str(), kv.second);
    return 0;
}
