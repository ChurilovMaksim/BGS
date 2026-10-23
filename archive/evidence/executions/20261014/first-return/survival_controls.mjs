function runFirstReturnControls(){
 const start=Date.now(), n=4, p=3, N=n*p;
 const z=()=>[0n,0n], add=(x,y)=>[x[0]+y[0],x[1]+y[1]];
 const mul=(x,y)=>[x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1]];
 const cj=x=>[x[0]-x[1],-x[1]], sc=(a,x)=>[a*x[0],a*x[1]];
 const eq=(x,y)=>x[0]===y[0]&&x[1]===y[1];
 const zero=x=>x[0]===0n&&x[1]===0n;
 const mat=()=>Array.from({length:N},()=>Array.from({length:N},z));
 const prod=(a,b)=>{let c=mat();for(let i=0;i<N;i++)for(let l=0;l<N;l++)if(!zero(a[i][l]))for(let j=0;j<N;j++)if(!zero(b[l][j]))c[i][j]=add(c[i][j],mul(a[i][l],b[l][j]));return c;};
 const W=[[1,1,1,1],[1,-1,-1,1],[1,1,-1,-1],[1,-1,1,-1]];
 const K=[[1,0,0,0],[0,0,1,0],[0,0,0,1],[0,1,0,0]];
 const A=mat();
 for(let i=0;i<N;i++)for(let j=0;j<N;j++){
  const g=(i%p===j%p)?[1n,2n]:[1n,-1n];
  A[i][j]=sc(BigInt(W[Math.floor(i/p)][Math.floor(j/p)]),g);
 }
 const Ast=A[0].map((_,i)=>A.map(row=>cj(row[i])));
 const gram=prod(A,Ast);
 for(let i=0;i<N;i++)for(let j=0;j<N;j++)if(!eq(gram[i][j],[i===j?36n:0n,0n]))throw Error("Unitarity failure");
 let checked=0;
 for(let col=0;col<N;col++){
  let X=mat();X[col][col]=[1n,0n];let denominator=1n;
  for(let t=1;t<=12;t++){
   X=prod(prod(A,X),Ast);denominator*=36n;
   for(let i=0;i<N;i++){
    const a=Math.floor(i/p),b=i%p,c=Math.floor(col/p),d=col%p;
    let numerator=0;
    if(t===1)numerator=1;
    if(t===2)numerator=4*K[a][c]-1;
    if(t===p)numerator=3*Number(b===d)-1;
    if(t===2*p)numerator=(4*Number(a===c)-1)*(3*Number(b===d)-1);
    const expected=[BigInt(numerator)*(denominator/12n),0n];
    if(!eq(X[i][i],expected))throw Error(`First return mismatch col=${col} row=${i} t=${t}`);
    checked++;
    X[i][i]=z();
   }
   if(t===6) for(let i=0;i<N;i++)for(let j=0;j<N;j++)if(!zero(X[i][j]))throw Error('Nonzero survival at time6');
  }
 }
 return {status:"passed",arithmetic:"BigInt Z[omega], omega^2+omega+1=0; exact common denominators 36^t",dimension:N,core_tensor_k:1,prime:p,unitarity_entries:N*N,first_return_entries:checked,all_diagonal_source_columns:N,times_checked:[1,12],nonzero_amplitude_times:[1,2,3,6],largest_pulse_subspace_dimension:(n-1)*(p-1),survival_zero_entries:1728,scope:"Finite k=1,p=3 full projected superoperator replay and all-source survival zero at time6; does not prove asymptotics, min-max, phase-genericity or BGS; functions V8 function execution, no Node wrapper execution",elapsed_ms:Date.now()-start};
}

if (typeof console !== 'undefined') console.log(JSON.stringify(runFirstReturnControls(), null, 2));
