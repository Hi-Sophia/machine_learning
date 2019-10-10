import pandas as pd

'''
pandas可以读取与存取的资料格式有很多种，像csv、excel、json、html与pickle等
'''

data = pd.read_csv("/Users/wujuhong/PycharmProjects/code/machine_learning_xx/pandas_demo/student.csv")
print(data)


data.to_pickle("/Users/wujuhong/PycharmProjects/code/machine_learning_xx/pandas_demo/student.pickle")