"""
动手试一试
"""
"""
9-1 餐馆：创建一个名为Restaurant 的类，其方法__init__() 设置两个属性：restaurant_name 和cuisine_type 。创建一个名
为describe_restaurant() 的方法和一个名为open_restaurant() 的方法，其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
"""
class Restaurant():
    def __init__(self,restaurant_name,restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type

    def describe_restaurant(self):
        print(f"这家旅馆的名字是{self.restaurant_name},类型是{self.restaurant_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name}正在营业。")

my_restaurant = Restaurant("喜来登大酒店","五星级")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print(my_restaurant.restaurant_name)
print(my_restaurant.restaurant_type)

"""
9-2 三家餐馆：根据你为完成练习9-1而编写的类创建三个实例，并对每个实例调用方法describe_restaurant() 。
"""
your_restaurant = Restaurant("希尔顿酒店","五星级")
her_restaurant = Restaurant("骆马湖假日酒店","四星级")
my_brother_restaurant =Restaurant("钓鱼台国宾馆","七星级")

your_restaurant.describe_restaurant()
her_restaurant.open_restaurant()
my_brother_restaurant.open_restaurant()
my_brother_restaurant.describe_restaurant()

"""
9-3 用户：创建一个名为User 的类，其中包含属性first_name 和last_name ，还有用户简介通常会存储的其他几个属性。在类User 中定义一个名
为describe_user() 的方法，它打印用户信息摘要；再定义一个名为greet_user() 的方法，它向用户发出个性化的问候。
"""
class User():
    def __init__(self,first_name,last_name,age=40):
        user_info=[]
        self.first_name= first_name
        self.last_name= last_name
        self.name = self.first_name + self.last_name
        self.age =age


    def describe_user(self):
        print(f"{self.name}姓{self.first_name}名{self.last_name},年龄{self.age}岁.")

    def greet_user(self):
        print(f"Hello {self.name},welcome to my home.")


my_user =User("孙","炜")
my_user.describe_user()
my_user.greet_user()
print(my_user.age)













