"""Line J3: 2-state finite factor = one exact invariant block of the 64-state (a,16) automaton (logs/blocks16_exact.json).
Env: BGS16_CASE='m,a' (m in 3..45 step 6, a=+-2), BGS16_BLOCK=index.  In basis (f1,f2): perm=(0,1): A_n f1 = z^p f1, A_n f2 = z^q f2;
perm=(1,0): A_n f1 = z^p f2, A_n f2 = z^q f1 (z = e(1/16)).  finite() returns (out,in,ph16,tw) with entry e(-ph16/16) e(n tw/7)."""
import os, sys, json
sys.path.insert(0,'/workspace/bgs-lineI/dom_v3')
from gstates import g2params, taus7
here=os.path.dirname(os.path.abspath(__file__))
_J=json.load(open(os.path.join(here,'../logs/blocks16_exact.json')))
CASE=os.environ['BGS16_CASE']; BLK=int(os.environ['BGS16_BLOCK'])
_B=_J['cases'][CASE]['blocks'][BLK]['act']
def reach(P,Nmax): return [0,1], None
def finite(P,idx,tg,n,cyc):
    A=_B[str(n%16)]; perm=A['perm']; ex=A['exps']; out=[]
    for i_in in (0,1):
        o=perm[i_in]; ph=(-ex[i_in])%16
        if cyc is None: out.append((o,i_in,ph,0))
        else:
            for i in range(3): out.append((o*3+(i+1)%3,i_in*3+i,ph,cyc[i]))
    return out
