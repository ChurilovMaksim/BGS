"""Independent exact rational tests of the full ordered operator construction.

No author numerical code or symmetric-space implementation is imported.
The finite range does not prove any universal or asymptotic assertion.
"""
import itertools
import json
from pathlib import Path
import sympy as sp


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def tensor(matrices):
    result = sp.ones(1, 1)
    for matrix in matrices:
        result = sp.kronecker_product(result, matrix)
    return result


def flat(matrix):
    return sp.Matrix(list(matrix))


def rational_unitary(n):
    # Distinct deterministic reflectors, different from the author's vectors.
    a = sp.Matrix(range(1, n + 1))
    b = sp.Matrix([2*j*j + 1 for j in range(n)])
    return (sp.eye(n)-2*a*a.T/(a.dot(a))) * (sp.eye(n)-2*b*b.T/(b.dot(b)))


def objects(n, m):
    words = list(itertools.product(range(n), repeat=m))
    index = {word: j for j, word in enumerate(words)}
    dimension = n**m
    permutations = []
    for p in itertools.permutations(range(m)):
        op = sp.zeros(dimension)
        for col, word in enumerate(words):
            op[index[tuple(word[p[j]] for j in range(m))], col] = 1
        permutations.append(op)
    # Physical operator Gram retains all finite-N relations in Schur-Weyl.
    gram_all = sp.Matrix([[sum(a.multiply_elementwise(b)) for b in permutations] for a in permutations])
    pivots = gram_all.rref()[1]
    basis = [permutations[j] for j in pivots]
    z = sp.Matrix.hstack(*[flat(a) for a in basis])
    gz = z.T*z
    local = [sp.ones(n,1)]
    for k in range(1, n):
        local.append(sp.Matrix([1]*k+[-k]+[0]*(n-k-1)))
    labels = [word for word in words if any(word)]
    diag = sp.Matrix.hstack(*[tensor([local[j] for j in word]) for word in labels])
    mass = diag.T*diag
    overlap = sp.Matrix([[sum(a[j,j]*diag[j,col] for j in range(dimension)) for col in range(len(labels))] for a in basis])
    haar_metric = overlap.T*gz.inv()*overlap
    h = mass.inv()*haar_metric
    g = mass-haar_metric
    cycle = sp.zeros(dimension)
    for col, word in enumerate(words):
        cycle[index[word[1:]+word[:1]],col] = 1
    r = mass.inv()*diag.T*cycle*diag
    return words, labels, dimension, basis, z, gz, diag, mass, overlap, h, g, cycle, r


