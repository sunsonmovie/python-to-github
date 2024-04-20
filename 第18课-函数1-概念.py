'''
要执行函数定义的特定任务，可调用该函数。需要在程序中多次执行同一项任务时，你无需反复编写完成该任务的代码，而只需调用执行该任务的函数，让Python运行
其中的代码。你将发现，通过使用函数，程序的编写、阅读、测试和修复都将更容易。
'''
'''
Python函数是一种封装一段代码的方式，使得我们可以重复使用这段代码，同时还可以传递参数给函数，从而让函数能够处理不同的数据。在Python中，定义一个函数的基本语法如下：
    def function_name(parameters):
        # 函数体
        return something
其中function_name是你想要给函数命名的名称，parameters是可选的，代表函数接受的参数，return something是函数返回的内容。

举个例子，如果我们想要定义一个函数，该函数接受一个参数，并返回该参数的两倍，我们可以这样做：
    def double(number):
        return number * 2
然后，我们可以通过调用这个函数并传入一个参数来使用它：
    result = double(5)
    print(result)  # 输出将会是 10
在这个例子中，double就是函数名，number是函数接受的参数，return number * 2是函数体，最后的结果result是我们调用函数并传入参数5得到的结果1
'''

#向函数传递参数
def greet_user(username):  #这里的username是形参
    print(f"Hello {username},how are you today?")
greet_user('Jason')        #调用函数，这里的Jason是实参

'''
在Python中，函数的参数分为形式参数（简称形参）和实际参数（简称实参）。
形参：在函数定义时，括号内的参数被称为形参。形参本质上是一个变量名，用于接收外部传递的值。例如，在函数定义def func(a, b):中，a和b就是形参。
实参：在函数调用时，括号内的值被称为实参。实参是传递给函数的实际值，可以是常量、变量、表达式或它们的组合。例如，在函数调用func(1, 2)中，1和2就是实参。
需要注意的是，Python函数的参数传递是有一定顺序的。在函数定义时，形参的顺序决定了它们接受的实参的顺序。而在函数调用时，实参的顺序也需要与形参的顺序相匹配。如果不匹配，可能会导致错误。
此外，Python还支持不定长的参数，即可以通过星号*来表示一个可变的参数列表。例如，在函数定义def func(*args):中，args就是一个不定长的形参，它可以接受任意数量的实参。
总的来说，形参和实参是函数定义和调用的基础，它们共同构成了函数的工作流程。在实际编程中，合理地使用形参和实参可以使我们的代码更加清晰、易维护。
'''

#动手试一试
'''
8-1 消息：编写一个名为display_message()的函数，它打印一个句子，指出你在本章学的是什么。调用这个函数，确认显示的消息正确无误。
'''
def display_message(list_of_function):
    print(f"本学期学习的内容有：")
    for item in list_of_function:
        print(f"·{item}")
display_message(["线性代数","微积分","概率与统计","复变函数"])


'''
8-2 喜欢的图书：编写一个名为favorite_book() 的函数，其中包含一个名为title 的形参。这个函数打印一条消息，如One of my favorite books is
Alice in Wonderland 。调用这个函数，并将一本图书的名称作为实参传递给它。
'''
def favorite_book(title):
    print(f"One of my favorite book is 《{title}》.")

favorite_book("三国演义")








