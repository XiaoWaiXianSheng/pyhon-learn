""""
age = int(input("你的年龄\n"))
if age >= 18:
    print("已经成年")
else:
    print("未成年")
"""

"""
number = 10

if int(input("你猜的数字\n")) == number:
    print("恭喜你猜对了")
elif int(input("不对，再猜一次\n")) == number:
    print("恭喜你猜对了")
elif int(input("不对，再猜一次\n")) == number:
    print("恭喜你猜对了")
else:
    print("全部错误，我的数字是10")
"""

"""
if 18 <= int(input("你的年龄")) <= 30:
    if int(input("年龄符合，请问你的入职时间是")) >= 2:
        print("恭喜你获得礼物")
    elif int(input("入职时间太短，请问你的级别是")) >= 3:
        print("恭喜你获得礼物")
    else:
        print("您的级别不符合，未能获得礼物")
else:
    print("您的年龄不符合，未能获得礼物")
"""

"""
第一种方式
import random

num = random.randint(1, 10)

number = int(input("请猜第一次"))
if number == num:
    print("恭喜你猜对了")
elif number > num:
    print("猜大了")
else:
    print("猜小了")
number = int(input("请猜第二次"))
if number == num:
    print("恭喜你猜对了")
elif number > num:
    print("猜大了")
else:
    print("猜小了")
number = int(input("请猜第三次"))
if number == num:
    print("恭喜你猜对了")
else:
    print("次数用尽，没有猜对")
"""

import random

num = random.randint(1, 10)

number = int(input("请猜第一次"))
if number == num:
    print("恭喜你猜对了")
else:
    if number > num:
        print("猜大了")
    else:
        print("猜小了")
    number = int(input("请猜第二次"))
    if number == num:
        print("恭喜你猜对了")
    else:
        if number > num:
            print("猜大了")
        else:
            print("猜小了")
        number = int(input("请猜第三次"))
        if number == num:
            print("恭喜你猜对了")
        else:
            print("次数用尽，没有猜对")