// Exploratory Monte Carlo for the EXACT Ewens/one-circuit Wick measure.
// Finite sampling only: never a proof of asymptotics or a certified bound.
// g++ -std=c++20 -O3 sample_conditioned_ewens.cpp -o /tmp/bgs_ewens_sample
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <random>
#include <unordered_map>
#include <vector>

int main(int argc, char** argv) {
    const int N=argc>1?std::stoi(argv[1]):100;
    const int m=argc>2?std::stoi(argv[2]):N;
    const int target=argc>3?std::stoi(argv[3]):10000;
    const uint64_t seed=argc>4?std::stoull(argv[4]):20261016;
    std::mt19937_64 gen(seed);
    std::vector<int> sigma(m), colour(m), counts(N*N);
    uint64_t trials=0;
    long double sc=0, sc2=0, sr=0, sr2=0, sf2=0, sf3=0, sf4=0;
    int accepted=0, triples=0;
    while(accepted<target) {
        ++trials;
        for(int j=0;j<m;++j) {
            const int k=std::uniform_int_distribution<int>(0,N+j-1)(gen);
            if(k<N) sigma[j]=j;
            else { const int i=k-N; sigma[j]=sigma[i]; sigma[i]=j; }
        }
        int i=0, len=0;
        do { i=(sigma[i]+1)%m; ++len; } while(i!=0);
        if(len!=m) continue;
        std::fill(colour.begin(),colour.end(),-1);
        for(int j=0;j<m;++j) if(colour[j]<0) {
            const int c=std::uniform_int_distribution<int>(0,N-1)(gen);
            int k=j;
            do { colour[k]=c; k=sigma[k]; } while(k!=j);
        }
        std::fill(counts.begin(),counts.end(),0);
        long double cc=0, invd=1;
        bool triple=false;
        for(int j=0;j<m;++j) {
            const int e=colour[j]*N+colour[(j+1)%m];
            cc+=counts[e];
            ++counts[e];
            invd/=counts[e];
            triple|=counts[e]>=3;
        }
        ++accepted;
        triples+=triple;
        sc+=cc; sc2+=cc*cc; sr+=invd; sr2+=invd*invd;
        sf2+=cc*(cc-1); sf3+=cc*(cc-1)*(cc-2); sf4+=cc*(cc-1)*(cc-2)*(cc-3);
    }
    long double ec=sc/target, er=sr/target;
    std::cout<<std::setprecision(12)
      <<"{\"N\":"<<N<<",\"m\":"<<m<<",\"accepted\":"<<target
      <<",\"trials\":"<<trials<<",\"seed\":"<<seed
      <<",\"mean_C\":"<<ec<<",\"se_mean_C\":"<<sqrtl(std::max(0.L,sc2/target-ec*ec)/target)
      <<",\"mean_inverse_factorial\":"<<er
      <<",\"se_mean_inverse_factorial\":"<<sqrtl(std::max(0.L,sr2/target-er*er)/target)
      <<",\"factorial_C_2\":"<<sf2/target<<",\"factorial_C_3\":"<<sf3/target
      <<",\"factorial_C_4\":"<<sf4/target<<",\"triple_edge_samples\":"<<triples
      <<",\"nonclaim\":\"Exploratory Monte Carlo only\"}\n";
}
