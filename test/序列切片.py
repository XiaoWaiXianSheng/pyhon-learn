str4 = "0123456"
print(str4[:0:-2])


my_str = "万过薪月，员序程马黑来，nohtyP学"

print(my_str[9:4:-1])

print(my_str[::-1][9:14])

print(my_str[5:10][::-1])

print(my_str.split("，"))

my_list = my_str.split("，")

print(my_list[1].replace("来", "")[::-1])