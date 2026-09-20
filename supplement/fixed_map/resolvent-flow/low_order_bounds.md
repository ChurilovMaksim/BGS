# What the first two mixed loop levels actually imply

Status: exact identities and a conditional bound, internally audited.
The residual hypotheses below are unproved for the frozen map. No
universality theorem or priority is claimed.

Use the notation of `loop_bridge.md`. Fix s>0, w=is/2, v=-is/2,
S=s_N(w), M_r=E_alpha |S|^r. Let

\[
 e_2=\Re\frac{\mathcal E_{2,N}(w,v)}{8i}
       =L_N+\Re C_N^0-\frac1{4s^2},\qquad
 e_3=\mathcal E_{3,N}(w,v,v).
\]

Then the second mixed level has the exact scalar form

\[
 \boxed{e_3=M_4-1-\frac2{s^2}(M_2+1)\in\mathbb R.}\tag{1}
\]

Indeed, put T=s_N(v)=bar(S). The holomorphic same-half-plane identities
give E T^2=-1 and E T'T=0, where the prime is the derivative with respect
to v. Each differentiated quotient in the loop equation contributes

\[
 E\left[\left(-\frac{T'}{w-v}
                   +\frac{S-T}{(w-v)^2}\right)T\right]
       =-\frac{M_2+1}{s^2}.
\]

There are two identical quotient terms. The leading term is M_4-1,
proving (1), including its reality.

Set P=(S/i-1)/2 and Q=E|P|^4. Its strictly positive origin Fourier
frequencies give E P=E P^2=0 and

\[
 M_2=1+4L_N,\qquad
 M_4=1+16L_N+32\Re C_N^0+16Q.
\tag{2}
\]

Eliminating the cubic term between (1), (2), and e_2 gives

\[
 Q=\left(1+\frac1{2s^2}\right)L_N-\frac1{4s^2}
                         +\frac{e_3}{16}-2e_2.
\tag{3}
\]

Jensen's inequality Q>=L_N^2 therefore proves the finite-dimensional
bound

\[
 L_N^2-\left(1+\frac1{2s^2}\right)L_N+\frac1{4s^2}
                         \le\frac{e_3}{16}-2e_2.
\tag{4}
\]

The quantity on the right may have either sign; no absolute-value loss
or presumed independence was used.

## Normalized residuals already supply boundedness

Suppose only that the p=3 residual at this pair of points obeys

\[
 |e_3|\le\delta_N(1+M_4),\qquad\delta_N\to0.
\tag{5}
\]

From (1), writing t=s^-2 and x=M_2, Jensen M_4>=x^2 gives

\[
 (1-\delta_N)x^2-2tx-(1+\delta_N+2t)\le0.
\]

For large N this bounds x and then M_4 uniformly. Therefore (5) improves
to e_3->0. In particular, limsup L_N(s)<=1/(2s^2).

If the p=2 residual also tends to zero after division by 1+M_3, the
fourth-moment bound makes it tend to zero without normalization, so
e_2->0. Every subsequential limit ell of L_N(s) then lies in the interval

\[
 \frac12+\frac1{4s^2}-\frac12\sqrt{1+\frac1{4s^4}}
 \ \le\ \ell\ \le\ \frac1{2s^2}.
\tag{6}
\]

The upper bound from (1) is sharper than the larger root of (4).
The interval has positive width for every s>0. These inequalities do
not identify the CUE value (1-exp(-2s))/(4s^2), establish convergence,
or construct a non-CUE process satisfying both residual hypotheses.
They show precisely how much this low-order elimination proves before
additional spectral input is needed. Vanishing of the actual fixed-map
residuals, even at these first two levels, remains unproved.

An independent internal algebra audit checked signs, coefficients, and
the moment bound. `low_order.py` compares the original loop expression,
cotangent moments, and the separate trace/geometric sums at 27 finite
cases. Auxiliary exponent 0.17 checks the algebra only, not the original
coupling tau=10^-80. Lean kernels record selected cleared-denominator
algebra; they do not formalize the Herglotz or asymptotic arguments.
