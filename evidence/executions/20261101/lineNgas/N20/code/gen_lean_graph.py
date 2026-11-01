"""N20: emit literal bitmasks FW, BW (forward/backward reachable sets of the lambda-carry graph, box |e|<=15, offset 15)
and BFS depth tables (31x31, 99 = not in set) for the memory-light Lean certificate (lean/LineN20.lean, v2)."""
B=15; R=range(-B,B+1); ok=lambda a,b,c: abs(c-6*b+a)<=60
def bfs(fwd):
    D={(0,0):0}; fr=[(0,0)]; d=0
    while fr:
        d+=1; nf=[]
        for (x,y) in fr:
            for w in R:
                if fwd: s=(y,w); good=ok(x,y,w)
                else: s=(w,x); good=ok(w,x,y)
                if good and s not in D: D[s]=d; nf.append(s)
        fr=nf
    return D
out=[]
for name,fwd in (('FW',True),('BW',False)):
    D=bfs(fwd); m=0
    for (a,b) in D: m|=1<<((a+15)*31+(b+15))
    T=[[99]*31 for _ in range(31)]
    for (a,b),d in D.items(): T[a+15][b+15]=d
    out.append(f'def {name} : Nat := {m}')
    out.append(f'def D{name} : List (List Nat) := [\n  '+',\n  '.join('['+','.join(map(str,r))+']' for r in T)+']')
    print(name,len(D),max(D.values()))
open('../lean/graph_table.lean.inc','w').write('\n'.join(out)+'\n')
