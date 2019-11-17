import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])

np.vstack((A,B))  #上下合并
np.hstack((A,B))  #左右合并
np.stack((A,B),axis=0) #对指定axis增加维度

C = np.array([1, 1, 1])[:,np.newaxis]  #转置
D = np.array([2, 2, 2])[:,np.newaxis]  #转置
np.hstack((C,D))  #左右合并


#np.concatenate((A,B,B,A),axis=1) #合并操作需要针对多个矩阵或序列时

x = np.array([0, 1, 2])
y = np.array([0, 1])
X, Y = np.meshgrid(x, y)


'''
np.split(A,2,axis=1)   等量分割
np.vsplit()
np.hsplit()
np.array_split(A,3,axis=1)  不等量分割


= 的赋值方式会带有关联性 
copy() 的赋值方式没有关联性
'''


