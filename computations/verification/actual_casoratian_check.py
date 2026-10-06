"""Check the exact Casoratian identity and its uniform order exclusion."""
from pathlib import Path
import argparse
import json
from actual_commutant_common import verify_data, require

def main(argv=None):
    import sympy as s
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parents[2] / 'build' / 'actual_commutant')
    args=parser.parse_args(argv)
    data=Path(__file__).resolve().parent/'actual_commutant_data'
    verify_data(data)
    q=s.symbols('q')
    P=s.Poly.from_list(json.loads((data/'casoratian_results.json').read_text())['determinant_coefficients'],q,modulus=5)
    yd=json.loads((data/'bounded_boundary_polynomials.json').read_text())
    require(P.degree()==113,'Casoratian degree')
    require(P.monic()==s.Poly(s.sympify(yd['denominator']),q,modulus=5).monic(),'Casoratian identity')
    h=s.Poly(q,q,modulus=5)
    for _ in range(84):h=(h**5).rem(P)
    require(s.gcd(P,h-s.Poly(q,q,modulus=5)).monic()==s.Poly(q*q+1,q,modulus=5),'Casoratian Frobenius gcd')
    require(pow(5,42,49)==1 and all(pow(5,k,49)!=1 for k in (21,14,6)),'order49(5)')
    result={'degree':113,'frobenius_power':84,'gcd':'q^2+1','ord49_5':42,'passed':True}
    args.output.mkdir(parents=True,exist_ok=True)
    (args.output/'actual_casoratian_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':main()
