
#动手试一试
'''
5-3 外星人颜色#1 ：假设在游戏中刚射杀了一个外星人，请创建一个名为alien_color 的变量，并将其设置为'green' 、'yellow' 或'red' 。
编写一条if 语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出玩家获得了5个点。
'''
print("*"*100)
alien_color = ["green","yellow","red"]
color = input("请输入颜色：")
if color in alien_color:
    goat = 5
    print(f"恭喜您获得{goat}个积分.")
else:
    print(f"I'm sorry,您的积分为0.")

'''
5-4 外星人颜色#2 ：像练习5-3那样设置外星人的颜色，并编写一个if-else 结构。
如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5个点。
如果外星人不是绿色的，就打印一条消息，指出玩家获得了10个点。
编写这个程序的两个版本，在一个版本中执行if 代码块，而在另一个版本中执行else 代码块。
'''
color = input("请输入颜色：")
if color == alien_color[0]:
    goat=5
    print(f"你射杀了该外星人，获得{goat}积分.")
else:
    goat = 10
    print(f"你获得了{goat}积分.")

'''
5-5 外星人颜色#3 ：将练习5-4中的if-else 结构改为if-elif-else 结构。
    ·如果外星人是绿色的，就打印一条消息，指出玩家获得了5个点。
    ·如果外星人是黄色的，就打印一条消息，指出玩家获得了10个点。
    ·如果外星人是红色的，就打印一条消息，指出玩家获得了15个点。
编写这个程序的三个版本，它们分别在外星人为绿色、黄色和红色时打印一条消息。
'''
print("*"*100)
color = input("请输入颜色：")
if color == alien_color[0]:
    print(f"玩家获得5积分.")
elif color == alien_color[1]:
    print(f"玩家获得10积分.")
elif color == alien_color[2]:
    print(f"玩家获得15积分.")
else:
    print(f"玩家没有获得积分.")


'''
5-6 人生的不同阶段：设置变量age 的值，再编写一个if-elif-else 结构，根据age 的值判断处于人生的哪个阶段。
    ·如果一个人的年龄小于2岁，就打印一条消息，指出他是婴儿。
    ·如果一个人的年龄为2（含）～4岁，就打印一条消息，指出他正蹒跚学步。
    ·如果一个人的年龄为4（含）～13岁，就打印一条消息，指出他是儿童。
    ·如果一个人的年龄为13（含）～20岁，就打印一条消息，指出他是青少年。
    ·如果一个人的年龄为20（含）～65岁，就打印一条消息，指出他是成年人。
    ·如果一个人的年龄超过65（含）岁，就打印一条消息，指出他是老年人。
'''
print('*'*100)
age=int(input("请输入你的年龄："))
if age<2:
    print("你还是一个婴儿.")
elif 2<=age<4:
    print("你正蹒跚学步.")
elif 4<=age<13:
    print("你是儿童.")
elif 13<=age<20:
    print("你是青少年.")
elif 20<=age<65:
    print("你是成年人.")
else:
    print("你是老年人.")

'''
5-7 喜欢的水果：创建一个列表，其中包含你喜欢的水果，再编写一系列独立的if 语句，检查列表中是否包含特定的水果。
将该列表命名为favorite_fruits ，并在其中包含三种水果。
编写5条if 语句，每条都检查某种水果是否包含在列表中，如果包含在列表中，就打印一条消息，如“You really like bananas!”。
'''
favorite_fruits = ["apples","bananas","oranges","blueberries","grapes","mango","kiwi","pineapple","strawberries"]
if "apples" in favorite_fruits:
    print("You really like apples!")
if "bananas" in favorite_fruits:
    print("You really like bananas!")
if "kiwi" in favorite_fruits:
    print("You really like kiwi!")
if "pineapple" in favorite_fruits:
    print("You really like pineapple!")
if "oranges" in favorite_fruits:
    print("You really like oranges!")










