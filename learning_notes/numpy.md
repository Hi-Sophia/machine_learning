1、伪随机数生成器：numpy.random.RandomState()

**伪随机数是用确定性的算法计算出来的来自[0,1]均匀分布的随机数序列**。并不真正的随机，但具有类似于随机数的统计特征，如均匀性、独立性等

```python
import numpy as np
rng = np.random.RandomState(0)
rng.rand(4)
Out[14]: array([0.5488135 , 0.71518937, 0.60276338, 0.54488318])
    
rng = np.random.RandomState(0)
rng.rand(4)
Out[16]: array([0.5488135 , 0.71518937, 0.60276338, 0.54488318])
```

