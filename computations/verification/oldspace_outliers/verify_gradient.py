#!/usr/bin/env python3
"""Exact cyclotomic derivatives of the seven diagonal and hopping profiles."""
import sympy as sp


def require(condition, name):
    if not condition:
        raise ArithmeticError(name)


def main():
    x, z = sp.symbols("x z")
    phi = sp.cyclotomic_poly(28, x)
    cosine = lambda k: (z**k + z**(-k))/2
    sine = lambda k: (z**k - z**(-k))/(2*sp.I)
    r = (1-cosine(7))*(1+cosine(1))
    potential = cosine(7)-sp.Rational(1, 10) + r*(sp.Rational(1, 10)+sine(1)/100)

    def derivative(expr):
        return sp.expand(sp.I*z*sp.diff(expr, z))

    def field(expr, power):
        expr = sp.expand(expr.subs(sp.I, x**7))
        monomials = expr.as_coefficients_dict()
        total = 0
        for monomial, coefficient in monomials.items():
            powers = monomial.as_powers_dict()
            e = powers.get(x, 0) + power*powers.get(z, 0)
            total += coefficient*x**(e % 28)
        return sp.Poly(total, x).rem(sp.Poly(phi, x)).as_expr()

    gradients = []
    curvature = 0
    for j in range(7):
        power = 14+4*j
        gradient = field(100*derivative(potential), power)
        expected = field(20*sine(1)+2*cosine(2)-2*cosine(1), 4*j)
        # 100 V'(q_j)/(2*pi) = 20 sin(theta_j)+2(cos(2 theta_j)-cos(theta_j)).
        require(gradient == expected, f"gradient {j}")
        gradients.append(gradient)
        curvature += field(derivative(derivative(potential)), power)
        require(field(r, 4*j) == field(derivative(r), 4*j) == 0, f"hopping zero {j}")
        require(field(derivative(derivative(r)), 4*j) == field(49*(1+cosine(1)),4*j),
                f"hopping second derivative {j}")
    curvature -= 7*field(derivative(derivative(potential)),14)
    require(curvature == -sp.Rational(357, 10), "sum curvature in angular units")
    nonconstant = sp.Matrix(11, 6, lambda i,j: gradients[j+1].coeff(x,i+1))
    require(nonconstant.rank() == 5, "rank of nonconstant coefficients")
    require(sp.expand(sum(gradients)) == 0, "one relation with zero constant")
    require(1352*40**48 < 47**48, "Haar net factor")
    print("PASS Haar net factor < 1")
    print("PASS cyclotomic gradient rank 5, sum curvature -357/10, 7 quadratic hopping zeros")
    if __import__("sys").argv[1:] == ["--rows"]:
        for exponent in range(1, 12):
            print(exponent, [gradients[j].coeff(x, exponent) for j in range(1,7)])


if __name__ == "__main__":
    main()
