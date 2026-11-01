import json,collections
def chi(d): 
    if d%2==0: return 0
    return 1 if d%8 in (1,7) else -1
M=2**16; cnt=[0]*M
for d in range(1,M):
    c=chi(d)
    if c:
        for m in range(d,M,d): cnt[m]+=c
for j in range(2,15):
    print(j, sum(cnt[2**j:2**(j+1)]))
