#include <algorithm>
#include <array>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>

// Exact finite-field rank checks for distinct unoriented Hamiltonian cycles.
// Each cycle is represented with vertex 0 first and second vertex < last.
// No numerical or random arithmetic is used.
int mod(int x, int p) { x %= p; return x < 0 ? x+p : x; }
int rank_mod(std::vector<std::vector<int>> a, int p) {
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
int main() {
    bool first=true, all=true;
    std::cout << "{\"records\":[";
    for (int n=3; n<=10; ++n) {
        for (int p : {3,5}) {
            std::map<std::pair<int,int>,long long> counts;
            std::vector<int> tail(n-1);
            std::iota(tail.begin(),tail.end(),1);
            bool stronger=true;
            std::vector<int> counterexample;
            int minimum_slack=999, collision_slack=999;
            do {
                if (tail.front()>tail.back()) continue;
                std::vector<int> cycle={0};
                cycle.insert(cycle.end(),tail.begin(),tail.end());
                std::vector<std::vector<int>> a(n,std::vector<int>(n));
                for (int i=0; i<n; ++i) {
                    int j=(i+1)%n;
                    ++a[i][j]; ++a[j][i];
                    --a[cycle[i]][cycle[j]]; --a[cycle[j]][cycle[i]];
                }
                int b=0;
                for (int i=0; i<n; ++i) if (a[i][(i+1)%n]==1) ++b;
                int r=rank_mod(a,p);
                ++counts[{b,r}];
                if (b>0) {
                    all = all && b>=2 && r>=2 && 4*r>=b;
                    minimum_slack=std::min(minimum_slack,4*r-b);
                    if (2*r<b) {
                        stronger=false;
                        if (counterexample.empty()) counterexample=cycle;
                    }
                }
                if (n<=7) {
                    for (int u=0; u<n; ++u) for (int v=u+1; v<n; ++v) {
                        std::vector<int> id;
                        for (int i=0; i<n; ++i) if (i!=v) id.push_back(i);
                        std::vector<std::vector<int>> restricted(n-1,std::vector<int>(n-1));
                        for (int i=0; i<n-1; ++i) for (int j=0; j<n-1; ++j) {
                            int x=id[i],y=id[j];
                            restricted[i][j]=a[x][y]+(x==u?a[v][y]:0)+(y==u?a[x][v]:0)
                                             +(x==u && y==u?a[v][v]:0);
                        }
                        int rr=rank_mod(restricted,p);
                        all=all && rr>=r-2;
                        collision_slack=std::min(collision_slack,rr-r+2);
                    }
                }
            } while (std::next_permutation(tail.begin(),tail.end()));
            if (!first) std::cout << ',';
            first=false;
            std::cout << "{\"n\":" << n << ",\"p\":" << p
                      << ",\"rank_bound_passed\":" << (all?"true":"false")
                      << ",\"minimum_4r_minus_b\":" << minimum_slack
                      << ",\"observed_rank_at_least_b_over_2\":" << (stronger?"true":"false")
                      << ",\"counterexample\":[";
            for (std::size_t j=0; j<counterexample.size(); ++j) {
                if (j) std::cout << ',';
                std::cout << counterexample[j];
            }
            std::cout << "],\"minimum_collision_rank_slack\":";
            if (n<=7) std::cout << collision_slack; else std::cout << "null";
            std::cout << ",\"counts\":[";
            bool comma=false;
            for (auto const& [key,value]:counts) {
                if (comma) std::cout << ',';
                comma=true;
                std::cout << "[" << key.first << ',' << key.second << ',' << value << ']';
            }
            std::cout << "]}";
        }
    }
    std::cout << "],\"all_passed\":" << (all?"true":"false") << "}\n";
    return all?0:1;
}
