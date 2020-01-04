
f = open("record.txt")

'''
一、文件的读取和定位 【'r' 只读 'b' 二进制模式】
文件的写入 【'w' 覆盖  'a' 追加】
'''
#按字节为单位读取，不设置参数，文件指针指向文件末尾
f.read()

#当前文件指针的位置
f.tell()

#调整文件指针的位置
f.seek(0,0)

#在文件中读取一行
f.readline()

#迭代读取文本文件的每一行
for each_line in f:
    print(each_line.strip().split("\t"))
exit()
''' write'''

f = open("record.txt",'a')
f.write("I want to fly")

#文件关闭 python会缓存写入的数据，写入操作必须关闭文件
f.close()


'''
二、OS模块【文件系统的访问】
'''
import os

#返回当前工作目录 current working directory
os.getcwd()

#改变当前工作目录
#os.chdir("/Users/wujuhong/PycharmProjects/code/a1_python_lib")

#列举指定目录的文件名
os.listdir("python_basic")

#使用系统自带的小工具 如calc计算器
os.system("calc")

#遍历指定路径下的所有子目录
for i in os.walk("/Users/wujuhong/PycharmProjects/code"):
    print(i)

'''
三、pickle模块【把python对象转化为二进制形式存储 -- pickling】
dump 保存数据   load 加载数据
'''

import pickle

#保存数据
my_list = [123,3.14,'小甲鱼',['another list']]
pickle_file = open('/Users/wujuhong/PycharmProjects/code/machine_learning_xx/python_basic/my_list.pkl','wb')
pickle.dump(my_list,pickle_file)
pickle_file.close()

#加载数据
pickle_file = open('/Users/wujuhong/PycharmProjects/code/machine_learning_xx/python_basic/my_list.pkl','rb')
my_list=pickle.load(pickle_file)
print(my_list)


