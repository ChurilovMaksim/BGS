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
PM constant(const M&a){int n=a.size();PM b(n,std::vector<P>(n));for(int i=0;i<n;++i)for(int j=0;j<n;++j)b[i][j][{0,0}]=a[i][j];return b;}
PM padj(const PM&a){int n=a.size();PM b(n,std::vector<P>(n));for(int i=0;i<n;++i)for(int j=0;j<n;++j)for(auto&[pq,x]:a[i][j])b[j][i][{pq.second,pq.first}]=std::conj(x);return b;}
M mean(const PM&a){int n=a.size();M b=zero(n);for(int i=0;i<n;++i)for(int j=0;j<n;++j)for(auto&[pq,x]:a[i][j])if(pq.first==pq.second)b[i][j]+=x;return b;}
int main(){int cases=0;for(int n=2;n<=5;++n)for(int seed=0;seed<4;++seed){
 auto left=eye(n),right=eye(n),sw=eye(n);sw[0][0]=sw[1][1]=C(0);sw[0][1]=sw[1][0]=C(1);
 if(n>=3){left[1][1]=left[2][2]=C(R(3)/5);left[1][2]=C(0,R(4)/5);left[2][1]=C(0,R(4)/5);
 right[1][1]=right[2][2]=C(R(3)/5);right[1][2]=C(R(4)/5);right[2][1]=-C(R(4)/5);}
 auto s=mul(mul(left,sw),right);for(int i=0;i<n;++i)for(int j=0;j<n;++j)if((i+seed)%3==0)s[i][j]*=C(0,1);
 if(mul(s,adj(s))!=eye(n)||s[0][0]!=C(0))throw std::runtime_error("bad zero-diagonal unitary");
 auto l=zero(n);for(int i=0;i<n;++i)for(int j=0;j<n;++j)l[i][j]=C(R((i+2*j+seed)%5-2),R((2*i+j+seed)%3-1));
 auto t=mul(adj(l),l);for(int i=0;i<n;++i)t[i][i]+=C(1);
 auto q=mul(mul(s,t),adj(s)),t2=mul(t,t),q2=mul(q,q),t3=mul(t2,t),q3=mul(q2,q),t4=mul(t3,t),gamma=mul(s,t);
 PM kp(n,std::vector<P>(n)),sp(n,std::vector<P>(n));
 for(int j=1;j<n;++j){kp[j][j][{0,0}]=C(1);kp[0][j][{1,0}]=s[0][j];}
 for(int i=1;i<n;++i)for(int j=1;j<n;++j){sp[i][j][{0,0}]=s[i][j];sp[i][j][{1,0}]=s[i][0]*s[0][j];}
 auto tp=mmul(mmul(padj(kp),constant(t)),kp),tp2=mmul(tp,tp),tp3=mmul(tp2,tp),tp4=mmul(tp3,tp);
 auto mix=mean(mmul(sp,tp));for(int i=1;i<n;++i)for(int j=1;j<n;++j)if(mix[i][j]!=gamma[i][j])throw std::runtime_error("compressed mixed martingale failed");
 auto av2=mean(tp2);for(int j=1;j<n;++j){C expected=t2[j][j]+C(std::norm(s[0][j]))*t2[0][0]+C(2)*t[0][0]*C((std::conj(s[0][j])*gamma[0][j]).real());if(av2[j][j]!=expected)throw std::runtime_error("diagonal square identity failed");}
 C tt=t[0][0],ss=q[0][0];
 C expected4=tr(t4)+C(4)*(tt*q3[0][0]+t2[0][0]*q2[0][0]+ss*t3[0][0])+C(2)*tt*tt*ss*ss+C(4)*tt*ss*C(std::norm(gamma[0][0]));
 if(tr(mean(tp4))!=expected4){throw std::runtime_error("quartic identity failed");}
 ++cases;
 }std::cout<<"{\"exact_cases\":"<<cases<<",\"checked\":[\"mixed_clock_martingale\",\"diagonal_square\",\"quartic_zero_diagonal\"],\"passed\":true}\n";}
