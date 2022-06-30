'''
os.1istdir()获取指定目录的目录结构需要一个路径作为参数，会获取到该路径下的目录结构，
默认路径为.:当前目录
该方法会返回一个列表，目录中的每一个文件（夹）的名字都是列表中的一个元素

下面代码可以逐行阅读,还是很好理解的!
'''

import os

list1 = os.listdir()
dir1 = os.getcwd()
os.chdir("D:/")
dir2 = os.getcwd()
list2 = os.listdir()
os.mkdir("temp")  # 在当前目录下创建一个名字为temp的目录
open("tmp.txt", 'x')  # x:表示严格意义上的新建文件
list3 = os.listdir()
os.rmdir("temp")
os.remove('tmp.txt')
list4 = os.listdir()
print("end")
