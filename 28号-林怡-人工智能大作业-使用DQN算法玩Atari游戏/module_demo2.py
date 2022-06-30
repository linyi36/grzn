a=10
b=20
_c =30 #添加了下划线的变量不能被其他模块访问
def fun():
    print("I am fun")

class MyClass():
    def __init__(self):
        print(__name__+":...__init__...")

def test():
    print("这是测试代码,在被其他模块引用时不要执行")

if __name__=='__main__':
    test()