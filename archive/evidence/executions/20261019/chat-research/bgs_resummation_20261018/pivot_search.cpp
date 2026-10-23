#include <algorithm>
#include <array>
#include <bit>
#include <iostream>
#include <numeric>
#include <vector>
constexpr int M=10;
using Matrix=std::array<std::array<int,M>,M>;
int rankmod(Matrix a, const std::vector<int>& ind, int p){
  int n=ind.size(),r=0;Matrix b{};
  for(int i=0;i<n;++i)for(int j=0;j<n;++j)b[i][j]=(a[ind[i]][ind[j]]%p+p)%p;
  for(int c=0;c<n;++c){int k=r;while(k<n&&!b[k][c])++k;if(k==n)continue;
    std::swap(b[k],b[r]);int inv=1;while(inv*b[r][c]%p!=1)++inv;
    for(int j=c;j<n;++j)b[r][j]=b[r][j]*inv%p;
    for(int i=r+1;i<n;++i){int f=b[i][c];for(int j=c;j<n;++j)b[i][j]=(b[i][j]-f*b[r][j]%p+p)%p;}++r;
  }return r;
}
void arrayout(const std::vector<int>& v){std::cout<<"[";for(unsigned i=0;i<v.size();++i){if(i)std::cout<<",";std::cout<<v[i];}std::cout<<"]";}
bool tau_basis(const Matrix& k,const std::vector<int>& tau,int rank,int p){
  if(!rank)return true;int n=tau.size();
  // A union of g disjoint edges of the directed tau cycle has rank vertices.
  // Deduplicate endpoint sets; a set may have multiple matching descriptions.
  std::vector<unsigned char> seen(1u<<n,0);
  for(unsigned mask=0;mask<(1u<<n);++mask){if(std::popcount(mask)!=rank/2)continue;
    unsigned vertices=0;bool disjoint=true;
    for(int i=0;i<n;++i)if(mask&(1u<<i)){unsigned edge=(1u<<i)|(1u<<tau[i]);if(vertices&edge){disjoint=false;break;}vertices|=edge;}
    if(!disjoint||seen[vertices])continue;seen[vertices]=1;
    std::vector<int> ind;for(int i=0;i<n;++i)if(vertices&(1u<<i))ind.push_back(i);
    if(rankmod(k,ind,p)==rank)return true;
  }return false;
}
int main(){
  long long total=0,fieldcases=0,pivotfails=0,edgefails=0;bool firstp=true,firste=true;
  std::cout<<"{\"counterexamples\":[";bool first=true;
  for(int n=3;n<=M;++n){std::vector<int> rest(n-1),all(n);std::iota(rest.begin(),rest.end(),1);std::iota(all.begin(),all.end(),0);long long visits=0;
    do{std::vector<int> tau(n);int last=0;for(int v:rest){tau[last]=v;last=v;}tau[last]=0;Matrix k{};int common=0;
      for(int i=0;i<n;++i){int j=(i+1)%n;++k[i][j];--k[j][i];j=tau[i];--k[i][j];++k[j][i];common+=tau[i]==(i+1)%n;}
      bool full=true;for(int i=0;i<n;++i){bool nz=false;for(int j=0;j<n;++j)nz|=k[i][j]!=0;full&=nz;}
      for(int p:{3,5,13}){++fieldcases;int r=rankmod(k,all,p);bool pivot=tau_basis(k,tau,r,p);bool edges=!full||common<=r;
        if(!pivot)++pivotfails;if(!edges)++edgefails;
        if((!pivot&&firstp)||(!edges&&firste)){
          if(!first)std::cout<<",";first=false;
          std::cout<<"{\"m\":"<<n<<",\"p\":"<<p<<",\"rank\":"<<r<<",\"common\":"<<common<<",\"full_support\":"<<(full?"true":"false")<<",\"tau_edge_basis\":"<<(pivot?"true":"false")<<",\"edge_bound\":"<<(edges?"true":"false")<<",\"tau\":";arrayout(tau);std::cout<<"}";
          if(!pivot)firstp=false;if(!edges)firste=false;
        }
      }++visits;
    }while(std::next_permutation(rest.begin(),rest.end()));total+=visits;std::cerr<<"m="<<n<<" cycles="<<visits<<"\n";
  }
  std::cout<<"],\"cycles\":"<<total<<",\"field_cases\":"<<fieldcases<<",\"tau_pivot_failures\":"<<pivotfails<<",\"common_edge_failures\":"<<edgefails<<"}\n";
}
