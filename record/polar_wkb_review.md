# Review scope: principal WKB polar comparison

Date: 6 October 2026. Curated from the independent internal review of the
source research proof. This is not external referee certification. The
[provenance mapping](../evidence/polar_wkb_provenance.json) records the original
review and proof hashes and the publication-path transformations. No
mathematical assertion is strengthened during curation.

## Verdict and scope

**Proved as written**, at the fixed coupling tau=10^-80 and for sufficiently
large odd N, subject to the already stated smooth no-caustic WKB construction.
The original smooth polar bridge has the correct sign and normalization.
The proposed additional transport and second-order composition also prove

    ||W0_N* W0_N-I||op = O(h^2),
    ||polar(W0_N)-W0_N||op = O(h^2),                 h=1/N.

They sharpen the bridge to

    polar(W0_N)=exp(-i h Op_N(Im c1)) U_N+O_op(h^2).

This review independently derives the WKB/polar portions of
[the maintained proof](../mathematics/polar_wkb_quantization_stability.md),
sections 3–5 (source sections 3–4A). It does
not independently audit that note's marked factorial transport, logarithmic
mixing input, external source leaves, or resulting spectral-statistics
transfer. In particular these conclusions do not establish BGS statistics.

## Source and dependency checks

Canonical inputs inspected:

- `mathematics/four_branch_parametrix.md`, especially its exact initial
  Gauss identity, sections 2 and 4, and global characteristic paragraph.
  SHA256: `c696ebd39a52ca83205800a41fc30a9d570ebd3ed5dc96069f212948275600d7`.
- `mathematics/fixed_map_path_model.md`, exact ordinary Weyl action and
  odd-N convention. SHA256:
  `d5365063f0967dabcac741a93c6f411d6402c913074944e1f9e383b2b5149b08`.

Dependency chain: exact finite-shift action and initial Gauss identity ->
smooth glued transports -> explicit finite Taylor residual -> unitary
Duhamel -> direct smooth-symbol composition -> elementary polar functional
calculus. No continuous FIO theorem, Poisson summation, or oscillatory
operator-norm theorem is invoked in the new comparison.

## 1. Global symbol and positive leading amplitude: passed

Write the characteristic flow as (X(t,a,y),P(t,a,y)), initially
(a,(y+r-3a)/4). Its vector field (-g_p,g_x)/(2pi) has zero divergence.
Therefore det d(X,P)/d(a,y)=1/4. Solving X(t,a,y)=x gives exactly

    S_r,xy=(X_a P_y-X_y P_a)/X_a=1/(4 X_a)>0.

The canonical estimate X_a>=1-2*10^-8 supplies the positive denominator.
Along the same characteristics the leading amplitude is

    a_r,0=X_a^(-1/2)>0.

Thus ratios a_r,j/a_r,0 are smooth. The phase and amplitude gluing imply,
with p_r=S_r,x and c_r=a_r,j/a_r,0,

    (p_r,c_r)(x,y)=(p_0,c_0)(x,y+r),
    p_0(x,y+4)=p_0(x,y)+1,       c_0(x,y+4)=c_0(x,y),
    (p_0,c_0)(x+1,y)=(p_0,c_0)(x,y-3).

The positive twist and the y+4 identity make y -> p_0(x,y) a global
bijection. Its inverse Y defines c(x,p)=c_0(x,Y(x,p)), a smooth symbol
periodic with period one in both variables. The same reasoning applies to
a2 and to the composition amplitude below. All derivative bounds needed
are uniform in N, with constants allowed to depend on the fixed time.

## 2. Exact composition and Fourier aliases: passed

For every integer mode (k,l), including |k| or |l| above N, the actual
quantizer acts by

    W_N(l,k)u(x)=e(k(x+h l/2))u(x+h l).

Use the entire lattice-periodic four-branch sum before applying this
identity, and global branch extensions after the shift. This handles
wraparound exactly. For an individual branch put a=a0, p=S_x and

    delta(h)=[S(x+h l)-S(x)]/h-l p+h k l/2.

Bounded S_xx and a_x give a first-order factored error
C h (|l|+l^2+|kl|). The sqrt(h) kernel prefactor and
||R||op<=N max|R_jk| give

    Op_N(c1)W0=K1+O_op(h^(1/2)).

The coefficient sum is legitimate because every polynomially weighted
Fourier l1 norm of a fixed smooth torus symbol is finite. No frequency
cutoff, untracked alias, or periodicity of an individual branch is assumed.

For the stronger expansion, use

    delta'(h)=l^2 integral_0^1 s S_xx(x+s h l) ds+kl/2,
    delta''(h)=l^3 integral_0^1 s^2 S_xxx(x+s h l) ds.

