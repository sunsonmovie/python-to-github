'''
你经常需要遍历列表的所有元素，对每个元素执行相同的操作。例如，在游戏中，可能需要将每个界面元素平移相同的距离；对于包含数字的列表，可能需要对每个元素执行相
同的统计运算；在网站中，可能需要显示文章列表中的每个标题。需要对列表中的每个元素都执行相同的操作时，可使用Python中的for 循环。
'''

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

'''
编写for 循环时，对于用于存储列表中每个值的临时变量，可指定任何名称。然而，选择描述单个列表元素的有意义的名称大有帮助。例如，对于小猫列表、小狗列表和
一般性列表，像下面这样编写for 循环的第一行代码是不错的选择：
for cat in cats:
for dog in dogs:
for item in list_of_items:
'''
for magician in magicians:
    print(f"{magician.title()},that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}\n" )

#动手试一试
'''
4-1 比萨：想出至少三种你喜欢的比萨，将其名称存储在一个列表中，再使用for 循环将每种比萨的名称都打印出来。
修改这个for 循环，使其打印包含比萨名称的句子，而不仅仅是比萨的名称。对于每种比萨，都显示一行输出，如“I like pepperoni pizza”。
在程序末尾添加一行代码，它不在for 循环中，指出你有多喜欢比萨。输出应包含针对每种比萨的消息，还有一个总结性句子，如“I really love pizza!”。
'''
pizza_list =["Margherita pizza","Hawaiian pizza","Chicago deep-dish pizza"]
for pizza in pizza_list:
    print(f"I like pepperoni on my {pizza}")
print("I really love pizza!")


'''
4-2 动物：想出至少三种有共同特征的动物，将这些动物的名称存储在一个列表中，再使用for 循环将每种动物的名称都打印出来。
修改这个程序，使其针对每种动物都打印一个句子，如“A dog would make a great pet”。
在程序末尾添加一行代码，指出这些动物的共同之处，如打印诸如“Any of these animals would make a great pet!”这样的句子。
'''
print("*"*100)
animals = ["monkey","dog","cat","tigger","duck"]
for animal in animals:
    print(f"A {animal} would make a great pet!")
print("Any of these animals would make a great pet!")
















