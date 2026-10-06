#include <algorithm>
#include <array>
#include <functional>
#include <iostream>
#include <numeric>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>
using V=std::vector<int>;
struct Count {long partitions=0, matches=0;};
void combinations(int n,int k,const std::function<void(const V&)>& f){V a;std::function<void(int)> rec=[&](int lo){if((int)a.size()==k){f(a);return;}for(int j=lo;j<=n-(k-(int)a.size());++j){a.push_back(j);rec(j+1);a.pop_back();}};rec(0);}
void test(int n,const std::vector<V>& classes,bool triple,Count& total){
 V lab(n),t(n),ti(n),c(n);std::iota(lab.begin(),lab.end(),0);std::iota(t.begin(),t.end(),0);std::set<int>S;
 for(const V&cl:classes)for(int j=0;j<(int)cl.size();++j){lab[cl[j]]=cl[0];t[cl[j]]=cl[(j+1)%cl.size()];S.insert(cl[j]);}
 for(int i=0;i<n;++i){ti[t[i]]=i;c[i]=(i+n-1)%n;}
 ++total.partitions;
 combinations(n,4,[&](const V&H){
  std::set<int>labels;for(int j:H)labels.insert(lab[j]);if(labels.size()!=4)return;
  V h(n);std::iota(h.begin(),h.end(),0);std::swap(h[H[0]],h[H[2]]);std::swap(h[H[1]],h[H[3]]);
  V r(n),rp(n),Hp;for(int j=0;j<n;++j)r[j]=c[h[j]];for(int j=0;j<n;++j){rp[j]=t[r[ti[j]]];if(rp[j]!=c[j])Hp.push_back(j);}
  if(Hp.size()!=4) return;
  labels.clear();for(int j:Hp)labels.insert(lab[j]);if(labels.size()!=4)return;
  V hp(n);std::iota(hp.begin(),hp.end(),0);std::swap(hp[Hp[0]],hp[Hp[2]]);std::swap(hp[Hp[1]],hp[Hp[3]]);for(int j=0;j<n;++j)if(rp[j]!=c[hp[j]])return;
  if(H==Hp) throw std::runtime_error("identical heads");
  ++total.matches;
  if(triple)throw std::runtime_error("triple equality ambiguity");
  bool valid=false;
  for(int a=0;a<n;++a){std::set<int>s;for(int j=0;j<4;++j)s.insert((a+j)%n);if(s!=S)continue;
   if(lab[a]!=lab[(a+2)%n] || lab[(a+1)%n]!=lab[(a+3)%n] || lab[a]==lab[(a+1)%n])continue;
   for(int z=0;z<n;++z){std::set<int>h1{a,(a+1)%n,(a+4)%n,z},h2{a,(a+3)%n,(a+4)%n,z};std::set<int>sh(H.begin(),H.end()),sp(Hp.begin(),Hp.end());if(h1.size()==4&&h2.size()==4&&((sh==h1&&sp==h2)||(sh==h2&&sp==h1)))valid=true;}
  }
  if(!valid)throw std::runtime_error("nonlocal or unexpected local cut form");
 });
}
int main(){try{Count pair,triple;
 for(int n=5;n<=12;++n)combinations(n,4,[&](const V&v){test(n,{{v[0],v[1]},{v[2],v[3]}},false,pair);test(n,{{v[0],v[2]},{v[1],v[3]}},false,pair);test(n,{{v[0],v[3]},{v[1],v[2]}},false,pair);});
 for(int n=5;n<=10;++n)combinations(n,3,[&](const V&v){test(n,{v},true,triple);test(n,{{v[0],v[2],v[1]}},true,triple);});
 if(pair.partitions!=3859 || pair.matches!=560 || triple.partitions!=650 || triple.matches!=0) throw std::runtime_error("unexpected exhaustive totals");
 std::cout<<"{\"pairs\":{\"partitions\":"<<pair.partitions<<",\"directed_matches\":"<<pair.matches<<"},\"triple\":{\"oriented_cycles\":"<<triple.partitions<<",\"directed_matches\":"<<triple.matches<<"}}\n";
 }catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 1;}return 0;}
