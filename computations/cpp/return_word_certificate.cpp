// Independent exact free-group and rational-support verification.
// A finite block model is separate from the smooth torus quantization proof.
#include <array>
#include <cstdlib>
#include <iostream>
#include <map>
#include <stdexcept>
#include <vector>
using Mat=std::array<std::array<long long,2>,2>;
using Vec=std::array<long long,2>;
Mat mul(Mat a,Mat b){Mat c{};for(int i=0;i<2;++i)for(int j=0;j<2;++j)for(int k=0;k<2;++k)c[i][j]+=a[i][k]*b[k][j];return c;}
long long dot(Vec a,Vec b){return a[0]*b[0]+a[1]*b[1];}
std::vector<int> reduce(std::vector<int> a){std::vector<int>b;for(int x:a){if(!b.empty()&&b.back()==-x)b.pop_back();else b.push_back(x);}return b;}
std::vector<int> inverse(std::vector<int>a){std::vector<int>b;for(auto i=a.rbegin();i!=a.rend();++i)b.push_back(-*i);return b;}
int main(){try{
 Mat s{{{3,4},{2,3}}},a{{{1,0},{0,1}}};int obligations=0;
 for(int k=1;k<=3;++k){a=mul(s,a);for(int sign:{-1,1}){
 Vec c{480*(a[0][0]-sign),480*a[1][0]};
 Vec rad{11*(1+std::abs(a[0][0])+std::abs(a[0][1])),11*(1+std::abs(a[1][0])+std::abs(a[1][1]))};
 const std::array<Vec,4>normals{{{1,0},{0,1},{-a[1][0],a[0][0]},{-a[1][1],a[0][1]}}};
 for(long long x=-300;x<=300;++x)for(long long y=-300;y<=300;++y){
 Vec d{1056*x-c[0],1056*y-c[1]};if(std::abs(d[0])>rad[0]||std::abs(d[1])>rad[1])continue;
 bool separated=false;for(Vec w:normals){long long rhs=11*(std::abs(w[0]*a[0][0]+w[1]*a[1][0])+std::abs(w[0]*a[0][1]+w[1]*a[1][1])+std::abs(w[0])+std::abs(w[1]));if(std::abs(dot(w,d))>rhs)separated=true;}
 if(!separated)throw std::runtime_error("support overlap");
 ++obligations;
 }}}
 if(obligations!=30)throw std::runtime_error("geometry count");
 int tests=0;
 for(int half=1;half<=11;++half){int l=2*half;std::vector<int>w;
 for(int j=1;j<=half;++j)w.push_back(j);
 for(int j=half;j>=1;--j)w.push_back(-j);
 std::vector<std::vector<int>>prefix;std::vector<int>p;
 for(int j=0;j<l-1;++j){p.insert(p.begin(),w[j]);p=reduce(p);prefix.push_back(p);}
 std::map<int,std::vector<int>>site;
 for(int j=0;j<l-1;++j)site[j]=prefix[j];
 for(int j=l-2;j>=0;--j){auto inv=inverse(prefix[j]);auto&z=site[j+1];z.insert(z.end(),inv.begin(),inv.end());}
 for(int j=0;j<l;++j)if(reduce(site[j])!=std::vector<int>{w[j]})throw std::runtime_error("return-word identity");
 ++tests;
 }
 std::array<int,4>bracket{0,-1,1,0},transfer{0,-1,0,0};
 for(int j=0;j<4;++j){int expected=transfer[j]-(j?transfer[j-1]:0);if(bracket[j]!=expected)throw std::runtime_error("bracket coboundary");}
 std::cout<<"{\"status\":\"PASS\",\"geometry_obligations\":"<<obligations<<",\"free_word_tests\":"<<tests<<",\"exact_bracket_coefficients\":[0,-1,1,0]}\n";
 return 0;
 }catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 1;}}
