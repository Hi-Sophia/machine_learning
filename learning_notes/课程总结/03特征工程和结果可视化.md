一、数据预处理：

1、StandardScaler()【行、列可指定】：适合整体都不太规整，方差较大的场景

```python
scaler = preprocessing.StandardScaler().fit(data)
'''
公式：(X-X_mean)/X_std   将数据按其属性(按列进行)减去其均值，然后除以其标准差
sklearn.preprocessing.scale(X, axis=0, with_mean=True,with_std=True,copy=True)
根据参数的不同，可以沿任意轴标准化数据集。

参数解释：StandardScaler(copy=True, with_mean=True, with_std=True)
X：数组或者矩阵
axis：int类型，初始值为0，axis用来计算均值(means)和标准方差(standard deviations). 如果是0，则单独的标准化每个特征（列），如果是1，则标准化每个观测样本（行）。
with_mean: boolean类型，默认为True，表示将数据均值规范到0
with_std: boolean类型，默认为True，表示将数据方差规范到1
'''
```

2、MinMaxScaler()【行、列可指定】：适合存在极端大和小的点的数据

```python
min_max_scaler = preprocessing.MinMaxScaler().fit(data)
'''
公式：X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
将属性缩放到一个指定的最大值和最小值(通常是1-0)之间

参数解释：MinMaxScaler(copy=True, feature_range=(0, 1))
'''
```

3、归一化 Normalizer()【行】：服务于大量**向量点乘运算**的场景，防止因为向量值过大造成极端的影响

```python
normalizer = preprocessing.Normalizer(norm='l2').fit(data)
'''
公式：样本中的每个点/l2 norm  
p-范数的计算公式：||X||p=(|x1|^p+|x2|^p+...+|xn|^p)^1/p

参数解释：Normalizer(copy=True, norm='l2')
'''
```

4、二值化 Binarizer()：如学习成绩，只关心“及格”或不“及格，转换成“1”和“0”表示及格和未及格

```python
binarizer = preprocessing.Binarizer(threshold=0).fit(X) 
```

5、OneHotEncoder()：【列】有多少个状态就有多少比特，而且只有一个比特为1，其他全为0的一种码制

```python
enc = preprocessing.OneHotEncoder().fit(x)
'''
参数解释：OneHotEncoder(categorical_features='all', dtype=<class 'numpy.float64'>,
       handle_unknown='error', n_values='auto', sparse=True)
categorical_features = 'all'：这个参数指定了对哪些特征进行编码，默认对所有类别都进行编码【可以自己指定选择哪些特征，通过索引或者 bool 值来指定，没有进行编码，就放在最后一位】
handle_unknown=’error’：其值可以指定为 "error" 或者 "ignore"，即如果碰到未知的类别，是返回一个错误还是忽略它
n_values=’auto’：表示每个特征使用几维的数值由数据集自动推断，即几种类别就使用几位来表示
sparse=True：表示编码的格式，默认为 True，即为稀疏的格式
     
'''
```

6、PolynomialFeatures()

```python
'''
一个输入样本是２维的。形式如[a,b] ,则二阶多项式的特征集如下[1,a,b,a^2,ab,b^2]。

参数解释：PolynomialFeatures(degree=2, include_bias=True, interaction_only=False)
include_bias(默认为True)：如果为False的话，那么就不会有上面的1那一项。
interaction_only(默认为False):如果指定为True，那么就不会有特征自己和自己结合的项
'''
```

