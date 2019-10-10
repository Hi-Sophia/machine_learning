# 摄氏度转换为华氏度
def c2f(cel):
    fah = cel * 1.8 + 32
    return fah


# 华氏度转换为摄氏度
def f2c(fah):
    cel = (fah - 32) / 1.8
    return cel

def test():
    print("测试，0摄氏度=%.2f华氏度" % c2f(0))
    print("测试，0华氏度=%.2f摄氏度" % f2c(0))

if __name__ == '__name__':
    test()