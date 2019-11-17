import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import sympy as sym
import math
import numpy as np


# def pca(X):
#     m, n = X.shape
#
#     # 计算协方差
#     # C = 1.0 / m * X.T.dot(X)
#     X = X - np.mean(X,axis=0)
#     C = np.cov(X)
#
#     # 特征值赋值给evalues，对应特征向量赋值给evectors
#     evalues, evectors = np.linalg.eig(C)
#
#     # 特征值从大到小排列，返回数组索引
#     sorted_indices = np.argsort(-evalues)
#
#     # 特征向量按特征值大小从左到右排列
#     sorted_evectors = evectors[:, sorted_indices]
#     sorted_evalues = evalues[sorted_indices]
#
#     return sorted_evectors, np.diag(sorted_evalues), sorted_evalues
#
#
# print(pca(np.array([[1,2],[3,4],[5,6]])))


#
# total = 20
# red = 2
# white = 8
# blue = 3
# black = 1
# purple = 6
#
def calcuateEntropy(x):
    H = 0
    total = np.sum(x)
    for i in x:
        p_x = float(i) / float(total)
        H = H - p_x * np.log2(p_x)
    return H


x = [2, 8, 3, 1, 6]
print(calcuateEntropy(x))


sym.Function('y')
