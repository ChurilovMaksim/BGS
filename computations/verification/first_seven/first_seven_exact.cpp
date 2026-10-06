#include <array>
#include <vector>
#include <iostream>
#include <fstream>
#include <stdexcept>
#include <algorithm>
#include <chrono>
using namespace std;
using P=vector<int>;using Mat=vector<P>;
void req(bool b,const string&s){if(!b)throw runtime_error(s);}
int ad[125][125],ng[15625],ex[31248],lg[15625];
int add(int a,int b){return ad[a%125][b%125]+125*ad[a/125][b/125];}
int sub(int a,int b){return add(a,ng[b]);}
int mul(int a,int b){return a&&b?ex[lg[a]+lg[b]]:0;}
int inv(int a){req(a!=0,"zero inverse");return ex[15624-lg[a]];}
int pw(int a,long long e){if(!a){req(e>0,"bad zero power");return 0;} e%=15624;if(e<0)e+=15624;return ex[(lg[a]*e)%15624];}
int direct(int a,int b){array<int,11>c{};int aa=a;for(int i=0;i<6;i++){int ai=aa%5;aa/=5;int bb=b;for(int j=0;j<6;j++){c[i+j]+=ai*(bb%5);bb/=5;}}
 int f[]={1,0,1,3,1,0,1};for(int k=10;k>=6;k--){int v=(c[k]%5+5)%5;for(int j=0;j<=6;j++)c[k-6+j]-=v*f[j];}
 int out=0;for(int i=5;i>=0;i--)out=5*out+(c[i]%5+5)%5;return out;}
void field(){for(int a=0;a<125;a++)for(int b=0;b<125;b++){int aa=a,bb=b,z=0,wt=1;for(int i=0;i<3;i++){z+=wt*((aa%5+bb%5)%5);wt*=5;aa/=5;bb/=5;}ad[a][b]=z;}
 for(int a=0;a<15625;a++){int aa=a,z=0,wt=1;for(int i=0;i<6;i++){z+=wt*((5-aa%5)%5);aa/=5;wt*=5;}ng[a]=z;lg[a]=-1;}
 int x=1;for(int i=0;i<15624;i++){req(lg[x]==-1,"generator early repeat");lg[x]=i;ex[i]=ex[i+15624]=x;x=direct(x,9);}req(x==1,"generator closure");for(int a=1;a<15625;a++)req(lg[a]>=0,"nonzero field element omitted");
 for(int a=0;a<15625;a++)for(int b: {0,1,2,3,4,5,9,125,2697,15624})req(mul(a,b)==direct(a,b),"multiplication dictionary");
 req(pw(5,63)==1&&pw(5,21)!=1&&pw(5,9)!=1,"root63");int w=pw(5,9);req(pw(w,7)==1&&w!=1,"root7");cout<<"FIELD PASS: full multiplicative orbit, 156250 direct-product controls; t order63,w="<<w<<endl;}
