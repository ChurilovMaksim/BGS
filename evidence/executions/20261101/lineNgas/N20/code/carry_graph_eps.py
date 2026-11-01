"""N20 [P, exact integer computation]: carry pair-state graph of the JOINT (A,B) exact-collision system.
Joint relation (REPORT_N20 sec.2, Lemma J): sum_k u_k eps^k = 0, u_{2t} = v^A_t, u_{2t-1} = -v^B_t, |u_k| <= 60
<=> u_k = e_{k-2} - 2 e_{k-1} - e_k with integer carries e (x^2 - 2x - 1 monic irreducible; Gauss).
Green bound: sum_k |g(k)| = (2+sqrt2)/4 = 0.85355 (computed below in floats and as closed form), so |e| <= floor(60*0.85355) = 51.
State (e_{k-1}, e_k); transition (a,b)->(b,c) iff |a - 2b - c| <= 60.  Reachable = on a closed path (0,0)->(0,0)."""
import json, numpy as np, math
# Green kernel of p(z) = z^2 - 2z - 1 on |z| = 1 (Laurent coefficients), numerically
M=4096; z=np.exp(2j*np.pi*np.arange(M)/M); g=np.fft.fft(1/(z**2-2*z-1))/M; G1=float(np.abs(g).sum())
closed=(2+math.sqrt(2))/4
B=51; R=range(-B,B+1); ok=lambda a,b,c: abs(a-2*b-c)<=60
def bfs(fwd):
    S={(0,0)}; fr=[(0,0)]
    while fr:
        nf=[]
        for (x,y) in fr:
            for w in R:
                if fwd and ok(x,y,w) and (y,w) not in S: S.add((y,w)); nf.append((y,w))
                if not fwd and ok(w,x,y) and (w,x) not in S: S.add((w,x)); nf.append((w,x))
        fr=nf
    return S
fw=bfs(True); bw=bfs(False); S=fw&bw
emax=max(max(abs(a),abs(b)) for a,b in S)
# also: is the box bound hit? (states with |e| = 51)
idx={s:i for i,s in enumerate(sorted(S))}; n=len(S)
deg=[sum(1 for c in R if ok(a,b,c) and (b,c) in idx) for (a,b) in sorted(S)]
out=dict(green_l1_float=G1,green_l1_closed=closed,carry_bound=60*closed,n_states=len(S),n_fw=len(fw),n_bw=len(bw),emax=emax,
         n_edges=int(sum(deg)),mean_outdeg=float(np.mean(deg)))
print(out); json.dump(out,open('../logs/carry_graph_eps.json','w'),indent=1)
