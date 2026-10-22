# Hash-specific confirmation of the rotated-box revision

Date: 6 October 2026. Scope: review only the correction from the previously audited first version to the supplied second version. No author or canonical files were edited.

## Verdict

**Confirmed: every correction requested in `local_review/review.md` is addressed in the reviewed v2.** The prior verdict remains: the theorem is proved for the explicitly defined Gaussian-conditioned rotated-box integral under the stated actual-model local hypotheses. The revision does not change the claimed rate or extend the theorem to the original lattice trace.

## Verified bytes

- Corrected source: `rotated_local_first_loop_v2.md`
  - SHA-256: `fe41ac7dc34660f2adedb82f741903be482e2b8eaef35d84feba6341bfcc32f1`
- Recorded diff: `local_first_loop_v1_v2.diff`
  - SHA-256: `4a6fb1f8c851f673fc1b1880bc36e722db15a86fd852815de83f4adb29d8a5a3`
- Frozen original: `rotated_local_first_loop.md`
  - SHA-256: `7550e19989ba9efe41bf5f2b3daf5199a2952d6e144fb8e1b95f2fc0da4602b3`
- Prior review: `local_review/review.md`
  - SHA-256: `4abbf247e2e578b83d98b42e4d01e69702afe8b2e77d122c28f057a00cfd89e5`

All four entries in `local_first_loop_revision_hashes.json` were recomputed and match. A newly computed unified diff, using the recorded old/new filenames, agrees byte-for-byte with the recorded diff. The original and prior review remain unchanged.

## Item-by-item closure

1. **Sum of entrywise suprema: addressed.** Lines 78–86 explicitly impose the off-diagonal sum of suprema, explain the fixed local-degree factor, and permit a smaller radius. This supplies the precise bound used by the conditional-mode contraction and conditional variance estimate.
2. **Upper diagonal curvature: addressed.** Lines 81–86 give both lower and upper bounds, including the one-dimensional case. The marginal upper-curvature claim now has its required explicit input.
3. **Componentwise boundary flux: addressed.** Lines 216–220 use the infinity norm and explain that each face uses only one normal component. No dimension-free Euclidean norm is claimed.
4. **Signed outward flux: addressed.** Lines 190–197 display the negative flux term with the outward normal, full Gaussian density, and conditional normalization. It agrees with the reconstructed integration-by-parts identity.
5. **Complete tilt family: addressed.** Lines 67–70 include the pure linear/cubic exponent and the exponent with the constant mean substituted. Lines 146–149 explicitly restrict tilt strengths to the bounded range certified by the chosen radius and account for the constant mean in normalization. All exponential weights actually used are covered.
6. **Poincare locator: addressed.** Lines 128–130 place Theorem 3.1(1) on printed p. 13 and equation (3.2) on printed p. 14.
7. **Conditional normalization: addressed.** Lines 27–30 distinguish the authoritative conditional expectation from the full-Gaussian-normalized unconditioned box integral and state the Gaussian box-probability factor.

The revision also clarifies conditioning on all other coordinates, the range in which Minkowski is applied, the consequence for smaller positive moments, and the repeated neighbor at m=2. These are consistent with the prior proof reconstruction.

## Notation and boundary of confirmation

As in the surrounding displayed formulas, `sum_k c_jk` in (L5), line 100, denotes the off-diagonal neighbor sum; line 82 states that range explicitly and line 99 uses it explicitly. This is the only interpretation used in this confirmation. If that isolated abbreviation is expanded during ordinary copyediting, it should read `sum_(k!=j) c_jk` (or define c_jj=0). No analytic estimate depends on a bound for the diagonal within this off-diagonal sum.

This confirmation applies only to the exact hashes above. No numerical test is being substituted for the analytic argument. The original-trace contour deformation, side-contour/gluing control, all-order exponential remainder, and entropy-compatible signed saddle summation remain outside the confirmed theorem.
