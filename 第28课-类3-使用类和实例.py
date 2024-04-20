'''
你可以使用类来模拟现实世界中的很多情景。类编写好后，你的大部分时间都将花在使用根据类创建的实例上。你需要执行的一个重要任务是修改实例的属性。你可以直接修改
实例的属性，也可以编写方法以特定的方式进行修改。
'''

class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model =model
        self.year = year

    def get_descriptive_name(self):
        long_name = print(f"{self.year} {self.make} make {self.model}.")


my_new_car = Car("audi","A4","2024")
my_new_car.get_descriptive_name()


#给属性制定默认值
"""
类中的每个属性都必须有初始值，哪怕这个值是0或空字符串。在有些情况下，如设置默认值时，在方法__init__() 内指定这种初始值是可行的；如果你对某个属性这样做
了，就无需包含为它提供初始值的形参。下面来添加一个名为odometer_reading 的属性，其初始值总是为0。我们还添加了一个名为read_odometer() 的方法，用于读取
汽车的里程表：
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

my_car_02 =Car("toyota","S4",2023)
my_car_02.read_odometer()


#修改属性的值
"""
要修改属性的值，最简单的方式是通过实例直接访问它
"""
my_car_02.odometer=1000
my_car_02.read_odometer()

"""
通过方法修改属性的值
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
print("*"*100)
my_car_03 =Car("toyota","S4",2023)
my_car_03.up_odometer(23)
my_car_03.read_odometer()


#通过方法对属性的值进递增
"""
有时候需要将属性值递增特定的量，而不是将其设置为全新的值。假设我们购买了一辆二手车，且从购买到登记期间增加了100英里的里程，下面的方法让我们能够传递这个增
量，并相应地增加里程表读数：
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
my_car_04 =my_car_03 =Car("toyota","S4",2023)
my_car_04.increment_odometer(500)
my_car_04.read_odometer()
my_car_04.increment_odometer(1000)
my_car_04.read_odometer()
my_car_04.increment_odometer("2000")
my_car_04.read_odometer()














