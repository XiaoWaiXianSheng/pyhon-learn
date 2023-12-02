from pymysql import Connection

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True         # 设置自动提交
)


cursor = conn.cursor()
'''选择数据库'''
conn.select_db("world")
'''执行SQL'''
cursor.execute("insert into students values(10001, '周杰伦', 31, '男')")
cursor.execute("insert into students values(10002, '林俊杰', 31, '男')")
'''通过commit确认'''
# conn.commit()
'''关闭链接'''
conn.close()
