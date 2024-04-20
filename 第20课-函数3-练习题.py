#动手试一试
'''
8-3 T恤：编写一个名为make_shirt() 的函数，它接受一个尺码以及要印到T恤上的字样。这个函数应打印一个句子，概要地说明T恤的尺码和字样。
使用位置实参调用这个函数来制作一件T恤；再使用关键字实参来调用这个函数。
'''
def make_shirt(size,type="Made in China"):
    print(f"Make a size {size} T_Shirt with the type of {type}. ")
print("*"*100)
make_shirt(22)

'''
8-4 大号T恤 ：修改函数make_shirt() ，使其在默认情况下制作一件印有字样“I love Python”的大号T恤。调用这个函数来制作如下T恤：一件印有默认字样的大号T
恤、一件印有默认字样的中号T恤和一件印有其他字样的T恤（尺码无关紧要）。
'''
def make_shirt(size="大号",type="I Love Python"):
    print(f"Make a size {size} T_Shirt with the type of {type}. ")

make_shirt()
make_shirt("中号")
make_shirt(type="I Love China")


'''
8-5 城市：编写一个名为describe_city() 的函数，它接受一座城市的名字以及该城市所属的国家。这个函数应打印一个简单的句子，如Reykjavik is in
Iceland 。给用于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。
'''
def describe_city(city_name,city_of_country="CHINA"):
    print(f"{city_name.upper()} is the capital of {city_of_country}.")
print("*"*100)
describe_city("BeiJing")
describe_city("tokyo","JAPAN")
describe_city(city_of_country="USA",city_name="nanjing")

#返回值
'''
函数并非总是直接显示输出，相反，它可以处理一些数据，并返回一个或一组值。函数返回的值被称为返回值 返 。在函数中，可使用return 语句将值返回到调用函数的代码行。
返回值让你能够将程序的大部分繁重工作移到函数中去完成，从而简化主程序。
'''
print("*"*100)
def get_formatted_name(first_name, last_name):
    full_name = first_name +" "+last_name
    return full_name.title()
my_name=get_formatted_name("孙","炜")
print(my_name)

'''
假设我们要扩展函数get_formatted_name() ，使其还处理中间名。
然而，并非所有的人都有中间名，但如果你调用这个函数时只提供了名和姓，它将不能正确地运行。为让中间名变成可选的，可给实参middle_name 指定一个默认值——空字
符串，并在用户没有提供中间名时不使用这个实参。为让get_formatted_name() 在没有提供中间名时依然可行，可给实参middle_name 指定一个默认值——空字符串，
并将其移到形参列表的末尾：
'''
def get_formatted_name(first_name,last_name,middle_name=""):  #有默认值的形参要放在无默认值的形参的后面
    full_name = first_name +" "+middle_name+" "+last_name
    return full_name.title()

my_name=get_formatted_name("jimi","hendrix")
print(my_name)

my_name=get_formatted_name("jimi","hendrix",middle_name="alexander")
print(my_name)

#返回字典
'''
函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。例如，下面的函数接受姓名的组成部分，并返回一个表示人的字典：
'''
def build_person(first_name, last_name):
    person = {'first_name': first_name, 'last_name': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)
'''
这个函数接受简单的文本信息，将其放在一个更合适的数据结构中，让你不仅能打印这些信息，还能以其他方式处理它们。当前，字符串 'jimi' 和 'hendrix' 被标记为名和
姓。你可以轻松地扩展这个函数，使其接受可选值，如中间名、年龄、职业或你要存储的其他任何信息。例如，下面的修改让你还能存储年龄：
'''
def build_person(first_name, last_name,age='',middle_name=''):
    person={
        "first_name":first_name.title(),
        "middle_name":middle_name.title(),
        "last_name":last_name.title(),
    }
    if age:
        person['age']=age
    return person
my_person = build_person("jimi","hendrix",age=27)
print("*"*100)
print(my_person)

my_person = build_person("jimi","hendrix",middle_name="alexander")
print("*"*100)
print(my_person)


'''
8-6 城市名 城 ：编写一个名为city_country() 的函数，它接受城市的名称及其所属的国家。这个函数应返回一个格式类似于下面这样的字符串：
"Santiago belong to Chile"
'''
def city_belongto_country(city_name,city_of_country):
    message =print(f"{city_name}属于{city_of_country}.")
    return message
city_belongto_country('西安',"中国")
city_belongto_country("伦敦","英国")

'''
8-7 专辑：编写一个名为make_album() 的函数，它创建一个描述音乐专辑的字典。这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。使
用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
给函数make_album() 添加一个可选形参，以便能够存储专辑包含的歌曲数。如果调用这个函数时指定了歌曲数，就将这个值添加到表示专辑的字典中。调用这个
函数，并至少在一次调用中指定专辑包含的歌曲数。
'''
def make_album(singer,name_of_album,number_of_songs=10):
    music_album={
        "singer":singer,
        "name_of_album":name_of_album,
        "number_of_songs":number_of_songs
    }
    return music_album
my_album =make_album("光良","第一次")
print(my_album)
my_album =make_album("张信哲","就懂了",number_of_songs=9)
print(my_album)










