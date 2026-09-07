#include <boost/multiprecision/cpp_int.hpp>
#include <boost/rational.hpp>
#include <fstream>
#include <iostream>
#include <stdexcept>
using Z=boost::multiprecision::cpp_int;
Z power(Z a,unsigned n){Z r=1;while(n){if(n&1U)r*=a;a*=a;n>>=1U;}return r;}
Z fact(unsigned n){Z r=1;for(unsigned k=2;k<=n;++k)r*=k;return r;}
Z floor_div(const Z&a,const Z&b){Z q=a/b,r=a%b;if(r!=0&&a<0)--q;return q;}
Z ceil_div(const Z&a,const Z&b){return -floor_div(-a,b);}
void need(bool ok,const char*msg){if(!ok)throw std::runtime_error(msg);}
struct I{
 Z lo,hi,S;
 static I rational(const Z&p,const Z&q,const Z&S){return{floor_div(p*S,q),ceil_div(p*S,q),S};}
 I add(const I&x)const{return{lo+x.lo,hi+x.hi,S};}
 I sub(const I&x)const{return{lo-x.hi,hi-x.lo,S};}
 I mul(const I&x)const{Z v[4]={lo*x.lo,lo*x.hi,hi*x.lo,hi*x.hi},a=v[0],b=v[0];for(auto&z:v){if(z<a)a=z;if(z>b)b=z;}return{floor_div(a,S),ceil_div(b,S),S};}
 I inv()const{need(lo>0,"inverse crosses zero");return{floor_div(S*S,hi),ceil_div(S*S,lo),S};}
 I times(unsigned n)const{return{lo*n,hi*n,S};}
};
using Rat=boost::rational<Z>;
unsigned half_loss(){
 const Rat u(1,128),h(1,Z(1)<<128),a=1-u+u*h,b=u*h,c=u*(1-u)*h,s=a+b,d=a*b-c;
 const Rat r2=(a-b)*(a-b)+4*c,gap=4*c/(2*s-4*c/s); const Z lo=3*power(10,39),hi=4*power(10,39);
 need(2*lo*gap/(1-gap)<Rat(5,18),"loss lower"); Z m=(9*hi*s.numerator())/(10*s.denominator());
 need(m*(4*c/r2)>Rat(8,25),"loss exponent"); need(hi*s*(1-s)/((hi*s-m)*(hi*s-m))<Rat(1,1000),"loss concentration");
 need(4*hi*d/s<Rat(1,1000),"loss replacement"); Rat x(8,25);need(1+x+x*x/2+x*x*x/6>Rat(10000,7399),"exp bound");
 need(Rat(999,1000)*Rat(51,100)-Rat(1,1000)>Rat(1,2),"loss success"); return 6;
}
int main(int argc,char**argv){try{
 unsigned M=2048,digits=60;Z expected_lo=0,expected_hi=0;bool compare=false;
 if(argc==2){std::ifstream in(argv[1]);need(bool(in>>M>>digits>>expected_lo>>expected_hi),"bad packet");compare=true;} else need(argc==1,"usage");
 need(M>=16&&M<=32768&&digits>=30&&digits<=100,"unsafe dimensions"); Z S=power(10,digits),f=fact(80),partial=0;
 for(unsigned k=0;k<=80;++k){partial+=f/fact(k);}
 I elo=I::rational(partial,f,S),tail=I::rational(82,81*fact(81),S);
 I e={elo.lo,elo.hi+tail.hi,S},a=e.inv(),one={S,S,S},sum={0,0,S}; Z central=1;
 for(unsigned k=1;k<=M;++k){central=central*2*(2*k-1)/k; I c=I::rational(central*central,power(16,k)*Z(2*k-1)*Z(2*k-1),S);
  I l=I{Z(2*k)*S,Z(2*k)*S,S}.sub(a).inv(),r=I{Z(2*k-1)*S,Z(2*k-1)*S,S}.add(a).inv(); sum=sum.add(c.mul(l.add(r)));}
 I value=a.times(2).mul(one.sub(a).inv().add(a.inv()).sub(sum)),rem=a.mul(I::rational(1,Z(3)*M*M*M,S)); Z lower=value.lo-rem.hi,upper=value.hi;
 need(lower>0&&upper>lower,"invalid enclosure"); if(compare)need(lower>=expected_lo&&upper<=expected_hi,"not contained");
 central=1;for(unsigned k=1;k<=4096;++k){central=central*2*(2*k-1)/k;need(central*central*(3*k+1)<=power(16,k),"central bound");need(Z(3*k+1)*Z(2*k-1)*Z(2*k-1)>=Z(4)*k*k*k,"denominator bound");}
 need(4*power(63,18)>3*power(64,18),"9-copy"); need(4*power(63,20)<3*power(64,20),"10-copy"); Z c128=fact(128)/(fact(64)*fact(64));
 need(64*c128>127*power(3*power(10,18),2),"heterodyne"); need(8*fact(129)>3*power(10,218),"aperture");
 std::cout<<"PASS M="<<M<<" bounds=4096 finite_copy=4 loss="<<half_loss()<<"\n"<<"lower="<<lower<<"\nupper="<<upper<<"\nscale="<<S<<"\n";
 }catch(const std::exception&e){std::cerr<<"FAIL "<<e.what()<<'\n';return 1;}return 0;}
