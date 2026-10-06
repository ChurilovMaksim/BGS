# Centered homoclinic action response: bounded values, unbounded label C1 norm

Status: an elementary all-period argument for the specified first action response, with independent exact finite arithmetic checks. It is a scoped smoothness discriminator. It neither estimates the actual fixed-tau paired sum nor contradicts locality in orbit-code coordinates.

## 1. Result

Keep the actual ordinary half-shifted symbol g, S=[[3,4],[2,3]], and G_m=Fix(S^m). Set

    d_m=(S^m-I)^(-1)(0,1) mod Z^2,
    I_m={-floor(m/2), ..., ceil(m/2)-1},
    F_m(x)=sum_{j in I_m} [g(S^j(x+d_m))-g(S^j x)].      (1)

This is the centered-time torus representative. On G_m it agrees exactly with the original sum over 0<=j<m. Statements below concern this centered representative and its finite-group values; they do not rely on the very large uncentered positive-time frequencies near j=m.

The actual isolated mode v=(1,0) has

    c_v=1/20-i/200=(10-i)/200,  |c_v|^2=101/40000.

Put lambda=3+2sqrt(2). If j tends to infinity and m-2j tends to infinity, then the Fourier coefficient A_(m,j) of F_m at k_j=(S^T)^j v obeys

    |k_j| |A_(m,j)| -> pi*sqrt(3/2)*|c_v| > 0.         (2)

The same holds at centered time -j. More strongly, for m>=12 define

    J_m={j in I_m : ceil(m/4)<=|j|<=floor(m/3)}.

Every C1 torus function f_m that agrees with F_m at every point of G_m satisfies

    ||partial_q f_m||_infinity^2 >= (101/625) |J_m|.    (3)

In particular the centered representative has unbounded C1 norm, and no choice of an exact smooth interpolation of these finite values repairs this. Since |J_m| is asymptotic to m/6, the lower bound grows like sqrt(m). Yet

    ||F_m||_infinity <= (sqrt(6)/2) ||gradient g||_infinity
                     <= 200 sqrt(6).                 (4)

Thus bounded local displacement responses coexist with a genuine loss of uniform C1 bounds on the two-dimensional label torus. Equation (3), rather than the single-coefficient observation (2) alone, establishes the unboundedness: a lone mode such as sin(Kx)/K would not suffice.

For B_m=C_m/(2*pi), divide F_m and the lower bound on its derivative norm by 2*pi.

## 2. Exact displacement and frequency formulas

Write

    S^r=[[a_r,2b_r],[b_r,a_r]],
    a_r=(lambda^r+lambda^(-r))/2,
    b_r=(lambda^r-lambda^(-r))/(2sqrt(2)), r>=0.

These a_r,b_r are integers, with a_r^2-2b_r^2=1. A convenient real lift is

    d_m=(b_m/(a_m-1), -1/2).

Direct multiplication gives (S^m-I)d_m=(0,1). For 0<=t<m,

    S^t d_m = 1/(1-lambda^(-m)) *
      ((lambda^(-t)+lambda^(t-m))/sqrt(2),
       (lambda^(t-m)-lambda^(-t))/2).                  (5)

For j>=0 the v-phase is therefore

    theta_(m,j)=v dot S^j d_m
      =(lambda^(-j)+lambda^(j-m))/(sqrt(2)(1-lambda^(-m)))
      =(b_(m-j)+b_j)/(a_m-1).                         (6)

The rational expression in (6) is used by the exact verifier. At centered time -j,

    v dot S^(-j)d_m - theta_(m,j) = 2b_j in Z.         (7)

Thus the positive and negative centered phases have identical exponentials.

The frequency is

    k_j=(a_j,2b_j),  k_(-j)=(a_j,-2b_j).

Its normalized norm tends to sqrt(3)/2. Equation (6) gives

    lambda^j theta_(m,j)
       =(1+lambda^(2j-m))/(sqrt(2)(1-lambda^(-m))).     (8)

For j->infinity and m-2j->infinity this tends to 1/sqrt(2). Since theta tends to zero and |e(theta)-1|/(2*pi*theta) tends to one, (2) follows. More generally, when m-2j is a fixed positive integer r, the limit in (2) is multiplied by 1+lambda^(-r); it still does not decay. Uniformity over the interior window in (3) is immediate from (8).

## 3. Actual support collisions and finite-group aliasing

### Ordinary integer frequencies

The maintained symbol has |l|<=1. For every nonzero integer r,

    |second coordinate of (S^T)^r(1,0)|=2b_|r|>=4.

Hence the oriented integer orbit of v meets the actual support only at v itself. The mode -v lies on a separate oriented orbit. Consequently the coefficient at k_j in (1) is exactly

    A_(m,j)=c_v [e(theta_(m,|j|))-1].                  (9)

No ordinary support collision can cancel it.

### Finite-group characters

This separate check is necessary: passing to G_m aliases frequencies modulo the annihilator. The previously established grid is

    G_m=(1/u_m Z/Z) x (1/v_m Z/Z),
    L_m=u_m Z x v_m Z,

where u_m=v_m=2x_m at odd m and u_m=2y_m, v_m=4y_m at even m, using the project Pell notation C^m=[[x_m,2y_m],[y_m,x_m]]. In all cases u_m divides v_m, and u_m>=478 when m>=7.

The integer quadratic form

    Q(k,l)=l^2-2k^2

