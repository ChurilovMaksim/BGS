// Wave 46, task 7, step 7 (C++): exhaustive (81, 512) joint compatibility.
// Same semantics as wave46_PC_joint81512.py, but fast: a full pair with
// components only at 81 and 512 is a pair of joint sequences with equal
// multiset of the 24 value-pairs. Tests Pi_81 ∩ Pi_512 on every match.
#include <cstdio>
#include <array>
#include <vector>
#include <map>
#include <algorithm>
using Seq = std::array<short, 24>;
using Pairs = std::array<std::pair<short, short>, 24>;

static std::vector<Seq> kernel_small(int q) {
    std::vector<Seq> out;
    for (int y0 = 0; y0 < q; y0++) for (int y1 = 0; y1 < q; y1++) {
        int y[26]; y[0] = y0; y[1] = y1;
        for (int n = 0; n < 24; n++) y[n + 2] = ((6 * y[n + 1] - y[n]) % q + q) % q;
        if (y[24] == y0 && y[25] == y1) {
            Seq s; for (int i = 0; i < 24; i++) s[i] = (short)y[i];
            out.push_back(s);
        }
    }
    return out;
}

// class profile: 4 sorted 6-multisets
using Prof = std::array<std::array<short, 6>, 4>;
static Prof prof(const Seq &y) {
    Prof p;
    for (int r = 0; r < 4; r++) {
        std::array<short, 6> c;
        int k = 0;
        for (int i = r; i < 24; i += 4) c[k++] = y[i];
        std::sort(c.begin(), c.end());
        p[r] = c;
    }
    return p;
}
// D4 class maps as pi[r]
static std::vector<std::array<int, 4>> D4maps() {
    std::vector<std::array<int, 4>> v;
    for (int b = 0; b < 4; b++) {
        std::array<int, 4> s, f;
        for (int r = 0; r < 4; r++) { s[r] = (r + b) % 4; f[r] = ((-r + b) % 4 + 4) % 4; }
        v.push_back(s); v.push_back(f);
    }
    std::sort(v.begin(), v.end());
    v.erase(std::unique(v.begin(), v.end()), v.end());
    return v;
}
static const char *piname(const std::array<int, 4> &pi) {
    static char buf[8];
    bool shift = true;
    for (int r = 0; r < 4; r++) if (pi[r] != (r + pi[0]) % 4) shift = false;
    if (shift) { snprintf(buf, 8, "s%d", pi[0]); return buf; }
    snprintf(buf, 8, "f%d", pi[0] % 4); return buf;
}
static unsigned pi_mask(const Prof &p, const Prof &pp,
                        const std::vector<std::array<int, 4>> &D4) {
    unsigned m = 0;
    for (int k = 0; k < (int)D4.size(); k++) {
        bool ok = true;
        for (int r = 0; r < 4; r++) if (pp[r] != p[D4[k][r]]) ok = false;
        if (ok) m |= (1u << k);
    }
    return m;
}

