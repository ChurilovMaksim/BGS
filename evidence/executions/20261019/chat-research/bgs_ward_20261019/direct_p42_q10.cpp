#define main inherited_rank_main
#include "dependencies/full_rank.cpp"
#undef main
#include <cassert>
struct Partition{std::array<int,M> labels{};int blocks=0,codim=0;long long weight720=0;unsigned support=0;};
struct DSU{std::array<int,M> p{};DSU(){std::iota(p.begin(),p.end(),0);}int root(int x){return p[x]==x?x:p[x]=root(p[x]);}void join(int x,int y){p[root(x)]=root(y);}};
std::vector<Partition> partitions(int n){std::vector<Partition> out;std::array<int,M> l{};
  auto visit=[&](auto&& self,int at,int mx)->void{if(at<n){for(int v=0;v<=mx+1;++v){int next=std::max(mx,v);if(at-next>4)continue;l[at]=v;self(self,at+1,next);}return;}
    Partition a;a.labels=l;a.blocks=mx+1;a.codim=n-a.blocks;std::array<int,M> sz{};for(int i=0;i<n;++i)++sz[l[i]];
    const long long num[]={0,1,-1,2,-11,19},den[]={1,1,2,3,8,5};long long nu=1,de=1;
    for(int i=0;i<a.blocks;++i){assert(sz[i]<=5);nu*=num[sz[i]];de*=den[sz[i]];long long d=std::gcd(std::abs(nu),de);nu/=d;de/=d;}
    assert(720%de==0);a.weight720=nu*(720/de);for(int i=0;i<n;++i)if(sz[l[i]]>1)a.support|=1u<<i;out.push_back(a);
  };visit(visit,1,0);long long stir[11][11]{};stir[0][0]=1;for(int i=1;i<=n;++i)for(int j=1;j<=i;++j)stir[i][j]=stir[i-1][j-1]+j*stir[i-1][j];long long expected=0;for(int j=std::max(1,n-4);j<=n;++j)expected+=stir[n][j];assert((long long)out.size()==expected);return out;}
int main(){long long total=0,checks=0;
  for(int n=10;n<=10;++n){auto parts=partitions(n);std::vector<int> rest(n-1);std::iota(rest.begin(),rest.end(),1);std::array<long long,3> sums{};long long coverage=0,relevant_cycles=0;
    do{++coverage;std::vector<int> tau(n);int last=0;for(int v:rest){tau[last]=v;last=v;}tau[last]=0;int common=0;for(int i=0;i<n;++i)common+=tau[i]==(i+1)%n;if(common!=6)continue;++relevant_cycles;
      Matrix k{};for(int i=0;i<n;++i){int j=(i+1)%n;++k[i][j];--k[j][i];j=tau[i];--k[i][j];++k[j][i];}
      unsigned active=0,full=(1u<<n)-1;for(int i=0;i<n;++i)for(int j=0;j<n;++j)if(k[i][j])active|=1u<<i;
      std::vector<std::pair<int,int>> ac;if(active)for(int i=0;i<n;++i)if(active&(1u<<i)){int s=(i+1)%n;while(!(active&(1u<<s)))s=(s+1)%n;int t=tau[i];while(!(active&(1u<<t)))t=tau[t];if(s==t)ac.emplace_back(i,s);}
      for(const auto& part:parts){if((active|part.support)!=full)continue;Matrix comp{};for(int i=0;i<n;++i)for(int j=0;j<n;++j)comp[part.labels[i]][part.labels[j]]+=k[i][j];
        DSU cl;for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)if(k[i][j]||part.labels[i]==part.labels[j])cl.join(i,j);
        std::vector<std::vector<int>> groups;std::array<int,M> ids;ids.fill(-1);for(int i=0;i<n;++i){int root=cl.root(i);if(ids[root]<0){ids[root]=groups.size();groups.push_back({});}groups[ids[root]].push_back(i);}
        if(groups.size()!=2)continue;
        bool boundary_ok=true;for(const auto& nodes:groups){int t=0,ell=0;bool has_active=false;for(int v:nodes)if(active&(1u<<v))has_active=true;else ++t;
          for(auto [a,b]:ac){ell+=cl.root(a)==cl.root(nodes[0]);ell+=cl.root(b)==cl.root(nodes[0]);}assert(ell%2==0);int ei=has_active?ell/2+t:nodes.size();boundary_ok&=ei==3;}
        if(!boundary_ok)continue;
        int f=0;for(int p:{3,5,13}){++checks;bool selected=true;for(const auto& nodes:groups){std::vector<int> blocks;for(int v:nodes)blocks.push_back(part.labels[v]);std::sort(blocks.begin(),blocks.end());blocks.erase(std::unique(blocks.begin(),blocks.end()),blocks.end());int c=nodes.size()-blocks.size();int r=rankmod(comp,blocks,p);assert(r%2==0);selected&=c+r/2==2;}
          if(selected)sums[f]+=part.weight720;++f;}
      }
    }while(std::next_permutation(rest.begin(),rest.end()));total+=coverage;std::cerr<<"q="<<n<<" cycles="<<coverage<<" common6="<<relevant_cycles<<" partitions="<<parts.size()<<"\n";
    for(int f=0;f<3;++f)std::cout<<"{\"q\":"<<n<<",\"p\":"<<(f==0?3:f==1?5:13)<<",\"cycles\":"<<coverage<<",\"weight720\":"<<sums[f]<<"}\n";
  }std::cerr<<"total_cycles="<<total<<" selected_field_checks="<<checks<<"\n";
}
