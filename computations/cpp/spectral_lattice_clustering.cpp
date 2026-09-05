// Exact finite regression for the spectral lattice concentration lemma.
// No floating-point arithmetic or Gaussian/RMT assumptions are used.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <random>
#include <stdexcept>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::cpp_int;
using I = std::int64_t;

void check(std::vector<I> points, I L, I K, I W, I a, I b) {
    // Coordinates have denominator L; width=W/L and spacing threshold=a/b.
    if (points.empty() || K < 1 || L % K || W <= 0 || 2*K*W >= L || a <= 0 || b <= 0)
        throw std::invalid_argument("invalid concentration instance");
    for (I& t : points) t = (t % L + L) % L;
    std::sort(points.begin(), points.end());
    const I d = static_cast<I>(points.size());
    const I step = L/K;
    I squared_distance_sum = 0, long_gaps = 0, close_pairs = 0;
    for (I i=0; i<d; ++i) {
        const I r=points[static_cast<std::size_t>(i)] % step;
        const I distance=std::min(r,step-r);
        squared_distance_sum += distance*distance;
        const I next = i+1 == d ? points[0]+L : points[static_cast<std::size_t>(i+1)];
        const I gap = next-points[static_cast<std::size_t>(i)];
        if (d*gap*b > L*a) ++long_gaps;
        for (I j=0; j<d; ++j) if (i!=j) {
            const I delta=std::abs(points[static_cast<std::size_t>(i)]-points[static_cast<std::size_t>(j)]);
            if (d*std::min(delta,L-delta)*b <= L*a) ++close_pairs;
        }
    }
    const cpp_int w2=cpp_int(W)*W;
    const cpp_int spacing_left=cpp_int(long_gaps)*w2*L*a;
    const cpp_int spacing_right=cpp_int(2)*squared_distance_sum*L*a
        +cpp_int(K)*w2*L*a+cpp_int(2)*d*K*w2*W*b;
    if (spacing_left > spacing_right)
        throw std::runtime_error("cleared spacing inequality failed");
    const I good_numerator=std::max<I>(0,d*W*W-squared_distance_sum);
    const cpp_int pair_left=cpp_int(close_pairs+d)*K*(L*a+2*d*W*b)*w2*w2;
    const cpp_int pair_right=cpp_int(L)*a*good_numerator*good_numerator;
    if (pair_left < pair_right)
        throw std::runtime_error("cleared pair-count inequality failed");
}

int main() {
    try {
        std::mt19937 generator(20260905u);
        const I L=420;
        I cases=0;
        for (const I K : {1,2,3,4,5,6,7,10,12,14,15,20,21}) {
            const I step=L/K;
            for (I trial=0; trial<300; ++trial) {
                const I d=1+generator()%40;
                const I W=1+generator()%static_cast<unsigned>((step-1)/2);
                const I a=1+generator()%5, b=1+generator()%4;
                std::vector<I> points;
                for (I j=0; j<d; ++j) {
                    I t=generator()%static_cast<unsigned>(L);
                    if (trial%3==0) t=(generator()%static_cast<unsigned>(K))*step;
                    if (trial%3==1) t=(generator()%static_cast<unsigned>(K))*step
                        +static_cast<I>(generator()%static_cast<unsigned>(2*W+1))-W;
                    points.push_back(t);
                }
                check(points,L,K,W,a,b);
                ++cases;
            }
        }
        std::cout << "{\"passed\":true,\"integer_instances\":" << cases
                  << ",\"inequalities_per_instance\":2,\"coordinate_denominator\":420,"
                  << "\"seed\":20260905,\"scope\":\"finite exact integer regression, not a formal proof\"}\n";
        return 0;
    } catch (const std::exception& error) {
        std::cerr << error.what() << '\n';
        return 1;
    }
}
