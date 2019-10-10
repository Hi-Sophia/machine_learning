'''
一、三元操作符语法 a = x if 条件 else y
'''

def fun_branch(x, y):
    if x < y:
        small = x
    else:
        small = y

    small = x if x < y else y


'''
二、for 循环语句
'''
fruit = 'apple'
for each in fruit:
    print(each)

for i in range(1, 10, 2):
    print(i)
