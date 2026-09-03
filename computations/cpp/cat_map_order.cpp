#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <tuple>
#include <vector>

using i64 = long long;

static i64 modpow(i64 a, i64 e, i64 p) {
    i64 r = 1 % p; a %= p;
    while (e > 0) { if (e & 1) r = r * a % p; a = a * a % p; e >>= 1; }
    return r;
}
static i64 inv(i64 a, i64 p) { return modpow((a%p+p)%p, p-2, p); }

struct Mat2 { i64 a,b,c,d; };
static Mat2 mul(Mat2 x, Mat2 y, i64 p) {
    return { (i64)((x.a*y.a + x.b*y.c)%p),
             (i64)((x.a*y.b + x.b*y.d)%p),
             (i64)((x.c*y.a + x.d*y.c)%p),
             (i64)((x.c*y.b + x.d*y.d)%p) };
}
static int matrix_order(Mat2 A, int p, int max_iter=-1) {
    if (max_iter < 0) max_iter = p*p;
    Mat2 m{A.a%p,A.b%p,A.c%p,A.d%p};
    for(int k=1;k<=max_iter;++k){
        if(m.a==1 && m.b==0 && m.c==0 && m.d==1) return k;
        m=mul(A,m,p);
    }
    return -1;
}
static i64 tonelli(i64 n, i64 p){
    n=(n%p+p)%p;
    if(n==0) return 0;
    if(modpow(n,(p-1)/2,p)!=1) throw std::runtime_error("not a quadratic residue");
    if(p%4==3) return modpow(n,(p+1)/4,p);
    i64 q=p-1; int s=0; while((q&1)==0){q>>=1;++s;}
    i64 z=2; while(modpow(z,(p-1)/2,p)!=p-1) ++z;
    i64 c=modpow(z,q,p), x=modpow(n,(q+1)/2,p), t=modpow(n,q,p); int m=s;
    while(t!=1){
        int i=1; i64 tt=t*t%p; while(tt!=1){tt=tt*tt%p;++i; if(i>=m) throw std::runtime_error("Tonelli failure");}
        i64 b=modpow(c,1LL<<(m-i-1),p); x=x*b%p; c=b*b%p; t=t*c%p; m=i;
    }
    return x;
}
static int eigenvalue_order(Mat2 A,int p){
    i64 tr=(A.a+A.d)%p; i64 disc=(tr*tr-4)%p; if(disc<0) disc+=p;
    if(modpow(disc,(p-1)/2,p)!=1) return -1;
    i64 s=tonelli(disc,p); i64 alpha=(tr+s)%p*inv(2,p)%p;
    if(alpha==0) return -1;
    i64 x=1; for(int k=1;k<=p;++k){x=x*alpha%p;if(x==1)return k;} return -1;
}
static std::vector<int> primes(int lo,int hi){
    std::vector<bool> is(hi+1,true); is[0]=is[1]=false;
    for(int p=2;p*p<=hi;++p) if(is[p]) for(int q=p*p;q<=hi;q+=p) is[q]=false;
    std::vector<int> out; for(int p=std::max(2,lo);p<=hi;++p) if(is[p]) out.push_back(p); return out;
}
struct Row {int p,ord,k,pred;};
static std::vector<Row> scan(){
    Mat2 A{2,1,1,1}; std::vector<Row> out;
    for(int p:primes(500,5000)){
        if(p==5 || modpow(5,(p-1)/2,p)!=1) continue;
        int ord=matrix_order(A,p); if(ord<30||ord>60) continue;
        int k=eigenvalue_order(A,p); if(k<1) continue;
        int pred=p/ord; if(pred<30) continue;
        out.push_back({p,ord,k,pred});
    }
    std::sort(out.begin(),out.end(),[](const Row&x,const Row&y){return x.pred>y.pred;});
    return out;
}
static bool verify(){
    Mat2 A{2,1,1,1}; bool ok=true;
    ok &= matrix_order(A,31)==15; // corrected full matrix order; legacy helper comment claimed 5.
    ok &= matrix_order(A,4481)==64;
    auto rows=scan();
    const std::vector<Row> want={{3469,51,51,68},{3001,50,50,60},{2161,40,40,54},{2521,60,60,42}};
    if(rows.size()!=want.size()) ok=false;
    for(std::size_t i=0;i<std::min(rows.size(),want.size());++i)
        if(std::tie(rows[i].p,rows[i].ord,rows[i].k,rows[i].pred)!=std::tie(want[i].p,want[i].ord,want[i].k,want[i].pred)) ok=false;
    std::cout<<(ok?"PASS":"FAIL")<<" cat-map order/prime-scan regression\n";
    if(matrix_order(A,31)!=5) std::cout<<"NOTE legacy Julia comment p=31 -> 5 is false; exact matrix order is "<<matrix_order(A,31)<<"\n";
    return ok;
}
int main(int argc,char**argv){
    if(argc<2){std::cerr<<"usage: catmap_order {verify|scan|order p}\n";return 2;}
    std::string cmd=argv[1]; Mat2 A{2,1,1,1};
    if(cmd=="verify") return verify()?0:1;
    if(cmd=="scan") { for(auto r:scan()) std::cout<<r.p<<" "<<r.ord<<" "<<r.k<<" "<<r.pred<<"\n"; return 0; }
    if(cmd=="order"&&argc==3){int p=std::stoi(argv[2]);std::cout<<matrix_order(A,p)<<"\n";return 0;}
    return 2;
}
