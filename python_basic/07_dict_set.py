'''
字典
'''

# 创建字典
dict_empty = {}

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('one', 1), ('two', 2), ('three', 3)])
e = dict({'one': 1, 'two': 2, 'three': 3})

f = dict((('one', 1), ('two', 2), ('three', 3)))

a == b == c == d == e

dict_01 = dict((('F', 70), ('C', 67)))
dict_01['A'] = 50  # 键值存在覆盖，键值不存在创建并赋值

'''
各种内置方法
1、fromkeys()
2、keys() values() items()
3、get()
4、copy()
5、ll.pop('aa')  ll.popitem()
6、update()
7、** 收集参数两种打包方式：元组，字典
'''
dict_02 = {}
# 创建并返回一个新的字典
dict_03 = dict_02.fromkeys((1, 2, 3))

dict_03.keys()
dict_03.values()
dict_03.items()


dict_03.get(4)
dict_03.get(4,'木有')

a = {'姓名':'小甲鱼'}
b = a
a.clear()


ll = {'one': 1, 'two': 2, 'three': 3}
ll.pop('two')
ll.popitem()
'''
集合:唯一且无序
'''

# 创建集合
set_01 = {1, 2, 2, 3, 3, 4}
set_02 = set([1, 2, 2, 3, 3, 4])

# 访问集合
for each in set_01:
    print(each)

0 in set_01  # False
set_01.add(5)
set_01.remove(5)

# 不可变集合 frozenset()
set_03 = frozenset({1, 2, 3, 4, 5, 5})
set_03.add(6)  # AttributeError: 'frozenset' object has no attribute 'add'
