'''
使用open()打开文件时必须要指定打开文件所要做的操作(读、写、追加)
如果不指定操作类型,则默认是读取,
w表示是可写的,使用w来写入文件时,如果文件不存在会创建文件,如果文件存在则会截断文件(截断文件指删除原来文件中的所有内容)
a表示追加内容,如果文件不存在会创建文件,如果文件存在则会向文件中追加内容
    +为操作符增加功能
    r+即可读又可写,文件不存在会报错
    w+
    a+

write()来向文件中写入内容,如果操作的是一个文本文件的话,则write()需要传递一个字符串作为参数
该方法可以分多次向文件中写入内容
写入完成以后,该方法会返回写入的字符的个数
'''
filename_text_zh = 'write_text_zh.txt'
with open(filename_text_zh, mode="wt", encoding='utf8') as file_text_zh:
    file_text_zh.write("明日复明日,")
    file_text_zh.write("明日何其多\n")
    file_text_zh.write("我生待明日,")
    file_text_zh.write("万事成蹉跎\n")

with open(filename_text_zh, mode="wt", encoding='utf8') as file_text_zh:
    file_text_zh.write("---明日复明日,---")
    file_text_zh.write("---明日何其多---\n")
    file_text_zh.write("---我生待明日,---")
    file_text_zh.write("---万事成蹉跎---\n")

with open(filename_text_zh, mode="at", encoding='utf8') as file_text_zh:
    file_text_zh.write("\n!!!明日复明日,---")
    file_text_zh.write("---明日何其多---\n")
    file_text_zh.write("---我生待明日,---")
    file_text_zh.write("---万事成蹉跎!!!\n")

print("end")
