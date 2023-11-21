
try:
    f = open("D:/dev/abc.txt", "r", encoding="UTF-8")
except:
    print("出现异常，因为文件不存在，将模式改为w")
    f = open("D:/dev/abc.txt", "w", encoding="UTF-8")


'''捕获指定的异常'''
try:
    print(name)
except NameError as e:                  # e 是一个临时变量
    print("出现了变量未定义的异常")
    print(e)

'''捕获多个异常'''
try:
    print(name)
    1/0
except (NameError, ZeroDivisionError) as e:
    print("出现了变量未定义或除以0的异常")



'''捕获所有异常'''
try:
    1/0
except Exception as e:
    print("出现异常")
else:
    print("没有异常")
finally:                # finally  表示无论如何都要执行的代码
    print("必须输出")
