#!/usr/bin/env python3
"""Exact raw modular phases and coherent-orbit residue checks, no author imports."""
import itertools,json,time,sys,platform
from pathlib import Path
from replay import Field,need,raw_symbol,act,norm
ROOT=Path(__file__).resolve().parent

def omega(u,v):return u[0]*v[1]-u[1]*v[0]
def reduced(v,h):return (v[0]%h,v[1]%h)
def phase_rep(v,h):
 # phi_v=q^phase phi_(v mod h), q any primitive h²th root.
 r=reduced(v,h);d=((v[0]-r[0])//h,(v[1]-r[1])//h)
 return pow(2,-1,h*h)*h*omega(d,r)%(h*h)
def mphase(v,h):
 a,b=v;return phase_rep((3*a+4*b,2*a+3*b),h)
def tphase(u,v,h):return (pow(2,-1,h*h)*omega(u,v)+phase_rep((u[0]+v[0],u[1]+v[1]),h))%(h*h)

def main():
 start=time.time();F=Field([1]*6);xi=F.pow(F.g,2604);D=raw_symbol();upper=sorted(u for u in D if u[0]==1)
 modes=sorted(D);counts={'coherent_M_phase_entries':0,'coherent_T_phase_entries':0,'coherent_Gram_pairs':0,'residue_mode_packets':0,'intersection_quadratic_instances':0,'cycles':0,'eigenvector_recurrences':0,'exact_packet_terms':0};depths=[]
 for ell in [1,2,3]:
  h=5**ell;n=h*h;L=6*5**(ell-1);half=pow(2,-1,n);inv8=pow(8,-1,n)
  # All labels; exact geometric-sum kernel phase on its unique support coset.
  for a,b in itertools.product(range(h),repeat=2):
   v=(a,b);w=act(v,h);theta=mphase(v,h)
   for t in range(h):
    x=(-w[0]+h*t)%n
    raw=(-inv8*(3*x*x+2*x*a+3*a*a)-half*a*b)%n
    target=(theta+w[1]*(x+half*w[0]))%n
    need(raw==target,'actual raw cat versus coherent monomial phase');counts['coherent_M_phase_entries']+=1
   # Direct oldform-label equivalence and primitive iff unit norm.
   need((a%5==0 and b%5==0)==(norm(v,h)%5==0),'old/new classification')
  # Exact Gram supports and sums; h<=25 all pairs.
  if h<=25:
   for a,b in itertools.product(range(h),repeat=2):
    for c,d in itertools.product(range(h),repeat=2):
     same_support=(a==c);sum_nonzero=same_support and (b-d)%h==0
     need(sum_nonzero==((a,b)==(c,d)),'Gram orthogonality');counts['coherent_Gram_pairs']+=1
  # Exact T phase checks on all labels for h<=25, and representative labels for h125.
  labels=list(itertools.product(range(h),repeat=2)) if h<=25 else [(0,0),(1,0),(0,1),(1,1),(124,124),(0,124),(124,0),(24,57),(5,5)]
  for v in labels:
   for u in modes:
    a,b=u;c,d=v;w=reduced((a+c,b+d),h);theta=tphase(u,v,h)
    for t in range(h):
     x=(-w[0]+h*t)%n
     raw=(b*(x+half*a)+d*(x+a+half*c))%n
     target=(theta+w[1]*(x+half*w[0]))%n
     need(raw==target,'actual raw Weyl phase versus coherent translation');counts['coherent_T_phase_entries']+=1
  # All primitive circles, all nine upper modes, exact intersection root counts.
  small={}
  for c0 in range(1,5):
   v=min(v for v in itertools.product(range(5),repeat=2) if norm(v,5)==c0);o=[]
   for _ in range(6):o.append(v);v=act(v,5)
   small[c0]=o
  circle_counts=[]
  for c in range(1,h):
   if c%5==0:continue
   # Align orbit base with the canonical mod5 base, eliminating hidden conjugation.
   v0=next(v for v in itertools.product(range(h),repeat=2) if norm(v,h)==c and reduced(v,5)==small[c%5][0]);v=v0;orb=[];acc=[0]
   for k in range(L):
    orb.append(v);acc.append((acc[-1]+mphase(v,h))%n);v=act(v,h)
   need(v==v0 and len(set(orb))==L,'primitive orbit length');need(all(norm(v,h)==c for v in orb),'primitive circle');idx={v:k for k,v in enumerate(orb)};counts['cycles']+=1
   need(all(reduced(v,5)==small[c%5][k%6] for k,v in enumerate(orb)),'tame label indices')
   # Exact eigenvector exponents in zeta of order nL, q=zeta^L.
   # Test every eigenvector at h<=25 and six representatives at h125.
   E=acc[-1];eigen_indices=range(L) if h<=25 else range(6)
   for m in eigen_indices:
    exponent=E+n*m
    vec=[(L*acc[k]-k*exponent)%(n*L) for k in range(L)]
    for k,v in enumerate(orb):
     need((vec[k]+L*mphase(v,h)-exponent-vec[(k+1)%L])%(n*L)==0,'actual packet eigenvector recurrence');counts['eigenvector_recurrences']+=1
   for u in upper:
    a,b=u;nu=norm(u,h);rh=((1-4*c*pow(nu,-1,h))*pow(8,-1,h))%h
    solutions=[s for s in range(h) if s*s%h==rh]
    ys=[((-a*pow(2,-1,h)+2*b*s)%h,(-b*pow(2,-1,h)+a*s)%h) for s in solutions]
    intersections=[v for v in orb if reduced((v[0]+a,v[1]+b),h) in idx]
    need(set(ys)==set(intersections),'quadratic versus actual norm-circle intersections');counts['intersection_quadratic_instances']+=1
    degenerate=rh%5==0
    if degenerate:need(len(solutions)%5==0 if ell>=2 else len(solutions)==1,'degenerate count boundary')
    else:need(len(solutions) in [0,2],'generic root count')
    smallorb=small[c%5];smidx={v:k for k,v in enumerate(smallorb)}
    smallpairs=[(smidx[reduced((v[0]+a,v[1]+b),5)],ky) for ky,v in enumerate(smallorb) if reduced((v[0]+a,v[1]+b),5) in smidx]
    if ell>=2 and degenerate:smallpairs=[]
    actualpairs=[(idx[reduced((v[0]+a,v[1]+b),h)],idx[v]) for v in intersections]
    # Direct actual packet entry in a common cyclotomic root zeta of order nL.
    # Coefficients and duals are unnormalized, with the exact dual denominator L.
    big=n*L; cube_step=big//3; cube_choice=pow((cube_step%6)//2,-1,3)
    for m in (range(L) if h<=25 else range(6)):
     base=E+n*m; actual_lambda=[(base-cube_step*cube_choice*i)%big for i in range(3)]
     for kx,ky in actualpairs:
      v=orb[ky];qex=(acc[ky]-acc[kx]+tphase(u,v,h))%n
      for i,j in itertools.product(range(3),repeat=2):
       exponent=(L*qex+kx*actual_lambda[i]-ky*actual_lambda[j])%big
       tame=((base-2*i)*kx-(base-2*j)*ky)%6
       need(exponent%6==tame,'actual cyclotomic packet entry residue');counts['exact_packet_terms']+=1
    # Six tame residues, three source/target seven eigenvalue labels; multiplicities do not change weights.
    for tau in range(6):
     for zi,zj in itertools.product(range(3),repeat=2):
      gi=(tau-2*zi)%6;gj=(tau-2*zj)%6
      actual=F.sum(F.pow(xi,(gi*kx-gj*ky)%6) for kx,ky in actualpairs)
      predicted=F.sum(F.pow(xi,(gi*kx-gj*ky)%6) for kx,ky in smallpairs)
      need(actual==predicted,'actual packet residue versus 48-type dictionary');counts['residue_mode_packets']+=1
   circle_counts.append({'norm':c,'length':L,'cycle_q_exponent':acc[-1]})
  need(len(circle_counts)*L==h*h-(h//5)**2,'primitive completeness dimension')
  depths.append({'ell':ell,'h':h,'n':n,'circles':len(circle_counts),'orbit_length':L,'primitive_dimension':len(circle_counts)*L,'cycles':circle_counts,'raw_T_labels':'all' if h<=25 else labels,'eigenvalue_indices':'all' if h<=25 else list(range(6))})
  print('coherent controls ell',ell,'passed',flush=True)
 output={'status':'passed','counts':counts,'depths':depths,'arithmetic':'exact integer modular exponents and F5[w]/Phi7; all mode packet residues through h125','duration_seconds':time.time()-start,'python':sys.version,'platform':platform.platform()}
 (ROOT/'packet_results.json').write_text(json.dumps(output,indent=2)+'\n')
if __name__=='__main__':main()
