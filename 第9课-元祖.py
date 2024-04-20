'''
列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的，这对处理网站的用户列表或游戏中的角色列表至关重要。然而，有时候你需要创建一系列不可修
改的元素，元组可以满足这种需求。Python将不能修改的值称为不可变的 不 ，而不可变的列表被称为元组元 。
'''
'''
Python中的元组（tuple）是一种不可变的数据结构，它包含了一个有序的元素列表。元组的特点是它们一旦创建就不能被修改。
元组的创建非常简单，只需要将一系列的值放在括号内即可。例如：
    tup = (1, 2, 3)
    这里我们创建了一个包含三个整数的元组。
元组的元素可以是任何类型的数据，包括其他元组：
    tup = (1, 'a', (2, 'b'))
在这个例子中，元组tup包含了三个元素：一个整数1，一个字符串'a'，以及另一个元组(2, 'b')。
元组的主要用途是作为字典的键或者集合的元素，因为它们的不可变性使得它们更安全。此外，元组也常用于函数返回多个值。
元组的元素可以通过索引来访问，索引从0开始：
    tup = (1, 2, 3)
    print(tup[0])  # 输出 1
元组的长度可以通过内置函数len()来获取：
    tup = (1, 2, 3)
    print(len(tup))  # 输出 3
如果你想要创建一个只有一个元素的元组，你需要在元素后面加上一个逗号，否则Python会认为你只是在写一个括号包围的普通表达式：
    tup = (1,)
    print(type(tup))  # 输出 <class 'tuple'>
相反，如果你创建了一个没有逗号的元组，那么Python会将其解释为一个普通的圆括号表达式，而不是元组：             
    tup = (1)
    print(type(tup))  # 输出 <class 'int'>                    
最后，元组是不可变的，这意味着你不能修改它们的内容。例如，你不能给元组添加新的元素，也不能删除或更改现有的元素： 
    tup = (1, 2, 3)
    tup[0] = 4  # 这会引发一个错误
'''
#定义元组
print("*"*100)
dimensions = (200,5)
print(dimensions[0])
print(dimensions[1])
#print(dimensions[2])  #会提示错误：IndexError: tuple index out of range
#dimensions[0]=250     #会提示错误：TypeError: 'tuple' object does not support item assignment

'''
虽然不能修改元组的元素，但可以给存储元组的变量赋值。因此，如果要修改前述矩形的尺寸，可重新定义整个元组：
'''
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100) #给元组变量赋值是合法的
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


#动手试一试
'''
4-13 自助餐：有一家自助式餐馆，只提供五种简单的食品。请想出五种简单的食品，并将其存储在一个元组中。
使用一个for 循环将该餐馆提供的五种食品都打印出来。
尝试修改其中的一个元素，核实Python确实会拒绝你这样做。
餐馆调整了菜单，替换了它提供的其中两种食品。请编写一个这样的代码块：给元组变量赋值，并使用一个for 循环将新元组的每个元素都打印出来。
'''
print("*"*100)
Buffet_food = ("Seafood","Barbecue","Chinese cuisine","Western cuisine","Japanese cuisine","Fruit and desserts","Juice")
result=""
for food in Buffet_food:
    result += food + "、"
result=result[:-1]
print(f"自助餐馆的食品有：{result}",end="。")




















