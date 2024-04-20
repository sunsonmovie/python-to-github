'''
在Python中，if语句用于执行基于条件的代码块。以下是if语句的基本语法：
    if 条件表达式:
        代码块
如果条件表达式的结果为True，则执行代码块。如果条件结果为False，则跳过代码块。
此外，if语句还可以与else和elif（else if的简写）一起使用，以处理更复杂的逻辑判断：
    if 条件表达式1:
        代码块1
    elif 条件表达式2:
        代码块2
    else:
        代码块3
在这个结构中，如果条件表达式1为True，则执行代码块1；如果条件表达式1为False，则评估条件表达式2。如果条件表达式2也为False，则执行代码块3。
下面是一个简单的例子，演示如何使用if语句：
    # 定义一个变量
    age = 20
    # 使用if语句判断年龄是否超过18
    if age >= 18:
        print("成年")
    else:
        print("未成年")
在这个例子中，如果age变量的值大于或等于18，则输出“成年”，否则输出“未成年”。
'''
#检查是否相等
print("*"*100)
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#检查是否不相等
'''
要判断两个值是否不等，可结合使用惊叹号和等号（!= ），其中的惊叹号表示不 ，在很多编程语言中都如此。
下面再使用一条if 语句来演示如何使用不等运算符。我们将把要求的比萨配料存储在一个变量中，再打印一条消息，指出顾客要求的配料是否是意式小银鱼（anchovies）：
'''
print("*"*100)
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#比较数字
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")


#动手试一试
'''
5-1 条件测试：编写一系列条件测试；将每个测试以及你对其结果的预测和实际结果都打印出来。你编写的代码应类似于下面这样：
'''
print("*"*100)
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')


'''
5-2对于下面列出的各种测试，至少编写一个结果为True 和False 的测试。
   · 检查两个字符串相等和不等。
   · 使用函数lower() 的测试。
   · 检查两个数字相等、不等、大于、小于、大于等于和小于等于。
   · 使用关键字and 和or 的测试。
   · 测试特定的值是否包含在列表中。
   · 测试特定的值是否未包含在列表中。
'''
print("*"*100)
a="tigger"
b="dog"
c="CAT"

if a==b:
    print(f"wow,a==b!")
else:
    print("Q^Q,a!=b...")

print("*"*100)
print(c.lower())

if a==b and b!=c:
    print("wow,that's false!")
else:
    print("er....")
print("*"*100)
if a!=b or b!=c:
    print("That's ture!")


#if-elif-else结构
'''
经常需要检查超过两个的情形，为此可使用Python提供的if-elif-else 结构。Python只执行if-elif-else 结构中的一个代码块，它依次检查每个条件测试，直到遇到通过
了的条件测试。测试通过后，Python将执行紧跟在它后面的代码，并跳过余下的测试。
在现实世界中，很多情况下需要考虑的情形都超过两个。例如，来看一个根据年龄段收费的游乐场：
    ·4岁以下免费；
    ·4~18岁收费5美元；
    ·18岁（含）以上收费10美元。
如果只使用一条if 语句，如何确定门票价格呢？下面的代码确定一个人所属的年龄段，并打印一条包含门票价格的消息：
'''
print("*"*100)
age=int(input("请输入你的年龄："))
if age < 4:
    price=0
elif 4 <= age < 18:
    price=5
else:
    price=10
print(f"Your admission cost is ${price}.")

'''
可根据需要使用任意数量的elif 代码块，例如，假设前述游乐场要给老年人打折，可再添加一个条件测试，判断顾客是否符合打折条件。下面假设对于65岁（含）以上的老
人，可以半价（即5美元）购买门票：
'''

print("*"*100)
age=int(input("请输入你的年龄："))
if age < 4:
    price=0
elif 4 <= age < 18:
    price=5
elif 18 <= age < 60:
    price=10
else:
    price=0
print(f"Your admission cost is ${price}.")




























