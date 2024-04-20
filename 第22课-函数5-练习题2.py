'''
函数练习题
'''
#动手试一试
'''
8-9 魔术师：创建一个包含魔术师名字的列表，并将其传递给一个名为show_magicians() 的函数，这个函数打印列表中每个魔术师的名字。
'''
magicians = ["David Copperfield","Liu qian","Dynamo","Franz Harary","Jason Latimer","Criss Angel","Derren Brown","Houdini"]
def show_magicians(magicians):
    for magician in  magicians:
        print(f"\t{magician}",end=" ")

print("*"*100)
show_magicians(magicians)

'''
8-10 了不起的魔术师：在你为完成练习8-9而编写的程序中，编写一个名为make_great() 的函数，对魔术师列表进行修改，
在每个魔术师的名字中都加入字样“the Great”。调用函数show_magicians() ，确认魔术师列表确实变了。
'''
print("*"*100)
def make_great(magicians,new_list_of_magicians=[]):
    for magician in magicians:
        magician = "the Great"+" "+magician
        new_list_of_magicians.append(magician)
    print(f"Top 8 magicians in the world:")
    for item in new_list_of_magicians:
        print(f'\t·{item}')
make_great(magicians)





