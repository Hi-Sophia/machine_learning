from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

'''
数据集：https://scikit-learn.org/stable/modules/classes.html#module-sklearn.datasets


常见模型参数:
model.coef_   #输出模型的斜率
model.intercept_  #输出模型的截距（与y轴的交点）
model.get_params() #取出之前定义的参数
model.score(data_X, data_y): 对Model用 R^2 的方式进行打分，输出精确度
'''

'''
1、创建数据
'''
load_data = datasets.load_boston()
data_X = load_data.data
data_y = load_data.target

'''
2、训练模型
'''
model = LinearRegression()
model.fit(data_X, data_y)
#用 X 的前 4 个来预测
y_predict = model.predict(data_X[:4, :])
print(y_predict)
print(data_y[:4])

# 输出模型的斜率
print(model.coef_)
# 截距（与y轴的交点）
print(model.intercept_)
# 取出之前定义的参数。
print(model.get_params())
# 对Model用 R^2 的方式进行打分，输出精确度
print(model.score(data_X, data_y))


'''
3、创建虚拟数据－可视化

用函数来建立 100 个 sample，有一个 feature，和一个 target
noise 越大的话，点就会越来越离散
'''

X, y = datasets.make_regression(n_samples=100, n_features=1, n_targets=1, noise=50)
plt.scatter(X, y)
plt.show()
