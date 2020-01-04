一、TensorFlow简介：

TensorFlow使用数据流图进行数值计算的开源软件库

1、节点：被称为 *op* (operation 的缩写)，表示数学运算。也可以表示数据输入的起点和输出的终点，或者是读取/写入持久变量（persistent variable）的终点

2、边：代表在节点之间传递的多维数组（tensor 张量）

3、TensorFlow 程序通常被组织成一个**构建阶段**和一个**执行阶段**. 在构建阶段, o**p 的执行步骤被描述成一个图**. 在执行阶段, **使用会话执行执行图中的 op**

4、TensorFlow支持三种数据类型：常量、变量、占位符

```python
#变量在使用前必须进行初始化
a = tf.get_variable(name='v1',initializer=tf.constant(2))

#variable需要初始化
init = tf.global_variables_initializer()

#数据类型转换
A = tf.cast(A, tf.float64)

#矩阵连接操作，在大型神经网络中用的比较多
AA0 = tf.concat([A, A], axis=0)
```

  在神经网络中，变量一般可作为储存权重和其他信息的矩阵，而常量可用来储存超参数或其他结构信息 

5、tf.random

```python
tf.random.normal([2,3],stddev=1,seed=1)

#截断正态分布随机数，它只保留[mean-2*stddev,mean+2*stddev]范围内的随机数。
tf.random.truncated_normal() 
```

二、DataSet与Iterator

  Dataset可以看作是相同类型“元素”的有序列表。 

三、  TensorBoard

为了帮助你了解模型中张量的流动，以便调试和优化模型 

- 使用tf.get_default_graph()调用计算图，返回程序的默认计算图
- 将计算图设置为sess.graph，返回会话的计算【常用】

```python
tf.summary.histogram('W', W)
tf.summary.scalar('loss', loss)
merged = tf.summary.merge_all()

train_writer = tf.summary.FileWriter("mnist-logdir", sess.graph)

for itr in range(1000):
    if itr % 10 == 0:
        summary = sess.run(merged, 
                           feed_dict={x: batch_xs,
                                        label: batch_ys})
        train_writer.add_summary(summary, itr)

#查看命令
tensorboard --logdir ./graphs  
```

四、参数存储与加载

```python
#在构建计算图后调用,将TensorFlow模型保存为.ckpt 格式的文件
saver = tf.train.Saver() 
with tf.Session() as sess:
    # 保存模型到model文件夹下，
    saver.save(sess, "model/textrnn")
    #1、恢复
    saver.restore(sess, "model/textrnn")
    #2、恢复
    saver.restore(session, tf.train.latest_checkpoint('model/textrnn'))

```

