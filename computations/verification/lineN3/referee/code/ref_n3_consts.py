import math
lam=3+2*math.sqrt(2); T=1.28359
print("Lemma I V: O1->F theta=(0.5+1.2/lam)/0.75 = %.4f ; weight slope 0.25/lam=%.4f"%((0.5+1.2/lam)/0.75,0.25/lam))
print("Lemma I V: F->O1 2 steps theta=(0.5+1/(2lam)+0.75/lam^2)/1.2 = %.4f ; |c| exponent -0.25+2.5/lam^2 = %.4f ; 1 step would be %.4f"%((0.5+0.5/lam+0.75/lam**2)/1.2,-0.25+2.5/lam**2,-0.25+2.5/lam))
dE=1/(2*(lam-1))
print("Lemma I E: dev=%.4f ; O1->F 2 steps theta=(dev+0.8/lam^2)/0.2=%.4f (1 step %.4f) ; F->O1 exponent -0.3+2.5/lam^2=%.4f (1 step %.4f); F->O1 2-step theta=(dev+0.2/lam^2)/0.8=%.4f"%(dE,(dE+0.8/lam**2)/0.2,(1/(2*lam)+0.8/lam)/0.2,-0.3+2.5/lam**2,-0.3+2.5/lam,(dE+0.2/lam**2)/0.8))
for f,L,r in [('8V',1.965736,1.052901),('8E',1.660338,1.051923)]:
    print("%s rate (L r2)^(1/3)=%.5f  Lambda margin T^3/r2/L=%.4f  kappa=T^3/(L r2)=%.5f  sqrt=%.5f  log_lam=%.5f  delta=%.5f"%(f,(L*r)**(1/3),T**3/r/L,T**3/(L*r),math.sqrt(T**3/(L*r)),math.log(math.sqrt(T**3/(L*r)))/math.log(lam),1-(L*r)**(1/3)/T))
print("Lemma E: log_lam(264/256)+1=%.4f ; eps giving +0.76: %.4f"%(math.log(264/256)/math.log(lam)+1, math.sqrt(lam**(-0.24)/264)))
print("7 h_p ~ lam^(m/6) vs L_m=lam^(0.2271 m): 1/6=%.4f < 0.2271"%(1/6))
