import numpy as np
import matplotlib.pyplot as plt

'''
# figsize:指定figure的宽和高，单位为英寸
plt.figure(figsize=(8, 5))


#c表示颜色 默认是蓝色'b',表示的是标记的颜色，可以是一个表示颜色的字符、或一个长度为n的表示颜色的序列
plt.scatter(X, Y, c=T)


'''

x = np.linspace(-np.pi, np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi], ['$-\pi$', '$-\pi/2$', '$0$', '$+\pi/2$', '$+\pi$'])
plt.yticks([-1, 0, 1], ['$-1$', '$0$', '$1$'])

plt.plot(x, y1, color='red', linewidth=2.5, linestyle="-", label="sin")
plt.plot(x, y2, color='blue', linewidth=2.5, linestyle="--", label="cos")

# plt.gca() 移动脊柱 坐标系设置
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data', 0))  # 移动x坐标轴的位置
ax.spines['left'].set_position(('data', 0))  # 移动Y坐标轴的位置

# plt.legend()添加图例
plt.legend(loc='upper left')

# plt.annotate() 给特殊点做注释
'''

xycoords='data' 是说基于数据的值来选位置,
xytext=(+30, -30) 和 textcoords='offset points' 对于标注位置的描述 和 xy 偏差值
arrowprops 对图中箭头类型的一些设置.
'''

# plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
#              xy=(x, y1), xycoords='data',
#              xytext=(+10, +30),textcoords='offset points',
#              fontsize=16,
#              arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))



# plt.grid(True)
plt.show()
