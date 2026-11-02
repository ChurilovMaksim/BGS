import math
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

def check(m,P):
    t=math.gcd(m,4)
    L=None
    for i in range(1,10000):
        if alpha_pow(i,P)==(1,0): L=i; break
    g=math.gcd(L,t); Hlen=L//g; zeta=alpha_pow(Hlen,P)
    data={}
    for a in range(P):
        for b in range(P):
            A=(a,b); y=tuple(tr(mul(A,alpha_pow(i,P),P),P) for i in range(m)); data[A]=y
    groups={}
    for A,y in data.items(): groups.setdefault(tuple(sorted(y)),[]).append(A)
    tot_badB=0; tot_badNB=0; tot_badTr=0; tot=0
    for ms,As in groups.items():
        tot+=1
        A0=As[0]; B0=pw(A0,Hlen,P); zetas=[pw(zeta,k,P) for k in range(g)]
        for A in As:
            B=pw(A,Hlen,P)
            ok=any(B==mul(B0,z,P) or B==mul(conj(B0,P),z,P) for z in zetas)
            if not ok: tot_badB+=1
            if (B[0]*B[0]-2*B[1]*B[1])%P != (B0[0]*B0[0]-2*B0[1]*B0[1])%P: tot_badNB+=1
            if tr(pw(B,g,P),P)!=tr(pw(B0,g,P),P): tot_badTr+=1
    print(f"m={m} P={P} L={L} g={g} |H|={Hlen} groups={tot} badB={tot_badB} badNB={tot_badNB} badTrBg={tot_badTr}")
for m,P in [(12,9),(42,49),(36,27),(12,81),(14,169)]:
    # (12,81): P=81, As=6561, m=12 feasible? alpha_pow recomputed many times slow; skip if too big? try with precomputed powers
    check(m,P)
