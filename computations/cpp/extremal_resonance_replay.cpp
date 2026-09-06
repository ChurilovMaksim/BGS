// Independent exact checker. No floating-point roots or finite orbit cutoffs.
#include <boost/multiprecision/cpp_int.hpp>
#include <array>
#include <fstream>
#include <iostream>
#include <set>
#include <stdexcept>
#include <vector>
using Z=boost::multiprecision::cpp_int;
using V=std::array<Z,2>;
using M=std::array<Z,4>;
int sign(const Z& z){return z>0?1:(z<0?-1:0);}
struct Q {
 Z a,b,d;
 Q operator+(const Q& q)const{return {a+q.a,b+q.b,d};}
 Q operator-(const Q& q)const{return {a-q.a,b-q.b,d};}
 Q operator*(const Q& q)const{return {a*q.a+d*b*q.b,a*q.b+b*q.a,d};}
 Q scale(const Z& z)const{return {a*z,b*z,d};}
 int sgn()const{
  if(b==0)return sign(a);
  if(a==0)return sign(b);
  if(sign(a)==sign(b))return sign(a);
  return sign(a)*sign(a*a-d*b*b);
 }
 Q abs()const{return sgn()<0?scale(-1):*this;}
 bool operator>(const Q& q)const{return (*this-q).sgn()>0;}
};
V mv(const M& a,const V& v){return {a[0]*v[0]+a[1]*v[1],a[2]*v[0]+a[3]*v[1]};}
M mm(const M& a,const M& b){return {a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]};}
M power(M a,int n){M b={1,0,0,1};while(n){if(n&1)b=mm(b,a);a=mm(a,a);n/=2;}return b;}
Q qp(Q a,int n){Q b={1,0,a.d};while(n){if(n&1)b=b*a;a=a*a;n/=2;}return b;}
V plus(const V& a,const V& b){return {a[0]+b[0],a[1]+b[1]};}
void need(bool b,const char* text){if(!b)throw std::runtime_error(text);}
void check(const M& a,int r,const std::vector<V>& vs,const V& u,const V& v){
 need(r>=1,"nonpositive lag");
 need(a[0]*a[3]-a[1]*a[2]==1,"determinant is not one");
 Z tr=a[0]+a[3],t=tr<0?-tr:tr;need(t>=3,"nonhyperbolic matrix");
 Z sg=tr>0?1:-1,d=t*t-4;
 std::set<V> ss(vs.begin(),vs.end());
 need(!ss.empty()&&ss.size()==vs.size()&&!ss.count(V{0,0}),"invalid support");
 for(const auto& w:vs)need(ss.count(V{-w[0],-w[1]})!=0,"asymmetric support");
 need(ss.count(u)&&ss.count(v),"witness outside support");
 auto xi=[&](const V& w){return Q{2*sg*a[2]*w[0]+(t-2*sg*a[0])*w[1],w[1],d};};
 auto eta=[&](const V& w){Q q=xi(w);q.b=-q.b;return q;};
 Q X={0,0,d},Y={0,0,d},l={t,1,d};
 for(const auto& w:vs){Q x=xi(w).abs(),y=eta(w).abs();if(x>X)X=x;if(y>Y)Y=y;}
 V av=mv(power(a,r),v),k=plus(u,av);
 need(u[0]*av[1]-u[1]*av[0]!=0,"zero determinant");
 M aj={1,0,0,1};
 for(int j=1;j<=r;++j){aj=mm(aj,a);int count=0;
  for(const auto& p:vs)for(const auto& q:vs)if(plus(p,mv(aj,q))==k)++count;
  need(count==(j==r?1:0),"decomposition or lower-lag collision");
 }
 Z two=Z(1)<<r;
 need((l*xi(k).abs()).scale(two)>(Q{two,0,d}+qp(l,r))*X.scale(2),"forward escape");
 need(l*l*eta(k).abs()>(l.scale(2)+Q{4,0,d})*Y,"backward escape");
}
int main(int argc,char** argv){try{
 if(argc==1){int count=0;
  for(int t:{3,6,25})for(int s:{-1,1})for(int r=1;r<=10;++r){
   M a={s*t,-s,s,0};V v={((s<0&&(r&1))?-1:1),0};
   check(a,r,{{1,0},{-1,0}},{1,0},v);++count;
  }
  bool rejected=false;
  try{check({3,-1,1,0},1,{{1,0},{-1,0}},{0,0},{1,0});}catch(const std::runtime_error&){rejected=true;}
  need(rejected,"negative control accepted");
  std::cout<<"PASS self-tests="<<count<<" negative-controls=1\n";return 0;
 }
 need(argc==2,"usage: extremal_resonance_replay [packet]");
 std::ifstream in(argv[1]);need(bool(in),"cannot open packet");
 int cases;need(bool(in>>cases)&&cases>0&&cases<=1000000,"invalid case count");
 for(int c=0;c<cases;++c){M a;int r,n;V u,v;
  need(bool(in>>a[0]>>a[1]>>a[2]>>a[3]>>r>>n>>u[0]>>u[1]>>v[0]>>v[1]),"truncated header");
  need(r>=1&&r<=10000&&n>=1&&n<=100000,"invalid packet dimensions");
  std::vector<V> vs(static_cast<std::size_t>(n));
  for(auto& w:vs)need(bool(in>>w[0]>>w[1]),"truncated support");
  try{check(a,r,vs,u,v);}catch(const std::runtime_error& e){throw std::runtime_error("case "+std::to_string(c)+": "+e.what());}
 }
 std::string rest;need(!(in>>rest),"trailing input");
 std::cout<<"PASS independent exact witnesses="<<cases<<'\n';
 }catch(const std::exception& e){std::cerr<<"FAIL "<<e.what()<<'\n';return 1;}
}
