// Adapted prefix of primitive_defect.cpp; only the include path is changed.
#define main prior_open_second_main
#include "prior_open_second.cpp"
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
