name = "itheima is a brand of itcast"
i = 0
for x in name:
    if x == "a":
        i +=1
print(f"一共有{i}个a")

""" 
range(num) 获取一个从0开始到num（不包括num）结束的序列
range(num1, num2) 获取一个从num1开始，到num2（不包括num2）结束的序列
range(num1, num2, step)获取一个从num1开始，到num2（不包括num2）结束的序列  数字之间的步长为step（step默认为1）
"""

"""
for x in range(10):
    print("hello")
for x in  range(1,10,2):
    print(x)
"""
"""
for x in range(1,10):
    for y in range(1,x+1):
        print(f"{y} * {x}\t", end="")
    print()
"""

import random
money = 10000
for x in range(1,21):
    score = random.randint(1,10)
    if money <=0:
        break
    elif score < 5:
        print(f"员工{x}号，绩效分{score}，低于5，不发工资，下一位")
    else:
        money -=1000
        print(f"向员工{x}发放工资1000，账户余额还剩{money}")
print("工资发完了，下个月领取")

