'''
在 Python 中，列表切片是一种用于获取列表中部分元素的操作。通过指定起始索引、结束索引和步长，可以灵活地获取列表的子序列。
列表切片的语法格式为：list[start:end:step]，其中：
start：起始索引，从 0 开始计数，-1 表示结束，默认值为 0 。
end：结束索引，不包含在结果中，默认值为列表长度。
step：步长，为正数时从左往右取值，为负数时从右往左取值，默认值为 1 。
下面是一些示例：
    # 定义一个列表
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 示例 1：获取索引 1 到 4 的元素
    slice1 = numbers[1:5]
    print(slice1)

    # 示例 2：步长为 2，获取索引 0 到 4 的元素（隔一个取一个）
    slice2 = numbers[0:5:2]
    print(slice2)

    # 示例 3：从右边开始取，步长为-1
    slice3 = numbers[-1:-5:-1]
    print(slice3)
'''
print("*"*100)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])       #打印列表，包含前4个元素
print(players[-1])        #打印列表的最后一个元素
print(players[-2])        #打印列表的倒数第2个元素
print(players[0:-1])      #打印列表，不包含最后一个元素
print(players[:])         #打印列表，包含全部元素
print(players[:2])        #打印列表，包含前两个元素
print(players[2:])        #打印列表，包含从第3个元素到最后一个元素
print(players[-4:])       #打印列表，包含倒数4个元素

#遍历切片
'''
如果要遍历列表的部分元素，可在for 循环中使用切片。在下面的示例中，我们遍历前三名队员，并打印他们的名字：
'''
print("*"*100)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())


#复制列表
'''
你经常需要根据既有列表创建全新的列表。下面来介绍复制列表的工作原理，以及复制列表可提供极大帮助的一种情形。要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（[:] ）。这让Python创建一个始于第一个元素，终止于最后一个元素的切片，即复制整个
列表。例如，假设有一个列表，其中包含你最喜欢的四种食品，而你还想创建另一个列表，在其中包含一位朋友喜欢的所有食品。不过，你喜欢的食品，这位朋友都喜欢，因此你可以通过复制来创建这个列表：
'''
print("*"*100)
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(f"My favorite foods are:{my_foods}")
print(f"\nMy friend's favorite foods are:{sorted(friend_foods)}")

print("*"*100)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(f"My favorite foods are:{my_foods}")
print(f"\nMy friend's favorite foods are:{sorted(friend_foods)}")

#动手试一试
'''
4-10 切片：选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
        ·打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素。
        ·打印消息“Three items from the middle of the list are:”，再使用切片来打印列表中间的三个元素。
        ·打印消息“The last three items in the list are:”，再使用切片来打印列表末尾的三个元素。
'''
print("*"*100)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:3])
print(players[1:-1])
print(players[-3:])

'''
4-11 你的比萨和我的比萨 你 ：在你为完成练习4-1而编写的程序中，创建比萨列表的副本，并将其存储到变量friend_pizzas 中，再完成如下任务。
    ·在原来的比萨列表中添加一种比萨。
    ·在列表friend_pizzas 中添加另一种比萨。
    ·核实你有两个不同的列表。为此，打印消息“My favorite pizzas are:”，再使用一个for 循环来打印第一个列表；打印消息“My friend's favorite pizzas are:”，再使用一
     个for 循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中。
'''
print("*"*100)
pizza_list =["Margherita pizza","Hawaiian pizza","Chicago deep-dish pizza"]
friend_pizzas = pizza_list[:]
print(friend_pizzas)
print("*"*100)
pizza_list.append("Durian fruit pizza")
print("My favorite pizzas are:",end = " ")
result = ""
for pizza in pizza_list:
    result+= pizza + "、"
result=result[:-1]
print(result,end = "。 ")


print("\n")
friend_pizzas.append("Beef bacon pizza")
print(f"My friend's favorite pizzas are:",end = " ")
result=""
for friend_pizza in friend_pizzas:
    result+=friend_pizza + "、"
result=result[:-1]
print(result,end="。")

'''
要实现列表打印时不显示括号，元素用顿号隔开，并且去掉最后一个元素后的顿号，可以使用循环和字符串拼接的方式来实现。以下是示例代码：
    list_demo = [1, 2, 3, 4, 5]
    result = ""
    for element in list_demo:
        result += str(element) + "、"
    result = result[:-1]
    print(result)
在上述代码中，首先定义了一个列表list_demo。然后创建一个空字符串result，用于存储打印结果。通过循环遍历列表中的每个元素，将元素转换为字符串后与顿号拼接，
并添加到result中。最后，通过字符串的切片操作result[:-1]去掉最后一个顿号，再将处理后的结果打印出来。
'''






