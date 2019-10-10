import pandas as pd
import numpy as np

'''
1、赋值：
根据loc和iloc设置值 
根据条件设置值
按行或列设置 

2、缺失值删除： df1.dropna(how='any') 
3、缺失值填充： df1.fillna(value=5)

4、null
pd.isnull(df1) #NaN:True 其余为：False
pd.isna(df1)  #NaN:True 其余为：False
'''
dates = pd.date_range('20191001', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=dates)
df['F'] = s1  # 添加新列将自动根据索引对齐数据
df.at[dates[0], 'A'] = 0  # 通过标签赋值
df.iat[0, 1] = 0  # 通过位置赋值：

df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])  # 重建索引
df1.iloc[0:2, 5] = 1  # 赋值

'''
Pandas 处理丢失数据
'''
df1.dropna(how='any')  # 删除任何带有缺失值的行
df1.fillna(value=5)  # 填充缺失值

pd.isnull(df1)  # NaN:True 其余为：False
pd.isna(df1)  # NaN:True 其余为：False

'''
contact 行级合并 axis=0(默认)
'''
rowMerge = pd.DataFrame(np.random.randn(5, 4))
pd.concat([rowMerge[:1], rowMerge[2:4], rowMerge[4:]], ignore_index=True) #ignore_index (重置 index)

'''
merge 列级合并 SQL风格的合并
'''
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                             'A': ['A0', 'A1', 'A2', 'A3'],
                             'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                              'C': ['C0', 'C1', 'C2', 'C3'],
                              'D': ['D0', 'D1', 'D2', 'D3']})
pd.merge(left, right, on='key')
