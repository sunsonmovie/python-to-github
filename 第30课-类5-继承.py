"""
编写类时，并非总是要从空白开始。如果你要编写的类是另一个现成类的特殊版本，可使用继承继 。一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；原有的
类称为父类 ，而新类称为子类。子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。
"""
class ParentClass:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"My name is {self.name}")

class ChildClass(ParentClass):
    def __init__(self, name, age):
        super().__init__(name)  # 调用父类的构造函数
        self.age = age

# 创建 ChildClass 的实例
child = ChildClass("Alice", 25)

# 调用继承自父类的方法
child.display_name()

# 访问子类特有的属性
print(f"Age: {child.age}")

"""
在上述示例中：ParentClass 是父类，具有 name 属性和 display_name 方法。ChildClass 是子类，继承自 ParentClass。
在子类的构造函数中，使用 super().__init__(name) 调用父类的构造函数，以初始化父类的属性。
子类还添加了自己的属性age。通过创建子类的实例，可以使用继承自父类的方法和子类特有的属性。
继承的好处包括代码的重用和扩展，使得子类可以在父类的基础上添加新的功能或修改现有功能。
"""



class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model =model
        self.year = year
        self.odometer=0

    def get_descriptive_name(self):
        long_name = print(f"{self.year} {self.make} make {self.model}.")

    def read_odometer(self):
        print(f"This car has {self.odometer} miles on it.")

    def up_odometer(self,mileage):
        self.odometer = mileage

    def increment_odometer(self,mileage):
        if not isinstance(mileage,int) or mileage<0:
            print(f"行驶里程必须是数值且不能为负值！")
        else:
            self.odometer+=mileage
print("*"*100)
my_car=Car("TOYOTA","Proda",2024)
my_car.up_odometer(1000)
my_car.increment_odometer(2000)
print(my_car.odometer)

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size=500

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")

print("*"*100)
your_car=ElectricCar("Tesla","model S",2023)
print(your_car.odometer)
your_car.increment_odometer(10000)
your_car.battery_size=1000
your_car.describe_battery()

#重写父类的方法
"""
对于父类的方法，只要它不符合子类模拟的实物的行为，都可对其进行重写。为此，可在子类中定义一个这样的方法，即它与要重写的父类方法同名。这样，Python将不会考虑这
个父类方法，而只关注你在子类中定义的相应方法。
假设Car 类有一个名为fill_gas_tank() 的方法，它对全电动汽车来说毫无意义，因此你可能想重写它。下面演示了一种重写方式：
"""

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size=500

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")

    def fill_gas_tank(self):
        print(f"This car doesn't need a gas tank!")






























