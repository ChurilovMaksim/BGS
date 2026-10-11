#include <iostream>
#include <stdexcept>
#include <vector>

using I=__int128_t;
I checked_neg(I a){I c;if(__builtin_sub_overflow(I(0),a,&c))throw std::overflow_error("exact rational negation");return c;}
I gcd(I a,I b){if(a<0)a=checked_neg(a);if(b<0)b=checked_neg(b);while(b){I c=a%b;a=b;b=c;}return a;}
I checked_mul(I a,I b){I c;if(__builtin_mul_overflow(a,b,&c))throw std::overflow_error("exact rational multiplication");return c;}
I checked_add(I a,I b){I c;if(__builtin_add_overflow(a,b,&c))throw std::overflow_error("exact rational addition");return c;}
struct R {
 I n=0,d=1;
 R(long long a=0):n(a){}
 R(I a,I b):n(a),d(b){if(!d)throw std::runtime_error("zero rational denominator");if(d<0){n=checked_neg(n);d=checked_neg(d);}I g=gcd(n,d);n/=g;d/=g;}
 friend R operator+(R a,R b){I g=gcd(a.d,b.d);return R(checked_add(checked_mul(a.n,b.d/g),checked_mul(b.n,a.d/g)),checked_mul(a.d,b.d/g));}
 friend R operator-(R a){return R(checked_neg(a.n),a.d);}
 friend R operator-(R a,R b){return a+(-b);}
 friend R operator*(R a,R b){I g=gcd(a.n,b.d),h=gcd(b.n,a.d);return R(checked_mul(a.n/g,b.n/h),checked_mul(a.d/h,b.d/g));}
 friend R operator/(R a,R b){return a*R(b.d,b.n);}
 friend bool operator==(R a,R b){return a.n==b.n&&a.d==b.d;}
 R& operator+=(R b){return *this=*this+b;}
 R& operator-=(R b){return *this=*this-b;}
 R& operator*=(R b){return *this=*this*b;}
};
struct C {
 R r=0,i=0;
 C(long long a=0):r(a){}
 C(R a,R b=0):r(a),i(b){}
 friend C operator+(C a,C b){return C(a.r+b.r,a.i+b.i);}
 friend C operator-(C a){return C(-a.r,-a.i);}
 friend C operator-(C a,C b){return a+(-b);}
 friend C operator*(C a,C b){return C(a.r*b.r-a.i*b.i,a.r*b.i+a.i*b.r);}
 friend C operator/(C a,C b){R d=b.r*b.r+b.i*b.i;if(d==R(0))throw std::runtime_error("zero complex divisor");return C((a.r*b.r+a.i*b.i)/d,(a.i*b.r-a.r*b.i)/d);}
 friend bool operator==(C a,C b){return a.r==b.r&&a.i==b.i;}
 C&operator+=(C b){return *this=*this+b;}
};
using M=std::vector<std::vector<C>>;
M zero(int n,int m){return M(n,std::vector<C>(m));}
M eye(int n){M a=zero(n,n);for(int i=0;i<n;++i)a[i][i]=1;return a;}
M adj(const M&a){int n=a.size(),m=n?a[0].size():0;M b=zero(m,n);for(int i=0;i<n;++i)for(int j=0;j<m;++j)b[j][i]=C(a[i][j].r,-a[i][j].i);return b;}
M mul(const M&a,const M&b){int n=a.size(),p=n?a[0].size():0,m=b.size()?b[0].size():0;M c=zero(n,m);for(int i=0;i<n;++i)for(int k=0;k<p;++k)for(int j=0;j<m;++j)c[i][j]+=a[i][k]*b[k][j];return c;}
M add(M a,const M&b,int sign=1){for(unsigned i=0;i<a.size();++i)for(unsigned j=0;j<a[i].size();++j)a[i][j]+=C(sign)*b[i][j];return a;}
M block(const M&a,int r0,int r1,int c0,int c1){M b=zero(r1-r0,c1-c0);for(int i=r0;i<r1;++i)for(int j=c0;j<c1;++j)b[i-r0][j-c0]=a[i][j];return b;}
M inverse(M a){int n=a.size();M b=eye(n);for(int k=0;k<n;++k){int p=k;while(p<n&&a[p][k]==C(0))++p;if(p==n)throw std::runtime_error("singular exact inverse");std::swap(a[p],a[k]);std::swap(b[p],b[k]);C pivot=a[k][k];for(int j=0;j<n;++j){a[k][j]=a[k][j]/pivot;b[k][j]=b[k][j]/pivot;}for(int i=0;i<n;++i)if(i!=k){C v=a[i][k];for(int j=0;j<n;++j){a[i][j]=a[i][j]-v*a[k][j];b[i][j]=b[i][j]-v*b[k][j];}}}return b;}
R determinant(std::vector<std::vector<R>> a){int n=a.size();R d=1;for(int k=0;k<n;++k){int p=k;while(p<n&&a[p][k]==R(0))++p;if(p==n)return R(0);if(p!=k){std::swap(a[p],a[k]);d=-d;}R v=a[k][k];d*=v;for(int i=k+1;i<n;++i){R s=a[i][k]/v;for(int j=k+1;j<n;++j)a[i][j]-=s*a[k][j];}}return d;}
std::vector<R> coordinates(const M&h){int m=h.size();std::vector<R> v;for(int a=0;a<m;++a)v.push_back(h[a][a].r);for(int a=0;a<m;++a)for(int b=a+1;b<m;++b){v.push_back(h[a][b].r);v.push_back(h[a][b].i);}return v;}
void require(bool b,const char*s){if(!b)throw std::runtime_error(s);}

