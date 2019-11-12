import numpy as np
import sympy as sym

'''
教程：https://www.cnblogs.com/zyg123/p/10539650.html
'''
# 1、单个符号初始化
x = sym.Symbol('x')

# 2、多个符号初始化
y, z = sym.symbols('x y')

# 输出设置
sym.init_printing(use_latex=True)

# 输出结果
# print(x ** 2 + y + z)
# print(sym.latex(x ** 2 + y + z))


expr1 = sym.sin(x) ** 2 + sym.cos(x) ** 2
expr2 = sym.sin(x) ** 4 - 2 * sym.cos(x) ** 2 * sym.sin(x) ** 2 + sym.cos(x) ** 4
# 进行三角形简化
r1 = sym.trigsimp(expr1)
r2 = sym.trigsimp(expr2)


x = sym.symbols('x')
expr1 = sym.exp(sym.sin(x))

# 1、级数展开
r1 = expr1.series(x, 0, 6)
# 2、去除尾数
r2 = expr1.series(x, 0, 6).removeO()


print("r1:", r1)
print("r2:", r2)
# print("r3:", r3)

m2 = sym.Matrix([[1, -1], [3, 4], [0, 2]])
print(sym.latex(m2))


x = sym.symbols('x')
a = sym.Integral(sym.cos(x)*sym.exp(x), x)
sym.Eq(a, a.doit())
