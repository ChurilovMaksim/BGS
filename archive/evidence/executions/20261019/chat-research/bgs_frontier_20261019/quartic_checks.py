import itertools as it
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path


def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def integral(p):return sum(F(a,i+1) for i,a in enumerate(p))


def cycle_type(p):
    seen=set();lengths=[]
    for i in range(len(p)):
        if i in seen:continue
        v=i;k=0
        while v not in seen:seen.add(v);k+=1;v=p[v]
        lengths.append(k)
    return tuple(sorted(lengths))


def divide_one_minus_z(pol):
    current=F(0);out=[]
    for i in range(max(pol)+1):current+=pol.get(i,F(0));out.append(current)
    assert out[-1]==0
    return out[:-1]


def character_jet(perms,polys):
    result=[];weights=[]
    for pi,pol in zip(perms,polys):
        weight=-sum(q*a for q,a in pol.items());weights.append(weight)
        factor=[F(1)]
        for length in cycle_type(pi):
            local=[F((-1)**i*math.comb(length,i)) for i in range(length+1)]
            local[-1]-=(-1)**length
            factor=mul(factor,local)
        if len(result)<len(factor):result += [F(0)]*(len(factor)-len(result))
        for i,a in enumerate(factor):result[i]+=weight*a
    while result and result[-1]==0:result.pop()
    return result,weights


def onecycle(p):
    x=p[0];count=1
    while x!=0 and count<len(p):x=p[x];count+=1
    return x==0 and count==len(p)


def direct_mixed_gluing(sizes,weights,denominators,divide=1):
    n=sum(sizes);groups=[];base=0
    local_perms=[]
    for size in sizes:
        groups.append(tuple(range(base,base+size)))
        local_perms.append(list(it.permutations(range(size))));base+=size
    choices=[]
    for indices in it.product(*(range(len(p)) for p in local_perms)):
        pi=[];weight=1;base=0
        for j,index in enumerate(indices):
            pi += [base+a for a in local_perms[j][index]]
            weight *= weights[j][index];base+=sizes[j]
        choices.append((pi,weight))
    total=0;cycles=0
    for rest in it.permutations(range(1,n)):
        word=(0,)+rest
        valid=True
        for group in groups:
            sub=tuple(x for x in word if x in group)
            if sub not in tuple(group[j:]+group[:j] for j in range(len(group))):valid=False;break
        if not valid:continue
        cycles+=1;gamma=[0]*n
        for a,b in zip(word,word[1:]+word[:1]):gamma[a]=b
        for pi,weight in choices:
            if onecycle([gamma[pi[i]] for i in range(n)]):total+=weight
    assert cycles==math.factorial(n-1)//math.prod(math.factorial(e-1) for e in sizes)
    return F(total,divide*math.prod(denominators)),cycles,len(choices)


