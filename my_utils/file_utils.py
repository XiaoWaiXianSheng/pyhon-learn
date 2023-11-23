def print_file_info(file_name):
    """
    :param file_name: 传入文件路径
    :return:
    """
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        line = f.read()
        print(line)
    except  FileNotFoundError:
        print("文件不存在")
    finally:
        if f:
            f.close()


def append_to_file(file_name, data):
    f = None
    f = open(file_name, "a", encoding="UTF-8")
    f.write("\n" + str(data))


if __name__ == '__main__':
    print_file_info("D:/dev/test.txt")
    append_to_file("D:/dev/test.txt", 11223344)
