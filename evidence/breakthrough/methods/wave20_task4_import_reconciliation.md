# Wave 20, task 4 — Derand import path and pellQ/pellP signatures, reconciled with main

All facts fetched via the GitHub connector ONLY, at HEAD
`d87dce0d9277579568edfee6cffecbc96ea61024` (PR #76). Nothing modified;
no draft, no repository file touched.

## 1. Import line for Derand in Bgs.lean

File: `formalization/Bgs.lean`,
blob SHA `db8299548765eeef41d814586fcb2224c4ba7579`. Verbatim line:

```
import Bgs.LineBDerand
```

Flat, single segment after `Bgs.` — exactly the wave-6-verified form.

## 2. File path of the Derand module

```
formalization/Bgs/LineBDerand.lean
```

Blob SHA `01fa6e63551542de55cce52cb9fb54c660f89b54`
(matches the task's `01fa6e63…`). The dotted path does NOT exist:
`formalization/Bgs/LineB/Derand.lean` returns "path does not point to
a file or directory" at the same ref.

## 3. Signatures in LineBDerand.lean (verbatim)

Namespace declared inside the file (first line):

```
namespace Bgs.LineB.Derand
```

That is the whole discrepancy, resolved: the NAMESPACE is dotted
(`Bgs.LineB.Derand`), but the MODULE/IMPORT PATH is flat
(`Bgs.LineBDerand`). The drafts' `import Bgs.LineB.Derand` is wrong
as an import (no such file); the correct form is
`import Bgs.LineBDerand` plus qualification/open of namespace
`Bgs.LineB.Derand` for the names. File ends with
`end Bgs.LineB.Derand`.

```
def pellX : Nat → Int
  | 0 => 1
  | n+1 => 3 * pellX n + 8 * pellY n
where pellY : Nat → Int
  | 0 => 0
  | n+1 => pellX n + 3 * pellY n

def pellY (n : Nat) : Int := pellX.pellY n

def Dm (m : Nat) : Int := 2 * (pellX m - 1)

def gp (m : Nat) : Nat :=
  (pellX m - 1).toNat / Nat.gcd (pellX m - 1).toNat (pellY m).toNat

def yp (m : Nat) : Nat :=
  (pellY m).toNat / Nat.gcd (pellX m - 1).toNat (pellY m).toNat

def pellP : Nat → Int          -- Pell numbers P_0=0, P_1=1, P_{n+1} = 2P_n + P_{n-1}
  | 0 => 0
  | 1 => 1
  | n+2 => 2 * pellP (n+1) + pellP n

def pellQ : Nat → Int          -- companion Pell numbers Q_0=2, Q_1=2
  | 0 => 2
  | 1 => 2
  | n+2 => 2 * pellQ (n+1) + pellQ n
```

## Consequence for the pellC1 cast caveat

**No cast fix is needed on the `Nat → Int` ground: both `pellQ` and
`pellP` ARE `Nat → Int` in main.** The remaining caveat is narrower:
`gp` and `yp` are `Nat → Nat` (via `.toNat` and `Nat.gcd`), so any
draft statement mixing them with `Int`-valued `pellQ`/`pellP`/`Dm`
still needs its casts checked — but the feared case (pellQ/pellP not
being `Nat → Int`) does not occur.

Cross-check (values in main, by `decide`):
`gp` for m=1..10 = [2, 8, 14, 48, 82, 280, 478, 1632, 2786, 9512];
`yp` for m=1..10 = [1, 3, 5, 17, 29, 99, 169, 577, 985, 3363].
This matches the milestone-1 draft's C1 restatement (odd: `gp =
pellQ`; even: `gp = 4·pellP`: e.g. m=3, pellQ 3 = 14; m=4, 4·pellP 4
= 4·12 = 48). Note `D_closed` in main is itself only a finite check
(1 ≤ m ≤ 20, by `decide`), not a general theorem.

## Nothing missing

All three requested facts were fetched; no connector gap.
