'''空元组的定义方式'''

a = ()
b = tuple()

'''定义单个元素的元组'''

c = ('hello', )     # 必须加逗号

d = ('hello', 998, True, None)

# while 循环遍历

index = 0
while index < len(d):
    print(d[index])
    index +=1

# for 循环遍历

for x in d:
    print(x)


