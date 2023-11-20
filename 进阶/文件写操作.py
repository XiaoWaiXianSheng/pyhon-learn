'''打开不存在的文件'''

f = open("D:/dev/test1.txt", "w", encoding="UTF-8")
f.write("Hello World")
f.flush()

'''close方法内置了flush的功能'''
f.close()


'''打开存在的文件'''
f = open("D:/dev/test1.txt", "w", encoding="UTF-8")
f.write("你好世界")
'''write会将之前的内容清空'''

f.close()