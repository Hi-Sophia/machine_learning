'''
一、机器学习的方法包括:
监督学习 supervised learning;  有数据，有标签
非监督学习 unsupervised learning; 只有数据，没有标签
半监督学习 semi-supervised learning; 结合监督学习和非监督学习
强化学习 reinforcement learning;  从经验中总结提升
遗传算法 genetic algorithm.  适者生存

二、选择学习方法：
看图选方法：根据官网提供的图
首先看数据的样本是否 >50，小于则需要收集更多的数据。
算法有四类:
分类（监督式学习）
回归（监督式学习）
聚类（非监督式学习）
降维（当数据集有很多很多属性的时候，可以通过 降维 算法把属性归纳起来）

三、knn算法基本原理：
KNN算法既可以应用于分类应用中，也可以应用在回归应用中。
KNN在分类预测时，一般采用多数表决法；而在做回归预测时，一般采用平均值法

四、模型保存
我们训练好了一个Model 以后总需要保存和再次预测
使用：pickle与joblib。

from sklearn.externals import joblib #jbolib模块
'''

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

'''
KNN算法既可以应用于分类应用中，也可以应用在回归应用中。
KNN在分类预测时，一般采用多数表决法；而在做回归预测时，一般采用平均值法

1、创建数据（加载iris数据集）
'''
iris = load_iris()
iris_X = iris.data
iris_y = iris.target

# print(iris_y)

# 把数据集分为训练集和测试集，其中 test_size=0.3，即测试集占总数据的 30%
X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3)

'''
2、建立模型 定义模块方式 KNeighborsClassifier()
'''
knn = KNeighborsClassifier(n_neighbors=5)

'''
3、基础验证
用fit来训练training data，这一步就完成了训练的所有步骤，后面的knn 就已经是训练好的模型，可以直接用来 predict 测试集的数据
'''
# 把数据集分为训练集和测试集，其中 test_size=0.3，即测试集占总数据的 30%
X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3, random_state=4)
knn.fit(X_train, y_train)
y_predict = knn.predict(X_test)

print(y_predict)
print(y_test)

print(knn.score(X_test, y_test))

'''
4、交叉验证:用于神经网络的调参,机器学习方法的调参
'''
scores = cross_val_score(knn, iris_X, iris_X, cv=5, scoring='accuracy')
print("cross validation")
print(scores)
print(scores.mean())


'''
5、判断模型好坏:
准确率(accuracy)会用于判断分类(Classification)模型的好坏
'''
# k_range = range(1,30)
# k_score = []
#
# for k in k_range:
#     knn = KNeighborsClassifier(n_neighbors=k)
#     scores = cross_val_score(knn,iris_X, iris_y, cv=10, scoring='accuracy')
#     k_score.append(scores.mean())
#
# #可视化数据
# plt.plot(k_range,k_score)
# plt.xlabel('Value of K for KNN')
# plt.ylabel('Cross-Validated Accuracy')
# plt.show()


'''
5、判断模型好坏:
平均方差(Mean squared error)会用于判断回归(Regression)模型的好坏
平均方差 越低越好
'''
k_range = range(1, 30)
k_score = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    loss = -cross_val_score(knn, iris_X, iris_y, cv=10, scoring='neg_mean_squared_error')
    k_score.append(loss.mean())

# 可视化数据
plt.plot(k_range, k_score)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated MSE')
plt.show()
