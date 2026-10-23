"""Exact and certified checks of all clusters of defect one, with neutral clusters."""
import itertools
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path
from maximal_check import onecycle, read_kernels, quotient_bivariate, q_moments, root_bracket


def mixed_port_jet(r, b, moments):
    e = r+3*b
    order = [(0,1,2),(1,2,0),(2,0,1),(1,0,2),(2,1,0),(0,2,1)]
    weights = [-34,-1,-1,4,4,4]
    local = []
    for choices in itertools.product(range(6), repeat=b):
        pi = list(range(r))
        weight = 1
        for index, choice in enumerate(choices):
            base = r+3*index
            pi += [base+x for x in order[choice]]
            weight *= weights[choice]
        local.append((pi, weight))
    count = 0
    weighted = 0
    for rest in itertools.permutations(range(1,e)):
        word = (0,)+rest
        if any(tuple(x-base for x in word if base <= x < base+3) not in ((0,1,2),(1,2,0),(2,0,1)) for base in range(r,e,3)):
            continue
        g = [0]*e
        for a,c in zip(word,word[1:]+word[:1]):
            g[a] = c
        count += 1
        for pi, weight in local:
            if onecycle([g[pi[i]] for i in range(e)]):
                weighted += weight
    assert count == math.factorial(e-1)//2**b
    direct = F(weighted, math.factorial(r)*math.factorial(b)*12**b)
    predicted = F(math.factorial(e-1)*(-1)**b, math.factorial(r)*math.factorial(b)*2**b)*moments[b]
    assert direct == predicted
    return {'one_port_clusters':r,'three_port_clusters':b,'ports':e,'shuffles':count,
            'local_choices':len(local),'jet_direct':str(direct),'jet_character_formula':str(predicted)}


def exp_bounds(w, order=32):
    term = F(1)
    total = term
    for k in range(1, order+1):
        term *= w/k
        total += term
    next_term = term*w/(order+1)
    remainder = next_term/(1-w/(order+2))
    return total, total+remainder


def integrand_bounds(tau,q):
    lo,hi = root_bracket(tau,q)
    elo = exp_bounds(lo)[0]
    ehi = exp_bounds(hi)[1]
    vlo = elo*(1+lo+q*lo*lo/2)/(1+2*hi+3*q*hi*hi/2)-1
    vhi = ehi*(1+hi+q*hi*hi/2)/(1+2*lo+3*q*lo*lo/2)-1
    scale = 2**56
    a,b = vlo*scale,vhi*scale
    return a.numerator//a.denominator, -((-b.numerator)//b.denominator)


def integral_bounds(tau,K=1024):
    # A+1=e^w*tau/(w*D); its derivative in q at fixed tau is negative.
    points = []
    for i in range(K+1):
        x = F(i,K)
        points.append(integrand_bounds(tau,2+3*x/2+x*x/2))
    return F(sum(a for a,b in points[1:]), K*2**56), F(sum(b for a,b in points[:-1]), K*2**56)


