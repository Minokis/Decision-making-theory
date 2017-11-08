# пример использования sympy для поиска производной
import sympy as sym

x = sym.Symbol('x')
alpha = sym.pi/2 - sym.atan(x/1.7) - sym.atan(1/x)
alpha_deriv = sym.diff(alpha, x, 1)
sym.simplify(alpha_deriv)
solution = sym.solve(alpha_deriv, x)
print(solution)
