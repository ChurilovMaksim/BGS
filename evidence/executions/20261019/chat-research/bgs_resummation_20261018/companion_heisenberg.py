import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path
from companion_certificate import plus,times,shift
from first_defect_verification import P1,P2

def expect(a,N):
    # Horner form of sum a_k (1/2)_k / N^k; exact at every step.
    acc=F(0)
    for k in range(len(a)-1,-1,-1):acc=a[k]+F(2*k+1,2*N)*acc
    return acc

def main(destination):
    Ns=(49,169,625);ratios=(F(1,2),F(9,10));M=max(int(N*t) for N in Ns for t in ratios)
    Q=[[1],[-1],[0,1],[0,1],[0,1],[0,1]]
    denom=[[1]];recip={}
    for k in range(1,4):
        new=[[] for _ in range(len(denom)+5)]
        for i,a in enumerate(denom):
            for j,b in enumerate(Q):new[i+j]=plus(new[i+j],times(a,b))
        denom=new
        r=[[1]]
        for m in range(1,M+1):
            out=[]
            for d in range(1,min(m,len(denom)-1)+1):out=plus(out,times(denom[d],r[m-d]),-1)
            r.append(out)
        recip[k]=r
    S=[[5]]
    for m in range(1,M+1):
        sm=[]
        for j in range(1,min(m-1,5)+1):sm=plus(sm,times(Q[j],S[m-j]),-1)
        if m<=5:sm=plus(sm,[m*x for x in Q[m]],-1)
        S.append(sm)
    Q2={};running=F(0)
    for q in range(max(P2)+1):
        running+=P2.get(q,F(0))
        if running:Q2[q]=running
    assert running==0
    rows=[]
    for N in Ns:
        for target in ratios:
            m=int(N*target);tau=F(m,N);v0=(expect(S[m],N)-1)/2;v1=F(0)
            for q,v in P1.items():
                if m>=q:v1+=F(m,N)*v*expect(recip[1][m-q],N)
            for q,v in Q2.items():
                if m>=q:v1+=F(m,N*N)*v*expect(recip[2][m-q],N)
                for d in range(2,6):
                    if m>=q+d:v1-=F(4*m,N*N)*v*expect(shift(recip[3][m-q-d],1),N)
            t=float(tau);l0=((1+4*t)**(-.5)-1)/2;l1=t/math.sqrt(1+4*t)-35*t*t/(12*(1+4*t)**1.5)
            rows.append({'N':N,'m':m,'target_ratio':str(target),'actual_ratio':str(tau),
                         'R0_exact':str(v0),'R1_exact':str(v1),'R0_display':float(v0),'R1_display':float(v1),
                         'R0_limit_at_actual_ratio':l0,'R1_limit_at_actual_ratio':l1,
                         'R0_difference':float(v0)-l0,'R1_difference':float(v1)-l1})
    data={'status':'completed_exact_finite_values','rows':rows,
          'scope':'Every finite sector value is exact. Comparison values are numerical displays of the analytic limit; no assertion of monotonic error or a numerical proof.'}
    Path(destination).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({**data,'rows':[{k:v for k,v in r.items() if not k.endswith('_exact')} for r in rows]}))

if __name__=='__main__':main(sys.argv[1])
