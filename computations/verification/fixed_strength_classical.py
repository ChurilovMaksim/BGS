#!/usr/bin/env python3
"""Independent ODE checks of the classical conjugacy and Hamiltonian signs.

Analytic Anosov/mixing assertions are proved in the companion note, not by
finite trajectories. ODE tolerances below are not interval enclosures.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
import hashlib
import json
import math
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from fixed_strength_locality import RADIUS, ASYMMETRY, bump, wrapped, symbol

T=np.array([[3.,2.],[4.,3.]])
M=T.T


def beta_prime(t: float) -> float:
    return 0. if abs(t)>=1 else -2*t*float(bump(t))/(1-t*t)**2


def gradient_g(z: np.ndarray) -> np.ndarray:
    q,p=z
    u=float(wrapped(q-.25))/RADIUS
    v=float(wrapped(q+.25))/RADIUS
    w=float(wrapped(p))/RADIUS
    au=float(bump(u));av=float(bump(v));bw=float(bump(w))
    a=au*(1+ASYMMETRY*u)+av*(1-ASYMMETRY*v)
    da=(beta_prime(u)*(1+ASYMMETRY*u)+ASYMMETRY*au
        +beta_prime(v)*(1-ASYMMETRY*v)-ASYMMETRY*av)/RADIUS
    db=beta_prime(w)/RADIUS
    return np.array([da*bw,a*db])


def gradient_f(z: np.ndarray) -> np.ndarray:
    return gradient_g(z)-T@gradient_g(M@z)


def flow(z: np.ndarray, time: float, residual: bool=False) -> np.ndarray:
    gradient=gradient_f if residual else gradient_g
    def rhs(_t,y):
        q,p=gradient(y)
        return [-p,q]
    if time==0: return z.copy()
    answer=solve_ivp(rhs,(0,time),z,method='DOP853',rtol=3e-12,atol=3e-13,
                     max_step=max(abs(time)/20,1e-6))
    if not answer.success: raise RuntimeError(answer.message)
    return answer.y[:,-1]


def report() -> dict:
    points=[np.array(z) for z in ((.25,0),(.27,.01),(.75,-.02),
                                (.11,.28),(.0,.0),(.13,.37))]
    points += [np.linalg.solve(M,z) for z in points[:3]]
    gradient_checks=[]
    for z in points:
        h=1e-7
        approx=np.array([(float(symbol(*(z+h*e)))-float(symbol(*(z-h*e))))/(2*h)
                         for e in np.eye(2)])
        error=float(np.max(abs(approx-gradient_g(z))))
        assert error<2e-6
        gradient_checks.append(error)
    rows=[]
    for kappa in (-.125,.01,.125):
        time=kappa/(2*math.pi)
        for z in points:
            direct=M@flow(z,time,True)
            conjugated=flow(M@flow(z,time),-time)
            error=float(np.max(abs(wrapped(direct-conjugated))))
            assert error<2e-8
            displacement=float(np.max(abs(wrapped(direct-M@z))))
            # Hamiltonian conservation is checked independently along its flow.
            end=flow(z,time,True)
            energy=lambda w: float(symbol(*w)-symbol(*(M@w)))
            conservation=abs(energy(end)-energy(z))
            assert conservation<2e-9
            rows.append({'kappa':kappa,'point':z.tolist(),
                         'conjugacy_circle_error':error,
                         'nonlinear_displacement_from_M':displacement,
                         'Hamiltonian_conservation_error':conservation})
    assert max(r['nonlinear_displacement_from_M'] for r in rows)>.01
    return {'producer':'computations/verification/fixed_strength_classical.py',
            'status':'PASS','scope':'Finite ODE/gradient sign and conjugacy checks, not proof of Anosov dynamics or certified trajectory intervals.',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'gradient_errors':gradient_checks,'checks':rows}


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    data=report();text=json.dumps(data,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text)
    else: print(text,end='')

if __name__=='__main__':main()
