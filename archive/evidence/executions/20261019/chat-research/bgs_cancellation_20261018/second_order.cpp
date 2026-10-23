#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <numeric>
#include <vector>
constexpr int M=12;
using Perm=std::array<int,M>;
struct Collision {Perm labels{};int blocks=0;int weight12=0;};
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
 auto add=[&](const Perm& input,int weight){Perm map{},canonical{};map.fill(-1);int b=0;
  for(int i=0;i<n;++i){int v=input[i];if(map[v]<0)map[v]=b++;canonical[i]=map[v];}
  assert(b==n-codim);out.push_back({canonical,b,weight});};
 std::iota(labels.begin(),labels.end(),0);
 if(codim==1){for(int a=0;a<n;++a)for(int b=a+1;b<n;++b){auto x=labels;x[b]=a;add(x,-6);}}
 if(codim==2){
  for(int a=0;a<n;++a)for(int b=a+1;b<n;++b)for(int c=b+1;c<n;++c){auto x=labels;x[b]=x[c]=a;add(x,8);}
  for(int a=0;a<n;++a)for(int b=a+1;b<n;++b)for(int c=b+1;c<n;++c)for(int d=c+1;d<n;++d){
   auto x=labels;x[b]=a;x[d]=c;add(x,3);x=labels;x[c]=a;x[d]=b;add(x,3);x=labels;x[d]=a;x[c]=b;add(x,3);}
 }
 return out;
}
int main(){
 int requests;std::cin>>requests;
 while(requests--){int p,n;std::cin>>p>>n;assert(3<=n&&n<=M);
  auto one=collisions(n,1),two=collisions(n,2);std::vector<int> rest(n-1);std::iota(rest.begin(),rest.end(),1);
  long long coverage=0,reps=0,n0=0,n2=0,n4=0,pair_zero=0,pair_two=0,triple_zero=0,double_zero=0;
  do{Perm tau{};int prev=0;for(int v:rest){tau[prev]=v;prev=v;}tau[prev]=0;
   auto best=tau;int stabilizer=0;for(int s=0;s<n;++s){auto v=rotated(tau,n,s);if(v<best)best=v;if(v==tau)++stabilizer;}
   if(best!=tau)continue;long long orbit=n/stabilizer;coverage+=orbit;++reps;
   int k[M][M]{},a[M][M]{};for(int i=0;i<n;++i){int j=(i+1)%n;++k[i][j];--k[j][i];j=tau[i];--k[i][j];++k[j][i];}
   for(int i=0;i<n;++i)for(int j=0;j<n;++j)a[i][j]=k[i][j];int r=rank_mod(a,n,p);assert(r%2==0);if(r>4)continue;
   if(r==0)n0+=orbit;if(r==2)n2+=orbit;if(r==4)n4+=orbit;
   for(auto& part:one){int b[M][M]{};for(int i=0;i<n;++i)for(int j=0;j<n;++j)b[part.labels[i]][part.labels[j]]+=k[i][j];
    int s=rank_mod(b,part.blocks,p);assert(s%2==0);if(s==0)pair_zero+=orbit;if(s==2)pair_two+=orbit;
   }
   for(auto& part:two){int b[M][M]{};for(int i=0;i<n;++i)for(int j=0;j<n;++j)b[part.labels[i]][part.labels[j]]+=k[i][j];
    bool zero=true;for(int i=0;i<part.blocks;++i)for(int j=i+1;j<part.blocks;++j)if(b[i][j]%p)zero=false;
    if(zero){if(part.weight12==8)triple_zero+=orbit;else double_zero+=orbit;}
   }
  }while(std::next_permutation(rest.begin(),rest.end()));
  assert(coverage==factorial(n-1)&&n0==1);
  long long first12=12*n2-6*pair_zero,second12=12*n4-6*pair_two+8*triple_zero+3*double_zero;
  std::cout<<"{\"p\":"<<p<<",\"m\":"<<n<<",\"coverage\":"<<coverage<<",\"cycle_orbits\":"<<reps
   <<",\"n2\":"<<n2<<",\"n4\":"<<n4<<",\"pair_zero\":"<<pair_zero<<",\"pair_two\":"<<pair_two
   <<",\"triple_zero\":"<<triple_zero<<",\"double_pair_zero\":"<<double_zero<<",\"first12\":"<<first12<<",\"second12\":"<<second12<<"}\n";
 }
 std::cerr<<"rank_calls="<<calls<<"\n";
}
