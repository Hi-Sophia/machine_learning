'''
模块的作用：
封装组织python代码
实现代码的重用

if __name__ == '__name__':
    test()
'''

import import_module as fc
from import_module import f2c, c2f

print(fc.c2f(32))
print(fc.f2c(99))

print("测试，32摄氏度=%.2f华氏度" % c2f(32))
print("测试，99华氏度=%.2f摄氏度" % f2c(99))

'''
搜索路径
'''
import sys
sys.path

'''
timeit 计时模块

dir()函数 查询该模块定义了哪些变量、函数和类
__doc__ 查看模块简介
__all__获得可调用接口的信息
__file__ 指明了该模块源码的位置
help:查看帮助信息

'''
import timeit

# print(timeit.__doc__)
print(dir(timeit))
print(timeit.__all__)
print(timeit.__file__)
# print(help(timeit))
