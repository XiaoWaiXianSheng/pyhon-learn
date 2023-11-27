class Student:
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel): # 构造方法在构建类对象的时候会自动执行
        self.name = name                # 构建类对象的传参会传递给构造方法
        self.age = age
        self.tel = tel
        print("创建了Student类的对象")


stu = Student("Ming", 18, 88886666)
print(stu.name)
print(stu.age)
print(stu.tel)