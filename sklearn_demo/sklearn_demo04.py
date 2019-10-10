
from sklearn import preprocessing  # 标准化数据模块
from sklearn.model_selection import train_test_split  # 将数据集分割成train与test的模块
from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC
import matplotlib.pyplot as plt


'''
正规化(标准化)数据可以提升机器学习的成效

1、生成具有2种属性的300笔数据
'''
X, y = make_classification(n_samples=300, n_features=2,
    n_redundant=0, n_informative=2,random_state=22, n_clusters_per_class=1,scale=100)

#可视化数据
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()

'''
2、标准化前的预测准确率只有0.477777777778
'''
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
clf = SVC()
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))


'''
3、标准化后的预测准确率提升至0.9
'''
X = preprocessing.scale(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
clf = SVC()
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))