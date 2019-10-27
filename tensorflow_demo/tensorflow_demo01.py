import tensorflow as tf
import numpy as np

'''
TensorFlow是采用数据流图（data flow graphs）来计算，


张量（Tensor):
张量有多种. 零阶张量为纯量或标量 (scalar) 也就是一个数值. 比如 [1]
一阶张量为 向量 (vector), 比如 一维的 [1, 2, 3]
二阶张量为 矩阵 (matrix), 比如 二维的 [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

'''
#1、创建数据
x_data = np.random.rand(100).astype(np.float)
y_data = x_data * 0.1 + 0.3

#2、搭建模型
Weight = tf.Variable(tf.random.uniform([1],-1.0,1.0))
baises = tf.Variable(tf.zeros([1]))

y = Weight * x_data + baises

#计算误差
loss = tf.reduce_mean(tf.square(y-y_data))

#传播误差
optimiter = tf.compat.v1.train.GradientDescentOptimizer(0.5)
train = optimiter.minimize(loss)

