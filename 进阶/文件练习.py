f = open("D:/dev/test1.txt", "r", encoding="UTF-8")
g = open("D:/dev/test2.txt.bak", "w", encoding="UTF-8")

for x in f:
    z = x.strip()
    y = z.split("，")
    if y[-1] == "测试":
        continue
    else:
        g.write(x)
f.close()
g.close()
