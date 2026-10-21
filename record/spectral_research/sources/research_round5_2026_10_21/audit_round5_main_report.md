> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round5_2026_10_21/audit_round5_main_report.md`. Embedded SHA256: `eb1cb385cdcfca1e378de8420ea23656ee9560bf2d12f806539c65cf98910d2d`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Final validation of the Round 5 main report

Date: 21 October 2026. Auditor: /root/audit_uniform_word_r4.

Reviewed file: round5_main_report.md.

Exact reviewed SHA256:
8a4629d270c1b70e2478ce98cc2ed66b8e4a6c836cc27c35fbaf1555587420c2.

The hash was recomputed before and after validation and was unchanged.
The reviewed file contains 65,540 UTF-8 bytes and 1,302 lines.
It was not modified by this auditor.

## Scope and verdict

This is the final byte-level and formula-consistency review requested
after the earlier draft comments. Sections 4--6 were reread against
their independently audited frozen proof sources. The repaired
formulas (9.1)--(9.2), the scalar cutoff notation, and the report's
statements of the remaining spectral obligation were also checked.
This review does not claim to replace the separate full audits of
every primary proof or of the eventual cumulative document.

The requested edits are present and correct. No unresolved
mathematical correction was found within this review's scope.

## Verified corrections

1. The exact positive endpoint contraction in Section 4.4 is now
   labelled $\mathcal H^=_{n,N}$, the marked functional. Its
   length sum explicitly includes $\ell_i\ge L$. The subsequent
   passage to the unmarked $\mathcal T^=$ explicitly states its
   superpolynomial exceptional-set error.

2. Section 4.4 now specifies
   $K=\lceil4\log_2N\rceil$, $L=2K+2$, with fixed maximal
   order $M\ge r$. This gives
   $\delta\le(C-1)N^{-8}=o(1/N)$ and superpolynomial
   irregular and reversed losses at each fixed $M$.
   The displayed $O(N\log N)$ three-arc error and the
   aggregate cycle-count formula (4.10) are consequently
   justified by the frozen general theorem.

3. The square-root-order scalar cutoff is consistently denoted
   $m_N=\lfloor\sqrt N/10\rfloor$ in (4.7) and the definition
   of the growing class. The original matrix $M_N$ is no
   longer reused for that scalar.

4. The report keeps the logarithmic-cutoff positive formulas
   separate from the square-root-cutoff error
   $O(N^{c(\pi)}L_N)$. It does not silently merge the two
   different pair classes. The positive endpoint classification
   remains restricted to the distinct-start subclass; the
   broader literal-mismatch signed theorem is stated separately.

5. Section 6.2 now defines $\mathcal N_x(q)$ explicitly as a
   count of coherent partners with $L(y)=L(x)$, in addition
   to the trigram-distance condition. The factorial pairing
   bound applies to precisely this class.

6. Section 6.3 now states the strict necessary inequality
   $r>\lfloor\delta_0N\rfloor/2$. Its fixed-length consequence
   $L_*>2B/\delta_0$ is valid for all sufficiently large
   $N$: the strict fixed linear margin absorbs the rounding.

7. Formulas (9.1) and (9.2) contain valid
   $\frac1{N^2}$ commands. They preserve the exact pair
   functional and the proved $O(N^{-2})$ correction.
   The report still identifies (9.3), with its strictly negative
   integral target, as unproved. It does not claim that the
   remaining signed class should simply tend to zero.

## Byte and delimiter checks

The current file has:

- no ASCII control bytes other than line feed;
- no DEL bytes;
- 346 balanced pairs of inline math delimiters;
- 83 balanced pairs of display math delimiters;
- no unmatched braces or mismatched begin/end environments
  in the 429 extracted math blocks.

In particular the two carriage-return corruptions of the
distinct-start annotations are gone: the formulas now use
the valid command $\mathrm{distinct}$. The two previously
reported form-feed corruptions in the fraction commands are
also gone. Delimiter checks supplement the manual formula
review; they are not presented as mathematical proof.

## Qualifications for the cumulative document

The reviewed hash belongs only to the main report above.
Appending primary sources, audits and older books creates
a different artifact, whose final bytes and hash require
their own assembly validation.

If typography is repaired only in embedded copies of older
frozen books, the original files must remain unchanged and
the cumulative document should identify the exact original
and rendered-copy hashes together with the replacements.
That operation is separate from this review; this audit
does not purport to certify an embedded copy not yet examined.

The report's substantive scope is accurate: exact signed
cancellation is proved for specific original-family
unmarked classes, while exponential positive coherent mass
is proved outside the long-arc coverage. Neither result
estimates the full signed complement at the required
spectral precision. The original $H_{\rm diag}$ and
CUE/Sine_2 conclusions remain explicitly unresolved.
