'''
动手试一试
'''
'''
6-1 人：使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。该字典应包含键first_name 、last_name 、age 和city 。将存储在该字典中
的每项信息都打印出来。
'''
people_dict = {
"first_name":"sun",
"last_name":"wei",
"age":"40",
"city":"suq,ian"
}
print(people_dict)

'''
6-2 喜欢的数字：使用一个字典来存储一些人喜欢的数字。请想出5个人的名字，并将这些名字用作字典中的键；想出每个人喜欢的一个数字，并将这些数字作为值存
储在字典中。打印每个人的名字和喜欢的数字。为让这个程序更有趣，通过询问朋友确保数据是真实的。
'''
favorite_numbers ={
    "孙炜":"7",
    "徐俊宇":"6",
    "王超":"8",
    "王艳":"5",
    "栗栋栋":"1"
}

for key,value in favorite_numbers.items():
    print(f"{key}喜欢的数字是：{value}.")

'''
6-3 词汇表：Python字典可用于模拟现实生活中的字典，但为避免混淆，我们将后者称为词汇表。
想出你在前面学过的5个编程词汇，将它们用作词汇表中的键，并将它们的含义作为值存储在词汇表中。
以整洁的方式打印每个词汇及其含义。为此，你可以先打印词汇，在它后面加上一个冒号，再打印词汇的含义；也可在一行打印词汇，再使用换行符（\n ）插
入一个空行，然后在下一行以缩进的方式打印词汇的含义。
'''
python_dict = {
    "变量":"变量是一种存储数据的容器，它们可以存储各种类型的数据，比如数字、字符串、列表、字典等。",
    "控制流":"控制流是指程序执行过程中的决策和循环机制。",
    "函数":"函数是一种子程序，它可以接收输入（参数），执行一定的任务，并返回输出（返回值）。",
    "类":"类是一种用于封装数据和行为的结构。它们允许开发者定义具有特定属性和方法的对象。",
    "库":"库是一种包含了预先编写好的代码片段的集合，它们可以被用来解决各种常见的问题或者实现某些特定的功能。"
}
print("*"*100)
for key,value in python_dict.items():
    print(f"Python中{key}的基本概念是:{value}")

print("*"*100)
for key in python_dict.keys():
    print(f"{key}")

print("*"*100)
for key in sorted(python_dict.keys()):  #按顺序遍历字典中的所有键
    print(f"{key}")

print("*"*100)
for value in python_dict.values():
    print(f"{value}")

print("*"*100)
for value in sorted(python_dict.values()):
    print(f"按顺序遍历字典中的所有值：{value}")


'''
for语句提取字典中的每个值，并将它们依次存储到变量language 中。通过打印这些值，就获得了一个列表，其中包含被调查者选择的各种语言：
'''
#6.3.1 favorite_languages
print("*"*100)
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

favorite_languages_list = ""
for language in favorite_languages.values():
    favorite_languages_list+= language+"、"
favorite_languages_list=favorite_languages_list[:-1]
print(f"The following languages have been mentioned:{favorite_languages_list}")

'''
这种做法提取字典中所有的值，而没有考虑是否重复。涉及的值很少时，这也许不是问题，但如果被调查者很多，最终的列表可能包含大量的重复项。为剔除重复项，可使用集
合（set）。集合类似于列表，但每个元素都必须是独一无二的：
'''

favorite_languages_list = ""
for language in set(favorite_languages.values()):
    favorite_languages_list+= language+"、"
favorite_languages_list=favorite_languages_list[:-1]
print(f"The following languages have been mentioned:{favorite_languages_list}")


#动手试一试
'''
6-5 河流：创建一个字典，在其中存储三条大河流及其流经的国家。其中一个键—值对可能是'nile': 'egypt' 。
使用循环为每条河流打印一条消息，如“The Nile runs through Egypt.”。
使用循环将该字典中每条河流的名字都打印出来。
使用循环将该字典包含的每个国家的名字都打印出来。
'''
print("*"*100)
river = {
    "Nile":"Egypt",
    "Amazon River":"Brazil",
    "Yangtze River":"China",
    "Mississippi River":"USA",
    "Yellow River":"China"
}
for k,v in river.items():
    print(f"The {k} runs through {v}.")

'''
6-6 调查：在6.3.1节编写的程序favorite_languages.py中执行以下操作。
创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。
遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢。对于还未参与调查的人，打印一条消息邀请他参与调查。
'''
print("*"*100)
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
list_of_investigation =["sunwei","jen","phil","wangchao","xujuny","wangyan"]

for name in list_of_investigation:
    if name not in favorite_languages.keys():
        print(f"Hello,{name},would you like to accept to a investigation?")
    else:
        print(f"Thank you {name},I'm very grateful for your participation in the survey.")
