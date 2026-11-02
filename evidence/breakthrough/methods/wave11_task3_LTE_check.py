def v2(n):
    c=0
    while n%2==0: n//=2; c+=1
    return c
s=[2,6]
for n in range(2,31):
    s.append(6*s[-1]-s[-2])
ok=True
for m in range(1,31):
    D=s[m]-2
    k=v2(m)
    pred=2 if k==0 else 2*k+3
    got=v2(D)
    print(f"m={m} D={D} v2={got} pred={pred} {'OK' if got==pred else 'FAIL'}")
    ok &= (got==pred)
print("ALL OK" if ok else "MISMATCH")
