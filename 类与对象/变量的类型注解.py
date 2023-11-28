import json
import random

var_1: int = 10
var_2: str = "itheima"
var_3: bool = True


class Student:
    pass


stu: Student = Student()

my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {"itheima": 666}


my_list01: list[int] = [1, 2, 3]
my_tuple01: tuple[int, str, bool] = (1, "itheima", True)
my_dict01: dict[str, int] = {"itheima": 666}


var_4 = random.randint(1, 10)   # type: int
var_5 = json.loads("data")            # type: dict

def func():
    return 10


var_6 = func()                        # type: int
