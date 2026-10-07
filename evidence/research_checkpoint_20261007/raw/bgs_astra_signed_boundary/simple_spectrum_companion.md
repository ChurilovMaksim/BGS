# Simple-spectrum version of the growing coherent-return witness

Short companion candidate, 7 October 2026. This changes the quantizer, as does its source growing_period_counterexample.md. It makes no claim about the maintained actual map.

Let V_N be the N=p^2 growing-period witness. Choose an orthonormal eigenbasis v_1,...,v_N, with eigenvalues omega_j satisfying omega_j^(2p)=1. Define

    W_N v_j=omega_j exp(i j/N^4) v_j.

Then ||W_N-V_N||<=N^-3. Every ratio of two distinct W_N eigenvalues is a root of unity times exp(i(j-k)/N^4), with nonzero rational (j-k)/N^4. Such a ratio cannot be a root of unity: otherwise a nonzero rational would be a nonzero rational multiple of 2pi, contradicting irrationality of pi. Thus W_N has simple spectrum, and no positive power of W_N is scalar. This is an exact exclusion, not a numerical separation estimate.

Put epsilon=N^-3. The adjoint transfers differ by at most 2epsilon in HS-induced operator norm. Their zero-charge compressions and their full charge pinchings differ by at most 2epsilon as well. Consequently

    ||P_(W_N)-J_N||<=2N^-3,
    sup_(c!=0)||B_(W_N,c)|| <=sup_(c!=0)||B_(V_N,c)||+2N^-3 ->0.

The entries obey |W_(jk)|<=N^-1/2+epsilon. Since ||W-V||_HS<=sqrt(N)epsilon, the Hadamard-product decomposition of the reverse kernels gives

    ||Q_W-Q_V||op <=||Q_W-Q_V||HS
       <=2epsilon+sqrt(N)epsilon^2.

Hence ||Q_W||<=N^-1/2+2N^-3+N^-11/2 ->0. Entrywise flatness survives with a fixed constant.

For m<=bN, telescoping gives

    |Tr W_N^m-Tr V_N^m|<=mN epsilon<=b/N.

At every m divisible by 2p in the fixed band, |Tr W_N^m|>=N-b/N. The compact weighted return lower bound remains (sqrt(N)/2)integral w+O_w(1), with only o(1) additional error. The supplied universal phase-Abel estimate bounds the balanced aggregate for W_N by O_w(1) without any transfer argument. The low-Hamming bound now has t_N<=2N^-3, so its exponent m-2floor(.49m)>=.02m makes it superexponentially small relative to ordinary exp(-cN); the low-switch bound still applies because the charge gap tends to one. Therefore the same literal residual diverges as in P5 of the growing-period source.

Also every fixed normalized trace tends to zero, with the same uniform estimate up to an O(N^-5/2) correction for 1<=m<2sqrt(N). This companion removes exact finite order and spectral multiplicities as essential features of the coarse-data obstruction. It does not preserve the actual raw symbol, algebraic-commutant exclusions, exact kick/cat factors, or their complete literal quantization.
