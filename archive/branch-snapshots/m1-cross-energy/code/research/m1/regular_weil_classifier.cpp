// Independent C++17 exponent classifier for the M1 regular Weil step.
// It checks only the finite m-th-power obstruction; the external Weil theorem
// and assembled energy estimate are not proved by this program.
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

static int mod(int x, int m) {
    x %= m;
    return x < 0 ? x + m : x;
}

static std::vector<int> residues(int m, int r, int s, int cat) {
    const int nr = mod(-r, m), ns = mod(-s, m);
    if (cat == 0) return {mod(r, m), nr, mod(s, m), ns};
    if (cat == 1) return {mod(r, m), mod(nr + s, m), ns};
    if (cat == 2) return {nr, mod(r + ns, m), mod(s, m)};
    throw std::runtime_error("bad category");
}

static bool classify(int m) {
    if (m <= 1) return false;
    for (int cat = 0; cat < 3; ++cat) {
        for (int r = 0; r < m; ++r) {
            for (int s = 0; s < m; ++s) {
                if (r == 0 && s == 0) continue;
                bool nonzero = false;
                for (int v : residues(m, r, s, cat)) {
                    if (v % m != 0) {
                        nonzero = true;
                        break;
                    }
                }
                if (!nonzero) return false;
            }
        }
    }
    return true;
}

int main(int argc, char** argv) {
    if (argc < 2) {
        std::cerr << "usage: " << argv[0] << " m [m ...]\n";
        return 2;
    }
    std::cout << "{\n  \"all_nontrivial_pairs_not_mth_power\": {\n";
    for (int i = 1; i < argc; ++i) {
        const int m = std::stoi(argv[i]);
        std::cout << "    \"" << m << "\": " << (classify(m) ? "true" : "false");
        if (i + 1 < argc) std::cout << ",";
        std::cout << "\n";
    }
    std::cout << "  }\n}\n";
    return 0;
}
