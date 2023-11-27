class Student:
    def __init__(self, name, age): # 构造方法在构建类对象的时候会自动执行
        self.name = name                # 构建类对象的传参会传递给构造方法
        self.age = age
        print("创建了Student类的对象")

    def __str__(self):
        return f"Student类对象，name:{self.name},age:{self.age}"

    '''lt用于小于符号比较'''
    def __lt__(self, other):
        return self.age < other.age

    '''le用于小于等于符号比较'''
    def __le__(self, other):
        return self.age <= other.age

    '''eq用于比较运算符'''
    def __eq__(self, other):
        return self.age == other.age


stu1 = Student("周杰伦", 31)
stu2 = Student("林俊杰", 36)

print(Student)
print(stu1)
print(stu1 < stu2)
print(stu1 > stu2)

print(stu1 <= stu2)

print(stu1 == stu2)