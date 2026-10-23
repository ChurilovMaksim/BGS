#define main original_pivot_main
#include "pivot_search.cpp"
#undef main
#include <cassert>
Matrix difference(const std::vector<int>& tau){int n=tau.size();Matrix k{};
  for(int i=0;i<n;++i){int j=(i+1)%n;++k[i][j];--k[j][i];j=tau[i];--k[i][j];++k[j][i];}return k;}
int compressed_rank(const Matrix& k,int n,int a,int b,int p){Matrix out{};std::vector<int> lab(n),ind(n-1);int at=0;
  for(int i=0;i<n;++i)if(i!=b)lab[i]=at++;lab[b]=lab[a];
  for(int i=0;i<n;++i)for(int j=0;j<n;++j)out[lab[i]][lab[j]]+=k[i][j];
  std::iota(ind.begin(),ind.end(),0);return rankmod(out,ind,p);}
int main(){
  long long cycles=0,fields=0,saturated=0,k22=0,k24=0;std::vector<long long> sat(3);
  for(int n=3;n<=10;++n){std::vector<int> rest(n-1),all(n);std::iota(rest.begin(),rest.end(),1);std::iota(all.begin(),all.end(),0);long long visits=0;
    do{std::vector<int> tau(n);int last=0;for(int v:rest){tau[last]=v;last=v;}tau[last]=0;Matrix k=difference(tau),fact{};
      std::vector<int> deg(n),color(n,-1),component(n,-1),active;int edges=0,d2=0,d3=0;
      for(int i=0;i<n;++i){int sum=0;for(int j=0;j<n;++j){sum+=k[i][j];deg[i]+=k[i][j]!=0;}assert(sum==0);
        assert(deg[i]!=1&&deg[i]<=4);if(deg[i])active.push_back(i);d2+=deg[i]==2;d3+=deg[i]==3;
        for(int j=i+1;j<n;++j)if(k[i][j]){++edges;int w=k[i][j];fact[i][i]+=w;fact[i][j]+=w;fact[j][i]-=w;fact[j][j]-=w;}}
      assert(fact==k);std::vector<std::vector<int>> comps;std::vector<bool> bip;
      for(int i:active)if(color[i]<0){int cid=comps.size();std::vector<int> nodes{i};color[i]=0;component[i]=cid;bool good=true;
        for(unsigned at=0;at<nodes.size();++at){int v=nodes[at];for(int j=0;j<n;++j)if(k[v][j]){
          if(color[j]<0){color[j]=1-color[v];component[j]=cid;nodes.push_back(j);}else if(color[j]==color[v])good=false;}}
        comps.push_back(nodes);bip.push_back(good);}
      int common=0,q=active.size();
      if(q){Matrix core{};for(int i:active){int s=(i+1)%n;while(!deg[s])s=(s+1)%n;int t=tau[i];while(!deg[t])t=tau[t];
          common+=s==t;++core[i][s];--core[s][i];--core[i][t];++core[t][i];}
        assert(core==k);}
      int bcount=std::count(bip.begin(),bip.end(),true),cc=comps.size();int fi=0;
      for(int p:{3,5,13}){++fields;int r=rankmod(k,all,p);assert(r%2==0);assert(r>=2*q-cc-bcount-edges);assert(common<=r);
        if(r&&common==r){++saturated;++sat[fi];assert(2*common==d2&&d2==2*r&&d3==0&&cc==r/2&&cc==bcount);
          for(unsigned ci=0;ci<comps.size();++ci){const auto& nodes=comps[ci];std::vector<int> part[2];for(int v:nodes)part[color[v]].push_back(v);
            if(part[0].size()>part[1].size())std::swap(part[0],part[1]);
            assert(part[0].size()==2&&(part[1].size()==2||part[1].size()==4));
            for(int a:part[0])for(int b:part[1])assert(k[a][b]!=0);
            int drops=0;for(unsigned a=0;a<nodes.size();++a)for(unsigned b=a+1;b<nodes.size();++b)
              drops+=compressed_rank(k,n,nodes[a],nodes[b],p)==r-2;
            if(part[1].size()==2){++k22;assert(drops==2);}else{++k24;assert(drops==1);
              int a=part[0][0],b=part[0][1];auto t=tau;auto sw=[&](int i){return i==a?b:i==b?a:i;};
              for(int i=0;i<n;++i)t[i]=sw(tau[sw(i)]);Matrix reduced=difference(t),expected=k;
              for(int i:nodes)for(int j:nodes)expected[i][j]=0;assert(reduced==expected);
            }
          }
        }++fi;
      }++visits;
    }while(std::next_permutation(rest.begin(),rest.end()));cycles+=visits;std::cerr<<"m="<<n<<" cycles="<<visits<<"\n";
  }
  std::cout<<"{\"cycles\":"<<cycles<<",\"field_cases\":"<<fields<<",\"saturated_field_cases\":"<<saturated<<",\"K22_components_checked\":"<<k22<<",\"K24_components_checked\":"<<k24<<",\"saturated_by_field\":["<<sat[0]<<","<<sat[1]<<","<<sat[2]<<"]}\n";
}
