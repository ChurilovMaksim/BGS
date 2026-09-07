// Independent multiprecision scalar checks for the pure-loss discrimination theorem.
// Finite-grid verification is evidence for algebra/implementation, not the continuum proof.
#include <boost/multiprecision/cpp_dec_float.hpp>
#include <iostream>
#include <stdexcept>
using R = boost::multiprecision::number<boost::multiprecision::cpp_dec_float<100>>;
R powi(R x,int n){R y=1;while(n-- > 0)y*=x;return y;}
void need(bool x,const char* m){if(!x)throw std::runtime_error(m);}
int main(){try{
  const R us[] = {R(1)/16,R(1)/32,R(1)/100,R(1)/1000};
  const R es[] = {R("0.01"),R("0.05"),R("0.2"),R("0.5"),R("0.8"),R("0.99"),R(1)};
  const int ns[] = {1,2,3,5,10,20};
  unsigned count=0; R maxdq=0,maxl=0;
  for(R u:us)for(R eta:es)for(int n:ns){
    R en=powi(eta,n), zn=powi(R(1)-eta,n), q=u*en;
    R a=1-u+u*zn,b=q,c2=u*(1-u)*en,s=a+b;
    R r2=(a-b)*(a-b)+4*c2;
    R d=a*b-c2, gamma=(a-b)*(a-b)/r2, delta=1-gamma,L=-log(gamma);
    need(abs(d-u*u*powi(eta*(1-eta),n)) < R("1e-80"),"determinant identity");
    need(s>=1-u && s<=1,"block weight");
    need(r2>=(1-2*u)*(1-2*u),"gap lower bound");
    need(delta<=5*q,"delta upper");
    need(abs(delta-4*q)<=16*u*q,"delta comparison");
    need(abs(L-4*q)<=35*u*q,"log comparison");
    need(L<=8*q,"log upper");
    maxdq=max(maxdq,delta/q); maxl=max(maxl,abs(L-4*q)/(u*q)); ++count;
  }
  std::cout << "{\"status\":\"PASS\",\"cases\":"<<count
            <<",\"max_delta_over_q\":\""<<maxdq
            <<"\",\"max_log_error_ratio\":\""<<maxl
            <<"\",\"scope\":\"multiprecision finite scalar grid\"}\n";
  return 0;
 }catch(const std::exception& e){std::cerr<<e.what()<<'\n';return 1;}}
