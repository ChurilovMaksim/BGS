# Full-lag uniform classical resonance gap for the frozen physical symbol

Stable claim ID: `BGS-RES-005`. Date: 23 September 2026.

Status: project proof with separate internal derivation audit; no external referee or priority claim. This concerns brackets transported by the *linear* map S, not the nonlinear kicked classical map and not quantum joint traces or BGS.

Let S=[[3,4],[2,3]], A=S^T, lambda=3+2 sqrt(2), C f=f composed with S, and let g be precisely the ordinary-Weyl physical symbol (1) of `mathematics/fixed-map/fixed_model_symmetry_theorem.md`. Put h_r={g,C^r g}/(4 pi), r>=1. The bracket convention is {f,k}=f_q k_p-f_p k_q, so its Fourier pair coefficient is -pi det(u,A^r v). With normalized torus measure, every finite complex array a_(r,l), r>=1, l in Z, satisfies

    (7 pi/2)^2 sum |a_(r,l)|^2
      <= ||sum a_(r,l) lambda^(-r) C^l h_r||_2^2
      <= (40 pi)^2 sum |a_(r,l)|^2.                    (1)

For each oriented nonzero A-orbit choose a representative v_O and set J_omega(f)_O=sum_(j in Z) fhat(A^j v_O) exp(i j omega). This gives J_omega(Cf)=exp(i omega)J_omega(f).

There is no discarded initial lag and no restriction on the translation window. These constants are conservative certified rational bounds, not optimal constants.

## 1. A one-visit refinement on this support

Set xi(x,y)=x+y/sqrt(2), eta(x,y)=(-x+y/sqrt(2))/sqrt(2). Their coordinate determinant is one, xi(Av)=lambda xi(v), eta(Av)=lambda^(-1) eta(v), and det(u,v)=xi(u)eta(v)-eta(u)xi(v).

Every nonzero frequency of g belongs to

    D={(x,y) in Z²: |y|<=|x|, x!=0} union {(0,y): y!=0}.

For horizontal-cone frequencies, rho(v)=(x+y/sqrt(2))/(x-y/sqrt(2)) lies in [lambda^(-1),lambda]; on the vertical axis rho=-1. Thus for u,v in D, the ratio

    R=xi(u)eta(v)/(eta(u)xi(v))=rho(u)/rho(v)

is either negative or positive and at most lambda². Neither denominator vanishes for a nonzero integer frequency.

The invariant q(k)=det(k,Ak) is (lambda^(-1)-lambda)xi(k)eta(k). Apart from a nonzero common factor and an additive constant, q(u+A^r v) is

    D0 lambda^r + E0 lambda^(-r),
    D0=eta(u)xi(v), E0=xi(u)eta(v).

Its consecutive difference is

    D0 lambda^r (lambda-1) [1-R lambda^(-2r-1)].

For R<0 the square bracket is positive; for 0<R<=lambda² and r>=1 it is at least 1-lambda^(-1)>0. Therefore q(u+A^r v) is strictly monotone in r>=1. Each oriented A-orbit is visited at most once by this sequence. A zero output has determinant coefficient zero and may be omitted.

## 2. Anisotropic synthesis estimate without sqrt(2)

Write

    X(f)=sum_v |xi(v)| |fhat(v)|,
    Y(f)=sum_v |eta(v)| |fhat(v)|.

For functions f,k supported in D, their bilinear synthesis at every dynamical Fourier frequency omega is

    B_(f,k)(omega)a = sum_(r>=1) a_r lambda^(-r)
                     J_omega({f,C^r k}/(4 pi)).

For a fixed ordered Fourier pair (u,v), the one-visit result makes its output rows disjoint for distinct r. Hence its operator norm is bounded by its largest individual coefficient, without the sqrt(2) loss in the general two-visit lemma. Since

    lambda^(-r) det(u,A^r v)
       =lambda^(-2r)xi(u)eta(v)-eta(u)xi(v),

summing pair norms gives, uniformly in omega,

    ||B_(f,k)(omega)||
       <= pi [Y(f)X(k)+lambda^(-2)X(f)Y(k)].          (2)

The same holds for limits in these weighted Fourier norms. For the present polynomial all sums are finite. Each dynamical phase has modulus one, so the estimate is uniform at every omega, not merely almost everywhere.

## 3. Dominant harmonic and exact Fourier moments

Decompose g=b+e with b=(9/10)cos(14 pi q). Thus bhat(±7,0)=9/20, X(b)=63/10, Y(b)=63/(10 sqrt(2)).

The following table gives the coefficients of e at the listed frequencies; opposite frequencies have conjugate coefficients. In rows with independent signs, both signs are included.

| frequency | coefficient |
|---|---|
| (1,0) | 1/20-i/200 |
| (2,0) | -i/400 |
| (5,0) | -i/800 |
| (6,0) | -1/40-i/400 |
| (8,0) | -1/40+i/400 |
| (9,0) | i/800 |
| (0,1) | -3/1000-i/250 |
| (±1,1) | 3/2000+i/500 |
| (±6,1) | 3/4000+i/1000 |
| (±7,1) | -3/2000-i/500 |
| (±8,1) | 3/4000+i/1000 |

