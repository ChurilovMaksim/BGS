#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <stdexcept>
#include <vector>

// Exact coefficients through N^{-2}, for Fourier(F_p^d), d divisible by 4.
// No fitting or floating point: 12 times every relevant partition weight
// is an integer. Unoriented Hamilton cycles have multiplicity 2*n.
using Matrix = std::vector<std::vector<int>>;
int mod(int x, int p) { x %= p; return x < 0 ? x+p : x; }
int rank_mod(Matrix a, int p) {
    int n=static_cast<int>(a.size()), r=0;
    for (int col=0; col<n && r<n; ++col) {
        int pivot=r;
        while (pivot<n && mod(a[pivot][col],p)==0) ++pivot;
        if (pivot==n) continue;
        std::swap(a[r],a[pivot]);
        int inverse=1;
        while (mod(inverse*a[r][col],p)!=1) ++inverse;
        for (int j=col; j<n; ++j) a[r][j]=mod(a[r][j]*inverse,p);
        for (int i=r+1; i<n; ++i) {
            int z=mod(a[i][col],p);
            for (int j=col; j<n; ++j) a[i][j]=mod(a[i][j]-z*a[r][j],p);
        }
        ++r;
    }
    return r;
}
Matrix quotient(const Matrix& a, const std::vector<int>& labels, int p) {
    int m=*std::max_element(labels.begin(),labels.end())+1;
    Matrix out(m,std::vector<int>(m));
    for (int i=0; i<static_cast<int>(a.size()); ++i)
        for (int j=0; j<static_cast<int>(a.size()); ++j)
            out[labels[i]][labels[j]]=mod(out[labels[i]][labels[j]]+a[i][j],p);
    return out;
}
std::vector<int> labels_for(int n, const std::vector<std::vector<int>>& blocks) {
    std::vector<int> parent(n),labels(n,-1);
    std::iota(parent.begin(),parent.end(),0);
    for (const auto& b:blocks) for (int i:b) parent[i]=b.front();
    int k=0;
    std::map<int,int> ids;
    for (int i=0; i<n; ++i) {
        if (!ids.count(parent[i])) ids[parent[i]]=k++;
        labels[i]=ids[parent[i]];
    }
    return labels;
}
bool zero(const Matrix& a) {
    for (const auto& row:a) for (int v:row) if (v) return false;
    return true;
}
int main(int argc,char** argv) {
    int limit=argc>1 ? std::stoi(argv[1]):10;
    if (limit<3 || limit>10) throw std::runtime_error("limit must be 3..10");
    bool first=true, all=true;
    std::cout << "{\"scope\":\"Exact finite coefficients; d divisible by 4; no extrapolation in n\",\"cases\":[";
    for (int n=3; n<=limit; ++n) {
        std::vector<std::pair<std::vector<int>,int>> collision_two;
        for (int a=0;a<n;++a) for (int b=a+1;b<n;++b) for (int c=b+1;c<n;++c)
            collision_two.push_back({labels_for(n,{{a,b,c}}),8});
        for (int a=0;a<n;++a) for (int b=a+1;b<n;++b)
            for (int c=b+1;c<n;++c) for (int e=c+1;e<n;++e) {
                collision_two.push_back({labels_for(n,{{a,b},{c,e}}),3});
                collision_two.push_back({labels_for(n,{{a,c},{b,e}}),3});
                collision_two.push_back({labels_for(n,{{a,e},{b,c}}),3});
            }
        for (int p:{3,5,7}) {
            std::array<std::int64_t,5> numerator{};
            std::array<std::array<std::int64_t,5>,3> by_h{};
            std::map<int,std::int64_t> ranks;
            std::vector<int> tail(n-1);
            std::iota(tail.begin(),tail.end(),1);
            std::int64_t cycles=0, restrictions=0;
            do {
                if (tail.front()>tail.back()) continue;
                std::vector<int> cycle={0}; cycle.insert(cycle.end(),tail.begin(),tail.end());
                Matrix a(n,std::vector<int>(n));
                for (int i=0;i<n;++i) {
                    int j=(i+1)%n;
                    ++a[i][j]; ++a[j][i];
                    --a[cycle[i]][cycle[j]]; --a[cycle[j]][cycle[i]];
                }
                int r=rank_mod(a,p); ++ranks[r]; ++cycles;
                int active=0;
                std::vector<bool> is_active(n,false);
                for (int i=0;i<n;++i) {
                    const auto& row=a[i];
                    is_active[i]=std::any_of(row.begin(),row.end(),[&](int v){return mod(v,p)!=0;});
                    if (is_active[i]) ++active;
                }
                all=all && active<=4*r;
                int active_runs=0;
                for (int i=0;i<n;++i) if (is_active[i]) {
                    all=all && (is_active[(i+n-1)%n] || is_active[(i+1)%n]);
                    if (!is_active[(i+n-1)%n]) ++active_runs;
                }
                all=all && 2*active_runs<=active && active_runs<=2*r;
                if (r<=4) {
                    numerator[r]+=12; by_h[0][r]+=12;
                    for (int u=0;u<n;++u) for (int v=u+1;v<n;++v) {
                        int rr=rank_mod(quotient(a,labels_for(n,{{u,v}}),p),p);
                        all=all && rr>=r-2;
                        if (r==2) all=all && rr!=1;
                        ++restrictions;
                        if (2+rr<=4) {numerator[2+rr]-=6; by_h[1][2+rr]-=6;}
                    }
                    for (const auto& [labels,weight]:collision_two) {
                        ++restrictions;
                        if (zero(quotient(a,labels,p))) {numerator[4]+=weight; by_h[2][4]+=weight;}
                    }
                }
            } while (std::next_permutation(tail.begin(),tail.end()));
            all=all && numerator[0]*2*n==24*n;
            std::int64_t target=n==3?-9:(n==4?-24:-2*n*n);
            all=all && numerator[2]*2*n==12*target;
            if (n>=5) all=all && ranks[2]==n*(n-4);
            if (p==3 && n<=6) {
                // d=0 mod 4 here. The earlier d=1 mod 4 polynomial has
                // coefficient 165, not 185, at n=5: Gaussian signs matter.
                std::array<int,7> known={0,0,0,4,42,185,390};
                all=all && numerator[4]*2*n==12*known[n];
            }
            if (!first) std::cout << ',';
            first=false;
            std::cout << "{\"n\":"<<n<<",\"p\":"<<p<<",\"cycles\":"<<cycles
                      <<",\"collision_restrictions\":"<<restrictions
                      <<",\"coefficient_denominator\":12,\"coefficient_numerators\":[";
            for (int e=0;e<=4;++e) {if(e)std::cout<<',';std::cout<<numerator[e]*2*n;}
            std::cout << "],\"by_h_numerators\":[";
            for (int h=0;h<=2;++h) {if(h)std::cout<<',';std::cout<<'[';
                for (int e=0;e<=4;++e) {if(e)std::cout<<',';std::cout<<by_h[h][e]*2*n;}std::cout<<']';}
            std::cout << "],\"rank_counts\":["; bool comma=false;
            for (const auto& [r,count]:ranks) {if(comma)std::cout<<',';comma=true;std::cout<<'['<<r<<','<<count<<']';}
            std::cout << "]}";
        }
    }
    std::cout << "],\"all_passed\":"<<(all?"true":"false")<<"}\n";
    return all?0:1;
}
