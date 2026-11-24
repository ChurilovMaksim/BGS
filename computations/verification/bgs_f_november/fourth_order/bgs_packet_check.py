"""Check the arithmetic of the fourth-order trace bounds over powers of seven."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from argparse import ArgumentParser
from collections import Counter
from itertools import product
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from research.coefficients import raw_symbol
from spectrum.bgs_packet_check import rho_at, split

P = 7


def value(x, depth):
    if x == 0:
        return depth
    result = 0
    while result < depth and x % P == 0:
        result += 1
        x //= P
    return result


def orbit(depth):
    modulus = P**depth
    order = 3 * P**(depth-1)
    gamma = (3+2*rho_at(depth)) % modulus
    powers = [pow(gamma,j,modulus) for j in range(order)]
    assert len(set(powers)) == order and pow(gamma,order,modulus) == 1
    assert all(1+x != modulus for x in powers)
    return modulus, powers


def single_orbit(depth):
    modulus, powers = orbit(depth)
    invert = {x:pow(x,-1,modulus) for x in powers}
    marginal = Counter()
    for a,x in enumerate(powers):
        for b,z in enumerate(powers):
            y = (x+z-1) % modulus
            closed = y in invert and (1-invert[x]+invert[y]-invert[z])%modulus == 0
            expected = (x-1)*(z-1)%modulus == 0
            assert expected == closed
            if closed:
                assert y == x*z%modulus
                assert powers[(a+b)%len(powers)] == y
                marginal[a] += 1
    for a,x in enumerate(powers):
        depth_x = value(x-1,depth)
        expected = len(powers) if a == 0 else P**depth_x
        assert marginal[a] == expected
    count = sum(marginal.values())
    assert count == (6*depth-1)*P**(depth-1)
    return {"orbit_length":len(powers),"ordered_closed_words":count,
            "marginal_histogram":dict(sorted(Counter(marginal.values()).items()))}


def exact_labels():
    labels = sorted(raw_symbol())
    for label in labels:
        v = int(label[0]%P == label[1]%P == 0)
        divisor = P**v
        a,b = split(tuple(x//divisor for x in label),3,P)
        assert a%P and b%P
    return labels


def check_pair(depth, v, w):
    # Modulus common to the original Weyl identities after removal of min depth.
    left_depth = int(v[0]%P == v[1]%P == 0)
    right_depth = int(w[0]%P == w[1]%P == 0)
    common = min(left_depth, right_depth)
    reduced = depth-common
    modulus, powers = orbit(reduced)
    rho = rho_at(reduced)
    dv,dw = left_depth-common, right_depth-common
    a,b = split(tuple(i//P**left_depth for i in v),rho,modulus)
    c,d = split(tuple(i//P**right_depth for i in w),rho,modulus)
    eta = a*d*pow(b*c,-1,modulus)%modulus
    invert = {x:pow(x,-1,modulus) for x in powers}
    actual_count = 0
    for X in powers:
        s = value(X-1,reduced)
        distinct_depth = min(s+dv,reduced)
        mod_segment = P**(reduced-dw)
        if distinct_depth < dw:
            candidates = {}
        else:
            delta = (a*pow(c,-1,modulus)*P**dv*(X-1)//P**dw)%mod_segment
            candidates = {
                Y:[Z for Z in powers if (Y-Z-delta)%mod_segment == 0]
                for Y in powers
            }
        # Independently determine the allowable Z from the first coordinate.
        for Y in powers:
            expected = set()
            for Z in candidates.get(Y, []):
                first = P**dv*a*(1-X)+P**dw*c*(Y-Z)
                second = P**dv*b*(1-invert[X])+P**dw*d*(invert[Y]-invert[Z])
                assert first%modulus == 0
                actual = second%modulus == 0
                transformed = P**dv*(X-1)*(Y*Z-eta*X)%modulus == 0
                assert actual == transformed
                if actual:
                    expected.add(Z)
                if distinct_depth < reduced:
                    quadratic_modulus = P**(reduced-distinct_depth)
                    assert transformed == ((Y*Y-delta*Y-eta*X)%quadratic_modulus == 0)
            actual_count += len(expected)
    return actual_count


def mixed_cases(labels):
    summary = {}
    # All ordered pairs at N=49, plus pairs covering both depths at N=343.
    for v,w in product(labels,repeat=2):
        result = check_pair(2,v,w)
        summary[f"{v}:{w}"] = result
    sample = ((0,7),(0,-7),(0,1),(0,2),(1,0),(-1,-7))
    larger = {f"{v}:{w}":check_pair(3,v,w) for v,w in product(sample,repeat=2)}
    return {"all_at_49":summary,"sample_at_343":larger}


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--verify",action="store_true")
    args = parser.parse_args()
    result = {"same_orbit":{k:single_orbit(k) for k in (1,2,3,4)},
              "mixed_orbits":mixed_cases(exact_labels())}
    encoded = json.dumps(result,indent=2)+"\n"
    destination = ROOT/"fourth_order/data/arithmetic.json"
    if args.verify:
        assert destination.read_text() == encoded
        print("Fourth-order conic identities and the mixed quadratic reductions verified.")
    else:
        destination.write_text(encoded)
        print("Wrote",destination)
