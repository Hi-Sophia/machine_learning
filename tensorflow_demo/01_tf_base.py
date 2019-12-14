import tensorflow as tf
'''
定义计算操作
'''
# a = 2
a = tf.constant(2)
# b = 3
b = tf.constant(3)
c = tf.add(a,b)
# c = tf.add(a, b, name="Add")  # 每个节点以零或更多张量为输入，并生成一个张量作为输出
print(c)

'''
打开一个会话（session）来运行整个计算图
在会话中，我们可以将所有计算分配到可用的CPU 和GPU 资源中
'''
# sess = tf.Session()
# print(sess.run(c))
# sess.close()


'''
TensorFlow中最基本的单位是常量（Constant）、变量（Variable）和占位符（Placeholder）
常量定义后值和维度不可变，变量定义后值可变而维度不可变。
在神经网络中，常量可作为储存超参数或其他结构信息的变量,变量一般可作为储存权重和其他信息的矩阵。
'''

# 该变量的值服从标准差为1 的正态分布，并随机生成。
# tf.truncated_normal()函数，即截断正态分布随机数，它只保留[mean2*stddev,mean+2*stddev]范围内的随机数。
# w1 = tf.Variable(tf.random.normal([2, 3], stddev=1.0, seed=1))
#
# a = tf.compat.v1.global_variables( initializer=tf.constant(2))
# b = tf.compat.v1.global_variables(initializer=tf.constant(3))
# c = tf.add(a, b, name="Add")
#
# tf.initialize_all_variables()
#
#
# with tf.compat.v1.Session() as sess:
#     print(sess.run(a))
#     print(sess.run(b))
#     print(sess.run(c))



