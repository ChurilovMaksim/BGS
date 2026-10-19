#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <numeric>
#include <set>
#include <vector>
using Mat=std::vector<std::vector<int>>;
struct DSU{std::vector<int> p;explicit DSU(int n):p(n){std::iota(p.begin(),p.end(),0);}int root(int x){return p[x]==x?x:p[x]=root(p[x]);}void join(int a,int b){p[root(a)]=root(b);}};
int rank_mod(Mat a,int p){int n=a.size(),r=0;for(auto& row:a)for(int& v:row)v=(v%p+p)%p;
  for(int col=0;col<n;++col){int pivot=r;while(pivot<n&&!a[pivot][col])++pivot;if(pivot==n)continue;
    std::swap(a[pivot],a[r]);int inv=1;while(inv*a[r][col]%p!=1)++inv;
    for(int j=col;j<n;++j)a[r][j]=a[r][j]*inv%p;
    for(int i=r+1;i<n;++i){int f=a[i][col];for(int j=col;j<n;++j)a[i][j]=(a[i][j]-f*a[r][j]%p+p)%p;}++r;
  }return r;}
Mat sub(const Mat& k,const std::vector<int>& v){Mat a(v.size(),std::vector<int>(v.size()));for(unsigned i=0;i<v.size();++i)for(unsigned j=0;j<v.size();++j)a[i][j]=k[v[i]][v[j]];return a;}
std::vector<std::vector<int>> all_parts(int n){std::vector<std::vector<int>> out;std::vector<int> l(n);auto visit=[&](auto&& self,int at,int mx)->void{
  if(at==n){out.push_back(l);return;}for(int v=0;v<=mx+1;++v){l[at]=v;self(self,at+1,std::max(mx,v));}};visit(visit,1,0);return out;}
