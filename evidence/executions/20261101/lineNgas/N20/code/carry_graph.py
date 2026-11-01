"""N20 [P, exact integer computation]: carry pair-state graph of the exact-collision system (N15 sec.3.1, lineN15 N15-F3).
Carries e_t in Z with v_t = e_t - 6 e_{t-1} + e_{t-2}, |v_t| <= 60 (letters n, m in [-30,30]).  State (e_{t-1}, e_t).
Transition (a,b) -> (b,c) allowed iff |c - 6 b + a| <= 60.  Box |e| <= 15 (a-priori Green bound, N15 [P]).
Reachable = on a closed path (0,0) -> ... -> (0,0)  (forward reachable from (0,0) AND backward reachable to (0,0)).
Also: Collatz-Wielandt lower bound for the spectral radius of the 0/1 adjacency matrix on the reachable states (used in the
obstruction lemma O1 of REPORT_N20 sec.4), and an integer certificate vector exported for Lean."""
import json, numpy as np
B=15; R=range(-B,B+1)
ok=lambda a,b,c: abs(c-6*b+a)<=60
fw={(0,0)}; fr=[(0,0)]
while fr:
    nf=[]
    for (a,b) in fr:
        for c in R:
            if ok(a,b,c) and (b,c) not in fw: fw.add((b,c)); nf.append((b,c))
    fr=nf
bw={(0,0)}; fr=[(0,0)]
while fr:
    nf=[]
    for (b,c) in fr:
        for a in R:
            if ok(a,b,c) and (a,b) not in bw: bw.add((a,b)); nf.append((a,b))
    fr=nf
S=sorted(fw&bw); idx={s:i for i,s in enumerate(S)}
emax=max(max(abs(a),abs(b)) for a,b in S); vals=sorted(set(a for a,b in S)|set(b for a,b in S))
A=np.zeros((len(S),len(S)))
for (a,b) in S:
    for c in R:
        if ok(a,b,c) and (b,c) in idx: A[idx[(a,b)],idx[(b,c)]]=1
ev=np.linalg.eigvals(A); rho=max(abs(ev))
w,V=np.linalg.eig(A); x=np.abs(V[:,np.argmax(abs(w))].real); x=x/x.min()
xi=np.maximum(1,np.floor(x*1000)).astype(int)
Ax=A@xi; cw=min(Ax[i]/xi[i] for i in range(len(S)))
out=dict(n_states=len(S),n_fw=len(fw),n_bw=len(bw),emax=emax,n_values=len(vals),n_edges=int(A.sum()),rho_adj_float=float(rho),
         collatz_wielandt_lower=float(cw),diag_00_selfloop=bool(A[idx[(0,0)],idx[(0,0)]]))
print(out)
json.dump(out,open('../logs/carry_graph.json','w'),indent=1)
json.dump(dict(states=S,x=[int(t) for t in xi]),open('../logs/carry_graph_cert.json','w'))
