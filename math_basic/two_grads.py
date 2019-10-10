def f_2d(x, y):
    return x ** 2 + 4 * x +  y ** 2 + 4 * y + 1


def df_2d(x, y):
    return 2 * x + 4, 2 * y + 4


x, y = 4, 4

for i in range(20):
    v_x, v_y = df_2d(x, y)
    x, y = x - 0.1 * v_x, y - 0.1 * v_y
    print("f({}{}) = {}".format(x, y, f_2d(x, y)))

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 3)
y = np.linspace(-6, 3)

X,Y = np.meshgrid(x,y)
fig = plt.figure()
ax = fig.gca(projection = '3d')

surf = ax.plot_surface(X,Y,f_2d(X,Y))

plt.show()