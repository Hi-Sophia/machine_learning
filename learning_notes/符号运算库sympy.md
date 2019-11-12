参考博文：<https://www.cnblogs.com/zyg123/p/10539650.html>

#### 一、基本操作：

##### 1、符号的初始化与输出设置symbol() symbols() latex()

```python
import sympy as sym
# 1、单个符号初始化
x = sym.Symbol('x')

# 2、多个符号初始化
y, z = sym.symbols('x y')

# 3、输出设置
sym.init_printing(use_latex=True)
```

##### 2、替换符号-subs(old,new)

- 数值替换，用数值替换符号，进行带入计算。
- 符号替换，用一些符号替换符号。

##### 3、将字符串变为sympy表达式-sympify（）

##### 4、数值计算-evalf()

```python
expr = sym.sqrt(8)
result = expr.evalf()
print(result)
```

#### 二、简化操作：

##### 1、有理数与多项式的简化

- expand()：对括号里的多项式进行展开
- factor()：对展开的多项式提取公因式
- ceiling()：对多项式进行合并同类项
- cancel()：简化分式
- apart()：分式展开（原本只有一项的分式表达式，展开为多项的分式表达式）

##### 2、三角函数的简化

- trigsimp()：可以简化三角函数，反三角函数也可以
- expand_trig()：可以展开三角函数，同样反三角函数也可以

##### 3、指数函数的简化

（1）指数的合并（进行指数的合并，如果不符合，则不进行简化）

- powsimp()：主要用于同底数或者同指数  如： $$x^2 x^3 = x^5$$
- powdenest()：主要用于只有一个底数的不同指数  $$(x^a)^b = x^{ab}$$

（2）指数的展开：

- expand_power_exp()：用于同底数的展开
- expand_power_base()：用于同指数的展开 

##### 4、对数函数的简化

- logcombine()：用于合并对数。
- expand_log()：用于对数的展开。

#### 三、微积分

##### 1、求导数-diff()

```python
#1、一阶求导
x = sym.Symbol('x')
expr1 = sym.exp(x**2)
r1 = sym.diff(expr1, x)

#2、多阶求导
#a、带参数中，添加几个x,就是对x的几次求导。diff(expr, x, x,x……)
#b、用数字来控制所求的阶数：diff(expr, x, n)

#3、求偏导数
x, y, z = sym.symbols('x y z')
expr2 = sym.exp(x*y*z)
r2 = sym.diff(expr1, x, 1, y, 2, z, 4)
```

##### 2、求积分-integrate()

```python
x, y = sym.symbols('x y')

# 1、求不定积分
expr1 = sym.cos(x)
r1 = sym.integrate(expr1, x)

# 2、求定积分
expr2 = sym.exp(-x)
r2 = sym.integrate(expr2, (x, 0, sym.oo))

# 3、求多重积分
expr3 = sym.exp(-x ** 2 - y ** 2)
r3 = sym.integrate(expr3, (x, -sym.oo, sym.oo), (y, -sym.oo, sym.oo))
```

##### 3、求极限-limit()

```python
x = sym.symbols('x')

# 1、求趋于某个值的极限
expr1 = sym.sin(x)/x
r1 = sym.limit(expr1, x, 0)

# 2、正向趋进
expr2 = 1/x
r2 = sym.limit(expr2, x, 0, '+')

# 3、负向趋进
r3 = sym.limit(expr2, x, 0, '-')
```

##### 4、级数展开-series()

```python
x = sym.symbols('x')
expr1 = sym.exp(sym.sin(x))

# 1、级数展开
r1 = expr1.series(x, 0, 6)
# 2、去除尾数
r2 = expr1.series(x, 0, 6).removeO()
```

#### 四、解方程组

1、求解多元一次方程-slove()

2、解线性方程组-linslove()

3、解非线性方程组-nonlinslove()

4、解微分方程-dslove()

五、[矩阵的操作](https://www.cnblogs.com/zyg123/p/10554686.html)

1、矩阵的创建-Matrix()

2、常用的构造矩阵

- 单位矩阵：eye(）
- 零矩阵：zeros(）
- 一矩阵：ones(）
- 对角矩阵：diag(）

3、基本操作

- 获取形状：.shape()
- 获得单行与单列：.row(n) .col(n)
- 删除行与列：row_del(n) .col_del(n)
- 插入新行与列：.row_insert(pos, M) .col_insert(pos, M)
- 对矩阵求转置：m.T

4、矩阵的运算

- 加减法：直接使用+ -即可
- 乘法：*
- 求逆矩阵：M**(-1)

5、行列式

- 求行列式：M.det()
- 求阶梯矩阵：M.rref()
- 求特征值与向量：M.eignvals()

6、对角化矩阵-diagonalize()