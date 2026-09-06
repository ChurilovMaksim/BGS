// Independent original-coordinate finite checks of Pell orbit pair supports.
#include <iostream>
#include <set>
#include <stdexcept>
#include <utility>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
using boost::multiprecision::cpp_int;
using Vec=std::pair<cpp_int,cpp_int>;
cpp_int mod(cpp_int x,const cpp_int& n) { x%=n; if(x<0) x+=n; return x; }
int main() {
    try {
        bool first=true;
        std::cout << "{\"passed\":true,\"representation\":\"original integral T coordinates\",\"cases\":[";
        for(int k : {11,13,17,19,23,31,47,101}) {
            cpp_int n=1,f=0;
            for(int j=0;j<k;++j) { cpp_int nn=n+2*f; f=n+f; n=nn; }
            if(n*n-2*f*f!=-1) throw std::runtime_error("Pell identity failed");
            Vec v{1,0};
            std::vector<Vec> orbit;
            for(int j=0;j<k;++j) {
                orbit.push_back(v);
                v={mod(3*v.first+2*v.second,n),mod(4*v.first+3*v.second,n)};
            }
            if(v!=Vec{1,0}) throw std::runtime_error("original map period failed");
            std::set<Vec> signed_orbit;
            for(const auto& p:orbit) for(int s : {-1,1})
                signed_orbit.emplace(mod(s*p.first,n),mod(s*p.second,n));
            if(signed_orbit.size()!=static_cast<std::size_t>(2*k))
                throw std::runtime_error("signed orbit multiplicity failed");
            std::set<Vec> sums;
            for(int i=0;i<k;++i) for(int j=i+1;j<k;++j)
                for(int s : {-1,1}) for(int t : {-1,1})
                    sums.emplace(mod(s*orbit[i].first+t*orbit[j].first,n),
                                 mod(s*orbit[i].second+t*orbit[j].second,n));
            if(sums.count(Vec{0,0}) || sums.size()!=static_cast<std::size_t>(2*k*(k-1)))
                throw std::runtime_error("signed pair support collision");
            if(!first) std::cout << ',';
            first=false;
            std::cout << "{\"K\":" << k << ",\"N\":\"" << n
                      << "\",\"signed_pair_count\":" << sums.size() << '}';
        }
        std::cout << "]}\n";
        return 0;
    } catch(const std::exception& e) { std::cerr << e.what() << '\n'; return 1; }
}
