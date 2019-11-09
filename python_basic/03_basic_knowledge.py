
'''
一、变量
'''

'''
二、字符串:
1、使用（\）对字符串中的引号进行转义
2、原始字符串:在字符串前面加一个英文字符r，不能以反斜杠作为结尾
3、长字符串:三重单引号
'''
'Let\'s go'
"Let's go"

string = r"C:\now"

long_str = '''
从明天起，做一个幸福的人
喂马,劈材,周游世界
从明天起，关心粮食和蔬菜
'''

'''
三、数据类型
类型转换：int()、float()、str()
获得关于类型的信息：type(num_test)  isinstance(num_test,int)
'''
num_test = 520
type(num_test)
isinstance(num_test,int)


'''
四、常见操作符
'''


[i**i for i in range(3)]


a = 1
try:
    a += 1
except:
    a += 1
else:
    a += 1
finally:
    a += 1
print(a)


x = "foo"
y = 2
print(x+y)

x=1
def change(a):
    x+=1
    print(x)
change(x)

import copy
a = [1,2,3,4,['a','b']]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
a.append(5)
a[4].append('c')


x= 43
ch = "A"
y = 1
(x >= y and ch < 'b' and y)


dict = {[1,2,3]:'345'}

[3] in [1,2,3,4]


