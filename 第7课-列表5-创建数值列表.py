'''
需要存储一组数字的原因有很多，例如，在游戏中，需要跟踪每个角色的位置，还可能需要跟踪玩家的几个最高得分。在数据可视化中，处理的几乎都是由数字（如温度、距
离、人口数量、经度和纬度等）组成的集合。
列表非常适合用于存储数字集合，而Python提供了很多工具，可帮助你高效地处理数字列表。明白如何有效地使用这些工具后，即便列表包含数百万个元素，你编写的代码也能运
行得很好。
'''


#使用函数range()
'''
在 Python 中，range() 函数用于生成一个整数序列。
range() 函数的语法如下：
参数说明：
start：起始值（包含），默认值为 0 。
stop：结束值（不包含）。
step：步长，默认为 1 。
range() 函数返回一个可迭代对象，而不是列表。可以通过遍历该可迭代对象来获取序列中的元素。
以下是一些示例：
# 生成 0 到 4 的整数序列
range(5)  
# 生成 1 到 5 的整数序列
range(1, 6)  
# 生成 2 到 10，步长为 2 的整数序列
range(2, 11, 2)  
在实际使用中，可以根据需要设置不同的参数来生成不同的整数序列。
'''
print("*"*100)
for value in range(5):
    print(value)

for value in range(1,6):
    print(value)

#使用range()创建数字列表
num = list(range(1,6))
print(num)

even_numbers = list(range(1,30,2))
print(even_numbers)


'''
使用函数range() 几乎能够创建任何需要的数字集，例如，如何创建一个列表，其中包含前10个整数（即1~10）的平方呢？在Python中，两个星号（**）表示乘方运算。下面
的代码演示了如何将前10个整数的平方加入到一个列表中：
'''
print("*"*100)
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

#列表解析
print("*"*100)
squares_1 = [value**2 for value in range(1,11)]
print(squares_1)

#对数字列表执行简单的统计计算
print("*"*100)
nature_numbers = []
for nature_number in range(1,101):
    nature_numbers.append(nature_number)
print(nature_numbers)
print(min(nature_numbers))
print(max(nature_numbers))
print(sum(nature_numbers))



#动手试一试
'''
4-3 数到20：使用一个for 循环打印数字1~20（含）。
'''
print("*"*100)
for i in range(1,21,1):
    print(i)

'''
4-4 一百万：创建一个列表，其中包含数字1~1 000 000，再使用一个for 循环将这些数字打印出来（如果输出的时间太长，按Ctrl+ C停止输出，或关闭输出窗口）。
'''
print("*"*100)
for i in range(1000000):
    print(i)

'''
4-5 计算计1~1 000 000的总和 的 ：创建一个列表，其中包含数字1~1 000 000，再使用min() 和max() 核实该列表确实是从1开始，到1 000 000结束的。另外，对这个列表
调用函数sum() ，看看Python将一百万个数字相加需要多长时间。
'''
print("*"*100)
millions = []
for million in range(1,1000001,1):
    millions.append(million)
print(millions)
print(min(millions))
print(max(millions))
print(sum(millions))

'''
4-6 奇数：通过给函数range() 指定第三个参数来创建一个列表，其中包含1~20的奇数；再使用一个for 循环将这些数字都打印出来。
'''
print("*"*100)
for i in range(1,20,2):
    print(i)

'''
4-7 3的倍数：创建一个列表，其中包含3~30内能被3整除的数字；再使用一个for 循环将这个列表中的数字都打印出来。
'''
print("*"*100)
odd_number = [] #奇数
for i in range(3,31):
    if i%3 ==0:
        odd_number.append(i)
print(odd_number)

'''
4-8 立方：将同一个数字乘三次称为立方。例如，在Python中，2的立方用2**3 表示。请创建一个列表，其中包含前10个整数（即1~10）的立方，再使用一个for 循
环将这些立方数都打印出来。
'''
print("*"*100)
cubic = []
for i in range(1,11):
    cubic.append(i**3)
print(cubic)

'''
4-9 立方解析：使用列表解析生成一个列表，其中包含前10个整数的立方。
'''
print("*"*100)
cubics = [ cubic**3 for cubic in range(1,11,1)]
print(cubics)









