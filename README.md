# 机器学习概述
### 一、学习流程

[1、python基础](https://github.com/wujuhong/machine_learning/python_basic)

2、[numpy](https://github.com/wujuhong/machine_learning/numpy_demo)

3、[pandas](https://github.com/wujuhong/machine_learning/pandas_demo)

4、[matplotlib](https://github.com/wujuhong/machine_learning/matplotlib_demo)

5、[sklearn](https://github.com/wujuhong/machine_learning/sklearn_demo)

### 二、机器学习流程

1. 特征工程

2. Train、Test数据分割
3. 模型训练
4. 预测
5. 交叉验证
6. 搜索最优参数

### 三、knn算法基本原理

KNN算法既可以应用于分类应用中，也可以应用在回归应用中。
KNN在分类预测时，一般采用多数表决法；而在做回归预测时，一般采用平均值法


def __init__(self, n_neighbors=5,
                 weights='uniform', algorithm='auto', leaf_size=30,
                 p=2, metric='minkowski', metric_params=None, n_jobs=1,
                 **kwargs):

### 四、[特征工程](<https://www.cnblogs.com/jasonfreak/p/5448385.html>)

特征处理是特征工程的核心部分，sklearn提供了较为完整的特征处理方法，包括数据预处理、特征选择、降维等

1、数据预处理:

| 类                  | 功能               | 说明                                                     |
| ------------------- | ------------------ | -------------------------------------------------------- |
| StandardScaler      | 无量纲化           | 标准化，基于特征矩阵的列，将特征值转换至服从标准正态分布 |
| MinMaxScaler        | 无量纲化           | 区间缩放，基于最大最小值，将特征值转换到[0, 1]区间上     |
| Normalizer          | 归一化             | 基于特征矩阵的行，将样本向量转换为“单位向量”             |
| Binarizer           | 二值化             | 基于给定阈值，将定量特征按阈值划分                       |
| OneHotEncoder       | 哑编码             | 将定性数据编码为定量数据                                 |
| Imputer             | 缺失值计算         | 计算缺失值，缺失值可填充为均值等                         |
| PolynomialFeatures  | 多项式数据转换     | 多项式数据转换                                           |
| FunctionTransformer | 自定义单元数据转换 | 使用单变元的函数来转换数据                               |

2、特征选择:

| 类                | 所属方式 | 说明                                                   |
| ----------------- | -------- | ------------------------------------------------------ |
| VarianceThreshold | Filter   | 方差选择法                                             |
| SelectKBest       | Filter   | 可选关联系数、卡方校验、最大信息系数作为得分计算的方法 |
| RFE               | Wrapper  | 递归地训练基模型，将权值系数较小的特征从特征集合中消除 |
| SelectFromModel   | Embedded | 训练基模型，选择权值系数较高的特征                     |

3、降维:

| 库            | 类   | 说明           |
| ------------- | ---- | -------------- |
| decomposition | PCA  | 主成分分析法   |
| lda           | LDA  | 线性判别分析法 |

### 五、了解调参