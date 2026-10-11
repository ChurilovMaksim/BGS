// Exact finite controls over Q(i); no numerical tolerances or sqrt evaluations.
// These witnesses do not replace the universally quantified written proofs.
#include <iostream>
#include <stdexcept>
#include <vector>

using Int = __int128_t;
Int neg(Int a){Int c;if(__builtin_sub_overflow(Int(0),a,&c))throw std::overflow_error("negation overflow");return c;}
Int gcd(Int a,Int b){if(a<0)a=neg(a);if(b<0)b=neg(b);while(b){Int c=a%b;a=b;b=c;}return a;}
Int mul(Int a,Int b){Int c;if(__builtin_mul_overflow(a,b,&c))throw std::overflow_error("multiplication overflow");return c;}
Int add(Int a,Int b){Int c;if(__builtin_add_overflow(a,b,&c))throw std::overflow_error("addition overflow");return c;}
struct R {
 Int n=0,d=1;
 R(long long a=0):n(a){}
 R(Int a,Int b):n(a),d(b){if(!d)throw std::runtime_error("zero rational denominator");if(d<0){n=neg(n);d=neg(d);}Int g=gcd(n,d);n/=g;d/=g;}
 friend R operator+(R a,R b){Int g=gcd(a.d,b.d);return R(add(mul(a.n,b.d/g),mul(b.n,a.d/g)),mul(a.d,b.d/g));}
 friend R operator-(R a){return R(neg(a.n),a.d);}
 friend R operator-(R a,R b){return a+(-b);}
 friend R operator*(R a,R b){Int g=gcd(a.n,b.d),h=gcd(b.n,a.d);return R(mul(a.n/g,b.n/h),mul(a.d/h,b.d/g));}
 friend R operator/(R a,R b){return a*R(b.d,b.n);}
 friend bool operator==(R a,R b){return a.n==b.n&&a.d==b.d;}
 friend bool operator<(R a,R b){return (a-b).n<0;}
 friend bool operator>=(R a,R b){return !(a<b);}
 R&operator+=(R b){return *this=*this+b;}
};
struct C {
    R re, im;
    C(R x=R(0), R y=R(0)): re(x), im(y) {}
};
C operator+(C a,C b){return {a.re+b.re,a.im+b.im};}
C operator-(C a,C b){return {a.re-b.re,a.im-b.im};}
C operator-(C a){return {-a.re,-a.im};}
C operator*(C a,C b){return {a.re*b.re-a.im*b.im,a.re*b.im+a.im*b.re};}
C star(C a){return {a.re,-a.im};}
R square(C a){return a.re*a.re+a.im*a.im;}
C operator/(C a,C b){R den=square(b); if(den==R(0))throw std::runtime_error("zero division"); return a*star(b)*C(R(1)/den);}
bool operator==(C a,C b){return a.re==b.re && a.im==b.im;}
using M = std::vector<std::vector<C>>;
M zero(int n,int m){return M(n,std::vector<C>(m));}
M eye(int n){M a=zero(n,n);for(int i=0;i<n;i++)a[i][i]=C(1);return a;}
M operator+(const M&a,const M&b){M c=a;for(int i=0;i<(int)a.size();i++)for(int j=0;j<(int)a[0].size();j++)c[i][j]=a[i][j]+b[i][j];return c;}
M operator-(const M&a,const M&b){M c=a;for(int i=0;i<(int)a.size();i++)for(int j=0;j<(int)a[0].size();j++)c[i][j]=a[i][j]-b[i][j];return c;}
M operator*(const M&a,const M&b){M c=zero(a.size(),b[0].size());for(int i=0;i<(int)a.size();i++)for(int k=0;k<(int)b.size();k++)for(int j=0;j<(int)b[0].size();j++)c[i][j]=c[i][j]+a[i][k]*b[k][j];return c;}
M operator*(C v,const M&a){M b=a;for(auto&row:b)for(auto&x:row)x=v*x;return b;}
M adj(const M&a){M b=zero(a[0].size(),a.size());for(int i=0;i<(int)a.size();i++)for(int j=0;j<(int)a[0].size();j++)b[j][i]=star(a[i][j]);return b;}
C trace(const M&a){C x;for(int i=0;i<(int)a.size();i++)x=x+a[i][i];return x;}
R hs2(const M&a){R x(0);for(const auto&row:a)for(C y:row)x+=square(y);return x;}
void require(bool b,const char*what){if(!b)throw std::runtime_error(what);}
void equal(const M&a,const M&b,const char*what){require(a==b,what);}
M inverse(M a){int n=a.size();M b=eye(n);for(int j=0;j<n;j++){int pivot=j;while(pivot<n && a[pivot][j]==C(0))pivot++;require(pivot<n,"singular matrix");std::swap(a[pivot],a[j]);std::swap(b[pivot],b[j]);C d=a[j][j];for(int k=0;k<n;k++){a[j][k]=a[j][k]/d;b[j][k]=b[j][k]/d;}for(int i=0;i<n;i++)if(i!=j){C q=a[i][j];for(int k=0;k<n;k++){a[i][k]=a[i][k]-q*a[j][k];b[i][k]=b[i][k]-q*b[j][k];}}}return b;}
C det(M a){int n=a.size();C out(1);for(int j=0;j<n;j++){int p=j;while(p<n && a[p][j]==C(0))p++;if(p==n)return C(0);if(p!=j){std::swap(a[p],a[j]);out=-out;}C d=a[j][j];out=out*d;for(int i=j+1;i<n;i++){C q=a[i][j]/d;for(int k=j;k<n;k++)a[i][k]=a[i][k]-q*a[j][k];}}return out;}
M powm(M a,int k){M out=eye(a.size());for(int j=0;j<k;j++)out=out*a;return out;}
M rotate(int m,int offset){M r=eye(m);for(int j=offset;j+1<m;j+=2){r[j][j]=C(R(3,5));r[j][j+1]=C(R(-4,5));r[j+1][j]=C(R(4,5));r[j+1][j+1]=C(R(3,5));}return r;}
M mobius(const M&a,C center){return (a-center*eye(a.size()))*inverse(eye(a.size())-star(center)*a);}

