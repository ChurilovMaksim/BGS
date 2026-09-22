// Exact finite controls for pell_polynomial_edgeworth.md.
//
// Standalone build (not claimed executed by the existence of this source):
// c++ -std=c++20 -O2 -Wall -Wextra -Wpedantic computations/cpp/pell_minimal_relation_verifier.cpp -o pell_minimal_relation_verifier
//
// These checks concern finite arithmetic and combinatorics. They do not
// prove the general Gaussian limit or microscopic BGS.
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <stdexcept>
#include <utility>
#include <vector>

namespace {
void require(bool condition, const char* message) {
    if (!condition) throw std::runtime_error(message);
}

struct Vec { long long x, y; };
long long wedge(Vec a, Vec b) { return a.x*b.y-a.y*b.x; }

std::map<long long, std::uint64_t> phase_histogram() {
    std::map<long long, std::uint64_t> histogram;
    for (int a=0; a<8; ++a) {
        for (int b=0; b<8; ++b) {
            if (a==b) continue;
            std::array<Vec,8> word;
            word.fill(Vec{-1,0});
            word[a]=Vec{3,-4};
            word[b]=Vec{3,4};
            Vec sum{0,0};
            long long symplectic_sum=0;
            for (int i=0; i<8; ++i) {
                sum.x+=word[i].x;
                sum.y+=word[i].y;
                for (int j=i+1; j<8; ++j)
                    symplectic_sum+=wedge(word[i],word[j]);
            }
            require(sum.x==0 && sum.y==0,"word is not closed");
            require(symplectic_sum%2==0,"nonintegral half phase");
            const long long phase=symplectic_sum/2;
            const long long endpoint_formula=4*(a-b)+16*(b>a?1:-1);
            require(phase==endpoint_formula,"endpoint phase formula mismatch");
            ++histogram[phase];
        }
    }
    require(histogram.size()==7,"unexpected phase support size");
    for (long long phase=-12; phase<=12; phase+=4)
        require(histogram.at(phase)==8,"wrong phase multiplicity");
    return histogram;
}

struct MatchingStats {
    std::uint64_t count=0;
    std::uint64_t crossings=0;
};

void enumerate_matchings(const std::vector<int>& remaining,
                        std::vector<std::pair<int,int>>& pairs,
                        MatchingStats& result) {
    if (remaining.empty()) {
        ++result.count;
        for (std::size_t i=0; i<pairs.size(); ++i) {
            const auto [a,b]=pairs[i];
            for (std::size_t j=i+1; j<pairs.size(); ++j) {
                const auto [c,d]=pairs[j];
                if ((a<c && c<b && b<d) || (c<a && a<d && d<b))
                    ++result.crossings;
            }
        }
        return;
    }
    const int first=remaining.front();
    for (std::size_t partner=1; partner<remaining.size(); ++partner) {
        std::vector<int> next;
        for (std::size_t j=1; j<remaining.size(); ++j)
            if (j!=partner) next.push_back(remaining[j]);
        pairs.emplace_back(first,remaining[partner]);
        enumerate_matchings(next,pairs,result);
        pairs.pop_back();
    }
}

std::uint64_t pairing_count(int r) {
    std::uint64_t result=1;
    for (int j=1; j<=r; ++j) result*=static_cast<std::uint64_t>(2*j-1);
    return result;
}

std::pair<int,int> small_polynomial_controls() {
    int checked=0, equality_cases=0;
    // Mechanically form (z^2-6z+1)Q rather than assuming a leading-term
    // argument. This is a bounded regression, not a universal classification.
    for (int a=-2; a<=2; ++a)
    for (int b=-2; b<=2; ++b)
    for (int c=-2; c<=2; ++c)
    for (int d=-2; d<=2; ++d) {
        const std::array<int,4> q{a,b,c,d};
        if (a==0 && b==0 && c==0 && d==0) continue;
        std::array<int,6> p{};
        for (std::size_t j=0; j<q.size(); ++j) {
            p[j]+=q[j]; p[j+1]-=6*q[j]; p[j+2]+=q[j];
        }
        int norm=0;
        for (int coefficient:p) norm+=std::abs(coefficient);
        require(norm>=8,"weight below eight found");
        ++checked;
        if (norm==8) {
            int nonzero=0;
            for (int coefficient:q) {
                if (coefficient!=0) {
                    ++nonzero;
                    require(std::abs(coefficient)==1,"nonunit equality coefficient");
                }
            }
            require(nonzero==1,"equality was not a shifted minimal polynomial");
            ++equality_cases;
        }
    }
    require(checked==624 && equality_cases==8,"polynomial-control count mismatch");
    return {checked,equality_cases};
}
} // namespace

int main() {
    try {
        const auto histogram=phase_histogram();
        const auto [polynomial_checks,equalities]=small_polynomial_controls();
        std::uint64_t power5=1;
        for (int j=0; j<21; ++j) power5*=5;
        require(power5>(std::uint64_t{1}<<48),"K=29 integer cutoff failed");
        require(320*81>256*100,"K=29 rational cutoff failed");

        std::cout << "{\n  \"status\": \"passed\",\n"
                  << "  \"scope\": \"Exact finite combinatorial controls only; not a BGS or Gaussian-limit proof.\",\n"
                  << "  \"polynomial_controls\": " << polynomial_checks << ",\n"
                  << "  \"minimal_polynomial_equalities\": " << equalities << ",\n"
                  << "  \"eight_word_phase_histogram\": {";
        bool first=true;
        for (const auto& [phase,count]:histogram) {
            if (!first) std::cout << ',';
            first=false;
            std::cout << '\"' << phase << "\":" << count;
        }
        std::cout << "},\n  \"matching_controls\": [\n";
        for (int r=1; r<=6; ++r) {
            std::vector<int> remaining;
            for (int j=0; j<2*r; ++j) remaining.push_back(j);
            std::vector<std::pair<int,int>> pairs;
            MatchingStats result;
            enumerate_matchings(remaining,pairs,result);
            const auto expected=pairing_count(r);
            require(result.count==expected,"perfect-matching count mismatch");
            const auto numerator=expected*static_cast<std::uint64_t>(r*(r-1));
            require(numerator%6==0,"crossing count is not integral");
            require(result.crossings==numerator/6,"total crossing identity failed");
            if (r>1) std::cout << ",\n";
            std::cout << "    {\"r\":" << r << ",\"pairings\":" << result.count
                      << ",\"crossings\":" << result.crossings << '}';
        }
        std::cout << "\n  ]\n}\n";
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "verification failed: " << error.what() << '\n';
        return 1;
    }
}
