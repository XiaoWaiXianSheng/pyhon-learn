"""open()函数"""

f = open("D:/dev/test.txt", "r", encoding="UTF-8")
print(type(f))

print(f.read())

line = f.readlines()
print(line)

x = open("D:/dev/test.txt", "r", encoding="UTF-8")
line = x.readlines()
print(line)

z = open("D:/dev/test.txt", "r", encoding="UTF-8")
# print(z.readline())
while z.readline():
    result = z.readline()
    print(result)

"""用for循环读取文件行"""
for line in open("D:/dev/test.txt", "r", encoding="UTF-8"):
    print(line)

"""关闭文件对象"""
f.close()

"""with open语法
    通过在with open的语句块中对文件进行操作
    可以在操作结束后自动close文件对象，避免遗忘掉close方法"""

with open("D:/dev/test.txt", "r", encoding="UTF-8") as f:
    print(f.readlines())