# Why nonzero endpoint weights alone cannot settle the residue boundary

This is an obstruction to a proposed simplification, not to the actual matrix pair. The actual endpoint product must be retained.

Fix the first-seven right-row matrix V(q) from the actual low-depth gauge, over an algebraically closed field of characteristic different from2 and7, wherever V is invertible. Let f_b(j)=w^(bj). Write a freely chosen endpoint inverse gauge as R=diag(R_j), and put U_s=R f_(4+2s), s=0,...,6. The seven U_s form a basis when every R_j is nonzero.

Let c=V^(-1)e_0. For generic q every coordinate of c is nonzero: at q=0, V has Fourier rows f_(2t+3)^T, so c=(1/7)f_4 has no zero coordinate. Set R_j=c_j/f_4(j). Then U_0=c and VU_0=e_0.

The nontrivial rank-one projector C_0=c v_0^T (v_0 the first row of V) is diagonal in the V-eigenbasis, with eigenvalues1,0,...,0, and maps every U_s into span(U_0). Consequently it is upper triangular in the U basis and satisfies every necessary leading-compatibility equation. It is not scalar.

In fact it extends to a solution of all seven last-row boundary equations with suitable C_1,...,C_6. Write E_s=gamma_s U_s v_s^T with nonzero gamma_s. Since C_0U_s−lambda_s U_s lies in span(U_0,...,U_(s−1)), write its coefficients as a_(t,s). The boundary equation is equivalent to

v_t^T C_d=(gamma_(t+d)/gamma_t) a_(t,t+d) v_(t+d)^T,
0<=t<=6−d.

For each fixed d these impose the values of C_d on only7−d independent left rows of V, so they can be extended linearly to some C_d. Different d impose conditions on different unknown matrices and do not conflict.

Thus a symbolic leading-boundary argument valid for *arbitrary* nonzero endpoint factors is false, even with all low-depth Casoratians invertible. A single product/determinant normalization of R does not rescue it: common rescaling of R leaves the flag and C_0 unchanged, and can enforce such a normalization over the algebraic closure.

For the actual model, R_j is the specific long q-Pochhammer product, so this example does not refute scalarity. It explains why the bounded low-depth system must use an additional identity or nonvanishing property of that product. Characteristic-zero positive-weight domination supplies one; no characteristic-five counterpart has yet been proved in this work.
