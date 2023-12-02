from pymysql import Connection

from 数据分析案例.data_define import Record
from 数据分析案例.file_define import TextFileReader, JsonFileReader


text_file_reader = TextFileReader("D:/dev/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("D:/dev/2011年2月销售数据JSON.txt")


jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

'''将两个月份的数据合并成一个list存储'''

all_data: list[Record] = jan_data + feb_data

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True         # 设置自动提交
)

cursor = conn.cursor()
conn.select_db("py_sql")

for record in all_data:
    sql = (f"insert into orders(order_date, order_id, money, province) "
           f"values('{record.date}', '{record.order_id}', {record.money}, '{record.province}')")
    cursor.execute(sql)

conn.close()
