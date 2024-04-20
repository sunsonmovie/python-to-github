"""
使用代码模拟实物时，你可能会发现自己给类添加的细节越来越多：属性和方法清单以及文件都越来越长。在这种情况下，可能需要将类的一部分作为一个独立的类提取出来。
你可以将大型类拆分成多个协同工作的小类。
例如，不断给ElectricCar 类添加细节时，我们可能会发现其中包含很多专门针对汽车电瓶的属性和方法。在这种情况下，我们可将这些属性和方法提取出来，放到另一个名
为Battery 的类中，并将一个Battery 实例用作ElectricCar 类的一个属性：
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

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")

    # def get_range(self):
    #     if self.battery_size==70:
    #         range=240
    #     elif self.battery_size==85:
    #         range=350
    #     print(f"This car can go approximately {range} miles on a full charge.")


class ElectriCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()

    def get_approximately_miles(self):
        if self.battery.battery_size==70:
            range=240
        elif self.battery.battery_size==85:
            range=350
        print(f"This car can go approximately {range} miles on a full charge.")

print("*"*100)
my_tesla=ElectriCar("Tesla","model S",2024)
my_tesla.battery.battery_size=85
my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
my_tesla.get_approximately_miles()
"""
在ElectricCar 类中，我们添加了一个名为self.battery 的属性。这行代码让Python创建一个新的Battery 实例（由于没有指定尺寸，因此为默认值70 ），并将
该实例存储在属性self.battery 中。每当方法__init__() 被调用时，都将执行该操作；因此现在每个ElectricCar 实例都包含一个自动创建的Battery 实例。
我们创建一辆电动汽车，并将其存储在变量my_tesla 中。要描述电瓶时，需要使用电动汽车的属性battery。
"""

"""
模拟较复杂的物件（如电动汽车）时，需要解决一些有趣的问题。续航里程是电瓶的属性还是汽车的属性呢？如果我们只需描述一辆汽车，那么将方法get_range() 放
在Battery 类中也许是合适的；但如果要描述一家汽车制造商的整个产品线，也许应该将方法get_range() 移到ElectricCar 类中。在这种情况下，get_range() 依然
根据电瓶容量来确定续航里程，但报告的是一款汽车的续航里程。我们也可以这样做：将方法get_range() 还留在Battery 类中，但向它传递一个参数，如car_model ；在
这种情况下，方法get_range() 将根据电瓶容量和汽车型号报告续航里程。
"""



