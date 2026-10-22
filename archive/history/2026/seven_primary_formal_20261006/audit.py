import pathlib, hashlib, json, re, itertools, random, time
import sympy as S
T=pathlib.Path('/workspace/shared/bgs_seven_primary_lean'); O=pathlib.Path(__file__).parent
src=(T/'SevenPrimary.lean').read_text(); sh=hashlib.sha256(src.encode()).hexdigest()
assert sh=='431e5d111238a962ec2bb994f21d4cb1ac17df250379651aa4e8fcd065604cb4'
q=S.Symbol('q'); P=lambda a:S.Poly.from_list(list(reversed(a or [0])),q,modulus=5)
A=lambda p:[] if p.is_zero else [int(c)%5 for c in reversed(p.all_coeffs())]
arr=lambda a:'#['+','.join(map(str,a))+']'
raw=json.loads((T/'inputs/bounded_boundary_polynomials.json').read_text())
norm=json.loads((T/'inputs/bounded_boundary_norm.json').read_text())
cert=json.loads((T/'inputs/bounded_factor_certificates_fast.json').read_text())['certificates']
expected_hashes=json.loads((T/'input_hashes.json').read_text())
for n,h in expected_hashes.items(): assert hashlib.sha256((T/'inputs'/n).read_bytes()).hexdigest()==h
review=json.loads((T/'inputs/actual_review_manifest.json').read_text())['source_bound_sha256']
for n in expected_hashes:
 if 'actual_source/'+n in review: assert expected_hashes[n]==review['actual_source/'+n]
pat=r'def entry(\d+) : Entry := ⟨#\[([^]]*)\], (\d+), #\[(.*?)\]⟩'
entries=re.findall(pat,src,re.S); assert [int(e[0]) for e in entries]==list(range(7))
parse=lambda s:list(map(int,s.split(','))) if s else []
summ=[]
for (idx,pol,unit,fs),c in zip(entries,cert):
 i=int(idx); a=parse(pol); factors=[(parse(co),int(m)) for co,m in re.findall(r'⟨#\[([^]]*)\],(\d+)⟩',fs)]
 assert a and a[-1] and all(0<=v<5 for v in a)
 expected=A(S.Poly(S.sympify(raw['y_numerators'][i+1]),q,modulus=5)) if i<6 else [v%5 for v in norm['norm_coefficients'][::-1]]
 assert a==expected and int(unit)==c['factorization_unit']%5 and int(unit) in range(1,5)
 assert len(factors)==len(c['factors'])
 prod=P([int(unit)])
 for (f,m),cf in zip(factors,c['factors']):
  assert f==[v%5 for v in cf['coefficients'][::-1]] and m==cf['multiplicity'] and m>0
  assert len(f)-1==cf['degree'] and f[-1]==1 and all(0<=v<5 for v in f)
  assert P(f).is_irreducible and (len(f)-1)%42!=0
  prod*=P(f)**m
 assert prod==P(a)
 summ.append({'entry':i,'degree':len(a)-1,'factors':len(factors),'degree_multiplicity':[(len(f)-1,m) for f,m in factors]})
 assert sum((len(f)-1)*m for f,m in factors)==len(a)-1
 print('PASS literal binding and independent GF(5) product/irreducibility',i,flush=True)
assert pow(5,42,49)==1 and all(pow(5,k,49)!=1 for k in range(1,42))
# Fresh actual-Lean tests against independently generated SymPy reference values.
lines=[src.split('def entry0')[0]]; count=0
# exhaustive monic degrees 1..4 (780 objects)
for d in range(1,5):
 for low in itertools.product(range(5),repeat=d):
  a=list(low)+[1]; b=bool(P(a).is_irreducible)
  lines.append(f'example : rabinChecks {arr(a)} = {str(b).lower()} := by native_decide'); count+=1
rng=random.Random(640231)
for t in range(220):
 a=[rng.randrange(5) for _ in range(rng.randrange(0,14))]; a=A(P(a))
 b=[rng.randrange(5) for _ in range(rng.randrange(0,9))]+[rng.randrange(1,5)]
 for name,args,expected in [('mul5',[a,b],A(P(a)*P(b))),('rem5',[a,b],A(P(a).rem(P(b)))),('gcd5',[a,b],A(S.gcd(P(a),P(b)).monic())),('frob5',[a,b],A((P(a)**5).rem(P(b)))),('subX',[a],A(P(a)-P([0,1])))]:
  lines.append(f'example : {name} '+ ' '.join(arr(z) for z in args)+f' = {arr(expected)} := by native_decide'); count+=1
for a in [[],[0],[1],[2],[1,0],[1,2],[5,1],[1,1,0],[0,0,1],[1,2,1],[4,0,1]]:
 lines.append(f'example : rabinChecks {arr(a)} = false := by native_decide'); count+=1
lines += ['example : factorCheck ⟨#[1], 1, #[⟨#[0,1],0⟩]⟩ = false := by native_decide', 'example : trim #[0,0,0] = #[] := by native_decide','example : trim #[1,0,0] = #[1] := by native_decide','example : subX #[] = #[0,4] := by native_decide','example : subX #[2] = #[2,4] := by native_decide', 'end SevenPrimary']
count+=5
(O/'IndependentControls.lean').write_text('\n'.join(lines)+'\n')
(O/'result.json').write_text(json.dumps({'source_sha256':sh,'entries':summ,'factor_occurrences':sum(z['factors'] for z in summ),'generated_lean_controls':count,'gf5_reference':'SymPy '+S.__version__,'full_recompile_performed':False},indent=2)+'\n')
print('PASS independent literal replay; generated',count,'actual-Lean controls',flush=True)
