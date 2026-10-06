#!/usr/bin/env python3
"""Exact bounded controls for paired characters, locality and Frostman constants."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path(__file__).resolve().parent / 'paired_phase'

def require(ok, message):
    if not ok:
        raise RuntimeError(message)

def symbolic_checks():
    import sympy as s
    x,y,r,z,w,l=s.symbols('x y r z w l')
    f=lambda x,y,r:-(3*x*x-2*x*(y+r)+3*(y+r)**2)/8
    require(s.expand(f(x+z,y+w,r)-f(x,y,r+w-3*z)-(-2*z*y-2*r*z-2*w*z+3*z*z))==0,'P1')
    require(s.expand(f(x,y,r+4*l)-f(x,y,r)-(l*x-3*l*y-3*l*r-6*l*l))==0,'P2')
    t,N,a,b=s.symbols('t N a b')
    require(s.diff(s.exp(s.I*N*t*(a-b)),t).subs(t,0)==s.I*N*(a-b),'P10 normalized derivative factor')
    return {'P1':True,'P2':True,'literal_derivative_factor_iN':True}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    output=args.output.resolve() if args.output else None
    if output:
        require(not output.is_relative_to(ROOT) or output.is_relative_to(ROOT/'build'),'Output inside maintained source is forbidden')
        output.mkdir(parents=True,exist_ok=True)
        require(not (output/'receipt.json').exists(),'Refusing to overwrite receipt')
    rows=[]
    for name in ('branch_quotient','locality_constants','frostman_constants'):
        p=SOURCE/(name+'.py');before=hashlib.sha256(p.read_bytes()).hexdigest()
        cmd=[sys.executable]+(['-O'] if sys.flags.optimize else [])+[str(p)]
        start=time.monotonic();r=subprocess.run(cmd,text=True,capture_output=True,timeout=180)
        require(r.returncode==0,name+' failed: '+r.stderr[-2000:])
        require(hashlib.sha256(p.read_bytes()).hexdigest()==before,'Source changed during execution')
        d=json.loads(r.stdout)
        if name=='branch_quotient':
            require(sum(x['listed_classes'] for x in d['rows'])==307984,'branch coverage')
            require(sum(x['polarization_pairs'] for x in d['rows'])==1366560,'pairing coverage')
            require(sum(len(x['Gauss_calibrations']) for x in d['rows'])==16,'noncoprime Gauss coverage')
        elif name=='locality_constants':
            require(len(d['rows'])==24,'locality coverage')
        else:
            require(len(d['finite_cycles'])==24,'Frostman cycle coverage')
        rows.append({'name':name,'exit_code':r.returncode,'seconds':time.monotonic()-start,
                     'source_sha256':before,'result':d})
        if output:(output/(name+'.json')).write_text(r.stdout)
    result={'status':'PASS','python_optimized':bool(sys.flags.optimize),'symbolic':symbolic_checks(),'runs':rows,
            'scope':'Exact finite coordinate/phase algebra and rational constants only. No nonlinear infinite-chain proof, pointwise Fourier decay, complete quantum-weight comparison or BGS certified by execution.'}
    if output:(output/'receipt.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
