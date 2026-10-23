function runIndependentFirstReturnControls(){
  const start=Date.now();
  const W=[[1,1,1,1],[1,-1,-1,1],[1,1,-1,-1],[1,-1,1,-1]].map(r=>r.map(BigInt));
  const zeros=n=>Array.from({length:n},()=>Array(n).fill(0n));
  const eye=n=>Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>i===j?1n:0n));
  const mul=(a,b)=>{
    const n=a.length,c=zeros(n);
    for(let i=0;i<n;i++)for(let h=0;h<n;h++)if(a[i][h]!==0n)
      for(let j=0;j<n;j++)if(b[h][j]!==0n)c[i][j]+=a[i][h]*b[h][j];
    return c;
  };
  const tr=a=>a.reduce((s,r,i)=>s+r[i],0n);
  const trans=a=>a.map((_,i)=>a.map(r=>r[i]));
  const kron=(a,b)=>Array.from({length:a.length*b.length},(_,i)=>
    Array.from({length:a.length*b.length},(_,j)=>a[Math.floor(i/b.length)][Math.floor(j/b.length)]*b[i%b.length][j%b.length]));
  const nonzero=a=>a.some(row=>row.some(x=>x!==0n));
  const pow=(a,j)=>{let o=eye(a.length);for(let h=0;h<j;h++)o=mul(o,a);return o;};
  const eqmat=(a,b)=>a.length===b.length&&a.every((r,i)=>r.every((x,j)=>x===b[i][j]));
  const assert=(b,msg)=>{if(!b)throw Error(msg);};
  const K=mul(W,W).map(row=>row.map(x=>{assert(x%4n===0n,"core square");return x/4n;}));
  assert(eqmat(pow(K,3),eye(4)),"K cubed");
  const prime=p=>{for(let q=2;q*q<=p;q++)if(p%q===0)return false;return p>1;};
  const cases=[];
  let entryCount=0;
  for(const [k,p,maxT] of [[1,5,32],[1,7,44],[2,3,20]]){
    assert(prime(p)&&p%2===1,"prime domain");
    const n=4**k,N=n*p,BN=BigInt(N),Bp=BigInt(p);
    let B=eye(1),S=eye(1);
    for(let h=0;h<k;h++){B=kron(B,W);S=kron(S,K);}
    assert(eqmat(mul(B,trans(B)),eye(n).map(r=>r.map(x=>BigInt(n)*x))),"tensor core Gram");
    const gauss=[];
    for(let q=0;q<p;q++){
      gauss[q]=[];
      for(let d=0;d<p;d++){
        const counts=Array(p).fill(0n);
        for(let b=0;b<p;b++)for(let c=0;c<p;c++){
          const exponent=((q*(b*b-c*c)+d*(b-c))%p+p)%p;
          counts[exponent]+=1n;
        }
        const reduced=counts.slice(0,p-1).map(x=>x-counts[p-1]);
        assert(reduced.slice(1).every(x=>x===0n),"Gauss norm must be rational");
        gauss[q][d]=reduced[0];
      }
    }
    const R=[];
    let Bpower=eye(n),hnormDen=1n;
    for(let m=0;m<=maxT;m++){
      const r=zeros(N),den=hnormDen*Bp*Bp;
      for(let i=0;i<N;i++)for(let j=0;j<N;j++){
        const h=Bpower[Math.floor(i/p)][Math.floor(j/p)];
        const d=(j%p-i%p+p)%p;
        const num=BN*h*h*gauss[m%p][d];
        assert(num%den===0n,"unmeasured common denominator");
        r[i][j]=num/den;
      }
      R.push(r);
      Bpower=mul(Bpower,B);
      hnormDen*=BigInt(n);
    }
    assert(eqmat(R[0],eye(N).map(row=>row.map(x=>x*BN))),"R0");
    const F=[zeros(N)],nonzeroTimes=[];
    const Sp=pow(S,p);
    for(let m=1;m<=maxT;m++){
      const accum=zeros(N);
      for(const t of nonzeroTimes){
        const product=mul(F[t],R[m-t]);
        for(let i=0;i<N;i++)for(let j=0;j<N;j++)accum[i][j]+=product[i][j];
      }
      const f=zeros(N);
      for(let i=0;i<N;i++)for(let j=0;j<N;j++){
        assert(accum[i][j]%BN===0n,"renewal denominator");
        f[i][j]=R[m][i][j]-accum[i][j]/BN;
        const a=Math.floor(i/p),b=i%p,c=Math.floor(j/p),d=j%p;
        let expected=0n;
        if(m===1)expected=1n;
        if(m===2)expected=BigInt(n)*S[a][c]-1n;
        if(m===p)expected=Bp*BigInt(b===d)-1n;
        if(m===2*p)expected=(BigInt(n)*Sp[a][c]-1n)*(Bp*BigInt(b===d)-1n);
        assert(f[i][j]===expected,"first-return exact coefficient");
        entryCount++;
      }
      F.push(f);
      if(nonzero(f))nonzeroTimes.push(m);
    }
    assert(JSON.stringify(nonzeroTimes)===JSON.stringify([1,2,p,2*p]),"support");
    const pulse=F[2*p],dW=BigInt((n-1)*(p-1));
    let fp=eye(N),traceDen=1n;
    const pulseTraces=[];
    for(let j=1;j<=3;j++){
      fp=mul(fp,pulse);traceDen*=BN;
      const numerator=tr(fp);
      assert(numerator%traceDen===0n,"trace denominator");
      const value=numerator/traceDen;
      assert(value===((p===3||j===3)?dW:0n),"unconjugated pulse trace");
      pulseTraces.push(value.toString());
    }
    const gram=mul(pulse,trans(pulse));
    for(let i=0;i<N;i++)for(let j=0;j<N;j++){
      const a=Math.floor(i/p),b=i%p,c=Math.floor(j/p),d=j%p;
      const Pnum=(BigInt(n)*BigInt(a===c)-1n)*(Bp*BigInt(b===d)-1n);
      assert(gram[i][j]===BN*Pnum,"pulse conjugated Gram");
      assert(fp[i][j]===BN*BN*Pnum,"pulse cube projection");
    }
    assert(tr(gram)===BN*BN*dW,"conjugated trace");
    const gramSum=zeros(N);
    for(const t of nonzeroTimes){
      const g=mul(trans(F[t]),F[t]);
      for(let i=0;i<N;i++)for(let j=0;j<N;j++)gramSum[i][j]+=g[i][j];
    }
    assert(eqmat(gramSum,eye(N).map(row=>row.map(x=>x*BN*BN))),"first-return Gram partition");
    cases.push({k,p,N,times:[1,maxT],first_return_entries:maxT*N*N,
      first_return_gram_sum:"I_N, all four pulses by time 2p",
      support:nonzeroTimes,pulse_unconjugated_traces_j_1_to_3:pulseTraces,
      pulse_conjugated_trace:dW.toString(),arithmetic:"matrix BigInt/common denominator N; direct power and cyclotomic Gauss norms"});
  }
  const permutationChecks=[];
  const kp=K.map(row=>row.findIndex(x=>x===1n));
  for(let k=2;k<=6;k++){
    const n=4**k;
    const perm=Array.from({length:n},(_,i)=>{
      let x=i,y=0,place=1;
      for(let h=0;h<k;h++){y+=kp[x%4]*place;place*=4;x=Math.floor(x/4);}
      return y;
    });
    for(const p of [3,5,7,11]){
      const fixed=[];
      for(let j=1;j<=3;j++){
        let count=0;
        for(let i=0;i<n;i++){
          let x=i;for(let h=0;h<p*j;h++)x=perm[x];
          if(x===i)count++;
        }
        fixed.push(count);
      }
      assert(JSON.stringify(fixed)===JSON.stringify(p===3?[n,n,n]:[1,1,n]),"tensor permutation trace");
      permutationChecks.push({k,p,n,fixed_S_p_S_2p_S_3p:fixed});
    }
  }
  return {status:"passed",source_candidate_commit:"d5411d8f8ec64868a6138dd8e100b1c0a6d06d4c",
    source_candidate_blob:"ad149b38e5e26ba31e78388cd2991bf5df77428b",
    comparison_order:"F_t times R_(m-t) on the left, no commutation used",
    cases,first_return_entries:entryCount,permutation_checks:permutationChecks,
    non_claims:["No universal finite-support proof from tested times","No min-max certification",
      "No phase-genericity or asymptotic proof","No physical measurement probability or BGS",
      "Unmeasured returns recomputed from direct tensor core powers and quadratic phase sums; first returns reconstructed by exact renewal"],
    environment:"functions V8; no Node wrapper or local filesystem execution",elapsed_ms:Date.now()-start};
}