def check(n, m, literal=True):
    words, labels, dim, basis, z, gz, diag, mass, overlap, h, g, cycle, r = objects(n,m)
    count = n**m-1
    require(g.det()!=0, 'centered Gram singular')
    require(g==g.T, 'centered Gram not symmetric')
    require(r.T*mass*r==mass, 'cycle not metric unitary')
    require(r*h==h*r, 'cycle does not commute with Haar compression')
    support = [tuple(j for j,x in enumerate(label) if x) for label in labels]
    for a in range(count):
        for b in range(count):
            if support[a] != support[b]:
                require(h[a,b]==0 and g[a,b]==0, 'support mixing')
    u = rational_unitary(n)
    require(u*u.T==sp.eye(n), 'unitary fixture invalid')
    big_u = tensor([u]*m)
    p = u.multiply_elementwise(u)
    actual_b = mass.inv()*diag.T*tensor([p]*m)*diag
    for a in range(count):
        for b in range(count):
            if support[a] != support[b]:
                require(actual_b[a,b]==0, 'actual compression mixes support')
    y = None
    if literal:
        f = sp.Matrix.hstack(*[flat(sp.diag(*diag[:,j])) for j in range(count)])
        y = f-z*gz.inv()*overlap
        require(y.T*y==g, 'literal full-End Gram mismatch')
        def apply(vector):
            x = sp.Matrix(dim,dim,list(vector))
            return flat(cycle*big_u*x*big_u.T*cycle.T)
        rc_y = sp.Matrix.hstack(*[apply(y[:,j]) for j in range(count)])
        direct = sp.trace(g.inv()*y.T*rc_y)
        # Explicit full End projector/superoperator in the smallest cases.
        if dim<=4:
            projector = y*g.inv()*y.T
            action = sp.kronecker_product(cycle*big_u,cycle*big_u)
            require(sp.trace(projector*action)==direct, 'full superoperator trace mismatch')
    else:
        # Exact physical-operator bilinear expansion; no Sym^m restriction.
        f_rc_f = diag.T*cycle*tensor([p]*m)*diag
        cz = [cycle*a*cycle.T for a in basis]
        f_rc_z = sp.Matrix([[sum(diag[j,col]*a[j,j] for j in range(dim)) for a in cz] for col in range(count)])
        z_rc_f = sp.Matrix([[sum(a[j,j]*(cycle*diag)[j,col] for j in range(dim)) for col in range(count)] for a in basis])
        z_rc_z = sp.Matrix([[sum(a.multiply_elementwise(b)) for b in cz] for a in basis])
        coeff = gz.inv()*overlap
        numerator = f_rc_f-f_rc_z*coeff-coeff.T*z_rc_f+coeff.T*z_rc_z*coeff
        direct = sp.trace(g.inv()*numerator)
    compressed = sp.trace(r*(sp.eye(count)-h).inv()*(actual_b-h))
    require(direct==compressed, 'full-End / O1 mismatch')
    full = [j for j,s in enumerate(support) if len(s)==m]
    hm = h.extract(full,full)
    bm = actual_b.extract(full,full)
    rm = r.extract(full,full)
    surviving = sp.trace(rm*(sp.eye(len(full))-hm).inv()*(bm-hm))
    require(direct==surviving, 'proper-support reduction mismatch')
    sector_trace = r*(sp.eye(count)-h).inv()*(actual_b-h)
    proper = sorted(set(support)-{tuple(range(m))})
    for s in proper:
        ids=[j for j,t in enumerate(support) if s==t]
        require(sum(sector_trace[j,j] for j in ids)==0, 'proper support contributes')
    # Exact all-support spectrum, hence conditioning in the tested range.
    eigen = h.eigenvals()
    for value in eigen:
        require(value.is_rational and 0<=value<=sp.Rational(1,n+1), 'Haar norm bound failed')
    # Invariant trace and residual dimensions using the literal permutation span.
    czvec = sp.Matrix.hstack(*[flat(cycle*a*cycle.T) for a in basis])
    invariant_trace = sp.trace(gz.inv()*z.T*czvec)
    require(invariant_trace==min(m,n), 'Haar cycle trace cutoff')
    for a in basis:
        for j,ket in enumerate(words):
            for k,bra in enumerate(words):
                if sorted(ket)!=sorted(bra):
                    require(a[j,k]==0, 'Haar vector outside balanced range')
    balanced_rank=sum(1 for a in words for b in words if sorted(a)==sorted(b))
    require(balanced_rank-len(basis)-count>=0, 'negative balanced residual dimension')
    # Exact Neumann finite sums with the algebraic tail retained.
    finite = sp.zeros(len(full))
    for k in range(4):
        finite += hm**k*(bm-hm)
        tail = hm**(k+1)*(sp.eye(len(full))-hm).inv()*(bm-hm)
        require(sp.trace(rm*(finite+tail))==surviving, 'finite Neumann/tail identity')
    if n==2:
        hu = sp.Rational(0) if m%2 else sp.Rational(1,m+1)
        t = p[0,0]-p[0,1]
        require(hm==sp.Matrix([[hu]]), 'N2 Haar moment')
        expected=t**m if m%2 else ((m+1)*t**m-1)/m
        require(surviving==expected, 'N2 exact even/odd formula')
    nonnormal=p*p.T!=p.T*p
    return {'N':n,'m':m,'literal_full_End':literal,'arithmetic':'exact rational',
            'End_dimension':dim**2,'ordered_centered_dimension':count,
            'Haar_rank':len(basis),'balanced_rank':balanced_rank,
            'remaining_balanced_rank':balanced_rank-len(basis)-count,
            'off_charge_rank':dim**2-balanced_rank,'proper_supports_checked':len(proper),
            'trace':str(direct),'H_spectrum':{str(k):v for k,v in eigen.items()},
            'full_support_H_rank':hm.rank(),'nonnormal_P':nonnormal,
            'H_B_noncommuting':hm*bm!=bm*hm,'invariant_trace':str(invariant_trace)}


def low_dimension_products():
    # General matrix-product trace identity, with deliberately noncommuting factors.
    a=sp.Matrix([[1,2],[3,5]])
    b=sp.Matrix([[2,1],[-1,3]])
    c=sp.Matrix([[0,1],[2,-1]])
    require(a*b!=b*a,'commuting fixture')
    outputs=[]
    for m in range(1,5):
        words=list(itertools.product(range(2),repeat=m)); ix={w:i for i,w in enumerate(words)}
        r=sp.zeros(2**m)
        for j,w in enumerate(words):r[ix[w[1:]+w[:1]],j]=1
        lhs=sp.trace(r*tensor([a]*m)*tensor([b]*m)*tensor([c]*m))
        rhs=sp.trace((a*b*c)**m)
        require(lhs==rhs,'matrix-product cyclic identity')
        outputs.append({'m':m,'trace':str(rhs)})
    # Exact five-node cubature for Haar T in dimension N=2, degrees 0..5.
    nodes=[-sp.Integer(1),-sp.Rational(1,2),0,sp.Rational(1,2),sp.Integer(1)]
    weights=[sp.Rational(7,90),sp.Rational(16,45),sp.Rational(2,15),sp.Rational(16,45),sp.Rational(7,90)]
    t=sp.Rational(-7,25)
    for m in range(1,6):
        h=sp.Rational(0) if m%2 else sp.Rational(1,m+1)
        require(sum(w*x**m for x,w in zip(nodes,weights))==h,'Haar cubature moment')
        for k in range(4):
            value=0
            for choices in itertools.product(range(5),repeat=k):
                product=sp.Integer(1); weight=sp.Integer(1)
                for j in choices:product*=nodes[j];weight*=weights[j]
                value+=weight*(product*t)**m
            require(value==h**k*t**m,'independent Haar product moment')
    # A constant all-even-m obstruction: for the Hadamard t=0, s=-1/m.
    for m in [2,4,6,8,10]:
        h=sp.Rational(1,m+1)
        require(-h/(1-h)==-sp.Rational(1,m),'fixed-N even tail')
    return outputs
