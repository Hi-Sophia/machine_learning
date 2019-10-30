import tensorflow as tf

mat1 = tf.constant([3, 3], dtype=tf.float32, shape=[1, 2])
mat2 = tf.constant([[2.], [2.]])

product = tf.matmul(mat1, mat2)

# 启动默认图
sess = tf.Session()
result = sess.run(product)
print("type:{}.value:{}".format(type(result), result))

#使用with代码块，自动完成关闭操作
with tf.Session() as sess2:
    result2 = sess2.run([product])
    print(result2)


    

a = tf.constant(4.0)
print("a在默认图:{}".format(a.graph is tf.get_default_graph()))

g = tf.Graph()

with g.as_default():
    b = tf.constant(3.0)
    c = tf.constant(5.0)
    print("b在图g上：{}".format(b.graph is g))
    print("c在图g上：{}".format(c.graph is g))

d = tf.constant(5.0)
print("d在默认图:{}".format(d.graph is tf.get_default_graph()))

with tf.Graph().as_default() as g2:
    e = tf.constant(6.0)
    print("e在图g2上：{}".format(e.graph is g2))