int main(){
 try{
  int julia=0,terms=0,mobius_controls=0;
  for(int m: {2,3,5}){
   M left=rotate(m,0),right=rotate(m,1);
   M phase=eye(m);for(int j=0;j<m;j++)phase[j][j]=j%2?C(R(3,5),R(4,5)):C(0,1);
   right=right*phase;
   M values=zero(m,m),defects=zero(m,m);
   for(int j=0;j<m;j++){values[j][j]=C(j%2?R(4,5):R(3,5));defects[j][j]=C(j%2?R(3,5):R(4,5));}
   M g=left*values*adj(right),gamma=left*defects*adj(left),delta=right*defects*adj(right);
   equal(g*delta,gamma*g,"intertwining");
   equal(g*adj(g)+gamma*gamma,eye(m),"left defect");
   equal(adj(g)*g+delta*delta,eye(m),"right defect");
   M jg=zero(2*m,2*m);M gs=adj(g);
   for(int i=0;i<m;i++)for(int j=0;j<m;j++){jg[i][j]=g[i][j];jg[i][m+j]=-gamma[i][j];jg[m+i][j]=delta[i][j];jg[m+i][m+j]=gs[i][j];}
   equal(adj(jg)*jg,eye(2*m),"julia left unitary");equal(jg*adj(jg),eye(2*m),"julia right unitary");
   julia++;
  }
  for(int q: {1,2}){
   int n=4*q;M a=zero(n,n),u=zero(n,n);
   C omega(0,1);
   for(int i=0;i<4;i++)for(int j=0;j<4;j++){
    C v(1);for(int k=0;k<(i*j)%4;k++)v=v*omega;
    for(int h=0;h<q;h++)u[i*q+h][j*q+h]=C(R(1,2))*v;
   }
   for(int i=0;i<4;i++)for(int j=0;j<q;j++)for(int k=0;k<q;k++)a[i*q+j][i*q+k]=C(R(i+j+1,32),R(k-i,64));
   M b=u*a*adj(u);equal(adj(u)*u,eye(n),"Fourier unitary");
   require(hs2(a)<R(1),"strict contraction witness");
   M aa=a*adj(a),bb=b*adj(b),ba=b*adj(a);
   for(int k=1;k<=8;k++){
    R term=(trace(powm(aa,k)).re+trace(powm(bb,k)).re)/R(2)-trace(powm(ba,k)).re;
    require(term>=R(0),"nonnegative log coefficient");terms++;
    if(k==1)require(term==hs2(a-b)/R(2),"first coefficient");
   }
  }
  for(int choice: {0,1}){
   int n=2;M a=zero(n,n),b=zero(n,n);
   a[0][0]=C(R(1,8));a[0][1]=C(0,R(1,16));a[1][0]=C(R(1,32));a[1][1]=C(R(1,8));
   b[0][0]=C(R(1,16));b[0][1]=C(R(1,32));b[1][0]=C(0,R(1,64));b[1][1]=C(R(1,16));
   C center=choice?C(R(1,4),R(1,8)):C(R(1,4));M fa=mobius(a,center),fb=mobius(b,center);
   M right=C(R(1)-square(center))*inverse(eye(n)-star(center)*b)*(eye(n)-b*adj(a))*inverse(eye(n)-center*adj(a));
   equal(eye(n)-fb*adj(fa),right,"ordered Mobius identity");
   // Exponentiating 2D avoids logarithms; this ratio lies in Q.
   R before=square(det(eye(n)-b*adj(a)))/(det(eye(n)-a*adj(a)).re*det(eye(n)-b*adj(b)).re);
   R after=square(det(eye(n)-fb*adj(fa)))/(det(eye(n)-fa*adj(fa)).re*det(eye(n)-fb*adj(fb)).re);
   require(before==after,"diastasis ratio invariant");mobius_controls++;
  }
  std::cout<<"{\"arithmetic\":\"exact Q(i), 128-bit integers with overflow traps\",\"julia_witnesses\":"<<julia<<",\"log_coefficient_witnesses\":"<<terms<<",\"mobius_witnesses\":"<<mobius_controls<<",\"all_passed\":true,\"scope\":\"finite controls, not formal proof of all parameters\"}\n";
 }catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 1;}
}
