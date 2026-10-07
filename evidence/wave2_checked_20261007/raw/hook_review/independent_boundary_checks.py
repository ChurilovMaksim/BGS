#!/usr/bin/env python3
"""Bounded review checks; no imports from the authored checker."""
from fractions import Fraction as F
from itertools import product, permutations
from collections import Counter, defaultdict
from math import factorial
from functools import reduce
import pathlib, json, hashlib

ROOT = pathlib.Path(__file__).resolve().parent
AUTHOR = pathlib.Path('/workspace/shared/bgs_wave2_hook_identity')
SNAP = pathlib.Path('/workspace/shared/bgs_checked_checkpoint_validation/source_snapshot')

def require(ok, message):
    if not ok:
        raise RuntimeError(message)

def determinant(A):
    n = len(A)
    answer = F(0)
    for p in permutations(range(n)):
        parity = sum(p[i] > p[j] for i in range(n) for j in range(i+1,n))
        answer += (-1)**parity * reduce(lambda a, i: a*A[i][p[i]], range(n), F(1))
    return answer

def compositions(total, places):
    if places == 1:
        yield (total,)
    else:
        for k in range(total+1):
            for rest in compositions(total-k, places-1):
                yield (k,) + rest

def edge_type(w, N):
    count = [0] * (N*N)
    for i in range(len(w)):
        count[w[i]*N+w[(i+1)%len(w)]] += 1
    return tuple(count)

def row(E, N):
    return tuple(sum(E[i*N:(i+1)*N]) for i in range(N))

def transpose(E, N):
    return tuple(E[j*N+i] for i in range(N) for j in range(N))

def rotations(w):
    return {w[k:]+w[:k] for k in range(len(w))}

balanced_types = 0
disconnected_zero_types = 0
ordered_pair_checks = 0
word_checks = 0
for N, max_m in [(2,6),(3,4)]:
    for m in range(1,max_m+1):
        words = list(product(range(N), repeat=m))
        types = {w:edge_type(w,N) for w in words}
        counts = Counter(types.values())
        kappa = Counter()
        alpha = Counter()
        for w in words:
            E = types[w]
            d = len(rotations(w))
            kappa[E] += d
            if w[::-1] in rotations(w):
                alpha[E] += d
        for E in compositions(m,N*N):
            n = row(E,N)
            if n != tuple(sum(E[i*N+j] for i in range(N)) for j in range(N)):
                continue
            S = [i for i in range(N) if n[i]]
            cut = S[:-1]
            tau = determinant([[n[i]*int(i==j)-E[i*N+j] for j in cut] for i in cut])
            c = F(m)*tau*reduce(lambda a,x:a*factorial(x-1), [n[i] for i in S],1)
            c /= reduce(lambda a,x:a*factorial(x),E,1)
            theta = determinant([[F(int(i==j))-F(E[i*N+j],n[i])+F(n[j],m)
                                  for j in S] for i in S])
            multinomial = F(reduce(lambda a,x:a*factorial(x),n,1),
                            reduce(lambda a,x:a*factorial(x),E,1))
            require(c==counts.get(E,0),'independent tree count')
            require(c==theta*multinomial,'independent determinant normalization')
            require(0<=theta<=len(S),'independent determinant bounds including zeros')
            balanced_types += 1
            if not c:
                require(theta==0,'disconnected determinant must vanish')
                disconnected_zero_types += 1
        actual = Counter()
        by_occupation = defaultdict(list)
        for w in words:
            by_occupation[row(types[w],N)].append(w)
        for bucket in by_occupation.values():
            for w in bucket:
                cw = rotations(w)
                rw = rotations(w[::-1])
                for v in bucket:
                    ordered_pair_checks += 1
                    if v not in cw and v not in rw:
                        actual[(types[w],types[v])] += 1
        for E in counts:
            for H in counts:
                if row(E,N)!=row(H,N):
                    continue
                formula = counts[E]*counts[H]-int(E==H)*kappa[E]
                formula -= int(H==transpose(E,N))*kappa[E]
                formula += int(E==H)*alpha[E]
                require(formula==actual[(E,H)],'independent once-counted dihedral residual')
                require(formula>=0,'independent nonnegative residual')
        word_checks += len(words)

# A separately implemented Q(i) direct-amplitude discriminator, m=4 only.
def multiply(z,w):
    return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def add(z,w):
    return (z[0]+w[0],z[1]+w[1])
def norm(z):
    return z[0]*z[0]+z[1]*z[1]
