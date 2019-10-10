'''
一、List(列表)：
数据类型可以不一致
列表里面可以包含另一个列表 in not in 只能判断一个层次的成员关系
1、创建列表
2、添加
3、获取
4、删除
5、分片:建立原列表的一个拷贝
*号：复制自身若干次
'''

number = [1, 2, 3, 4, 5]
number.append(6)  # 向列表末尾添加一个元素
number.extend([7, 8])  # 向列表末尾添加多个元素
number.insert(0, 0)  # 向列表指定位置添加元素

number[2]  # 获取指定位置元素
number[2], number[4] = number[4], number[2]  # 元素位置互调

number.remove(1)  # 根据元素名称删除，元素不在列表会报错
del number[1]  # 删除指定位置元素
del number  # 删除整个列表
number.pop()  # 弹出列表中最后一个元素

number[1:3]
number[0:5:2]  # 等价于 number[::2]
number[::-1]  # 反转一个列表
'''
二、tuple(元组)：不可改变
'''

tuple_01 = (1, 2, 3, 4, 5)
tuple_02 = (1,) #创建的元组只有一个元素加，