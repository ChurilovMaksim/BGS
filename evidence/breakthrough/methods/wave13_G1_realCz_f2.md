# Wave 13, task 1 — G1 at f=2: PROVED (real-Cz subcase closed)

**Verdict.** G1′ (wave 12, §0) at f=2, i.e. v_p(D_m)=4, is proved.
Both subcases s=0 (k=2) and s=1 (k=1) are proved; the L6/L7 real-Cz
subcase does not survive at f=2: in case s=0 it never arises (no digit
induction is used), in case s=1 it is proved away by digit vanishing.
Repository untouched, no Lean built; this is a mathematical argument.

## 0. Setup and citations

p odd, f=2, P=p², R=Z[√2], α=3+2√2, β=ᾱ, Tr(x)=x+x̄, N(x)=xx̄.
L₀ = order of α mod p (coprime to p), k=v_𝔭(α^{L₀}−1) (same ∀𝔭|p),
s=f−k ∈ {0,1}, γ=α^{L₀}=1+pᵏu. G=⟨α⟩ mod P, |G|=L₀pˢ,
G₀=⟨α^{pˢ}⟩ (|G₀|=L₀), H₀=⟨α^{tpˢ}⟩, t=gcd(m,4).
Wave-12 Lemmas 1–5 and the wave-11 mod-p per-class lemma are used as
given. Divisible case (p|A, i.e. A≡0 mod p) in both §1–§2: A=pA₁,
A′=pA₁′, sequences are p×(mod-p sequences), and G1′ follows from the
wave-11 mod-p lemma. Henceforth A is a unit mod p.

**Lemma A (u is purely imaginary mod p).** δ=α^{L₀}−1 satisfies
δ̄=−β^{L₀}δ. Writing δ=pᵏu (u a unit at p, wave-12 Lemma 2),
ū=−β^{L₀}u, and β^{L₀}≡1 mod p, so Tr(u)≡0 mod p: u=μ√2, μ≠0 mod p.
Checked: p=3,5,7,11,17,19 (k=1) give u≡(0,1),(0,2),(0,3),(0,10),
(0,3),(0,4) mod p. Consequence: the collapsed line
L={x : Tr(xu)=0} equals F_p (xμ√2 purely imaginary ⟺ x∈F_p),
and Tr|_L is bijective (Tr(λ)=2λ, p odd).

## 1. Case s=0 (k=2): polynomial identity + Hensel

Here G=G₀, order L₀. For odd p, L₀≥3: L₀=1 forces p|2 (α−1=2+2√2),
L₀=2 forces p|4 (α²−1=16+12√2), both impossible.

**Identity.** For C a unit mod P, ∏_{z∈G}(X−Tr(Cz)) = V_{L₀}(X,N(C))
−Tr(C^{L₀}), where V_n is the Lucas polynomial (V₀=2, V₁=X,
V_{n+1}=XV_n−NV_{n−1}). Proof: Tr(Cz)=Cz+C̄z̄, and with T=Cz,
X−Tr(Cz)=(XT−T²−N)/T (z z̄=1). Now ∏_{z}(S−Cz)=S^{L₀}−C^{L₀}
(each factor divides it, factors comaximal by wave-12 Lemma 3,
both monic of degree L₀). With u+v=X, uv=N, the resultant gives
∏(X−Tr(Cz))=−(u^{L₀}−C^{L₀})(v^{L₀}−C^{L₀})/C^{L₀}
=V_{L₀}−Tr(C^{L₀}), using u^{L₀}+v^{L₀}=V_{L₀}, u^{L₀}v^{L₀}=N^{L₀}.
Verified exactly mod 25 (|H|=6) and mod 49 (|H|=3), 30 random C each.

