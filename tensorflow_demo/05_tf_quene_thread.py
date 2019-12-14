import tensorflow as tf

'''
1、在使用TensorFlow进行异步计算时，队列是一种强大的机制。
队列就是TensorFlow图中的节点。这是一种有状态的节点，就像变量一样：其他节点可以修改它的内容。
具体来说，其他节点可以把新元素插入到队列后端(rear)，也可以把队列前端(front)的元素删除

2、tf常见队列：
FIFOQueue：先进先出队列
RandomShuffleQueue：随机混淆队列

3、队列使用常见结构：
多个线程准备训练样本，并且把这些样本推入队列。
一个训练线程执行一个训练操作，此操作会从队列中移除最小批次的样本（mini-batches)。

4、TensorFlow的Session对象是可以支持多线程的，因此多个线程可以很方便地使用同一个会话（Session）并且并行地执行操作。
然而，在Python程序实现这样的并行运算却并不容易。
所有线程都必须能被同步终止，异常必须能被正确捕获并报告，回话终止的时候， 队列必须能被正确地关闭

5、Coordinator类:用来帮助多个线程协同工作，多个线程同步终止。 其主要方法有：
should_stop():如果线程应该停止则返回True。
request_stop(<exception>): 请求该线程停止。
join(<list of threads>):等待被指定的线程终止。

首先创建一个Coordinator对象，然后建立一些使用Coordinator对象的线程。
这些线程通常一直循环运行，一直到should_stop()返回True时停止。 
任何线程都可以决定计算什么时候应该停止。它只需要调用request_stop()，同时其他线程的should_stop()将会返回True，然后都停下来


6、QueueRunner类：会创建一组线程，这些线程可以重复的执行Enquene操作， 他们使用同一个Coordinator来处理线程同步终止。
此外，一个QueueRunner会运行一个closer thread，当Coordinator收到异常报告时，这个closer thread会自动关闭队列
'''