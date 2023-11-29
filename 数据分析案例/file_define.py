"""
文件相关的类定义
"""
import json

from 数据分析案例.data_define import Record


class FileReader:

    def read_data(self) -> list[Record]:
        """读取文件数据，将督导的每一条数据都转换为Record对象，都封装到list内返回"""
        pass


class TextFileReader(FileReader):

    def __init__(self, path):
        self.path = path        # 定义成员变量，记录文件路径

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()     # 消除换行符
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list


class JsonFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            # print(type(line))
            # print(f"Line{line}")
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list


if __name__ == '__main__':
    text_file_reader = TextFileReader("D:/dev/2011年1月销售数据.txt")
    json_file_reader = JsonFileReader("D:/dev/2011年2月销售数据JSON.txt")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()

    # for l in list1:
    #     print(l)

    for l in  list2:
        print(l)