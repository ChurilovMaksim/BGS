"""Independent Fourier-versus-Jacobi finite diagnostics for BGS-FM-005."""
import importlib.util
import json
from math import gcd, pi
from pathlib import Path
import numpy as np
from scipy.linalg import expm
import argparse

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    root=Path(__file__).resolve().parents[2]
    spec=importlib.util.spec_from_file_location('frozen',root/'supplement/fixed_map/secular-route/exact_structure_checks.py')
    module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    rows=[]
    for n in [3,5,7,9,15,19,21,23,35,49,63,77]:
        a,m=module.frozen_matrices(n)
        x=np.arange(n); q=2*pi*x/n
        r=(1-np.cos(7*q))*(1+np.cos(q))
        diag=np.cos(7*q)+r/10+r*np.sin(q)/100-.1
        y=(x+pow(2,-1,n))%n; qm=2*pi*y/n
        bonds=(1-np.cos(7*qm))*(1+np.cos(qm))/200
        exact_zero=(7*y)%n==0
        assert np.count_nonzero(exact_zero)==gcd(n,7)
        bonds[exact_zero]=0
        b=np.diag(diag).astype(complex)
        for j in range(n):
            b[j,(j+1)%n]=((-3-4j)/5)*bonds[j]
            b[(j+1)%n,j]=np.conj(b[j,(j+1)%n])
        err=float(np.max(abs(a-b))); assert err<1e-12
        zeros=np.flatnonzero(exact_zero)
        gaps=np.diff(np.r_[zeros,zeros[0]+n]); assert np.all(gaps==n//gcd(n,7))
        variance=float(np.trace(a@a).real/n)
        if n>=19: assert abs(variance-66033/160000)<1e-12
        t=.4
        kick=expm(1j*t*a)-np.eye(n)
        singular=np.linalg.svd(kick,compute_uv=False)
        B=79/50
        margins=[]
        if n>=19:
            for rank in [0,1,n//20,n//10]:
                actual=float(np.linalg.norm(singular[rank:])/np.sqrt(n))
                lower=2*t/pi*np.sqrt(max(0,66033/160000-rank*B*B/n))
                assert actual+1e-12>=lower
                margins.append({'rank':rank,'actual_best_residual':actual,'lower_bound':float(lower)})
        rows.append({'N':n,'zero_bonds':int(sum(exact_zero)),'chain_lengths':gaps.tolist(),'assembly_error':err,'variance':variance,'approximation_checks':margins})
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps({'status':'passed','scope':'floating diagnostics; moderate t=.4, not frozen-tau numerics','cases':rows},indent=2)+'\n')
    print(json.dumps({'status':'passed','cases':len(rows),'max_assembly_error':max(r['assembly_error'] for r in rows),'variance_checks':sum(r['N']>=19 for r in rows),'bound_checks':sum(len(r['approximation_checks']) for r in rows)}))

if __name__ == "__main__":
    main()
