#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using Matrix=std::vector<std::vector<int>>;
using Counts=std::array<long long,7>;
const std::vector<int> primes={3,5,7,11,13,17,19,23,29,31};
const std::array<int,7> weights24={24,-12,16,6,-33,-8,-3};
int mod(int x,int p){x%=p;return x<0?x+p:x;}
int inverse(int a,int p){for(int b=1;b<p;++b)if(a*b%p==1)return b;assert(false);return 0;}
int rref(Matrix& a,int p,std::vector<int>* pivots=nullptr){
  int r=0,n=a.size(),m=a[0].size();
  for(auto& row:a)for(int& x:row)x=mod(x,p);
  for(int j=0;j<m&&r<n;++j){int k=r;while(k<n&&!a[k][j])++k;if(k==n)continue;
    std::swap(a[r],a[k]);int u=inverse(a[r][j],p);for(int& x:a[r])x=x*u%p;
    for(int i=0;i<n;++i)if(i!=r&&a[i][j]){int v=a[i][j];for(int l=j;l<m;++l)a[i][l]=mod(a[i][l]-v*a[r][l],p);}
    if(pivots)pivots->push_back(j);++r;
  }return r;
}
int rank(Matrix a,int p){return rref(a,p);}
Matrix compress(const Matrix& k,const std::vector<int>& labels,int blocks){
  Matrix out(blocks,std::vector<int>(blocks));
  for(unsigned i=0;i<k.size();++i)for(unsigned j=0;j<k.size();++j)out[labels[i]][labels[j]]+=k[i][j];return out;
}
std::vector<int> normalize(std::vector<int> labels){
  std::map<int,int> seen;int next=0;for(int& v:labels){auto [it,inserted]=seen.emplace(v,next);if(inserted)++next;v=it->second;}return labels;
}
int type(const std::vector<int>& sizes){
  int pairs=0,triples=0,quads=0;for(int x:sizes){assert(1<=x&&x<=4);pairs+=x==2;triples+=x==3;quads+=x==4;}
  if(quads){assert(quads==1&&!pairs&&!triples);return 4;}
  if(triples){assert(triples==1&&pairs<=1);return pairs?5:2;}
  assert(pairs<=3);return pairs==0?0:pairs==1?1:pairs==2?3:6;
}
int type_labels(const std::vector<int>& labels){
  int blocks=*std::max_element(labels.begin(),labels.end())+1;std::vector<int> sizes(blocks);for(int x:labels)++sizes[x];return type(sizes);
}
std::vector<std::vector<int>> eligible_classes(const Matrix& k,int p){
  Matrix a=k;std::vector<int> pivots;int r=rref(a,p,&pivots),n=k.size();
  std::set<int> pivotset(pivots.begin(),pivots.end());std::vector<std::vector<int>> signatures(n);
  for(int j=0;j<n;++j)if(!pivotset.count(j)){
    std::vector<int> v(n);v[j]=1;for(int i=0;i<r;++i)v[pivots[i]]=mod(-a[i][j],p);
    for(int i=0;i<n;++i)signatures[i].push_back(v[i]);
  }
  std::map<std::vector<int>,std::vector<int>> classes;
  for(int i=0;i<n;++i)classes[signatures[i]].push_back(i);
  std::vector<std::vector<int>> out;for(const auto& [s,c]:classes)out.push_back(c);return out;
}
// All maximal-rank-drop partitions: roots lie in rowspace, and the resulting
// normal subspace is isotropic. The rank test checks the latter exactly.
void maximal_parts(const Matrix& k,int p,int g,const std::function<void(const std::vector<int>&)>& emit){
  auto classes=eligible_classes(k,p);int n=k.size();std::vector<int> labels(n);
  std::function<void(int,int,int)> next_class;
  next_class=[&](int ci,int blocks,int codim){
    if(ci==(int)classes.size()){
      if(rank(compress(k,labels,blocks),p)==2*(g-codim))emit(normalize(labels));return;
    }
    const auto& nodes=classes[ci];int size=nodes.size();std::vector<int> local(size);local[0]=0;
    std::function<void(int,int)> grow=[&](int pos,int maximum){
      if(pos==size){int count=maximum+1,c=codim+size-count;if(c>g)return;
        for(int i=0;i<size;++i)labels[nodes[i]]=blocks+local[i];next_class(ci+1,blocks+count,c);return;}
      for(int v=0;v<=maximum+1;++v){local[pos]=v;grow(pos+1,std::max(maximum,v));}
    };grow(1,0);
  };next_class(0,0,0);
}
Counts connected_weight(const Matrix& active,int p,int g,int passive){
  Counts out{};
  maximal_parts(active,p,g,[&](const std::vector<int>& labels){
    int b=*std::max_element(labels.begin(),labels.end())+1;std::vector<int> sizes(b);for(int x:labels)++sizes[x];
    std::function<void(int)> attach=[&](int i){if(i==passive){++out[type(sizes)];return;}
      for(int j=0;j<b;++j){++sizes[j];attach(i+1);--sizes[j];}
    };attach(0);
  });return out;
}
Counts two_component_weight(const Matrix& k,int first_size,int p){
  std::set<std::uint64_t> seen;Counts out{};int n=k.size();
  for(int a=0;a<first_size;++a)for(int b=first_size;b<n;++b){
    std::vector<int> bridge(n);std::iota(bridge.begin(),bridge.end(),0);bridge[b]=a;bridge=normalize(bridge);
    Matrix contracted=compress(k,bridge,n-1);assert(rank(contracted,p)==4);
    maximal_parts(contracted,p,2,[&](const std::vector<int>& after){
      std::vector<int> final(n);for(int i=0;i<n;++i)final[i]=after[bridge[i]];final=normalize(final);
      std::uint64_t code=0;for(int v:final)code=(code<<4)|v;
      if(seen.insert(code).second)++out[type_labels(final)];
    });
  }return out;
}
long long factorial(int n){long long v=1;for(int i=2;i<=n;++i)v*=i;return v;}
int permutation_index(const std::vector<int>& p){int out=0;for(unsigned i=0;i<p.size();++i){int smaller=0;for(unsigned j=i+1;j<p.size();++j)smaller+=p[j]<p[i];out+=smaller*factorial(p.size()-i-1);}return out;}
std::vector<long long> path_histogram(const Matrix& k,int passive,int e,long long& assignments,long long& covers){
  int active=k.size(),n=active+passive;std::vector<std::pair<int,int>> edges;
  std::vector<std::vector<int>> positive(active),negative(active);
  for(int i=0;i<active;++i)for(int j=0;j<active;++j)if(k[i][j]==1){
    int index=edges.size();edges.emplace_back(i,j);positive[i].push_back(index);negative[j].push_back(index);
  }
  int m=edges.size();std::vector<std::vector<int>> constraints(m);
  auto pair=[&](int a,int b){assert(a!=b);constraints[a].push_back(b);constraints[b].push_back(a);};
  for(int i=0;i<active;++i){
    if(positive[i].size()==1){assert(negative[i].size()==1);pair(positive[i][0],negative[i][0]);}
    else{assert(positive[i].size()==2&&negative[i].size()==2);pair(positive[i][0],positive[i][1]);pair(negative[i][0],negative[i][1]);}
  }
  std::vector<int> color(m,-1),component(m,-1);int loops=0;
  for(int i=0;i<m;++i)if(color[i]<0){std::vector<int> queue{i};color[i]=0;component[i]=loops;
    for(unsigned j=0;j<queue.size();++j){int v=queue[j];assert(constraints[v].size()==2);
      for(int w:constraints[v]){if(color[w]<0){color[w]=1-color[v];component[w]=loops;queue.push_back(w);}else if(color[w]==color[v])return std::vector<long long>(factorial(e));}
    }++loops;
  }
  assert(loops<24);std::vector<long long> histogram(factorial(e));
  for(unsigned mask=0;mask<(1u<<loops);++mask){++assignments;
    std::vector<int> sigma(n,-1),tau(n,-1),sin(n),tin(n);
    for(int index=0;index<m;++index){auto [a,b]=edges[index];bool selected=color[index]^((mask>>component[index])&1u);
      if(selected){assert(sigma[a]<0);sigma[a]=b;++sin[b];}else{assert(tau[b]<0);tau[b]=a;++tin[a];}
    }
    std::vector<int> starts,ends,end_label(n,-1),seen(n);
    for(int i=0;i<n;++i){assert(sin[i]<=1&&tin[i]<=1);assert((sin[i]==0)==(tin[i]==0));if(!sin[i])starts.push_back(i);}
    assert((int)starts.size()==e);bool valid=true;
    for(int start:starts){int v=start;
      while(v>=0){if(seen[v]){valid=false;break;}seen[v]=1;if(sigma[v]<0){ends.push_back(v);break;}v=sigma[v];}
      if(!valid)break;
    }
    if(!valid||std::accumulate(seen.begin(),seen.end(),0)!=n)continue;
    for(int i=0;i<e;++i)end_label[ends[i]]=i;
    std::fill(seen.begin(),seen.end(),0);std::vector<int> pi(e);
    for(int i=0;i<e&&valid;++i){int v=starts[i];
      while(true){if(seen[v]){valid=false;break;}seen[v]=1;if(tau[v]<0)break;v=tau[v];}
      if(valid){pi[i]=end_label[v];assert(pi[i]>=0);}
    }
    if(!valid||std::accumulate(seen.begin(),seen.end(),0)!=n)continue;++covers;
    std::vector<int> rest(e-1);std::iota(rest.begin(),rest.end(),1);
    do{std::vector<int> word{0};word.insert(word.end(),rest.begin(),rest.end());
      for(int shift=0;shift<e;++shift){std::vector<int> order(e),inv(e),relative(e);
        for(int i=0;i<e;++i){order[i]=word[(i+shift)%e];inv[order[i]]=i;}
        for(int i=0;i<e;++i)relative[i]=inv[pi[order[i]]];++histogram[permutation_index(relative)];
      }
    }while(std::next_permutation(rest.begin(),rest.end()));
  }return histogram;
}
Matrix skew(const Matrix& b){int r=b.size(),c=b[0].size();Matrix k(r+c,std::vector<int>(r+c));for(int i=0;i<r;++i)for(int j=0;j<c;++j){k[i][r+j]=b[i][j];k[r+j][i]=-b[i][j];}return k;}
void output_case(int id,int j,int g,int passive,long long denominator,const Matrix& k,int first_component=-1){
  int e=j+1,n=k.size()+passive;long long assignments=0,covers=0;auto hist=path_histogram(k,passive,e,assignments,covers);
  std::cout<<"{\"id\":"<<id<<",\"j\":"<<j<<",\"g\":"<<g<<",\"passive\":"<<passive<<",\"q\":"<<n<<",\"denominator\":"<<denominator<<",\"assignments\":"<<assignments<<",\"path_covers\":"<<covers<<",\"histogram\":[";
  for(unsigned i=0;i<hist.size();++i){if(i)std::cout<<',';std::cout<<hist[i];}std::cout<<"],\"fields\":[";
  for(unsigned f=0;f<primes.size();++f){int p=primes[f];Counts counts=first_component<0?connected_weight(k,p,g,passive):two_component_weight(k,first_component,p);
    long long weight=0;for(int i=0;i<7;++i)weight+=counts[i]*weights24[i];if(f)std::cout<<',';
    std::cout<<"{\"p\":"<<p<<",\"weight24\":"<<weight<<",\"type_counts\":[";
    for(int i=0;i<7;++i){if(i)std::cout<<',';std::cout<<counts[i];}std::cout<<"]}";
  }std::cout<<"]}\n";
}
int main(int argc,char** argv){assert(argc==2);std::ifstream input(argv[1]);assert(input);int count;input>>count;
  struct Graph{int id,g;long long denominator;Matrix k;};std::vector<Graph> graphs;std::vector<Graph> rank_one;
  for(int a=0;a<count;++a){int id,g,r,c;long long den;input>>id>>g>>r>>c>>den;Matrix b(r,std::vector<int>(c));for(auto& row:b)for(int& v:row)input>>v;
    graphs.push_back({id,g,den,skew(b)});if(g==1)rank_one.push_back(graphs.back());
  }
  assert(rank_one.size()==2);int serial=0;
  for(int j=1;j<=3;++j){int e=j+1;std::cout<<"{\"id\":"<<serial++<<",\"j\":"<<j<<",\"g\":0,\"passive\":"<<e<<",\"q\":"<<e<<",\"denominator\":"<<factorial(e)<<",\"assignments\":1,\"path_covers\":1,\"histogram\":[";
    for(int i=0;i<factorial(e);++i){if(i)std::cout<<',';std::cout<<(i==0?factorial(e):0);}std::cout<<"],\"fields\":[";
    Counts counts{};counts[j==1?1:j==2?2:4]=1;
    for(unsigned f=0;f<primes.size();++f){if(f)std::cout<<',';std::cout<<"{\"p\":"<<primes[f]<<",\"weight24\":"<<weights24[j==1?1:j==2?2:4]<<",\"type_counts\":[";for(int i=0;i<7;++i){if(i)std::cout<<',';std::cout<<counts[i];}std::cout<<"]}";}std::cout<<"]}\n";
    for(const auto& graph:graphs)if(graph.g<=j){int passive=j-graph.g;output_case(serial++,j,graph.g,passive,graph.denominator*factorial(passive),graph.k);}
    if(j==3)for(unsigned a=0;a<rank_one.size();++a)for(unsigned b=a;b<rank_one.size();++b){
      const auto& ka=rank_one[a].k;const auto& kb=rank_one[b].k;int na=ka.size(),nb=kb.size();Matrix k(na+nb,std::vector<int>(na+nb));
      for(int i=0;i<na;++i)for(int l=0;l<na;++l)k[i][l]=ka[i][l];for(int i=0;i<nb;++i)for(int l=0;l<nb;++l)k[na+i][na+l]=kb[i][l];
      long long den=rank_one[a].denominator*rank_one[b].denominator*(a==b?2:1);output_case(serial++,j,2,0,den,k,na);
    }
    std::cerr<<"order="<<j<<" complete; cases="<<serial<<'\n';
  }
}
