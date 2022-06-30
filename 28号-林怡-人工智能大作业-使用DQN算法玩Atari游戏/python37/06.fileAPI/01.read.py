'''为了突出重点,本应具有的try-expected异常处理舍弃!
在with open() as ... 的语句块通过read()来读取文件中的内容
如果直接调用read()它会将文本文件的所有内容全部都读取出来.
    在读取的文件较大的话,会一次性将硬盘中文件的内容加载到内存中,容易导致内存溢出.
    所以对于较大的文件,不要直接调用read()
    help(file_obj.read) #help用法,后接函数,不带括号
read()可以接收一个size作为参数,该参数用来指定要读取的字符的数量
    size默认值为-1,它会读取文件中的所有字符.
    可以显式地为size指定一个值,这样read()会读取指定数量的字符,
    每一次读取都是从上次读取到的位置开始读取
    如果字符的数量小于size,则会读取剩余所有的.
    如果已经读取到了文件的最后了,则会返回''空串
'''
'''1.通过二进制&&文本两种方式读取文本文件'''
filename_text_zh = "text_zh.txt"
with open(filename_text_zh,
          # mode='rt', # 默认就是rt : read text
          encoding='utf8'
          ) as file_text_zh:
    # help(file_text_zh.read)
    # negative,omited,suitable positive,big positive to EOF 都试试
    content0_zh = file_text_zh.read(5)
    content1_zh = file_text_zh.read(0)
    content2_zh = file_text_zh.read(6)
    content3_zh = file_text_zh.read(100)

filename_text_en = "text_en.txt"
# 以读取二进制的方式读取纯英文文本文件
with open(filename_text_en, mode='rb') as file_text_en:
    content0_en = file_text_en.read(5)
    content1_en = file_text_en.read(0)
    content2_en = file_text_en.read(6)
    content3_en = file_text_en.read(100)
    aByte = content0_en[0]  # 证实确是字节
'''2.读取大文件'''
with open("readme.md", encoding='utf8') as file_readme:
    chunk = 10  # 每次读取的阈值
    while True:
        content_readme = file_readme.read(chunk)
        print(content_readme, end='')
        if not content_readme:  # 如果读取到内容
            break
'''3.
按行读取 readline():很有用
readlines():将行封装成列表

seek: change stream position
tell: display stream position
# 墙裂注意上面的stream都是以二进制形式存在的,所以必须确定mode为'b'
# help(file_text_en.seek) #忘记了运行下
# help(file_text_en.tell) #忘记了运行下
下面的例子特别适合复习,逐行代码逐行地考究!!!
'''
with open(filename_text_en, mode='rb', ) as file_text_en:
    # help(file_text_en.seek)
    # help(file_text_en.tell)

    streamPosition1 = file_text_en.tell()
    line0 = file_text_en.readline()
    streamPosition2 = file_text_en.tell()
    streamPosition3 = file_text_en.seek(3)
    line1 = file_text_en.readline()
    streamPosition4 = file_text_en.tell()
    streamPosition5 = file_text_en.seek(6, 1)
    streamPosition6 = file_text_en.seek(-6, 2)
    streamPosition7 = file_text_en.seek(14, 0)
    line2 = file_text_en.readline()
    lineAll = file_text_en.readlines()
    file_text_en.seek(3)
    print("\n")
    for i in file_text_en:
        print(i)
print("\nend")
