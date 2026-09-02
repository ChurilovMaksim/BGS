# Results

This directory is the **status-controlled result layer**.  The broader raw/historical research-output corpus remains under `data/`; see `data/MANIFEST.md`.

- `verified/` — outputs rerun or independently checked as part of the canonical computational checks;
- `numerical/` — current useful numerical evidence with explicit provenance;
- `historical-numerical/` — selected finite-N measurements whose statistic, interpretation, or surrounding proof claim was superseded/quarantined.

The old `N=95419` result is deliberately under `historical-numerical/`: its producer computed consecutive-gap ratios and then compared the KS statistic with the ordinary Wigner spacing CDF.  The raw measurement is preserved, but that named GOE spacing test is invalid.

`bgs_spacing_goe.json` is mixed-provenance numerical evidence: the `N=3571` row was freshly reproduced during the 2026-09-03 bounded audit, while the heavier `N=19489` row is retained from the previous run and marked as such.  `number_variance_goe_control.json` was freshly rerun during the audit.

Additional moment scans, diagnostics, spectral experiments, rank-2/Sp4 calculations, and old proof-oriented JSON live under `data/{diagnostics,moments,proof,rank2_sp4,spectral,legacy}` rather than being discarded.

A JSON filename, historical directory called `proof`, or an old `PASS` field does not confer theorem status.  Root `STATUS.md` is authoritative.
