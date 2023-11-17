# 列表的定义

a = ["a", 5, True, ["b", 9, False]]
b = list()
d = ['x', 66, None]

print(a[3][1])
print(a[-1][-1])

'''index 查找列表中元素的下标索引'''
c = a[3].index("b")

print(c)

a[0] = "aa"
print(a)

'''insert 在列表指定位置插入元素'''
a.insert(1, '插入值')
print(a)

'''append 在列表尾部追加元素'''
a.append("追加值")
print(a)

a.append(d)
print(a)

'''extend 在列表尾部追加一批元素'''
a.extend(d)
print(a)

'''删除指定下标的元素'''
del a[4]
print(a)

f = a.pop(5)
print(a)
print(f)
print(f"{f} 666")

'''删除某元素在列表中的第一个匹配项'''
a.remove(None)
print(a)

'''清空列表'''
# a.clear()
# print(a)

'''统计某元素的数量'''
x = a.count(6)
print(x)

'''列表中所有元素的数量'''
lenth = len(a)
print(lenth)
