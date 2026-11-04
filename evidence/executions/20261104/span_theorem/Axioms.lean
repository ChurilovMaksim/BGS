import Bgs.LineNSpanArith
#print axioms Bgs.LineNSpan.eps4
#print axioms Bgs.LineNSpan.eps4_gt_32
#print axioms Bgs.LineNSpan.norm_116
#print axioms Bgs.LineNSpan.norm_82s2
#print axioms Bgs.LineNSpan.norm_118
#print axioms Bgs.LineNSpan.shell13_116
#print axioms Bgs.LineNSpan.shell13_82s2
#print axioms Bgs.LineNSpan.shell13_118
#print axioms Bgs.LineNSpan.cert_116
#print axioms Bgs.LineNSpan.cert_82s2
#print axioms Bgs.LineNSpan.cert_118
#print axioms Bgs.LineNSpan.cert_2
#print axioms Bgs.LineNSpan.cert_3s2
#print axioms Bgs.LineNSpan.span_116
#print axioms Bgs.LineNSpan.span_82s2
#print axioms Bgs.LineNSpan.span_118
#print axioms Bgs.LineNSpan.span_2
#print axioms Bgs.LineNSpan.span_3s2
-- negative control: a wrong word is rejected
example : Bgs.LineNSpan.cert 116 0 Bgs.LineNSpan.w116_k0 Bgs.LineNSpan.w116_ns [1, -1, 0, 1, 1] = false := by decide +kernel
example : Bgs.LineNSpan.floorOK 116 0 0 100 = false := by decide +kernel