int main() {
    auto K81 = kernel_small(81);
    auto K512 = kernel_small(512);
    printf("|ker81|=%zu |ker512|=%zu\n", K81.size(), K512.size());
    // fibers: multiset key (sorted seq) -> indices
    std::map<Seq, std::vector<int>> fib81, fib512;
    for (int i = 0; i < (int)K81.size(); i++) {
        Seq s = K81[i]; std::sort(s.begin(), s.end());
        fib81[s].push_back(i);
    }
    for (int i = 0; i < (int)K512.size(); i++) {
        Seq s = K512[i]; std::sort(s.begin(), s.end());
        fib512[s].push_back(i);
    }
    std::map<Seq, std::vector<int>> idx81, idx512;
    for (int i = 0; i < (int)K81.size(); i++) {
        Seq s = K81[i]; std::sort(s.begin(), s.end()); idx81[s].push_back(i);
    }
    for (int i = 0; i < (int)K512.size(); i++) {
        Seq s = K512[i]; std::sort(s.begin(), s.end()); idx512[s].push_back(i);
    }
    // per-vector fiber lists (by index)
    std::vector<std::vector<int>> F81(K81.size()), F512(K512.size());
    for (int i = 0; i < (int)K81.size(); i++) {
        Seq s = K81[i]; std::sort(s.begin(), s.end()); F81[i] = idx81[s];
    }
    for (int i = 0; i < (int)K512.size(); i++) {
        Seq s = K512[i]; std::sort(s.begin(), s.end()); F512[i] = idx512[s];
    }
    std::vector<Prof> P81(K81.size()), P512(K512.size());
    for (int i = 0; i < (int)K81.size(); i++) P81[i] = prof(K81[i]);
    for (int i = 0; i < (int)K512.size(); i++) P512[i] = prof(K512[i]);
    auto D4 = D4maps();
    // dihedral position maps
    std::vector<std::array<int, 24>> D24;
    for (int k = 0; k < 24; k++) {
        std::array<int, 24> s, f;
        for (int i = 0; i < 24; i++) { s[i] = (i + k) % 24; f[i] = ((-i + k) % 24 + 24) % 24; }
        D24.push_back(s); D24.push_back(f);
    }
    long long tot_mates = 0, joint_pairs = 0, dihedral_joint = 0, failures = 0;
    for (int i81 = 0; i81 < (int)K81.size(); i81++) {
        for (int i512 = 0; i512 < (int)K512.size(); i512++) {
            Pairs base;
            for (int i = 0; i < 24; i++) base[i] = {K81[i81][i], K512[i512][i]};
            std::sort(base.begin(), base.end());
            for (int m81 : F81[i81]) for (int m512 : F512[i512]) {
                if (m81 == i81 && m512 == i512) continue;
                tot_mates++;
                Pairs pr;
                for (int i = 0; i < 24; i++) pr[i] = {K81[m81][i], K512[m512][i]};
                std::sort(pr.begin(), pr.end());
                if (pr != base) continue;
                joint_pairs++;
                unsigned a = pi_mask(P81[i81], P81[m81], D4);
                unsigned b = pi_mask(P512[i512], P512[m512], D4);
                if (a & b) {
                    bool dih = false;
                    for (auto &d : D24) {
                        bool ok = true;
                        for (int i = 0; i < 24; i++)
                            if (K81[m81][i] != K81[i81][d[i]] ||
                                K512[m512][i] != K512[i512][d[i]]) ok = false;
                        if (ok) { dih = true; break; }
                    }
                    if (dih) dihedral_joint++;
                } else {
                    failures++;
                    if (failures <= 10) {
                        printf("FAIL base81=(");
                        for (int i = 0; i < 24; i++) printf("%d%s", K81[i81][i], i < 23 ? "," : "");
                        printf(") base512=(");
                        for (int i = 0; i < 24; i++) printf("%d%s", K512[i512][i], i < 23 ? "," : "");
                        printf(") mate81=(");
                        for (int i = 0; i < 24; i++) printf("%d%s", K81[m81][i], i < 23 ? "," : "");
                        printf(") mate512=(");
                        for (int i = 0; i < 24; i++) printf("%d%s", K512[m512][i], i < 23 ? "," : "");
                        printf(") Pi81={");
                        bool first = true;
                        for (int k = 0; k < (int)D4.size(); k++) if (a & (1u << k)) {
                            printf("%s%s", first ? "" : ",", piname(D4[k])); first = false;
                        }
                        printf("} Pi512={");
                        first = true;
                        for (int k = 0; k < (int)D4.size(); k++) if (b & (1u << k)) {
                            printf("%s%s", first ? "" : ",", piname(D4[k])); first = false;
                        }
                        printf("}\n");
                    }
                }
            }
        }
    }
    printf("mate combos checked: %lld\n", tot_mates);
    printf("joint pairs (ordered, excl diagonal): %lld\n", joint_pairs);
    printf("dihedral joint pairs: %lld\n", dihedral_joint);
    printf("FAILURES (Pi81 ∩ Pi512 empty): %lld\n", failures);
    return 0;
}
