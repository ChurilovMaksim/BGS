import struct, sys
M=60
DIH=[]
for k in range(60):
    DIH.append(tuple((i+k)%60 for i in range(60)))
    DIH.append(tuple(((-i+k)%60)%60 for i in range(60)))
DIH=sorted(set(DIH))
assert len(DIH)==120
SIGMA=[(11*i+9)%60 for i in range(60)]
def mul(a,b,q): return ((a[0]*b[0]+2*a[1]*b[1])%q,(a[0]*b[1]+a[1]*b[0])%q)
def seq(A,q):
    out=[]; cur=A
    for i in range(60):
        out.append((2*cur[0])%q); cur=mul(cur,(3,2),q)
    return tuple(out)
def load_shifts(fn):
    out=set()
    with open(fn,'rb') as f:
        data=f.read()
    for off in range(0,len(data),240):
        out.add(struct.unpack_from('<60i',data,off))
    return out
SH={81:load_shifts('wave32_shift81.bin'),625:load_shifts('wave32_shift625.bin')}
PE={128:None,81:9,625:25,49:7,121:11,361:19,841:29,923521:961,1681:41,3481:59,72361:269,361201:601,5202961:2281}
def genuine(A,q):
    if q==128: return A[0]%16==0 and A[1]%8==0 and A[0]<128 and A[1]<128
    pe=PE[q]; return A[0]%pe==0 and A[1]%pe==0 and A[0]<q and A[1]<q
COMBO={
 128:'cccccccccccccccc:cccccccccccccc',
 81:'2424242424242424:24242424242424',
 625:'ffffffffffffffff:ffffffffffffff',
 49:'1041041041041042:4104104104104',
 361:'ffffffffffffffff:ffffffffffffff',
 841:'1800018000180002:40001800018000',
 923521:'ffffffffffffffff:ffffffffffffff',
 1681:'1806018060180602:40601806018060',
 3481:'ffffffffffffffff:ffffffffffffff',
 72361:'ffffffffffffffff:ffffffffffffff',
 361201:'ffffffffffffffff:ffffffffffffff',
 5202961:'ffffffffffffffff:ffffffffffffff',
}
def parsemask(s):
    lo,hi=s.split(':'); return (int(lo,16),int(hi,16))
def maskstr(m):
    return '%x:%x'%m
pairs={}
for q,mask in COMBO.items():
    with open(f'wave32_COH_m60_sigma_examples_q{q}.txt') as f:
        for line in f:
            parts=line.split()
            if parts[0]==mask:
                pairs[q]=(tuple(map(int,parts[1:3])),tuple(map(int,parts[3:5]))); break
        else:
            print(f'NO example for q={q} mask={mask}'); sys.exit(1)
# 121: any mask (intersection already empty without it); take first line
with open('wave32_COH_m60_sigma_examples_q121.txt') as f:
    parts=f.readline().split()
    pairs[121]=(tuple(map(int,parts[1:3])),tuple(map(int,parts[3:5])))
    print('121 uses mask',parts[0])
inter=(0xFFFFFFFFFFFFFFFF,0x00FFFFFFFFFFFFFF)
ok=True
for q,(A,Ap) in sorted(pairs.items()):
    assert genuine(A,q), (q,'A not genuine',A)
    assert genuine(Ap,q), (q,'Ap not genuine',Ap)
    S=seq(A,q); Sp=seq(Ap,q)
    for i in range(60):
        assert Sp[i]==S[SIGMA[i]], (q,'sigma mismatch',i)
    # recompute mask
    lo=hi=0
    for ti,tau in enumerate(DIH):
        if q in (81,625):
            diff=tuple((Sp[i]-S[tau[i]])%q for i in range(60))
            good = diff in SH[q]
        else:
            good = all(Sp[i]==S[tau[i]] for i in range(60))
        if good:
            if ti<64: lo|=(1<<ti)
            else: hi|=(1<<(ti-64))
    got=(lo,hi)
    if q in COMBO:
        want=parsemask(COMBO[q])
        print(f'q={q} recomputed mask matches claimed: {got==want}')
        if got!=want: ok=False
    else:
        print(f'q=121 recomputed mask: {maskstr(got)}')
    inter=(inter[0]&lo, inter[1]&hi)
print('intersection:',maskstr(inter),'EMPTY' if inter==(0,0) else 'NONEMPTY')
# direct tau check over the constructed pair
passing=[]
for ti,tau in enumerate(DIH):
    good=True
    for q,(A,Ap) in sorted(pairs.items()):
        S=seq(A,q); Sp=seq(Ap,q)
        if q in (81,625):
            diff=tuple((Sp[i]-S[tau[i]])%q for i in range(60))
            if diff not in SH[q]: good=False; break
        else:
            if not all(Sp[i]==S[tau[i]] for i in range(60)): good=False; break
    if good: passing.append(ti)
print('tau passing direct check:',passing)
print('VERDICT:', 'COH COUNTEREXAMPLE CONFIRMED' if (ok and inter==(0,0) and not passing) else 'NOT CONFIRMED')
print('pair (per component A -> Ap):')
for q,(A,Ap) in sorted(pairs.items()):
    print(f'  q={q}: {A} -> {Ap}')
