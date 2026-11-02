import sys
sys.setrecursionlimit(10000)
m=12; D=1536796800
y=(1114177680, 345779280, 960498000, 806818320, 806818320, 960498000, 345779280, 1114177680, 192099600, 38419920, 38419920, 192099600)
comp={128:(16,80,80,16,16,80,80,16,16,80,80,16),81:(0,)*12,25:(5,5,0,20,20,0,5,5,0,20,20,0),49:(0,)*12,121:(0,)*12}
def fix_mod(q):
    res=[]
    for a in range(q):
        for b in range(q):
            seq=[a,b]
            for _ in range(m):
                seq.append((6*seq[-1]-seq[-2])%q)
            if seq[m]==a and seq[m+1]==b:
                v=tuple(seq[:m])
                if all((6*v[i]-v[(i-1)%m]-v[(i+1)%m])%q==0 for i in range(m)):
                    res.append(v)
    return res
FIX={q:fix_mod(q) for q in comp}
# candidate fiber vectors per component (same sorted multiset as comp[q])
cand={}
for q in comp:
    cand[q]=[v for v in FIX[q] if tuple(sorted(v))==tuple(sorted(comp[q]))]
    print(f"q={q} fiber size={len(cand[q])}")
perms=[]
for k in range(m):
    perms.append(tuple((j+k)%m for j in range(m)))
    perms.append(tuple((k-j)%m for j in range(m)))
perms=sorted(set(perms))
def canon(v): return min(tuple(v[p[j]] for j in range(m)) for p in perms)
# backtrack tau: tau[j]=position i, used; candidate sets filtered by w_q[j]==comp[q][i]
canons=set(); yprimes=set(); count_tau=[0]
# order positions 0..11
def bt(j, used, cur_cand, tau):
    if j==m:
        count_tau[0]+=1
        yp=tuple(y[tau[t]] for t in range(m))
        yprimes.add(yp); canons.add(canon(yp)); return
    # candidate values at position j across components: tau[j]=i must satisfy exists cand with cand[j]==comp[q][i] for each q
    for i in range(m):
        if used[i]: continue
        new_cand={}
        ok=True
        for q in comp:
            lst=[w for w in cur_cand[q] if w[j]==comp[q][i]]
            if not lst: ok=False; break
            new_cand[q]=lst
        if not ok: continue
        used[i]=True; tau.append(i)
        bt(j+1, used, new_cand, tau)
        tau.pop(); used[i]=False
bt(0, [False]*m, cand, [])
print("taus giving Fix vectors:", count_tau[0])
print("distinct y' in fiber (in Fix):", len(yprimes))
print("distinct Gamma canons (orbits in fiber):", len(canons))
for c in sorted(canons): print(c)
