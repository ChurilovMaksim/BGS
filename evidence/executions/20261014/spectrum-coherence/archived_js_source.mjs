function runFlatSpectrumObstructionControls() {
  const assert=(ok,label)=>{if(!ok)throw new Error(label);};
  const eye=n=>Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>+(i===j)));
  const transpose=A=>A[0].map((_,j)=>A.map(row=>row[j]));
  const multiply=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((s,x,h)=>s+x*B[h][j],0)));
  const equal=(A,B)=>JSON.stringify(A)===JSON.stringify(B);
  const W=Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>{
    const a=(j&1)^((j>>1)&1), b=(j>>1)&1;
    return ((i&1)*a+((i>>1)&1)*b)%2===0?1:-1;
  }));
  const fourI=eye(4).map(row=>row.map(x=>4*x));
  assert(equal(multiply(W,transpose(W)),fourI),"four-dimensional unitary core");
  const R=W.map((row,i)=>row.map((x,j)=>x*W[j][i]));
  assert(equal(multiply(R,transpose(R)),fourI),"reversal Gram matrix");
  const powers=[];let Q=eye(4);
  for(let q=1;q<=6;q++){
    Q=multiply(Q,W);
    assert(Q.every(row=>row.every(Number.isSafeInteger)),"finite core arithmetic bound");
    powers.push({q,numerator:Q,denominator:2**q,trace:Q.reduce((s,row,i)=>s+row[i],0)/(2**q)});
  }
  assert(equal(powers[5].numerator,eye(4).map(row=>row.map(x=>64*x))),"sixth power");
  assert(equal(powers[1].numerator,[[4,0,0,0],[0,0,4,0],[0,0,0,4],[0,4,0,0]]),"second power");
  const primeControls=[];
  for(const p of [3,5,7,11,13,17,19,23,29,31]){
    for(let d=2;d*d<=p;d++)assert(p%d!==0,"input prime");
    const productCounts=Array(p).fill(0);
    for(let a=0;a<p;a++)for(let h=0;h<p;h++)productCounts[a*h%p]++;
    assert(productCounts[0]===2*p-1&&productCounts.slice(1).every(x=>x===p-1),"Gauss coefficient counts");
    for(let d=0;d<p;d++){
      const seen=new Set();
      for(let b=0;b<p;b++)for(let c=0;c<p;c++)seen.add(((b-c+p)%p)*p+(b+c+d)%p);
      assert(seen.size===p*p,"odd-prime pair substitution");
    }
    const squaredResidues=Array(p).fill(0);
    for(let b=0;b<p;b++)squaredResidues[b*b%p]++;
    assert(squaredResidues[0]===1&&squaredResidues.slice(1).every(x=>x===0||x===2),"quadratic residue multiplicities");
    primeControls.push({p,substitutions_checked:p,pair_count_per_substitution:p*p,productCounts,squaredResidues});
  }
  const tensorControls=[];
  const c1=[2n,1n,-1n,-2n,-1n,1n],c2=[2n,-1n,-1n,2n,-1n,-1n];
  for(let k=1;k<=16;k++){
    const N=4n**BigInt(k),sqrtN=2n**BigInt(k),sign=k%2===0?1n:-1n;
    const numerators=c1.map((x,r)=>N+sign*x+c2[r]+sqrtN*(r%2===0?1n:-1n));
    assert(numerators.every(x=>x%6n===0n),"tensor multiplicity divisibility");
    const multiplicities=numerators.map(x=>x/6n);
    assert(multiplicities.every(x=>x>=0n),"tensor multiplicity positivity");
    assert(multiplicities.reduce((s,x)=>s+x,0n)===N,"tensor dimension");
    if(k>=2)assert(multiplicities.every(x=>x>0n),"all six roots present");
    assert(N%6n===4n,"Heisenberg resonance remainder");
    tensorControls.push({k,N:String(N),multiplicities:multiplicities.map(String),nearest_periodic_time:String(N-4n)});
  }
  return {status:"pass",arithmetic:"bounded safe integers for core/prime controls; BigInt for tensor multiplicities",execution:"functions JavaScript V8; Node stdout wrapper not executed",
    scope:"Finite arithmetic controls only; no generic discriminant or asymptotic proof, Python, C++ or Lean certification",core:{W,R,powers},
    primeControls,tensorControls};
}

console.log(JSON.stringify(runFlatSpectrumObstructionControls(), null, 2));