def moments(H):
    powers=[]
    for base,maximum in (([7,20],H//2),([4,3,1],H//2),([12,25,19,4],H//3)):
        values=[[1]]
        for _ in range(maximum):values.append(mul(values[-1],base))
        powers.append(values)
    A,B,C=powers;out={}
    for b in range(H//2+1):
        for k in range((H-2*b)//3+1):
            bc=mul(B[b],C[k])
            for s in range((H-2*b-3*k)//2+1):
                out[s,b,k]=integral(mul(bc,A[s]))/2**(b+k)/12**s
    return out


def limiting_coefficients(H):
    values=moments(H);facts=[math.factorial(i) for i in range(2*H+1)];out={}
    for h in range(1,H+1):
        total=F(0)
        for k in range(h//3+1):
            for b in range((h-3*k)//2+1):
                for s in range((h-3*k-2*b)//2+1):
                    left=h-3*k-2*b-2*s
                    denominator=facts[s]*facts[b]*facts[k]*facts[h-1]*2**b*6**k
                    numerator=values[s,b,k]
                    for n in range(left+1):
                        r=left-n
                        total += F(facts[h+b+k+n-1]*(-1)**(b+k+n),denominator*facts[r]*facts[n])*numerator
        out[h]=total
    assert out[1]==0 and out[2]==0 and out[3]==-3
    return out


def root_bounds(tau,q3,q4,bits=64):
    lo,hi=F(0),tau
    for _ in range(bits):
        w=(lo+hi)/2
        if w+w*w+q3*w**3/2+q4*w**4/6<=tau:lo=w
        else:hi=w
    return lo,hi


def exp_bounds(w):
    term=total=F(1)
    for k in range(1,33):term*=w/k;total+=term
    remainder=term*w/33/(1-w/34)
    return total,total+remainder


def parameters(x):return F(7,12)+5*x/3,2+3*x/2+x*x/2,6+25*x/2+19*x*x/2+2*x**3


def certified_integral(tau,K=1024):
    total_lo=0;total_hi=0;scale=2**56
    for j in range(K):
        vl,a,b=parameters(F(j,K));vh,A,B=parameters(F(j+1,K))
        lo=root_bounds(tau,A,B)[0];hi=root_bounds(tau,a,b)[1]
        elo=exp_bounds(lo+vl*lo*lo)[0];ehi=exp_bounds(hi+vh*hi*hi)[1]
        numerator_lo=1+lo+a*lo*lo/2+b*lo**3/6
        numerator_hi=1+hi+A*hi*hi/2+B*hi**3/6
        denominator_lo=1+2*lo+3*a*lo*lo/2+2*b*lo**3/3
        denominator_hi=1+2*hi+3*A*hi*hi/2+2*B*hi**3/3
        lower=(elo*numerator_lo/denominator_hi-1)*scale
        upper=(ehi*numerator_hi/denominator_lo-1)*scale
        total_lo+=lower.numerator//lower.denominator
        total_hi+=-((-upper.numerator)//upper.denominator)
    return F(total_lo,K*scale),F(total_hi,K*scale)


def main(destination):
    source=json.loads(Path('two_port_v2_run/result.json').read_text())
    four=json.loads(Path('kernel_run/result.json').read_text())
    three=json.loads(Path('dependencies/three_port_reference.json').read_text())
    baseline=four['summary'][0]['four_port_polynomials']
    for entry in four['summary']:
        assert entry['four_port_polynomials']==baseline
        assert entry['all_open_channels_zero_at_one']
        classes={}
        for pi,pol in zip(entry['permutations'],entry['four_port_polynomials']):
            key=cycle_type(pi)
            if key in classes:assert classes[key]==pol
            else:classes[key]=pol
    for entry in source['summary']:assert entry['polynomials']==source['summary'][0]['polynomials']
    p4=[{int(q):F(a) for q,a in pol.items()} for pol in baseline]
    p2=[{int(q):F(a) for q,a in pol.items()} for pol in source['summary'][0]['polynomials']]
    old=[{int(q):F(a) for q,a in pol.items()} for pol in three['summary'][0]['polynomials']]
    perms3=list(it.permutations(range(3)));perms4=list(it.permutations(range(4)))
    p3=[old[0],{q:a/3 for q,a in old[3].items()},{q:a/3 for q,a in old[3].items()},old[1],old[2],{q:a/3 for q,a in old[3].items()}]
    jet3,weights3=character_jet(perms3,p3);jet4,weights4=character_jet(perms4,p4)
    assert jet3==[F(-2),F(-3,2),F(-1,2)]
    assert jet4==[F(-6),F(-25,2),F(-19,2),F(-2)]
    C2=sum(abs(a) for pol in p2 for a in pol.values())
    C3=sum(abs(a) for pol in p3 for a in divide_one_minus_z(pol))
    C4=sum(abs(a) for pol in p4 for a in divide_one_minus_z(pol))
    assert (C2,C3,C4)==(F(121,12),F(53,9),F(1349,16))
    w=F(1,6);rho=F(1,9);k3=C3/2;k4=C4/6
    assert rho+w*w+k3*w**3+k4*w**4<w
    contraction=2*w+3*k3*w*w+4*k4*w**3
    assert contraction==F(4349,5184)
    assert w+C2*w*w==F(193,432)
    assert (1/(1-w-C2*w*w))/(1-contraction)-1<11
    print('checking mixed-port gluing directly',flush=True)
    w3=[int(a*12) for a in weights3];w4=[int(a*48) for a in weights4]
    w2=[17,-10]
    q3=[F(2),F(3,2),F(1,2)];q4=[F(6),F(25,2),F(19,2),F(2)];v=[F(7,12),F(5,3)]
    jobs=[([3,4],[w3,w4],[12,48],1,60*integral(mul(q3,q4))),
          ([4,4],[w4,w4],[48,48],2,70*integral(mul(q4,q4))),
          ([2,4],[w2,w4],[12,48],1,-20*integral(mul(v,q4)))]
    gluing=[]
    for sizes,weights,denoms,divide,expected in jobs:
        direct,cycles,choices=direct_mixed_gluing(sizes,weights,denoms,divide)
        assert direct==expected,(sizes,direct,expected)
        gluing.append({'ports':sizes,'cyclic_shuffles':cycles,'local_choices':choices,'direct_value':str(direct),'character_integral_value':str(expected)})
    print('checking exact limiting coefficients and certified quartic integrals',flush=True)
    H=48;coefficients=limiting_coefficients(H);checks=[]
    for tau in (F(1,20),F(2,25)):
        series=sum(a*tau**h for h,a in coefficients.items());tail=11*(9*tau)**(H+1)
        lo,hi=certified_integral(tau)
        assert lo-tail<=series<=hi+tail
        checks.append({'tau':str(tau),'order_cutoff':H,'series_exact':str(series),'series_display':float(series),
                       'tail_bound_exact':str(tail),'tail_bound_display':float(tail),
                       'certified_integral_interval_exact':[str(lo),str(hi)],'certified_integral_interval_display':[float(lo),float(hi)]})
    print('checking the coefficient bound used for the uniform finite-N rate',flush=True)
    coefficient_checks=0
    for h in range(2,31):
        for m in range(9,65):
            for q in range(h-1,5*h+1):
                actual=math.factorial(h-1)*math.comb(m-q+h-1,h-1) if q<=m else 0
                difference=m**(h-1)-actual
                assert 0<=difference<=5*h*(h-1)*m**(h-2)
                coefficient_checks+=1
    data={'status':'passed_central_kernel_mixed_gluing_and_certified_quartic_checks',
          'kernel_L1_constants':{'C2':str(C2),'C3':str(C3),'C4':str(C4)},
          'character_jets':{'three_port':[str(a) for a in jet3],'four_port':[str(a) for a in jet4]},
          'majorant':{'rho':'1/9','fixed_point_disk':'1/6','contraction':'4349/5184','bound':11},
          'mixed_port_gluing':gluing,'coefficients_through_h12':{str(h):str(coefficients[h]) for h in range(1,13)},
          'certified_limits':checks,'integer_coefficient_bound_checks':coefficient_checks,
          'certification':{'root_bisections':64,'exponential_order':32,'interval_cells':1024,'rounding':'outward to 2^-56'},
          'scope':'All neutral clusters and all open positive clusters of individual defect one or two, in arbitrary numbers; for m>8 closed residual clusters are absent. Higher individual defects, full mixed hierarchy and frozen transfer remain open.'}
    Path(destination).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'status':data['status'],'leading_coefficients':[str(coefficients[h]) for h in range(1,5)],
                      'limit_displays':[a['series_display'] for a in checks],'mixed_gluing':gluing}))


if __name__=='__main__':main(sys.argv[1])
