import numpy as np

'''批量初始化向量:real'''
vector1 = np.ones(5)
vector2 = np.zeros(3)
vector3 = np.random.random(6)
'''逐个初始化向量:list[]'''
vector4 = np.array([1, 2, 3])

'''向量的加减乘除'''
data = np.array([1, 2, 3])
data2 = np.array([4, 5, 6])
add = data + data2
sub = data - data2
mul = data * data2
div = data / data2
'''向量的广播特性'''
add_broadcasting = data + 10
mul_broadcasting = data * 10
'''向量的切片特性'''
split = data[1:]
'''向量的聚合函数(统计函数)'''
max = data.max()
min = data.min()
sum = data.sum()
prod = data.prod()  # 累乘
mean = data.mean()  # 均值
std = data.std()  # 标准差
'''向量的dot product: 行向量·列向量'''
dot = data.dot(data2)
print("end")
