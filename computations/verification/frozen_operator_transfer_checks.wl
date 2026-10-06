(* Independent symbolic checks for FM-018; no BGS or asymptotic certificate. *)
ClearAll[l, r, n, x, t, theta, rho];
cosAd = (l + 1/l - r - 1/r)/2;
sinAd = (l - 1/l - r + 1/r)/(2 I);
gaussian = Integrate[Exp[-x^2/2 + I t x]/Sqrt[2 Pi],
  {x, -Infinity, Infinity}, Assumptions -> Element[t, Reals]];
weylFunctional = 1 - (1 - 1/n) rho;
fourierFunctional = (1 - rho)/(1 - rho/n);
checks = <|
  "squaredCommutatorPair" ->
    (Together[cosAd^2 + sinAd^2 - (2 - l/r - r/l)] === 0),
  "gaussianCharacteristic" ->
    FullSimplify[gaussian == Exp[-t^2/2], Element[t, Reals]],
  "sameQuadraticCoefficient" ->
    (Together[(D[-Log[weylFunctional], rho] -
      D[-Log[fourierFunctional], rho]) /. rho -> 0] === 0),
  "differentQuarticCoefficient" ->
    (Together[((D[-Log[weylFunctional], {rho, 2}] -
      D[-Log[fourierFunctional], {rho, 2}])/2 /. rho -> 0) -
      (-1/n + 1/n^2)] === 0),
  "commonNoiseCommutatorEntry" ->
    FullSimplify[(Exp[I theta] + Exp[-I theta] - 2)^2 ==
      4 (1 - Cos[theta])^2, Element[theta, Reals]],
  "swapNorm" ->
    (Together[(n (1 - 1/n)^2 + (n^2 - n) (1 + 1/n^2))/n^2 -
      (1 - 1/n^2)] === 0)
|>;
<|"claim" -> "BGS-FM-018", "checks" -> checks,
  "allPassed" -> And @@ Values[checks],
  "scope" -> "Six symbolic identities; no analytic gap, large-N spectral computation or BGS certificate"|>
