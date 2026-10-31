import sys; sys.path.insert(0,'/workspace/bgs-lineI/dom_v3'); from law import mdata
tab={}; bad=0
for m in range(9,4000,6):
    D=mdata(m); h=D['h']; yp=D['yp']
    nus=next(x for x in [((-1)*pow(4,-1,h))%h+s*h for s in (0,1)] if x%2==1)
    assert (-4*nus-1)%h==0
    k=((-4*nus-1)//h)*yp%8
    if tab.setdefault(m%8,k)!=k: bad+=1
print('kappa(m) for m=9..3999, m=3 mod 6: depends only on m mod 8?', bad==0, tab)
