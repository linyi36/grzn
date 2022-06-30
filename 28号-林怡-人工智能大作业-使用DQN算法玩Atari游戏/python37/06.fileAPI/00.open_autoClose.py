'''
open(file,mode='r,buffering=-1,encoding=None,errors=None,newline=None,closefd=True,opener=None)
使用open函数打开一个文件
    file:要打开的文件的绝对路径或者相对路径(相对于执行程序的py文件)
'''

file_name = 'text_en.txt'
'''tips:在windows中的路径分隔符使用\\或者/来代替'''
# file_name = '../01.variable/01.locals().py' # ok line ,转义字符串
# file_name= r'..\01.variable\01.locals().py' # ok line ,非转义的原始字符串
# file_name = 'D:/code/Python_WorkSpace/learnDQN/python37/01.variable/01.locals().py'  # ok line ,绝对路径
# file_name = 'demoNoExist.txt' #error line
file_obj = open(file_name)
print(file_obj)
''' with ... as ... 语句 '''
with open(file_name) as file_obj2:
    '''在with 语句中可以直接使用file_obj进行文件操作'''
    print(file_obj2.read())

    '''with结束则文件close,无法进行文件操作了'''
# print(file_obj2.read()) # error : file_obj2在with结束后就会自动关闭


'''添加异常体系的文件打开,操作和关闭'''
try:
    print("---exception---")
    file_name3 = 'demoNoExist.txt'
    with open(file_name3) as file_obj3:
        print(file_obj3.read())
except FileNotFoundError:
    print(f'{file_name3}文件不存在')  # f''表示格式化,https://blog.csdn.net/qq_35290785/article/details/90634344

'''读取中文文件的注意事项:设置encoding,否则会报错
调用open()来打开一个文件,可以将文件分成两种类型:
一种是纯文本文件(使用utf-8等编码编写的文本文件);
一种是二进制文件(图片、mp3、ppt等这些文件)
open()打开文件时,默认是以文本文件的只读形式打开的---即 mode='rt' #read text
'''

try:
    print('---读取中文文件的注意事项:设置encoding,否则会报错---')
    file_name4 = "text_zh.txt"
    # with open(file_name4) as file_obj4: # UnicodeDecodeError: 'gbk' codec can't decode byte 0xa6 in position 4: illegal multibyte sequence
    with open(file_name4, encoding='utf8') as file_obj4:
        ''''''
        print(file_obj4.read(-1))
except  FileNotFoundError:
    print(f'{file_name4}文件不存在')
print("---end---")
