// Independent finite Gelfand--Tsetlin enumeration, exact checked integers.
// This checks stated finite weights, not arbitrary rank or all representations.
#include <algorithm>
#include <cstdint>
#include <functional>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <stdexcept>
#include <vector>
using Row=std::vector<int>;
using Key=std::pair<Row,Row>;
using Wide=__int128_t;
static std::map<Key,std::int64_t> memo;

static std::int64_t narrow(Wide value) {
    if (value<0 || value>std::numeric_limits<std::int64_t>::max())
        throw std::overflow_error("int64 conversion overflow");
    return static_cast<std::int64_t>(value);
}
static Wide multiply(Wide a,Wide b) {
    Wide out;
    if (__builtin_mul_overflow(a,b,&out)) throw std::overflow_error("int128 multiplication overflow");
    return out;
}
static std::int64_t multiplicity(const Row& top,const Row& weights) {
    Key key{top,weights};
    if (auto it=memo.find(key);it!=memo.end()) return it->second;
    if (top.size()!=weights.size()) return 0;
    if (std::accumulate(top.begin(),top.end(),0)!=std::accumulate(weights.begin(),weights.end(),0)) return 0;
    if (top.size()==1) return top[0]==weights[0];
    Row lower(top.size()-1), rest(weights.begin(),weights.end()-1);
    int target=std::accumulate(rest.begin(),rest.end(),0);
    Wide total=0;
    std::function<void(std::size_t,int)> visit=[&](std::size_t i,int sum) {
        if (i==lower.size()) {
            if (sum==target) {
                Wide next;
                if (__builtin_add_overflow(total,static_cast<Wide>(multiplicity(lower,rest)),&next))
                    throw std::overflow_error("int128 addition overflow");
                total=next;
            }
            return;
        }
        for (int v=top[i+1];v<=top[i];++v) {lower[i]=v;visit(i+1,sum+v);}
    };
    visit(0,0);
    return memo.emplace(std::move(key),narrow(total)).first->second;
}
static std::int64_t dimension(const Row& lam) {
    Wide numerator=1,denominator=1;
    for (std::size_t i=0;i<lam.size();++i) for(std::size_t j=i+1;j<lam.size();++j) {
        numerator=multiply(numerator,lam[i]-lam[j]+static_cast<int>(j-i));
        denominator=multiply(denominator,static_cast<int>(j-i));
    }
    if (numerator%denominator!=0) throw std::logic_error("noninteger Weyl dimension");
    return narrow(numerator/denominator);
}
struct Result {Row lam;std::int64_t dim,zero,root;};
static std::map<Row,Result> results;
static void check(const Row& lam) {
    if (results.count(lam)) return;
    const int n=static_cast<int>(lam.size()), k=-lam.back();
    Row top=lam,zero(n,k),root=zero;
    for (int& v:top) v+=k;
    ++root[n-2];--root[n-1];
    auto m0=multiplicity(top,zero), mr=multiplicity(top,root), dim=dimension(lam);
    if (static_cast<Wide>(m0)>multiply(n-1,mr) ||
        static_cast<Wide>(dim)<static_cast<Wide>(m0)+multiply(n*(n-1),mr) ||
        static_cast<Wide>(dim)<multiply(n+1,m0))
        throw std::logic_error("dimension/injection inequality failed");
    results.emplace(lam,Result{lam,dim,m0,mr});
}
static void enumerate(int n,int bound) {
    Row row(n);
    std::function<void(int,int,int)> visit=[&](int i,int upper,int sum) {
        if(i==n) {
            if(sum==0 && std::any_of(row.begin(),row.end(),[](int v){return v!=0;})) check(row);
            return;
        }
        for(int v=-bound;v<=upper;++v) {
            int partial=sum+v, remaining=n-i-1;
            if(partial-remaining*bound>0 || partial+remaining*v<0) continue;
            row[i]=v;visit(i+1,v,partial);
        }
    };
    visit(0,bound,0);
}
int main() {
    for(int n=2;n<=7;++n) enumerate(n,2);
    for(int n=2;n<=5;++n) enumerate(n,4);
    std::cout<<"{\"all_passed\":true,\"exact_cases\":"<<results.size()<<",\"cases\":[";
    bool comma=false;
    std::vector<Result> sorted;
    for(const auto& [key,value]:results) sorted.push_back(value);
    std::sort(sorted.begin(),sorted.end(),[](const Result& a,const Result& b){
        if(a.lam.size()!=b.lam.size()) return a.lam.size()<b.lam.size();
        return a.lam<b.lam;
    });
    for(const auto& r:sorted) {
        if(comma) std::cout<<',';
        comma=true;
        std::cout<<"{\"N\":"<<r.lam.size()<<",\"lambda\":[";
        for(std::size_t j=0;j<r.lam.size();++j) {if(j)std::cout<<',';std::cout<<r.lam[j];}
        std::cout<<"],\"dimension\":"<<r.dim<<",\"m_zero\":"<<r.zero<<",\"m_root\":"<<r.root<<'}';
    }
    std::cout<<"],\"arithmetic\":\"checked int128 products and int64 results\"}\n";
}
