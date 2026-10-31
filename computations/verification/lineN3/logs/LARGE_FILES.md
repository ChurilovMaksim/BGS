# Large binary files of Line N3 not committed (integration, 31 Oct 2026)

Policy (as in PRs #64/#65): `.npy` files up to 1 MiB are committed; larger ones are listed here with sha256 and a regeneration note.
**One exception:** `g_R_V_final.npy` (3.9 MB) **is committed**. It is the extremal-norm matrix R used by N4's [CA] 8V certificate
(`../../lineN4/code/b_arb_cert.py`, Λ_free^{8V} ≤ 1.9656353), and the Adam search that made it cannot be rerun to the same bytes. The author's packet
`/workspace/bgs-lineN/N3/logs/` holds the other files.

| File | Bytes | sha256 | How to regenerate |
|---|---|---|---|
| `R_identity_320.npy` | 1638528 | 7df289c79ce9210a8064af8e5a6848a5ba54ca4e8488efebfd098e9a0e3360f5 | `np.save('R_identity_320.npy', np.eye(320, dtype=np.complex128))`; byte-identical (checked: array equal to `np.eye(320, dtype=complex128)`) |
| `g_R_V_final.npy` (**committed**) | 3920528 | 3dec95e4616afd6caf7f1a09c57e42960def967e50bbf7154e5dbf5b2a1add7c | made by `code/g2_ext_norm.py V 4 1.2 55 ...` (Adam search, phase 2); same bytes as `g_R_V_K04_K55_NT25_cert2.npy`. The search is not bit-reproducible, so the file is committed |
| `g_R_V_K04_K55_NT25_cert2.npy` | 3920528 | 3dec95e4616afd6caf7f1a09c57e42960def967e50bbf7154e5dbf5b2a1add7c | identical to `g_R_V_final.npy` |
| `g_R_V_phase1.npy` | 3920528 | fd1c8d8bbee1dd54363bd8327b5e6d52f4acd00879e8defe8c3be3f2ebf3cf49 | `code/g2_ext_norm.py` phase 1; same bytes as `g_R_V_K04_K55_NT24_cert.npy` |
| `g_R_V_K04_K55_NT24_cert.npy` | 3920528 | fd1c8d8bbee1dd54363bd8327b5e6d52f4acd00879e8defe8c3be3f2ebf3cf49 | identical to `g_R_V_phase1.npy` |

**Why leaving the others out is safe.** Every file not committed is either the identity matrix or a byte-for-byte duplicate or an
earlier search iterate (phase 1) of the committed `g_R_V_final.npy`. No registered claim depends on one of them.
