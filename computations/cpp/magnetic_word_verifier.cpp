// Exact histogram generator via affine monomial operators and fixed points.
// Default execution generates histograms; it does not independently validate them.
// No Weyl-state formula is used: O f(x)=e_p(q(l*x+d)) f(u*x+v).
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using I=std::int64_t;
I mod(I a,I p){a%=p;return a<0?a+p:a;}
I pw(I a,I e,I p){I b=1;for(;e;e/=2,a=a*a%p)if(e%2)b=b*a%p;return b;}
bool isprime(I p){if(p<2)return false;for(I d=2;d*d<=p;++d)if(p%d==0)return false;return true;}
struct Audit{
 I p,K,h,m,half;std::vector<I> ih,c;
 Audit(I P,I k,I g,I M):p(P),K(k),h(g),m(M),half((p+1)/2){
  if(!isprime(p)||p==2||p>1009||K<1||K%2==0||(p-1)%K||m<1||m>8)
   throw std::invalid_argument("require odd prime p<=1009, odd K|p-1, 1<=m<=8");
  c.assign(static_cast<std::size_t>(p),0);
  h=mod(h,p);I a=1,work=1;
  for(I i=0;i<K;++i){if(i&&a==1)throw std::invalid_argument("smaller order");ih.push_back(pw(a,p-2,p));a=a*h%p;}
  if(a!=1)throw std::invalid_argument("wrong order");
  for(I i=0;i<m;++i){if(work>10000000/(2*K))throw std::invalid_argument("too many words");work*=2*K;}
 }
 void visit(I j,I u,I v,I l,I d){
  if(j==m){
   for(I x=0;x<p;++x){
    if(mod(u*x+v,p)==x)++c[mod(l*x+d,p)];
    if(mod(-u*x+v,p)==x)--c[mod(-l*x+d,p)];
   }return;
  }
  for(I invh:ih)for(I e:{I(-1),I(1)})
   visit(j+1,mod(invh*u,p),mod(invh*(v-e),p),mod(l+e*u,p),mod(d+e*v-half,p));
 }
 std::vector<I> run(){visit(0,1,0,0,0);I z=c.back();for(I& x:c)x-=z;return c;}
};
int main(int argc,char**argv){try{
 if(argc==6&&std::string(argv[1])=="--histogram"){
  Audit a(std::stoll(argv[2]),std::stoll(argv[3]),std::stoll(argv[4]),std::stoll(argv[5]));
  auto c=a.run();for(std::size_t i=0;i<c.size();++i)std::cout<<(i?" ":"")<<c[i];std::cout<<"\n";return 0;
 }
 if(argc!=1)throw std::invalid_argument("usage: magnetic_word_verifier [--histogram p K h m]");
 std::cout<<"GENERATED exact affine-word histograms; no independent expected-value check\n";
 for(I m=1;m<=6;++m){Audit a(7,3,2,m);auto c=a.run();
  std::cout<<"p=7 K=3 m="<<m<<" canonical=";for(I x:c)std::cout<<x<<",";std::cout<<"\n";}
 return 0;
}catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 1;}}
