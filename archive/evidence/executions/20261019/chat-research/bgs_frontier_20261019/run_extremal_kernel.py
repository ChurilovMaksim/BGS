import itertools
import json
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path


def main(destination):
    target=Path(destination);folder=target.parent;binary=folder/'extremal_kernel'
    build=subprocess.run(['g++','-O2','-std=c++20','-Wall','-Wextra','extremal_kernel.cpp','-o',str(binary)],capture_output=True,text=True)
    (folder/'compiler_stderr.txt').write_text(build.stderr)
    assert build.returncode==0,build.stderr
    process=subprocess.run([str(binary.resolve()),'catalogue_run/graph_catalogue.dat'],capture_output=True,text=True)
    (folder/'engine_stdout.txt').write_text(process.stdout);(folder/'engine_stderr.txt').write_text(process.stderr)
    assert process.returncode==0,process.stderr
    rows=[json.loads(line) for line in process.stdout.splitlines()]
    primes=[3,5,7,11,13,17,19,23,29,31]
    reference=json.loads(Path('dependencies/three_port_reference.json').read_text())
    summaries=[]
    for p in primes:
        by_j={};symbolic={}
        for j in (1,2,3):
            e=j+1;polys=[{} for _ in range(__import__('math').factorial(e))]
            type_at_one=[[F(0)]*7 for _ in polys]
            for row in rows:
                if row['j']!=j:continue
                data=next(a for a in row['fields'] if a['p']==p)
                for channel,count in enumerate(row['histogram']):
                    base=F(count,e*row['denominator'])
                    coefficient=base*F(data['weight24'],24)
                    if coefficient:polys[channel][row['q']]=polys[channel].get(row['q'],F(0))+coefficient
                    for t,c in enumerate(data['type_counts']):type_at_one[channel][t]+=base*c
            polys=[{q:a for q,a in pol.items() if a} for pol in polys]
            by_j[j]=polys;symbolic[j]=type_at_one
        assert by_j[1]==[{2:F(-1,4),6:F(1,4)},{}],(p,by_j[1])
        old=next(s for s in reference['summary'] if s['p']==(p if p!=31 else 13))
        oldpolys=[{int(q):F(a) for q,a in pol.items()} for pol in old['polynomials']]
        grouped=[by_j[2][0],by_j[2][3],by_j[2][4],{}]
        for channel in (1,2,5):
            for q,a in by_j[2][channel].items():grouped[3][q]=grouped[3].get(q,F(0))+a
        grouped[3]={q:a for q,a in grouped[3].items() if a}
        assert grouped==oldpolys,('three-port coefficient mismatch',p,grouped,oldpolys)
        group_types=[symbolic[2][0],symbolic[2][3],symbolic[2][4],
                     [sum(symbolic[2][c][t] for c in (1,2,5)) for t in range(7)]]
        assert [[str(x) for x in row[:4]] for row in group_types]==old['symbolic_coefficients_in_order_1_a2_a3_a2sq'],('symbolic mismatch',p,group_types)
        perms=list(itertools.permutations(range(4)))
        values=[sum(pol.values(),F(0)) for pol in by_j[3]]
        jets=[sum(F(q)*a for q,a in pol.items()) for pol in by_j[3]]
        closed={}
        allowed=[]
        for index,pi in enumerate(perms):
            product=[(pi[i]+1)%4 for i in range(4)]
            x=0;seen=set()
            while x not in seen:seen.add(x);x=product[x]
            if len(seen)==4:
                allowed.append(index)
                for q,a in by_j[3][index].items():closed[q]=closed.get(q,F(0))+a
        closed={q:a for q,a in closed.items() if a}
        summaries.append({'p':p,'permutations':[list(pi) for pi in perms],
                          'four_port_polynomials':[{str(q):str(a) for q,a in sorted(pol.items())} for pol in by_j[3]],
                          'four_port_values_at_one':[str(a) for a in values],
                          'four_port_derivatives_at_one':[str(a) for a in jets],
                          'all_open_channels_zero_at_one':all(a==0 for a in values),
                          'closed_channel_indices':allowed,
                          'P32_connected':{str(q):str(a) for q,a in sorted(closed.items())},
                          'P32_connected_value_at_one':str(sum(closed.values(),F(0))),
                          'P32_connected_quotient_jet':str(-sum(q*a for q,a in closed.items())),
                          'symbolic_four_port_values_in_order_1_a2_a3_a2sq_a4_a2a3_a2cube':[[str(a) for a in row] for row in symbolic[3]]})
    data={'status':'passed_neutral_and_full_three_port_comparison','cases':rows,'summary':summaries,
          'checks':['Exact neutral kernel','All three-port coefficients at every q','All connected symbolic cumulant totals at order two'],
          'scope':'Four-port result is a new computed candidate pending the classification proof, original-cycle prefix check and characteristic transfer.'}
    target.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'status':data['status'],'cases':len(rows),
                      'four_port_observations':[{k:s[k] for k in ['p','all_open_channels_zero_at_one','P32_connected_value_at_one','P32_connected_quotient_jet']} for s in summaries]}))


if __name__=='__main__':main(sys.argv[1])
