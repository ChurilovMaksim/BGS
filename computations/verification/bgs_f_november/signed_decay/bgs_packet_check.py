"""Verify the time progressions used by the signed-resolvent estimate."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from argparse import ArgumentParser
from collections import defaultdict
from itertools import product
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from fourth_order.bgs_packet_check import orbit, value
from spectrum.bgs_packet_check import rho_at, split

P = 7
SAMPLES = ((0, 1), (0, -1), (0, 7), (0, -7), (1, 0), (0, 2))


def progression_count(k, label1, label2):
    depth1 = int(all(x % P == 0 for x in label1))
    depth2 = int(all(x % P == 0 for x in label2))
    common = min(depth1, depth2)
    depth = k-common
    n, powers = orbit(depth)
    order_small = len(powers)
    order = 3*P**(k-1)
    rho = rho_at(depth)
    a,b = split(tuple(x//P**depth1 for x in label1),rho,n)
    c,d = split(tuple(x//P**depth2 for x in label2),rho,n)
    d1,d2 = depth1-common,depth2-common
    eta = a*d*pow(b*c,-1,n)%n
    ratio = a*pow(c,-1,n)%n
    inv = {x:pow(x,-1,n) for x in powers}
    target_mod = P**(depth-d2)
    frequencies_by_residue = defaultdict(list)
    for z,x in enumerate(powers):
        frequencies_by_residue[x%target_mod].append(z)
    result = defaultdict(int)
    for h,X in enumerate(powers):
        s = value(X-1,depth)
        r = s+d1
        if r < d2:
            result["impossible_first"] += 1
            continue
        shift = ratio*P**d1*(X-1)//P**d2
        if r >= depth:
            result["vanishing_outer_pair"] += 1
            continue
        l = depth-r
        module = P**l
        step = 3*P**(l-1)
        y_classes = set()
        z_classes = set()
        distinct = 0
        for y,Y in enumerate(powers):
            for z in frequencies_by_residue[(Y-shift)%target_mod]:
                Z = powers[z]
                exact = (P**d1*b*(1-inv[X])+P**d2*d*(inv[Y]-inv[Z]))%n == 0
                quad_y = (Y*Y-shift*Y-eta*X)%module == 0
                quad_z = (Z*Z+shift*Z-eta*X)%module == 0
                assert exact == quad_y == quad_z
                if exact:
                    y_classes.add(y%step)
                    z_classes.add(z%step)
                    distinct += 1
        inverse_gamma = pow((3+2*rho)%module,-1,module)
        # Each time class has the same reduction along the progression.
        for z in y_classes | z_classes:
            assert pow(inverse_gamma,z+step,module) == pow(inverse_gamma,z,module)
        if r>d2:
            result["regular"] += 1
            assert len(y_classes) <= 2 and len(z_classes) <= 2
        else:
            result["exceptional"] += 1
            discr = (shift*shift+4*eta*X)%module
            b0 = value(discr,l)
            # 2 * 7^(b0/2) bound, squared to remain in integer arithmetic.
            assert max(len(y_classes),len(z_classes))**2 <= 4*P**b0
        result["completed_words"] += distinct
        result["max_progression_length"] = max(result["max_progression_length"], order//step)
    return dict(result)


def compute():
    results = {}
    for k in (2,3,4):
        one = defaultdict(int)
        for v,w in product(SAMPLES,repeat=2):
            result = progression_count(k,v,w)
            for key,count in result.items():
                if key=="max_progression_length":
                    one[key]=max(one[key],count)
                else:
                    one[key]+=count
        results[k]=dict(one)
    return results


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--verify",action="store_true")
    args = parser.parse_args()
    result = compute()
    target = ROOT/"signed_decay/data/progressions.json"
    out = json.dumps(result,indent=2)+"\n"
    if args.verify:
        assert target.read_text()==out
        print("Exact mixed closures and their time progressions verified at 49, 343, and 2401.")
    else:
        target.write_text(out)
        print("Wrote",target)
