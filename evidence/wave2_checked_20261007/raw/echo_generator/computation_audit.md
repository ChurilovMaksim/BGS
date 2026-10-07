# Exact computation contract and actual execution record

## Arithmetic and covered assertions

`python check_exact_controls.py` and `python -O check_exact_controls.py` run
explicit exception-based checks, with no Python assert statements. The output
JSONs are compared byte for byte after both finish. No stochastic input,
floating tolerance, numerical matrix exponential, or auxiliary-time sample is
used. A pass certifies only the finite assertions listed below.

1. The literal physical symbol is built as a Laurent polynomial over Q(i),
   including r(q+1/2). Its 32 nonzero Fourier coefficients are recorded.
2. For each N in {3,5,7,9}, arithmetic is exactly Q[z]/Phi_(4N)(z), with
   the explicitly declared embedding i=z^N. Matrices A_N are constructed
   independently from the Fourier/Weyl expansion and the midpoint Jacobi
   formula and compared exactly.
3. Seven fixed ordinary-integer labels at each N include negative and
   multiply wrapped labels. Each has nine alias-shift checks, for 63/N;
   all 49 ordered products are checked; all seven generator and cat
   conjugation identities are checked. No high-N coverage is implied.
4. Cat unitarity is checked using the unnormalized chirp M0 M0*=N I,
   avoiding unnecessary square-root embeddings. A_N Hermiticity and the
   scalar N=7 exception are reported. Controls explicitly reject omission
   of a wrap sign and, in nonscalar fixtures, reversal of the sine sign.
5. The independent dense rational N=3 reflection fixture checks the
   superoperator trace, finite b-twirl and charge-energy form for m=1,...,8
   at three exact occupation-phase choices: 24 equalities in total.
6. Actual N=3 U(t)=exp(i t N A_N)M_N is maintained as a formal real-time
   Taylor jet through degree two. Rooted path enumeration retaining every
   occupation vector independently agrees with the superoperator jet for
   m=1,...,6. This includes 3,9,23,39,57,78 nonzero (charge,occupation)
   keys respectively. The occupation integral is a coefficient-norm sum;
   no independent phases are substituted into the actual target U_N.
7. The changed period-six family at p=5,N=25 is constructed cyclotomically
   and checked for unitarity, U^6=I, U^5=U*, and E_25,6(0)=25 exactly.

## Literal-time finite sign certificates

The symbol coefficients give the exact bound

    ||A_N|| <=sum_v (|Re c_v|+|Im c_v|)=593/500

for every N, with aliases allowed. For real t,
||U_N(t)-U_N(0)||<=|t| N(593/500), and hence
||T_N(t)-T_N(0)||, ||D_N(t)-D_N(0)||<=2|t|N(593/500).
The occupation twists do not alter these bounds. Telescoping the m-factor
one-pinch trace and using |Tr_H X|<=N^2||X|| gives

    |E_N,m(theta;t)-E_N,m(theta;0)|
       <=2m N^3(593/500)|t|.

For the signed occupation subtraction the corresponding bound is twice this.
The exact N=3 zeroth-order controls give

    E_3,3(0;0)-integral E_3,3(theta;0)dtheta=-4/9,
    E_3,4(0;0)-integral E_3,4(theta;0)dtheta=44/27.

At literal t=10^-80 the absolute errors are respectively bounded by
(48033/125)*10^-80 and (64044/125)*10^-80. Thus the actual literal N=3
one-pinch signed source is strictly negative at m=3 and strictly positive
at m=4. These are rigorous bounded actual-model controls, not asymptotic
counterexamples, and not an inference from a different nonzero coupling.
No displayed first/second derivative is used without its remainder bound.

## Failed development checks retained

Three early failed logs are retained rather than overwritten:

- `failed_run_01_embedding.log`: SymPy's implicit algebraic-field embedding
  of i was conjugate to the declared i=z^N at N=5 and N=7. The independent
  midpoint check detected the mismatch. The final code explicitly embeds
  every Gaussian rational as Re(c)+Im(c)z^N and forbids floating symbol
  coefficients. This was an implementation-convention error.
- `failed_run_02_field_inverse.log`: Python int/ANP division was unsupported.
  It was replaced by field-one/root. This was an execution error.
- `failed_run_03_m1_expectation.log`: a proposed m=1 zero control was false.
  The endpoint marked-switch derivative vanishes at m=1, but the one-pinch
  occupation source need not: it is |tr U|^2-sum_j |U_jj|^2. The control was
  corrected to that exact identity. No theorem in the deliverable assumes
  the false zero statement. This distinction is worth retaining.

## Source closure and limits

The JSON records exact SHA256 pins for the read-only input files before and
after each successful run. The checked 3930-file parent snapshot manifest is
recorded as the base supplied by the parent; this bounded control does not
re-run the complete snapshot validator or claim to audit all of its files.
The final local manifest pins source code, proofs, results and logs.

The analytic band theorem and the infinite-family counterexample are proved
in their mathematical notes from explicit inputs. The finite computations
check conventions, low-N identities and implementation. They do not establish
compactness, the Abel inequality, Heisenberg asymptotics, generic T16, or BGS.
