(* Exact finite enumeration; not an asymptotic spectral assertion. *)
Table[
  Module[{g = RotateLeft[Range[r]], data, s, inv, pi},
    data = Table[
      s = ConstantArray[0, r];
      Do[s[[ord[[i]]]] = ord[[Mod[i, r] + 1]], {i, r}];
      If[And @@ MapThread[Unequal, {s, g}],
        inv = Ordering[s];
        pi = inv[[g]];
        Length[First[PermutationCycles[pi]]],
        Nothing
      ],
      {ord, (Prepend[#, 1] & /@ Permutations[Range[2, r]])}
    ];
    {r, Length[data], Sort[Tally[data]],
      Sum[(-1)^j Binomial[r, j] (r - j - 1)!, {j, 0, r - 1}] + (-1)^r}
  ],
  {r, 3, 9}
]
