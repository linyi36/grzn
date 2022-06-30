'''basic knowledge
    函数定义时的参数叫做形式参数(简称"形参"),函数调用时传递的参数叫做实际参数(简称"实参")
    函数调用时,实参-->形参的映射方式有两种:1.位置参数;2.关键字参数.
    Q:positon arg和keyword arg的本质区别是什么?
    A:position arg是默认传参规则,keyword arg是显式自定义传参规则
'''


def arg_position_keyword(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    print(arg3)
# (1)函数调用的正确示范
'''
pure position arg
'''
arg_position_keyword(1, 5, 3)

'''
position arg + keyword arg
'''
arg_position_keyword(1, arg2="I am arg2", arg3="I am arg3")  # keyword arg
arg_position_keyword(1, arg3="I am arg2", arg2="I am arg3")  # keyword arg

# (2)函数调用的错误示范
'''error 1
当混用两种参数映射方式时,position arg应该放在前面一部分,keyword arg应该放在后面一部分,不要交叉感染
 keyword arg should follows position arg
'''
# arg_position_keyword(1, arg2="I am arg2", 5)
# arg_position_keyword(arg2="I am arg2",1,5)
'''error 2
当混用两种参数映射方式时,放在前面的position arg只能赋值给前面对应的形参,python应该是不支持先用keyword arg赋值,再只能用position arg赋值的
TypeError: got multiple values for argument 'xxx'
'''
# arg_position_keyword(3, arg2="I am arg2", arg1="I am arg1")



'''summary:position arg && keyword arg的调用机制
1.将传递实参分为两部分,前部是position arg,后部是keyword arg
2.首先position arg会依次传递到对应的形参前部(有序)
3.然后由keyword arg来自定义传递到对应名称的形参后部(无序)
'''
