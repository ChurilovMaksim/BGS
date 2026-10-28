# Orbit-orthogonal spike at \(u_{203}\)

28 October 2026. `BGS-TRACE-118` is a project proof, not a closure of `BGS-TRACE-005`.

The one-term majorant of `BGS-TRACE-117` is at most \(3/4\) at \(n=203\). The replacement is a second-order expansion of \(\operatorname{Tr}U_N^n\). Conjugates of \(A_N\) by powers of \(M_N\) are trace-orthogonal except for the overlap

\[
C(1,-1)=(1,1),\qquad C(-1,1)=(-1,-1),
\]

which contributes \(\gamma(1)=\gamma(202)=-7/2000000\). With that exact second moment, the third-order operator-norm remainder still leaves

\[
L_{u_{203}}(U;1)>\frac34.
\]

The integer \(u_{203}\) has 78 decimal digits. At \(n=205\) the third-order remainder is at least \(1\) and the Hilbert--Schmidt triangle deficit exceeds \(1\). The pure second-order center still clears \(3/4\) at that index. At \(n=207\) the same center satisfies \((1-\varepsilon_2)^2<3/4\), after the overlap classification is repeated there. This is a failure of the disk, not a drop of \(L_N\).

Python, C++ and `formalization/Bgs/OrbitOrthogonalRational.lean` certify the integers. The analytic comparison was checked by the author. There is no independent referee. `BGS-BGS-001` remains open.
