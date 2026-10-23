#define main prior_pivot_main
#include "pivot_search.cpp"
#undef main
#include <cassert>
struct Part{std::array<int,M> labels{};int blocks=0,codim=0,weight24=0;unsigned support=0;};
std::vector<Part> parts(int n){std::vector<Part> out;std::array<int,M> lab{};
  auto recur=[&](auto&& self,int i,int blocks)->void{
    if(i-blocks>3)return;
    if(i==n){std::array<int,M> sizes{};for(int j=0;j<n;++j)++sizes[lab[j]];int c=n-blocks,w=0;
      if(c==0)w=24;if(c==1)w=-12;
      if(c==2)w=std::find(sizes.begin(),sizes.end(),3)!=sizes.end()?16:6;
      if(c==3){if(std::find(sizes.begin(),sizes.end(),4)!=sizes.end())w=-33;
        else if(std::find(sizes.begin(),sizes.end(),3)!=sizes.end())w=-8;else w=-3;}
      unsigned support=0;for(int j=0;j<n;++j)if(sizes[lab[j]]>1)support|=1u<<j;
      out.push_back({lab,blocks,c,w,support});return;
    }
    for(int b=0;b<=blocks;++b){lab[i]=b;self(self,i+1,blocks+(b==blocks));}
  };recur(recur,0,0);return out;}
std::vector<int> rotate_tau(const std::vector<int>& t,int s){int n=t.size();std::vector<int> x(n);for(int i=0;i<n;++i)x[(i+s)%n]=(t[i]+s)%n;return x;}
int main(){long long coverage_total=0;
 for(int n=3;n<=10;++n){auto partitions=parts(n);std::vector<int> rest(n-1),all(n);std::iota(rest.begin(),rest.end(),1);std::iota(all.begin(),all.end(),0);
   std::array<std::array<long long,2>,3> hist{};long long coverage=0;
   do{std::vector<int> tau(n);int prev=0;for(int v:rest){tau[prev]=v;prev=v;}tau[prev]=0;
     auto best=tau;int stab=0;for(int s=0;s<n;++s){auto x=rotate_tau(tau,s);if(x<best)best=x;if(x==tau)++stab;}
     if(best!=tau)continue;long long orbit=n/stab;coverage+=orbit;
     Matrix k{};int common=0;for(int i=0;i<n;++i){int j=(i+1)%n;common+=tau[i]==j;++k[i][j];--k[j][i];j=tau[i];--k[i][j];++k[j][i];}
     if(common!=5&&common!=6)continue;
     unsigned active=0,full=(1u<<n)-1;for(int i=0;i<n;++i)for(int j=0;j<n;++j)if(k[i][j])active|=1u<<i;
     int field=0;for(int p:{3,5,13}){int r=rankmod(k,all,p);if(r>6){++field;continue;}
       for(const auto& part:partitions){if((active|part.support)!=full)continue;
         Matrix c{};for(int i=0;i<n;++i)for(int j=0;j<n;++j)c[part.labels[i]][part.labels[j]]+=k[i][j];
         std::vector<int> ind(part.blocks);std::iota(ind.begin(),ind.end(),0);
         if(part.codim+rankmod(c,ind,p)/2==3)hist[field][common-5]+=part.weight24*orbit;
       }++field;
     }
   }while(std::next_permutation(rest.begin(),rest.end()));coverage_total+=coverage;
   for(int f=0;f<3;++f)std::cout<<"{\"q\":"<<n<<",\"p\":"<<(f==0?3:f==1?5:13)<<",\"coverage\":"<<coverage<<",\"e5_weight24\":"<<hist[f][0]<<",\"e6_weight24\":"<<hist[f][1]<<"}\n";
   std::cerr<<"q="<<n<<" partitions="<<partitions.size()<<" cycles="<<coverage<<"\n";
 }std::cerr<<"total="<<coverage_total<<"\n";
}
