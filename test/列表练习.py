my_list = [21, 25, 21, 23, 22, 20]
my_list.append(31)
print(my_list)
my_list.append([29, 33, 30])
print(my_list)

first = my_list.pop(0)
print(first)

last = my_list.pop(-1)
print(last)

num = my_list.index(31)
print(num)

def list_while_func():
    my_list1 = ["a", "b", "c"]
    index = 0
    while index < len(my_list1):
        element = my_list1[index]
        print(element)
        index +=1

list_while_func()

def list_for_func():
    my_list2 = ["d", "e", "f"]
    for x in my_list2:
        print(x)

list_for_func()