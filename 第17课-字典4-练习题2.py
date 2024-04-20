'''
练习题2
'''
'''
6-8 宠物：创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；在每个字典中，包含宠物的类型及其主人的名字。
将这些字典存储在一个名为pets 的列表中，再遍历该列表，并将宠物的所有信息都打印出来。
'''
print("*"*100)
Persian_Cat = {
    "type":"cat",
    "master":"xujunyu",
    "favorite_foods":["fish","meet","milk"]
}
Golden_Retriever = {
    "type":"dog",
    "master":"sun wei",
    "favorite_foods":["bone","meet","watermelon"]
}
Baisuzhen = {
    "type":"snake",
    "master":"Xuxian",
    "favorite_foods":["rice","mouse","tomato"]
}
Pets = [Persian_Cat,Golden_Retriever,Baisuzhen]
for item in Pets:
    print(f"A {item['type']}",f"\nHer master is {item['master']}.")
    print(f"Her favorite foods is:")
    for food in item['favorite_foods']:
        print(f'\t{food}')
    print("*"*100)


'''
6-9 喜欢的地方：创建一个名为favorite_places 的字典。在这个字典中，将三个人的名字用作键；对于其中的每个人，都存储他喜欢的1~3个地方。为让这个练
习更有趣些，可让一些朋友指出他们喜欢的几个地方。遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。
'''
print("*"*100)
favorite_places = {
    "孙炜":['西安',"成都","三亚"],
    "王超":["北京","苏州","杭州"],
    "王艳":["西安","西藏","新疆","黑龙江","云南"]
}
for name in favorite_places.keys():
    print(f"{name}最喜欢旅游的地方有：")
    for place in favorite_places[name]:
        print(f"\t·{place}")
    print("*"*100)

'''
6-10 喜欢的数字：修改为完成练习6-2而编写的程序，让每个人都可以有多个喜欢的数字，然后将每个人的名字及其喜欢的数字打印出来。
'''
favorite_numbers ={
    "孙炜":[7,5,3,18,13,5],
    "徐俊宇":[6,8,10,9],
    "王超":[12,24,100],
    "王艳":[100,10000,0,1],
    "栗栋栋":[1,0,100,101]
}
for name in favorite_numbers.keys():
    print(f"{name}最喜欢的数字有：")
    for number in favorite_numbers[name]:
        print(f"\t{number}")
    print("*"*100)

'''
6-11 城市：创建一个名为cities 的字典，其中将三个城市名用作键；对于每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该
城市的美食。在表示每座城市的字典中，应包含country 、population 和food 等键。将每座城市的名字以及有关它们的信息都打印出来。
'''
print("*"*100)
cities = {
    "西安":{
        "国家":"中国",
        "人口":"1300万",
        "美食":["肉夹馍","臊子面","凉皮","酸汤水饺","羊肉泡馍"]
    },
    "东京":{
        "国家":"日本",
        "人口":"1400万",
        "美食":["寿司","拉面","生鱼片"]
    },
    "巴黎":{
        "国家":"法国",
        "人口":"200万",
        "美食":["法式洋葱汤","法式蜗牛","鹅肝酱","法式千层酥"]
    }
}
for city,city_info in cities.items():
    print(f"{city}属于{city_info['国家']},有{city_info['人口']}人口，拥有脍炙人口的美食：")
    for favorite_food in city_info['美食']:
        print(f"\t·{favorite_food}")


