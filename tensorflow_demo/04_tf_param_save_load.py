import os
import tensorflow as tf
import numpy as np

'''
参数存储与加载:
tf.train.Saver():在构建计算图后调用,将TensorFlow模型保存为.ckpt 格式的文件
saver.save():在训练结束时调用,保存变量
saver.restore():恢复参数：

一般该文件目录下会有三个文件，
第一个model.ckpt.meta 保存了TensorFlow计算图的结构，
第二个model.ckpt 文件保存了TensorFlow 中每一个变量的取值，
而最后一个cheekpoint 文件保存了同目录下所有的模型文件列表
'''

#1、保存变量
v1 = tf.Variable(tf.constant(1.0),name='v1')
v2 = tf.Variable(tf.constant(2.0), name="v2")

result = tf.add(v1,v2)
init_op = tf.initialize_all_variables()

saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(init_op)
    #保存模型到model文件夹下，
    saver.save(sess,"./my-model/model")


# 2、模型提取
# v1 = tf.Variable(tf.constant(1.0), name='v1')
# v2 = tf.Variable(tf.constant(2.0), name="v2")
#
# result = tf.add(v1, v2)
# saver = tf.train.Saver()
#
# with tf.Session() as sess:
#     # 保存模型到model文件夹下，
#     saver.restore(sess, "./my-model/model")
#     print(sess.run(result))
