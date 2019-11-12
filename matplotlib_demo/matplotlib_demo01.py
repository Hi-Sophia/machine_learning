import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

'''
plt.figure(figsize=(8, 5))  figsize:指定figure的宽和高，单位为英寸

plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^') 

颜色 r(红色) b(蓝色) g(绿色)
线条：o(圆圈) --(破折线) s(正方形) ^(一角朝上的三角形) -(实线)

ax = plt.gca()  #获取当前坐标轴信息
plt.legend(loc='upper right')   #Legend 图例


'''

#编号为三，大小为800*500像素的图片
plt.figure(num=3, figsize=(8, 5))

l1, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--',label='linear line')
l2, = plt.plot(x, y2,label='square line')


plt.xlim((-1, 2))  #x坐标轴范围：(-1, 2)
plt.ylim((-2, 3))

plt.xlabel('I am x') #设置x坐标轴名称
plt.ylabel('I am y')


plt.xticks(np.linspace(-1,2,5))  #设置x轴刻度
plt.yticks([-2, -1.8, -1, 1.22, 3],  #置y轴刻度以及名称
           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])


ax = plt.gca()  #获取当前坐标轴信息
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom') # 所有位置：top，bottom，both，default，none
ax.yaxis.set_ticks_position('left')   # 所有位置：left，right，both，default，none

ax.spines['bottom'].set_position(('data', 0))  # 移动x坐标轴的位置 位置所有属性：outward，axes，data
ax.spines['left'].set_position(('data', 0))  # 移动Y坐标轴的位置  位置所有属性：outward，axes，dat

#Legend 图例
# plt.legend(loc='upper right')
plt.legend(handles=[l1, l2], labels=['up', 'down'],  loc='best')

plt.show()
