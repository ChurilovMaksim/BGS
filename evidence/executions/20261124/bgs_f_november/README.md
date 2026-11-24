# Replay and scoped review of the November BGS-F packet

- Upstream baseline: e2757e4cc5ef996e08190f88c93c710377c10c22.
- User-supplied BGS-F cumulative ZIP SHA-256:
  d3ec9a6ebf166066b59643dbab86dcc4fd8d6d7630b69733818c42f3c4d8e464.
- The original packet's manifest checked all 307 listed paths; the default
  runner passed its 35 checks. The smaller vendored replay carries a new
  manifest because it omits duplicated PDFs, large regenerated matrices,
  upstream copies and working snapshots.
- The finite h209 trace had an independent binary64 check, with center
  approximately 1.828193907886074e-5 + 1.023190158698741e-6 i in the chosen
  scalar normalization. All four regenerated exact input matrices were
  compared byte for byte to the supplied originals. The default rational
  verification reads recorded diagonals; this is not a fresh exact matrix
  powering run. Use the explicit slow replay for that test.
- Analytical scope was checked separately from numerical and exact finite
  evidence. The fixed-strength central claims remain open. Results marked
  verification-pending are not counted as established project theorems.
  No new Lean theorem or external referee report is asserted.

See the [maintained notes](../../../../mathematics/fixed-map/archive_continuation/README.md)
and [replay guide](../../../../computations/verification/bgs_f_november/README.md).

The vendored default runner also passed all 35 checks (79.9 seconds), with
thread counts set to one. The execution log's SHA-256 was
44a68fc03dc6507da4a6d69d03dc3312a6d233be9b1559246ec865ea3733ab21.
The log is available in the work record, not a theorem statement.

The canonical manuscript built in three pdfLaTeX passes: 382 pages;
no overfull boxes, unresolved references, or duplicate destinations.
PDF SHA-256: af416f17b8d437a4450df27b035a137aec6ee4b1c89367e6cb19b72bf6568ce8. The new section was visually checked
on pages 270–271. This verifies the publication build, not the mathematics.

The separate slow exact Pell reproduction also finished. The regenerated
four input matrices and all four output diagonal files match the packet
byte for byte. The replay then passed the rational inequalities from the
regenerated diagonals. Log SHA-256:
c37da9335e15856d7885c8c449dc579abc8977c96c0fa38e27cd86b794a83a83.
This closes the computational reproduction, not the pending analytic scope
review or any asymptotic question.
