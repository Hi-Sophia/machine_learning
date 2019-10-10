import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2*x + 1

plt.figure(num=1, figsize=(8, 5),)
plt.plot(x, y,)


ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))


x0 = 1
y0 = 2*x0 + 1
plt.plot([x0,x0],[0,y0],'k--',linewidth = 2.5)
plt.scatter(x0,y0,color = 'b')

#用%.2f保留两位小数，横向居中对齐ha='center'，纵向底部（顶部）对齐va='bottom'：
# plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')

plt.text(-3.7,3,r'$This\ is\ some$',fontdict={'size':16,'color':'r'})
plt.show()