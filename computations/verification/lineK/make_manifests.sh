#!/bin/bash
cd /workspace/bgs-lineK
find REPORT_v2.md NOTES.md code logs lean -type f ! -name '*.olean' ! -name '*.ilean' | sort | xargs sha256sum > SHA256_v2.txt
(cd K2 && find REPORT_K2.md REPORT_K2_v2.md NOTES_K2.md code logs -type f | sort | xargs sha256sum > SHA256_K2.txt)
sha256sum -c --quiet SHA256_v2.txt && (cd K2 && sha256sum -c --quiet SHA256_K2.txt) && echo MANIFEST_OK
sha256sum SHA256_v2.txt > SHA256_v2.sha256; (cd K2 && sha256sum SHA256_K2.txt > SHA256_K2.sha256)
sha256sum REPORT.md REPORT_v2.md K2/REPORT_K2.md K2/REPORT_K2_v2.md SHA256_v2.txt K2/SHA256_K2.txt lean/K3Finite.lean; wc -l SHA256_v2.txt K2/SHA256_K2.txt
