# Independent audit of the literal kick-phase law

## Verdict

**PASS, with the stated scope. No mathematical defect requiring a change to K1–K5 was found.** The proof establishes all fixed nonzero kick moments and the uniform singular-value and best-rank residual laws for the unchanged raw-quantized family at the literal fixed strength `tau=10^-80`, through every odd-dimensional subsequence. It does not establish microscopic BGS or any Heisenberg-scale trace estimate.

This is an independent internal proof audit, not an external referee report or a formal proof certificate. The finite verifier checks exact algebra only; the asymptotic conclusion rests on the analytic argument audited below.

Candidate reviewed: `literal_kick_phase_law.md`, SHA-256 `64dddeceeaee9c8ef639f0d143572e50ed430596d73b9b4a5c311951a7c73230`. All five frozen input hashes agree with `manifest.json`. No canonical repository file was changed. The candidate's all-odd-N conclusion uses neither primality nor generator/evolution spectral simplicity.

## 1. Exact model and sign audit

Writing a Fourier mode as `e_(k,l)(q,p)=exp(2*pi*i*(kq+lp))`, the matrix is `Op_N(e_(k,l))=W_N(l,k)`. Directly from the specified raw convention,

    W_N(a,b) u(j) = exp(pi*i*b*(2j+a)/N) u(j+a),

with periodic sample indices and integer Weyl labels. Consequently

    W_N(a,b) W_N(c,d)
      = exp(pi*i*(ad-bc)/N) W_N(a+c,b+d).

This identity holds at odd composite dimensions too; retaining integer labels retains every alias sign. Multiplication by `(-1)^(kl)` changes precisely the odd-p-frequency part of the raw symbol. The required ordinary symbol therefore contains `r(q+1/2)` in the p-dependent term. The candidate uses this exact symbol, rather than silently replacing the quantization.

For a g-frequency `(k,l)` and an a-frequency `(k',l')`, put `omega=l*k'-k*l'`. Then the commutator coefficient of `i*N[A_N,Op_N(a)]` is

    -2*N*sin(pi*omega/N),

whereas that of `X_g a/(2*pi)` is `-2*pi*omega`, because `X_g=(g_p,-g_q)`. These signs agree. Since g has finite Fourier support,

    ||i*N[A_N,Op_N(a)] - Op_N(X_g a/(2*pi))||_op
      <= C_g N^-2 sum_nu |a_nu| |nu|^3
      <= C'_g N^-2 ||a||_H5.

The last inequality uses Cauchy–Schwarz in dimension two; the weighted square sum behaves as `|nu|^-4`, and is summable. The sine-remainder estimate is global in the integer labels, so this does not require the evolving smooth observable to fit into a centered Fourier cell.

For `V_N(s)=exp(i*2*pi*s*N*A_N)`, differentiation of `V_N(s)* Op(a) V_N(s)` gives the minus of the classical generator. Thus the candidate's Egorov map is correctly `Phi_g^(-s)`. Duhamel yields even an `O_s(N^-2)` error for each fixed smooth observable. Fixed finite time, not small `tau*N`, is the relevant parameter.

The Weyl product and normalized Hilbert–Schmidt laws follow by truncating smooth Fourier series first and then taking N large enough to avoid aliases in each fixed truncation. Operator-norm tails are bounded by Fourier l1 tails. There is no number-theoretic exclusion of seven-divisible N.

## 2. Nilpotent equilibrium and every nonzero real time

The exact rational Fourier reconstruction gives zero gradient at `(0,0)` and

    Hess g(0,0) = diag(-(19606/125)*pi^2, 0).

In particular the candidate's coefficient is correct. The separate q-q contributions are `-196`, `196/5`, `0`, and `-6/125`, in units of pi squared. The p-dependent q derivative cannot be computed from unshifted r.

With `b=-(19606/125)*pi^2`,

    B = DX_g(0,0) = [[0,0],[-b,0]],
    B^2=0, B!=0.

At an equilibrium the variational equation is constant-coefficient for all real time. Hence `D Phi_g^s(0,0)=exp(sB)=I+sB`. Every nonzero real s gives a nonidentity derivative. This is an exact exclusion of every nonzero global period, including very large times. It is not a first-order approximation in s.

Completeness follows from compactness. Analyticity of each finite-time flow map follows from the local analytic ODE theorem and finite composition along trajectories. For fixed nonzero s, the analytic function

    f_s = sum_j (a_j composed with Phi_g^s - a_j)^2

formed from the four standard torus embedding coordinates is nontrivial, and its zero set is exactly `Fix(Phi_g^s)`. A nontrivial real-analytic function on the connected torus has a measure-zero zero set. Thus the necessary fixed set has area zero for every nonzero s. No quantitative sublevel estimate is needed.

## 3. Overlap argument and the order of limits

Set `h_j=a_j composed with Phi_g^(-s)-a_j`, `f=sum h_j^2`, and `t_N(c)=Tr(V_N(s) Op_N(c))/N`. Egorov gives

    Op_N(a_j) V_N(s)
      = V_N(s) Op_N(a_j composed with Phi_g^(-s)) + o_op(1).

After multiplying by `Op_N(c)`, cyclicity and the product calculus give `t_N(c h_j)=o(1)`. All symbols here are fixed while N tends to infinity.

Choose the cutoff with `0<=chi_epsilon<=1`, equal to one in a neighborhood of zero and supported in `f<=2*epsilon`. Then

    1-chi_epsilon(f) = sum_j [(1-chi_epsilon(f))*h_j/f] h_j,

