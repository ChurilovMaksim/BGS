// Independent exact finite checks for fixed_strength_locality.md.
// No floating-point matrix calculation or Python implementation is reused.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <random>
#include <stdexcept>
#include <utility>
#include <vector>

using I = std::int64_t;
using Vec = std::pair<I,I>;
void require(bool condition, const char* text) {
    if (!condition) throw std::runtime_error(text);
}
I wedge(Vec a, Vec b) { return a.first*b.second-a.second*b.first; }
Vec add(Vec a, Vec b) { return {a.first+b.first,a.second+b.second}; }
I positive_mod(I a, I n) { a%=n; return a<0?a+n:a; }

std::map<Vec,I> coefficient(int degree) {
    // b=a^2 is assembled as a triple sum over the original four atoms.
    const std::array<Vec,4> atoms{{{1,0},{-1,0},{0,1},{0,-1}}};
    std::map<Vec,I> out;
    for (Vec v:atoms) for (Vec w:atoms) for (Vec z:atoms) {
        const Vec wz=add(w,z);
        I omega=wedge(v,wz), power=1;
        for (int j=0;j<degree;++j) power*=omega;
        out[add(v,wz)]+=power;
    }
    for (auto it=out.begin();it!=out.end();) {
        if (it->second==0) it=out.erase(it); else ++it;
    }
    return out;
}

I support_checks() {
    I count=0;
    for (I scale: {1,2,7,16,31,64}) {
        // Extremal support corners are independent of the Python grid scan.
        for (I u: {-scale,scale}) for (I v: {-scale,scale}) {
            const I image=8*scale+2*u+3*v;
            require(3*scale<=image && image<=13*scale,"support image bound");
            require(image>scale && image<15*scale,"disjoint support failed");
            ++count;
        }
    }
    require(3*3008>6561,"Cauchy bound");
    return count;
}

struct ClusterStats { I cases=0; I gaps=0; I ordered_pairs=0; };
ClusterStats clusters() {
    std::mt19937 generator(20260905u);
    ClusterStats stats;
    for (I k:{3,5,7,11,17}) for (I n:{1,2,3,7,19}) for (I trial=0;trial<8;++trial) {
        const I period=1000000, circle=k*period, width=3, dimension=k*n;
        std::vector<I> points;
        for (I j=0;j<k;++j) for (I l=0;l<n;++l) {
            const I offset=static_cast<I>(generator()%7)-width;
            points.push_back(positive_mod(j*period+offset,circle));
        }
        std::sort(points.begin(),points.end());
        I small=0,large=0,pairs=0,total_gaps=0;
        for (I j=0;j<dimension;++j) {
            const I gap=(j+1==dimension?points[0]+circle:points[j+1])-points[j];
            total_gaps+=gap;
            if (gap<=2*width) ++small;
            else {
                require(period-2*width<=gap && gap<=period+2*width,"large gap band");
                ++large;
            }
            for (I l=0;l<dimension;++l) if (j!=l) {
                I delta=std::abs(points[j]-points[l]);
                delta=std::min(delta,circle-delta);
                if (3*dimension*delta<=circle) ++pairs; // x=1/3: also separated when n=1
            }
        }
        require(small==dimension-k && large==k,"gap multiplicities");
        require(total_gaps==circle,"mean spacing conservation");
        require(pairs==dimension*(n-1),"exact ordered pair count");
        // Exact union measure for origins whose unit-mean window hits a level.
        // Scale every circle coordinate by dimension to keep all endpoints integral.
        const I total=circle*dimension;
        std::vector<std::pair<I,I>> arcs;
        for (I point:points) {
            I right=point*dimension;
            I left=right-circle;
            if (left<0) { arcs.emplace_back(0,right); arcs.emplace_back(left+total,total); }
            else arcs.emplace_back(left,right);
        }
        std::sort(arcs.begin(),arcs.end());
        I covered=0,left=-1,right=-1;
        for (const auto& arc:arcs) {
            if (left<0) { left=arc.first; right=arc.second; }
            else if (arc.first<=right) right=std::max(right,arc.second);
            else { covered+=right-left; left=arc.first; right=arc.second; }
        }
        if (left>=0) covered+=right-left;
        require(0<=covered && covered<=total,"circle union measure");
        require(covered<=k*(circle+2*width*dimension),"random-origin occupancy bound");
        ++stats.cases; stats.gaps+=dimension; stats.ordered_pairs+=pairs;
    }
    return stats;
}

int main() {
    try {
        const auto first=coefficient(1),third=coefficient(3);
        require(first.empty(),"Poisson coefficient should vanish");
        const std::map<Vec,I> expected{{{-2,-1},-6},{{-2,1},6},{{-1,-2},6},
          {{-1,2},-6},{{1,-2},-6},{{1,2},6},{{2,-1},6},{{2,1},-6}};
        require(third==expected,"cubic Weyl coefficient mismatch");
        const I corners=support_checks();
        const auto stats=clusters();
        std::cout << "{\"producer\":\"computations/cpp/fixed_strength_locality_exact.cpp\",\"status\":\"PASS\",\"scope\":\"Exact finite algebra and cluster controls; not an asymptotic proof\","
                  << "\"support_corners\":" << corners << ",\"seed\":20260905,"
                  << "\"cluster_cases\":" << stats.cases << ",\"gaps_checked\":" << stats.gaps
                  << ",\"origin_coverage_checks\":" << stats.cases
                  << ",\"ordered_close_pairs\":" << stats.ordered_pairs
                  << ",\"first_moyal_coefficient_zero\":true,\"third_moyal_coefficient\":[";
        bool comma=false;
        for (const auto& [v,a]:third) {
            if (comma) std::cout << ',';
            comma=true;
            std::cout << '[' << v.first << ',' << v.second << ',' << a << ']';
        }
        std::cout << "]}\n";
        return 0;
    } catch(const std::exception& error) {
        std::cerr << error.what() << '\n'; return 1;
    }
}
