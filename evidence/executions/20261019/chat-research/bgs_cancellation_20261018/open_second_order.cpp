#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <numeric>
#include <vector>
constexpr int M=12;
using Perm=std::array<int,M>;
struct Collision {Perm labels{};int blocks=0,weight12=0;unsigned support=0;};
long long factorial(int n){long long v=1;for(int j=2;j<=n;++j)v*=j;return v;}
long long calls=0;
int rank_mod(int a[M][M],int n,int p){
 ++calls;int r=0;for(int c=0;c<n;++c){int v=r;while(v<n&&(a[v][c]%p+p)%p==0)++v;if(v==n)continue;
  for(int j=c;j<n;++j)std::swap(a[v][j],a[r][j]);int x=(a[r][c]%p+p)%p,inv=1;while(x*inv%p!=1)++inv;
  for(int j=c;j<n;++j)a[r][j]=(a[r][j]%p+p)%p*inv%p;
  for(int i=r+1;i<n;++i){int f=(a[i][c]%p+p)%p;if(f)for(int j=c;j<n;++j)a[i][j]=(a[i][j]-f*a[r][j])%p;}++r;
 }return r;
}
Perm rotated(const Perm& tau,int n,int s){Perm v{};for(int i=0;i<n;++i)v[(i+s)%n]=(tau[i]+s)%n;return v;}
std::vector<Collision> collisions(int n,int codim){
 std::vector<Collision> out;Perm labels{};
 auto add=[&](const Perm& input,int weight,unsigned support){Perm map{},canonical{};map.fill(-1);int b=0;
  for(int i=0;i<n;++i){int v=input[i];if(map[v]<0)map[v]=b++;canonical[i]=map[v];}
  assert(b==n-codim);out.push_back({canonical,b,weight,support});};
 std::iota(labels.begin(),labels.end(),0);
 if(codim==1)for(int a=0;a<n;++a)for(int b=a+1;b<n;++b){auto x=labels;x[b]=a;add(x,-6,(1u<<a)|(1u<<b));}
 if(codim==2){
  for(int a=0;a<n;++a)for(int b=a+1;b<n;++b)for(int c=b+1;c<n;++c){auto x=labels;x[b]=x[c]=a;add(x,8,(1u<<a)|(1u<<b)|(1u<<c));}
  for(int a=0;a<n;++a)for(int b=a+1;b<n;++b)for(int c=b+1;c<n;++c)for(int d=c+1;d<n;++d){
   unsigned s=(1u<<a)|(1u<<b)|(1u<<c)|(1u<<d);
   auto x=labels;x[b]=a;x[d]=c;add(x,3,s);x=labels;x[c]=a;x[d]=b;add(x,3,s);x=labels;x[d]=a;x[c]=b;add(x,3,s);}
 }
 return out;
}
int main(){int p;std::cin>>p;assert(p>=3);
 for(int n=3;n<=12;++n){
  auto one=collisions(n,1),two=collisions(n,2);std::vector<int> rest(n-1);std::iota(rest.begin(),rest.end(),1);
  std::array<long long,M+1> histogram{};long long coverage=0,reps=0;
  do{Perm tau{};int prev=0;for(int v:rest){tau[prev]=v;prev=v;}tau[prev]=0;
   auto best=tau;int stabilizer=0;for(int s=0;s<n;++s){auto v=rotated(tau,n,s);if(v<best)best=v;if(v==tau)++stabilizer;}
   if(best!=tau)continue;long long orbit=n/stabilizer;coverage+=orbit;++reps;
   int k[M][M]{},a[M][M]{},common=0;for(int i=0;i<n;++i){int j=(i+1)%n;if(tau[i]==j)++common;++k[i][j];--k[j][i];j=tau[i];--k[i][j];++k[j][i];}
   unsigned active=0,full=(1u<<n)-1;
   for(int i=0;i<n;++i)for(int j=0;j<n;++j){a[i][j]=k[i][j];if(k[i][j]%p)active|=(1u<<i);}
   int r=rank_mod(a,n,p);assert(r%2==0);if(r>4)continue;
   if(r==4&&active==full)histogram[common]+=12*orbit;
   for(const auto& part:one){if((active|part.support)!=full)continue;
    int b[M][M]{};for(int i=0;i<n;++i)for(int j=0;j<n;++j)b[part.labels[i]][part.labels[j]]+=k[i][j];
    int s=rank_mod(b,part.blocks,p);if(s==2)histogram[common]+=-6*orbit;
   }
   for(const auto& part:two){if((active|part.support)!=full)continue;
    int b[M][M]{};for(int i=0;i<n;++i)for(int j=0;j<n;++j)b[part.labels[i]][part.labels[j]]+=k[i][j];
    bool zero=true;for(int i=0;i<part.blocks;++i)for(int j=i+1;j<part.blocks;++j)if(b[i][j]%p)zero=false;
    if(zero)histogram[common]+=part.weight12*orbit;
   }
  }while(std::next_permutation(rest.begin(),rest.end()));
  assert(coverage==factorial(n-1));std::cout<<"{\"p\":"<<p<<",\"q\":"<<n<<",\"coverage\":"<<coverage<<",\"cycle_orbits\":"<<reps<<",\"histogram12\":[";
  for(int j=0;j<=n;++j){if(j)std::cout<<",";std::cout<<histogram[j];}std::cout<<"]}\n";
 }
 std::cerr<<"rank_calls="<<calls<<"\n";
}
