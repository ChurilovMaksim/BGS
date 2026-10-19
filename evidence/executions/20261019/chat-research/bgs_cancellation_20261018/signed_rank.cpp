#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <vector>
using Wide=__int128_t;
struct Partition {std::array<int,8> label{}; int blocks=0; Wide weight=0;};
long long factorial(int n){long long v=1;for(int i=1;i<=n;++i)v*=i;return v;}
std::string decimal(Wide n){if(n==0)return "0";bool neg=n<0;if(neg)n=-n;std::string s;while(n){s.push_back('0'+n%10);n/=10;}if(neg)s.push_back('-');std::reverse(s.begin(),s.end());return s;}
std::vector<Partition> partitions(int n,const std::vector<long long>& kappa){
 std::vector<Partition> out; std::array<int,8> labels{};
 auto recurse=[&](auto&& self,int at,int blocks)->void {
  if(at==n){std::array<int,8> size{};for(int j=0;j<n;++j)++size[labels[j]];
   Wide numerator=factorial(n),denominator=1;for(int j=0;j<blocks;++j){numerator*=kappa[size[j]];denominator*=factorial(size[j]);}
   assert(numerator%denominator==0);out.push_back({labels,blocks,numerator/denominator});return;}
  for(int b=0;b<=blocks;++b){labels[at]=b;self(self,at+1,std::max(blocks,b+1));}
 };
 labels[0]=0;recurse(recurse,1,1);return out;
}
int rank_mod(int a[8][8],int n,int p){
 int r=0;for(int c=0;c<n;++c){int pivot=r;while(pivot<n && (a[pivot][c]%p+p)%p==0)++pivot;if(pivot==n)continue;
  for(int j=c;j<n;++j)std::swap(a[pivot][j],a[r][j]);int v=(a[r][c]%p+p)%p,inv=1;while(v*inv%p!=1)++inv;
  for(int j=c;j<n;++j)a[r][j]=((a[r][j]%p+p)%p)*inv%p;
  for(int i=r+1;i<n;++i){int f=(a[i][c]%p+p)%p;if(f)for(int j=c;j<n;++j)a[i][j]=(a[i][j]-f*a[r][j])%p;}++r;
 }return r;
}
std::array<int,8> rotate(const std::array<int,8>& tau,int n,int shift){std::array<int,8> v{};for(int i=0;i<n;++i)v[(i+shift)%n]=(tau[i]+shift)%n;return v;}
int main(){
 int nfield;std::cin>>nfield;std::vector<std::pair<int,int>> requests(nfield);int maximum=0;
 for(auto& [p,m]:requests){std::cin>>p>>m;maximum=std::max(maximum,m);}assert(maximum<=8);
 std::vector<long long> kappa(maximum+1);for(int i=1;i<=maximum;++i)std::cin>>kappa[i];
 long long rank_calls=0;
 for(auto [p,maxm]:requests)for(int n=1;n<=maxm;++n){
  auto parts=partitions(n,kappa);std::vector<int> rest;for(int i=1;i<n;++i)rest.push_back(i);
  std::vector<Wide> coefficients(n+1);long long orbit_coverage=0,representatives=0;
  do {std::array<int,8> tau{};int prev=0;for(int v:rest){tau[prev]=v;prev=v;}tau[prev]=0;
   auto best=tau;int stabilizer=0;for(int s=0;s<n;++s){auto v=rotate(tau,n,s);if(v<best)best=v;if(v==tau)++stabilizer;}
   if(tau!=best)continue;int orbit=n/stabilizer;orbit_coverage+=orbit;++representatives;
   int k[8][8]{};for(int i=0;i<n;++i){int j=(i+1)%n;++k[i][j];--k[j][i];j=tau[i];--k[i][j];++k[j][i];}
   for(const auto& part:parts){int q[8][8]{};for(int i=0;i<n;++i)for(int j=0;j<n;++j)q[part.label[i]][part.label[j]]+=k[i][j];
    int rank=rank_mod(q,part.blocks,p);++rank_calls;assert(rank%2==0);int degree=n-part.blocks+rank/2;
    coefficients[degree]+=Wide(n)*orbit*part.weight;
   }
  }while(std::next_permutation(rest.begin(),rest.end()));
  assert(orbit_coverage==factorial(n-1));std::cout<<"{\"p\":"<<p<<",\"m\":"<<n<<",\"partitions\":"<<parts.size()<<",\"cycle_orbits\":"<<representatives<<",\"cycle_coverage\":"<<orbit_coverage<<",\"scale\":"<<factorial(n)<<",\"scaled_coefficients\":[";
  for(int j=0;j<=n;++j){if(j)std::cout<<",";std::cout<<"\""<<decimal(coefficients[j])<<"\"";}std::cout<<"]}\n";
 }
 std::cerr<<"rank_calls="<<rank_calls<<"\n";
}
