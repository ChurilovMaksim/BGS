# Off-charge upgrade of microscopic spectral rounding

Short candidate consequence of prior rounding and the new independently reviewed universal phase-Abel bound. The operator is CHANGED, never identified with the literal fixed quantizer. No new rounding mechanism is claimed.

Let U_N be the actual fixed family and let w>=0 be nonzero, smooth, supported in a fixed positive compact band [a,b]. The universal Abel input gives, for every unitary W,

    N^-2 sum_m w(m/N) B_m(W)<=C_w,
    C_w=||w||infinity e^(2b) (1/2+1/6) for N>=3,

by taking s=1. The constant is independent of W and N.

Choose a fixed integer L large enough that sum_(r>=1)w(r/L)>C_w+1; this is possible because the sum divided by L tends to integral w>0. Put K_N=floor(N/L), and spectrally round each eigenphase of U_N to the nearest K_N-th root of unity, obtaining Uhat_N. Then

    ||Uhat_N-U_N||<=pi/K_N=O_L(N^-1),
    Uhat_N^(K_N)=I.

Consequently

    liminf N^-2 sum_m w(m/N)|Tr Uhat_N^m|^2
       >=sum_(r>=1)w(r/L)>C_w+1,

and subtracting the universal balanced bound proves liminf of the exact off-charge aggregate is at least 1. This supplies the off-charge conclusion absent from the earlier full-CUE rounding obstruction.

The following inherited coarse structures survive:
- P_N and all charge compressions change by O_L(N^-1), because they are compressions/pinching of the adjoint transfer.
- Reverse kernels change by O_L(N^-1), using actual entrywise O(N^-1/2) flatness and the HS Hadamard estimate from the simple-spectrum companion; entrywise flatness survives.
- The collective compact limit of D_N is unchanged. Every uniform Schatten S_p bound on D_N with p>2 is preserved, because the perturbation has S_p norm at most O_L(N^(2/p-1)).
- If Q_N=U_N M_N* is the literal kick, define Qhat_N=Uhat_N M_N*. Every fixed word in (Qhat_N,M_N) differs from the corresponding word in (Q_N,M_N) by O_word,L(N^-1); therefore the new actual fixed-word normalized freeness limits are also preserved.

These conclusions do not preserve the exact kick identity Q_N=exp(i tau N A_N), its finite-support raw-Weyl generator, or all-order uniform smooth-symbol data. No claim about those invariants is made.

Actual P has eventual gap t_N<=10^-63; after the O_L(N^-1) perturbation choose a slightly larger fixed eventual bound, such as 2*10^-63, which still satisfies the .49 Hamming entropy inequality. The one-step nonzero-charge gap stays below some fixed rho'<1. Thus the same generic low-Hamming and growing low-switch removals remain exponentially negligible (with a possibly smaller fixed switch-cutoff constant). The remaining literal high-Hamming/high-switch off-charge residual is therefore bounded away from zero for Uhat_N. Its damped endpoint is negligible by the corresponding all-switch gap theorem, and the signed boundary estimate fails for this changed family.

This is a rigorous discriminator: even actual principal classical dynamics, fixed-word limits, compact charge pinching, the three coarse gaps, and any proposed p>2 Schatten bound cannot alone distinguish the desired endpoint. Any successful use of a finite-loop reduction must estimate the surviving microscopic long-link loops with genuinely exact quantization information.
