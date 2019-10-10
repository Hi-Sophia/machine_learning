# machine_learning
一、机器学习流程

(1)、特征工程
(2)、Train、Test数据分割
(3)、模型训练
(4)、预测
(5)、交叉验证
(6)、搜索最优参数

二、knn算法基本原理
KNN算法既可以应用于分类应用中，也可以应用在回归应用中。
KNN在分类预测时，一般采用多数表决法；而在做回归预测时，一般采用平均值法


def __init__(self, n_neighbors=5,
                 weights='uniform', algorithm='auto', leaf_size=30,
                 p=2, metric='minkowski', metric_params=None, n_jobs=1,
                 **kwargs):



三、特征工程
参考博文：https://www.cnblogs.com/jasonfreak/p/5448385.html

特征处理是特征工程的核心部分，sklearn提供了较为完整的特征处理方法，包括数据预处理、特征选择、降维等

数据预处理:
StandardScaler(无量纲化)	标准化，基于特征矩阵的列，将特征值转换至服从标准正态分布
MinMaxScaler(无量纲化)	区间缩放，基于最大最小值，将特征值转换到[0, 1]区间上
Normalizer(归一化)	基于特征矩阵的行，将样本向量转换为“单位向量”
Binarizer(二值化)	基于给定阈值，将定量特征按阈值划分
OneHotEncoder(哑编码)	将定性数据编码为定量数据
Imputer(缺失值计算)	计算缺失值，缺失值可填充为均值等
PolynomialFeatures(多项式数据转换)	多项式数据转换
FunctionTransformer(自定义单元数据转换)	使用单变元的函数来转换数据

特征选择:
VarianceThreshold(Filter)	方差选择法
SelectKBest(Filter)	可选关联系数、卡方校验、最大信息系数作为得分计算的方法
RFE	Wrapper(递归地训练基模型) 将权值系数较小的特征从特征集合中消除
SelectFromModel(Embedded)	训练基模型，选择权值系数较高的特征

降维:
decomposition	PCA主成分分析法
lda	LDA线性判别分析法

四、了解调参