int main(){long long cycles=0,pairs=0,fields=0,leading=0,clusters=0,k22=0,k24=0,passivepairs=0,critical=0;
  for(int n=3;n<=7;++n){const auto parts=all_parts(n);std::vector<int> rest(n-1);std::iota(rest.begin(),rest.end(),1);long long per_n=0;
    do{std::vector<int> tau(n);int prev=0;for(int v:rest){tau[prev]=v;prev=v;}tau[prev]=0;
      Mat k(n,std::vector<int>(n));for(int i=0;i<n;++i){int j=(i+1)%n;++k[i][j];--k[j][i];j=tau[i];--k[i][j];++k[j][i];}
      std::vector<int> degree(n);DSU kc(n);for(int i=0;i<n;++i)for(int j=0;j<n;++j)if(k[i][j]){++degree[i];kc.join(i,j);}
      std::vector<int> active;for(int i=0;i<n;++i)if(degree[i])active.push_back(i);
      std::vector<std::pair<int,int>> active_common;
      for(int i:active){int s=(i+1)%n;while(!degree[s])s=(s+1)%n;int t=tau[i];while(!degree[t])t=tau[t];if(s==t)active_common.emplace_back(i,s);}
      for(const auto& lab:parts){++pairs;++per_n;int nb=1+*std::max_element(lab.begin(),lab.end());std::vector<int> sizes(nb);for(int x:lab)++sizes[x];
        DSU cl(n);for(int i=0;i<n;++i){for(int j=i+1;j<n;++j)if(k[i][j]||lab[i]==lab[j])cl.join(i,j);}
        std::vector<int> core;for(int i=0;i<n;++i)if(degree[i]||sizes[lab[i]]>1)core.push_back(i);
        int e=0;if(!core.empty())for(int i:core){int s=(i+1)%n;while(!degree[s]&&sizes[lab[s]]==1)s=(s+1)%n;int t=tau[i];while(!degree[t]&&sizes[lab[t]]==1)t=tau[t];e+=s==t;}
        std::vector<std::vector<int>> groups(n);for(int i:core)groups[cl.root(i)].push_back(i);
        for(int p:{3,5,13}){++fields;if(core.empty()){++leading;continue;}
          int sum_j=0,sum_e=0,sum_delta=0,prim_j=0,prim_q=0;Mat full(nb,std::vector<int>(nb));
          for(int i=0;i<n;++i)for(int j=0;j<n;++j)full[lab[i]][lab[j]]+=k[i][j];
          int actual_h=n-nb+rank_mod(full,p)/2;
          for(const auto& nodes:groups)if(!nodes.empty()){++clusters;std::vector<int> av;std::set<int> blocks,activeblocks,kcomps;int t=0;
            for(int v:nodes){blocks.insert(lab[v]);if(degree[v]){av.push_back(v);activeblocks.insert(lab[v]);kcomps.insert(kc.root(v));}else ++t;}
            std::vector<int> bid(blocks.begin(),blocks.end());Mat comp(bid.size(),std::vector<int>(bid.size()));
            for(int i:av)for(int j:av){int a=std::lower_bound(bid.begin(),bid.end(),lab[i])-bid.begin(),b=std::lower_bound(bid.begin(),bid.end(),lab[j])-bid.begin();comp[a][b]+=k[i][j];}
            int rg=rank_mod(sub(k,av),p),rs=rank_mod(comp,p);assert(rg%2==0&&rs%2==0);int g=rg/2,s=rs/2;
            int c=nodes.size()-blocks.size(),j=c+s,ei=0;
            if(av.empty()){assert(blocks.size()==1);ei=nodes.size();}
            else{int cc=av.size()-activeblocks.size(),u=cc-(g-s),kk=kcomps.size();
              assert(u>=kk-1&&c==cc+t&&j==g+u+t);int ell=0;
              for(auto [a,b]:active_common){ell+=cl.root(a)==cl.root(nodes[0]);ell+=cl.root(b)==cl.root(nodes[0]);}
              assert(ell%2==0);int n2=0;for(int v:av)n2+=degree[v]==2;assert(ell<=n2&&n2<=2*g+2*kk);ei=ell/2+t;
            }
            int delta=2*j-ei;assert(delta>=0&&j<=delta+1);sum_j+=j;sum_e+=ei;sum_delta+=delta;
            if(delta>0){prim_j+=j;prim_q+=nodes.size();critical+=j==delta+1;}
            else{assert(j==1);if(av.empty()){assert(nodes.size()==2);++passivepairs;}
              else{assert(g==1&&t==0&&kcomps.size()==1);assert(av.size()==4||av.size()==6);
                std::vector<int> color(n,-1),queue{av[0]};color[av[0]]=0;std::vector<int> side[2];
                for(unsigned at=0;at<queue.size();++at){int v=queue[at];side[color[v]].push_back(v);for(int w:av)if(k[v][w]){
                  if(color[w]<0){color[w]=1-color[v];queue.push_back(w);}else assert(color[w]!=color[v]);}}
                if(side[0].size()>side[1].size())std::swap(side[0],side[1]);assert(side[0].size()==2&&(side[1].size()==2||side[1].size()==4));
                for(int a:side[0])for(int b:side[1])assert(k[a][b]);
                if(side[1].size()==2)++k22;else{++k24;for(int v:av)if(sizes[lab[v]]!=1)assert(sizes[lab[v]]==2&&lab[side[0][0]]==lab[side[0][1]]&&lab[v]==lab[side[0][0]]);}
              }
            }
          }
          assert(sum_j==actual_h&&sum_e==e&&sum_delta==2*actual_h-e);assert(prim_j<=2*sum_delta&&prim_q<=16*sum_delta);
        }
      }++cycles;
    }while(std::next_permutation(rest.begin(),rest.end()));std::cerr<<"n="<<n<<" cycle_partition_pairs="<<per_n<<"\n";
  }
  std::cout<<"{\"status\":\"passed\",\"cycles\":"<<cycles<<",\"cycle_partition_pairs\":"<<pairs<<",\"field_cases\":"<<fields<<",\"empty_leading_cases\":"<<leading<<",\"cluster_checks\":"<<clusters<<",\"zero_defect_K22\":"<<k22<<",\"zero_defect_K24\":"<<k24<<",\"zero_defect_passive_pairs\":"<<passivepairs<<",\"critical_positive_clusters\":"<<critical<<"}\n";
}
