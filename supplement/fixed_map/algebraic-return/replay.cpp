// Exact certificate replay, independent of NumPy and the candidate generator.
// Compile with g++ -std=c++20 -O3 -Wall -Wextra -Werror; assertions are not used.
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>
using I = std::int64_t;
using V = std::vector<I>;
struct Coeff { I a, b, re, im; };
void require(bool b, const std::string& why) { if (!b) throw std::runtime_error(why); }
I mod(I x, I p) { x %= p; return x < 0 ? x+p : x; }
I power(I a, I b, I p) {
    I result=1;
    while (b) { if (b&1) result=result*a%p; a=a*a%p; b>>=1; }
    return result;
}
bool prime(I p) {
    if(p<2) return false;
    for(I d=2;d*d<=p;++d) if(p%d==0) return false;
    return true;
}
I inverse(I a, I p) { require(mod(a,p)!=0,"zero denominator"); return power(mod(a,p),p-2,p); }
void trim(V& a) { while(!a.empty() && a.back()==0) a.pop_back(); }
V rem(V a, V b, I p) {
    trim(a); trim(b); require(!b.empty(),"zero polynomial divisor");
    I inv=inverse(b.back(),p);
    while(a.size()>=b.size()) {
        I factor=a.back()*inv%p;
        std::size_t offset=a.size()-b.size();
        for(std::size_t j=0;j<b.size();++j) a[offset+j]=mod(a[offset+j]-factor*b[j],p);
        trim(a);
    }
    return a;
}
V gcd(V a, V b, I p) {
    trim(a); trim(b);
    while(!b.empty()) { V r=rem(a,b,p); a=b; b=r; }
    if(a.empty()) return a;
    I inv=inverse(a.back(),p);
    for(I& x:a) x=x*inv%p;
    return a;
}
V matvec(const V& B,const V& v,I n,I p) {
    V result(n);
    for(I i=0;i<n;++i) {
        I sum=0;
        for(I j=0;j<n;++j) sum+=B[i*n+j]*v[j];
        result[i]=sum%p;
    }
    return result;
}
void read_vector(std::istream& in,V& v,I p) {
    for(I& x:v) { require(bool(in>>x),"truncated vector"); require(0<=x && x<p,"noncanonical residue"); }
}

int main(int argc,char** argv) try {
    require(argc==2,"usage: replay certificates.txt");
    std::ifstream in(argv[1]); require(bool(in),"cannot open certificate");
    I count,den; require(bool(in>>count>>den),"missing coefficient header");
    require(count==33 && den==4000,"unexpected frozen coefficient format");
    std::vector<Coeff> coeff(count);
    for(auto& c:coeff) require(bool(in>>c.a>>c.b>>c.re>>c.im),"truncated coefficients");
    I cases; require(bool(in>>cases),"missing case count");
    for(I test=0;test<cases;++test) {
        I n,p,r,ordinary,weight,zeta,imag;
        require(bool(in>>n>>p>>r>>ordinary>>weight>>zeta>>imag),"truncated case");
        require(n>=3 && n%2==1 && r>=1,"invalid dimension/period");
        require(prime(p) && (p-1)%(4*n)==0,"prime does not split cyclotomic coefficients");
        require((__int128)n*(p-1)*(p-1)<std::numeric_limits<I>::max(),"overflow risk");
        require(mod(den*r*n,p)!=0,"bad reduction denominator");
        require(power(imag,2,p)==p-1 && power(zeta,n,p)==1,"incorrect roots");
        for(I d=1;d<n;++d) if(n%d==0) require(power(zeta,d,p)!=1,"root not primitive");
        V u(n),v(n),C(n+1); read_vector(in,u,p);read_vector(in,v,p);read_vector(in,C,p);
        require(C[0]==1,"polynomial not monic");
        I a=1,b=0,c=0,d=1;
        for(I j=0;j<r;++j) {
            I aa=mod(3*a+4*c,n),bb=mod(3*b+4*d,n);
            I cc=mod(2*a+3*c,n),dd=mod(2*b+3*d,n);
            a=aa;b=bb;c=cc;d=dd;
        }
        require(a==1 && b==0 && c==0 && d==1,"S^period is not identity");
        V roots(n); roots[0]=1;
        for(I j=1;j<n;++j) roots[j]=roots[j-1]*zeta%p;
        I inv8=0;
        for(I j=1;j<n;++j) if(8*j%n==1) {inv8=j;break;}
        require(inv8!=0,"8 not invertible");
        V G(n*n),B(n*n);
        for(I x=0;x<n;++x) for(I y=0;y<n;++y)
            B[x*n+y]=G[x*n+y]=roots[mod(-inv8*(3*x*x-2*x*y+3*y*y),n)];
        const I half=(n+1)/2, normalization=inverse(den*r,p);
        // Independently check the two generating Weyl covariance identities.
        for(I generator=0;generator<2;++generator) {
            I va=generator==0?1:0,vb=generator==0?0:1;
            I sa=mod(3*va+4*vb,n),sb=mod(2*va+3*vb,n);
            for(I x=0;x<n;++x) for(I y=0;y<n;++y) {
                I left=G[x*n+mod(y-va,n)]*roots[mod(vb*(y-va+va*half),n)]%p;
                I right=roots[mod(sb*(x+sa*half),n)]*G[mod(x+sa,n)*n+y]%p;
                require(left==right,"Weyl covariance sign/convention error");
            }
        }
        // Build E by adding all iterates individually, not Python's collected coefficients.
        for(auto cc:coeff) {
            I sign=(ordinary && mod(cc.a*cc.b,2))?-1:1;
            I value=mod(sign*(cc.re+imag*cc.im),p)*normalization%p;
            I xshift=mod(cc.a,n),momentum=mod(cc.b,n);
            for(I j=0;j<r;++j) {
                for(I x=0;x<n;++x) {
                    I index=x*n+mod(x+xshift,n);
                    B[index]=mod(B[index]+weight*value*roots[mod(momentum*(x+xshift*half),n)],p);
                }
                I next=mod(3*xshift+4*momentum,n);
                momentum=mod(2*xshift+3*momentum,n);xshift=next;
            }
        }
        V total(n,0),moments;
        for(I k=0;k<=n;++k) {
            for(I j=0;j<n;++j) total[j]=(total[j]+C[n-k]*v[j])%p;
            if(k<n) {
                I s=0;for(I j=0;j<n;++j) s+=u[j]*v[j];
                moments.push_back(s%p); v=matvec(B,v,n,p);
            }
        }
        require(std::all_of(total.begin(),total.end(),[](I x){return x==0;}),"q(B)v != 0");
        V q(C.rbegin(),C.rend()),num(n),derivative(n);
        for(I k=0;k<n;++k) {
            I sum=0;for(I j=0;j<=k;++j) sum+=C[j]*moments[k-j];
            num[n-1-k]=sum%p;
            derivative[k]=(k+1)*q[k+1]%p;
        }
        require(gcd(q,num,p)==V{1},"scalar resolvent not coprime");
        require(gcd(q,derivative,p)==V{1},"polynomial not squarefree");
        std::cout<<"{\"N\":"<<n<<",\"ordinary_midpoint\":"<<ordinary
                 <<",\"p\":"<<p<<",\"independent_replay\":\"passed\"}"<<std::endl;
    }
    std::string extra; require(!(in>>extra),"unexpected trailing certificate data");
    return 0;
} catch(const std::exception& e) {
    std::cerr<<"REJECTED: "<<e.what()<<std::endl;
    return 1;
}
