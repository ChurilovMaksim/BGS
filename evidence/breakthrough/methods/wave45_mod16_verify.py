import numpy as np

# Pell numbers P_n: P_0=0, P_1=1, P_{n+1}=6P_n-P_{n-1}
P = [0, 1]
for n in range(1, 30):
    P.append(6*P[-1] - P[-2])
print('P16', P[16], 'P17', P[17], 'P18', P[18], 'P19', P[19])
X = (P[19]-P[3]) - (P[17]-P[1])
Y = (P[18]-P[2]) - (P[16]-P[0])
print('X', X, '=', X//2**9, '*2^9 ?', X == 2**9*(X//2**9))
print('Y', Y, '=', Y//2**8, '*2^8 ?', Y == 2**8*(Y//2**8))
print('X_odd mod 4', (X//2**9) % 4, 'Y_odd mod 8', (Y//2**8) % 8)

m, p = 512, 512
Q = 8*m*m
step0 = Q//(8*p)
rng = np.random.default_rng(1)
# sample (t,u): t odd, u = 11t mod 16
t = rng.choice(np.arange(1, 4096, 2), size=2048)
U0 = rng.integers(0, 256, size=2048)
u = (11*t + 16*U0) % 4096
y_prev = (step0*t) % Q
y_curr = (step0*u) % Q
W = np.zeros((128, len(t)), dtype=np.int64)
W[0] = y_curr
for nn in range(1, p+1):
    y_next = (6*y_curr - y_prev) % Q
    y_prev, y_curr = y_curr, y_next
    if nn % 2 == 0 and nn//2 < 128:
        W[nn//2] = y_curr
# E_k = (w_{k+8} - w_k)/(Q/16) mod 16
mu = Q//16
E = ((np.roll(W, -8, axis=0) - W) % Q)//mu % 16  # roll wraps period 128; w period is 128, ok
# check arithmetic progression mod 16: E_{k+1} = 2E_k - E_{k-1}
lhs = np.roll(E, -1, axis=0)
rhs = (2*E - np.roll(E, 1, axis=0)) % 16
print('arith prog violations:', int((lhs != rhs).sum()), 'of', lhs.size)
# delta_E = E_1 - E_0 mod 16, and mod 8
dE = (E[1] - E[0]) % 16
print('delta_E mod 16 values:', sorted(set(dE.tolist())), 'mod 8:', sorted(set((dE % 8).tolist())))
# formula check: E_0 = ((P17-1)u - P16 t)/256 ; delta = (X u - Y t)/256
E0f = ((P[17]-1)*u - P[16]*t)//256
print('E0 formula violations:', int((E0f % 16 != E[0]).sum()))
dEf = (X*u - Y*t)//256
print('delta formula violations (mod 16):', int((dEf % 16 != dE).sum()))
print('delta formula values mod 8:', sorted(set((dEf % 8).tolist())))
# flip rule: t_{k+8} ^ t_k == 1 iff Q/2 <= rho_k + mu*d_k < Q
# rho_k = w_k mod (Q/2), d_k = E_k (0..15), t_k = w_k // (Q/2)
rho = W % (Q//2)
tt = W // (Q//2)
tt8 = np.roll(tt, -8, axis=0)
S = rho + mu*E
flip_pred = ((S >= Q//2) & (S < Q)).astype(np.int64)
flip_act = tt8 ^ tt
print('flip rule violations:', int((flip_pred != flip_act).sum()), 'of', flip_act.size)
# small-class check on full reps for sampled points: reps, classes, t-equality
q = 64
pj = 32
eps = ((W[q:2*q] - W[0:q]) % Q)//(Q//2)
phi = (((W[pj:2*pj] - W[0:pj]) % Q)//(Q//4)) % 4
v = W[0:q] % (Q//2)
bad_small = 0
bad_big = 0
npts = 0
for idx in range(len(t)):
    reps = [j for j in range(pj) if eps[j, idx] == 0 and phi[j, idx] == 0]
    if len(reps) != 8:
        continue
    npts += 1
    classes = {}
    for j in reps:
        classes.setdefault(int(v[j, idx]), []).append(j)
    for c, js in classes.items():
        if len(js) == 2:
            if tt[js[0], idx] != tt[js[1], idx]:
                bad_small += 1
        if len(js) == 4:
            tv = [int(tt[j, idx]) for j in js]
            if sorted(tv) != [0, 0, 1, 1]:
                bad_big += 1
print('points with 8 reps:', npts, 'small-class t-unequal:', bad_small, 'big-class non-2-2:', bad_big)
