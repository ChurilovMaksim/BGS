"""Six finite shifted N49 bases for a proposed q-Lucas lift; not a lift proof."""
if not __debug__:raise RuntimeError('Checks required')
from pathlib import Path
ns={};exec(Path('/workspace/shared/bgs_seven_adic_resume/actual_residue_base49.py').read_text().split('# Original position order.')[0],ns)
np=ns['np'];sp=ns['sp'];mul=ns['mul'];inv=ns['inv'];rank=ns['rank'];Z=ns['Z'];O=ns['O'];powers=ns['powers']
import json,time
n=49;m=7;a=25;order=[(a+t+7*j)%49 for t in range(7)for j in range(7)]
def bond(u,j):
 z=(u+7*j)%49;c7=3*(powers[(7*z)%49]+powers[(-7*z)%49])%5;c1=3*(powers[z]+powers[-z%49])%5
 return 4*mul((O-c7)%5,(O+c1)%5)%5
D=np.zeros((7,7,42),dtype=np.int64);D[0,:]=O
for t in range(1,7):
 for j in range(7):D[t,j]=mul(D[t-1,j],inv(bond(t,j)))
d=D.reshape(49,42);di=np.array([inv(x)for x in d]);G=np.zeros((49,49,42),dtype=np.int64)
for i,x in enumerate(order):
 for j,y in enumerate(order):G[i,j]=mul(di[i],mul(powers[(-pow(8,-1,49)*(3*x*x-2*x*y+3*y*y))%49],d[j]))
def J(v):
 out=np.zeros_like(v);out[:42]=v[7:];return out
def mv(A,v):
 out=np.zeros((49,42),dtype=np.int64)
 for i in range(49):
  for j in range(49):out[i]=(out[i]+mul(A[i,j],v[j]))%5
 return out
out=[];st=time.time()
for shift in range(6):
 h=[]
 for j in range(7):
  v=O.copy()
  for u in range(1,7*shift+1):v=mul(v,mul((O+powers[(u+7*j)%49])%5,(O+powers[(u+7*j)%49])%5))
  h.append(v)
 E=np.zeros_like(G)
 for t in range(7):
  for j in range(7):
   for k in range(49):E[7*t+j,k]=mul(h[j],G[7*t+(j+shift)%7,k])
 attempts=[];success=False
 for c in (1,2,3):
  v=np.zeros((49,42),dtype=np.int64);v[24]=O;w=J(v);K=[];C=[]
  for k in range(49):
   K.append(v.copy());C.append((w-J(v))%5);v=(J(v)+c*mv(E,v))%5;w=(J(w)+c*mv(E,w))%5
  rk=rank(np.array(K).transpose(1,0,2));rd=rank(np.array(C).transpose(1,0,2));attempts.append({'c':c,'cyclic_rank':rk,'commutator_rank':rd})
  print('shift',shift,'c',c,'ranks',rk,rd,flush=True)
  if rk==49 and rd==48:success=True;break
 out.append({'shift':shift,'attempts':attempts,'certified_scalar':success});assert success
record={'field':'F5[q]/Phi49(q)','scope':'Six shifted low-block auxiliary bases only; q-Lucas lift not certified here.','variants':out,'seconds':time.time()-st}
Path('/workspace/shared/bgs_seven_adic_resume/ramified_higher_base_variants.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
