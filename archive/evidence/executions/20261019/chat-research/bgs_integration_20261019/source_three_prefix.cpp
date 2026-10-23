#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <numeric>
#include <vector>
constexpr int M=11;
struct Part{std::array<int,M> labels{};std::vector<std::pair<int,int>> merges;int blocks=0,c=0,weight24=0;unsigned support=0;};
int weight(const std::vector<int>& sizes){int a=0,b=0,c=0;for(int n:sizes){a+=n==2;b+=n==3;c+=n==4;assert(n<=4);}
  if(c)return -33;if(b)return a?-8:16;return a==0?24:a==1?-12:a==2?6:-3;}
std::vector<Part> partitions(int n){
  std::vector<Part> out;std::array<int,M> labels{};
  auto grow=[&](auto&& self,int pos,int maximum,int codim)->void{
    if(pos==n){Part p;p.labels=labels;p.blocks=maximum+1;p.c=codim;std::vector<int> sizes(p.blocks),first(p.blocks,-1);
      for(int i=0;i<n;++i){int b=labels[i];++sizes[b];if(first[b]<0)first[b]=i;else p.merges.emplace_back(first[b],i);}
      for(int i=0;i<n;++i)if(sizes[labels[i]]>1)p.support|=1u<<i;p.weight24=weight(sizes);out.push_back(p);return;}
    for(int v=0;v<=maximum+1;++v){int next=codim+(v<=maximum);if(next>3)continue;labels[pos]=v;self(self,pos+1,std::max(v,maximum),next);}
  };grow(grow,1,0,0);return out;
}
int rank_mod(const int input[M][M],int n,int p,int cap){
  int a[M][M]{};for(int i=0;i<n;++i)for(int j=0;j<n;++j){a[i][j]=input[i][j]%p;if(a[i][j]<0)a[i][j]+=p;}
  int r=0;
  for(int j=0;j<n&&r<n;++j){int pivot=r;while(pivot<n&&!a[pivot][j])++pivot;if(pivot==n)continue;
    for(int k=j;k<n;++k)std::swap(a[pivot][k],a[r][k]);int inv=1;while(a[r][j]*inv%p!=1)++inv;
    for(int i=r+1;i<n;++i)if(a[i][j]){int f=a[i][j]*inv%p;for(int k=j;k<n;++k){a[i][k]=(a[i][k]-f*a[r][k])%p;if(a[i][k]<0)a[i][k]+=p;}}
    if(++r>=cap)return r;
  }return r;
}
long long factorial(int n){long long out=1;for(int j=2;j<=n;++j)out*=j;return out;}
int index(const std::array<int,3>& pi){int out=0;for(int i=0;i<3;++i){int count=0;for(int j=i+1;j<3;++j)count+=pi[j]<pi[i];out+=count*factorial(2-i);}return out;}
int root(const std::array<int,M>& parent,int v){while(parent[v]!=v)v=parent[v];return v;}
int main(){const std::array<int,3> primes={3,5,31};long long total_candidates=0,total_partition_tests=0;
  for(int n=3;n<=9;++n){auto parts=partitions(n);unsigned full=(1u<<n)-1;long long coverage=0,path_covers=0;
    std::array<std::array<long long,6>,3> sums{};long long tests=0;
    for(int a=0;a<n;++a)for(int b=a+1;b<n;++b)for(int c=b+1;c<n;++c){
      unsigned mask=(1u<<a)|(1u<<b)|(1u<<c),heads_mask=0;std::array<int,M> tau{};std::vector<int> tails,heads,starts;
      for(int i=0;i<n;++i)if(mask&(1u<<i)){tau[i]=(i+1)%n;heads_mask|=1u<<tau[i];starts.push_back(tau[i]);}else tails.push_back(i);
      std::sort(starts.begin(),starts.end());for(int i=0;i<n;++i)if(!(heads_mask&(1u<<i)))heads.push_back(i);
      std::array<int,M> end_label;end_label.fill(-1);for(int i=0;i<3;++i){int v=starts[i];while(!(mask&(1u<<v)))v=(v+1)%n;end_label[v]=i;}
      do{++coverage;bool extra=false;for(unsigned i=0;i<tails.size();++i){tau[tails[i]]=heads[i];extra|=heads[i]==(tails[i]+1)%n;}if(extra)continue;
        unsigned seen=0;std::array<int,3> pi{};bool valid=true;
        for(int i=0;i<4&&valid;++i){int v=starts[i];while(true){if(seen&(1u<<v)){valid=false;break;}seen|=1u<<v;if(mask&(1u<<v))break;v=tau[v];}if(valid){pi[i]=end_label[v];assert(pi[i]>=0);}}
        if(!valid||seen!=full)continue;++path_covers;
        std::array<int,3> channels{};for(int shift=0;shift<3;++shift){std::array<int,3> relative{};for(int i=0;i<3;++i)relative[i]=(pi[(i+shift)%3]-shift+3)%3;channels[shift]=index(relative);}
        int k[M][M]{};for(int i=0;i<n;++i){int j=(i+1)%n;++k[i][j];--k[j][i];j=tau[i];--k[i][j];++k[j][i];}
        unsigned active=0;std::array<int,M> components{};std::iota(components.begin(),components.end(),0);int clusters=n;
        for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)if(k[i][j]){active|=(1u<<i)|(1u<<j);int x=root(components,i),y=root(components,j);if(x!=y){components[x]=y;--clusters;}}
        if(clusters>4)continue;
        std::array<int,3> ranks{};for(int f=0;f<3;++f)ranks[f]=rank_mod(k,n,primes[f],7);
        if(std::all_of(ranks.begin(),ranks.end(),[](int r){return r>6;}))continue;
        std::array<long long,3> aggregate{};
        for(const auto& part:parts){if(part.c<clusters-1||(active|part.support)!=full)continue;
          auto parent=components;int remaining=clusters;for(auto [i,j]:part.merges){int x=root(parent,i),y=root(parent,j);if(x!=y){parent[x]=y;--remaining;}}
          if(remaining!=1)continue;
          int target=6-2*part.c;int compressed[M][M]{};
          for(int i=0;i<n;++i)for(int j=0;j<n;++j)compressed[part.labels[i]][part.labels[j]]+=k[i][j];
          for(int f=0;f<3;++f)if(ranks[f]<=6&&target<=ranks[f]){++tests;
            bool match=part.c==0?ranks[f]==target:rank_mod(compressed,part.blocks,primes[f],target+1)==target;
            if(match)aggregate[f]+=part.weight24;
          }
        }
        for(int f=0;f<3;++f)for(int channel:channels)sums[f][channel]+=aggregate[f];
      }while(std::next_permutation(heads.begin(),heads.end()));
    }
    assert(coverage==factorial(n)/6);total_candidates+=coverage;total_partition_tests+=tests;
    for(int f=0;f<3;++f){std::cout<<"{\"q\":"<<n<<",\"p\":"<<primes[f]<<",\"candidate_coverage\":"<<coverage<<",\"path_covers\":"<<path_covers<<",\"partition_rank_tests\":"<<tests<<",\"boundary_weight24_rotations\":[";
      for(int i=0;i<6;++i){if(i)std::cout<<',';std::cout<<sums[f][i];}std::cout<<"]}\n";
    }std::cerr<<"q="<<n<<" complete\n";
  }
  std::cerr<<"total_candidates="<<total_candidates<<" partition_rank_tests="<<total_partition_tests<<'\n';
}
