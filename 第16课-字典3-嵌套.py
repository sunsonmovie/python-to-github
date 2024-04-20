'''
复杂的数据结构：
有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套嵌 。你可以在列表中嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典。正如下面的示例
将演示的，嵌套是一项强大的功能。
'''

#字典列表
'''
字典alien_0 包含一个外星人的各种信息，但无法存储第二个外星人的信息，更别说屏幕上全部外星人的信息了。如何管理成群结队的外星人呢？一种办法是创建一个外星人列
表，其中每个外星人都是一个字典，包含有关该外星人的各种信息。例如，下面的代码创建一个包含三个外星人的列表：
'''
print("*"*100)
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

'''
更符合现实的情形是，外星人不止三个，且每个外星人都是使用代码自动生成的。在下面的示例中，我们使用range() 生成了30个外星人：
'''
# 创建一个用于存储外星人的空列表
print("*"*100)
import random
aliens = []
speed = ["slow","medium","fast"]

# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points':random.randint(5,20), 'speed': random.choice(speed)}
    aliens.append(new_alien)
# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")
# 显示创建了多少个外星人
print(f"Total number of aliens:{len(aliens)}")


#在字典中存储列表
'''
有时候，需要将列表存储在字典中，而不是将字典存储在列表中。例如，你如何描述顾客点的比萨呢？如果使用列表，只能存储要添加的比萨配料；但如果使用字典，就不仅可
在其中包含配料列表，还可包含其他有关比萨的描述。
在下面的示例中，存储了比萨的两方面信息：外皮类型和配料列表。其中的配料列表是一个与键 'toppings' 相关联的值。要访问该列表，我们使用字典名和键 'toppings' ，
就像访问字典中的其他值一样。这将返回一个配料列表，而不是单个值：
'''
print("*"*100)
# 存储所点比萨的信息
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese']
}
# 概述所点的比萨
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

'''
每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表。在本章前面有关喜欢的编程语言的示例中，如果将每个人的回答都存储在一个列表中，被调查者就
可选择多种喜欢的语言。在这种情况下，当我们遍历字典时，与每个被调查者相关联的都是一个语言列表，而不是一种语言；因此，在遍历该字典的for 循环中，我们需要再使
用一个for 循环来遍历与被调查者相关联的语言列表：
'''
favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}
for name,langusge in favorite_languages.items():
    print(f"{name}'s favorite langusge is :")
    for langusge in favorite_languages[name]:
        print("\t"+langusge)

#在字典中存储字典
'''
可在字典中嵌套字典，但这样做时，代码可能很快复杂起来。例如，如果有多个网站用户，每个都有独特的用户名，可在字典中将用户名作为键，然后将每位用户的信息存储在
一个字典中，并将该字典作为与用户名相关联的值。在下面的程序中，对于每位用户，我们都存储了其三项信息：名、姓和居住地；为访问这些信息，我们遍历所有的用户名，
并访问与每个用户名相关联的信息字典：
'''
print("*"*100)
users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}
for username,user_info in users.items():
    print(f"Username:{username.title()}'s full_name:{user_info['first'].title()+' '+user_info['last'].title()}"+f"\n\t location:{user_info['location']}")



#动手试一试
'''
6-7 人 ：在为完成练习6-1而编写的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个名为people 的列表中。遍历这个列表，将其中每个人的所有
信息都打印出来。
'''
print("*"*100)
people_dict_1 = {
"first_name":"sun",
"last_name":"wei",
"age":"40",
"city":"suq,ian"
}
people_dict_2 ={
    "first_name":"wang",
    "last_name":"chao",
    "age":"35",
    "city":"suqian"
}
people_dict_3 = {
    "first_name":"wang",
    "last_name":"yan",
    "age":"30",
    "city":"linyi"
}
people = [people_dict_1,people_dict_2,people_dict_3]

for item in people:
    print(f'{item['first_name'].title()} {item['last_name'].title()}\'s age is:{item['age']} and his city is:{item['city']}')






