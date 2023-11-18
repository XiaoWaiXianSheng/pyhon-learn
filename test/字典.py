'''定义空字典'''

my_dict = {}
my_dict1 = dict()
print(type(my_dict))

my_dict2 = {"王力宏": 99, "周杰伦": 88, "林俊杰": 77}

'''从字典中取值'''

print(my_dict2["王力宏"])

'''定义嵌套字典'''

stu_score_dict = {
    "王力宏": {"语文": 77, "数学": 66, "英语": 33},
    "周杰伦": {"语文": 88, "数学": 86, "英语": 55},
    "林俊杰": {"语文": 99, "数学": 96, "英语": 66}
}

print(stu_score_dict["王力宏"])

'''删除元素 pop'''
print(stu_score_dict.pop("周杰伦"))
print(stu_score_dict)

'''清空字典 clear'''
print(my_dict2.keys())
my_dict2.clear()
print(my_dict2)

'''获取字典中所有 key'''
keys = stu_score_dict.keys()
print(keys)

'''遍历字典'''
for key in stu_score_dict:
    print(stu_score_dict[key])

for key in keys:
    print(stu_score_dict[key])

lenth = len(stu_score_dict)
print(lenth)