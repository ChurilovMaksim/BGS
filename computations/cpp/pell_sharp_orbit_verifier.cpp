// Independent exact check: quadratic-ring frequencies, exhaustive orbit window.
// Python uses neighbour descent in the original integral T coordinates.
// Finite certificates do not establish the universal variational theorem.
#include <boost/multiprecision/cpp_int.hpp>
#include <array>
#include <iostream>
#include <map>
#include <stdexcept>
#include <utility>
#include <vector>
using Z = boost::multiprecision::cpp_int;
using V = std::pair<Z,Z>; // x+y sqrt(2), where x=b and y=a
V step(const V& v) { return {3*v.first+4*v.second,2*v.first+3*v.second}; }
V back(const V& v) { return {3*v.first-4*v.second,-2*v.first+3*v.second}; }
V sign(V v) { V neg{-v.first,-v.second}; return neg<v?neg:v; }
Z energy(const V& v) { return v.first*v.first+2*v.second*v.second; }
Z wedge(const V& v,const V& w) { return v.second*w.first-v.first*w.second; }
V canonical(const V& v) {
    if (v.first==0 && v.second==0) throw std::runtime_error("zero vector");
    V w=v;
    for(int j=0;j<12;++j) w=back(w);
    V best=sign(w); Z e=energy(best); int at=-12;
    for(int j=-12;j<=12;++j) {
        V s=sign(w); Z ee=energy(s);
        if(ee<e || (ee==e && s<best)) {best=s;e=ee;at=j;}
        w=step(w);
    }
    if(at==-12 || at==12) throw std::runtime_error("orbit minimizer at window boundary");
    return best;
}
Z gamma(const V& v,const std::array<int,5>& c) {
    std::array<V,6> vv;vv[0]=v;
    for(int j=1;j<6;++j) vv[j]=step(vv[j-1]);
    std::map<V,Z> raw;
    for(int j=0;j<5;++j) for(int k=0;k<5;++k) {
        Z z=c[j]*c[k]*wedge(vv[j],vv[k+1]);
        if(z==0)continue;
        V plus{vv[j].first+vv[k+1].first,vv[j].second+vv[k+1].second};
        V minus{vv[j].first-vv[k+1].first,vv[j].second-vv[k+1].second};
        raw[sign(minus)]+=z;raw[sign(plus)]-=z;
    }
    std::map<V,Z> orbit;
    for(const auto& [w,z]:raw) if(z!=0)orbit[canonical(w)]+=z;
    Z sum=0;
    for(const auto& [w,z]:orbit) {(void)w;sum+=2*z*z;}
    return sum;
}
Z gamma_four(const std::array<int,4>& c) {
    // Original frequencies (0,1), (1,-1), (1,0), (1,1), in x+y sqrt(2).
    const std::array<V,4> vv{{{1,0},{-1,1},{0,1},{1,1}}};
    std::map<V,Z> raw, orbit;
    for(int i=0;i<4;++i) for(int j=0;j<4;++j) {
        V w=step(vv[j]); Z z=c[i]*c[j]*wedge(vv[i],w);
        if(z==0) continue;
        raw[sign(V{vv[i].first-w.first,vv[i].second-w.second})]+=z;
        raw[sign(V{vv[i].first+w.first,vv[i].second+w.second})]-=z;
    }
    for(const auto& [w,z]:raw) if(z!=0) orbit[canonical(w)]+=z;
    Z result=0;
    for(const auto& [w,z]:orbit) { (void)w; result+=2*z*z; }
    return result;
}
Z gamma_radius_three() {
    const std::vector<std::pair<int,int>> xy{{0,1},{0,2},{0,3},{1,-3},
      {1,-2},{1,-1},{1,1},{1,2},{1,3},{2,-2},{2,-1},{2,0},{2,1},{2,2},{3,-1},{3,1}};
    const std::vector<int> c{-5,-7,4,1,5,-10,10,-5,-1,2,2,-6,2,2,1,-1};
    std::map<V,Z> raw, orbit;
    for(std::size_t i=0;i<xy.size();++i) for(std::size_t j=0;j<xy.size();++j) {
        V v{xy[i].second,xy[i].first};
        V w=step(V{xy[j].second,xy[j].first}); Z z=c[i]*c[j]*wedge(v,w);
        if(z==0) continue;
        raw[sign(V{v.first-w.first,v.second-w.second})]+=z;
        raw[sign(V{v.first+w.first,v.second+w.second})]-=z;
    }
    for(const auto& [w,z]:raw) if(z!=0) orbit[canonical(w)]+=z;
    Z result=0;
    for(const auto& [w,z]:orbit) { (void)w; result+=2*z*z; }
    if(result!=1890144) throw std::runtime_error("radius-three witness");
    return result;
}
int main() {
    try {
        int lo=100,hi=-100;
        for(int u:{-1,1})for(int v:{-1,1}) {
            int w=8+2*u+3*v; if(w<lo)lo=w;if(w>hi)hi=w;
        }
        if(lo!=3 || hi!=13 || lo-1!=2)throw std::runtime_error("support separation");
        std::cout<<"{\"scaled_support_range\":["<<lo<<','<<hi<<"],\"rows\":[";
        bool comma=false;
        for(const auto& v:std::array<std::pair<int,int>,3>{{{1,0},{0,1},{1,1}}}) {
            for(int index=0;index<243;++index) {
                int rem=index;std::array<int,5> c;bool nonzero=false;
                for(int j=4;j>=0;--j) {c[j]=rem%3-1;rem/=3;if(c[j])nonzero=true;}
                if(!nonzero)continue;
                Z value=gamma(V{v.second,v.first},c);
                if(comma) std::cout<<',';
                comma=true;
                std::cout<<'['<<v.first<<','<<v.second;
                for(int x:c)std::cout<<','<<x;
                std::cout<<','<<value<<']';
            }
        }
        std::cout<<"],\"four_mode_rows\":[";
        bool second_comma=false;
        for(int index=0;index<81;++index) {
            int rem=index;std::array<int,4> c;bool nonzero=false;
            for(int j=3;j>=0;--j) {c[j]=rem%3-1;rem/=3;if(c[j])nonzero=true;}
            if(!nonzero) continue;
            if(second_comma) std::cout<<',';
            second_comma=true;
            std::cout<<'['<<c[0]<<','<<c[1]<<','<<c[2]<<','<<c[3]<<','<<gamma_four(c)<<']';
        }
        std::cout<<"],\"radius_three_Gamma_over_pi_squared\":"<<gamma_radius_three()<<"}\n";
        return 0;
    }catch(const std::exception& e){std::cerr<<e.what()<<'\n';return 1;}
}
