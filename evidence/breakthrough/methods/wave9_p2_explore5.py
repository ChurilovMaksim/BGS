# c_i, e_i sequences: c0=1,c1=3 ; e0=0,e1=1 ; both satisfy x_{n+1}=6x_n-x_{n-1}
def seqs(N):
    c=[1,3]; e=[0,1]
    for _ in range(N):
        c.append(6*c[-1]-c[-2]); e.append(6*e[-1]-e[-2])
    return c,e
c,e=seqs(20)
for mod in [4,8,16,32]:
    print(f"mod {mod}: c={[x%mod for x in c[:16]]}")
    print(f"mod {mod}: e={[x%mod for x in e[:16]]}")
# v_i = v0*c_i + d*e_i where d=v1-3v0
# Check class sums C_r, E_r for m=8,12,16: sum over k of c_{r+4k}, e_{r+4k}
for m in [8,12,16,20]:
    print(f"m={m}")
    for r in range(4):
        C=sum(c[r+4*k] for k in range(m//4)); E=sum(e[r+4*k] for k in range(m//4))
        print(f"  r={r} C_r={C} E_r={E}  C mod 512={C%512} E mod 512={E%512}")
