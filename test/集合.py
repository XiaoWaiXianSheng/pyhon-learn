'''定义空集合'''

my_set = set()

my_set1 = {"a", "b", "c", "d"}

'''随机取值'''
print(my_set1.pop())


set1 = {1, 2, 3}
set2 = {1, 4, 5}

'''取两个集合的差集'''
set3 = set1.difference(set2)

print(set3)

'''消除两个集合的差集'''
set1.difference_update(set2)
print(set1)

'''合并两个集合'''
set4 = set1.union(set2)
print(set4)

set1.update(set2)
print(set1)

'''集合的遍历 
    不可以使用while循环
    只能使用for循环'''

for x in set1:
    print(x)