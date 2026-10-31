from math import log,sqrt
mu=1.9154712
x,y=1,1;H={1:1}
for m in range(2,200):
    x,y=x+2*y,x+y
    if m%2:H[m]=x
for m in range(3,200,2):
    if 2*m*log(mu)-log(4) >= log(4*m*H[m]):
        print("(+-2,8): all d<=sqrt(h) included for odd m >=",m,"(using |Z|>=mu^m/2, monotone after)");break
# (+-2,16) float rate 1.615 (Line G [N]); coefficient unknown -> report base only
print("(+-2,16) base comparison 1.615^2 vs sqrt(lambda):",1.615**2,(3+2*sqrt(2))**0.5)
