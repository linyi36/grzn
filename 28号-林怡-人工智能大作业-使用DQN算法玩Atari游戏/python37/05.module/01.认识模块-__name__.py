'''
模块(module)
    1.模块化,模块化将一个完整的程序分解为一个一个小的模块(适合大型程序的多人开发&&维护,模块可以复用)
        通过将模块组合,来搭建出一个完整的程序
    2.不采用模块化,统一将所有代码写一个文件里头

在Python中一个py文件就是一个模块.创建一个模块本质上就是创建一个python文件
注意:模块名要符合标识符的规范

Q:如何在一个模块中引入外部模块?
A:import 模块名(就是python文件的名字,不包含后缀) as 别名
'''
'''我们可以引用多次,但是模块实例只会创建一个------单例模式'''
import module_demo
import module_demo
import module_demo as demo # 给模块起别名
print(module_demo) #默认打印绝对路径
'''在每一模块内部都有一个__name__属性,通过这个属性可以获取到模块的名字
有一个特殊的模块叫主模块,就是直接通过python执行的模块,它的__name__就叫__main__
'''
print(demo.__name__)
print(__name__) #__main__  程序执行的入口__
variables=locals()
print("end")