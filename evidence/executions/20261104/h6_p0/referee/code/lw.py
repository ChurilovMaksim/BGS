from sympy import primerange, isprime, factorint
def h(n):
    a,b=1,1
    for _ in range(n-1): a,b=b,2*b+a
    return b if n>=1 else 1
viol=0;hits=0
Q=list(primerange(3,300000))
for p in primerange(3,300):
    H=h(p)
    for q in Q:
        if H%q==0:
            hits+=1
            if (q%(2*p)) not in (1,2*p-1): viol+=1; print('VIOL',p,q)
print('p<300, q<3e5: hits',hits,'violations',viol)
H=h(419); print('p=419 claimed factors divide:',[H%q==0 for q in (839,17599,211177,54054353)], [q%838 for q in (839,17599,211177,54054353)])
# full factorization small p, squarefree and omega
mx=0
for p in primerange(3,110):
    f=factorint(h(p)); assert all((q%(2*p)) in (1,2*p-1) for q in f); assert all(e==1 for e in f.values()); mx=max(mx,len(f))
print('full factorisation p<110: all ok, squarefree, max omega',mx)
