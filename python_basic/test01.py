import numpy as np
import urllib

def adder(x):
    def wrapper(y):
        return x + y

    return wrapper


adder5 = adder(5)
print(adder5(adder5(6)))

a = np.repeat(np.arange(5).reshape([1, -1]), 10, axis=0) + 10.0  # np.repeat(a,b) 将a重复b次
b = np.random.randint(5, size=a.shape)  #生成（0，5）随机矩阵，大小和矩阵a相同
c = np.argmin(a * b, axis=1) #矩阵a b相乘，返回每行最小值位置
b = np.zeros(a.shape) #与矩阵a相同的全零矩阵
b[np.arange(b.shape[0]), c] = 1 #b中所有c返回位置置为1


urllib.quote()





