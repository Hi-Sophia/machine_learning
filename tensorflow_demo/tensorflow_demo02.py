import tensorflow as tf

'''
TensorFlow介绍：
TensorFlow是一个采用数据流图（data flow graphs），用于数值计算的开源软件库
Tensor（张量）意味着N维数组，Flow（流）意味着基于数据流图的计算。
Tensorflow运行过程就是张量从图的一端流动到另一端的计算过程


TensorFlow基本用法：
使用图(graph)来表示计算任务；
在会话(session)的上下文中执行图；
使用tensor表示数据；
通过变量(Variable)来维护状态 ；
使用feed和fetch可以为任意的操作(Operation/op)赋值或者从其中获取数据。


张量（Tensor):
张量有多种. 零阶张量为纯量或标量 (scalar) 也就是一个数值. 比如 [1]
一阶张量为 向量 (vector), 比如 一维的 [1, 2, 3]
二阶张量为 矩阵 (matrix), 比如 二维的 [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
'''


# 使用tf.name_scope在hidden命名域下定义了三个操作
with tf.name_scope('hidden') as scope:
  a = tf.constant(5, name='alpha')
  W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0), name='weights')
  b = tf.Variable(tf.zeros([1]), name='biases')