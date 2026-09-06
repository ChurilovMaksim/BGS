# Transversality of the inverse translated resultant

Status: exact initial-form identity and squarefree inverse application, with the multiple-input-root gap repaired. These identities concern local resultant multiplicities, not bounds on large split prime divisors.

The former proof applied a formula requiring a root simple in each of E and O. Squarefreeness of F(X)=E(X^2)+X O(X^2) only implies that E and O cannot both have a multiple root at the same nonzero y; either input separately may have a multiple root. The derivative-free argument below closes that gap.

## 1. A universal initial resultant identity

Let f=GA and g=GB have degrees n,m. Let G be monic of degree d. For degree-preserving perturbations f_t=f+t phi, g_t=g+t psi, put D=A psi-B phi. With Res(f,g)=lc(f)^deg(g) product g(alpha), including root multiplicities, one has

    Res(f_t,g_t)
      =(-1)^(d(n-d)) Res(A,B) Res(G,D) t^d+O(t^(d+1)).        (1)

No squarefreeness is needed for this coefficient identity. If G=gcd(f,g), the resultant has order exactly d whenever Res(G,D)!=0.

Proof. On the generic characteristic-zero locus where G is squarefree and coprime to A, each root y of G contributes

    t D(y)/A(y)+O(t^2).

The other roots contribute Res(A,G)Res(A,B), and monicity of G gives Res(A,G)=(-1)^(d(n-d)) product A(y). Multiplication proves (1) and vanishing of every lower coefficient. Both sides are polynomial expressions over the integers in all the coefficients, with G monic. The generic identity is therefore universal and survives specialization, including multiple roots and arbitrary characteristic. In particular no division by f'(y) is present in (1).

For a unique common root y and G=Y-y this recovers

    d/dt Res(f_t,g_t)|_0
      =(-1)^(n-1) Res(A,B) [f'(y)psi(y)-g'(y)phi(y)],

provided gcd(f,g)=Y-y. The formula still applies when one of the two derivatives vanishes; it is not necessary that both inputs be simple at y.

## 2. The inverse translation direction

Write

    F(X)=E(X^2)+X O(X^2),
    F(X+t/2)=E_t(X^2)+X O_t(X^2).

The first variations are

    phi(Y)=(O(Y)+2Y O'(Y))/2,
    psi(Y)=E'(Y).

Assume the characteristic is not two, F is squarefree, and F(0)!=0. Let G=gcd(E,O) be monic, E=GA, O=GB. The polynomial G is squarefree: a repeated factor of G would induce repeated factors of F. Every root y of G is nonzero. At such a root,

    E'(y)=G'(y)A(y), O'(y)=G'(y)B(y),
    D(y)=G'(y)[A(y)^2-y B(y)^2].

Choosing z with z^2=y gives

    F'(z)F'(-z)=-4y G'(y)^2 [A(y)^2-y B(y)^2].

All factors needed for D(y)!=0 are nonzero. Thus Res(G,D)!=0. Formula (1) proves

    ord_(t=0) Res(E_t,O_t)=deg gcd(E,O).                    (2)

This proof includes roots that are multiple in E alone or in O alone. If the gcd degree is one, the constant coefficient vanishes but the linear coefficient does not. If it is at least two, both vanish. Hence

    deg gcd(E,O)>=2 iff rho(0)=rho'(0)=0,
    rho(t)=Res(E_t,O_t).

As in the maintained row construction, all resultants are interpreted with their fixed ambient degrees. In the inverse translation application E has fixed degree and leading coefficient; the degree of O can drop on a special fibre without altering the relevant leading coefficient formula. When this occurs the Sylvester fixed-degree convention is retained rather than silently switching conventions.

## 3. The simple-gcd formula and its scope

For G=Y-y, formula (1) becomes

    rho'(0)=(-1)^(deg(E)-1)
       Res(E/(Y-y),O/(Y-y))*[E'(y)^2-y O'(y)^2].

The identity

    E'(y)^2-y O'(y)^2=-F'(z)F'(-z)/(4y)

makes its nonvanishing transparent. The reduced resultant is nonzero because the gcd has degree exactly one. The first principal subresultant and rho'(0) therefore differ by a nonzero residue-field multiplier on the maintained fixed-degree squarefree locus. This identifies their prime support, not their integral valuations.

For a squarefree higher-degree G, one may alternatively express the leading coefficient through the product of local Jacobians and the discriminant of G, up to the fixed sign. Formula (1) is preferable because it avoids derivative denominators and continues to make sense on multiple-root strata.

## 4. Exact negative and positive controls

The former fixed-f shift claim had omitted a necessary hypothesis:

    f=X^2, g=X(X-1), G=X, psi=1
    gives Res(f,g+t)=t^2, not order one.

For inverse translation take

    E=(Y-1)^2, O=Y-1,
    F=(X^2-1)(X^2+X-1).

Over Q, F is squarefree with F(0)=1, but E'(1)=0. The translated resultant has linear coefficient one. This is a positive control for the repaired argument and was not covered by the former simple-in-both proof.

The existing cyclotomic controls remain:

    K=11,p=23,tau=14: gcd degree zero;
    K=11,p=23,tau=10: gcd degree one;
    K=23,p=47,tau=10: gcd degree two.

The former K=7,p=29 positive anchor remains retracted: every real embedding there has degree zero.

## 5. Arithmetic boundary

The maintained split trace cofactor is squarefree and nonzero at the reflection centre, so the two-scalar inverse prime-support criterion survives these corrections. Neither (1) nor (2) bounds the largest supported rational prime. A local transversality identity is not a growing-parameter common-divisor theorem, and it is not microscopic spectral universality.
