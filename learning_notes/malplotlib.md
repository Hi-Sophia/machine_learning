matplotlib常见用法：

###### pyplot.style.use[定制画布风格](https://zhuanlan.zhihu.com/p/37891729):

```python
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight') #定制画布风格
print(plt.style.available) #获取所有的自带样式

plt.rcParams['font.sans-serif']=['SimHei']#用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False#用来正常显示负号

def f(x, y):
    return (1 - x / 2 + x ** 3 + y ** 5) * np.exp(-x ** 2 - y ** 2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

#生成网格点坐标矩阵
X, Y = np.meshgrid(x, y)

# 绘制等高线
C = plt.contour(X, Y, f(X, Y))

# 填充等高线
#C = plt.contourf(X, Y, f(X, Y), cmap=plt.cm.hot)

# 添加高度与数字,inline=True，表示高度写在等高线上
plt.clabel(C, inline=True, fontsize=10)

plt.grid(True)
plt.show()
```



