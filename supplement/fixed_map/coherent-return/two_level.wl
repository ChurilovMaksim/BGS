(* Independent symbolic verification; 0<t<1, -1<c<1.
   t is the invariant spectral weight, c=cos(eigenphase gap).
   No BGS conclusion is claimed. *)
Clear[z, t, c, a, s, cf, f];
a = t + (1 - t) c;
s = 1 - t + (1 + t) c;
cf = t/(1 - z) + (1 - t) (1 - z c)/(1 - 2 z c + z^2);
f = z (a - s z + z^2)/(1 - s z + a z^2);
{
 Factor[1 - 1/cf - f],
 Factor[f /. z -> 1],
 Factor[D[f,z] /. z -> 1],
 Factor[D[f,{z,2}] /. z -> 1],
 Factor[D[f,{z,3}] /. z -> 1]
}
