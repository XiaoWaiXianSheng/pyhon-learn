class Student:
    name = None

    def say_hi(self):
        print("Hello")

    def say_hi2(self,msg):
        print(f"Hello {self.name}, {msg}")


stu = Student()
stu.name = "Ming"
stu.say_hi()
stu.say_hi2("很高兴认识大家")