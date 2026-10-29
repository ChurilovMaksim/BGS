# Driver: exact E = a + b*sqrt(p) (p = 1 mod 4) or a (p = 3 mod 4) from brute-force class counts.
import subprocess, sys, json, os
from fractions import Fraction as F
HERE = os.path.dirname(os.path.abspath(__file__))
def exact(p,m,nth=8):
    out = subprocess.run([HERE+'/brute',str(p),str(m),str(nth)],capture_output=True,text=True,check=True).stdout.split()
    n0,nsq,nns = map(int,out[2:5])
    a = F(n0,1) - F(nsq+nns,p-1)
    b = F(nsq-nns,p-1)   # coefficient of the Gauss sum g = sum (k/p) zeta^k
    pm = F(p**m)
    if p%4==3:
        assert nsq==nns, (p,m,nsq,nns)
        return a/pm, F(0)
    return a/pm, b/pm      # g = sqrt(p)
if __name__=="__main__":
    p,m = int(sys.argv[1]), int(sys.argv[2])
    a,b = exact(p,m)
    print(json.dumps({"p":p,"m":m,"rat":str(a),"sqrtp_coeff":str(b),"float":float(a)+float(b)*p**0.5}))
