// Independent exact pair-key check in the ORIGINAL fixed-map coordinates.
// This finite verifier is not a proof of an asymptotic spectral law.
#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>
#include <set>
#include <stdexcept>
#include <utility>
#include <vector>
using Z = boost::multiprecision::cpp_int;
using V = std::pair<Z,Z>;
Z mod(Z a, const Z& n) { a %= n; if (a < 0) a += n; return a; }
V map_step(const V& v, const Z& n) {
    return {mod(3*v.first+2*v.second,n), mod(4*v.first+3*v.second,n)};
}
void require(bool x, const char* message) { if (!x) throw std::runtime_error(message); }
int main() {
 try {
    const std::vector<int> periods{3,5,7,11,13,17,23,31,47,101};
    std::cout << "{\"checks\":[";
    bool first = true;
    for (int k : periods) {
        Z n=1, f=0;
        for (int j=0;j<k;++j) { Z nn=n+2*f, ff=n+f; n=nn; f=ff; }
        require(n*n-2*f*f == -1,"Pell identity failed");
        std::vector<V> v;
        V x{1,0};
        for (int j=0;j<k;++j) { v.push_back(x); x=map_step(x,n); }
        require(x == V{1,0},"fixed map period failed");
        std::set<V> keys;
        for (int t=0;t<k;++t) for (int s=t+1;s<k;++s)
            for (int e : {-1,1}) for (int d : {-1,1}) {
                V key{mod(e*v[t].first+d*v[s].first,n),
                      mod(e*v[t].second+d*v[s].second,n)};
                require(key != V{0,0},"nontrivial zero pair");
                require(keys.insert(key).second,"pair-key collision");
            }
        require(keys.size() == static_cast<std::size_t>(2*k*(k-1)),"wrong key count");
        int total=0;
        for (int j=0;j<k;++j) {
            int b=k-1-2*j;
            int prev=k-1-2*((j+k-1)%k);
            require(b-prev == (j==0 ? 2*(k-1) : -2),"cohomology failed");
            total+=b;
        }
        require(total==0,"centering failed");
        if (!first) std::cout << ',';
        first=false;
        std::cout << "{\"K\":" << k << ",\"N\":\"" << n
                  << "\",\"signed_pair_keys\":" << keys.size() << '}';
    }
    std::cout << "],\"status\":\"PASS\"}\n";
    return 0;
 } catch (const std::exception& e) {
    std::cerr << e.what() << '\n'; return 1;
 }
}
