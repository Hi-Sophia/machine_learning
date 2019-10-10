def f(x):
    return x ** 2 + 4 * x +1

def df(x):
    return 2 * x + 4

x_old = 3.14

for i in range(20):
    x_new = x_old - 0.1 * df(x_old)
    x_old = x_new
    print("f({}) = {}".format(x_new,f(x_new)))


import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-6,3)
plt.plot(x,f(x))
plt.show()
