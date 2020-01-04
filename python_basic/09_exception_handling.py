'''
常见的异常：
FileNotFoundError
ZeroDivisionError【5/0】
TypeError【1+'1'】

一、文件打开异常处理
'''
try:
    f = open('record.txt', 'r')
    print("文件的内容是：")

    for each_line in f:
        print(each_line)

# 1、针对不同异常设置多个except
except OSError as reason:
    print("文件打开的过程中出错了... 原因是：" + str(reason))
except TypeError as reason:
    print("类型出错了...原因是：" + str(reason))
# 2、对多个异常统一处理
except (OSError, TypeError) as reason:
    print("出错了...原因是:" + str(reason))
# 3、捕获所有异常
except:
    print("出错了...")
finally:
    f.close()

'''
raise语句抛出一个异常
with语句自动帮你关闭文件【再也不用担心文件打开关闭的问题】
'''
raise ZeroDivisionError('除数不能为0')

try:
    with open("record.txt", 'r') as f:
        for each_line in f:
            print(each_line)
except OSError as reason:
    print("文件打开的过程中出错了... 原因是：" + str(reason))

'''
丰富的else语句
1、与for、while循环语句配合使用，else语句只在循环完成后执行【break跳出循环，else中的语句不会执行】
2、try语句块中没有出现异常，执行else语句块里的内容
'''


def showMaxFactor(num=15):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print("%d的最大公约数是%d" % (num, count))
            break
        count = count - 1
    else:
        print("%d是素数：" % num)


try:
    int('abc')
except ValueError as reason:
    print("出错了,原因是:" + str(reason))
else:
    print("没有任何异常")
