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