is invariant under S^T. If an actual support vector w is congruent to some (S^T)^r v modulo L_m, then Q(w)=-2 mod u_m. The actual 32-mode support has -162<=Q(w)<=1, so |Q(w)+2|<=160. For m>=7, the congruence forces Q(w)=-2 exactly. Among the actual support only w=+v and w=-v have this invariant.

The orbit of v modulo L_m has exact period m. To see this, its period h divides m. If h<m, then h<=m/2, but its second coordinate 2b_h is strictly between 0 and v_m:

- if m is even, 2b_h<=2b_(m/2)=v_m/2;
- if m is odd, 2b_h<=[lambda^(m/2)-lambda^(-m/2)]/sqrt(2)<v_m.

It cannot be zero modulo v_m, contradiction.

The -v orbit is distinct. Otherwise (S^T)^r v=-v mod L_m would imply m divides 2r. With 0<=r<m, the only possible nonzero case is even m and r=m/2; again the second coordinate is v_m/2, not zero. The r=0 case is excluded by u_m>2.

Therefore the 2m signed orbit characters are all distinct, and no other actual support orbit aliases to them, for every m>=7. In particular (9) is also the EXACT finite-group Fourier coefficient at these characters. Centered times near either endpoint alias to the corresponding negative or positive times exactly as expected; this does not merge the distinct interior characters or alter their coefficients.

## 4. Finite difference proof of the interpolation-independent C1 obstruction

Let bracket denote the normalized uniform average on G_m. Define the finite-grid q-difference operator

    D_q F(z)=u_m [F(z+(1/u_m,0))-F(z)].

Its character multiplier at (k,l) is u_m[e(k/u_m)-1]. Finite-group Parseval and the isolated characters from Section 3 therefore give an exact lower bound using only j in J_m and the two signs ±v.

For each j in that window, with r=|j|,

    0<theta_(m,r)<1/2,
    0<a_r/u_m<1/2,
    a_r theta_(m,r)>=1/(2sqrt(2)).                    (10)

Here a_r>=lambda^r/2 and (6) gives theta>=lambda^(-r)/sqrt(2). For the first upper bound use r>=1, m>2r, lambda>5, and sqrt(2)>1. For the second, u_m>=lambda^(m/2)/2, a_r<=lambda^r, and m>=12 give

    a_r/u_m<=2lambda^(-m/6)<=2/25<1/2.

For 0<=t<=1/2, |e(t)-1|=2sin(pi t)>=4t. Consequently each one of the signed modes at a given j contributes at least

    |u_m[e(a_r/u_m)-1]|^2 |c_v[e(theta_(m,r))-1]|^2
      >= 256 |c_v|^2 (a_r theta_(m,r))^2
      >= 32 |c_v|^2.

There are two signs for each j, all distinct characters. Thus

    <|D_q F_m|^2> >=64|c_v|^2 |J_m|
                    =(101/625)|J_m|.                (11)

Now let f_m be ANY C1 periodic function agreeing with these values on G_m. Along each horizontal grid segment, the fundamental theorem of calculus gives

    |D_q F_m(z)|
      =|u_m integral_0^(1/u_m) partial_q f_m(z+t e_q) dt|
      <=||partial_q f_m||_infinity.

Averaging and using (11) proves (3). This argument uses only the sampled finite-group response, so the obstruction is not an artifact of choosing an uncentered Fourier extension.

Since |J_m|=2[floor(m/3)-ceil(m/4)+1]>=m/6-2, the right side diverges. The use of interior modes, far from both centered endpoints and far below the grid frequency scale, is explicit.

## 5. Uniform C0 control is compatible with the obstruction

In (5), the two eigendirection vectors each have Euclidean norm sqrt(3)/2. Summing their geometric majorants gives

    sum_(t=0)^(m-1) |S^t d_m|
      <=(sqrt(3)/2) (1+lambda^(-1))/(1-lambda^(-1))
      =sqrt(6)/2.

For negative centered times use the congruent displacement with t=j mod m; they differ by an integer vector. Periodicity of g and its Lipschitz bound prove (4), also for arbitrary torus x in the centered representative. The maintained model supplies ||gradient g||<=400.

This is consistent with a response localized in the orbit index. Differentiating with respect to the two-dimensional starting label introduces hyperbolically growing frequencies, and linearly many interior modes retain nonzero derivative size. A locality estimate in orbit-code coordinates does not assert a uniform C1 bound in these label coordinates.

## 6. Scope, attribution, and reproducibility

The parent action-response package and the canonical repository are preserved unchanged. New files are only in this `homoclinic` continuation directory.

This uses the actual symbol and derivative bound from `mathematics/fixed_map_path_model.md`, the exact periodic grids from `mathematics/frozen_periodic_point_annihilator.md`, and elementary Pell/invariant methods already present in the sparse-orbit and Pell routes. The specialized collision proof above is explicitly separated from those broader existing results. No external novelty claim is made.

The verifier checks every m=7,...,96, all 32 actual support modes at all m times, exact isolation of all 2m signed e1 characters, the rational phase formulas, negative centered-time agreement, and every interior lower-bound ingredient. It uses only Python integers and fractions. It also records exact rational enclosures illustrating the squared algebraic core tending to 3/8; no trigonometric floating evaluation enters a decision. The separate proof supplies the all-m conclusion.

Run from the parent action-response directory:

    PYTHONDONTWRITEBYTECODE=1 python homoclinic/run_recorded.py
    python validate_manifest.py homoclinic/manifest.json --root /workspace/shared

No actual fixed-tau estimate follows from the first action response, and no conclusion about the complete signed paired sum, Heisenberg comparison, or BGS is asserted. The applicable fixed coupling remains tau=10^-80.
