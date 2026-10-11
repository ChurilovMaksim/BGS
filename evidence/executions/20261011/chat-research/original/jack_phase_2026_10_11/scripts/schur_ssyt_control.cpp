// Independent control at alpha=1: count semistandard Young tableaux.
// No Jack differential operator or coefficient recurrence is used here.
#include <algorithm>
#include <cstdint>
#include <functional>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <vector>

struct Counts { std::int64_t all=0, balanced=0; };
Counts tableaux(const std::vector<int>& lambda) {
    const int n=static_cast<int>(lambda.size()), shift=-lambda.back();
    std::vector<int> shape(n);
    for(int i=0;i<n;++i) shape[i]=lambda[i]+shift;
    std::vector<std::pair<int,int>> cells;
    for(int i=0;i<n;++i)
        for(int j=0;j<shape[i];++j) cells.emplace_back(i,j);
    std::vector<std::vector<int>> table(n);
    for(int i=0;i<n;++i) table[i].assign(shape[i],0);
    std::vector<int> content(n,0);
    Counts count;
    std::function<void(std::size_t)> visit = [&](std::size_t pos) {
        if(pos==cells.size()) {
            ++count.all;
            if(std::all_of(content.begin(),content.end(),
                           [&](int x){return x==shift;})) ++count.balanced;
            return;
        }
        auto [i,j]=cells[pos];
        int lo=1;
        if(j>0) lo=std::max(lo,table[i][j-1]);
        if(i>0 && j<shape[i-1]) lo=std::max(lo,table[i-1][j]+1);
        for(int x=lo;x<=n;++x) {
            table[i][j]=x; ++content[x-1];
            visit(pos+1);
            --content[x-1]; table[i][j]=0;
        }
    };
    visit(0);
    return count;
}
std::int64_t weyl_dimension(const std::vector<int>& lambda) {
    std::int64_t a=1,b=1;
    const int n=static_cast<int>(lambda.size());
    for(int i=0;i<n;++i) for(int j=i+1;j<n;++j) {
        a*=lambda[i]-lambda[j]+j-i; b*=j-i;
        auto g=std::gcd(a,b); a/=g; b/=g;
    }
    if(b!=1) throw std::runtime_error("Nonintegral Weyl dimension");
    return a;
}
int main() {
    bool first=true;
    std::cout << "{\"all_passed\":true,\"cases\":[";
    for(int n=2;n<=4;++n) {
        std::vector<int> lambda(n);
        std::function<void(int,int,int)> visit = [&](int i,int upper,int sum) {
            if(i==n) {
                if(sum!=0 || lambda.front()==0) return;
                auto c=tableaux(lambda);
                auto dim=weyl_dimension(lambda);
                bool root=lambda.front()==1 && lambda.back()==-1;
                for(int j=1;j<n-1;++j) root=root && lambda[j]==0;
                if(c.all!=dim || (n+1)*c.balanced>dim ||
                   (((n+1)*c.balanced==dim)!=root))
                    throw std::runtime_error("SSYT/Weyl/sharpness control failed");
                if(!first) std::cout << ",";
                first=false;
                std::cout << "{\"N\":" << n << ",\"lambda\":[";
                for(int j=0;j<n;++j) { if(j)std::cout<<","; std::cout<<lambda[j]; }
                std::cout << "],\"dimension\":" << dim
                          << ",\"zero_weight\":" << c.balanced << "}";
                return;
            }
            for(int x=upper;x>=-2;--x) { lambda[i]=x; visit(i+1,x,sum+x); }
        };
        visit(0,2,0);
    }
    std::cout << "]}\n";
}

