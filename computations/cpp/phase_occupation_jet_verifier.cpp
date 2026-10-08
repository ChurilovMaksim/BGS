// Exact finite occupation multiplicities for the symmetric Fourier witness.
// No floating-point arithmetic; these checks are not an asymptotic theorem.
// Build: c++ -std=c++20 -O2 -Wall -Wextra -Werror this_file.cpp -o verifier
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <stdexcept>

int main() {
    std::uint64_t words = 0, cases = 0;
    for (std::uint64_t m = 3; m <= 40; ++m) {
        std::map<std::array<std::uint64_t, 2>, std::uint64_t> pairs;
        std::map<std::array<std::uint64_t, 3>, std::uint64_t> triples;
        for (std::uint64_t i = 0; i < m; ++i)
            for (std::uint64_t j = 0; j < m; ++j) {
                std::array<std::uint64_t, 2> pair{i, j};
                std::sort(pair.begin(), pair.end());
                ++pairs[pair];
                ++words;
                for (std::uint64_t k = 0; k < m; ++k) {
                    std::array<std::uint64_t, 3> triple{i, j, k};
                    std::sort(triple.begin(), triple.end());
                    ++triples[triple];
                    ++words;
                }
            }
        std::uint64_t n2 = 0, n3 = 0;
        for (const auto& [key, count] : pairs) { (void)key; n2 += count * count; }
        for (const auto& [key, count] : triples) { (void)key; n3 += count * count; }
        if (n2 != 2 * m * m - m || n3 != 6 * m * m * m - 9 * m * m + 4 * m)
            throw std::runtime_error("exact occupation count failed");
        cases += 2;
    }
    std::cout << "{\"status\":\"PASS\",\"dimensions\":[3,40],\"orders\":[2,3],"
              << "\"cases\":" << cases << ",\"enumerated_words\":" << words
              << ",\"arithmetic\":\"uint64; maximum sums below 384000\"}\n";
}
