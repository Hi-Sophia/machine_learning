import tensorflow as tf
import numpy as np
import tensorflow.contrib.eager as tfe

'''
1、创建dataset
dataset可以看作是相同类型元素的有序列表。
切分传入Tensor的第一个维度，生成相应的dataset
'''
# 1、创建一个简单的dataset,Dataset的每一个元素是一个数字
dataSet = tf.data.Dataset.from_tensor_slices(np.array([1.0, 2.0, 3.0, 4.0, 5.0]))

#2、让每个元素是一个字典，这时函数会分别切分'a'中的数值以及'b'中的数值
dataset = tf.data.Dataset.from_tensor_slices(
    {
        "a": np.array([1.0, 2.0, 3.0, 4.0, 5.0]),
        "b": np.random.uniform(size=(5, 2))
    }
)

'''
2、在非Eager模式下，读取dataset中元素
'''
# 从dataSet中实例化一个iterator,one_shot_iterator只能从头到尾读一次
iterator = dataSet.make_one_shot_iterator()
# get_next 从iterator里取出一个元素
one_element = iterator.get_next()  # tensor，并不是一个实际的值
with tf.Session() as sess:
    for i in range(5):
        # 真正地取出值
        print(sess.run(one_element))

'''
3、eager模式 
通过tfe.Iterator(dataset) 的形式直接创建Iterator并迭代
'''
import tensorflow as tf

# 程序启动时调用
tfe.enable_eager_execution()

dataSet = tf.data.Dataset.from_tensor_slices(np.array([1.0, 2.0, 3.0, 4.0, 5.0]))

for one_element in tfe.Iterator(dataSet):
    print(one_element)

'''
4、dataset中的元素做变换
常用的Transformation有：map batch shuffle repeat
'''
# #map接收函数
# dataSet.map(lambda x: x + 1)
#
# #将多个元素组合成batch
# dataSet.batch(32)
#
# #打乱dataSet中的元素，buffer_size打乱时使用的buffer大小
# dataSet.shuffle(buffer_size=10000)
#
# #将整个序列重复多次，主要用来处理机器学习中的epochepoch
# dataSet.repeat(5)
