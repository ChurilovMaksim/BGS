"""Referee: check Prop I2' per member at m=9 (k1 kick |n|<=2, brute force): Z(nu0+2hj/7) = omega_t Z0/7 + Delta_t, t=j y' mod 7."""
import numpy as np, json, math
J=json.load(open('out/brute_m9_L2_nu1045.json')); Zh=np.load('out/brute_m9_L2_nu1045.npy'); d=7; h=J['h']; yp=J['yp']; nu0=J['nu']
gx,gy=np.meshgrid(range(d),range(d),indexing='ij'); Nm=(gx*gx-2*gy*gy)%d
G=lambda t,bx,by: np.exp(-2j*np.pi*((t*Nm+2*(bx*gx+2*by*gy))%d)/d).sum()
S=sum(abs(Zh[b]) for b in np.ndindex(7,7) if b!=(0,0)); worst=0; bnd=0
for j in range(1,d):
    nu=(nu0+(2*h//d)*j)%(2*h); t=(j*yp)%d; Zd=complex(*J['members'][str(nu)])
    om=G(t,0,0)/d; Dl=sum(Zh[b]*G(t,*b) for b in np.ndindex(7,7) if b!=(0,0))/d**2
    gabs=[abs(G(t,*b)) for b in np.ndindex(7,7)]
    worst=max(worst,abs(Zd-(om*Zh[0,0]/d+Dl))/abs(Zd)); unit=math.gcd(nu,2*h)==1
    print(f'j={j} t={t} unit={unit} |omega|={abs(om):.15f} min/max|G_t|={min(gabs):.12f}/{max(gabs):.12f} |Delta|={abs(Dl):.4f} <= S/d={S/d:.4f}: {abs(Dl)<=S/d}')
print('max rel err of member formula: %.2e'%worst)
