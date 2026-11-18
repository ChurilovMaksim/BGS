// Orthogonality on the six-phase torus with its angle sum held fixed.
// The seventh letter has phase 1. Count ordered word pairs exactly.
#include <array>
#include <cstdint>
#include <iostream>
#include <map>

using Counts = std::array<int, 7>;
using Weight = std::int64_t;
using Histogram = std::map<Counts, Weight>;

int main() {
    constexpr std::array<Weight, 6> diagonal = {7, 91, 1645, 36715, 948157, 27210169};
    Histogram words{{Counts{}, 1}};
    for (int length = 1; length <= 6; ++length) {
        Histogram next;
        for (const auto& [counts, weight] : words) {
            for (int letter = 0; letter < 7; ++letter) {
                Counts added = counts;
                ++added[letter];
                next[added] += weight;
            }
        }
        words.swap(next);
        std::map<int, Weight> harmonics;
        for (const auto& [left, left_weight] : words) {
            for (const auto& [right, right_weight] : words) {
                int excess = left[1] - right[1];
                bool survives = true;
                for (int j = 2; j <= 6; ++j)
                    survives = survives && (left[j] - right[j] == excess);
                if (survives)
                    harmonics[excess] += left_weight * right_weight;
            }
        }
        std::map<int, Weight> expected{{0, diagonal[length-1]}};
        if (length == 6) {
            expected[-1] = 720;
            expected[1] = 720;
        }
        if (harmonics != expected) {
            std::cerr << "Character mismatch at length " << length << '\n';
            return 1;
        }
        std::cout << length;
        for (const auto& [frequency, weight] : harmonics)
            std::cout << "  harmonic " << frequency << " = " << weight;
        std::cout << '\n';
    }
}
