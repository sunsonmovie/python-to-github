'''
有时候，你预先不知道函数需要接受多少个实参，好在Python允许函数从调用语句中收集任意数量的实参。
例如，来看一个制作比萨的函数，它需要接受很多配料，但你无法预先确定顾客要多少种配料。下面的函数只有一个形参*toppings ，但不管调用语句提供了多少实参，这个
形参都将它们统统收入囊中：
'''
def make_pizza(*toppings):
    print(f"Making a pizza with the following toppings:")
    for item in toppings:
        print(f"\t-{item}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
'''
基于上述函数定义，Python将收到的第一个值存储在形参size 中，并将其他的所有值都存储在元组toppings 中。在函数调用中，首先指定表示比萨尺寸的实参，然后根据需要
指定任意数量的配料。
'''

'''
如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
例如，如果前面的函数还需要一个表示比萨尺寸的实参，必须将该形参放在形参*toppings 的前面：
'''
def make_pizza(size,*toppings):
    print(f"Making a  {size}-inch pizza with the following toppings:")
    for item in toppings:
        print(f"\t-{item}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


#使用任意数量的关键字实参
'''有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。在这种情况下，可将函数编写成能够接受任意数量的键—值对——调用语句提供了多少就接
受多少。一个这样的示例是创建用户简介：你知道你将收到有关用户的信息，但不确定会是什么样的信息。在下面的示例中，函数build_profile() 接受名和姓，同时还接受
任意数量的关键字实参：
'''
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)

'''
函数build_profile() 的定义要求提供名和姓，同时允许用户根据需要提供任意数量的名称—值对。形参**user_info 中的两个星号让Python创建一个名为user_info 的
空字典，并将收到的所有名称—值对都封装到这个字典中。在这个函数中，可以像访问其他字典那样访问user_info 中的名称—值对。
'''




















