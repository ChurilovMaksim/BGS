# independent: reachable carry pair states for lambda (x^2-6x+1) and eps (x^2-2x-1) systems; Green l1 by direct series
import math, collections
def reach(coef, B, V=60):
    # u_k = c0*e_k + c1*e_{k-1} + c2*e_{k-2}; state (e_{k-1}, e_k) -> (e_k, e_{k+1})
    c0,c1,c2=coef; R=range(-B,B+1)
    succ=lambda s: [(s[1],c) for c in R if abs(c0*c+c1*s[1]+c2*s[0])<=V]
    pred=lambda s: [(a,s[0]) for a in R if abs(c0*s[1]+c1*s[0]+c2*a)<=V]
    def bfs(f):
        seen={(0,0)}; dq=collections.deque([(0,0)])
        while dq:
            s=dq.popleft()
            for t in f(s):
                if t not in seen: seen.add(t); dq.append(t)
        return seen
    F=bfs(succ); Bk=bfs(pred); S=F&Bk
    edges=sum(1 for s in S for t in succ(s) if t in S)
    return len(F),len(Bk),len(S),max(max(map(abs,s)) for s in S),edges, any(B in map(abs,s) for s in F|Bk)
# eps: u_k = e_{k-2} - 2e_{k-1} - e_k  ; use a bigger box (60) to check the box never binds
for B in (51,60):
    print('eps B=%d'%B, reach((-1,-2,1),B))
for B in (15,20):
    print('lam B=%d'%B, reach((1,-6,1),B))
# Green l1 by direct series: g = inverse of p(S), via partial fractions numerically checked by convolution
import numpy as np
N=200; r=1+math.sqrt(2); rp=1-math.sqrt(2)
# bounded solution of e_{k-2}-2e_{k-1}-e_k = delta_{k,0}: try g_k = A r^{-k} (k>=?) ... compute by solving a large banded system
K=121; M=np.zeros((K,K)); 
for k in range(K):
    for d,c in ((0,-1),(-1,-2),(-2,1)):
        if 0<=k+d<K: M[k,k+d]=c
rhs=np.zeros(K); rhs[K//2]=1; g=np.linalg.solve(M,rhs)
print('eps green l1 (truncated solve)', np.abs(g).sum(), (2+math.sqrt(2))/4, 60*(2+math.sqrt(2))/4)
M2=np.zeros((K,K))
for k in range(K):
    for d,c in ((0,1),(-1,-6),(-2,1)):
        if 0<=k+d<K: M2[k,k+d]=c
g2=np.linalg.solve(M2,rhs); print('lam green l1', np.abs(g2).sum())
