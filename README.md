# 机器学习概述
### 一、学习流程

1、[python基础](https://github.com/wujuhong/machine_learning/tree/master/python_basic)

2、[numpy](https://github.com/wujuhong/machine_learning/tree/master/numpy_demo)

3、[pandas](https://github.com/wujuhong/machine_learning/tree/master/pandas_demo)

4、[matplotlib](https://github.com/wujuhong/machine_learning/tree/master/matplotlib_demo)

5、[sklearn](https://github.com/wujuhong/machine_learning/tree/master/sklearn_demo)

6、数学基础

- [x] [导数与微分（高数上）](https://app.yinxiang.com/fx/29f52780-3b5a-4144-9110-2a27b044c0ee)
- [x] [多元函数微分法（高数下）](https://app.yinxiang.com/fx/98e868d6-7d2e-47fe-ae71-6c7efd6261a5)
- [x] [无穷级数（高数下）](https://app.yinxiang.com/fx/58533420-d7e0-463b-8691-099328955ea8)
- [x] [线性代数](https://app.yinxiang.com/fx/00d4254e-f750-4cef-998a-15f1adc321b1)
- [x] [概率论](https://app.yinxiang.com/fx/63412cfb-3436-4970-98dc-6f13b9ae1670)

7、人工智能概念

### 二、机器学习流程

1. 特征工程

2. Train、Test数据分割
3. 模型训练
4. 预测
5. 交叉验证
6. 搜索最优参数

### 三、[KNN算法基本原理](https://github.com/wujuhong/machine_learning/blob/master/learning_notes/KNN算法基本原理.md)

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