These follow by expanding the physical symbol, including its essential q→q+1/2 shift in the p-dependent term. The (±7,0) coefficients have been removed exactly into b; the zero coefficient is zero.

Reflection symmetry of coefficient magnitudes yields

    X(e)=E=2 sqrt(101)/25+(39+sqrt(2))/200,
    Y(e)=E/sqrt(2),      E<101/100.                     (3)

For example, the q-only contribution is 2 sqrt(101)/25+9/200, the nonzero-q mixed contribution is 3/20, and the vertical contribution is sqrt(2)/200. The upper bound follows from sqrt(101)<201/20 and sqrt(2)<283/200.

## 4. Uniform lower bound for the unperturbed harmonic

For b, the four output frequencies ±v±A^r v, v=(7,0), lie on mutually distinct oriented A-orbits, for all r>=1. Indeed their q-values are q(v)(2±(lambda^r+lambda^(-r))); these separate different r and the plus/minus cases. Each frequency and its negative lie on different oriented orbits because A has positive eigenvalues and an integer nonzero frequency has nonzero expanding coordinate. Therefore the columns of B_(b,b)(omega) are orthogonal, independently of omega, with norm

    2 pi (9/20)^2 lambda^(-r)|det(v,A^r v)|
      =2 pi (9/20)^2 (49/sqrt(2))(1-lambda^(-2r)).

The infimum is at r=1 and equals

    s_b=3969 pi/(50 lambda)> (68/5)pi.                  (4)

Here det(v,Av)=196 and lambda<583/100 prove the last strict inequality by rational arithmetic.

## 5. Perturbation bound and passage to translated arrays

Let S_f=B_(f,f). Bilinearity, (2), and (3) imply

    sup_omega ||S_g(omega)-S_b(omega)||
      <= pi (1+lambda^(-2))/sqrt(2) [(63/5)E+E²]
      < (401/40)pi.                                    (5)

A purely rational verification uses lambda^(-2)<3/100, 1/sqrt(2)<177/250, and E<101/100: the resulting coefficient is 10.024205964 < 401/40=10.025. Consequently

    ||S_g(omega)a|| >= (143/40)pi ||a|| > (7/2)pi ||a||.

Also (2) gives

    ||S_g(omega)|| <= pi(1+lambda^(-2))(63/10+E)²/sqrt(2)
                   <40 pi.

These statements hold simultaneously for all omega and all l2 lag sequences. Apply them to a_r(omega)=sum_l a_(r,l)exp(i l omega) and integrate in omega. The dynamical orbit Fourier transform is unitary by ordinary Fourier Parseval and J_omega(Cf)=exp(i omega)J_omega(f). Parseval in l then proves (1).

## 6. What this changes and what it leaves open

This closes the finite-initial-lag and uniform-dynamical-frequency gap for this particular frozen physical observable under linear transport. The previous general eventual-tail theorem alone did not imply (1), and fixed finite-lag independence alone could not imply a uniform infinite-dimensional lower bound. The decisive extra input is the one-visit geometry of this concrete Fourier support.

It does not estimate brackets along the nonlinear kicked map F_tau, quantum traces at Heisenberg time, or microscopic eigenphase statistics. In particular, BGS-TRACE-005 remains open. No novelty or priority claim is made pending literature comparison and independent review.

## 7. Explicit infinite-support neighborhood

The cone restriction is required only for certifying the center g. Let w be any real perturbation (possibly with infinitely many Fourier orbits) with M1(w)=sum_(v!=0)|v||what(v)|<=1/100. Constants are irrelevant. The existing unrestricted two-visit bound gives

    sup_omega ||S_(g+w)(omega)-S_g(omega)||
      <= sqrt(2) pi kappa_A M1(w)[2 M1(g)+M1(w)].

Here kappa_A<=sqrt(2): D^(-1) A D, with D=diag(1,sqrt(2)), is the symmetric matrix [[3,2sqrt(2)],[2sqrt(2),3]], with norm lambda. The physical-symbol bound sum(|Re ghat|+|Im ghat|)|v|²=51451/1000<52 implies M1(g)<52, since |v|>=1 for nonzero integer v. Thus the displayed perturbation norm is at most

    (10401/5000)pi=2.0802 pi.

Combining this with the conservative 7pi/2 lower bound proves, for every such w and finite array,

    pi² sum |a_(r,l)|²
      <= ||sum a_(r,l)lambda^(-r) C^l h_r(g+w)||_2²
      <= (43pi)² sum |a_(r,l)|².                         (6)

Indeed 7/2-10401/5000>1 and 40+10401/5000<43. This is an explicit full-lag Riesz neighborhood in the unrestricted weighted Wiener space, including smooth and analytic perturbations of infinite Fourier support. It does not establish the corresponding property for every analytic observable.