def hadamard(a):
    one, minus = (F(1),F(0)),(F(-1),F(0))
    neg_a = (-a[0],-a[1])
    return [[(z[0]/2,z[1]/2) for z in r] for r in
            [[one,one,one,one],[one,a,minus,neg_a],
             [one,minus,one,minus],[one,neg_a,minus,a]]]

discriminator = []
for a, expected in [((F(1),F(0)),F(295,64)),((F(0),F(1)),F(279,64))]:
    U = hadamard(a)
    sums = defaultdict(lambda:(F(0),F(0)))
    for w in product(range(4),repeat=4):
        z = (F(1),F(0))
        for i in range(4):
            z = multiply(z,U[w[i]][w[(i+1)%4]])
        sums[tuple(w.count(i) for i in range(4))] = add(
            sums[tuple(w.count(i) for i in range(4))],z)
    B = sum(norm(z) for z in sums.values())
    require(B==expected,'independent exact Hadamard discriminator')
    require(all(norm(z)==F(1,4) for r in U for z in r),'exact P=J4')
    require(U==[list(col) for col in zip(*U)],'symmetry gives Q=P')
    discriminator.append(str(B))

# The author's unrestricted K2 marking is not the literal j<=N expansion
# when m>N. This is a proof-boundary witness, not a failure of trace identity.
def marked_weight(lengths, N=None):
    answer = 0
    for mask in product((0,1),repeat=len(lengths)):
        degree = sum(a*b for a,b in zip(lengths,mask))
        if N is None or degree<=N:
            answer += (-1)**(sum(mask)+1)*degree
    return answer
require(marked_weight((1,1),1)==2,'N1 m2 truncated identity permutation witness')
require(marked_weight((2,),1)==0,'N1 m2 truncated transposition witness')
require(marked_weight((1,1))==0 and marked_weight((2,))==2,
        'zero-extended universal marking restores K2')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

manifest = json.loads((AUTHOR/'computation_manifest.json').read_text())
verified_outputs = {}
for item in manifest['outputs']:
    p = AUTHOR/item['path']
    require(sha(p)==item['sha256'],'declared output hash '+str(p))
    verified_outputs[item['path']] = sha(p)
verified_inputs = {}
for p,digest in manifest['input_sha256'].items():
    require(sha(SNAP/p)==digest,'declared source hash '+p)
    verified_inputs[p] = digest
require(sha(SNAP.parent/'source_manifest.json')==manifest['repository']['source_manifest_sha256'],
        'pinned source manifest')
original = json.loads((AUTHOR/'check_results.json').read_text())
replay = json.loads((ROOT/'check_results.json').read_text())
for key in ['rows','cases','cycle_marking_checks','script_sha256','source_manifest_sha256']:
    require(original[key]==replay[key],'bounded replay equality '+key)
require((ROOT/'replay_normal.log').read_bytes()==(ROOT/'replay_optimized.log').read_bytes(),
        'normal and optimized scientific replay')

result = {
    'status':'all bounded independent review checks passed',
    'arithmetic':'exact fractions.Fraction / explicit rational Gaussian pairs',
    'direct_word_ranges':{'N2':'m=1..6','N3':'m=1..4'},
    'rooted_words':word_checks,
    'balanced_integer_edge_types':balanced_types,
    'disconnected_zero_types':disconnected_zero_types,
    'ordered_equal_occupation_word_pairs':ordered_pair_checks,
    'direct_Hadamard_S4':discriminator,
    'truncation_bridge_witness':{
        'N':1,'m':2,'cycle_lengths':[ [1,1],[2] ],
        'literal_j_le_N_marked_weights':[2,0],
        'unrestricted_zero_extended_marked_weights':[0,2],
        'correction':'Append zero characters e_j(A)=0 for j>N before cycle marking'},
    'authored_checker_replay_cases':original['cases'],
    'authored_checker_replay_permutations':original['cycle_marking_checks'],
    'normal_optimized_scientific_output_equal':True,
    'verified_authored_output_hashes':verified_outputs,
    'verified_pinned_input_hashes':verified_inputs,
    'proof_sha256':sha(AUTHOR/'hook_tree_current_identity.md'),
    'manifest_sha256':sha(AUTHOR/'computation_manifest.json'),
    'independent_script_sha256':sha(pathlib.Path(__file__)),
    'nonclaims':['No finite-check extrapolation','No actual BGS operator evaluation',
                 'No asymptotic identification','No source or repository edits'],
}
(ROOT/'independent_check_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if not k.startswith('verified_')},indent=2))