Twice differentiating exp(2pi i delta(h)) a(x+h l) bounds its second
derivative by C(1+|k|+|l|)^4, uniformly for 0<=h<=1. Taylor's remainder
therefore remains summable over all integer modes, and proves

    Op_N(c1)W0=K1+h L1+O_op(h^(3/2)),

where the amplitude defining L1 is

    sum_{k,l} chat1_kl e(kx+l p)
        [l a0_x+pi i(l^2 S_xx+kl)a0].

The ratio ell of this amplitude to a0 has the exact amplitude gluing and
descends to a fixed smooth torus symbol. In local (x,y) notation it equals

    ell=c1_p (a0_x/a0)/(2pi i)
          -i(S_xx c1_pp+c1_xp)/(4pi),

where the c1 derivatives are evaluated at (x,S_x); a0_x is at fixed y.
The first-order composition estimate consequently gives

    L1=Op_N(ell)W0+O_op(h^(1/2)).

## 3. Explicit reality check for the first correction: passed

Direct expansion of the canonical finite-shift definition gives

    P2 a=-g_pp a_xx/(8pi^2)
          -(g_xpp+S_xx g_ppp)a_x/(8pi^2)
          -[S_xxx g_ppp/(24pi^2)
             +(g_xxpp+2 S_xx g_xppp+S_xx^2 g_pppp)/(32pi^2)]a.

All g derivatives are evaluated at (x,S_x). Thus P2 preserves real
amplitudes. Since D2=i P2, the real D1 transport with a1(0)=0 makes a1
purely imaginary. Therefore c1 is purely imaginary and the exact adjoint
identity Op_N(c)*=Op_N(conjugate c) gives

    C1*= -C1,                    C1=Op_N(c1).

This is an exact parity assertion, not an estimate inferred from
unitarity. The displayed P2 formula also checks every coefficient and sign.

## 4. Additional transport and strengthened defect: passed

Introduce a2 by

    (partial_t-D1)a2=D2 a1+D3 a0,     a2(0)=0.

This cancels through order h^2 in the factored evolution equation. Smooth
finite Taylor expansion leaves a factored residual O(h^3), hence an
entrywise residual O(h^(7/2)) and an operator residual O(h^(5/2)). Exact
initial data and unitary Duhamel prove

    U=W0+h K1+h^2 K2+O_op(h^(5/2)).

The transport source has the same gluing as the lower amplitudes. The
symbol c2=a2/a0 is therefore smooth on the torus, and

    K2=Op_N(c2)W0+O_op(h^(1/2)).

There is no circular norm estimate: the original two-amplitude result and
the crude bound ||K1||=O(h^-1/2) first give ||W0||=O(1). It follows that
K2 and L1 are both O_op(1). Combining the composition identities yields

    K1=[C1-h Op_N(ell)]W0+O_op(h^(3/2)),
    U=[I+h C1+h^2 D]W0+O_op(h^(5/2)),
    D=Op_N(c2)-Op_N(ell)=O_op(1).

Set F=I+h C1+h^2 D. Exact skew-adjointness of C1 implies
F*F=I+O_op(h^2). Thus, using bounded W0 and the last equation,

    W0*W0=W0*F*F W0+O_op(h^2)=I+O_op(h^2).

For sufficiently large odd N this matrix is positive definite. Functional
calculus near one gives (W0*W0)^(-1/2)=I+O_op(h^2), establishing the stated
O(h^2) polar correction. Also

    W0=exp(-h C1)U+O_op(h^2).

Since C1=i Op_N(Im c1), the improved bridge follows. Its exponential is the
ordinary exp, so there is no extra 2pi factor. The generator acts on the
left; no classical-map pullback of c1 is needed.

## Remaining boundaries

- All assertions concern the explicit principal matrix W0 and actual raw
  ordinary quantizer, not an arbitrary quantization of the same map.
- Only sufficiently large odd N is claimed for the unique unitary polar
  factor; no assertion is made about invertibility at every small N.
- Finite additional smooth transports suffice. All-order FIO calculus and
  a rate uniform as tau varies are neither assumed nor established.
- The P2 and composition identities are algebraic derivations. No finite
  numerical experiment is being presented as proof of an asymptotic limit.
- The original O(h^(3/2)) bridge is valid; section 5 strengthens its error
  to O(h^2). A spectral matching step justified separately then has maximum
  unfolded residual displacement O(h), rather than O(h^(1/2)), for the two
  unitary endpoints. No eigenvalue matching between the possibly nonnormal
  W0 and its unitary polar factor is asserted: an O(h^2) polar correction
  is a singular-value/unitarization statement, not a nonnormal spectral
  continuity theorem.
