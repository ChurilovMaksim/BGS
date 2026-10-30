"""Line H: kappa lemma check. For every odd m in [5,599] with 3 not| m and s = +-1: kappa = law_params(m,7,s)['kappa'] is odd,
and |c_b|^2 = |8^-1 sum_{t mod 8} e((kappa t^2 - b t)/8)|^2 equals 1/4 (b even) / 0 (b odd), computed EXACTLY in Q(sqrt2)."""
import sys
from fractions import Fraction as Fr
sys.path.insert(0,'/workspace/bgs-next/lineE/step2')
from lawlib import law_params
# cos(2 pi j/8) = (a + b sqrt2): j=0:1, 1:s/2, 2:0, 3:-s/2, 4:-1, ...
COS={0:(Fr(1),Fr(0)),1:(Fr(0),Fr(1,2)),2:(Fr(0),Fr(0)),3:(Fr(0),Fr(-1,2)),4:(Fr(-1),Fr(0)),5:(Fr(0),Fr(-1,2)),6:(Fr(0),Fr(0)),7:(Fr(0),Fr(1,2))}
def abs2(kappa,b):
    n=[0]*8
    for t in range(8): n[(kappa*t*t-b*t)%8]+=1
    A=Fr(0); B=Fr(0)
    for j in range(8):
        for k in range(8):
            a,bb=COS[(j-k)%8]; A+=n[j]*n[k]*a; B+=n[j]*n[k]*bb
    return A/64,B/64
cnt=0
for m in range(5,600,2):
    if m%3==0: continue
    for s in (1,-1):
        P=law_params(m,7,s); kap=P['kappa']; assert kap%2==1,(m,s,kap)
        assert (49*P['u'])%8==1 and P['u']%8==1
        for b in range(8):
            v=abs2(kap,b); assert v==((Fr(1,4),Fr(0)) if b%2==0 else (Fr(0),Fr(0))),(m,s,b,v)
        cnt+=1
print('OK: kappa odd and |c_b|^2 = 1/4 (b even), 0 (b odd) exactly for',cnt,'(m,s) pairs, odd m<=599, 3 not| m')