Mat mm(const Mat&a,const Mat&b){Mat c(a.size(),P(b[0].size()));for(int i=0;i<(int)a.size();i++)for(int k=0;k<(int)b.size();k++)for(int j=0;j<(int)b[0].size();j++)c[i][j]=add(c[i][j],mul(a[i][k],b[k][j]));return c;}
Mat mi(Mat a){int n=a.size();Mat out(n,P(n));for(int i=0;i<n;i++)out[i][i]=1;for(int k=0;k<n;k++){int r=k;while(r<n&&!a[r][k])r++;req(r<n,"singular inverse");swap(a[r],a[k]);swap(out[r],out[k]);int c=inv(a[k][k]);for(int j=0;j<n;j++){a[k][j]=mul(a[k][j],c);out[k][j]=mul(out[k][j],c);}for(int i=0;i<n;i++)if(i!=k){int v=a[i][k];for(int j=0;j<n;j++){a[i][j]=sub(a[i][j],mul(v,a[k][j]));out[i][j]=sub(out[i][j],mul(v,out[k][j]));}}}return out;}
int det(Mat a){int n=a.size(),d=1;for(int k=0;k<n;k++){int r=k;while(r<n&&!a[r][k])r++;if(r==n)return 0;if(r!=k){swap(a[r],a[k]);d=ng[d];}int v=a[k][k];d=mul(d,v);int vi=inv(v);for(int i=k+1;i<n;i++)if(a[i][k]){int c=mul(a[i][k],vi);for(int j=k+1;j<n;j++)a[i][j]=sub(a[i][j],mul(c,a[k][j]));a[i][k]=0;}}return d;}
P trim(P a){while(a.size()>1&&!a.back())a.pop_back();return a;}
P pa(P a,const P&b){a.resize(max(a.size(),b.size()));for(int j=0;j<(int)b.size();j++)a[j]=add(a[j],b[j]);return trim(a);}
P ps(P a,const P&b){a.resize(max(a.size(),b.size()));for(int j=0;j<(int)b.size();j++)a[j]=sub(a[j],b[j]);return trim(a);}
P pm(const P&a,const P&b){P c(a.size()+b.size()-1);for(int i=0;i<(int)a.size();i++)if(a[i])for(int j=0;j<(int)b.size();j++)if(b[j])c[i+j]=add(c[i+j],mul(a[i],b[j]));return trim(c);}
pair<P,P>pd(P a,const P&b){req(b!=P{0},"poly zero denominator");P q(max(1,(int)a.size()-(int)b.size()+1));int v=inv(b.back());for(int k=(int)a.size()-(int)b.size();k>=0;k--){q[k]=mul(a[k+b.size()-1],v);for(int j=0;j<(int)b.size();j++)a[k+j]=sub(a[k+j],mul(q[k],b[j]));}return {trim(q),trim(a)};}
P pg(P a,P b){while(b!=P{0}){P c=pd(a,b).second;a=b;b=c;}int c=inv(a.back());for(int&v:a)v=mul(c,v);return a;}
P pp(P a,const P&n,const P&m){P b{1};a=pd(a,m).second;for(int j=0;j<(int)n.size();j++){if(n[j])b=pd(pm(a,b),m).second;if(j+1<(int)n.size())a=pd(pm(a,a),m).second;}return b;}
int eval(const P&a,int q){int v=0;for(auto it=a.rbegin();it!=a.rend();++it)v=add(mul(v,q),*it);return v;}
P readp(istream&in){int n=0;req(bool(in>>n),"missing vector length");req(n>=1&&n<100000,"bad vector");P a(n);for(int&v:a){in>>v;req(v>=0&&v<15625,"bad field code");}req(bool(in),"short input");return a;}
struct System{int w,l;Mat A,Ai;System(int ell):l(ell){w=pw(5,9);A=Mat(7,P(7));for(int j=0;j<7;j++)for(int k=0;k<7;k++){int e=-3*l*(j*j+k*k)+2*l*j*k+(l+4)*j+(2*l+3)*k;A[j][k]=pw(w,e);}Ai=mi(A);req(mm(A,Ai)==identity(),"Fourier inverse");}
Mat identity(){Mat a(7,P(7));for(int i=0;i<7;i++)a[i][i]=1;return a;}
Mat system(int q){P sc(7),sq(7),U(7),Ui(7);for(int j=0;j<7;j++){int z=pw(w,j),t1=ng[mul(w,z)],t2=ng[mul(q,z)],c=0,s=0,p1=1,p2=1;for(int k=0;k<=6;k++){int qp=k==6?1:pw(q,6-k);c=add(c,mul(p1,qp));s=add(s,p2);p1=mul(p1,t1);p2=mul(p2,t2);}sc[j]=mul(c,c);sq[j]=mul(s,s);U[j]=pw(w,2*j);Ui[j]=inv(U[j]);}
Mat da=A,ua=A;for(int j=0;j<7;j++)for(int k=0;k<7;k++){da[j][k]=mul(sc[j],da[j][k]);ua[j][k]=mul(U[j],ua[j][k]);}Mat J=mm(Ai,da),K=mm(Ai,ua);for(int j=0;j<7;j++)for(int k=0;k<7;k++){J[j][k]=mul(J[j][k],Ui[k]);K[j][k]=mul(K[j][k],mul(U[k],sq[k]));}Mat H=mm(J,K),JA=mm(J,Ai),AJ=mm(A,J),M(63,P(48));
for(int u=0;u<7;u++)for(int v=0;v<7;v++){int col=7*u+v-1;if(col<0)continue;for(int i=0;i<7;i++){M[i][col]=sub(i==u&&i==v?1:0,mul(A[i][u],Ai[v][i]));int c=sub(i==u?K[v][i]:0,i==v?K[i][u]:0);int e=sub(mul(A[i][u],JA[v][i]),mul(AJ[i][u],Ai[v][i]));M[7+i][col]=add(mul(pw(w,2),c),e);for(int j=0;j<7;j++)M[14+7*i+j][col]=sub(i==u?H[v][j]:0,j==v?H[i][u]:0);}}return M;}
};
int main(int argc,char**argv){try{req(argc==2,"usage: review input_file");field();ifstream in(argv[1]);int cases=0;req(bool(in>>cases)&&cases==6,"six classes required");for(int cc=0;cc<cases;cc++){int l=0,n=0;req(bool(in>>l>>n),"missing class header");req(l==cc+1&&n==937,"class/nodes");P nodes=readp(in);req(nodes.size()==937,"node count");P sorted=nodes;sort(sorted.begin(),sorted.end());req(unique(sorted.begin(),sorted.end())==sorted.end(),"duplicate nodes");vector<P> rows(3),vals(3),polys(3);for(int k=0;k<3;k++){rows[k]=readp(in);vals[k]=readp(in);polys[k]=readp(in);req(rows[k].size()==48&&vals[k].size()==937,"row/value count");P rr=rows[k];sort(rr.begin(),rr.end());req(unique(rr.begin(),rr.end())==rr.end()&&rr.back()<63,"row set");int d=0,n0=0,n1=0,n2=0;for(int r:rr){d+=r<7?0:r<14?12:24;if(r<7)n0++;else if(r<14)n1++;else n2++;}req(d==936&&n0==6&&n1==6&&n2==36&&polys[k].size()<=937,"degree contract");}
System S(l);for(int i=0;i<n+10;i++){int q=i<n?nodes[i]:12000+i-n;Mat M=S.system(q);for(int k=0;k<3;k++){Mat a;for(int r:rows[k])a.push_back(M[r]);int d=det(a);req(d==eval(polys[k],q),"determinant vs polynomial at l="+to_string(l)+" node="+to_string(q));if(i<n)req(d==vals[k][i],"determinant vs recorded value");}}cout<<"CLASS "<<l<<" 2841 independent determinant evaluations PASS"<<endl;
P g=readp(in);req(pg(pg(polys[0],polys[1]),polys[2])==g,"gcd exact");P total{0};for(int k=0;k<3;k++){P b=readp(in);total=pa(total,pm(b,polys[k]));}req(total==g,"three minor Bezout");for(int k=0;k<3;k++){P q=readp(in);req(pm(g,q)==polys[k],"gcd quotient");}
int nf=0;req(bool(in>>nf)&&nf>=0&&nf<=8,"excluded-factor count");vector<pair<int,int>>factors;for(int j=0;j<nf;j++){int r=0,m=0;req(bool(in>>r>>m)&&r>=0&&r<15625&&m>0&&m<=936,"excluded-factor input");req(r==0||pw(r,7)==4,"excluded root order");req(m>0,"multiplicity");factors.push_back({r,m});}
P rem=readp(in);P recon=rem;for(auto [r,m]:factors)for(int j=0;j<m;j++)recon=pm(recon,P{ng[r],1});req(recon==g,"gcd reconstruction");P product{1};vector<P> component_polys;int components=0;req(bool(in>>components),"missing components");req(components==2,"components");for(int k=0;k<components;k++){int d=0;req(bool(in>>d),"missing component degree");P b=readp(in),oddrecord=readp(in),u=readp(in),v=readp(in);req(d==(k==0?3:17)&&b.size()==(k==0?7:35),"component degree");product=pm(product,b);component_polys.push_back(b);P power{1};for(int j=0;j<6*d;j++){int c=0;for(int&bit:power){c+=5*bit;bit=c%2;c/=2;}while(c){power.push_back(c%2);c/=2;}}req(pd(ps(pp(P{0,1},power,b),P{0,1}),b).second==P{0},"Frobenius containment");P order=power;int pos=0;while(order[pos]==0){order[pos]=1;pos++;}order[pos]=0;int twos=0;while(order[0]==0){order.erase(order.begin());twos++;}req(twos==3,"two valuation");P odd=ps(pp(P{0,1},order,b),P{1});req(odd==oddrecord,"odd power recorded remainder");req(pg(b,odd)==P{1},"odd gcd");req(pa(pm(u,b),pm(v,odd))==P{1},"odd Bezout");}req(product==rem,"component reconstruction");req(pg(component_polys[0],component_polys[1])==P{1},"coprime components");cout<<"CLASS "<<l<<" exact gcd, Bezout, quotients, factor reconstruction, Frobenius and odd-order exclusions PASS"<<endl;
}in>>ws;req(in.eof(),"trailing certificate data");cout<<"ALL INDEPENDENT CHECKS PASS"<<endl;return 0;}catch(exception&e){cerr<<"FAIL "<<e.what()<<endl;return 1;}}
