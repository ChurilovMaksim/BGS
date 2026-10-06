import pathlib,json
if not __debug__:raise RuntimeError("Assertions must be enabled")
R=pathlib.Path('/workspace/shared/bgs_seven_adic_resume');D=pathlib.Path(__file__).parent
cs=json.loads((R/'single_seven_gcd_certificates.json').read_text())['classes']
with (D/'independent_inputs.txt').open('w') as f:
 def line(*a): print(*a,file=f)
 def arr(a):line(len(a),*a)
 line(6)
 for l,c in enumerate(cs,1):
  p=json.loads((R/f'single_seven_minors_l{l}.json').read_text());a=json.loads((R/f'single_seven_gcd_analysis_l{l}.json').read_text())
  assert p['field_modulus']==[1,0,1,3,1,0,1] and p['field_generator']==9 and p['w_code']==1208
  assert p['l_mod7']==c['l_mod7']==l
  assert all(pc[-1] for pc in p['minor_coefficients'])
  line(l,len(p['nodes']));arr(p['nodes'])
  for r,v,pc in zip(p['row_sets'],p['values'],p['minor_coefficients']):arr(r);arr(v);arr(pc)
  arr(p['gcd_coefficients'])
  for b in c['minor_gcd_bezout']:arr(b)
  for q in c['minor_gcd_quotients']:arr(q)
  line(len(c['excluded_linear_factors']))
  for x in c['excluded_linear_factors']:line(x['root_code'],x['multiplicity'])
  arr(a['remaining_coefficients']);line(len(c['remaining_components']))
  for x in c['remaining_components']:
   line(x['field_degree_bound']);arr(x['component_coefficients']);arr(x['odd_power_remainder'])
   for b in x['odd_gcd_bezout']:arr(b)
print('Serialized six classes without importing candidate code')
