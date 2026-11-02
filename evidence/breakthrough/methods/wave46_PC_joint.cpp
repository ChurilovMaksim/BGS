// Wave 46, task 7, step 12: generic exhaustive (q1, q2) joint compatibility.
// Usage: ./wave46_PC_joint q1 q2
// A pair with components only at q1, q2 is a pair of joint sequences
// with equal multiset of the 24 value-pairs (common-sigma condition).
// Tests Pi_q1 ∩ Pi_q2 on every match. Exact, no sampling.
#include <cstdio>
#include <cstdlib>
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
        for (int n = 0; n < 24; n++)
            y[n + 2] = ((6 * y[n + 1] - y[n]) % q + q) % q;
        if (y[24] == y0 && y[25] == y1) {
            Seq s; for (int i = 0; i < 24; i++) s[i] = (short)y[i];
            out.push_back(s);
        }
    }
    return out;
}

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
static std::vector<std::array<int, 4>> D4maps() {
    std::vector<std::array<int, 4>> v;
    for (int b = 0; b < 4; b++) {
        std::array<int, 4> s, f;
        for (int r = 0; r < 4; r++) {
            s[r] = (r + b) % 4;
            f[r] = ((-r + b) % 4 + 4) % 4;
        }
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

int main(int argc, char **argv) {
    int q1 = atoi(argv[1]), q2 = atoi(argv[2]);
    auto K1 = kernel_small(q1);
    auto K2 = kernel_small(q2);
    printf("q1=%d |ker|=%zu  q2=%d |ker|=%zu\n", q1, K1.size(), q2, K2.size());
    std::map<Seq, std::vector<int>> idx1, idx2;
    for (int i = 0; i < (int)K1.size(); i++) {
        Seq s = K1[i]; std::sort(s.begin(), s.end()); idx1[s].push_back(i);
    }
    for (int i = 0; i < (int)K2.size(); i++) {
        Seq s = K2[i]; std::sort(s.begin(), s.end()); idx2[s].push_back(i);
    }
    std::vector<std::vector<int>> F1(K1.size()), F2(K2.size());
    for (int i = 0; i < (int)K1.size(); i++) {
        Seq s = K1[i]; std::sort(s.begin(), s.end()); F1[i] = idx1[s];
    }
    for (int i = 0; i < (int)K2.size(); i++) {
        Seq s = K2[i]; std::sort(s.begin(), s.end()); F2[i] = idx2[s];
    }
    std::vector<Prof> P1(K1.size()), P2(K2.size());
    for (int i = 0; i < (int)K1.size(); i++) P1[i] = prof(K1[i]);
    for (int i = 0; i < (int)K2.size(); i++) P2[i] = prof(K2[i]);
    auto D4 = D4maps();
    std::vector<std::array<int, 24>> D24;
    for (int k = 0; k < 24; k++) {
        std::array<int, 24> s, f;
        for (int i = 0; i < 24; i++) {
            s[i] = (i + k) % 24;
            f[i] = ((-i + k) % 24 + 24) % 24;
        }
        D24.push_back(s); D24.push_back(f);
    }
    long long tot_mates = 0, joint_pairs = 0, dihedral_joint = 0, failures = 0;
    for (int i1 = 0; i1 < (int)K1.size(); i1++) {
        for (int i2 = 0; i2 < (int)K2.size(); i2++) {
            Pairs base;
            for (int i = 0; i < 24; i++) base[i] = {K1[i1][i], K2[i2][i]};
            std::sort(base.begin(), base.end());
            for (int m1 : F1[i1]) for (int m2 : F2[i2]) {
                if (m1 == i1 && m2 == i2) continue;
                tot_mates++;
                Pairs pr;
                for (int i = 0; i < 24; i++) pr[i] = {K1[m1][i], K2[m2][i]};
                std::sort(pr.begin(), pr.end());
                if (pr != base) continue;
                joint_pairs++;
                unsigned a = pi_mask(P1[i1], P1[m1], D4);
                unsigned b = pi_mask(P2[i2], P2[m2], D4);
                if (a & b) {
                    bool dih = false;
                    for (auto &d : D24) {
                        bool ok = true;
                        for (int i = 0; i < 24; i++)
                            if (K1[m1][i] != K1[i1][d[i]] ||
                                K2[m2][i] != K2[i2][d[i]]) ok = false;
                        if (ok) { dih = true; break; }
                    }
                    if (dih) dihedral_joint++;
                } else {
                    failures++;
                    if (failures <= 3) {
                        printf("FAIL base1=(");
                        for (int i = 0; i < 24; i++) printf("%d%s", K1[i1][i], i < 23 ? "," : "");
                        printf(") base2=(");
                        for (int i = 0; i < 24; i++) printf("%d%s", K2[i2][i], i < 23 ? "," : "");
                        printf(") mate1=(");
                        for (int i = 0; i < 24; i++) printf("%d%s", K1[m1][i], i < 23 ? "," : "");
                        printf(") mate2=(");
                        for (int i = 0; i < 24; i++) printf("%d%s", K2[m2][i], i < 23 ? "," : "");
                        printf(") Pi1={");
                        bool first = true;
                        for (int k = 0; k < (int)D4.size(); k++) if (a & (1u << k)) {
                            printf("%s%s", first ? "" : ",", piname(D4[k])); first = false;
                        }
                        printf("} Pi2={");
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
    printf("mate combos: %lld  joint pairs: %lld  dihedral: %lld  FAILURES: %lld\n",
           tot_mates, joint_pairs, dihedral_joint, failures);
    return 0;
}
