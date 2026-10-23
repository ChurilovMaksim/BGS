#define main prior_open_second_main
#include "dependencies/prior_open_second.cpp"
#undef main

bool neutral(const int k[M][M],const Collision& part,unsigned active,int n){
  std::array<std::vector<int>,M> blocks;
  for(int i=0;i<n;++i)blocks[part.labels[i]].push_back(i);
  for(const auto& block:blocks)if(block.size()==2&&!(active&(1u<<block[0]))&&!(active&(1u<<block[1])))return true;
  std::array<int,M> color; color.fill(-1);
  for(int i=0;i<n;++i)if((active&(1u<<i))&&color[i]<0){
    std::vector<int> nodes{i},parts[2];color[i]=0;bool bip=true;
    for(unsigned a=0;a<nodes.size();++a){int v=nodes[a];parts[color[v]].push_back(v);
      for(int j=0;j<n;++j)if(k[v][j]){if(color[j]<0){color[j]=1-color[v];nodes.push_back(j);}else if(color[j]==color[v])bip=false;}}
    if(!bip||nodes.size()!=6)continue;if(parts[0].size()>parts[1].size())std::swap(parts[0],parts[1]);
    if(parts[0].size()!=2||parts[1].size()!=4)continue;
    bool complete=true;for(int a:parts[0])for(int b:parts[1])complete&=k[a][b]!=0;if(!complete)continue;
    bool untouched=true;for(int v:nodes){const auto& block=blocks[part.labels[v]];
      if(block.size()==1)continue;
      if(block.size()==2&&block[0]==std::min(parts[0][0],parts[0][1])&&block[1]==std::max(parts[0][0],parts[0][1]))continue;
      untouched=false;}
    if(untouched)return true;
  }return false;
}
int main(){
  const std::vector<int> primes={3,5,7,11,13,17,19,23,29};long long total=0;
  for(int n=3;n<=12;++n){auto one=collisions(n,1),two=collisions(n,2);std::vector<int> rest(n-1);std::iota(rest.begin(),rest.end(),1);
    std::vector<long long> all(primes.size()),primitive(primes.size());long long coverage=0;
    do{Perm tau{};int prev=0;for(int v:rest){tau[prev]=v;prev=v;}tau[prev]=0;
      auto best=tau;int stabilizer=0;for(int s=0;s<n;++s){auto v=rotated(tau,n,s);if(v<best)best=v;if(v==tau)++stabilizer;}
      if(best!=tau)continue;long long orbit=n/stabilizer;coverage+=orbit;
      int k[M][M]{},common=0;for(int i=0;i<n;++i){int j=(i+1)%n;common+=tau[i]==j;++k[i][j];--k[j][i];j=tau[i];--k[i][j];++k[j][i];}
      if(common!=3)continue;
      unsigned active=0,full=(1u<<n)-1;for(int i=0;i<n;++i)for(int j=0;j<n;++j)if(k[i][j])active|=(1u<<i);
      if(active!=full&&(std::popcount(active)>8||std::popcount(full^active)>4))continue;
      Collision discrete;discrete.blocks=n;discrete.weight12=12;std::iota(discrete.labels.begin(),discrete.labels.end(),0);
      auto add=[&](const Collision& part,int weight,unsigned field){all[field]+=weight*orbit;if(!neutral(k,part,active,n))primitive[field]+=weight*orbit;};
      int witness=0;if(n>=6){witness=std::abs(pf6(k,{0,1,2,3,4,5}));std::array<int,6> s={0,1,n/3,n/3+1,2*n/3,2*n/3+1};witness=std::gcd(witness,std::abs(pf6(k,s)));}
      for(unsigned f=0;f<primes.size();++f){int p=primes[f];if(witness%p)continue;int a[M][M]{};for(int i=0;i<n;++i)for(int j=0;j<n;++j)a[i][j]=k[i][j];
        int rank=rank_mod(a,n,p);if(rank>4)continue;
        if(rank==4&&active==full)add(discrete,12,f);
        for(const auto& part:one){if((active|part.support)!=full)continue;int b[M][M]{};
          for(int i=0;i<n;++i)for(int j=0;j<n;++j)b[part.labels[i]][part.labels[j]]+=k[i][j];
          if(rank_mod(b,part.blocks,p)==2)add(part,-6,f);}
        for(const auto& part:two){if((active|part.support)!=full)continue;int b[M][M]{};
          for(int i=0;i<n;++i)for(int j=0;j<n;++j)b[part.labels[i]][part.labels[j]]+=k[i][j];
          bool zero=true;for(int i=0;i<part.blocks;++i)for(int j=i+1;j<part.blocks;++j)if(b[i][j]%p)zero=false;
          if(zero)add(part,part.weight12,f);}
      }
    }while(std::next_permutation(rest.begin(),rest.end()));assert(coverage==factorial(n-1));total+=coverage;
    for(unsigned f=0;f<primes.size();++f)std::cout<<"{\"q\":"<<n<<",\"p\":"<<primes[f]<<",\"coverage\":"<<coverage<<",\"all12\":"<<all[f]<<",\"primitive12\":"<<primitive[f]<<"}\n";
    std::cerr<<"q="<<n<<" complete\n";
  }
  std::cerr<<"total="<<total<<"\n";
}
