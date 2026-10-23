(* Finite exact algebra; no universal representation-theory certification. *)
ClearAll[hh, thirdFormula, phaseOccupation, matrixZero, nn, s];
matrixZero[m_List] := And@@((Expand[#]===0)& /@ Flatten[m]);
hh[v_List] := IdentityMatrix[Length[v]] -
  2 Outer[Times, v, Conjugate[v]]/(Conjugate[v].v);
thirdFormula[u_List] := Module[{p, q, n, mix},
  n=Length[u];
  p=Map[Abs[#]^2 &, u, {2}];
  q=u Conjugate[Transpose[u]];
  mix=Total[Flatten[Table[If[i==j,0,p[[i,i]]p[[i,j]]p[[j,i]]],
    {i,n},{j,n}]]];
  FullSimplify[3 Tr[MatrixPower[p,3]]+3 Tr[MatrixPower[q,3]]-
    5 Total[Diagonal[p]^3]-9 mix]
];
phaseOccupation[u_List] := Module[{vars, rules, n},
  n=Length[u]; vars=Array[s,n];
  rules=CoefficientRules[Expand[Tr[MatrixPower[DiagonalMatrix[vars].u,3]]],vars];
  FullSimplify[Total[Abs[Last[#]]^2 & /@ rules]]
];
f4=Table[I^((i-1)(j-1))/2,{i,4},{j,4}];
units={hh[{1,I}],
  hh[{1,2,I}].DiagonalMatrix[{1,I,(3+4I)/5}],
  f4.hh[{1,2,I,-I}].DiagonalMatrix[{1,I,-1,(3+4I)/5}]};
unitaryFlags=FullSimplify[#.ConjugateTranspose[#]==IdentityMatrix[Length[#]]] & /@ units;
occupationValues=phaseOccupation /@ units;
traceValues=thirdFormula /@ units;
occupationFlags=MapThread[SameQ,{occupationValues,traceValues}];
adjointVariance=FullSimplify[
 nn*2/(nn*(nn+1))+nn*(nn-1)/(nn^2-1)-1,
 Assumptions->nn>1];
adjointFlag=FullSimplify[adjointVariance==1/(nn+1),Assumptions->nn>1];
vecs=Tuples[Range[0,2],2]; bb={{1,1},{0,1}};
omega3=(-1+I Sqrt[3])/2;
u9=Table[Expand[omega3^Mod[x.bb.y,3]]/3,{x,vecs},{y,vecs}];
q9=Map[Expand,u9 Conjugate[Transpose[u9]],{2}];
qFlags={
  matrixZero[u9.ConjugateTranspose[u9]-IdentityMatrix[9]],
  matrixZero[MatrixPower[q9,3]-q9/9],
  Expand[Tr[MatrixPower[q9,3]]-1/9]===0,
  FullSimplify[thirdFormula[u9]==3+3/9-9/9+4/81]
};
ExportString[<|"kernel_version"->$Version,
 "unitary_flags"->unitaryFlags,"occupation_flags"->occupationFlags,
 "exact_occupation_values"->(ToString[#,InputForm] & /@ occupationValues),
 "adjoint_variance"->ToString[adjointVariance,InputForm],
 "adjoint_flag"->adjointFlag,"bilinear_flags"->qFlags,
 "all_passed"->And@@Join[unitaryFlags,occupationFlags,{adjointFlag},qFlags]|>,"RawJSON"]
