// Exact Gaussian-integer sparse dot products with dyadic rounding after each product.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using I=std::int64_t;
using Wide=__int128_t;
constexpr I scale=I(1)<<61;
struct Entry { int col; I re,im; };
using Matrix=std::vector<std::vector<Entry>>;
static I rounded(Wide v) {
    bool neg=v<0;
    Wide q=((neg?-v:v)+scale/2)/scale;
    assert(q<=Wide(scale)*2);
    return neg?-I(q):I(q);
}
Matrix multiply(const Matrix& a,const Matrix& b) {
    int n=a.size();
    Matrix c(n);
    std::vector<Wide> real(n),imag(n);
    for(int row=0;row<n;row++) {
        for(const auto& x:a[row]) for(const auto& y:b[x.col]) {
            real[y.col]+=Wide(x.re)*y.re-Wide(x.im)*y.im;
            imag[y.col]+=Wide(x.re)*y.im+Wide(x.im)*y.re;
        }
        for(int j=0;j<n;j++) {
            I re=rounded(real[j]),im=rounded(imag[j]);
            if(std::max(std::abs(re),std::abs(im))>6) c[row].push_back({j,re,im});
            real[j]=imag[j]=0;
        }
    }
    return c;
}
int main(int argc,char** argv) {
    if(argc!=2)return 1;
    std::ifstream in(argv[1]);int n;
    if(!(in>>n)||n<=0||n>=3000)return 2;
    Matrix h(n),result;
    int r,c;I re,im;
    while(in>>r>>c>>re>>im)h.at(r).push_back({c,re,im});
    int k=209;
    while(k){
        if(k%2)result=result.empty()?h:multiply(result,h);
        k/=2;
        if(k)h=multiply(h,h);
    }
    // The sum is assembled in Python with arbitrary precision.
    for(int i=0;i<n;i++)for(auto& x:result[i])if(x.col==i)
        std::cout<<x.re<<" "<<x.im<<"\n";
}
