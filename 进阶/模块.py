"""使用import导入time模块的全部函数"""

import time

print("你好")
time.sleep(5)
print("hello")


"""使用from导入time的sleep函数"""
from time import sleep

print("你好")
sleep(5)
print("hello")

"""使用*导入time的全部功能"""
from time import *
print("nihao")
sleep(6)
print(6)

"""使用as定义别名"""

"""定义模块别名"""
import time as tt
tt.sleep(5)

"""定义方法别名"""
from time import sleep as sl
sl(6)