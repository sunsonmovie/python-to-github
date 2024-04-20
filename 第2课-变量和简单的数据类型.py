
#1 字符串
message="Hello Python world!"
print(message)
message="Hello Python Crash Course world!"
print(message)

'''
·变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头，例如，可将变量命名为message_1，但不能将其命名为1_message。
·变量名不能包含空格，但可使用下划线来分隔其中的单词。例如，变量名greeting_message可行，但变量名greetingmessage会引发错误。
·不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词，如print 。
·变量名应既简短又具有描述性。例如，name比n好，student_name比s_n好，name_length比length_of_persons_name好。
·慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0。
'''

name="ada loveace"
print(name.title()) #首字母大写
print(name.upper()) #全体大写

first_name="ada"
last_name="loveace"
full_name=first_name+" "+last_name   #拼接字符串
print(full_name.title())
print("hello,"+full_name.title()+"!")

print("\tPython\tis me")  #制表符\t  空格4位
print("Languages:\n\tPython\n\tC\n\tJavaScript") #换行符\n

#删除空白的方法:
# 删除右空白 rstrip()    rest 右
# 删除左空白 lstrip()    left 左
# 删除左右两端的空白 strip()
favorite_language=" Python  JavaScript "
favorite_language
favorite_language.rstrip()
print(favorite_language)
print(favorite_language.lstrip())
print(favorite_language.strip())

message = "One of Python's strengths is its diverse community."
print(message)

name="sunson"
print(f"Hello,{name.title()},would you like to learn some Python today?")

#2.数字
a=2+3 #加法
b=6-4 # 减法
c=2*3 # 乘法
d=10/5 # 除法
e=10//3 #整除取整
f=10%3 #取余
g=2**3 #指数运算
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

#str()方法，将非字符串值表示为字符串
age=23
message="Happy "+str(age)+"rd Birthday!"
print(message)

#random 随机数
#方法randrange(start,stop,step)
import random
num=random.randrange(1,100,3)
print(num)

#Python之禅
'''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
import this
print(this)