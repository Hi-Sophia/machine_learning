import tensorflow as tf
'''
TensorBoard的创建是为了帮助你了解模型中张量的流动，以便调试和优化模型

TensorFlow图表有两种连接关系：数据依赖和控制依赖。
数据依赖显示两个操作之间的tensor流程，用实心箭头指示,控制依赖用点线表示
 
 参考：http://www.tensorfly.cn/tfdoc/how_tos/summaries_and_tensorboard.html

tf.get_default_graph() 调用计算图，返回程序的默认计算图
sess.graph graph，返回会话的计算图【常用】

writer = tf.summary.FileWriter(logdir ,graph)

'''


a = tf.constant(2)
b = tf.constant(3)
c = tf.add(a,b)

#writer = tf.summary.FileWriter('./graphs',tf.get_default_graph())

with tf.Session() as sess:
    writer = tf.summary.FileWriter('./graphs' ,sess.graph)
    print(sess.run(c))

    writer.close()


'''
tensorboard --logdir=/Users/wujuhong/Pycharmojects/code/machine_learning/tensorflow_demo/graphs
'''