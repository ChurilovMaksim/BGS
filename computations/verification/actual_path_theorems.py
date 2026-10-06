#!/usr/bin/env python3
"""Portable exact finite controls. Python standard library only.
No analytic asymptotic, actual-tau numerical limit, or BGS certification.
Failure checks are explicit and remain active under python -O.
"""
from fractions import Fraction as F
from itertools import product
import json, sys, platform

def require(test, label):
    if not test:
        raise RuntimeError(label)

def mm(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]

def trace_power(a,m):
    r=[[int(i==j) for j in range(len(a))] for i in range(len(a))]
    for _ in range(m): r=mm(r,a)
    return sum(r[i][i] for i in range(len(a)))

def main():
    out={'arithmetic':'Python arbitrary-precision integers and Fraction; no floating arithmetic',
         'boundary':'Finite identities only; no asymptotic or BGS certificate',
         'python':platform.python_version(),'optimized':not __debug__}
    # Cyclic seven-interval overlap: all displacements, all listed odd N.
    checks=0
    for n in range(15,252,2):
        s=[(2*j*n+7)//14 for j in range(8)]
        blocks=[set(range(s[j],s[j+1])) for j in range(7)]
        for d in range(n):
            count=sum(len(b.intersection((x+d)%n for x in b)) for b in blocks)
            require(count==max(n-7*min(d,n-d),0),f'overlap {n} {d}')
            checks+=1
    out['overlap']={'odd_N':[15,251],'dimensions':119,'all_displacements':checks}
    # Exact eighth-root arithmetic in Z[z]/(z^4+1).
    def z8(k):
        k%=8
        v=[0]*4;v[k%4]=1 if k<4 else -1
        return v

    def add(vs): return [sum(v[j] for v in vs) for j in range(4)]
    for n in (1,3,5,7):
        for t in range(8):
            lhs=add([z8(-3*n*r*r+2*t*r) for r in range(4)])
            rhs=[2*v for v in z8(-3*n+3*n*t*t)]
            require(lhs==rhs,f'Gauss {n} {t}')
    # This is exhaustive mod 8 coverage of an identity depending only on N,t mod8.
    out['gauss_identity']={'arithmetic':'exact cyclotomic basis 1,z,z²,z³ with z^4=-1','N_mod_8':[1,3,5,7],'t_mod_8':list(range(8)),'instances':32,'coverage':'all odd N and integer t via proved dependence only on residues modulo 8'}
    count=0
    for n in range(3,82,2):
        iv=pow(8,-1,n)
        for b in range(n):
            for x in range(n):
                xp=(x+4*b)%n
                require((-3*iv*(x*x-xp*xp)-3*b*(x+2*b))%n==0,'Weyl covariance')
                count+=1
    out['covariance']={'odd_N':[3,81],'x_b_pairs':count,'boundary':'finite modular check; analytic algebra is in the proof'}
    # Fourier coefficient: Gaussian-rational complex pairs.
    def cm(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
    def sc(s,a):return(s*a[0],s*a[1])
    I=[(F(1),F(0)),(F(0),F(1)),(F(-1),F(0)),(F(0),F(-1))]
    B={0:F(1,100),1:F(-1,200),-1:F(-1,200),7:F(1,200),-7:F(1,200),6:F(-1,400),-6:F(-1,400),8:F(-1,400),-8:F(-1,400)}
    coeff=[]
    for r in range(4):
        for s in range(4):
            # Store pi times phi_t's Fourier coefficients. HJ factor is 1/(2pi).
            tab={}
            for branch,swapped,sign in [(r,False,1),(s,True,-1)]:
                for k,b in B.items():
                    for ell in [-1,1]:
                        alpha=(F(-3,5),F(-4*ell,5))
                        c=sc(sign*b/4,cm(alpha,I[(branch*ell)%4]))
                        key=(4*k-3*ell,ell)
                        if swapped:key=key[::-1]
                        prev=tab.get(key,(F(0),F(0)));tab[key]=(prev[0]+c[0],prev[1]+c[1])
            # d_x d_y multiplier = -pi² ab/4 for quarter-frequency labels a,b.
            mixed_over_pi=sc(F(-25,4),tab.get((25,1),(F(0),F(0))))
            expected=sc(F(-1,128),cm((F(-3,5),F(-4,5)),I[r]))
            require(mixed_over_pi==expected,'mixed Fourier coefficient')
            require(sum(z*z for z in mixed_over_pi)==F(1,128**2),'mixed magnitude')
            coeff.append({'r':r,'s':s,'mixed_coefficient_divided_by_pi':[str(x) for x in mixed_over_pi]})
    # pi>3 suffices to certify remainder 10^50 tau² < (pi/128) tau.
    tau=F(1,10**80)
    require(10**50*tau*tau<F(3,128)*tau,'specified-time remainder comparison')
    require(2*10**9*tau+10**50*tau*tau<F(1,4),'alias upper bound')
    out['mixed_coefficient']={'all_16_pairs':coeff,'remainder_comparison':'exact rational, using pi>3','boundary':'verifies finite coefficient and comparison, not the analytic bound 10^50 itself'}
    # Rational, non-symmetric 3x3 orthogonal matrix: product of two Householders.
    v=[1,2,2];w=[2,-1,2]
    def hh(v):return [[9*int(i==j)-2*v[i]*v[j] for j in range(3)] for i in range(3)]
    A=mm(hh(v),hh(w));den=81**2
    require(mm(A,list(map(list,zip(*A))))==[[den*int(i==j) for j in range(3)] for i in range(3)],'unitarity')
    require(A!=list(map(list,zip(*A))),'non-symmetric witness')
    P=[[x*x for x in row] for row in A];Q=[[A[i][j]*A[j][i] for j in range(3)] for i in range(3)];q=max(map(max,P))
    counts=[]
    for m in range(1,8):
        words=list(product(range(3),repeat=m))
        amp={}
        for x in words:
            z=1
            for j in range(m):z*=A[x[j]][x[(j+1)%m]]
            amp[x]=z
        D=0;group={};revsum=0;weighted=0;overlap=0;repeat=0
        for x in words:
            rots={x[k:]+x[:k] for k in range(m)};rev=x[::-1]
            rrots={rev[k:]+rev[:k] for k in range(m)}
            D+=len(rots)*amp[x]**2
            group.setdefault(min(rots),[]).append(amp[x])
            revsum+=sum(amp[x]*amp[y] for y in rrots-rots)
            weighted+=len(rots)*amp[x]*amp[rev]
            overlap+=len(rots&rrots)*amp[x]**2
            repeat+=(m-len(rots))*amp[x]*amp[rev]
        require(D==sum(sum(g)**2 for g in group.values()),'cyclic orbit assembly')
        require(D<=m*trace_power(P,m),'cyclic trace inequality')
        require(revsum==weighted-overlap,'reverse orbit subtraction')
        require(m*trace_power(Q,m)==weighted+repeat,'reverse trace multiplicity')
        if m>=2:
            require(abs(revsum-m*trace_power(Q,m))<=2*m*m*3*q**(m//2)*den**(m-m//2),'reverse error bound')
        # Independently check every individual reflection and its precise loop count.
        reflection_counts=[]
        for k in range(m):
            fixed=[x for x in words if all(x[j]==x[(k-j)%m] for j in range(m))]
            value=sum(amp[x]**2 for x in fixed)
            if m%2: exponent=m//2+1
            elif k%2: exponent=m//2+1
            else: exponent=m//2
            require(value<=3*q**exponent*den**(m-exponent),'reflection case bound')
            reflection_counts.append(len(fixed))
        counts.append({'m':m,'words':len(words),'cyclic_orbits':len(group),'reflection_fixed_word_counts':reflection_counts})
    out['rational_word_checks']={'U_numerator':A,'U_denominator':81,'dimension':3,'m':[1,7],'all_words':counts,'boundary':'one exact rational unitary, not all unitaries'}
    # Same-coordinate off-diagonal phases needed for P, separately from reversal.
    phase_checks=[]
    for r in range(4):
        for t in range(4):
            if r==t:continue
            cr=sc(F(-1,128),cm((F(-3,5),F(-4,5)),I[r]))
            ct=sc(F(-1,128),cm((F(-3,5),F(-4,5)),I[t]))
            difference=(cr[0]-ct[0],cr[1]-ct[1])
            norm2=sum(x*x for x in difference)
            require(norm2>=F(2,128**2),'same-coordinate phase certificate')
            phase_checks.append({'r':r,'s':t,'coefficient_divided_by_pi':[str(x) for x in difference],'squared_magnitude_divided_by_pi_squared':str(norm2)})
    eps=F(2,10**66)
    require(2*eps+eps*eps<F(1,10**64),'leading amplitude comparison')
    out['position_chain_coefficients']={'all_12_pairs':phase_checks,'amplitude_comparison':'exact rational; transport exponential bound is analytic'}
    # Complex rational unitary, not a symmetric real-only check.
    v=[1,2,3]
    H=[[F(int(i==j))-F(v[i]*v[j],7) for j in range(3)] for i in range(3)]
    phases=I[:3]
    CU=[[tuple(sum(H[i][k]*H[k][j]*phases[k][c] for k in range(3)) for c in range(2)) for j in range(3)] for i in range(3)]
    def conj(z):return(z[0],-z[1])
    def ca(a,b):return(a[0]+b[0],a[1]+b[1])
    CP=[[sum(c*c for c in z) for z in row] for row in CU]
    for i,j in product(range(3),repeat=2):
        z=(F(0),F(0))
        for k in range(3):z=ca(z,cm(conj(CU[k][i]),CU[k][j]))
        require(z==(F(i==j),F(0)),'complex unitary columns')
    def power(A,n):
        R=[[F(i==j) for j in range(3)] for i in range(3)]
        for _ in range(n):R=mm(R,A)
        return R
    marked=[]
    ports=[a for a in product(range(3),repeat=3) if len(set(a))==3]
    for lengths in [(0,0,0),(0,1,2),(1,2,3)]:
        mats=[power(CP,L) for L in lengths]
        for uniform in range(3):
            z=(F(0),F(0))
            for a in ports:
                for b in product(range(3),repeat=3):
                    term=(F(1),F(0))
                    for i in range(3):
                        weight=F(1,3) if i==uniform else mats[i][a[i]][b[i]]
                        term=cm(term,sc(weight,cm(CU[b[i]][a[(i+1)%3]],conj(CU[b[i]][a[(i-1)%3]]))))
                    z=ca(z,term)
            require(z==(F(0),F(0)),'marked uniform-link cancellation')
            marked.append({'lengths':lengths,'uniform_link':uniform,'exact_value':[str(c) for c in z]})
    out['marked_complex_contraction']={'dimension':3,'unitary':'H diag(1,i,-1) H, H=I-vv^T/7, v=(1,2,3)','checks':marked,'boundary':'finite exact marked contraction, including zero lengths; not an unmarked family'}
    if '--inject-failure' in sys.argv: require(False,'intentional fault injection')
    print(json.dumps(out,indent=2))

if __name__ == '__main__':
    main()
