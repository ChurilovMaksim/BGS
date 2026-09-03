#include <algorithm>
#include <boost/multiprecision/cpp_int.hpp>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

using boost::multiprecision::cpp_int;

namespace relation {
constexpr int TRACE = 3;
constexpr int DISC = 5;

struct State {
    int a;
    int b;
    int cost;
    bool operator==(const State& o) const noexcept { return a == o.a && b == o.b && cost == o.cost; }
};
struct StateHash {
    std::size_t operator()(const State& s) const noexcept {
        std::size_t h = static_cast<std::uint32_t>(s.a) * 0x9e3779b1u;
        h ^= static_cast<std::uint32_t>(s.b) + 0x9e3779b9u + (h << 6) + (h >> 2);
        h ^= static_cast<std::uint32_t>(s.cost) + 0x85ebca6bu + (h << 6) + (h >> 2);
        return h;
    }
};

inline std::pair<int,int> trans(int a, int b, int c) { return {-b, a - c + TRACE*b}; }

inline bool le_sqrt(int B, int D) {
    if (B <= 0 && D >= 0) return true;
    if (B > 0 && D < 0) return false;
    boost::multiprecision::int128_t lhs = boost::multiprecision::int128_t(DISC) * B * B;
    boost::multiprecision::int128_t rhs = boost::multiprecision::int128_t(D) * D;
    return B > 0 ? lhs <= rhs : lhs >= rhs;
}

inline bool value_ok(int a, int b, int rem) {
    if (rem < 0) return false;
    int A = 2*a + TRACE*b;
    int M = 2*rem;
    return le_sqrt(b, M - A) && le_sqrt(-b, A + M);
}

std::vector<cpp_int> dense_counts(int rmax, int pmax = -1) {
    if (pmax < 0) pmax = rmax;
    std::unordered_map<State, cpp_int, StateHash> dp, next;
    dp.reserve(static_cast<std::size_t>(rmax) * 32);
    for (int c = 1; c <= rmax; ++c) {
        auto [a2,b2] = trans(0,0,c);
        if (!value_ok(a2,b2,rmax-c)) continue;
        dp[{a2,b2,c}] += 1;
    }
    std::vector<cpp_int> dense(rmax+1);
    for (int p = 1; p < pmax; ++p) {
        next.clear();
        next.reserve(dp.size()*2 + 32);
        int width = p + 1;
        for (const auto& kv : dp) {
            const State& s = kv.first;
            const cpp_int& count = kv.second;
            auto [a0,b0] = trans(s.a,s.b,0);
            if (value_ok(a0,b0,rmax-s.cost)) next[{a0,b0,s.cost}] += count;
            int rem = rmax - s.cost;
            for (int c = -rem; c <= rem; ++c) {
                if (c == 0) continue;
                int cost2 = s.cost + std::abs(c);
                auto [a2,b2] = trans(s.a,s.b,c);
                if (!value_ok(a2,b2,rmax-cost2)) continue;
                if (a2 == 0 && b2 == 0 && width <= cost2) dense[cost2] += count;
                next[{a2,b2,cost2}] += count;
            }
        }
        dp.swap(next);
        if (dp.empty()) break;
    }
    return dense;
}

bool glue_check(const std::vector<cpp_int>& s) {
    int rmax = static_cast<int>(s.size()) - 1;
    for (int r1=5;r1<=rmax;++r1) for (int r2=r1;r2<=rmax;++r2) {
        if (r1+r2>rmax || s[r1]==0 || s[r2]==0) continue;
        if (s[r1+r2] < s[r1]*s[r2]) return false;
    }
    return true;
}

using Series = std::vector<double>;
Series multiply(const Series& x,const Series& y,int L) {
    Series out(L,0.0);
    for(int i=0;i<L;++i) if(x[i]!=0.0)
        for(int j=0;j+i<L;++j) if(y[j]!=0.0) out[i+j]+=x[i]*y[j];
    return out;
}
Series I_series(int a,int L) {
    Series s(L,0.0);
    for(int k=0;2*k+a<L;++k) s[2*k+a]=std::exp(-std::lgamma(k+1.0)-std::lgamma(k+a+1.0));
    return s;
}
Series J_series(int c,int L) {
    Series num=I_series(std::abs(c),L), den=I_series(0,L), out(L,0.0);
    for(int d=0;d<L;++d){
        double acc=num[d];
        for(int e=0;e<d;++e) acc-=den[e+1]*out[d-e-1];
        out[d]=acc;
    }
    return out;
}
Series I0_power(int K,int L) {
    Series result(L,0.0); result[0]=1.0;
    Series base=I_series(0,L);
    int e=K;
    while(e){ if(e&1) result=multiply(result,base,L); base=multiply(base,base,L); e>>=1; }
    return result;
}

using VMap = std::unordered_map<State,Series,StateHash>;
Series bessel_dp(int rmax,int width_cap) {
    int L=rmax+1;
    std::vector<Series> jcache(rmax+1);
    for(int c=1;c<=rmax;++c) jcache[c]=J_series(c,L);
    VMap dp,next;
    for(int c=1;c<=rmax;++c){
        auto [a2,b2]=trans(0,0,c);
        if(!value_ok(a2,b2,rmax-c)) continue;
        dp.emplace(State{a2,b2,c},jcache[c]);
    }
    Series psi(L,0.0);
    for(int p=1;p<width_cap;++p){
        next.clear();
        for(const auto& kv:dp){
            const State& s=kv.first; const Series& wt=kv.second;
            auto add=[&](const State& key,const Series& val){
                auto it=next.find(key);
                if(it==next.end()) next.emplace(key,val);
                else for(int i=0;i<L;++i) it->second[i]+=val[i];
            };
            auto [a0,b0]=trans(s.a,s.b,0);
            if(value_ok(a0,b0,rmax-s.cost)) add({a0,b0,s.cost},wt);
            int rem=rmax-s.cost;
            for(int c=-rem;c<=rem;++c){
                if(c==0) continue;
                int cost2=s.cost+std::abs(c);
                auto [a2,b2]=trans(s.a,s.b,c);
                if(!value_ok(a2,b2,rmax-cost2)) continue;
                Series wt2=multiply(wt,jcache[std::abs(c)],L);
                if(a2==0 && b2==0) for(int i=0;i<L;++i) psi[i]+=wt2[i];
                add({a2,b2,cost2},wt2);
            }
        }
        dp.swap(next);
        if(dp.empty()) break;
    }
    return psi;
}

double X_moment(int K,int r,const Series& psi){
    int L=static_cast<int>(psi.size());
    Series i0=I0_power(K,L);
    double s=0.0;
    for(int d=0;d<=r;++d) s+=i0[d]*psi[r-d];
    return 2.0*K*std::exp(std::lgamma(r+1.0))*s;
}

constexpr double LAMP=(3.0-std::sqrt(5.0))/2.0;
struct Pair { int a,b; bool operator==(const Pair&o)const noexcept{return a==o.a&&b==o.b;} };
struct PairHash{std::size_t operator()(const Pair&s)const noexcept{return (static_cast<std::uint32_t>(s.a)*0x9e3779b1u)^static_cast<std::uint32_t>(s.b);}};
inline double val(const Pair&s){return s.a+s.b*LAMP;}
inline Pair trans_contract(const Pair&s,int c){return {c-s.b,s.a+3*s.b};}
std::vector<Pair> ellipse_states(int B){
    std::vector<Pair> st;
    int bm=static_cast<int>(std::ceil(B/LAMP));
    for(int b=-bm;b<=bm;++b){
        int lo=static_cast<int>(std::ceil(-B-b*LAMP-1e-9));
        int hi=static_cast<int>(std::floor(B-b*LAMP+1e-9));
        for(int a=lo;a<=hi;++a) st.push_back({a,b});
    }
    return st;
}
double transfer_perron(int B,double x,int iters=300){
    auto st=ellipse_states(B); int n=static_cast<int>(st.size());
    std::unordered_map<Pair,int,PairHash> index; index.reserve(st.size()*2);
    for(int i=0;i<n;++i) index[st[i]]=i;
    std::vector<std::vector<std::pair<int,double>>> rows(n);
    for(int i=0;i<n;++i){
        double v0=LAMP*val(st[i]);
        int lo=static_cast<int>(std::ceil(-B-v0-1e-9));
        int hi=static_cast<int>(std::floor(B-v0+1e-9));
        for(int c=lo;c<=hi;++c){
            Pair s2=trans_contract(st[i],c);
            if(std::abs(val(s2))>B*(1+1e-12)+1e-9) continue;
            auto it=index.find(s2); if(it==index.end()) continue;
            rows[i].push_back({it->second,std::pow(x,std::abs(c))});
        }
    }
    std::vector<double> v(n,1.0/std::sqrt(static_cast<double>(n))),w(n);
    double rho=0.0;
    for(int it=0;it<iters;++it){
        std::fill(w.begin(),w.end(),0.0);
        for(int i=0;i<n;++i) for(auto [j,wt]:rows[i]) w[i]+=wt*v[j];
        rho=0.0; for(double z:w) rho+=z*z; rho=std::sqrt(rho);
        if(rho==0.0) return 0.0;
        for(int i=0;i<n;++i) v[i]=w[i]/rho;
    }
    return rho;
}
std::pair<double,int> dense_constant(int B){
    double lo=.30,hi=.70;
    if(transfer_perron(B,lo)>1.0 || transfer_perron(B,hi)<1.0) throw std::runtime_error("legacy transfer bracket fails because zero-cost self-loop keeps rho >= 1");
    for(int i=0;i<60 && hi-lo>1e-10;++i){
        double mid=(lo+hi)/2;
        if(transfer_perron(B,mid)<=1.0) lo=mid; else hi=mid;
    }
    double x=(lo+hi)/2;
    return {1.0/x,static_cast<int>(ellipse_states(B).size())};
}

bool verify(){
    static const std::vector<std::pair<int,const char*>> anchors={
        {5,"1"},{8,"3"},{10,"23"},{20,"67815"},{30,"301160711"},
        {40,"1486136914085"},{50,"7639873992151089"},{56,"1303090486143334566"}
    };
    auto s=dense_counts(56);
    bool ok=glue_check(s);
    for(auto [r,txt]:anchors){ cpp_int want(txt); if(s[r]!=want){std::cerr<<"anchor mismatch R="<<r<<" got="<<s[r]<<" want="<<want<<"\n";ok=false;} }
    Series psi=bessel_dp(12,17);
    static const std::vector<std::pair<int,double>> banchors={{6,6120.0},{8,5464480.0},{10,3901524480.0}};
    for(auto [r,want]:banchors){ double got=X_moment(17,r,psi); double rel=std::abs(got-want)/want; if(rel>1e-9){std::cerr<<"Bessel mismatch r="<<r<<" rel="<<rel<<"\n";ok=false;} }
    double rho_lo=transfer_perron(4,0.30);
    if(rho_lo<=1.0){std::cerr<<"legacy transfer falsifier unexpectedly passed\n";ok=false;}
    std::cout<<(ok?"PASS":"FAIL")<<" relation-automaton regression; legacy cdense bracket="<<(rho_lo>1.0?"FALSIFIED":"unexpected")<<"\n";
    return ok;
}
}

