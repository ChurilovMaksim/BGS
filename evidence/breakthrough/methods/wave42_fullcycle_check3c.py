from collections import Counter
def mul(x,y,m): return ((x[0]*y[0]+2*x[1]*y[1])%m, (x[0]*y[1]+x[1]*y[0])%m)
B=(17,12)
def beta_pows(m,n):
    r=[(1,0)]
    for _ in range(n): r.append(mul(r[-1],B,m))
    return r
def trseq(C,m,n):
    bp=beta_pows(m,n)
    return tuple((2*mul(C,bp[k],m)[0])%m for k in range(n))
m=25; per=15
params=[(a,b) for a in range(m) for b in range(m)]
M={C:Counter(trseq(C,m,per)) for C in params}
byM={}
for C in params: byM.setdefault(tuple(sorted(M[C].items())),[]).append(C)
def neg(C): return ((-C[0])%m,(-C[1])%m)
def sub_le(A,B): return all(A[v]<=B[v] for v in A)
recomb=[]
for C in params:
    T=M[C]+M[neg(C)]
    for D in params:
        if M[D]==M[C] or M[D]==M[neg(C)]: continue  # same block: trivial
        if not sub_le(M[D],T): continue
        R=T-M[D]
        if tuple(sorted(R.items())) in byM:
            recomb.append((C,D))
print('genuine single-component recombinations at 25:',len(recomb))
for e in recomb[:20]: print('  ',e)
