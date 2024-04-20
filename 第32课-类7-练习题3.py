"""
动手试一试
"""
"""
解决问题时，你从较高的逻辑层面（而不是语法层面）考虑；你考虑的不是Python，而是如何使用代码来表示实物。到达这种境界后，你经常会发现，
现实世界的建模方法并没有对错之分。有些方法的效率更高，但要找出效率最高的表示法，需要经过一定的实践。只要代码像你希望的那样运行，就说明你
做得很好！即便你发现自己不得不多次尝试使用不同的方法来重写类，也不必气馁；要编写出高效、准确的代码，都得经过这样的过程。
"""
"""
9-6 冰淇淋小店：冰淇淋小店是一种特殊的餐馆。编写一个名为IceCreamStand 的类，让它继承你为完成练习9-1或练习9-4而编写的Restaurant 类。这两个版
本的Restaurant 类都可以，挑选你更喜欢的那个即可。添加一个名为flavors 的属性，用于存储一个由各种口味的冰淇淋组成的列表。编写一个显示这些冰淇淋
的方法。创建一个IceCreamStand 实例，并调用这个方法。
"""
from module.Restaurant import Restaurant
print("*"*100)
my_restaurant=Restaurant("骆马湖国宾馆","五星级")
my_restaurant.describe_restaurant()
my_restaurant.set_number_served(100)
my_restaurant.increment_number_served()
print("*"*100)

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,restaurant_type):
        super().__init__(restaurant_name,restaurant_type)
        self.flavors=[]

    def append_flavors(self,*flavors):
        for item in flavors:
            self.flavors.append(item)

    def get_flavors(self):
        print(f"Customers' favorite flavors include:")
        for item in self.flavors:
            print(f"\t{item}")

my_icecreamstand=IceCreamStand("三台山森林酒店","三星级")
my_icecreamstand.append_flavors("牛奶味","草莓味","芒果味","双拼")
my_icecreamstand.get_flavors()
print("*"*100)

"""
9-7 管理员：管理员是一种特殊的用户。编写一个名为Admin 的类，让它继承你为完成练习9-3或练习9-5而编写的User 类。添加一个名为privileges 的属性，用
于存储一个由字符串（如"can add post" 、"can delete post" 、"can ban user" 等）组成的列表。编写一个名为show_privileges() 的方法，它
显示管理员的权限。创建一个Admin 实例，并调用这个方法。
"""
from module.User import User

class Privileges():
    def __init__(self):
        self.privileges=["can add post" ,"can delete post","can ban user"]
    def show_privileges(self):
        for item in self.privileges:
            print(f"\t·{item}")

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        # self.privileges=["can add post" ,"can delete post","can ban user"]
        self.privileges=Privileges()
    # def show_privileges(self):
    #     for item in self.privileges:
    #         print(f"\t·{item}")

my_admin=Admin("sun","wei")
# my_admin.show_privileges()
print("*"*100)

"""
9-8 权限：编写一个名为Privileges 的类，它只有一个属性——privileges ，其中存储了练习9-7 所说的字符串列表。将方法show_privileges() 移到这
个类中。在Admin 类中，将一个Privileges 实例用作其属性。创建一个Admin 实例，并使用方法show_privileges() 来显示其权限。
"""

my_privileges=Admin("sun","wei")
my_privileges.privileges.show_privileges()


"""
9-9 电瓶升级：在本节最后一个electric_car.py版本中，给Battery 类添加一个名为upgrade_battery() 的方法。这个方法检查电瓶容量，如果它不是85，就将它
设置为85。创建一辆电瓶容量为默认值的电动汽车，调用方法get_range() ，然后对电瓶进行升级，并再次调用get_range() 。你会看到这辆汽车的续航里程增加了。
"""

from module.Car import Car,Battery,ElectriCar

my_electric_car=ElectriCar("Tesla","model S",2024)
my_electric_car.battery.upgrade_battery()
my_electric_car.battery.battery_size=70
my_electric_car.get_approximately_miles()
print("*"*100)
my_electric_car.battery.upgrade_battery()
my_electric_car.get_approximately_miles()























