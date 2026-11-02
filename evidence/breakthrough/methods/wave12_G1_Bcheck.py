# R mod P arithmetic: (a,b) = a + b*sqrt2, mult, conj, pow, trace=2a
def add(x,y,P): return ((x[0]+y[0])%P,(x[1]+y[1])%P)
def mul(x,y,P): return ((x[0]*y[0]+2*x[1]*y[1])%P,(x[0]*y[1]+x[1]*y[0])%P)
def conj(x,P): return (x[0]%P,(-x[1])%P)
def pw(x,n,P):
    r=(1,0)
    for _ in range(n): r=mul(r,x,P)
    return r
def tr(x,P): return (2*x[0])%P
def alpha_pow(i,P):
    r=(1,0); a=(3,2)
    for _ in range(i): r=mul(r,a,P)
    return r

def analyze(m,P):
    t=__import__('math').gcd(m,4)
    # order L of alpha mod P
    L=None
    for i in range(1,5000):
        if alpha_pow(i,P)==(1,0): L=i; break
    import math
    g=math.gcd(L,t); Hlen=L//g
    zeta=alpha_pow(Hlen,P)
    print(f"m={m} P={P} L={L} t={t} g={g} |H|={Hlen} zeta={zeta} zeta^g={pw(zeta,g,P)}")
    # sequences
    data={}
    for a in range(P):
        for b in range(P):
            A=(a,b)
            y=[]
            for i in range(m):
                ai=alpha_pow(i,P); prod=mul(A,ai,P); y.append(tr(prod,P))
            data[A]=tuple(y)
    groups={}
    for A,y in data.items(): groups.setdefault(tuple(sorted(y)),[]).append(A)
    # pick the N-varying group (largest? or any with >8 As)
    for ms,As in groups.items():
        if len(As)>8:
            print(" group size",len(As),"multiset",ms)
            # B and traces
            seen={}
            for A in As:
                B=pw(A,Hlen,P)
                traces=tuple(tr(mul(B,pw(zeta,r,P),P),P) for r in range(t))
                # B^g
                Bg=pw(B,g,P)
                key=(Bg, tr(Bg,P))
                seen.setdefault(traces,[]).append((A,B,Bg))
            print("  distinct trace-tuples (r=0..t-1):",len(seen))
            for trs,lst in seen.items():
                print("   traces",trs,"count",len(lst),"example A,B,Bg:",lst[0])
            # check B' vs B zeta^k / conj
            A0=As[0]; B0=pw(A0,Hlen,P)
            zetas=[pw(zeta,k,P) for k in range(g)]
            bad=0
            for A in As:
                B=pw(A,Hlen,P)
                ok=False
                for k in range(g):
                    if B==mul(B0,zetas[k],P): ok=True
                    if B==mul(conj(B0,P),zetas[k],P): ok=True
                if not ok:
                    bad+=1
                    if bad<=5: print("   B not in D-orbit of B0: A",A,"B",B,"B0",B0)
            print("  B not D-related count:",bad,"/",len(As))
            # N(B), Tr(B^g)
            print("  N(B) values:",sorted(set((B[0]*B[0]-2*B[1]*B[1])%P for A in As for B in [pw(A,Hlen,P)])))
            print("  Tr(B^g) values:",sorted(set(tr(pw(pw(A,Hlen,P),g,P),P) for A in As)))
            print()
for m,P in [(12,9),(36,27)]:
    analyze(m,P)
