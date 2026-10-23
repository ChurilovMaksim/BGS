"""Catalogue sparse balanced bipartite matrices of extremal ranks 1,2,3.

Completeness is an obligation of extremal_graphs_ru.md, not an inference from
successful execution. Matrices are quotiented by row/column permutations;
the bipartition orientation is retained, with a factor two when t=s.
"""
import itertools as it
import json
import math
import sys
from collections import Counter
from pathlib import Path


def rank_mod(A,p):
    a=[[x%p for x in row] for row in A]
    r=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][j]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][j],-1,p)
        a[r]=[(v*inv)%p for v in a[r]]
        for i in range(r+1,len(a)):
            if a[i][j]:
                v=a[i][j]
                a[i]=[(x-v*y)%p for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r


def root_groups(B):
    c=len(B[0]);parent=list(range(c));used=set()
    def find(x):
        while parent[x]!=x:x=parent[x]
        return x
    for row in B:
        support=[i for i,v in enumerate(row) if v]
        if len(support)==2:
            a,b=support;assert row[a]+row[b]==0
            parent[find(a)]=find(b);used.update(support)
    groups={}
    for i in sorted(used):groups.setdefault(find(i),[]).append(i)
    return sorted((tuple(v) for v in groups.values()),key=lambda v:(len(v),v)),tuple(i for i in range(c) if i not in used)


def canonical(B):
    B=tuple(sorted(tuple(row) for row in B));r=len(B);c=len(B[0])
    groups,outside=root_groups(B)
    # The degree-two rows recover these column components intrinsically.
    buckets={}
    for group in groups:buckets.setdefault(len(group),[]).append(group)
    block_orders=[list(it.permutations(buckets[size])) for size in sorted(buckets)]
    best=None;ties=0
    for choice in it.product(*block_orders):
        blocks=[g for bucket in choice for g in bucket]
        if outside:blocks.append(outside)
        for within in it.product(*(it.permutations(g) for g in blocks)):
            order=tuple(i for group in within for i in group)
            value=tuple(sorted(tuple(row[j] for j in order) for row in B))
            if best is None or value<best:best=value;ties=1
            elif value==best:ties+=1
    assert best is not None
    multiplicity=math.prod(math.factorial(v) for v in Counter(B).values())
    return (r,c,best),ties*multiplicity


def connected(B):
    r=len(B);c=len(B[0]);seen={0};queue=[0]
    for v in queue:
        neighbours=[r+j for j in range(c) if B[v][j]] if v<r else [i for i in range(r) if B[i][v-r]]
        for w in neighbours:
            if w not in seen:seen.add(w);queue.append(w)
    return len(seen)==r+c


def root_rows(groups,c):
    out=[]
    for group in groups:
        for a,b in it.permutations(group,2):
            row=[0]*c;row[a]=1;row[b]=-1;out.append(tuple(row))
    return sorted(out)


def four_rows(groups,c):
    out=[]
    for support in it.combinations(range(c),4):
        for positive in it.combinations(support,2):
            row=tuple(1 if i in positive else -1 if i in support else 0 for i in range(c))
            if all(sum(row[i] for i in group)==0 for group in groups):out.append(row)
    return sorted(out)


def extra_rows(inside,outside,c):
    out=[];size=4-len(outside)
    for support in it.combinations(inside,size):
        for signs in it.product((-1,1),repeat=4):
            row=[0]*c
            for i,v in zip(tuple(support)+tuple(outside),signs):row[i]=v
            if sum(row)==0:out.append(tuple(row))
    return sorted(out)


def main(output_dir):
    output=Path(output_dir);catalogue={};raw=Counter();accepted=Counter()
    def add(B,g,family):
        raw[family]+=1
        if not B:return
        r=len(B);c=len(B[0])
        row_degrees=[sum(v!=0 for v in row) for row in B]
        col_degrees=[sum(row[j]!=0 for row in B) for j in range(c)]
        if any(d not in (2,4) for d in col_degrees):return
        if any(sum(row[j] for row in B) for j in range(c)):return
        t=row_degrees.count(2);s=col_degrees.count(2)
        if t<s or t+s!=2*g+2:return
        if not connected(B):return
        groups,outside=root_groups(B)
        root_rank=sum(len(group)-1 for group in groups)
        if root_rank not in (g,g-1):return
        key,aut=canonical(B)
        if key in catalogue:
            assert catalogue[key]['automorphisms_preserving_bipartition']==aut
            catalogue[key]['generating_families'].add(family)
            return
        assert rank_mod(B,3)==g and rank_mod(B,31)==g,(g,B)
        den=aut*(2 if t==s else 1)
        value={'g':g,'nrows':r,'ncols':c,'q_active':r+c,'degree_two_rows':t,'degree_two_cols':s,
               'root_rank':root_rank,'automorphisms_preserving_bipartition':aut,
               'groupoid_denominator':den,'matrix':[list(row) for row in key[2]],
               'generating_families':{family}}
        catalogue[key]=value;accepted[family]+=1

    # Full span of the degree-two rows: all column root components are nontrivial.
    full=[(1,[2]),(2,[3]),(2,[2,2]),(3,[4]),(3,[3,2]),(3,[2,2,2])]
    for g,sizes in full:
        c=sum(sizes);groups=[];i=0
        for size in sizes:groups.append(tuple(range(i,i+size)));i+=size
        two=root_rows(groups,c);four=four_rows(groups,c);number_four=c-g-1
        family='full_g'+str(g)+'_'+'.'.join(map(str,sizes))
        for special in it.combinations_with_replacement(four,number_four):
            for t in range(g+1,2*g+3):
                for roots in it.combinations_with_replacement(two,t):
                    B=roots+special
                    actual_groups,outside=root_groups(B)
                    if outside or sum(len(group)-1 for group in actual_groups)!=g:continue
                    add(B,g,family)
        print(json.dumps({'family_done':family,'catalogue_so_far':len(catalogue)}),flush=True)

    # A one-dimensional quotient of the degree-two root span; precisely two
    # degree-four rows meet the outside columns. Those outside columns have
    # opposite nonzero entries in these two rows.
    mixed=[(2,[2],3,0),(3,[3],3,0),(3,[2,2],2,0),(3,[2,2],3,1)]
    for g,sizes,L,pure_four in mixed:
        a=sum(sizes);c=a+L;groups=[];i=0
        for size in sizes:groups.append(tuple(range(i,i+size)));i+=size
        outside=tuple(range(a,c));two=root_rows(groups,c);four=four_rows(groups,c)
        extra=extra_rows(tuple(range(a)),outside,c)
        family='mixed_g'+str(g)+'_'+'.'.join(map(str,sizes))+'_L'+str(L)
        for index,v in enumerate(extra):
            for w in extra[index:]:
                if any(v[i]+w[i] for i in outside):continue
                if any(sum(v[i]+w[i] for i in group) for group in groups):continue
                for special in it.combinations_with_replacement(four,pure_four):
                    for t in range(g+1,2*g+3-L):
                        for roots in it.combinations_with_replacement(two,t):
                            B=roots+special+(v,w)
                            actual_groups,actual_outside=root_groups(B)
                            if sum(len(group)-1 for group in actual_groups)!=g-1:continue
                            if tuple(actual_outside)!=outside:continue
                            add(B,g,family)
        print(json.dumps({'family_done':family,'catalogue_so_far':len(catalogue)}),flush=True)

    ordered=sorted(catalogue.values(),key=lambda x:(x['g'],x['q_active'],x['nrows'],x['ncols'],x['matrix']))
    keys=set(catalogue)
    transpose_checks=0
    for item in ordered:
        B=item['matrix']
        if item['degree_two_rows']==item['degree_two_cols']:
            negative_transpose=[[-B[i][j] for i in range(len(B))] for j in range(len(B[0]))]
            key,aut=canonical(negative_transpose)
            assert key in keys,('missing transposed orientation',item)
            transpose_checks+=1
        # Deterministic relabeling check independent of the generation order.
        permuted=[list(reversed(row)) for row in reversed(B)]
        assert canonical(permuted)[0]==canonical(B)[0]
    assert sum(x['g']==1 for x in ordered)==2
    assert max(x['q_active'] for x in ordered if x['g']==2)<=11
    assert max(x['q_active'] for x in ordered if x['g']==3)<=16
    for index,item in enumerate(ordered):
        item['id']=index
        item['generating_families']=sorted(item['generating_families'])
    data={'status':'passed_catalogue_internal_checks','matrices':ordered,
          'matrix_count':len(ordered),'by_g':{str(g):sum(x['g']==g for x in ordered) for g in (1,2,3)},
          'by_g_and_q':{str(g):dict(sorted(Counter(x['q_active'] for x in ordered if x['g']==g).items())) for g in (1,2,3)},
          'raw_family_candidates':dict(raw),'new_classes_by_family':dict(accepted),
          'transpose_orientation_checks':transpose_checks,
          'scope':'Finite enumeration of the stated matrix families; their mathematical completeness is a separate proof obligation.'}
    (output/'graph_catalogue.json').write_text(json.dumps(data,indent=2)+'\n')
    lines=[str(len(ordered))]
    for x in ordered:
        fields=[x['id'],x['g'],x['nrows'],x['ncols'],x['groupoid_denominator']]
        fields.extend(v for row in x['matrix'] for v in row)
        lines.append(' '.join(map(str,fields)))
    (output/'graph_catalogue.dat').write_text('\n'.join(lines)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k!='matrices'}))


if __name__=='__main__':main(sys.argv[1])
