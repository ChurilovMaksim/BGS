(* Executed in Wolfram Language through the connected evaluator.
   This checks calculus for a published support formula, not the return theorem.
   Python/SymPy provides a separate maintained check in return_local_limits.py. *)
With[{b = Sqrt[t (4 - t)]/2 + ArcCos[1 - t/2]},
 {FullSimplify[D[b, t] - Sqrt[(4 - t)/t]/2, 0 < t < 4],
  Series[1 - (b /. t -> 4 - s)/Pi, {s, 0, 2}],
  N[Table[{u, 1 - (b /. t -> u)/Pi}, {u, {1, 2, 3}}], 16]}]
