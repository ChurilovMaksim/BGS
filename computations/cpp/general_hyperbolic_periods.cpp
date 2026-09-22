// Exact finite checks using matrix trace sums, rather than the Python u-recurrence.
// Not a proof of the analytic or character-theoretic limit. Execution status
// is established only by an actual successful run and retained stdout.
#include <boost/multiprecision/cpp_int.hpp>
#include <array>
#include <iostream>
#include <stdexcept>
using Z=boost::multiprecision::cpp_int;
using Mat=std::array<Z,4>;
const Mat identity{1,0,0,1};
Z mod(Z x,const Z& n){x%=n;if(x<0)x+=n;return x;}
Z gcd(Z a,Z b){if(a<0)a=-a;if(b<0)b=-b;while(b!=0){Z r=a%b;a=b;b=r;}return a;}
Mat mul(const Mat& a,const Mat& b){return {a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]};}
Mat reduce(Mat a,const Z& n){for(auto& x:a)x=mod(x,n);return a;}
Mat shifted(Mat a,int s){a[0]+=s;a[3]+=s;return a;}
Z det(const Mat& a){return a[0]*a[3]-a[1]*a[2];}
Mat power(Mat a,int k){Mat r=identity;for(int j=0;j<k;++j)r=mul(r,a);return r;}
int euler(int x,int k){int r=1;x%=k;if(x<0)x+=k;for(int j=0;j<(k-1)/2;++j)r=r*x%k;if(r!=1&&r!=k-1)throw std::runtime_error("bad Euler sign");return r==1?1:-1;}
void require(bool p,const char* message){if(!p)throw std::runtime_error(message);}
int main(){
 try{
  std::cout<<"{\"checks\":[";bool comma=false;int count=0;
  for(int sign:{-1,1})for(int a=3;a<=12;++a)for(int k:{5,7,11,13,17,23,31}){
   if((a-2*sign)%k==0)continue;
   const int t=sign*a,m=(k-1)/2;const Mat A{t-1,t-2,1,1};
   Mat p=identity;Z signedN=1;
   for(int j=1;j<=m;++j){p=mul(p,A);signedN+=p[0]+p[3];}
   Z n=signedN<0?-signedN:signedN;const int c=euler(a-2*sign,k);
   require(mod(n,2)==1,"even modulus");
   require(mod(n-c,2*k)==0,"sector divisibility");
   Mat left=shifted(power(A,k),-1);Mat right=mul(power(A,m),shifted(A,-1));
   for(auto& x:right)x*=signedN;
   require(left==right,"exact factorization");
   Mat aj=identity;
   for(int j=1;j<=k;++j){
    aj=reduce(mul(aj,A),n);
    if(j<k)require(gcd(det(shifted(aj,-1)),n)==1,"minus determinant nonunit");
    require(gcd(det(shifted(aj,1)),n)==1,"plus determinant nonunit");
   }
   require(aj==identity,"wrong period");
   const Z base=(n-c)/k;
   require(k*base+c==n,"multiplicity total");
   require(k*base*base+2*c*base+1==(n*n+k-1)/k,"squared multiplicity total");
   if(comma) std::cout<<',';
   comma=true;
   ++count;
   std::cout<<"{\"trace\":"<<t<<",\"K\":"<<k<<",\"N\":\""<<n<<"\",\"sign\":"<<c<<",\"uniform_dimension\":\""<<(n-c)/2<<"\",\"root_multiplicity\":\""<<(n-c)/(2*k)<<"\"}";
  }
  require(count==131,"unexpected test count");
  Mat negPell{-3,-2,-4,-3},p=identity;
  for(int j=0;j<7;++j)p=reduce(mul(p,negPell),169);
  require(p==identity,"prime-square negative Pell control");
  require(Z(13)*13==169&&Z(23)*43==989,"factor controls");
  std::cout<<"],\"count\":"<<count<<",\"status\":\"PASS\",\"scope\":\"Finite exact matrix-arithmetic controls, not an analytic proof or measured quantum spectrum.\"}\n";
  return 0;
 }catch(const std::exception& e){std::cerr<<e.what()<<'\n';return 1;}
}
