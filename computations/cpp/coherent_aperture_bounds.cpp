// Exact finite arithmetic checks for the aperture-minimax proof.
// This checks scalar certificates, not the analytic/statistical theorem.
#include <boost/multiprecision/cpp_int.hpp>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using Z = boost::multiprecision::cpp_int;

Z power(Z base, unsigned n) {
    Z value = 1;
    while (n) {
        if (n & 1U) value *= base;
        base *= base;
        n >>= 1U;
    }
    return value;
}
Z factorial(unsigned n) {
    Z value = 1;
    for (unsigned j = 2; j <= n; ++j) value *= j;
    return value;
}
Z absz(const Z& x) { return x < 0 ? -x : x; }
void require(bool b, const char* text) {
    if (!b) throw std::runtime_error(text);
}
void bias_check(unsigned s, unsigned k, unsigned sn, unsigned sd) {
    require(s > 0 && s <= 16 && k > 0 && k <= 64 && sn > 0 && sd > 0,
            "invalid certificate parameters");
    require(Z(sn) <= Z(k)*sd, "squared radius exceeds cutoff");
    const unsigned L = 128*s*k;
    Z anum = factorial(k)*power(Z(2*s)*sd, k);
    Z aden = power(Z(sn), k);
    if (anum < aden) anum = aden;
    const Z numerator = power(Z(9), L)*anum*anum*power(Z(2)*sn, L+1)
                      *power(Z(2), 2*(64*s-1)*k);
    const Z denominator = aden*aden*power(Z(sd), L+1)*factorial(L+1);
    require(numerator <= denominator, "factorial bias bound failed");
    for (unsigned j=0; j<=k; ++j) {
        const Z lhs = factorial(j)*power(Z(2*s)*sd, j)*aden;
        const Z rhs = power(Z(sn), j)*anum;
        require(lhs <= rhs, "log-convex endpoint bound failed");
    }
    for (unsigned j: {L, L+1, 2*L, 5*L})
        require(Z(8)*sn*(j+2*s) <= Z(sd)*(j+1)*(j+1),
                "Taylor-tail ratio failed");
}
int main(int argc, char** argv) {
    try {
        unsigned bias_cases = 0;
        if (argc == 1) {
            for (unsigned s: {1U,2U,3U,5U})
                for (unsigned k=1; k<=4; ++k)
                    for (unsigned divisor: {1U,2U,17U,100U}) {
                        bias_check(s,k,k,divisor);
                        ++bias_cases;
                    }
        } else {
            require(argc == 2, "usage: coherent_aperture_bounds [packet]");
            std::ifstream in(argv[1]);
            require(bool(in), "cannot open certificate packet");
            unsigned n;
            require(bool(in>>n) && n>0 && n<=10000, "invalid certificate count");
            for (unsigned j=0; j<n; ++j) {
                unsigned s,k,sn,sd;
                require(bool(in>>s>>k>>sn>>sd), "truncated certificate");
                bias_check(s,k,sn,sd);
                ++bias_cases;
            }
            std::string extra;
            require(!(in>>extra), "trailing certificate data");
        }
        // Independent integer Chebyshev recurrence and coefficient l1 bound.
        std::vector<Z> previous{1}, current{0,1};
        unsigned chebyshev_cases=2;
        for (unsigned n=2; n<=512; ++n) {
            std::vector<Z> next(current.size()+1);
            for (unsigned j=0; j<current.size(); ++j) next[j+1]+=2*current[j];
            for (unsigned j=0; j<previous.size(); ++j) next[j]-=previous[j];
            Z l1=0; for (const auto& x:next) l1+=absz(x);
            require(l1<=power(Z(3),n), "Chebyshev coefficient bound failed");
            previous=current; current=next; ++chebyshev_cases;
        }
        Z central=1;
        unsigned binomial_cases=0;
        for (unsigned k=1; k<=2048; ++k) {
            Z numerator=central*2*(2*k-1);
            require(numerator%k==0, "binomial recurrence not integral");
            central=numerator/k;
            require(central*(2*k+1)>=power(Z(2),2*k), "central-binomial bound failed");
            ++binomial_cases;
        }
        bool rejected=false;
        try { bias_check(1,1,2,1); } catch(const std::runtime_error&) { rejected=true; }
        require(rejected, "negative control accepted");
        std::cout << "PASS exact-bias=" << bias_cases
                  << " chebyshev=" << chebyshev_cases
                  << " central-binomial=" << binomial_cases
                  << " negative-controls=1\n";
    } catch (const std::exception& error) {
        std::cerr << "FAIL " << error.what() << '\n';
        return 1;
    }
    return 0;
}