where every bracket extends smoothly across the zero set because the numerator vanishes in a whole neighborhood of it. Therefore `t_N(1-chi_epsilon(f))->0` for each fixed epsilon. Unitarity and normalized HS Cauchy–Schwarz give

    limsup_N |Tr V_N(s)|/N <= ||chi_epsilon(f)||_L2.

Now, and only now, send epsilon to zero. Bounded convergence and the area-zero fixed set give zero. Growth of cutoff derivatives as epsilon shrinks is harmless because the N limit came first.

For every fixed integer `m!=0`, `Q_N^m=V_N(m*tau/(2*pi))`, with a nonzero, N-independent real flow time. This proves K1 for all positive and negative fixed m. Fourier approximation then proves weak circular equidistribution. This does not interchange an infinite Fourier sum with an uncontrolled m-dependent limit and does not allow m to grow with N.

An important strength of this argument is that it uses the quantum propagator and Egorov directly. Applying only the macroscopic eigenvalue law of A_N to the N-dependent function `exp(i*m*tau*N*x)` would not justify K1.

## 4. Uniform arcs, chord distribution, and best rank

Weak convergence to atomless uniform circular measure implies uniform discrepancy over all circular arcs. For completeness, fix a finite mesh. Counts in the finitely many mesh arcs converge, and an arbitrary arc is bracketed by mesh arcs whose total excess length tends to zero as the mesh is refined. The same argument forces the largest atom to vanish, covering either endpoint convention and degenerate arcs.

The actual M_N is unitary at every odd N. This follows directly by summing its quadratic-kernel row inner products: the remaining frequency is a nonzero unit multiple of the row difference modulo N, so orthogonality holds for composite N as well. Therefore right multiplication by M_N* preserves singular values and rank, and

    (U_N-z M_N) M_N* = Q_N-zI.

The singular values are exactly `|exp(i*theta_j)-z|`. The sublevel set at `0<=s<=2` is an arc of length `4*arcsin(s/2)`. Uniform arc discrepancy proves K2 uniformly in both z and s, including the endpoints.

For increasing singular values `s_(j,N)(z)`, uniform distribution convergence to the continuous strictly increasing chord CDF implies uniform quantile convergence, with the endpoints obtained by positive limiting mass near 0 and 2. For `r_N/N->rho<1`,

    s_(N-r_N,N)(z) -> 2*cos(pi*rho/2),

uniformly in z. Integrating bounded quantiles, or bracketing their Riemann sums, similarly gives

    (1/N) sum_(j<=N-r_N) s_(j,N)(z)^2
      -> integral_0^(1-rho) 4*sin(pi*u/2)^2 du
       = 2*(1-rho) - (2/pi)*sin(pi*rho),

uniformly in z. The rank convention is correct: a rank-r approximation removes the r largest singular values, leaving the `(N-r)`th increasing singular value as the optimal operator residual. The HS residual is exactly the sum of the `N-r` smallest squared singular values. Thus K4 and K5 follow without restrictions on how a minimizing correction depends on N or z.

K3 is the rho=0 case. The necessity of rank `N-o(N)` for a vanishing error follows by taking a subsequence with a rank ratio bounded away from one and using the strictly positive limiting residual. In fact the same uniform CDF reasoning also gives sufficiency for the *optimal* residual when `r_N/N->1`, although that endpoint extension is not needed by the written theorem.

## 5. Exceptional 7 and safe scope

The isolated dimension N=7 has `A_7=(9/10)I` and a scalar kick. This is verified exactly over the seventh cyclotomic field. It does not contradict any asymptotic assertion. For large seven-divisible N, the direct-sum Jacobi decomposition remains a finite exceptional multiplicity phenomenon; the Egorov/product/HS proof still applies without modification. There is no hidden use of simplicity, no removal of this subsequence, and no extrapolation from p-adic values.

All of the following qualifications in the candidate are necessary and correctly retained:

- No uniformity in a growing moment index m or an N-dependent coupling.
- No effective startup estimate at the tiny literal strength.
- Direct comparison is with scalar multiples of the actual M_N.
- Arbitrary N-dependent conjugacy, selected low-dimensional subspaces, other comparison operators, and microscopic statistics of U_N are outside K1–K5.
- The product's signed factorial/Heisenberg trace problem remains open.

The proof actually needs only that tau be a fixed nonzero real number, rather than its rationality or tiny size. This observation strengthens the mathematical mechanism without changing the frozen target. The isolated finite-dimensional N=7 scalar return and possible long pre-asymptotic near-scalar behavior remain compatible with the result.

## 6. Defects and presentation notes

**Exact defects found: none.** Two harmless clarifications would make a final exposition harder to misread:

1. State `0<=chi_epsilon<=1` explicitly in the cutoff construction.
2. Optionally mention the finite N=7 scalar kick when saying that every seven-divisible subsequence is included. No claim of finite-N uniformity or a small effective onset is available.

Neither item changes the proof or theorem. In particular, the notation "centered generator" refers to the prescribed subtraction of `1/10`; it must not be read as a new finite-N trace recentering at the exceptional small dimensions.

## Exact verifier

Run `python review/audit_exact_verifier.py` from the artifact root. Its saved output is `review/audit_exact_verifier_output.json`. It checks all input hashes, the raw-to-midpoint coefficient dictionary, all four exact Hessians, nilpotent exponentiation, 6,561 integer modular Weyl product phases including aliasing, the exact N=7 matrix, gcd cut counts, the commutator sign, and the two rank-limit formulas. It contains no finite-N kick equidistribution experiment and cannot certify the asymptotic proof by itself.
