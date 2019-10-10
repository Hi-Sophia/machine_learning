'''
Python所有的函数都有返回值,默认返回 return None
1、创建函数
2、调用函数
3、函数的参数
形参【变量名】：函数创建过程中小括号中的参数
实参【具体内容】：函数被调用过程中传入的参数
4、函数的返回值
5、函数文档      【函数名.__doc__ 、 help(函数名)】
6、关键字参数：在传入实参时指定形参的变量名 【add(num1=5,num2=3)】
7、可变参数（收集参数）：
 python将其打包为一个元祖
 ** 将参数打包成 字典 形式
'''


def add(num1, num2):
    '''

    :param num1: 参数1
    :param num2: 参数2
    :return: 和
    '''
    return num1 + num2


# print(add(1, 2))
# print(add.__doc__)
# print(help(add))
# print(add(num1=5, num2=3))

'''

函数中定义的参数以及变量，都是局部变量
在函数内部试图修改全局变量，Python会创建一个名字相同的新的局部变量代替【函数内部不要修改全局变量，仅仅使用即可】


1、global 在函数内修改全局变量
2、内嵌函数：允许在函数内部创建另一个函数 【内部函数的作用域在外部函数内】
3、闭包：内部函数对外部函数的变量进行引用【只能访问不能修改】，内部函数就被认为是闭包
nonlocal 在内部函数中修改外部函数的局部变量的值

4、lambda表达式：创建匿名函数
'''

# 1、global 在函数内修改全局变量
count = 5


def myFun():
    global count
    count = 10
    print(count)


myFun()
print(count)


# 2、允许在函数内部创建另一个函数 【内部函数的作用域在外部函数内】
def fun1():
    print("fun1正在被调用")

    def fun2():
        print("fun2正在被调用")

    fun2()


fun1()


# 3、闭包：内部函数对外部函数的变量进行引用【只能访问不能修改】，内部函数就被认为是闭包
def funX(x):
    def funY(y):
        return x * y

    return funY


print(funX(5)(8))


# nonlocal 在内部函数中修改外部函数的局部变量的值
def funOuter():
    x = 5

    def funInner():
        nonlocal x
        x = x * x
        return x

    return funInner()


print(funOuter())

# lambda表达式：创建匿名函数
g = lambda x: x * 5 + 1

add = lambda x, y: x + y
print(g(2))
print(add(1, 2))

'''
内建函数
1、filter():过滤器
2、map()：返回加工后的元素构成的新序列

'''

temp = filter(None, [0, 1, False, True])
odd = filter(lambda x: x % 2, range(10))
print(list(temp))
print(list(odd))


new_num = map(lambda x:x*2,range(10))
print(list(new_num))




