def func01():
    print("这是func01的开始")
    num = 1/0
    print("这是func01的结束")


def func02():
    print("这是func02的开始")
    func01()
    print("这是func02的结束")


def main():
    try:
        func02()
    except Exception as e:
        print(e)

main()


