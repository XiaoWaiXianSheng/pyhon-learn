def tem(x):
    if x <= 37.5:
        print("体温正常")
    else:
        print("请隔离")


a = type(tem(38))
print(a)


def check_age(x):
    """
    对函数进行多行注释
    :param x:形参x表示年龄
    :return:返回值
    """
    if x > 18:
        return "success"
    else:
        return None


result = check_age(16)
if not result:
    print("未成年")

"""
# 变量的作用域

num = 200


def test_a():
    num = 300
    print(f"test_a:{num}")
    return num

def test_b():
    num = 500
    print(f"test_b:{num}")


test_a()
test_b()
print(num)
"""


# global关键字
num = 200


def test_a():
    global num
    num = 300
    print(f"test_a:{num}")
    return num

def test_b():
    global num
    num = 500
    print(f"test_b:{num}")


test_a()
test_b()
print(num)