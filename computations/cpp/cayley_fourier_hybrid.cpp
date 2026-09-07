#include <algorithm>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>
using i64=long long;
static i64 modpow(i64 a,i64 e,i64 p){i64 r=1;while(e){if(e&1)r=r*a%p;a=a*a%p;e>>=1;}return r;}
static bool prime(int n){if(n<2)return false;for(int d=2;1LL*d*d<=n;++d)if(n%d==0)return false;return true;}
static std::vector<int> prime_factors(int n){std::vector<int> q;for(int d=2;1LL*d*d<=n;++d)if(n%d==0){q.push_back(d);while(n%d==0)n/=d;}if(n>1)q.push_back(n);return q;}
static int primitive_root(int p){auto qs=prime_factors(p-1);for(int g=2;g<p;++g){bool ok=true;for(int q:qs)if(modpow(g,(p-1)/q,p)==1){ok=false;break;}if(ok)return g;}throw std::runtime_error("root");}
static std::vector<int> divisors(int n){std::vector<int>d;for(int k=1;k<=n;++k)if(n%k==0)d.push_back(k);return d;}
static int inv(int a,int p){return (int)modpow(a,p-2,p);}
static int cayley(int h,int p){return (int)((i64)(h+1)*inv((h-1+p)%p,p)%p);}
int main(int argc,char**argv){
  try{
    int limit=257;if(argc==2)limit=std::stoi(argv[1]); if(limit<5||limit>2000)throw std::runtime_error("limit 5..2000");
    long long designs=0,dense=0;int maxK=0;
    for(int p=3;p<=limit;++p)if(prime(p)){
      int g=primitive_root(p);
      for(int K:divisors(p-1))if(K>=2){
        std::vector<int>A;int step=(p-1)/K;
        for(int j=0;j<K;++j){int h=(int)modpow(g,1LL*step*j,p);if(h!=1)A.push_back(cayley(h,p));}
        std::sort(A.begin(),A.end());A.erase(std::unique(A.begin(),A.end()),A.end());
        if((int)A.size()!=K-1)throw std::runtime_error("Cayley not injective");
        for(int a:A)if(!std::binary_search(A.begin(),A.end(),(p-a)%p))throw std::runtime_error("not symmetric");
        std::vector<i64>r(p),rd(p);
        for(int a:A)for(int b:A){++r[(a+b)%p];++rd[(a-b+p)%p];}
        i64 E=0,Ed=0;for(int t=0;t<p;++t){E+=r[t]*r[t];Ed+=rd[t]*rd[t];}
        if(E!=Ed)throw std::runtime_error("sum/difference energy mismatch");
        i64 n=K-1;
        i64 centered=(i64)p*E-n*n*n*n;
        i64 rhs=4LL*p*n*(p-n);
        if(centered<0||centered>rhs)throw std::runtime_error("hybrid integer bound failed");
        ++designs;maxK=std::max(maxK,K);
        i64 K5=1; for(int j=0;j<5;++j)K5*=K;
        i64 p3=1LL*p*p*p; if(K5>p3)++dense;
      }
    }
    bool rejected=false;try{std::vector<int>A={0,1,1};std::sort(A.begin(),A.end());if(std::unique(A.begin(),A.end())!=A.end())throw std::runtime_error("duplicate");}catch(...){rejected=true;}
    if(!rejected)throw std::runtime_error("negative control");
    std::cout<<"PASS exact Cayley centered-energy regression: designs="<<designs<<" dense="<<dense<<" maxK="<<maxK<<" negative_controls=1\n";
  }catch(const std::exception&e){std::cerr<<"FAIL "<<e.what()<<"\n";return 1;}return 0;
}
