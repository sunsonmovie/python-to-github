
'''
继续使用前面的比萨店示例。这家比萨店在制作比萨时，每添加一种配料都打印一条消息。通过创建一个列表，在其中包含顾客点的配料，并使用一个循环来指出添加到比萨中
的配料，可以以极高的效率编写这样的代码：
'''
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

'''
然而，如果比萨店的青椒用完了，该如何处理呢？为妥善地处理这种情况，可在for 循环中包含一条if 语句：
'''
print("*"*100)
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

'''
顾客的要求往往五花八门，在比萨配料方面尤其如此。如果顾客要在比萨中添加炸薯条，该怎么办呢？可使用列表和if 语句来确定能否满足顾客的要求。
来看看在制作比萨前如何拒绝怪异的配料要求。下面的示例定义了两个列表，其中第一个列表包含比萨店供应的配料，而第二个列表包含顾客点的配料。这次对
于requested_toppings 中的每个元素，都检查它是否是比萨店供应的配料，再决定是否在比萨中添加它：
'''
print("*"*100)
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry,we don't have {requested_topping}.")
print("\nFinished making your pizza!")

#动手试一试
'''
5-8 以特殊方式跟管理员打招呼：创建一个至少包含5个用户名的列表，且其中一个用户名为'admin' 。想象你要编写代码，在每位用户登录网站后都打印一条问
候消息。遍历用户名列表，并向每位用户打印一条问候消息。
    ·如果用户名为'admin' ，就打印一条特殊的问候消息，如“Hello admin, would you like to see a status report?”。
    ·否则，打印一条普通的问候消息，如“Hello Eric, thank you for logging in again”。
'''
print("*"*100)
user_list = ["sunwei","wangchao","xujunyu","admin","lidongdong","jiaxianfu","anzhimin","liuguokai"]
for user in user_list:
    if user == "admin":
        print(f"Hello {user.upper()},would you like to see a status report?")
    else:
        print(f"Hello {user},thank you for logging in again")
print("*"*100)


'''
5-9 处理没有用户的情形：在为完成练习5-8编写的程序中，添加一条if 语句，检查用户名列表是否为空。
    ·如果为空，就打印消息“We need to find some users!”。
    ·删除列表中的所有用户名，确定将打印正确的消息。
'''

for user in range(len(user_list)):
    result = user_list.pop()

if user_list:
    for user in user_list:
        if user == "admin":
            print(f"Hello {user.upper()},would you like to see a status report?")
        else:
            print(f"Hello {user},thank you for logging in again")
else:
    print(f"We need to find some users!")

'''
5-10 检查用户名：按下面的说明编写一个程序，模拟网站确保每位用户的用户名都独一无二的方式。
    ·创建一个至少包含5个用户名的列表，并将其命名为current_users 。
    ·再创建一个包含5个用户名的列表，将其命名为new_users ，并确保其中有一两个用户名也包含在列表current_users 中。
    ·遍历列表new_users ，对于其中的每个用户名，都检查它是否已被使用。如果是这样，就打印一条消息，指出需要输入别的用户名；否则，打印一条消息，指
    ·出这个用户名未被使用。
    ·确保比较时不区分大消息；换句话说，如果用户名'John' 已被使用，应拒绝用户名'JOHN' 。
'''
print("*"*100)
user_list = ["sunwei","wangchao","xujunyu","admin","lidongdong","jiaxianfu","anzhimin","liuguokai"]
current_users = user_list[:]
new_users = ["sunwei","wangchao","wangyan","shenzhenjun","lichangdong","SUNWEI"]
for new_user in new_users:
    if new_user in user_list:
        print(f"{new_user},该用户名已经被使用，请重新输入")
    elif new_user.lower() in user_list:
        print(f"{new_user},该用户名已经被使用，请重新输入")
    else:
        print(f"{new_user},这个用户名未被使用，可以放心使用！")


'''
5-11 序数：序数表示位置，如1st和2nd。大多数序数都以th结尾，只有1、2和3例外。
    ·在一个列表中存储数字1~9。
    ·遍历这个列表。
    ·在循环中使用一个if-elif-else 结构，以打印每个数字对应的序数。输出内容应为1st 、2nd 、3rd 、4th 、5th 、6th 、7th 、8th 和9th ，
    但每个序数都独占一行。
'''
print("*"*100)
num_list = [num for num in range(1,10)]
for num in num_list:
    if num == 1:
        print(f"{num}st")
    elif num == 2 :
        print(f"{num}nd")
    elif num == 3 :
        print(f"{num}rd")
    else:
        print(f"{num}th")





