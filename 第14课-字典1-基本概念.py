'''
字典
'''
'''
Python字典基本概念
Python字典是一种数据结构，它允许存储键值对。每个键都是唯一的，而值可以是任何数据类型，包括数字、字符串、列表、集合、字典等。字典是动态的，这意味着你可以随时添加、删除或修改键值对3。

Python字典的使用
创建字典
你可以使用大括号 {} 或 dict() 函数来创建一个新的空字典。如果你想添加特定的键值对，可以使用方括号语法，例如 {'key1': 'value1', 'key2': 'value2'}3。

访问字典
要访问字典中的值，你需要知道它的键。你可以使用方括号语法来获取特定键对应的值，例如 my_dict['key1']。如果键不存在，则会引发一个 KeyError 异常3。

修改字典
你可以使用方括号语法来修改字典中的值，例如 my_dict['key1'] = 'new_value'。如果键不存在，则会添加一个新的键值对3。

删除字典
你可以使用 del 语句来删除字典中的键值对，例如 del my_dict['key1']。这将从字典中移除指定的键值对3。

字典的其他操作
除了上述的基本操作外，Python字典还提供了许多其他的操作，如 len() 函数可以用来获取字典的大小，in 操作符可以用来检查某个键是否存在于字典中，以及 for 循环可以用来遍历字典中的所有键值对3。

Python字典的应用示例
假设你想创建一个记录学生信息的字典，其中学生的ID作为键，学生的姓名、年龄和成绩作为值。你可以这样编写：

    student_info = {
        '1001': {'name': 'Alice', 'age': 20, 'score': 95},
        '1002': {'name': 'Bob', 'age': 22, 'score': 88},
        '1003': {'name': 'Charlie', 'age': 23, 'score': 92}
    }
在这个例子中，你可以使用 student_info['1001']['name'] 来获取Alice的姓名，使用 student_info['1002']['age'] 来获取Bob的年龄，等等3。
'''
print("*"*100)
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#修改字典中的值
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

'''
来看一个更有趣的例子：对一个能够以不同速度移动的外星人的位置进行跟踪。为此，我们将存储该外星人的当前速度，并据此确定该外星人将向右移动多远：
'''
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# 向右移动外星人
# 据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
# 这个外星人的速度一定很快
    x_increment = 3
# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"Nes x-position:{alien_0['x_position']}")

#删除键值对
print("*"*100)
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

#由类似对象组成的字典
'''
在前面的示例中，字典存储的是一个对象（游戏中的一个外星人）的多种信息，但你也可以使用字典来存储众多对象的同一种信息。例如，假设你要调查很多人，询问他们最喜
欢的编程语言，可使用一个字典来存储这种简单调查的结果，如下所示：
'''
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
                    }

for key,value in favorite_languages.items():
    print(f"{key}:{value.title()}")






