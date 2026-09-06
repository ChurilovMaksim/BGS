// Exact independent two-species pair audit in Z[sqrt(2)]/(N).
// Python uses original T-coordinate vectors; this program divides out the
// common factor 4+2sqrt(2), and iterates multiplication by 3+2sqrt(2).
// Regression evidence, not a proof for all primes.
#include <boost/multiprecision/cpp_int.hpp>
#include <array>
#include <iostream>
#include <map>
#include <stdexcept>
#include <utility>
#include <vector>
using Z = boost::multiprecision::cpp_int;
using Pair = std::pair<Z,Z>;

Z mod(Z x, const Z& n) { x %= n; if(x<0) x+=n; return x; }
Pair pell(int k) {
  Z n=1,f=0;
  for(int j=0;j<k;++j) { Z a=n+2*f; f=n+f; n=a; }
  return {n,f};
}
Pair step(const Pair& x,const Z& n) {
  return {mod(3*x.first+4*x.second,n),mod(2*x.first+3*x.second,n)};
}
void check(int k) {
  const auto [n,f]=pell(k);
  if(n*n-2*f*f != -1) throw std::runtime_error("Pell norm");
  std::array<std::vector<Pair>,2> v;
  for(int a=0;a<2;++a) {
    Pair x=a==0?Pair{1,0}:Pair{0,1};
    for(int j=0;j<k;++j) { v[a].push_back(x); x=step(x,n); }
    if(x!=v[a][0]) throw std::runtime_error("period");
  }
  // norm(4+2sqrt(2))=8 is a unit modulo every odd N, so this
  // cancellation preserves equality of the original vector keys.
  std::map<Pair,int> bins;
  for(int t=0;t<k;++t) for(int s=t+1;s<k;++s)
    for(int a=0;a<2;++a) for(int b=0;b<2;++b)
      for(int e : {-1,1}) for(int g : {-1,1}) {
        Pair x{mod(e*v[a][t].first+g*v[b][s].first,n),
               mod(e*v[a][t].second+g*v[b][s].second,n)};
        ++bins[x];
      }
  std::map<int,int> hist;
  for(const auto& [key,count] : bins) { (void)key; ++hist[count]; }
  if(k>=11 && (bins.count(Pair{0,0}) || hist.rbegin()->first!=2 ||
               hist[2]!=4*k || hist[1]!=8*k*(k-2)))
    throw std::runtime_error("two-species multiplicity classification");
  std::cout << "{\"K\":" << k << ",\"N\":\"" << n
    << "\",\"term_count\":" << 8*k*(k-1)
    << ",\"unique_keys\":" << bins.size() << ",\"multiplicity_histogram\":{";
  bool comma=false;
  for(const auto& [m,c] : hist) { if(comma) std::cout << ','; comma=true;
    std::cout << '\"' << m << "\":" << c; }
  std::cout << "}}";
}
int main() {
  try {
    std::cout << "{\"checks\":["; bool comma=false;
    for(int k : {3,5,7,11,13,17,23,31,47,101}) {
      if(comma) std::cout << ',';
      comma=true;
      check(k);
    }
    std::cout << "]}\n";
    return 0;
  } catch(const std::exception& e) { std::cerr << e.what() << '\n'; return 1; }
}
