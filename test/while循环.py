"""
num = 1
sum = 0
whjle num <= 100:
    sum += num
    num += 1
    print(sum)
"""
"""
import random

num = random.randint(1, 100)
guess = int(input("请猜第1次"))
time = 1

while guess != num:
    if guess > num:
        time += 1
        guess = int(input(f"猜大了，请猜第{time}次"))

    else:
        time += 1
        guess = int(input(f"猜小了，请猜第{time}次"))

print(f"恭喜你猜对了,总共{time}次猜对")
"""

"""
print("666", end="")   #end = ""  可以使输出不换行

print("1*3\t2*3")
print("11*3\t555*3")
"""

i = 1

while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={j * i}\t", end="")
        j += 1
    print("")
    i += 1
