#include "dependencies/neutral_test.hpp"

unsigned rotate_mask(unsigned mask,int n,int shift){unsigned out=0;for(int i=0;i<n;++i)if(mask&(1u<<i))out|=1u<<((i+shift)%n);return out;}

int main(){
  const std::vector<int> primes={3,5,7,11,13,17,19,23,29};long long candidates=0,accepted=0;
  for(int n=3;n<=12;++n){auto one=collisions(n,1),two=collisions(n,2);unsigned full=(1u<<n)-1;
    std::vector<std::array<long long,4>> all(primes.size()),primitive(primes.size());std::vector<std::array<std::array<long long,4>,4>> connected_counts(primes.size());long long set_coverage=0,permutations=0;
    for(int a=1;a<n;++a)for(int b=a+1;b<n;++b){unsigned mask=1u|(1u<<a)|(1u<<b),best=mask;int stabilizer=0;
      for(int s=0;s<n;++s){unsigned v=rotate_mask(mask,n,s);best=std::min(best,v);stabilizer+=v==mask;}
      if(best!=mask)continue;long long orbit=n/stabilizer;set_coverage+=orbit;
      Perm tau{};std::vector<int> tails,heads,starts;unsigned used_heads=0;
      for(int i=0;i<n;++i)if(mask&(1u<<i)){tau[i]=(i+1)%n;used_heads|=1u<<tau[i];starts.push_back(tau[i]);}else tails.push_back(i);
      for(int i=0;i<n;++i)if(!(used_heads&(1u<<i)))heads.push_back(i);std::sort(starts.begin(),starts.end());
      std::array<int,M> endlabel;endlabel.fill(-1);for(int j=0;j<3;++j){int v=starts[j];while(!(mask&(1u<<v)))v=(v+1)%n;endlabel[v]=j;}
      do{++candidates;permutations+=orbit;bool extra=false;for(unsigned i=0;i<tails.size();++i){tau[tails[i]]=heads[i];extra|=heads[i]==(tails[i]+1)%n;}if(extra)continue;
        unsigned seen=0;std::array<int,3> pi{};bool valid=true;
        for(int j=0;j<3&&valid;++j){int v=starts[j];while(true){if(seen&(1u<<v)){valid=false;break;}seen|=1u<<v;if(mask&(1u<<v))break;v=tau[v];}if(valid){pi[j]=endlabel[v];assert(pi[j]>=0);}}
        if(!valid||seen!=full)continue;++accepted;
        bool id=true,cyc=true,inv=true;for(int j=0;j<3;++j){id&=pi[j]==j;cyc&=pi[j]==(j+1)%3;inv&=pi[j]==(j+2)%3;}int channel=id?0:cyc?1:inv?2:3;
        if(channel==3){int fixed=0;for(int j=0;j<3;++j)fixed+=pi[j]==j;assert(fixed==1);}
        int k[M][M]{};for(int i=0;i<n;++i){int j=(i+1)%n;++k[i][j];--k[j][i];j=tau[i];--k[i][j];++k[j][i];}
        unsigned active=0;for(int i=0;i<n;++i)for(int j=0;j<n;++j)if(k[i][j])active|=1u<<i;
        if(active!=full&&(std::popcount(active)>8||std::popcount(full^active)>4))continue;
        Collision discrete;discrete.blocks=n;discrete.weight12=12;std::iota(discrete.labels.begin(),discrete.labels.end(),0);
        auto add=[&](const Collision& part,int weight,unsigned field){all[field][channel]+=weight*orbit;if(!neutral(k,part,active,n)){primitive[field][channel]+=weight*orbit;
          std::array<int,M> parent{};std::iota(parent.begin(),parent.end(),0);auto root=[&](int v){while(parent[v]!=v)v=parent[v];return v;};
          for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)if(k[i][j]||part.labels[i]==part.labels[j])parent[root(i)]=root(j);
          bool connected=true;for(int i=1;i<n;++i)connected&=root(i)==root(0);
          if(connected){int type=part.blocks==n?0:part.blocks==n-1?1:weight==8?2:3;connected_counts[field][channel][type]+=orbit;}
        }};
        int witness=0;if(n>=6){witness=std::abs(pf6(k,{0,1,2,3,4,5}));std::array<int,6> ss={0,1,n/3,n/3+1,2*n/3,2*n/3+1};witness=std::gcd(witness,std::abs(pf6(k,ss)));}
        for(unsigned f=0;f<primes.size();++f){int p=primes[f];if(witness%p)continue;int km[M][M]{};for(int i=0;i<n;++i)for(int j=0;j<n;++j)km[i][j]=k[i][j];int rank=rank_mod(km,n,p);if(rank>4)continue;
          if(rank==4&&active==full)add(discrete,12,f);
          for(const auto& part:one){if((active|part.support)!=full)continue;int m[M][M]{};for(int i=0;i<n;++i)for(int j=0;j<n;++j)m[part.labels[i]][part.labels[j]]+=k[i][j];if(rank_mod(m,part.blocks,p)==2)add(part,-6,f);}
          for(const auto& part:two){if((active|part.support)!=full)continue;int m[M][M]{};for(int i=0;i<n;++i)for(int j=0;j<n;++j)m[part.labels[i]][part.labels[j]]+=k[i][j];bool zero=true;for(int i=0;i<part.blocks;++i)for(int j=i+1;j<part.blocks;++j)if(m[i][j]%p)zero=false;if(zero)add(part,part.weight12,f);}
        }
      }while(std::next_permutation(heads.begin(),heads.end()));
    }
    assert(set_coverage==n*(n-1)*(n-2)/6);assert(permutations==factorial(n)/6);
    for(unsigned f=0;f<primes.size();++f){std::cout<<"{\"q\":"<<n<<",\"p\":"<<primes[f]<<",\"common_set_coverage\":"<<set_coverage<<",\"candidate_coverage\":"<<permutations<<",\"all12\":[";
      for(int c=0;c<4;++c){if(c)std::cout<<",";std::cout<<all[f][c];}std::cout<<"],\"primitive12\":[";for(int c=0;c<4;++c){if(c)std::cout<<",";std::cout<<primitive[f][c];}std::cout<<"],\"connected_type_counts\":[";for(int c=0;c<4;++c){if(c)std::cout<<",";std::cout<<"[";for(int tt=0;tt<4;++tt){if(tt)std::cout<<",";std::cout<<connected_counts[f][c][tt];}std::cout<<"]";}std::cout<<"]}\n";}
    std::cerr<<"q="<<n<<" complete\n";
  }
  std::cerr<<"actual_candidates="<<candidates<<" accepted_open_path_covers="<<accepted<<"\n";
}