int main(int argc,char**argv){
    using namespace relation;
    if(argc<2){std::cerr<<"usage: relation_automaton {verify|count R|bessel K RMAX|legacy-transfer-falsifier B}\n";return 2;}
    std::string cmd=argv[1];
    if(cmd=="verify") return verify()?0:1;
    if(cmd=="count"){
        if(argc!=3) return 2;
        int R=std::stoi(argv[2]);
        auto s=dense_counts(R);
        for(int r=5;r<=R;++r) if(s[r]!=0) std::cout<<r<<" "<<s[r]<<"\n";
        std::cerr<<"glue="<<(glue_check(s)?"PASS":"FAIL")<<"\n"; return 0;
    }
    if(cmd=="bessel"){
        if(argc!=4) return 2;
        int K=std::stoi(argv[2]);
        int R=std::stoi(argv[3]);
        auto psi=bessel_dp(R,K);
        for(int r=6;r<=R;r+=2) std::cout<<r<<" "<<std::setprecision(17)<<X_moment(K,r,psi)<<"\n";
        return 0;
    }
    if(cmd=="legacy-transfer-falsifier") {
        if(argc!=3) return 2;
        int B=std::stoi(argv[2]);
        const double rlo=transfer_perron(B,0.30);
        const double rhi=transfer_perron(B,0.70);
        std::cout << "B=" << B << " rho(0.30)=" << std::setprecision(12) << rlo
                  << " rho(0.70)=" << rhi << "\n";
        const bool bracket = rlo <= 1.0 && rhi >= 1.0;
        std::cout << "legacy_bracket=" << (bracket?"PASS":"FAIL_AS_EXPECTED") << "\n";
        return bracket ? 1 : 0;
    }
    return 2;
}
