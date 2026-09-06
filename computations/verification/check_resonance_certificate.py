#!/usr/bin/env python3
"""Small strict replay checker for real quadratic zero certificates.

No optimization and no search are performed. Row coefficients are independently
reconstructed by the C++ quadratic-ring program when --cpp is supplied. A
successful replay proves the stated implication over R, not positive BGS.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from pathlib import Path
import subprocess
from resonance_nondegeneracy_certificate import orbit_forms, canonical_bytes

class InvalidCertificate(ValueError):
    pass

def require(condition: bool, message: str) -> None:
    if not condition:
        raise InvalidCertificate(message)

def replay(steps: list, rows: list, dimension: int, zeros: set,
           products: set, nonzero: set, counters: dict) -> None:
    require(type(steps) is list, 'A proof must be a list.')
    for instruction in steps:
        require(not (zeros & nonzero), 'Instructions continue after a contradiction.')
        require(type(instruction) is list and instruction, 'Malformed instruction.')
        op = instruction[0]
        require(op in ('P','S','D','F'), 'Unknown deduction rule.')
        counters[op] += 1
        if op in ('P','S'):
            require(len(instruction)==2 and type(instruction[1]) is int, 'Malformed row instruction.')
            index=instruction[1]
            require(0 <= index < len(rows), 'Row index out of range.')
            remaining=[(i,e,j,f,a) for i,e,j,f,a in rows[index]['terms']
                       if i not in zeros and j not in zeros and (i,j) not in products]
            require(bool(remaining), 'An empty equation proves no new fact.')
            if op=='P':
                require(len(remaining)==1 and remaining[0][0]!=remaining[0][2], 'Not a sole cross monomial.')
                i,_,j,_,_=remaining[0]
                products.add((i,j))
            else:
                single_square=len(remaining)==1 and remaining[0][0]==remaining[0][2]
                hermitian_squares=all(i==j and e==-f for i,e,j,f,a in remaining)
                common_sign=all(a>0 for *_,a in remaining) or all(a<0 for *_,a in remaining)
                require(single_square or (hermitian_squares and common_sign),
                        'Not a sole complex square or sign-definite Hermitian squares.')
                zeros.update(i for i,*_ in remaining)
        elif op=='D':
            require(len(instruction)==3,'Malformed division instruction.')
            i,j=instruction[1:]
            require(type(i) is int and type(j) is int and 0<=i<dimension and 0<=j<dimension,
                    'Invalid variable indices.')
            require(i in nonzero and tuple(sorted((i,j))) in products,'Division has no nonzero pivot/product.')
            require(j not in zeros,'Division repeats an existing fact.')
            zeros.add(j)
        else:
            require(len(instruction)==3 and type(instruction[1]) is int,'Malformed refutation.')
            i=instruction[1]
            require(0<=i<dimension and i not in zeros and i not in nonzero,'Invalid refutation pivot.')
            local_z,local_p=set(zeros),set(products)
            replay(instruction[2],rows,dimension,local_z,local_p,nonzero|{i},counters)
            require(bool(local_z & (nonzero|{i})),'Refutation does not reach a contradiction.')
            zeros.add(i)

def validate(certificate: dict, rows: list) -> dict:
    require(certificate.get('schema')==1 and certificate.get('matrix')==[[3,2],[4,3]],'Wrong schema/matrix.')
    require(certificate.get('status')=='CERTIFICATE','Object is not a completed certificate.')
    n=certificate['variables']
    require(certificate.get('basis')=='complex_fourier' and certificate['dimension']==2*n,'Wrong real/complex dimensions.')
    require(n==2*certificate['radius']*(certificate['radius']+1),'Wrong Fourier dimension.')
    require(len(rows)==certificate['orbit_equations'],'Wrong number of rows.')
    require(hashlib.sha256(canonical_bytes(rows)).hexdigest()==certificate['equation_sha256'],
            'Coefficient table hash mismatch.')
    zeros,products=set(),set()
    counters={op:0 for op in ('P','S','D','F')}
    replay(certificate['proof'],rows,n,zeros,products,set(),counters)
    require(zeros==set(range(n)), 'The proof does not eliminate all coefficients.')
    return counters

def mutation_controls(cert: dict, rows: list) -> int:
    bad=[]
    x=copy.deepcopy(cert);x['proof']=[['F',0,[]]];bad.append((x,rows))
    x=copy.deepcopy(cert);x['proof']=[['D',0,1]];bad.append((x,rows))
    x=copy.deepcopy(cert);x['proof']=[['S',len(rows)]];bad.append((x,rows))
    x=copy.deepcopy(cert);r=copy.deepcopy(rows);r[0]['terms'][0][4]+=1;bad.append((x,r))
    for c,r in bad:
        try:
            validate(c,r)
        except InvalidCertificate:
            continue
        raise AssertionError('An invalid mutated certificate was accepted.')
    return len(bad)

def proof_text(cert: dict) -> str:
    lines=[f"RESONANCE_COMPLEX_V1 {cert['radius']}"]
    def emit(steps):
        for ins in steps:
            if ins[0]=='F':
                lines.append(f'F {ins[1]}');emit(ins[2]);lines.append('E')
            else:
                lines.append(' '.join(map(str,ins)))
    emit(cert['proof']);lines.append('X')
    return '\n'.join(lines)+'\n'

def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('certificate',type=Path)
    p.add_argument('--cpp',type=Path)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    cert=json.loads(args.certificate.read_text())
    modes,rows=orbit_forms(cert['radius'])
    independent='NOT_RUN'
    if args.cpp:
        text=subprocess.check_output([str(args.cpp.resolve()),str(cert['radius'])],text=True,timeout=40)
        other=json.loads(text)
        require(other['modes']==[list(x) for x in modes],'Independent frequency enumeration differs.')
        require(other['rows']==rows,'Independent quadratic-ring coefficient construction differs.')
        independent='PASS'
    rules=validate(cert,rows)
    negative=mutation_controls(cert,rows)
    wire=args.certificate.with_suffix('.proof')
    wire.write_text(proof_text(cert))
    replay_result=None
    if args.cpp:
        replay_result=json.loads(subprocess.check_output([str(args.cpp.resolve()),str(cert['radius']),'--proof',str(wire)],text=True,timeout=40))
        require(replay_result.get('status')=='PASS' and {k:replay_result['rules'].get(k,0) for k in rules}==rules,'Independent C++ proof replay disagrees.')
        for invalid in ('RESONANCE_COMPLEX_V1 '+str(cert['radius'])+'\nF 0\nE\nX\n',
                        'RESONANCE_COMPLEX_V1 '+str(cert['radius'])+'\nD 0 1\nX\n'):
            badfile=wire.with_suffix('.invalid');badfile.write_text(invalid)
            completed=subprocess.run([str(args.cpp.resolve()),str(cert['radius']),'--proof',str(badfile)],capture_output=True,text=True,timeout=40)
            badfile.unlink()
            require(completed.returncode!=0,'C++ accepted an invalid proof.')
        negative+=2
    out={'status':'PASS','radius':cert['radius'],'dimension':2*len(modes),'complex_variables':len(modes),
         'orbit_equations':len(rows),'rules':rules,'negative_controls_rejected':negative,
         'independent_cpp_coefficients':independent,'independent_cpp_proof_replay':replay_result,
         'proof_text_sha256':hashlib.sha256(wire.read_bytes()).hexdigest(),
         'certificate_sha256':hashlib.sha256(args.certificate.read_bytes()).hexdigest(),
         'equation_sha256':cert['equation_sha256'],
         'source_sha256':{Path(__file__).name:hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
         'scope':'Exact coefficient construction and real-algebra proof replay; no Lean, external priority or BGS claim.'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':
    main()
