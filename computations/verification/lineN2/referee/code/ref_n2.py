import math, numpy as np
from scipy.special import jv
from collections import deque
lam=3+2*math.sqrt(2); mu=1.9154732; mulo=1.9154712; T=1.28359; xi=2.4586893
def h(p):
    a,b=1,1
    for _ in range(p-1): a,b=a+2*b,a+b
    return a
print("[1] A^p - I = h_p B, det B = -4")
A=np.array([[3,4],[2,3]],dtype=object); ok=True
for p in [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]:
    M=np.array([[1,0],[0,1]],dtype=object)
    for _ in range(p): M=M.dot(A)
    D=M-np.array([[1,0],[0,1]],dtype=object); H=h(p)
    B=None
    if all(x%H==0 for x in D.flatten()):
        B=D//H; det=B[0,0]*B[1,1]-B[0,1]*B[1,0]
    else: det=None
    ok&=(det==-4)
print("    all p<=61:",ok)
print("[2] constants")
print("    mu*/lam^(1/3)=%.5f  mu*/lam^(1/6)=%.5f  (mu*^2/xi)=%.5f  log_lam=%.4f  lam/L^(2/m)=%.4f"%(mu/lam**(1/3),mu/lam**(1/6),mulo**2/xi,math.log(mulo**2/xi)/math.log(lam),lam/(mulo**2/xi)**2))
print("    T*lam^(1/3)=%.4f  G=sum|J_n(1.8)|=%.7f  T^3=%.5f"%(T*lam**(1/3),sum(abs(jv(n,1.8)) for n in range(-60,61)),T**3))
for f,r2 in [('8V',1.0529012),('8E',1.0519234)]: print("    %s threshold T^3/r2 = %.5f"%(f,T**3/r2))
for f,r2 in [('16V',1.0534557),('16E',1.0529202)]: print("    %s threshold 1.4742^3/r2 = %.5f"%(f,1.4742**3/r2))
print("    (1.98242*r2)^(1/3)=%.5f  (mu* r2)^(1/3)=%.5f  margin=%.4f"%((1.98242*1.0529012)**(1/3),(mu*1.0529012)**(1/3),1-(mu*1.0529012)**(1/3)/T))
print("    free k=24 max 2.01382 vs 8V threshold:",2.01382>T**3/1.0529012, " k'=20 sample 2.01677 >thr:",2.01677>T**3/1.0529012)
print("    3log mu* - log lam = %.4f ; 3 log T = %.4f ; log 1.26278 = %.4f < log T = %.4f"%(3*math.log(mu)-math.log(lam),3*math.log(T),math.log(1.26278),math.log(T)))
print("    mu* T = %.6f vs xi_lo %.6f"%(mulo*T,xi))
print("    slow-segment factor per unit log_lam c (rank p, 3 reps): (mu/T)^6/lam^2 = %.4f ; rank 3p: (mu/T)^2/lam^2 = %.4f"%((mu/T)**6/lam**2,(mu/T)**2/lam**2))
print("[3] carry exactness: big box E0=30, letters |d|<=40; states fwd-reachable from (0,0) AND co-reachable to (0,0)")
E0=30; V=40
def nbrs(s):
    p,q=s
    for e in range(-E0,E0+1):
        if abs(e-6*q+p)<=V: yield (q,e)
def rnbrs(s):
    q,e=s
    for p in range(-E0,E0+1):
        if abs(e-6*q+p)<=V: yield (p,q)
def bfs(f):
    seen={(0,0)}; dq=deque([(0,0)])
    while dq:
        s=dq.popleft()
        for t in f(s):
            if t not in seen: seen.add(t); dq.append(t)
    return seen
both=bfs(nbrs)&bfs(rnbrs)
print("    #states=%d  max|e|=%d (claim <= floor(V/4)=10)"%(len(both),max(max(abs(a),abs(b)) for a,b in both)))
