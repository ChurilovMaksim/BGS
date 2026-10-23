#!/usr/bin/env python3
"""Exact rational nondegenerate phase Jacobian, plus the singular scalar control."""
from fractions import Fraction as F
import json, platform, sys
from exact_unitaries import Q,eye,adj,mul,rational_unitary


def inverse(a):
    n=len(a);b=[list(row)+ident for row,ident in zip(a,eye(n))]
    for j in range(n):
        p=next(i for i in range(j,n) if b[i][j].abs2())
        b[p],b[j]=b[j],b[p]
        pivot=b[j][j];b[j]=[v/pivot for v in b[j]]
        for i in range(n):
            if i!=j:
                c=b[i][j];b[i]=[x-c*y for x,y in zip(b[i],b[j])]
    return [row[n:] for row in b]


def determinant(a):
    b=[list(row) for row in a];ans=Q(F(1));n=len(b)
    for j in range(n):
        p=next((i for i in range(j,n) if b[i][j].abs2()),None)
        if p is None:return Q()
        if p!=j:b[p],b[j]=b[j],b[p];ans=-ans
        pivot=b[j][j];ans=ans*pivot
        for i in range(j+1,n):
            c=b[i][j]/pivot
            for k in range(j,n):b[i][k]=b[i][k]-c*b[j][k]
    return ans


def sub(a,rows,cols):return [[a[i][j] for j in cols] for i in rows]
def subtract(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def diag(values):return [[v if i==j else Q() for j in range(len(values))] for i,v in enumerate(values)]


def main():
    n=6;m=2;W=rational_unitary(n);A=[0,1];E=[2,3,4,5]
    assert mul(W,adj(W))==eye(n)
    # At zero: independent complex Jacobian columns, not just a real numerical rank.
    L=[[W[a][e]*W[e][b] for e in E] for a in A for b in A]
    det0=determinant(L);assert det0.abs2()>0
    z=[Q(F(3,5),F(4,5)),Q(F(5,13),F(12,13)),Q(F(-8,17),F(15,17)),Q(F(7,25),F(-24,25))]
    Z=diag(z);Qe=sub(W,E,E);B=sub(W,A,E);Ce=sub(W,E,A)
    R=inverse(subtract(eye(4),mul(Z,Qe)))
    C=mul(B,R);X=mul(mul(R,Z),Ce)
    U=add(sub(W,A,A),mul(B,X));assert mul(U,adj(U))==eye(m)
    gram=mul(adj(C),C)
    assert gram==subtract(add(R,adj(R)),eye(4))
    iunit=Q(F(0),F(1));tangent=[]
    for e in range(4):
        dU=[[iunit*C[a][e]*X[e][b] for b in range(2)] for a in range(2)]
        H=[[C[a][e]*C[b][e].conj() for b in range(2)] for a in range(2)]
        assert mul(dU,adj(U))==[[iunit*x for x in row] for row in H]
        assert H[0][0].y==H[1][1].y==0
        assert H[0][1].conj()==H[1][0]
        tangent.append([Q(H[0][0].x),Q(H[1][1].x),Q(H[0][1].x),Q(H[0][1].y)])
    det_boundary=determinant(tangent);assert det_boundary.y==0 and det_boundary.abs2()>0
    # Scalar negative control: |W_aa|=r -> 1 makes the phase law converge to a point.
    # Fourier coefficient of order k is r^k, hence no TV continuity at r=1.
    controls=[{'r_exact':str(F(j,j+1)), 'first_Fourier_exact':str(F(j,j+1)),
               'TV_distance_from_delta_1_exact':'1'} for j in [1,3,15,255]]
    out={'status':'passed','python':platform.python_version(),
         'N':6,'external_m':2,'zero_complex_minor_squared_exact':str(det0.abs2()),
         'boundary_real_minor_exact':str(det_boundary.x),
         'unitarity_exact':True,'positive_rank_one_derivative_identity_exact':True,
         'resolvent_Gram_identity_exact':True,'singular_scalar_negative_control':controls,
         'non_claims':['A finite nonzero minor does not prove parameter-dependent TV continuity.',
                       'No uniform lower bound for all phase Jacobians or Haar universality.']}
    with open(sys.argv[1],'w') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps({'status':'passed','N':n,'m':m,'exact_full_rank_at_zero_and_boundary':True}))


if __name__=='__main__':main()
