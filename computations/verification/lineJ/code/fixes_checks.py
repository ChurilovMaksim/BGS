"""Line J v2, referee fixes F3/F4 (exact integer checks).
F3: (h_m, y'_m) are the coordinates of (1+sqrt2)^m = h + y' sqrt2 ... checked as h_m = (mu^m+mubar^m)/2, y'_m = (mu^m-mubar^m)/(2 sqrt2) for odd m;
    ord of 1+sqrt2 in (Z[sqrt2]/49)^* is 42 => (h mod 49, y' mod 7) has period | 42 => members/t-labels period | 42; sector constants period 24;
    hence B_C has period | 168.  F4: c4^{(case,-2)} = -c0^{(case,-2)} exactly in all 4 cases (sector table)."""
import sys, json, math
sys.path.insert(0,'/workspace/bgs-lineI/dom_v3')
from law import mdata
# coordinates of (1+sqrt2)^m
x,y=1,0; coords={}
for m in range(1,400):
    x,y=x+2*y,x+y; coords[m]=(x,y)
for m in range(3,400,2):
    D=mdata(m); assert coords[m]==(D['h'],D['yp']),m
# order mod 49
x,y=1,1; k=1
while (x%49,y%49)!=(1,0): x,y=(x+2*y)%49,(x+y)%49; k+=1
print('F3: (h_m,y\'_m) = coords of (1+sqrt2)^m for odd m<400 [checked]; ord_49(1+sqrt2) =',k)
assert k==42
# nu0 = +-2 mod 7 when 7|h
for m in range(3,400,6):
    D=mdata(m); h=D['h']
    for a in (2,-2):
        nu0=next(t for t in [((a//2)*pow(4,-1,h))%h+s*h for s in (0,1)] if t%2==1)
        assert nu0%7==((a//2)*2)%7, (m,a,nu0%7)
print('F3: nu0 = a mod 7 (a=+-2) for all m=3 mod 6 < 400 [also: 4 nu0 = a/2 mod h => 4 nu0 = +-1 mod 7 => nu0 = +-2]')
sec=json.load(open('/workspace/bgs-lineJ/logs/sectors_exact.json'))['cases']
for case in (9,15,21,27):
    c4=sec[f'{case},-2']['c']['4']['c_times16']; c0=sec[f'{case},-2']['c']['0']['c_times16']
    assert c4==[-v for v in c0],case
print('F4: c4^(case,-2) = -c0^(case,-2) exactly, all 4 cases')
print('ALL CHECKS PASSED')
