一、pandas

1、pd.set_option参数设置

```python
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)
```

2、pd.get_dummies：利用pandas实现one hot encode的方式

  【等同于sklearn中preprocessing.OneHotEncoder()】

```python
dummies_Embarked = pd.get_dummies(data_train['Embarked'], prefix= 'Embarked')
```

3、pd.merge(df, temp, on=['Sex'], how='left')  #合并

4、pd.cut()：离散化

```python
ages=[20,19,30,34,23,40,50]
discrete_ages=pd.Series(ages)
bin=[0,18,25,35,60]
discrete=pd.cut(se_ages,bin) #离散化
#value_counts可以对Series里面的每个值进行计数并且排序
pd.value_counts(discrete)  #离散化后的分组进行计数
```

二、dataframe

1、df.columns：看列名

2、df.info()：看每列性质【空值、类型】

```python
'''
问题：
1、空值填充
   缺失值可以删除处理
   若缺失值对于结果有比较大的影响可以通过赋值处理【训练模型，预测结果】
2、类别型数据(特征离散化)
   数据类型是object，也就是字符类型数据，转换为数值型数据
   统计字符类型数据，一些列中包含的字符类比较多，这些数据是不适合做分类算法的，需要将其剔除
3、特征抽取
   df.filter():抽取需要的特征
3、异常值处理与归一化
'''
```

3、df.describe()：看每列统计信息

4、df.as_matrix()|df.values：pandas的DataFrame转换为numpy中的ndarray

5、df.drop

6、df.filter(regex='Survived|SibSp|Parch')：正则方式过滤Survived|SibSp|Parch列

```python
df.filter(items=['one', 'three'])
df.filter(regex='e$', axis=1)
df.filter(like='bbi', axis=0)
```

7、df.groupby('A').mean()：按A列分组（groupby），获取其他列的均值

```python
#按Sex列分组，获取Age列的均值
df.groupby(['Sex'], as_index=False)['Age'].mean()
```

8、df.apply()：应用在dataframe的行或列中:

<https://stackoverflow.com/questions/32617811/imputation-of-missing-values-for-categories-in-pandas>

```python
#use most frequent, it is general for discrete and continues data
df = data_train.apply(lambda x:x.fillna(x.value_counts().index[0]))
```



