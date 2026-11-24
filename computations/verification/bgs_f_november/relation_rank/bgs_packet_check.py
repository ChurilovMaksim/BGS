"""Exact checks of cyclotomic projections for independent eigenphases."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from argparse import ArgumentParser
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from spectrum.bgs_packet_check import p_log, rho_at, split
from split_law.bgs_packet_check import SELECTED, primitive_stationary_support, data_at

P = 7
REMOVAL = ((17,2),(45,3),(10,3),(3,1),(38,2),(24,1))


def phase_data(mode, ell, k):
    phase, hessian, tame, depth, root = data_at(mode, ell, k)
    a, _ = split(mode, rho_at(k), P**k)
    ratio = (root+a)*pow(root,-1,P**k)%P**k
    derivative = p_log(ratio,k)
    assert derivative % P == 0
    return phase, derivative//P, hessian, tame, depth


def certificate():
    primitive_stationary_support()
    finite = {}
    for ell in range(3,49,7):
        rows = [phase_data(mode,ell,3) for mode in SELECTED]
        for i,row in enumerate(rows):
            assert row[2:]==((6,4,0) if i<3 else (2,1,1))
        assert tuple(row[0]%49 for row in rows)==(10,3,17,14)
        assert rows[3][1]%7==5
        finite[ell] = [(phase, slope%7) for phase,slope,*_ in rows]

    left = set(ell for ell, _ in REMOVAL)
    steps = []
    for ell, i in REMOVAL:
        phase,derivative = finite[ell][i-1]
        assert derivative
        contenders = [r for r in sorted(left) if finite[r][i-1][0]==phase]
        assert contenders==[ell]
        steps.append((ell,i,phase,derivative))
        left.remove(ell)
    assert not left
    return finite, steps


def verify_lifts(k):
    """Check exact residue injection and six cyclotomic coefficients per group."""
    n = P**k
    conductor = P**(k-2)
    basis = P**(k-1)
    cases = [(set(ell for ell,_ in REMOVAL),4)]
    cases.extend(({ell},i) for ell,i in REMOVAL)
    data = {}
    for ell in range(3,conductor,7):
        if ell%49 not in cases[0][0]:
            continue
        for i, mode in enumerate(SELECTED,1):
            data[ell,i] = phase_data(mode,ell,k)
    count = 0
    for classes,i in cases:
        residue_support = set()
        for ell in range(3,conductor,7):
            if ell%49 not in classes:
                continue
            phase, slope, *_ = data[ell,i]
            reduced = phase % basis
            assert reduced not in residue_support
            residue_support.add(reduced)
            coefficients=set()
            for u in range(6):
                raised = phase_data(SELECTED[i-1], ell+u*conductor,k)
                assert (raised[0]-phase)%n == basis * ((u*slope)%7)
                coefficients.add((raised[0]-reduced)//basis)
            assert len(coefficients)==6
        count+=len(residue_support)
    assert count==12*P**(k-4)
    return {"N":n,"checked_base_projections":count,"rank_lower":180*P**(k-4)}


def compute():
    table, order = certificate()
    # Re and Im of c_1 and its conjugate are independent over Q.
    real,imag = 200,-20
    assert -2*real*imag!=0
    # Fact about F=Q(i,zeta_3): equality sum_h a_h zeta_3^h=0
    # is a_0=a_1=a_2 for a_h in Q(i). Check the small rational
    # kernel which results after adding the deep phase condition.
    rows = []
    for h in range(2):
        for left,right in ((real,real),(imag,-imag)):
            row=[0]*6
            row[2*h:2*h+2]=[left,right]
            row[4:6]=[-left,-right]
            rows.append(row)
    rows.append([1]*6)
    row_reduced = [[x%101 for x in row[:5]] for row in rows]
    determinant=1
    for i in range(5):
        j=next(j for j in range(i,5) if row_reduced[j][i])
        if i!=j:
            row_reduced[i],row_reduced[j]=row_reduced[j],row_reduced[i]
            determinant=-determinant
        pivot=row_reduced[i][i]
        determinant=(determinant*pivot)%101
        for j in range(i+1,5):
            factor=row_reduced[j][i]*pow(pivot,-1,101)%101
            row_reduced[j]=[(a-factor*b)%101 for a,b in
                            zip(row_reduced[j],row_reduced[i])]
    assert determinant%101
    return {"stationary_table":table, "removal_steps":order,
            "quotient_matrix":rows, "minor_mod_101":determinant,
            "computational_lifts":[verify_lifts(k) for k in (4,5,6,7)]}


if __name__=="__main__":
    parser=ArgumentParser(description=__doc__)
    parser.add_argument("--verify",action="store_true")
    args=parser.parse_args()
    path=Path(__file__).resolve().parent/"data/certificates.json"
    encoded=json.dumps(compute(),indent=2)+"\n"
    if args.verify:
        assert path.read_text()==encoded
        print("Stationary phase table, elimination order and six-lift projections verified.")
    else:
        path.write_text(encoded)
        print("Wrote",path)
