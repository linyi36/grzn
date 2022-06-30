import module_demo2 as m2
print(m2.a+m2.b)
a=m2.MyClass()
m2.fun()

''' from 模块名 import 变量,方法,类 ------这种方式就不用老师...了,方便不少'''
from module_demo2 import MyClass as myclass
from module_demo2 import * # 引入到模块中所有的内容,一般不会使用,就相当于复制...这可能会导致主模块里头的一些同名变量\函数\类覆盖
mc=MyClass()

varibles=locals()
print("end")

'''import 小结
import xxx 
import xxx as yyy 
from xxx import yyy,zzz,fff 
from xxx import*
from xxx import yyy as zd
'''