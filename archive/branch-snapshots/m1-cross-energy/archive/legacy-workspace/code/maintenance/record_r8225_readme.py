import io
p='README.md'; s=io.open(p,encoding='utf-8').read()
NL=chr(10)
rows = (
 "| **R82: op:pairing resolved** - new exact identity `M6(q) = sum_(P,Q) |W(P,Q)|^2`"
 ": the sixth moment IS a family second moment (traces W over the curves "
 "C_P,Q = y with e3(y)=P, e3(y-1)=Q), machine-verified to 1.1e-15 at 10 primes; "
 "Catalan constant C_3 = 5 = normalised family second moment (monotone convergence "
 "4.19->4.83 at N=37..181, designs reach 5.00); matching picture dead. The k>=3 "
 "moments and the local law need the SAME single input: a Katz-type second-moment "
 "theorem for the S_3-family | **identity PROVEN; constant = cohomological input** |" + NL +
 "| **R82: Lean scale-law certificate** - S1_order, S2a_power, S2_trace, "
 "S3_branches at p=199 all closed by kernel decide with ZERO axioms | "
 "**PROVEN (machine)** |" + NL + NL)
rep = "## Layout" + NL
assert rep in s
io.open(p,'w',encoding='utf-8').write(s.replace(rep, rows + rep, 1))
print("README rows added")
