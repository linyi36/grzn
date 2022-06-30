'''
*和** 用于函数define时的形参:
    *:以positon arg的方式接受实参(可以有**,),将传递的实参封装成一个tuple(装包)
    **:以keyword arg的方式接受实参(因此没有**number),将传递的实参封装成一个dict(装包)

*和** 用于函数call时的形参:
    如果一个函数定义时指定了多个形式参数,用*或者**传递一个实际参数就可以代表多个参数了.
'''


# 1.*和** 用于函数define时的形参(装包):
def sum_pack1(*number):# *用于函数define时的形参
    res = 0
    for i in number:
        res += i
    print(res)
    print(type(number))


print(sum_pack1(1, 2, 3, 4, 5))  # 函数返回值默认为None


def sum_pack2(**kwargs):# **用于函数define时的形参
    res=0
    for i in kwargs:
        res+=kwargs[i]
    print(res)
    print(type(kwargs))
sum_pack2(a=11,b=22,c=33)


# 2.*和** 用于函数call时的形参(拆包):
def unpack(a, b, c):
    print(locals())


tuple = (1, 2, 3)
unpack(*tuple)
dict = {"a": 10, "b": 20, "c": 30}
unpack(**dict)
