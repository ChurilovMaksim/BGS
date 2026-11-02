def fix_pts(m,q):
    pts=[]
    for y0 in range(q):
        for y1 in range(q):
            seq=[y0,y1]
            for _ in range(m):
                seq.append((6*seq[-1]-seq[-2])%q)
            if seq[m]==y0 and seq[m+1]==y1:
                pts.append(tuple(seq[:m]))
    return pts

def v2(n):
    v=0
    while n%2==0:
        n//=2; v+=1
    return v

for m in [2,4,6,8,10,12,14,16,20,24,28,36]:
    L=v2(m); a=2*L+3 if L>=1 else 2
    q=2**a
    P=2**L
    fm=fix_pts(m,q)
    fp=fix_pts(P,q)
    # is every Fix_m point P-periodic?
    nonP=sum(1 for y in fm if any(y[i]!=y[i%P] for i in range(m)))
    print(f"m={m} L={L} a={a} q={q} |Fix_m|={len(fm)} |Fix_P|={len(fp)} nonPperiodic={nonP}")