int main(){
 int cases=0,channels=0;
 for(int m=1;m<=5;++m)for(int extra: {0,2}){
  int n=m*m+extra,e=n-m;
  M l=zero(e,m);int row=0;
  for(int a=0;a<m;++a)for(int b=a+1;b<m;++b){l[row][a]=1;l[row][b]=1;++row;l[row][a]=1;l[row][b]=C(0,1);++row;}
  M k=zero(n,m);for(int i=0;i<e;++i)for(int j=0;j<m;++j)k[i][j]=l[i][j];for(int j=0;j<m;++j)k[e+j][j]=1;
  M t=mul(adj(k),k),p=mul(mul(k,inverse(t)),adj(k));
  M w=add(add(p,p),eye(n),-1);
  require(mul(adj(w),w)==eye(n),"reflection unitarity");
  require(mul(w,k)==k,"reflection fixes graph");
  M inv,ss;
  if(e){inv=inverse(add(eye(e),block(w,0,e,0,e),-1));require(mul(inv,block(w,0,e,e,n))==l,"recovered internal L");ss=add(block(w,e,n,e,n),mul(block(w,e,n,0,e),l));}
  else ss=w;
  require(ss==eye(m),"cavity is identity");
  std::vector<std::vector<R>> columns(n);
  for(int phase=0;phase<n;++phase){
   M dw=zero(n,n);for(int j=0;j<n;++j)dw[phase][j]=C(0,1)*w[phase][j];
   M ds;
   if(e){M dl=mul(inv,add(block(dw,0,e,e,n),mul(block(dw,0,e,0,e),l)));ds=add(add(block(dw,e,n,e,n),mul(block(dw,e,n,0,e),l)),mul(block(w,e,n,0,e),dl));}
   else ds=dw;
   M h=mul(adj(ss),ds);for(auto& rr:h)for(auto& z:rr)z=C(0,-1)*z;
   M brow=zero(1,m);for(int a=0;a<m;++a)brow[0][a]=k[phase][a];
   require(h==mul(adj(brow),brow),"exact phase logarithmic derivative");
   require(h==adj(h),"Hermitian derivative");
   columns[phase]=coordinates(h);++channels;
  }
  std::vector<int> selected;for(int a=0;a<m;++a)selected.push_back(e+a);for(int a=0;a<m*m-m;++a)selected.push_back(a);
  std::vector<std::vector<R>> j(m*m,std::vector<R>(m*m));for(int r=0;r<m*m;++r)for(int c=0;c<m*m;++c)j[r][c]=columns[selected[c]][r];
  R det=determinant(j);require(det==R(1),"phase minor determinant is one");
  std::cout<<"{\"m\":"<<m<<",\"N\":"<<n<<",\"rank\":"<<m*m<<",\"selected_minor\":1,\"exact\":true}\n";
  ++cases;
 }
 std::cout<<"{\"cases\":"<<cases<<",\"channels_checked\":"<<channels<<",\"arithmetic\":\"Gaussian rational, 128-bit overflow traps\",\"passed\":true}\n";
}
