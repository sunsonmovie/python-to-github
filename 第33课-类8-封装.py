"""
承接上一节，学了Student类的定义及实例化，每个实例都拥有各自的name和score。现在若需要打印一个学生的成绩，可定义函数 print_score()
该函数为类外的函数，如下：
"""
class Student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

May = Student("May",90) # 须要提供两个属性
Peter = Student("Peter",85)
print(May.name, May.score)
print(Peter.name, Peter.score)

def print_score(Student):
    print(f"{Student.name}'s score is：{Student.score}.")

print_score(May)
print_score(Peter)


"""
既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，我们可以直接在Student类的内部定义访问数据的函数。这样，就把数据给“封装”起来了。
“封装”就是将抽象得到的数据和行为（或功能）相结合，形成一个有机的整体（即类）；封装的目的是增强安全性和简化编程，使用者不必了解具体的实现细节，而只是要通过外部接口，
一特定的访问权限来使用类的成员。而这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法。
那如何定义类的方法呢？就要用到对象 self 本身，参考上例，把 print_score() 函数写为类的方法：
"""
class Student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print(f"{self.name}'s score is:{self.score}.")
print("*"*100)
May = Student("May",90)
Peter = Student("Peter",85)
May.print_score()
Peter.print_score()

"""
定义类的方法：除了第一个参数是self外，其他和普通函数一样。
实例调用方法：只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入；注意，若类的方法仅需要self，不需要其他，调用该方法时，仅需 instance_name.function_name()
这样一来，我们从外部看Student类，就只需要知道，创建实例需要给出name和score，而如何打印，都是在Student类的内部定义的，这些数据和逻辑被“封装”起来了，调用很容易，但却不用
知道内部实现的细节。封装的另一个好处是可以给Student类增加新的方法；这边的方法也可以要求传参，如新增定义compare 函数，如下：
"""
class Student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print(f"{self.name}'s score is:{self.score}.")

    def compare(self,s):
        if self.score>s:
            print(f"better than {s}.")
        elif self.score==s:
            print(f"equal {s}.")
        else:
            print(f"lower than {s}.")
print("*"*100)
May = Student("May",90)
Peter = Student("Peter",85)
May.print_score()
Peter.print_score()
May.compare(100)
May.compare(90)
May.compare(89)







