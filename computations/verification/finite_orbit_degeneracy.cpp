// Exact independent regression for the invariant-degeneracy step.
// Build: g++ -std=c++20 -O2 finite_orbit_degeneracy.cpp -o finite_orbit_degeneracy
// No finite regression is a proof of analytic resonance rigidity.
#include <boost/multiprecision/cpp_int.hpp>
#include <array>
#include <iostream>
#include <stdexcept>
#include <vector>
using Z=boost::multiprecision::cpp_int;
using V=std::array<Z,2>;
using M=std::array<std::array<Z,2>,2>;
V add(const V&a,const V&b){return {a[0]+b[0],a[1]+b[1]};}
V mul(int t,const V&a){return {t*a[0],t*a[1]};}
V av(const M&a,const V&v){return {a[0][0]*v[0]+a[0][1]*v[1],a[1][0]*v[0]+a[1][1]*v[1]};}
Z det(const V&a,const V&b){return a[0]*b[1]-a[1]*b[0];}
Z q(const M&a,const V&v){return det(v,av(a,v));}
M inv(const M&a){return {{{a[1][1],-a[0][1]},{-a[1][0],a[0][0]}}};}
V power(const M&a,V v,int n){const M b=n<0?inv(a):a;for(int j=0;j<(n<0?-n:n);++j)v=av(b,v);return v;}
void check(bool v,const char*message){if(!v)throw std::runtime_error(message);}
int main(){
 try {
  std::vector<M> mats={M{{{2,1},{1,1}}},M{{{3,2},{4,3}}},M{{{0,-1},{1,4}}},M{{{1,3},{1,4}}}};
  for(int i=0;i<4;++i){M b=mats[i];for(auto&row:b)for(auto&x:row)x=-x;mats.push_back(b);}
  unsigned long long triples=0, identities=0, recurrence_checks=0, delayed=0;
  for(const M&a:mats){
   std::vector<V> vs={{1,0},{0,1},{1,1},{1,-1},{2,1},{1,2}};
   vs.push_back(av(a,vs[0]));
   vs.push_back(mul(-1,power(a,vs[1],-2)));
   const Z tr=a[0][0]+a[1][1];
   for(const V&u:vs)for(const V&v:vs){
    Z b0=q(a,add(u,v))-q(a,u)-q(a,v);
    Z b1=q(a,add(u,av(a,v)))-q(a,u)-q(a,v);
    for(int m=0;m<15;++m){
     Z b2=q(a,add(u,power(a,v,m+2)))-q(a,u)-q(a,v);
     check(b2==tr*b1-b0,"cross invariant recurrence failed");
     ++recurrence_checks;b0=b1;b1=b2;
    }
   }
   for(const V&vi:vs)for(const V&vj:vs)for(const V&vk:vs)
    for(int gap=-4;gap<=4;++gap)for(int eps:{-1,1})for(int parity=0;parity<2;++parity){
     ++triples;int n=gap<0?-gap+2:2;if(n%2!=parity)++n;
     bool three=true;
     for(int t=0;t<3;++t){
      int nn=n+2*t;
      if(q(a,add(vi,mul(-1,power(a,vi,nn))))!=q(a,add(vj,mul(eps,power(a,vk,nn+gap))))){three=false;break;}
     }
     if(!three)continue;
     ++identities;
     check(q(a,vj)==q(a,vi)&&q(a,vk)==q(a,vi),"double-root invariant condition failed");
     check(vj==mul(-eps,power(a,vk,gap)),"integer eigen-covector injectivity consequence failed");
     // Nontrivial invariant identity is checked at fresh, nonconsecutive gaps.
     for(int t:{7,11,18}){
      int nn=n+2*t;
      check(q(a,add(vi,mul(-1,power(a,vi,nn))))==q(a,add(vj,mul(eps,power(a,vk,nn+gap)))),"identity continuation failed");
     }
    }
   // Arbitrarily late new-family collision: vi-A^n vi=2vi+(-vi-A^n vi).
   const V vi={1,0};
   for(int n:{1,5,17,50,100}){
    const V target=add(vi,mul(-1,power(a,vi,n)));
    const V u=mul(2,vi), w=mul(-1,add(vi,power(a,vi,n)));
    check(target==add(u,w),"late collision identity failed");++delayed;
   }
  }
  std::cout<<"{\n  \"status\": \"passed exact finite regressions\",\n"
   <<"  \"matrices\": "<<mats.size()<<",\n"
   <<"  \"coefficient_identity_candidates\": "<<triples<<",\n"
   <<"  \"identities_found\": "<<identities<<",\n"
   <<"  \"recurrence_checks\": "<<recurrence_checks<<",\n"
   <<"  \"delayed_collision_checks\": "<<delayed<<",\n"
   <<"  \"arithmetic\": \"Boost arbitrary-precision integers\",\n"
   <<"  \"nonclaim\": \"No universal theorem certified by this finite run\"\n}\n";
 }catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 1;}
}
