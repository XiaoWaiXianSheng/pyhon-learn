
my_str = "itheima and itcast"

'''通过下标索引取值'''

value = my_str[2]
value1 = my_str[-1]
print(value, value1)

'''字符串无法修改'''

print(my_str.index("and"))

'''replace方法，将字符串进行替换'''
new_str = my_str.replace("it", "程序")
print(new_str)
print(my_str)

'''split方法,分割字符串'''
my_list = my_str.split()
print(my_list)

'''strip方法，字符串的规整操作（去除字符串的前后空格以及换行符）'''
my_str1 = " then itheima and itcast   "
my_str2 = my_str1.strip()
print(my_str1)
print(my_str2)

'''strip方法，字符串的规整操作（去除前后指定字符串）'''
my_str3 = "12then itheima and itcast12"
print(my_str3.strip("12ts"))
