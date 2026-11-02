#include <bits/stdc++.h>
using namespace std;
int main(){
    const int P=2197; // 13^3
    const int M=182;
    const int MOD1=1000000007, MOD2=1000000009, BASE=9113823;
    vector<int> pw1(P), pw2(P);
    long long cur1=1, cur2=1;
    for(int v=0;v<P;v++){ pw1[v]=(int)cur1; pw2[v]=(int)cur2; cur1=cur1*BASE%MOD1; cur2=cur2*BASE%MOD2; }
    size_t N=(size_t)P*P;
    vector<uint64_t> H; H.reserve(N);
    for(int a=0;a<P;a++){
        for(int b=0;b<P;b++){
            int ca=a, cb=b; long long h1=0,h2=0;
            for(int j=0;j<M;j++){
                int v=(2*ca)%P;
                h1+=pw1[v]; if(h1>=MOD1) h1-=MOD1;
                h2+=pw2[v]; if(h2>=MOD2) h2-=MOD2;
                int na=(3*ca+4*cb)%P, nb=(2*ca+3*cb)%P;
                ca=na; cb=nb;
            }
            // Note: sums may exceed mod by up to M*MOD; reduce properly:
            // we accumulated with conditional subtract only once per step, but h can grow: use mod each step via if>=2*MOD
            H.push_back(((uint64_t)(uint32_t)(h1%MOD1)<<32)|(uint32_t)(h2%MOD2));
        }
        if(a%500==0) fprintf(stderr,"a=%d\n",a);
    }
    sort(H.begin(), H.end());
    size_t best=0, run=1; uint64_t bestkey=0;
    for(size_t i=1;i<H.size();i++){
        if(H[i]==H[i-1]) run++; else { if(run>best){best=run;bestkey=H[i-1];} run=1; }
    }
    if(run>best){best=run;bestkey=H.back();}
    printf("total=%zu maxhashgroup=%zu\n", N, best);
    // collect C's with bestkey and verify exactly by sorting sequences
    vector<array<short,182>> seqs;
    for(int a=0;a<P;a++){
        for(int b=0;b<P;b++){
            int ca=a, cb=b; long long h1=0,h2=0;
            for(int j=0;j<M;j++){
                int v=(2*ca)%P;
                h1+=pw1[v]; if(h1>=MOD1) h1-=MOD1;
                h2+=pw2[v]; if(h2>=MOD2) h2-=MOD2;
                int na=(3*ca+4*cb)%P, nb=(2*ca+3*cb)%P; ca=na; cb=nb;
            }
            uint64_t key=((uint64_t)(uint32_t)(h1%MOD1)<<32)|(uint32_t)(h2%MOD2);
            if(key==bestkey){
                array<short,182> s; ca=a; cb=b;
                for(int j=0;j<M;j++){ s[j]=(short)((2*ca)%P); int na=(3*ca+4*cb)%P, nb=(2*ca+3*cb)%P; ca=na; cb=nb; }
                sort(s.begin(), s.end()); seqs.push_back(s);
            }
        }
    }
    sort(seqs.begin(), seqs.end());
    size_t bex=0, r2=1;
    for(size_t i=1;i<seqs.size();i++){ if(seqs[i]==seqs[i-1]) r2++; else { bex=max(bex,r2); r2=1; } }
    bex=max(bex,r2);
    printf("bestkey members=%zu exact max fiber in group=%zu\n", seqs.size(), bex);
    return 0;
}
