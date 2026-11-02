def seqs(N):
    c=[1,3]; e=[0,1]
    for _ in range(N):
        c.append(6*c[-1]-c[-2]); e.append(6*e[-1]-e[-2])
    return c,e
c,e=seqs(40)
for mod in [64,128,256]:
    print(f"mod {mod} c period? c[:32]={[x%mod for x in c[:32]]}")
    print(f"mod {mod} e[:32]={[x%mod for x in e[:32]]}")
    # find period of e mod mod (smallest p with e[i+p]==e[i] for i<32?)
    for p in range(1,65):
        if all(e[i]%mod==e[i+p]%mod for i in range(32)):
            print(f"  e period {p} mod {mod}"); break
    for p in range(1,65):
        if all(c[i]%mod==c[i+p]%mod for i in range(32)):
            print(f"  c period {p} mod {mod}"); break
