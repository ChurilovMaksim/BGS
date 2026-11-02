import random
random.seed(1234)
def mul(a,b,q): return ((a[0]*b[0]+2*a[1]*b[1])%q,(a[0]*b[1]+a[1]*b[0])%q)
def pw(a,n,q):
    r=(1,0)
    while n:
        if n&1: r=mul(r,a,q)
        a=mul(a,a,q); n>>=1
    return r
def tr(a,q): return (2*a[0])%q
DIH=[]
for k in range(36):
    DIH.append(tuple((i+k)%36 for i in range(36)))
    DIH.append(tuple((-i+k)%36 for i in range(36)))
DIH=sorted(set(DIH))
QS=[128,25,49,121,5329,32041,38809,39601]  # non-729
def genuine(q):
    if q==128: return [(16*a,8*b) for a in range(8) for b in range(16)]
    import math; p=int(round(q**0.5))
    return [(p*a,p*b) for a in range(p) for b in range(p)]
def seq(A,q):
    out=[]; cur=A
    for i in range(36):
        out.append(tr(cur,q)); cur=mul(cur,(3,2),q)
    return tuple(out)
def pattern(s):
    lab={}; out=[]
    for v in s:
        if v not in lab: lab[v]=len(lab)
        out.append(lab[v])
    return tuple(out)
# patterns + example sequence per component, and P o tau tables
comp={}
for q in QS+[729]:
    if q==729: G=[(27*a,27*b) for a in range(27) for b in range(27)]
    else: G=genuine(q)
    pats={}
    for A in G:
        s=seq(A,q); p=pattern(s)
        if p not in pats: pats[p]=s
    # table: pattern -> list over tau of P o tau
    tab={}
    for p in pats:
        tab[p]=[tuple(p[t[i]] for i in range(36)) for t in DIH]
    comp[q]=(list(pats.keys()), pats, tab)
    print(f"q={q} patterns={len(pats)}",flush=True)
# shifts at 729
shifts=set()
for a in range(9):
    for b in range(9):
        shifts.add(seq(((81*a)%729,(81*b)%729),729))
print("shifts:",len(shifts),flush=True)
fails=0; realizable=0; trials=3000
for trial in range(trials):
    sig=list(range(36)); random.shuffle(sig); sig=tuple(sig)
    masks={}; ok=True; chosen={}
    for q in QS+[729]:
        pats, ex, tab = comp[q]
        order=list(range(len(pats))); random.shuffle(order)
        found=None
        for pi in order:
            p=pats[pi]
            psig=tuple(p[sig[i]] for i in range(36))
            m=[ti for ti in range(72) if tab[p][ti]==psig]
            if m:
                found=(pi,m,psig); break
        if not found: ok=False; break
        chosen[q]=found; masks[q]=set(found[1])
    if not ok: continue
    realizable+=1
    # 729 pair: S = example of chosen pattern, S' = tau729(S) for first tau in mask
    pats729, ex729, tab729 = comp[729]
    p729=pats729[chosen[729][0]]; S729=ex729[p729]
    ti729=chosen[729][1][0]; tau729=DIH[ti729]
    Sp729=tuple(S729[tau729[i]] for i in range(36))
    T=set()
    for ti,tau in enumerate(DIH):
        diff=tuple((Sp729[i]-S729[tau[i]])%729 for i in range(36))
        if diff in shifts: T.add(ti)
    inter=set(T)
    for q in QS: inter &= masks[q]
    if not inter:
        fails+=1
        print("FAILURE trial",trial,"sigma",sig,"masks sizes",{q:len(masks[q]) for q in masks},"|T|",len(T))
        break
print(f"trials={trials} realizable={realizable} failures={fails}")
