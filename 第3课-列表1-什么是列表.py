'''
列表由一系列按特定顺序排列的元素组成。你可以创建包含字母表中所有字母、数字0~9或所有家庭成员姓名的列表；也可以将任何东西加入列表中，其中的元素之间可以没有
任何关系。鉴于列表通常包含多个元素，给列表指定一个表示复数的名称（如letters 、digits 或names ）是个不错的主意。
'''
bicycles=["trek","cannodale","redline","specialized"]
print(bicycles)

#for 循环
'''
range() 函数的语法如下：
range(start, stop[, step])
start：可选参数，表示序列的起始值，默认为 0 。
stop：必需参数，表示序列的结束值，但不包含该值。
step：可选参数，表示步长，默认为 1 。
range() 函数返回一个可迭代对象，可以用于 for 循环等场景。
例：
for i in range(5):
    print(i)
'''
for i in range(len(bicycles)):
    print(bicycles[i].title())

#random模块
'''
在 Python 中，random 模块提供了一系列用于生成随机数和执行其他随机操作的函数。
以下是一些常见的 random 函数：
randint(a, b)：返回一个指定范围内（包括 a 和 b）的随机整数。
choice(seq)：从给定的序列中随机选择一个元素。
uniform(a, b)：返回一个在指定范围内（包括 a 和 b）的随机浮点数。
这些函数可以帮助你在程序中引入随机性，例如模拟随机事件、生成随机数据等。
'''
'''
如何生成1到100的随机整数序列？
'''
import random
# 生成 1 到 100 的随机整数序列

#1.random.randint(start,stop)
random_sequence = [random.randint(1, 100) for _ in range(10)]
print(random_sequence)

random_sequence_1=[random.randint(2,40) for _ in range(10)]
print(random_sequence_1)


#2.random.choice(sequence)
'''
在 Python 中，random.choice() 函数可以从给定的序列中随机返回一个元素。使用方法为：random.choice(sequence)，
其中 sequence 表示要从中随机选择的序列，可以是列表、元组、字符串等。下面是一个例子，演示了如何使用 random.choice() 函数：

import random
fruits = ('apple', 'banana', 'orange', 'grape')
random_fruit = random.choice(fruits)
print("随机水果是：", random_fruit)

'''
print(random.choice(random_sequence_1))

import random
fruits = ('apple', 'banana', 'orange', 'grape')
random_fruit = random.choice(fruits)
print(f"随机水果是：{random_fruit}!")

#3.random.uniform(start,stop)  随机返回一个浮点数
s=random.uniform(2,15)
print(s)


#动手试一试
'''
3-1 姓名： 将一些朋友的姓名存储在一个列表中，并将其命名为names 。依次访问该列表中的每个元素，从而将每个朋友的姓名都打印出来。
'''
name=["孙炜","王超","王艳","栗栋栋","纪玲国","吴小伟","沈振军"]
for i in range(len(name)):
    print(name[i])

print("#"*80)
name2 =[random.choice(name) for _ in range(len(name))]
name3 = [random.choice(name)]
print(name2)
print(name3)

'''
3-2 问候语：继续使用练习3-1中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
'''
for i in range(len(name)):
    print(f"Hello,{name[i]},How are you today?")

'''
3-3 自己的列表： 想想你自己喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的宣言，
如“I would like to own a Honda motorcycle”。
'''
list=["哈雷戴维森","雅马哈","川崎","宝马","奥迪","红旗","东风"]
for i in range(len(list)):
    print(f"I would like to own a {list[i]} motorcycle")



#修改列表元素
motorcycles=["honda","yamaha","suzuki"]
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

#在列表中添加元素 append()在列表末尾添加元素
motorcycles.append("honda")
print(motorcycles)
motorcycles.append("宝马")
print(motorcycles)

#在列表中插入元素insert() 使用方法insert() 可在列表的任何位置添加新元素。为此，你需要指定新元素的索引和值。
'''
list.insert(index, element)
·index：要插入元素的索引位置。
·element：要插入的元素
'''
motorcycles.insert(1,"奥迪")
print(motorcycles)

motorcycles.insert(3,"红旗")
print(motorcycles)


#在列表中删除元素
'''
在 Python 中，del 是一个用于删除对象的语句或函数。
del 可以用于删除以下类型的对象：
变量：删除一个变量，使其不再存在。
列表中的元素：从列表中删除指定索引或范围的元素。
字典中的键值对：删除字典中指定的键。
示例如下：
python
# 删除变量
x = 5
del x

# 删除列表中的元素  使用del 可删除任何位置处的列表元素，条件是知道其索引。
my_list = [1, 2, 3, 4, 5]
del my_list[2]
print(my_list)

# 删除字典中的键值对
my_dict = {"name": "Alice", "age": 25}
del my_dict["name"]
print(my_dict)
'''
del motorcycles[3]
print(motorcycles)

my_first_dict={"姓名":"孙炜","年龄":"40","体重":75,"籍贯":"泗洪"}
print(my_first_dict)
del my_first_dict["籍贯"]
print(my_first_dict)

#使用方法pop()删除元素
'''
在 Python 中，列表的 pop() 函数用于移除并返回列表中的最后一个元素。
pop() 函数的语法如下：
list.pop()
示例如下：
my_list = [1, 2, 3, 4, 5]
last_element = my_list.pop()
print("移除的最后一个元素：", last_element)
print("更新后的列表：", my_list)
'''

last_motorcycle = motorcycles.pop()
print(f"移除的最后一辆车是：{last_motorcycle}")
print("更新后的列表：",motorcycles)

'''
实际上，你可以使用pop() 来删除列表中任何位置的元素，只需在括号中指定要删除的元素的索引即可。
'''
print("*"*100)
print(motorcycles)
random_motorcycle = motorcycles.pop(random.randint(1,len(motorcycles)))
print(f"随机删除的车辆是：{random_motorcycle}")
print(motorcycles)

#根据值删除元素
'''
list.remove(element)
其中，element 是要移除的元素。
示例如下：
python
my_list = [1, 2, 3, 2, 4]
my_list.remove(2)
print(my_list)
需要注意的是，如果要移除的元素不在列表中，会抛出一个 ValueError 异常。
'''
motorcycles.remove("suzuki")
print(motorcycles)

