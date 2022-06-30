import numpy as np

'''批量初始化矩阵:tuple()'''
matrix1 = np.ones((3, 4))  # 元组中第一个数是矩阵的行数(从上往下),第二个数是矩阵的列数(从左往右)
matrix2 = np.zeros((3, 4))
matrix3 = np.random.random((2, 3))
'''逐个初始化矩阵:[][]'''
matrix4 = np.array([[1, 2], [3, 4]])

'''矩阵的加减乘除'''
data = np.array([[1, 2], [3, 4]])
data2 = np.array([[5, 6], [7, 8]])
add = data + data2
sub = data - data2
mul = data * data2
div = data / data2
'''向量的广播特性'''
add_broadcasting = data + 10
mul_broadcasting = data * 10
add2_broadcasting = data + np.array([10, 20])  # 按列来加,广播逻辑是一列一列的计算.
'''向量的切片特性'''
split = data[1:]
'''向量的聚合函数(统计函数)'''
max = data.max()
min = data.min()
sum = data.sum()
prod = data.prod()  # 累乘
mean = data.mean()  # 均值
std = data.std()  # 标准差
print("end")
