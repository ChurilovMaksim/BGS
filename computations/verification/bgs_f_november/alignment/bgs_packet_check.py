"""Exact tests of the folded trace, its markings, and the triple-contact estimate."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')


from argparse import ArgumentParser
from collections import Counter
from itertools import combinations, product
from math import comb, gcd
import json
from pathlib import Path

import numpy as np


DATA = Path(__file__).with_name("data") / "checks.json"


def apply_map(mapping, position, m):
    sign, shift = mapping
    return (sign*position+shift) % m


def relative_map(reference, mapping, m):
    sign, shift = reference
    other_sign, other_shift = mapping
    return sign*other_sign, sign*(other_shift-shift) % m


def make_slices(m, r, reflection):
    quotient = m//r
    if reflection is None:
        return [tuple(((j+i*quotient) % m, 1) for i in range(r))
                for j in range(quotient)]
    c = reflection
    return [
        tuple(((j+i*quotient) % m, 1) for i in range(r))
        + tuple(((c-j+i*quotient) % m, -1) for i in range(r))
        for j in range(c//2+1, (c+quotient+1)//2)
    ]


def verify_layout(m, r, comparisons):
    reference = comparisons[0]
    relative = [relative_map(reference, f, m) for f in comparisons]
    reflection = next((shift for sign,shift in relative if sign == -1), None)
    slices = make_slices(m, r, reflection)
    assert slices
    used = {t for row in slices for t,_ in row}
    assert len(used) == sum(len(row) for row in slices)
    missing = set(range(m))-used
    assert len(missing) <= 2*r
    if reflection is None:
        assert not missing
    else:
        assert all((2*t-reflection) % (m//r) == 0 for t in missing)
    for row in slices:
        times = {t for t,_ in row}
        for g in relative:
            assert {apply_map(g,t,m) for t in times} == times
        for first,second in combinations(relative,2):
            assert all(apply_map(first,t,m) != apply_map(second,t,m) for t in times)

    horizontal = []
    used_edges = set()
    for before,after in zip(slices,slices[1:]):
        edges = []
        for (source,orientation),(target,new_orientation) in zip(before,after,strict=True):
            assert orientation == new_orientation
            assert (target-source) % m == orientation % m
            earlier = source if orientation == 1 else target
            assert earlier not in used_edges
            used_edges.add(earlier)
            edges.append((source,target,orientation))
        horizontal.append(edges)
    boundary = sorted(set(range(m))-used_edges)
    edge_endpoints = missing | {t for row in (slices[0],slices[-1]) for t,_ in row}
    assert all(t in edge_endpoints and (t+1)%m in edge_endpoints for t in boundary)
    return slices, sorted(missing), horizontal, boundary


def direct_polynomial(m, count, phases, comparisons, slices):
    polynomial = Counter()
    words = tuple(product(range(count), repeat=m))
    for x in words:
        phase_x = sum(phases[x[(t+1)%m]][x[t]] for t in range(m))
        for y in words:
            matches = tuple(sum(x[t] == y[apply_map(f,t,m)] for t in range(m))
                            for f in comparisons)
            over = sum(sum(x[t] == y[apply_map(f,t,m)]
                           for t,_ in row for f in comparisons[:2]) > len(row)
                       for row in slices[1:])
            phase_y = sum(phases[y[(t+1)%m]][y[t]] for t in range(m))
            polynomial[matches,over,(phase_x-phase_y)%count] += 1
    return polynomial


def folded_polynomial(m, count, phases, comparisons, layout):
    slices,missing,horizontal,boundary = layout
    reference = comparisons[0]
    relative = [relative_map(reference,f,m) for f in comparisons]
    arc = len(slices[0])
    states = tuple(product(range(count), repeat=2*arc))
    outside_states = tuple(product(range(count), repeat=2*len(missing)))
    polynomial = Counter()

    def step_phase(x,y,source,target,orientation):
        if orientation == -1:
            source,target = target,source
        x_term = phases[x[target]][x[source]]
        y_term = (phases[y[target]][y[source]] if reference[0] == 1
                  else phases[y[source]][y[target]])
        return x_term-y_term

    for path in product(states, repeat=len(slices)):
        for outside in outside_states:
            x = {}
            y = {}
            for (row,state) in zip(slices,path,strict=True):
                for index,(t,_) in enumerate(row):
                    x[t],y[t] = state[index],state[index+arc]
            for k,t in enumerate(missing):
                x[t],y[t] = outside[k],outside[k+len(missing)]

            slice_counts = [
                tuple(sum(x[t] == y[apply_map(g,t,m)] for t,_ in row) for g in relative)
                for row in slices
            ]
            over = sum(sum(marks[:2]) > arc for marks in slice_counts[1:])
            boundary_counts = tuple(sum(x[t] == y[apply_map(g,t,m)] for t in missing)
                                    for g in relative)
            counts = tuple(boundary_counts[i]+sum(row[i] for row in slice_counts)
                           for i in range(len(comparisons)))
            phase = sum(step_phase(x,y,h,t,sign)
                        for row in horizontal for h,t,sign in row)
            phase += sum(step_phase(x,y,t,(t+1)%m,1) for t in boundary)
            polynomial[counts,over,phase%count] += 1
    return polynomial


def finite_polynomials():
    cases = [
        # A half-turn, a half-turn with both words reverse-compared,
        # and a double-fold with two forwards and two reflections.
        (4,2,3,((1,0),(1,2))),
        (4,2,3,((-1,1),(-1,3))),
        (6,2,2,((1,0),(1,3),(-1,1),(-1,4))),
        (8,2,2,((1,0),(1,4),(-1,1),(-1,5))),
        # Odd and even reflection periods with fixed and unfixed positions.
        (5,1,3,((1,2),(-1,0))),
        (6,1,2,((1,0),(-1,0))),
        (6,1,2,((1,0),(-1,1))),
    ]
    results = []
    for m,r,count,maps in cases:
        # Row and column phases make the entries nonsymmetric at dimension 3.
        phases = [[(x*y+y*y+2*x*x+x)%count for y in range(count)]
                  for x in range(count)]
        layout = verify_layout(m,r,maps)
        direct = direct_polynomial(m,count,phases,maps,layout[0])
        folded = folded_polynomial(m,count,phases,maps,layout)
        assert direct == folded
        assert sum(direct.values()) == count**(2*m)
        results.append({"m":m,"r":r,"alphabet":count,"comparisons":len(maps),
                        "regular_slices":len(layout[0]),"missing_rows":len(layout[1]),
                        "exact_coefficient_slots":len(direct)})
    return results


def test_layouts():
    used = 0
    for m in range(5,81):
        for r in range(1,m//5+1):
            if m%r:
                continue
            b = m//r
            rotations = tuple((1,k*b) for k in range(r))
            assert m//gcd(m,b) == r
            verify_layout(m,r,rotations)
            used += 1
            for c in range(min(4,b)):
                reflections = tuple((-1,c+k*b) for k in range(r))
                verify_layout(m,r,rotations+reflections)
                used += 1
    return used


def mobius_coefficients():
    cases = 0
    for width in range(2,13,2):
        threshold = width//2
        for matches in range(width+1):
            value=sum((-1)**(s-threshold-1)*comb(s-1,threshold)*comb(matches,s)
                      for s in range(threshold+1,matches+1))
            assert value == int(matches>threshold)
            cases += 1
    return cases


def check_cycle_rank():
    count = 0
    for m in range(3,8):
        for rotation in range(1,m):
            order = m//gcd(m,rotation)
            for k in range(1,m+1):
                subsets = tuple(combinations(range(m),k))
                for first,second in product(subsets, repeat=2):
                    parent = list(range(2*m))
                    def root(v):
                        while parent[v]!=v:
                            v = parent[v]
                        return v
                    independent = 0
                    edges = [(v,m+v) for v in first]
                    edges.extend((v,m+(v+rotation)%m) for v in second)
                    for s,t in edges:
                        x,y = root(s),root(t)
                        if x!=y:
                            parent[x]=y
                            independent += 1
                    assert 2*k-independent <= k//order
                    count += 1
    return count


def check_triple_operator():
    results = []
    for n in (3,5):
        grid = np.arange(n)
        u = np.exp(2j*np.pi*np.outer(grid,grid)/n)/np.sqrt(n)
        v = np.diag(np.exp(2j*np.pi*grid**2/n))@u
        w = np.kron(np.kron(u,v),np.kron(u.conj(),v.T))
        labels = np.array(list(product(range(n), repeat=4)))
        tri = (labels[:,0]==labels[:,1]) & (labels[:,0]==labels[:,2])
        norm_bounds = []
        for e in ((0,1),(0,3),(1,3)):
            same = labels[:,e[0]] == labels[:,e[1]]
            value = float(np.linalg.norm(w[np.ix_(same,tri)],ord=2))
            assert value <= n**(-0.5)+1e-12
            norm_bounds.append(value)
        results.append({"N":n,"largest_compression":max(norm_bounds)})
    return results


def boundary_switch():
    """Compare the two-scheme transfer with direct trajectories at m/2."""
    n = 3
    m = 4
    grid = np.arange(n)
    omega = np.exp(2j*np.pi/n)
    u = omega**(np.outer(grid,grid)+grid[None,:]**2+2*grid[:,None]**2)/np.sqrt(n)
    letters = tuple((a,b) for a,b in product(range(n),repeat=2) if a!=b)
    size = len(letters)
    c = np.empty((size,size),dtype=complex)
    d = np.empty((size,size),dtype=complex)
    intensity = abs(u)**2
    for i,(a,b) in enumerate(letters):
        for j,(x,y) in enumerate(letters):
            c[i,j] = u[a,x]*u[b,y]*np.conj(u[a,y]*u[b,x])
            d[i,j] = intensity[a,x]*intensity[b,y]
    assert np.linalg.norm(c,ord=2)<n**(-0.5)+1e-12
    theta = (n-np.sum(intensity**2))/(n*(n-1))
    assert abs(c.sum()/size+theta)<1e-14
    assert abs(d.sum()/size-1+theta)<1e-14
    swap = np.zeros((size,size))
    for i,(a,b) in enumerate(letters):
        swap[i,letters.index((b,a))]=1
    seam = np.kron(np.eye(2),swap)
    unweighted = np.block([[d,c],[c,d]])
    assert np.linalg.norm(unweighted,ord=2)<=1+1e-14
    assert np.max(abs(seam@unweighted-unweighted@seam))<1e-14
    from_transfer = 0j
    for j in range(3):
        z = omega**j
        weighted = np.block([[d,c],[z*c,z*d]])
        from_transfer += np.trace(seam@weighted@weighted)*z**-1/3
    words = tuple(product(range(n),repeat=m))
    from_words = 0j
    for x,y in product(words,repeat=2):
        if any(max(Counter((x[t],x[t+2],y[t],y[t+2])).values())>2
               for t in range(m//2)):
            continue
        if any(sum(x[t]==y[(t+shift)%m] for t in range(m))<m//2 for shift in (0,2)):
            continue
        a = np.prod([u[x[(t+1)%m],x[t]] for t in range(m)])
        b = np.prod([u[y[(t+1)%m],y[t]] for t in range(m)])
        from_words += a*np.conj(b)
    assert abs(from_transfer-from_words)<1e-12
    return {"N":n,"m":m,"real_part":float(from_words.real),
            "imaginary_part":float(from_words.imag)}


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--record",action="store_true")
    parser.add_argument("--verify",action="store_true")
    args = parser.parse_args()
    results = {
        "exact_folded_polynomials": finite_polynomials(),
        "layout_cases": test_layouts(),
        "mobius_cases": mobius_coefficients(),
        "cycle_rank_cases": check_cycle_rank(),
        "triple_operator": check_triple_operator(),
        "two_scheme_boundary": boundary_switch(),
    }
    if args.record:
        DATA.write_text(json.dumps(results,indent=2)+"\n",encoding="utf-8")
    if args.verify:
        expected = json.loads(DATA.read_text(encoding="utf-8"))
        for key,value in results.items():
            if key == "triple_operator":
                for row,old in zip(value,expected[key],strict=True):
                    assert row["N"]==old["N"]
                    assert abs(row["largest_compression"]-old["largest_compression"]) < 1e-11
            elif key == "two_scheme_boundary":
                assert all(abs(v-expected[key][k])<1e-11 for k,v in value.items())
            else:
                assert value==expected[key]
    print(json.dumps(results,indent=2))


if __name__=="__main__":
    main()
