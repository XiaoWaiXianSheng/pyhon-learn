def test_return():
    return 1, "hello", True


x, y, z = test_return()

print(x, y, z)

'''多种传参方式'''


def user_info(name, age, sex):
    print(name, age, sex)


# 位置参数必须在关键字参数之前
user_info(name="MT", age=18, sex="man")

user_info(age=20, sex="women", name="XiaoMing")

user_info("Ming", sex="man", age="26")

'''缺省参数
    默认值参数必须写在最后'''


def user_info1(name, age=18, sex="man"):
    print(name, age, sex)


user_info1("", 18)

'''不定长参数'''
# 位置传递


def user_info2(*args):
    print(args)


user_info2(8, "Tom", True)

# 关键字传递


def user_info3(**kwargs):
    print(kwargs)


user_info3(name="Tom", age=18)

"""函数作为参数传递"""


def test_func(compute1):
    print(type(compute1))
    print(type(compute))
    result = compute1(1, 2)
    print(result)


def compute(x, y):
    return x + y


test_func(compute)

'''匿名函数 lambda
    只可临时使用一次
    函数体只能写一行'''
test_func(lambda xx, yy: xx + yy)



