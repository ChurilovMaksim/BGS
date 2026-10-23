#include <complex>
#include <map>
#include <vector>
#include <iostream>
#include <stdexcept>

using I=__int128_t;
I gcd(I a,I b){if(a<0)a=-a;if(b<0)b=-b;while(b){I c=a%b;a=b;b=c;}return a;}
I times(I a,I b){I c;if(__builtin_mul_overflow(a,b,&c))throw std::overflow_error("exact rational multiplication");return c;}
I plus(I a,I b){I c;if(__builtin_add_overflow(a,b,&c))throw std::overflow_error("exact rational addition");return c;}
struct R {
 I n=0,d=1;R(long long x=0):n(x){} R(I a,I b):n(a),d(b){if(!d)throw std::runtime_error("zero denominator");if(d<0){n=-n;d=-d;}I g=gcd(n,d);n/=g;d/=g;}
 friend R operator+(R a,R b){I g=gcd(a.d,b.d);return R(plus(times(a.n,b.d/g),times(b.n,a.d/g)),times(a.d,b.d/g));}
 friend R operator-(R a){return R(-a.n,a.d);} friend R operator-(R a,R b){return a+(-b);}
 friend R operator*(R a,R b){I g=gcd(a.n,b.d),h=gcd(b.n,a.d);return R(times(a.n/g,b.n/h),times(a.d/h,b.d/g));}
 friend R operator/(R a,R b){return a*R(b.d,b.n);}
 R& operator+=(R b){return *this=*this+b;} R& operator-=(R b){return *this=*this-b;}
 R& operator*=(R b){return *this=*this*b;} R& operator/=(R b){return *this=*this/b;}
 friend bool operator==(R a,R b){return a.n==b.n&&a.d==b.d;}friend bool operator!=(R a,R b){return !(a==b);}
 friend bool operator<(R a,R b){return times(a.n,b.d)<times(b.n,a.d);}friend bool operator<=(R a,R b){return a<b||a==b;}
 friend bool operator>(R a,R b){return b<a;}friend bool operator>=(R a,R b){return b<=a;}
};
using C=std::complex<R>;
using M=std::vector<std::vector<C>>;
using P=std::map<std::pair<int,int>,C>;
using PM=std::vector<std::vector<P>>;
M zero(int n){return M(n,std::vector<C>(n));}
M eye(int n){auto a=zero(n);for(int i=0;i<n;++i)a[i][i]=C(1);return a;}
M adj(const M&a){int n=a.size();auto b=zero(n);for(int i=0;i<n;++i)for(int j=0;j<n;++j)b[j][i]=std::conj(a[i][j]);return b;}
M mul(const M&a,const M&b){int n=a.size();auto c=zero(n);for(int i=0;i<n;++i)for(int k=0;k<n;++k)for(int j=0;j<n;++j)c[i][j]+=a[i][k]*b[k][j];return c;}
C tr(const M&a){C s(0);for(unsigned i=0;i<a.size();++i)s+=a[i][i];return s;}
P pmul(const P&a,const P&b){P c;for(auto &[i,x]:a)for(auto &[j,y]:b)c[{i.first+j.first,i.second+j.second}]+=x*y;return c;}
PM mmul(const PM&a,const PM&b){int n=a.size();PM c(n,std::vector<P>(n));for(int i=0;i<n;++i)for(int k=0;k<n;++k)for(int j=0;j<n;++j)for(auto &[ij,x]:pmul(a[i][k],b[k][j]))c[i][j][ij]+=x;return c;}
C avgtrace(const PM&a,C aa){R d=1-std::norm(aa);C out(0);for(unsigned i=0;i<a.size();++i)for(auto &[pq,x]:a[i][i]){auto [p,q]=pq;C moment(0);if(p==0&&q==0)moment=1;else if(p==1&&q==1)moment=C(1/d);else if(p==2&&q==1)moment=std::conj(aa)/C(d*d);else if(p==1&&q==2)moment=aa/C(d*d);else if(p&&q)throw std::runtime_error("unexpected degree");out+=x*moment;}return out;}
int main(){int cases=0;for(int n=2;n<=6;++n)for(int seed=0;seed<8;++seed){
 auto s=eye(n);
 for(int k=0;k<2+seed%2;++k){int i=k%n,j=(i+1+k/(2*n))%n;if(i==j)j=(j+1)%n;C phase=(k+seed)%2?C(0,1):C(1);auto g=eye(n);g[i][i]=g[j][j]=C(R(3)/5);g[i][j]=C(R(4)/5)*phase;g[j][i]=-C(R(4)/5)*std::conj(phase);s=mul(g,s);}
 for(int i=0;i<n;++i)for(int j=0;j<n;++j)if((i+seed)%3==0)s[i][j]*=C(0,1);
 if(mul(s,adj(s))!=eye(n))throw std::runtime_error("nonunitary input");
 auto l=zero(n);for(int i=0;i<n;++i)for(int j=0;j<n;++j)l[i][j]=C(R((3*i+2*j+seed)%7-3),R((i+4*j+seed)%5-2));
 auto t=mul(adj(l),l);for(int i=0;i<n;++i)t[i][i]+=C(1);
 auto q=mul(mul(s,t),adj(s)),t2=mul(t,t),q2=mul(q,q),t3=mul(t2,t);
 C aa=s[0][0],tt=t[0][0],ss=q[0][0];R d=1-std::norm(aa);if(d<=0)throw std::runtime_error("degenerate feedback");
 PM tw(n,std::vector<P>(n));
 // TW=T+q T e v*+conj(q) T v e*, with v=S*e.
 auto ts=mul(t,adj(s));
 for(int i=0;i<n;++i)for(int j=0;j<n;++j){tw[i][j][{0,0}]=t[i][j];tw[i][j][{1,0}]=t[i][0]*s[0][j];if(j==0)tw[i][j][{0,1}]=ts[i][0];}
 auto tw2=mmul(tw,tw),tw3=mmul(tw2,tw);
 C e2=tr(t2)+C(2)*tt*ss/C(d);
 C gamma=mul(s,t)[0][0];
 C e3=tr(t3)+C(3)*(tt*q2[0][0]+ss*t2[0][0])/C(d)+C(6)*tt*ss*C((std::conj(aa)*gamma).real())/C(d*d);
 if(avgtrace(tw,aa)!=tr(t)||avgtrace(tw2,aa)!=e2||avgtrace(tw3,aa)!=e3)throw std::runtime_error("exact identity failure");
 ++cases;
 }std::cout<<"{\"exact_noncommuting_cases\":"<<cases<<",\"moments_checked\":3,\"arithmetic\":\"Gaussian rational\",\"passed\":true}\n";
}
