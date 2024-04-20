'''
鉴于函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。向函数传递实参的方式很多，可使用位置实参 位 ，这要求实参的顺序与形参的顺序相同；也可使用关键关
字实参 字 ，其中每个实参都由变量名和值组成；还可使用列表和字典。下面来依次介绍这些方式。
'''

#位置实参
'''
你调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。为此，最简单的关联方式是基于实参的顺序。这种关联方式被称为位置实参 位 。
为明白其中的工作原理，来看一个显示宠物信息的函数。这个函数指出一个宠物属于哪种动物以及它叫什么名字，如下所示：
'''
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}\'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

'''
调用函数多次是一种效率极高的工作方式。我们只需在函数中编写描述宠物的代码一次，然后每当需要描述新宠物时，都可调用这个函数，并向它提供新宠物的信息。即便描述
宠物的代码增加到了10行，你依然只需使用一行调用函数的代码，就可描述一个新宠物。
在函数中，可根据需要使用任意数量的位置实参，Python将按顺序将函数调用中的实参关联到函数定义中相应的形参。
'''

'''
位置实参的顺序很重要
在这个函数调用中，我们先指定名字，再指定动物类型。由于实参'harry' 在前，这个值将存储到形参animal_type 中；同理，'hamster' 将存储到形参pet_name 中。
结果是我们得到了一个名为Hamster 的harry ：
'''
describe_pet('harry', 'hamster')  #如果结果像上面一样搞笑，请确认函数调用中实参的顺序与函数定义中形参的顺序一致。


#关键字实参
'''
关键字实参是传递给函数的名称—值对。你直接在实参中将名称和值关联起来了，因此向函数传递实参时不会混淆（不会得到名为Hamster的harry这样的结果）。
关键字实参让你无需考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。
'''

def describe_pet(animal_type="dog", pet_name="little black"):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}\'s name is {pet_name.title()}.")
print("*"*100)
describe_pet()
describe_pet(pet_name='little blue', animal_type='cat')

#默认值
'''编写函数时，可给每个形参指定默认值 默 。在调用函数中给形参提供了实参时，Python将使用指定的实参值；否则，将使用形参的默认值。因此，给形参指定默认值后，可在函数
调用中省略相应的实参。使用默认值可简化函数调用，还可清楚地指出函数的典型用法。
例如，如果你发现调用describe_pet() 时，描述的大都是小狗，就可将形参animal_type 的默认值设置为 'dog' 。这样，调用describe_pet() 来描述小狗时，就可不
提供这种信息：'''

def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type},",f"\nMy {animal_type}\'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
'''
请注意，在这个函数的定义中，修改了形参的排列顺序。由于给animal_type 指定了默认值，无需通过实参来指定动物类型，因此在函数调用中只包含一个实参——宠物的名
字。然而，Python依然将这个实参视为位置实参，因此如果函数调用中只包含宠物的名字，这个实参将关联到函数定义中的第一个形参。
'''
describe_pet("willie")

#等效的函数调用
'''
鉴于可混合使用位置实参、关键字实参和默认值，通常有多种等效的函数调用方式。
在任何情况下都必须给pet_name 提供实参；指定该实参时可以使用位置方式，也可以使用关键字方式。如果要描述的动物不是小狗，还必须在函数调用中
给animal_type 提供实参；同样，指定该实参时可以使用位置方式，也可以使用关键字方式。
'''
print("*"*100)
# 一条名为Willie的小狗
describe_pet('willie')
describe_pet(pet_name='willie')
# 一只名为Harry的仓鼠
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')






