一、numpy常见用法：

1、random

- numpy.random.rand()：生成0,1之间的随机数

- np.random.random((3,3))：据给定维度生成[0,1)之间的数据，包含0，不包含1

- numpy.random.seed()：使得随机数据可预测。

  当我们设置相同的seed，每次生成的随机数相同。如果不设置seed，则每次会生成不同的随机数

  ```python
  np.random.seed(0)
  np.random.rand(4,3)
  ```

- numpy.random.RandomState()：伪随机数生成器

  **伪随机数是用确定性的算法计算出来的来自[0,1]均匀分布的随机数序列**。并不真正的随机，但具有类似于随机数的统计特征，如均匀性、独立性等

  ```python
  #对于某一个伪随机数发生器，只要该种子（seed）相同，产生的随机数序列就是相同的
  rng = np.random.RandomState(23355)
  rng.uniform(0,1,(2,3))
  ```

- np.random.normal(*loc=0.0*, *scale=1.0*, *size=None*)：高斯分布的概率密度函数

  loc：概率分布的均值，scale：概率分布的标准差

- numpy.random.standard_normal() ：标准正态分布随机样本

- np.random.randn(size)：正态分布随机数（μ=0, σ=1），对应于np.random.normal(loc=0, scale=1, size)

```python
import numpy as np
rng = np.random.RandomState(0)
rng.rand(4)
Out[14]: array([0.5488135 , 0.71518937, 0.60276338, 0.54488318])
    
rng = np.random.RandomState(0)
rng.rand(4)
Out[16]: array([0.5488135 , 0.71518937, 0.60276338, 0.54488318])
```

- np.random.uniform(low=0.0, high=1.0, size=None)

2、np.linspace(-1, 1, 50)：在指定的间隔内返回均匀间隔的数字

3、[Numpy数组的保存与读取](https://www.cnblogs.com/mfryf/p/9018325.html)

```python
np.savez("save.npz", array1=a1, array2=a2) #保存矩阵
data = np.load("save.npz") #加载矩阵
data["array1"]
```

4、np.ones_like(y)：返回一个用1填充的跟输入形状和类型一致的数组。

5、dx = np.mean(x[1:]-x[:-1])

6、trapz(y, x=None, dx=1.0, axis=-1) ：使用复合梯形规则沿给定轴积分

7、np.transpose(An)：矩阵转置

8、np.trace()：方阵的迹，即矩阵主对角元素之和

9、np.cov(x)：计算协方差

10、np.matmul(a, b) 等价于 np.dot(a, b) 

​      dot()和matmul()的区别是：当a或b其中一个是标量的时候，只能用np.dot，用matmul会报错。 

11、np.mat(a)：将目标数据的类型转换为矩阵（matrix）

12、np.flatnonzero()：该函数输入一个矩阵，返回扁平化后矩阵中非零元素的位置（index）

13、扁平化函数np.ravel()与np.flatten()的区别

```python
import numpy as np

a = np.arange(0,12).reshape(3,4)
b = a.ravel() #在修改b的时候,a中相应的数也改变了
b[1] = 99

c = np.arange(0,12).reshape(3,4)
d = c.flatten() #对拷贝所做修改不会影响原始矩阵 尽量使用flatten()避免意外错误
d[1] = 99
```

14、np.newaxis()：插入新维度

```python
np.linspace(-1,1,10)[:,np.newaxis]
np.linspace(-1,1,10)[:,np.newaxis]
```

15、np.c_ np.r_ 实现数组转矩阵

```python
a = np.array([[1,2,3],[11,22,33]])
b = np.array([[4,5,6],[44,55,66]])

c = np.c_[a,b] #按列转换成矩阵
r = np.r_[a,b] #按行转换成矩阵
```

二、numpy线性代数np.linalg：

np.linalg.inv(A)：求方阵的逆矩阵

np.linalg.det(A)：求矩阵的行列式

np.linalg.solve(A,b)：解形如AX=b的线性方程组

np.linalg.eig(A)：求特征值和特征向量

np.linalg.eigvals(A)：求矩阵的特征值

np.linalg.svd(A)：svd分解

```python
np.linalg.svd(a,full_matrices=1,compute_uv=1)
#a是一个形如(𝑀,𝑁)的矩阵
#full_matrices的取值为0或者1，默认值为1，这时u的大小为(𝑀,𝑀)，v的大小为(𝑁,𝑁)。否则u的大小为(𝑀,𝐾)，v的大小为(𝐾,𝑁),𝐾=𝑚𝑖𝑛(𝑀,𝑁) 
#compute_uv的取值是为0或者1，默认值为1，表示计算u,s,v。为0的时候只计算s
```

np.linalg.norm(x, ord=None, axis=None, keepdims=False)：求范数，默认l2范数

二范数：$$\sqrt{x_1^2+x_2^2+\ldots +x_n^2}$$