def limiting_series(tau,moments,H=80):
    by_h = {}
    for h in range(1,H+1):
        coefficient = F(0)
        for b in range(h//2+1):
            for n in range(h-2*b+1):
                r = h-2*b-n
                coefficient += F(math.factorial(r+3*b+2*n-1)*(-1)**(b+n),
                                 math.factorial(r)*math.factorial(b)*2**b*math.factorial(n)*math.factorial(h-1))*moments[b]
        by_h[h] = coefficient
    assert by_h[1] == 0
    assert by_h[2] == F(-17,12)
    series = sum(c*tau**h for h,c in by_h.items())
    tail = F(1091,444)*(tau/F(13,100))**(H+1)
    return series,tail,by_h


def all_finite_sums(G,cases):
    M = max(m for m,N in cases)
    power = {(0,0):1}
    totals = [F(0)]*len(cases)
    counted = [0]*len(cases)
    for b in range(M//3+1):
        if b:
            out = {}
            for (i,j),a in power.items():
                for (k,l),c in G.items():
                    if i+k <= M:
                        key = i+k,j+l
                        out[key] = out.get(key,0)+a*c
            power = {key:a for key,a in out.items() if a}
        H = {}
        for (i,j),a in power.items():
            if j%2 == 0:
                H[i] = H.get(i,F(0))+F(a,j+1)
        H = {i:a/72**b for i,a in H.items() if a}
        for r in range((M-3*b)//4+1):
            A = {}
            for i,a in H.items():
                for k in range(r+1):
                    q = i+4*r+k
                    if q <= M:
                        A[q] = A.get(q,F(0))+a*F(math.comb(r,k),2**r)
            h0 = r+2*b
            e0 = r+3*b
            K = [math.comb(s+h0-1,h0-1) for s in range(M+1)] if h0 else [1]+[0]*M
            for n in range((M-3*b-4*r)//2+1):
                if n:
                    prefix = []
                    running = 0
                    for a in K:
                        running += a
                        prefix.append(running)
                    K = [sum(prefix[s-k] for k in range(4) if s >= k) for s in range(M+1)]
                if not h0+n:
                    continue
                base = F(math.factorial(e0+2*n-1)*(-1)**n,
                         math.factorial(r)*math.factorial(b)*2**b*4**n*math.factorial(n))
                for index,(m,N) in enumerate(cases):
                    if m < 4*r+3*b+2*n:
                        continue
                    coefficient = sum(a*K[m-2*n-i] for i,a in A.items() if i <= m-2*n)
                    totals[index] += m*base*coefficient/N**(h0+n)
                    counted[index] += 1
    return [{'m':m,'N':N,'ratio':str(F(m,N)),'terms':counted[i],
             'exact_value':str(totals[i]),'display_value':float(totals[i])} for i,(m,N) in enumerate(cases)]


def main(destination):
    u,v,t = read_kernels()
    G = quotient_bivariate(u,v,t)
    moments = q_moments(40)
    print('checking mixed one-port and three-port gluing',flush=True)
    jets = [mixed_port_jet(r,b,moments) for r,b in [(1,1),(2,1),(3,2)]]
    assert jets[0]['jet_direct'] == '-35/4'
    print('checking triple all-order series against certified exponential-cubic integral',flush=True)
    checks = []
    coefficients = None
    for tau in (F(1,20),F(1,10)):
        series,tail,coefficients = limiting_series(tau,moments)
        lo,hi = integral_bounds(tau)
        assert lo-tail <= series <= hi+tail
        checks.append({'tau':str(tau),'series_h_max':80,'series_exact':str(series),'series_display':float(series),
                       'tail_bound_exact':str(tail),'tail_bound_display':float(tail),
                       'integral_interval_exact':[str(lo),str(hi)],'integral_interval_display':[float(lo),float(hi)]})
    print('checking finite-N original sums without defect or decoration truncations',flush=True)
    finite = all_finite_sums(G,[(16,169),(62,625),(96,961)])
    for a in finite:
        lo,hi = integral_bounds(F(a['m'],a['N']),K=256)
        a['limit_interval_display'] = [float(lo),float(hi)]
        tau = F(a['m'],a['N'])
        s = tau/F(13,100)
        rate_bound = F(10*1091,444*a['m'])*s*s/(1-s)**3
        assert lo-rate_bound <= F(a['exact_value']) <= hi+rate_bound
        a['proven_finite_N_error_bound_exact'] = str(rate_bound)
        a['proven_finite_N_error_bound_display'] = float(rate_bound)
    data = {'status':'passed_exact_gluing_and_certified_triple_resummation_checks',
            'mixed_port_checks':jets,'coefficients_h_1_to_12':{str(h):str(coefficients[h]) for h in range(1,13)},
            'limit_comparisons':checks,'finite_N_all_terms':finite,
            'certification':{'root_bisections':64,'exponential_taylor_order':32,
                             'rounding':'outward to 2^-56','integral_subdivisions':1024,
                             'majorant_endpoint':'13/100','majorant_bound':'1091/444'},
            'scope':'All defect-one connected clusters in any number, and all neutral clusters. Defect-two and higher connected clusters are excluded; this is not the full form factor or BGS.'}
    Path(destination).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'status':data['status'],'limit_displays':[a['series_display'] for a in checks],
                      'finite_displays':[a['display_value'] for a in finite]}))


if __name__ == '__main__':
    main(sys.argv[1])
