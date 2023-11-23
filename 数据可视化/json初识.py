'''导入json模块'''
import json

data = [{"name": "老王", "age": "16"}, {"name": "张三", "age": "20"}]

'''将python数据转换为json数据'''
'''将列表转换'''
json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)
'''将字典转换'''
d = {"name": "老王", "age": "16"}
json_str = json.dumps(d, ensure_ascii=False)
print(type(json_str))
print(json_str)

'''将json数据转化为python数据'''
'''将json字符串转换'''

s = '[{"name": "老王", "age": "16"}, {"name": "张三", "age": "20"}]'
l = json.loads(s)
print(type(l))
print(l)

s = '{"name": "老王", "age": "16"}'
d = json.loads(s)
print(type(d))
print(d)
