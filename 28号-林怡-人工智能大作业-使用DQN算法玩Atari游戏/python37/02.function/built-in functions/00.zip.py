'''
zip([iterable, ...])
return <class 'tuple'>s:python3中将其作为一个对象
zip(* <class 'tuple'>)
'''
a = (1, 2, 3)
b = [3, 4, 5]
c = [32, 1, 23, 4, 3]
ab_zip = zip(a, b)
ac_zip = zip(a, c)  # 就短原则,故而是有损压缩
ac_zip_toList = list(ac_zip)
x, y, z = zip(*((1, 2, 3), (4, 5, 6)))  # zip(*) 可理解为解压

print("end")
