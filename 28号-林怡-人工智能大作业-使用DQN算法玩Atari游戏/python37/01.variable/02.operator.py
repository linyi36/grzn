'''Reference: https://www.runoob.com/python3/python3-basic-operators.html '''
'''Arithmetic operator: + - * / % ** //'''
a = 21
b = 10
add = a + b
sub = a - b
mul = a * b
div1 = a / b
mod = a % b
div2 = a // b
pow = 2 ** 10
'''Assignment Operator: += -= /= %= //= **= 
tips: if python3.8 :=海象运算符 '''

'''Bit Operators : & | ^ ~ >> <<'''
a = 0b_0011_1100
b = 0b_0000_1101
andRes = a & b
orRes = a | b
xorRes = a ^ b
notRes = ~a  # 全0为0,全1为-1,因为循环
rightScrollRes = a >> 1
leftScrollRes = a << 1
'''Compare Operators: > < == != >= <= '''
'''Logical Operators: and or not '''

'''member Operators && id Operators:
in	    如果在指定的序列中找到值返回 True，否则返回 False。	        x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	    x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。

is	    is 是判断两个标识符是不是引用自一个对象	    x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
is not	is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
'''

print("end")
