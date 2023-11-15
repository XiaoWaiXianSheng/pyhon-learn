money = 5000000
name = None


def check_money():
    global money
    print(f"{name}的余额为{money}")

    menu(name)


def draw_money(x):
    global money
    money -= x
    print(f"{name}的余额为{money}")
    menu(name)


def save_money(x):
    global money
    money += x
    print(f"{name}的余额为{money}")
    menu(name)


def menu(x):
    global name
    name = x

    print("查询余额请按1\n取款请按2\n存款请按3\n退出请按4")
    a = input("请输入您要进行的操作")
    if a == "1":
        check_money()
    elif a == "2":
        draw_money(int(input("取款金额")))
    elif a == "3":
        save_money(int(input("存款金额")))
    else:
        return


menu(input("请输入你的姓名"))