**Rigidity.** The global multiset mod P is ρ=m/L₀ copies of
{Tr(Ag) : g∈G}, so it determines the polynomial, hence N(A)
(coefficient of X^{L₀−2} is −L₀N, L₀ prime to p) and Tr(A^{L₀})
(constant term, V_{L₀}(0,N) known from N). Then A′^{L₀}∈{A^{L₀},Ā^{L₀}}:
same trace and norm force the unordered pair {t₁,t₂}={x₁,x₂} in the
split case (t₁+t₂, t₁t₂ fixed), and a quadratic has ≤2 roots in the
inert case — this is where the mixed-root objection dies.
Hence A′=Aζ or Āζ with ζ^{L₀}=1, N(ζ)=1. The L₀-torsion of the
norm-1 group mod P is exactly G: mod p it is cyclic of order p±1
with unique subgroup of order L₀, and each mod-p root of T^{L₀}−1
lifts uniquely mod P by Hensel (derivative L₀T^{L₀−1} a unit mod p).
So ζ∈G, i.e. A′ is a shift (class r↦r+j) or reflection (r↦−r) of A:
per-class multisets are D_t-related. ∎

## 2. Case s=1 (k=1): digits vanish

Normalise by the wave-11 mod-p result: after a shift/reflection,
A″≡A mod p; write A″=A(1+pη), η∈R/p (A unit). It suffices to prove
per-class equality for (A,A″). Class r = ρ copies of ⊔_{z∈H₀}F(C_{r,z}),
C_{r,z}=Aαʳz, F(C)={Tr(Cγʲ) : j∈Z/p}, γ=1+pu.

**Full rigidity.** Collapse status depends only on Tr(Cu) mod p,
unchanged since C″≡C mod p. If F(C) is full (Lemma 5, v=0),
F(C)={a+p·j : j∈Z/p} with a=Tr(C); a″≡a mod p gives
F(C″)=F(C) exactly. So full parts are equal per class, hence pooled.

**Pooled collapsed equality.** Global multisets equal + full parts
equal ⟹ the multiset {Tr(C(1+pη)) : C∈Coll} equals {Tr(C) : C∈Coll},
Coll = pooled collapsed C_{r,z} (×ρ). Hence as polynomials over Z/p²,
∏_{C∈Coll}(X−Tr(C)−p·Tr(ηC)) = ∏_{C∈Coll}(X−Tr(C)).
Expanding mod p² and reducing mod p gives, with t_C=Tr(C) mod p,
s_C=Tr(ηC) mod p: Σ_C s_C∏_{C′≠C}(X−t_{C′})=0 in F_p[X].
Partial fractions ⟹ for each distinct t: R_t:=Σ_{C:t_C=t}s_C=0.

**Digits vanish.** By Lemma A, collapsed C mod p lie in L=F_p^×,
so t_C=2c with C≡c∈F_p^×, and s_C=c·Tr(η). Thus
R_t=m_t·(t/2)·Tr(η)=0; if Coll≠∅ some m_t>0 with t≠0, so Tr(η)=0.
Then every collapsed digit d_C=Tr(ηC)=c·Tr(η)=0. So F(C″)=F(C)
for collapsed cosets too, and per-class multisets are EXACTLY equal
(π=id after normalisation). ∎ If Coll=∅ the claim is vacuous.

## 3. Numerical confirmation

- Identity (§1) mod 25/49: holds exactly (see §1).
- Unit-case digit test (normalised pairs, all A unit mod p):
  (m,p)=(12,3): 68 pairs, 66 collapsed cosets, 0 nonzero digits;
  (30,5): 588 pairs, 580 cosets, 0; (42,7): 1719 pairs, 1680 cosets, 0.
  Per-class equality exact in all cases; full parts exact throughout.
- Note: nonzero digits seen in an earlier unfiltered run were all
  divisible-case (p|A) artefacts, where mod-p normalisation is vacuous
  (A≡0 mod p) — e.g. A₀=(0,3), A₁=(0,6) mod 9 is A₁=Ā₀ exactly,
  the apparent 1↔3 swap being the reflection. The divisible case is
  handled by induction (§0), not by digits.

## 4. What remains

G1 is now proved at f=2 (v_p(D_m)=4). Still open: G1 at f≥3 (L6/L7
in general — the real-Cz subcase persists there as stated in wave 12),
G3 (Lemma PC, common π), and Lean formalisation of this argument.
Combined with wave-13 G2, the exact per-class lemma's remaining gaps
are exactly G1 (f≥3) and G3.
