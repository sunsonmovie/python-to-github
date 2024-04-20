'''
在你创建的列表中，元素的排列顺序常常是无法预测的，因为你并非总能控制用户提供数据的顺序。这虽然在大多数情况下都是不可避免的，但你经常需要以特定的顺序呈现信
息。有时候，你希望保留列表元素最初的排列顺序，而有时候又需要调整排列顺序。Python提供了很多组织列表的方式，可根据具体情况选用。
'''

#使用方法 使 sort() 对列表进行永久性排序
#1.按数字大小排序
num=[3,1,2,10,25,6,7]
num.sort()
print(num)

#2.按字母顺序排序
'''
Python方法sort() 让你能够较为轻松地对列表进行排序。假设你有一个汽车列表，并要让其中的汽车按字母顺序排列。为简化这项任务，我们假设该列表中的所有值都是小写
的。
'''
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars2=['bmw', 'audi', 'Toyota', 'Subaru',"红旗"]
cars2.sort()
print(cars2)

'''
按相反顺序排序
'''
cars.sort(reverse=True)
print(cars)

cars2.sort(reverse=True)
print(cars2)

#使用函数sorted()对列表进行临时排序
'''
要保留列表元素原来的排列顺序，同时以特定的顺序呈现它们，可使用函数sorted() 。函数sorted() 让你能够按特定顺序显示列表元素，同时不影响它们在列表中的原始排
列顺序。
'''
print("*"*100)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

'''
注意，调用函数sorted() 后，列表元素的排列顺序并没有变。如果你要按与字母顺序相反的顺序显示列表，也可向函数sorted() 传递参数reverse=True 。
'''
print("*"*100)
print(sorted(cars,reverse=True))

#倒着打印列表
'''
要反转列表元素的排列顺序，可使用方法reverse() 。假设汽车列表是按购买时间排列的，可轻松地按相反的顺序排列其中的汽车：
'''
print("*"*100)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

#确定列表的长度
'''
使用函数len() 可快速获悉列表的长度。在下面的示例中，列表包含4个元素，因此其长度为4：
'''
print("*"*100)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

#动手试一试

'''
3-8 放眼世界：想出至少5个你渴望去旅游的地方。
·将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。
·按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始Python列表。
·使用sorted() 按字母顺序打印这个列表，同时不要修改它。
·再次打印该列表，核实排列顺序未变。
·使用sorted() 按与字母顺序相反的顺序打印这个列表，同时不要修改它。
·再次打印该列表，核实排列顺序未变。
·使用reverse() 修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
·使用reverse() 再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
·使用sort() 修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
·使用sort() 修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。
'''
print("*"*100)
Tourist_list=["西安兵马俑","九寨沟","黄龙寨","石林","八达岭长城","故宫","西湖"]
print(Tourist_list)
print(sorted(Tourist_list))
print(Tourist_list)
print(sorted(Tourist_list,reverse=True))
print(Tourist_list)

print("*"*100)
Tourist_list.reverse()
print(Tourist_list)
Tourist_list.reverse()
print(Tourist_list)

print("*"*100)
Tourist_list.sort()
print(Tourist_list)

print("*"*100)
Tourist_list.sort(reverse=True)
print(Tourist_list)




'''
3-9 晚餐嘉宾：在完成练习3-4~练习3-7时编写的程序之一中，使用len() 打印一条消息，指出你邀请了多少位嘉宾来与你共进晚餐。
'''
print("*"*100)
guest_list=["王超","徐俊宇","王艳","栗栋栋","安志敏","谷晓峰"]
print(len(guest_list))

for i in range(len(guest_list)):
    print(f"嘉宾的名单有：{guest_list[i]}")

'''
3-10 尝试使用各个函数：想想可存储到列表中的东西，如山岳、河流、国家、城市、语言或你喜欢的任何东西。编写一个程序，在其中创建一个包含这些元素的列
表，然后，对于本章介绍的每个函数，都至少使用一次来处理这个列表。
'''
print("*"*100)
mountains=[]
mountains.insert(0,"东岳泰山")
print(mountains)
mountains.insert(1,"西岳华山")
print(mountains)
mountains.insert(2,"黄山")
print(mountains)
mountains.insert(3,"南岳衡山")
print(mountains)
mountains.insert(4,"中岳嵩山")
print(mountains)
print("*"*100)

for i in range(len(mountains)):
    print(mountains[i])

mountains[2] = "北岳恒山"
print(mountains)

sorted(mountains,reverse=True)
print(mountains)
print(sorted(mountains,reverse=True))

print(mountains[-1])


