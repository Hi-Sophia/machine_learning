pip install -i https://pypi.tuna.tsinghua.edu.cn/simple gensim 

1、for..in..if语法

```python
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

[i**i for i in range(3)] #[1, 1, 4]
[x for x in foo if x % 3 == 0] #[18, 9, 24, 12, 27]

```

2、lambda表达式

```python
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
list(filter(lambda x: x % 3 == 0, foo)) #[18, 9, 24, 12, 27]
list(map(lambda x: x * 2 + 10, foo)) #[14, 46, 28, 54, 44, 58, 26, 34, 64]
```

3、python中yield使用：<https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/>

4、sys.argv[ ]其实就是一个列表，里边的项为用户输入的参数，参数是从程序外部输入的。

5、统计最常出现的词

```python
import collections
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
print(collections.Counter(colors).most_common(2))
#[('blue', 3), ('red', 2)]
```

6、join() ：将序列中的元素以指定的字符连接生成一个新的字符串。

```python
str = "+"
seq = ("a", "b", "c") # 字符串序列
print(str.join(seq)) #a+b+c
```

