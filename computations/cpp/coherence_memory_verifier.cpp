// Exact finite Gaussian-integer endpoint witness and integer four-port core.
// This certifies no generic phase lemma, asymptotic law, or BGS theorem.
// All intermediate integers are bounded by 4096; no floating-point arithmetic.
#include <array>
#include <complex>
#include <cstdint>
#include <iostream>
#include <stdexcept>
using Z = std::complex<std::int64_t>;
template<std::size_t N> using M = std::array<std::array<Z,N>,N>;
template<std::size_t N> M<N> mul(const M<N>& a, const M<N>& b) {
  M<N> c{};
  for(std::size_t i=0;i<N;++i) for(std::size_t j=0;j<N;++j)
    for(std::size_t k=0;k<N;++k) c[i][j]+=a[i][k]*b[k][j];
  return c;
}
template<std::size_t N> M<N> adj(const M<N>& a) {
  M<N> b{};
  for(std::size_t i=0;i<N;++i) for(std::size_t j=0;j<N;++j)
    b[i][j]=std::conj(a[j][i]);
  return b;
}
template<std::size_t N> M<N> eye(std::int64_t scale=1) {
  M<N> a{};for(std::size_t i=0;i<N;++i)a[i][i]=scale;return a;
}
void require(bool condition) { if(!condition) throw std::runtime_error("exact control failed"); }
int main() {
  M<4> w{{{{1,1,1,1}},{{1,-1,-1,1}},{{1,1,-1,-1}},{{1,-1,1,-1}}}};
  require(mul(w,adj(w))==eye<4>(4));
  auto power=eye<4>();for(int k=0;k<6;++k)power=mul(power,w);
  require(power==eye<4>(64));
  M<4> reversal{};
  for(int i=0;i<4;++i)for(int j=0;j<4;++j)reversal[i][j]=w[i][j]*w[j][i];
  require(mul(reversal,adj(reversal))==eye<4>(4));
  // qubit U=g/2; its off-diagonal conjugation block E=b/4.
  M<2> g{{{{Z(1,-1),Z(-1,-1)}},{{Z(1,-1),Z(1,1)}}}};
  require(mul(g,adj(g))==eye<2>(4));
  for(const auto& row:g)for(auto x:row)require(std::norm(x)==2);
  std::array<std::array<int,2>,2> labels{{{{0,1}},{{1,0}}}};
  M<2> b{};
  for(int r=0;r<2;++r)for(int c=0;c<2;++c)
    b[r][c]=g[labels[r][0]][labels[c][0]]*std::conj(g[labels[r][1]][labels[c][1]]);
  require(b!=M<2>{} && mul(b,b)==M<2>{});
  auto gram=mul(adj(b),b);
  require(gram[0][0]+gram[1][1]==Z(16));
  require(gram[0][0]*gram[1][1]-gram[0][1]*gram[1][0]==Z(0));
  // Thus singular values of E are exactly 1,0, while E^2=0.
  std::cout << "{\"status\":\"pass\",\"arithmetic\":\"Gaussian integers\","
               "\"core_order_divides\":6,\"reversal_gram_scale\":4,"
               "\"endpoint_dimension\":2,\"coherence_singular_values\":[1,0],"
               "\"coherence_square_zero\":true,\"scope\":\"finite identities only\"}\n";
}
