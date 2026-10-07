#!/usr/bin/env python3
"""Independent exact transfer audit in the coordinate-pair basis.

The torus projector is a proved exact 4th-root average for m<=3.
This differs from a Laurent-symbolic coefficient implementation.
"""
from itertools import product
from pathlib import Path
import argparse,json
from independent_checks import require,add,mul,cj,scale,ROOTS

ZERO=(0,0)
ONE=(1,0)


def eye(n):
    return [[ONE if i==j else ZERO for j in range(n)] for i in range(n)]


def matmul(a,b):
    n=len(a);c=[[ZERO for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if a[i][k]!=ZERO:
                for j in range(n):
                    if b[k][j]!=ZERO:c[i][j]=add(c[i][j],mul(a[i][k],b[k][j]))
    return c


def trace(a):
    z=ZERO
    for i in range(len(a)):z=add(z,a[i][i])
    return z


def unitary():
    v=[(1,0),(1,1),(2,-1)];w=[(1,1),(2,0),(1,0)]
    h=[[add(scale(ONE,4*int(i==j)),scale(mul(v[i],cj(v[j])),-1))
        for j in range(3)] for i in range(3)]
    k=[[add(scale(ONE,7*int(i==j)),scale(mul(w[i],cj(w[j])),-2))
        for j in range(3)] for i in range(3)]
    u=matmul(h,k);d=28
    adj=[[cj(u[j][i]) for j in range(3)] for i in range(3)]
    require(matmul(u,adj)==[[scale(ONE,d*d*int(i==j)) for j in range(3)]
                          for i in range(3)],'auxiliary U must be exactly unitary')
    require(all(z!=ZERO for row in u for z in row),'auxiliary U must be dense')
    require(u!=adj,'auxiliary U must be non-Hermitian')
    return u,d


def path_tables(u,m):
    table={};fibers={};pairs=0;mask_checks=0
    words=list(product(range(3),repeat=m))
    amplitudes={}
    for x in words:
        z=ONE
        for i in range(m):z=mul(z,u[x[i]][x[(i+1)%m]])
        amplitudes[x]=z
    for x in words:
        for y in words:
            c=tuple((v-t)%3 for t,v in zip(x,y))
            h=sum(t!=0 for t in c);s=sum(c[i]!=c[(i+1)%m] for i in range(m))
            occ=tuple(x.count(j)-y.count(j) for j in range(3))
            key=(h,s,occ);a=mul(amplitudes[x],cj(amplitudes[y]))
            table[key]=add(table.get(key,ZERO),a)
            fkey=(c,any(occ));fibers[fkey]=add(fibers.get(fkey,ZERO),a)
            # For every possible low-switch cap, literal low/high masks partition
            # the high-Hamming offcharge set and survive cyclic rotation.
            cr=c[1:]+c[:1];xr=x[1:]+x[:1];yr=y[1:]+y[:1]
            require(sum(t!=0 for t in cr)==h and
                    sum(cr[i]!=cr[(i+1)%m] for i in range(m))==s and
                    tuple(xr.count(j)-yr.count(j) for j in range(3))==occ,
                    'simultaneous-cycle invariant mask')
            for cap in range(m+1):
                high=any(occ) and h>49*m//100
                low=high and s<=cap;dense=high and s>cap
                require(not(low and dense) and (low or dense)==high,'literal mask partition')
                mask_checks+=1
            pairs+=1
    return table,fibers,pairs,mask_checks


def direct_value(table,m,a,b,q,theta,derivative=False,off=False,hvalue=None,scap=None):
    result=ZERO
    for (h,s,occ),z in table.items():
        if off and not any(occ):continue
        if hvalue is not None and h!=hvalue:continue
        if scap is not None and s>scap:continue
        if derivative and s==0:continue
        phase=ROOTS[(q*h+sum(x*y for x,y in zip(theta,occ)))%4]
        coefficient=(s*a**(s-1)*b**(m-s+1) if derivative
                     else a**s*b**(m-s))
        result=add(result,scale(mul(phase,z),coefficient))
    return result


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True)
    ap.add_argument('--inject-failure',action='store_true');args=ap.parse_args()
    if args.inject_failure:require(False,'injected switch failure under optimization')
    u,d=unitary();basis=list(product(range(3),repeat=2));dim=len(basis)
    transfer=[[mul(u[j][k],cj(u[l][n])) for k,n in basis] for j,l in basis]
    blocks=0
    # Exact twisted zero-run endpoint identities for every 4th-root theta.
    for theta in product(range(4),repeat=3):
        for c in (1,2):
            for j in range(3):
                val=ZERO
                for k in range(3):val=add(val,mul(u[j][k],cj(u[(j+c)%3][k])))
                val=mul(ROOTS[(theta[j]-theta[(j+c)%3])%4],val)
                require(val==ZERO,'twisted B(c,0) must kill constant on right');blocks+=1
            for k in range(3):
                val=ZERO
                for j in range(3):val=add(val,mul(u[j][k],cj(u[j][(k+c)%3])))
                require(val==ZERO,'B(0,c) must kill constant on left');blocks+=1
    totals={'pairs':0,'mask_partitions':0,'matrix_trace_identities':0,
            'matrix_derivative_identities':0,'exact_torus_projections':0,
            'exact_Hamming_extractions':0,'weighted_dense_mask_subtractions':0,
            'twisted_zero_run_endpoints':blocks,'identity_reductions':0,
            'zero_run_replacements':0,'constant_zero_exclusions':0}
    witness=None
    # Parameter numerator/denominator includes endpoints and two interiors.
    for m in range(1,4):
        table,fibers,pairs,masks=path_tables(u,m)
        totals['pairs']+=pairs;totals['mask_partitions']+=masks
        for c in product(range(3),repeat=m):
            for theta in product(range(4),repeat=3):
                raw=eye(3);centered=eye(3)
                for i in range(m):
                    ci=c[i];di=c[(i+1)%m]
                    block=[[mul(ROOTS[(theta[j]-theta[(j+ci)%3])%4],
                                mul(u[j][k],cj(u[(j+ci)%3][(k+di)%3])))
                            for k in range(3)] for j in range(3)]
                    scaled=[[scale(z,3) for z in row] for row in block]
                    if ci==di==0:
                        scaled=[[add(z,scale(ONE,-d*d)) for z in row] for row in scaled]
                    raw=matmul(raw,block);centered=matmul(centered,scaled)
                difference=add(scale(trace(raw),3**m),scale(trace(centered),-1))
                if any(c):
                    require(difference==ZERO,'zero-run centered replacement in actual cyclic product')
                    totals['zero_run_replacements']+=1
                else:
                    require(difference==scale(ONE,(3*d*d)**m),
                            'constant-zero word must retain exactly one identity trace')
                    totals['constant_zero_exclusions']+=1
        for (c,off),value in fibers.items():
            if off and any(c) and sum(c)%3==0 and value!=ZERO and witness is None:
                allvalue=add(value,fibers.get((c,False),ZERO))
                if allvalue!=value:
                    witness={'m':m,'charge_word':c,'off_numerator':value,
                             'full_numerator':allvalue,'denominator':d**(2*m)}
        for a,b in ((0,1),(1,3),(2,3),(1,1)):
            denominator=d*d*b
            q_off=[];q_der=[]
            for q in range(4):
                torus_sum=ZERO;torus_der=ZERO;at_zero=None;der_zero=None
                for theta in product(range(4),repeat=3):
                    mat=[[ZERO]*dim for _ in range(dim)];delta=[[ZERO]*dim for _ in range(dim)]
                    for row,(j,l) in enumerate(basis):
                        c=(l-j)%3;phase=ROOTS[(q*int(c!=0)+theta[j]-theta[l])%4]
                        for col,(k,n) in enumerate(basis):
                            switch=c!=(n-k)%3
                            z=mul(phase,transfer[row][col])
                            mat[row][col]=scale(z,a if switch else b)
                            delta[row][col]=z if switch else ZERO
                    # Both M and M* fix the scalar identity. Using its unnormalized
                    # coordinate vector avoids any square-root representation.
                    for row,(j,l) in enumerate(basis):
                        val=ZERO
                        for col,(k,n) in enumerate(basis):
                            if k==n:val=add(val,mat[row][col])
                        require(val==scale(ONE,denominator*int(j==l)),'M identity')
                    for col,(k,n) in enumerate(basis):
                        val=ZERO
                        for row,(j,l) in enumerate(basis):
                            if j==l:val=add(val,mat[row][col])
                        require(val==scale(ONE,denominator*int(k==n)),'M adjoint identity')
                    totals['identity_reductions']+=1
                    power=eye(dim)
                    for _ in range(m-1):power=matmul(power,mat)
                    value=trace(matmul(power,mat))
                    deriv=scale(trace(matmul(power,delta)),m*b)
                    require(value==direct_value(table,m,a,b,q,theta),'rooted matrix trace')
                    require(deriv==direct_value(table,m,a,b,q,theta,True),'marked derivative')
                    totals['matrix_trace_identities']+=1;totals['matrix_derivative_identities']+=1
                    torus_sum=add(torus_sum,value);torus_der=add(torus_der,deriv)
                    if theta==(0,0,0):at_zero=value;der_zero=deriv
                require(all(x%64==0 for x in torus_sum+torus_der),'exact torus denominator')
                off=add(at_zero,scale(tuple(x//64 for x in torus_sum),-1))
                der=add(der_zero,scale(tuple(x//64 for x in torus_der),-1))
                require(off==direct_value(table,m,a,b,q,(0,0,0),off=True),'occupation projection')
                require(der==direct_value(table,m,a,b,q,(0,0,0),derivative=True,off=True),'derivative occupation projection')
                totals['exact_torus_projections']+=2;q_off.append(off);q_der.append(der)
            for h in range(m+1):
                extracted=ZERO;d_extracted=ZERO
                for q in range(4):
                    extracted=add(extracted,mul(ROOTS[(-q*h)%4],q_off[q]))
                    d_extracted=add(d_extracted,mul(ROOTS[(-q*h)%4],q_der[q]))
                expected=direct_value(table,m,a,b,0,(0,0,0),off=True,hvalue=h)
                expected_d=direct_value(table,m,a,b,0,(0,0,0),off=True,hvalue=h,derivative=True)
                require(extracted==scale(expected,4),'exact Hamming extraction')
                require(d_extracted==scale(expected_d,4),'exact derivative Hamming extraction')
                totals['exact_Hamming_extractions']+=2
                if h>49*m//100:
                    for cap in range(m+1):
                        low=direct_value(table,m,a,b,0,(0,0,0),off=True,hvalue=h,scap=cap)
                        dense_table={k:v for k,v in table.items() if k[1]>cap}
                        dense=direct_value(dense_table,m,a,b,0,(0,0,0),off=True,hvalue=h)
                        require(add(low,dense)==expected,'weighted high-Hamming residual subtraction')
                        totals['weighted_dense_mask_subtractions']+=1
    require(witness is not None,'missing checksum-zero partial-fiber control')
    result={'arithmetic':'exact Gaussian integer numerators with common rational denominators',
            'unitary_dimension':3,'word_lengths':[1,2,3],'theta_grid_order':4,
            'torus_exactness':'Each occupation exponent is in [-m,m] and m<4; root averaging kills exactly nonzero exponents.',
            'q_grid_exactness':'Degree m<4, so four roots extract each Hamming coefficient without alias.',
            'counts':totals,'checksum_zero_partial_fiber':witness,
            'non_claims':['No asymptotic gap for this auxiliary unitary is asserted.',
                          'No literal-tau quantum norms are computed.',
                          'No undamped boundary estimate is proved by these identities.']}
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
