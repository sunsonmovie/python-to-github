
'''
动手试一试
'''

'''
8-12 三明治：编写一个函数，它接受顾客要在三明治中添加的一系列食材。这个函数只有一个形参（它收集函数调用中提供的所有食材），并打印一条消息，对顾客
点的三明治进行概述。调用这个函数三次，每次都提供不同数量的实参。
'''
def make_sandwich(size,*toppings):
    print(f"Making a {size}-inch sandwich with the following toppings:")
    for item in toppings:
        print(f"\t-{item}")
make_sandwich(12,"Turkey")
make_sandwich(16,"Turkey","Ham","Sausage")
make_sandwich(18,"Turkey","Ham","Sausage","Vegetarian","Meatballs")

'''
8-13 用户简介：复制前面的程序user_profile.py，在其中调用build_profile() 来创建有关你的简介；调用这个函数时，指定你的名和姓，以及三个描述你的键-值
对。
'''
def build_profile(name,**user_info):
    person_profile={}
    person_profile["name"]=name
    for key,value in user_info.items():
        person_profile[key]=value
    return person_profile

sunwei=build_profile('孙炜',性别="男",祖籍="江苏·泗洪",身高=170,公司="五得利集团宿迁面粉有限公司",职位="行政办事员")
print(sunwei)
wangyan=build_profile("王艳",祖籍="江苏·临沂",公司="五得利集团宿迁面粉有限公司",职位="人事办事员")
print(wangyan)

'''
8-14 汽车：编写一个函数，将一辆汽车的信息存储在一个字典中。这个函数总是接受制造商和型号，还接受任意数量的关键字实参。这样调用这个函数：提供必不可
少的信息，以及两个名称—值对，如颜色和选装配件。这个函数必须能够像下面这样进行调用：
'''

def car(color,accessories,**car_information):
    car_info={}
    car_info["color"]=color
    car_info["accessories"]=accessories
    for key,value in car_information.items():
        car_info[key]=value
    return car_info
car_1=car("绿色","涡轮增压",车型="轿跑",发动机="插电混合动力")
print(car_1)









