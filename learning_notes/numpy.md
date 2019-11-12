1、random

- numpy.random.RandomState()：伪随机数生成器

**伪随机数是用确定性的算法计算出来的来自[0,1]均匀分布的随机数序列**。并不真正的随机，但具有类似于随机数的统计特征，如均匀性、独立性等

- np.random.normal(*loc=0.0*, *scale=1.0*, *size=None*)：高斯分布的概率密度函数

loc：概率分布的均值，scale：概率分布的标准差

- np.random.randn(size)：标准正太分布（μ=0, σ=1），对应于np.random.normal(loc=0, scale=1, size)

```python
import numpy as np
rng = np.random.RandomState(0)
rng.rand(4)
Out[14]: array([0.5488135 , 0.71518937, 0.60276338, 0.54488318])
    
rng = np.random.RandomState(0)
rng.rand(4)
Out[16]: array([0.5488135 , 0.71518937, 0.60276338, 0.54488318])
```

2、np.linspace(-1, 1, 50)：在指定的间隔内返回均匀间隔的数字

3、[Numpy数组的保存与读取](https://www.cnblogs.com/mfryf/p/9018325.html)

```python
np.savez("save.npz", array1=a1, array2=a2) #保存矩阵
data = np.load("save.npz") #加载矩阵
data["array1"]
```

