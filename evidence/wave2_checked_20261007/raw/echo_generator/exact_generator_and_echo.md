# Exact finite-N sine action and one-pinch trace

Independent reconstruction at the pinned checked snapshot. These identities
are already present in the accepted source chain; the independent work checks
signs, integer aliases and implementation. No claim of new identities.

## Literal quantizer, with no modular half-shift substitution

N is odd, tau=10^-80 is fixed, and indices j,k are residues modulo N.
Set e_N(x)=exp(2pi i x/N), inv2=(N+1)/2, and

    (T_N(a,b)u)_j=e_N(b(j+inv2*a))u_(j+a),
    W_N(a,b)=(-1)^(ab)T_N(a,b),
    (M_N)_jk=N^-1/2 e_N(-inv8*(3j^2-2jk+3k^2)),

where a,b are ORDINARY integers and inv8 is the inverse of 8 modulo N.
Since exp(2pi i b inv2 a/N)=(-1)^(ab)exp(pi i ab/N),

    (W_N(a,b)u)_j=exp(2pi i b(j+a/2)/N)u_(j+a).          (W1)

In particular, with omega(v,w)=v_a*w_b-v_b*w_a,

    W_N(v)W_N(w)=exp(pi i omega(v,w)/N)W_N(v+w),
    W_N(v)*=W_N(-v),
    W_N(a+Nr,b+Ns)=(-1)^(br+as+Nrs)W_N(a,b).             (W2)

The product follows by evaluating the two shifts in order: its extra phase
is (v_a*w_b-v_b*w_a)/2. The alias identity follows by substituting W1;
the integral term s*j contributes no phase. In particular a or b cannot
be reduced modulo N and the sign discarded.

The physical symbol is precisely

    r(q)=(1-cos(14pi q))(1+cos(2pi q)),
    g(q,p)=cos(14pi q)+r(q)/10+r(q)sin(2pi q)/100
             +r(q+1/2)cos(2pi p-alpha)/100-1/10,
    cos(alpha)=-3/5, sin(alpha)=4/5.

If e_(a,b)(q,p)=exp(2pi i(bq+ap)) and g=sum_v c_v e_v, then
A_N=sum_v c_v W_N(v). The Fourier support is fixed and finite. Equivalently,
with r(q)=sum_b r_b exp(2pi i bq),

    c_(1,b)=(-3-4i)(-1)^b r_b/1000,
    c_(-1,b)=(-3+4i)(-1)^b r_b/1000.

The diagonal coefficients are from cos(14pi q)+r(q)/10+
r(q)sin(2pi q)/100-1/10. In particular

    c_(0,1)=1/20-i/200, c_(0,2)=-i/400.

The half-shift (-1)^b in the off-diagonal coefficients is forced. The
independent midpoint construction used for finite controls is

    (A_N u)(j/N)=sum_(a,b)c_(a,b)
        exp(2pi i b(j+a/2)/N)u((j+a)/N).

For a=+/-1 its off-diagonal entry is
r(j/N+a/(2N)+1/2)(-3-4ai)/1000, and the diagonal entry is the displayed
p-independent part of g at q=j/N. At low N all aliases are retained.

## Generator, exponential order and cat orientation

Let L_N=iN ad(A_N), C_N=Ad(M_N), and T_N=Ad(U_N),
U_N=exp(i tau N A_N)M_N. Subtracting the reversed Weyl product gives

    L_N W_N(nu)
       =-2N sum_v c_v sin(pi omega(v,nu)/N)W_N(v+nu).      (W3)

The minus sign is i*(2i)=-2. The finite support is in the increment v;
iterating L_N is not a support truncation or classical sine linearization.
Substitution of the exact quadratic metaplectic kernel gives

    C_N W_N(nu)=W_N(S nu), S=[[3,4],[2,3]],
    T_N=exp(tau L_N) C_N.                                (W4)

This is the order of operations for Ad(exp(i tau N A)M); interchanging the
factors changes the operator. In (q,p) coordinates e_nu pulls back by S,
consistent with the frequency pair (p-frequency,q-frequency)=(a,b).
Repeated conjugations require ordered products of transported kick
exponentials. They do not permit an unordered exponential of summed kicks.

W1--W4 hold for every finite odd N, including composite N and low-N alias
collisions. The controls use a FORMAL real variable t for exp(t L_N);
no auxiliary numerical t is substituted for literal tau and no jet is used
to infer a fixed-tau size estimate.

## Charge twirl and ordinary traces

On H=End(C^N), put E_(c,j)=|j><j+c| and let P_c project onto its span.
For Z_b=diag(e_N(bj)), R_b=Ad(Z_b),

    R_b E_(c,j)=e_N(-bc) E_(c,j).

Character orthogonality therefore proves

    D=sum_c P_c T P_c=(1/N)sum_b R_b T R_b*.

V_theta=Ad(Z_theta) commutes with R_b. If W_theta=Z_theta U,
A_theta=V_theta T and B_theta=V_theta D, then

    B_theta=(1/N)sum_b Ad(Z_b W_theta Z_b*).

Since products of adjoint maps compose their unitary arguments and
Tr_H Ad(K)=|tr K|^2, cyclicity gives exactly

    E_N,m(theta)=Tr_H[B_theta A_theta^(m-1)]
       =(1/N)sum_b |tr(W_theta^(m-1) Z_b W_theta Z_b*)|^2. (E1)

There is no normalized matrix trace in E1. The factor 1/N is the finite
twirl, and the outer pair-aggregate normalization remains N^-2.

Writing H=W_theta^(m-1) and grouping the matrix trace by c=k-j gives

    tr(H Z_b W_theta Z_b*)
       =sum_c e_N(-bc) sum_j H_(j+c,j)(W_theta)_(j,j+c).

Thus Parseval gives the exact charge-energy identity

    E_N,m(theta)=sum_c |sum_j H_(j+c,j)(W_theta)_(j,j+c)|^2. (E2)

This formula retains the cyclic signs/orientation and has no phase
approximation. The coefficient-polynomial controls compare it with the
independent superoperator trace and literal rooted occupation expansion.

## The ordinary flatness bound and exact occupation subtraction

Suppose max_jk |U_jk|^2<=C/N. The same bound holds for W_theta. For each c,
Cauchy--Schwarz gives

    |sum_j H_(j+c,j)(W_theta)_(j,j+c)|^2
      <=(sum_j |H_(j+c,j)|^2)(sum_j |U_(j,j+c)|^2)
      <=C sum_j |H_(j+c,j)|^2.

Summing c and using unitarity of H gives

    0<=E_N,m(theta)<=C N                                (E3)

for every m>=1 and arbitrary theta. Both E_N,m(0) and its theta average
lie in [0,CN], so their difference has absolute value <=CN (even the
looser 2CN bound is unnecessary). This only gives O(1) after N^-2 compact
Heisenberg-time aggregation.

For a rooted cyclic path x of length m, let c=x_1-x_0 (at m=1, c=0),
A_U(x)=product_t U_(x_t,x_(t+1)), and n(x) its complete integer occupation
vector. Put

    a_(c,n)=sum_(x: x_1-x_0=c, n(x)=n) A_U(x).

Then E_N,m(0)=sum_c |sum_n a_(c,n)|^2 and

    integral E_N,m(theta)dtheta=sum_(c,n)|a_(c,n)|^2.

Their difference is the complete n!=n' cross term within each marked c,
with every repeated coordinate retained. A full phase integral is essential:
a linear modulation average alone only imposes a checksum condition.
