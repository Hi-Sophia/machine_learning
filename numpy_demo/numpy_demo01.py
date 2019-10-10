import numpy as np
from numpy import pi
import sys

'''
1、NumPy包的核心是 ndarray 对象
NumPy的每一个array对象只有一种数据类型

2、np.set_printoptions(threshold=sys.maxsize)  强制numpy打印整个数组

3、NumPy提供熟悉的数学函数，例如sin，cos和exp。在NumPy中，这些被称为“通函数”（ufunc）。
在NumPy中，这些函数在数组上按元素进行运算，产生一个数组作为输出。

'''
# a = np.arange(15).reshape(3, 5)

# 1、numpy属性
# a.shape  # 数组的维度
# a.ndim  # 数组轴的个数
# a.size  # 数组元素的总数

# a.dtype  # 数组中元素的类型
# a.itemsize  # 数组中每个元素的字节大小
# type(a)


# 2、数组的创建,数组类型根据元素类型推导
np.array([2, 3, 4.5])  # 一维
np.array([(1.5, 2, 3), (4, 5, 6)])  # 二维

np.zeros((3, 4))  # 创建全零数组，默认为float类型
np.ones((2, 3, 4), dtype=np.int16)  # 创建全一数组
np.empty((2, 3))  # 创建全空数组, 其实每个值都是接近于零的数:

np.arange(10, 20, 2)  # 用arange创建连续数组，10-19步长为2 【整数】
np.arange(12).reshape((3, 4))  # 3行4列，0到11
np.arange(24).reshape(2, 3, 4)  # 三维数组打印为矩数组表

np.linspace(1, 10, 20)  # 用linspace创建线段型数据  1-10且分割成20个数据，生成线段 【浮点数】
np.linspace(1, 10, 20).reshape((5, 4))  # 更改shape

# 3、矩阵运算   axis指定沿数组轴的操作
a = np.array([10, 20, 30, 40])  # array([10, 20, 30, 40])
b = np.arange(4)  # array([0, 1, 2, 3])

c = a - b
d = a + b
e = a * b
f = b ** 2
g = 10 * np.sin(a)
b < 3   #array([ True,  True,  True, False])


A = np.array([[1, 1], [0, 1]])
B = np.arange(4).reshape((2,2))

C = A + B  # 加法
D = np.add(A, B)  # 加法

E = A.dot(B)  # 矩阵相乘
F = A @ B  # 矩阵相乘
G = A * B  #元素相乘

# 4、常见函数
'''
a = np.array([1,2,3,4])
w = np.array([4,3,2,1])
np.average(a, weights=w) = a[0] * w[0] / w.sum()  + a[1] * w[1] / w.sum()  + a[2] * w[2] / w.sum()  + a[3] * w[3] / w.sum()  
'''
funarr = np.array([[1, 5, 5, 2],
                   [9, 6, 2, 8],
                   [3, 7, 9, 1]])

weights = np.array([1, 1, 1, 1])

np.argmin(funarr)  #元素最小值所对应的索引
np.argmax(funarr, axis=0)  # 元素最大值所对应的索引（按列）


np.mean(funarr, axis=0)  # 算数平均值
np.average(funarr, axis=0)  # 加权平均值


np.ptp(funarr, axis=0)  # 计算最大值与最小值差
np.median(funarr, axis=0)  # 中位数
np.percentile(funarr, q=50, axis=0)
np.std(funarr, axis=0)  # 计算每一列的标准差 =sqrt(((x1-x)^2 +(x2-x)^2 +......(xn-x)^2)/n)。


np.cumsum(funarr) #累加运算函数
np.diff(funarr) #累差运算函数
np.nonzero(funarr) #将所有非零元素的行与列坐标分割开，重构成两个分别关于行和列的矩阵。

np.sum(funarr,axis=0)  # sum of each column
np.sum(funarr,axis=1)  # sum of each row
np.min(funarr,axis=1)    # min of each row

funarr.cumsum(axis=1)  # cumulative sum along each row