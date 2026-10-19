#define main previous_unused_main
#include "dependencies/prior_open_second.cpp"
#undef main

unsigned rotate_bits(unsigned mask,int n,int s){unsigned out=0;for(int i=0;i<n;++i)if(mask&(1u<<i))out|=1u<<((i+s)%n);return out;}
bool connected_collision(const int k[M][M],const Collision& part,int n){
  std::array<int,M> parent{};std::iota(parent.begin(),parent.end(),0);
  auto root=[&](int x){while(parent[x]!=x)x=parent[x];return x;};
  for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)if(k[i][j]||part.labels[i]==part.labels[j])parent[root(i)]=root(j);
  for(int i=1;i<n;++i)if(root(i)!=root(0))return false;return true;
}
int main(){const std::vector<int> primes={3,5,7,11,13,17,19,23,29,31};long long candidates=0,accepted=0;
  for(int n=3;n<=12;++n){auto one=collisions(n,1),two=collisions(n,2);unsigned full=(1u<<n)-1;
    std::vector<std::array<long long,2>> counts(primes.size());long long set_coverage=0,permutation_coverage=0;
    for(int a=1;a<n;++a){unsigned mask=1u|(1u<<a),best=mask;int stabilizer=0;
      for(int s=0;s<n;++s){unsigned v=rotate_bits(mask,n,s);best=std::min(best,v);stabilizer+=v==mask;}
      if(mask!=best)continue;long long orbit=n/stabilizer;set_coverage+=orbit;
      Perm tau{};std::vector<int> starts,tails,heads;unsigned used_heads=0;
      for(int i=0;i<n;++i)if(mask&(1u<<i)){tau[i]=(i+1)%n;used_heads|=1u<<tau[i];starts.push_back(tau[i]);}else tails.push_back(i);
      std::sort(starts.begin(),starts.end());for(int i=0;i<n;++i)if(!(used_heads&(1u<<i)))heads.push_back(i);
      std::array<int,M> end_label;end_label.fill(-1);for(int i=0;i<2;++i){int v=starts[i];while(!(mask&(1u<<v)))v=(v+1)%n;end_label[v]=i;}
      do{++candidates;permutation_coverage+=orbit;bool extra=false;for(unsigned i=0;i<tails.size();++i){tau[tails[i]]=heads[i];extra|=heads[i]==(tails[i]+1)%n;}if(extra)continue;
        unsigned seen=0;std::array<int,2> pi{};bool valid=true;
        for(int i=0;i<2&&valid;++i){int v=starts[i];while(true){if(seen&(1u<<v)){valid=false;break;}seen|=1u<<v;if(mask&(1u<<v))break;v=tau[v];}if(valid){pi[i]=end_label[v];assert(pi[i]>=0);}}
        if(!valid||seen!=full)continue;++accepted;int channel=pi[0]==0?0:1;
        int k[M][M]{};for(int i=0;i<n;++i){int j=(i+1)%n;++k[i][j];--k[j][i];j=tau[i];--k[i][j];++k[j][i];}
        unsigned active=0;for(int i=0;i<n;++i)for(int j=0;j<n;++j)if(k[i][j])active|=1u<<i;
        if(active!=full&&(std::popcount(active)>8||std::popcount(full^active)>4))continue;
        int witness=0;if(n>=6){witness=std::abs(pf6(k,{0,1,2,3,4,5}));std::array<int,6> other={0,1,n/3,n/3+1,2*n/3,2*n/3+1};witness=std::gcd(witness,std::abs(pf6(k,other)));}
        std::vector<int> original_ranks(primes.size(),99);bool relevant=false;
        for(unsigned f=0;f<primes.size();++f){int p=primes[f];if(witness%p)continue;
          int km[M][M]{};for(int i=0;i<n;++i)for(int j=0;j<n;++j)km[i][j]=k[i][j];original_ranks[f]=rank_mod(km,n,p);relevant|=original_ranks[f]<=4;
        }
        if(!relevant)continue;
        Collision discrete;discrete.blocks=n;discrete.weight12=12;std::iota(discrete.labels.begin(),discrete.labels.end(),0);
        bool discrete_connected=active==full&&connected_collision(k,discrete,n);
        std::vector<const Collision*> eligible_one,eligible_two;
        for(const auto& part:one)if((active|part.support)==full&&connected_collision(k,part,n))eligible_one.push_back(&part);
        for(const auto& part:two)if((active|part.support)==full&&connected_collision(k,part,n))eligible_two.push_back(&part);
        if(!discrete_connected&&eligible_one.empty()&&eligible_two.empty())continue;
        for(unsigned f=0;f<primes.size();++f){int p=primes[f],rank=original_ranks[f];if(rank>4)continue;
          if(rank==4&&discrete_connected)counts[f][channel]+=12*orbit;
          for(const auto* part:eligible_one){int compressed[M][M]{};for(int i=0;i<n;++i)for(int j=0;j<n;++j)compressed[part->labels[i]][part->labels[j]]+=k[i][j];if(rank_mod(compressed,part->blocks,p)==2)counts[f][channel]-=6*orbit;}
          for(const auto* part:eligible_two){int compressed[M][M]{};for(int i=0;i<n;++i)for(int j=0;j<n;++j)compressed[part->labels[i]][part->labels[j]]+=k[i][j];bool zero=true;for(int i=0;i<part->blocks;++i)for(int j=i+1;j<part->blocks;++j)if(compressed[i][j]%p)zero=false;if(zero)counts[f][channel]+=part->weight12*orbit;}
        }
      }while(std::next_permutation(heads.begin(),heads.end()));
    }
    assert(set_coverage==n*(n-1)/2);assert(permutation_coverage==factorial(n)/2);
    for(unsigned f=0;f<primes.size();++f)std::cout<<"{\"q\":"<<n<<",\"p\":"<<primes[f]<<",\"set_coverage\":"<<set_coverage<<",\"candidate_coverage\":"<<permutation_coverage<<",\"connected12\":["<<counts[f][0]<<','<<counts[f][1]<<"]}\n";
    std::cerr<<"q="<<n<<" complete\n";
  }std::cerr<<"actual_candidates="<<candidates<<" accepted_path_covers="<<accepted<<'\n';
}
