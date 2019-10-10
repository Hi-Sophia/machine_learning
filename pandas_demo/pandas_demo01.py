import numpy as np
import pandas as pd

'''
pandas两个主要的数据结构：Series 一维数组、DataFrame 二维矩阵
Pandas会自动创建一个默认的整数索引
Pandas的每一列的数据类型都是相同的
'''

# Pandas会自动创建一个0到N-1（N为长度）的整数型索引
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

#构造时间数据集
dates = pd.date_range('20191001', periods=6)
print(dates)

# index指定索引   columns指定列名
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2.dtypes)

# 2、查看数据
df.head()
df.tail(3)

df.index  # 显示索引
df.columns  # 显示列
df.values # 查看值

df.describe()  # 显示数据的快速统计摘要
df.T  # 转置数据

df.sort_index(axis=1, ascending=False) #按轴排序
df.sort_values(by='B') #按值排序


'''
3、选择
loc 按照标签选择
iloc 按照位置选择
'''
# 获取A列数据(包含索引)
df['A']
df.A

#通过[]选择，对行进行切片
df[0:3]  #行标索引
df['2019-10-01':'2019-10-03']  #预定义index方式


# loc 按照标签选择
df.loc[dates[0]]  #通过标签获取第一行数据
df.loc[:,['A','B']]  #通过标签在多轴上选择数据
df.loc['2019-10-01':'2019-10-03',['A','B']] #在两个轴上同时切片

df.loc[dates[0], 'A']  #获取标量值
df.at[dates[0], 'A']


# iloc 按照位置选择
df.iloc[3] #第四行元素
df.iloc[3:5,0:2]
df.iloc[[1, 2, 4], [0, 2]]
df.iloc[1:3, :]  #整行切片
df.iloc[:, 1:3]  #整列切片

df.iloc[0, 1]  #获取标量值
df.iat[0, 1]

#通过判断的筛选
df[df.A > 8]