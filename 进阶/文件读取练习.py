f = open("D:/dev/word.txt", "r", encoding="UTF-8")

'''第一种方法'''
content = f.read()
count = content.count("itheima")
print(f"一共有{count}个 itheima")

f.close()
"""第二种方法"""
z = open("D:/dev/word.txt", "r", encoding="UTF-8")

count = 0
for line in z:
    words = line.split()
    # word = line.strip()
    print(words)
    for word in words:
        if word == "itheima":
            count += 1

print(count)