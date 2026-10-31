"""N10b [N]: which constant twists are 'slow' for the full TW trace Z (all sectors)? |Z(tau_i == t)| for t in {0,1/4,1/2,3/4}, m=39,90."""
import sys, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
for m in (39,90):
    h,nu=nu_rho(m,1); tw=TW(m,nu,L=8,K=16)
    Z=Zbatch(tw,[[t]*m for t in (0,.25,.5,.75,.125)])
    print(m,'S=',tw.S,[('%.3g'%abs(z)) for z in Z],'rates',[('%.4f'%(abs(z)**(1/m))) for z in Z])
