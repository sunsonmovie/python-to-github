"""
动手试一试
"""
"""
9-4 就餐人数：在为完成练习9-1而编写的程序中，添加一个名为number_served 的属性，并将其默认值设置为0。根据这个类创建一个名为restaurant 的实
例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。添加一个名为set_number_served() 的方法，它让你能够设置就餐人数。调用这个方法并向它
传递一个值，然后再次打印这个值。添加一个名为increment_number_served() 的方法，它让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值：你
认为这家餐馆每天可能接待的就餐人数。
"""

class Restaurant():
    def __init__(self,restaurant_name,restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"这家旅馆的名字是{self.restaurant_name},类型是{self.restaurant_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name}正在营业。")

    def set_number_served(self,number):
        if not isinstance(number,int) or number<0:
            print(f"服务的人数必须是数值且不能为负值！")
            return ValueError
        else:
            self.number_served+=number

    def increment_number_served(self):
        print(f"这家餐厅服务过的人数为:{self.number_served}")

my_restaurant=Restaurant("骆马湖国宾馆","五星级")
my_restaurant.set_number_served(20)
my_restaurant.increment_number_served()
my_restaurant.set_number_served(80)
my_restaurant.increment_number_served()


"""
9-5 尝试登录次数：在为完成练习9-3而编写的User 类中，添加一个名为login_attempts 的属性。编写一个名为increment_login_attempts() 的方法，
它将属性login_attempts 的值加1。再编写一个名为reset_login_attempts() 的方法，它将属性login_attempts 的值重置为0。根据User 类创建一个
实例，再调用方法increment_login_attempts() 多次。打印属性login_attempts 的值，确认它被正确地递增；然后，调用方法reset_login_attempts() ，
并再次打印属性login_attempts 的值，确认它被重置为0。
"""
class User():
    def __init__(self,first_name,last_name,age=40):
        user_info=[]
        self.first_name= first_name
        self.last_name= last_name
        self.name = self.first_name + self.last_name
        self.age =age
        self.login_attempts=0

    def describe_user(self):
        print(f"{self.name}姓{self.first_name}名{self.last_name},年龄{self.age}岁.")

    def greet_user(self):
        print(f"Hello {self.name},welcome to my home.")

    def increment_login_attempts(self,num):
        if not isinstance(num,int) or num<0:
            print(f"登录次数必须是数值且不能为负值！")
            return ValueError
        else:
            self.login_attempts+=num
            print(f"你登录了{self.login_attempts}次.")

    def reset_login_attempts(self):
        self.login_attempts=0
        print(f"登录次数已重置！")

my_user=User("sun","wei")
my_user.increment_login_attempts(10)
my_user.reset_login_attempts()
print(my_user.login_attempts)








