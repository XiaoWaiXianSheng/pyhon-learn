from pymysql import Connection

conn = Connection(
    host="localhost",   # 主机名
    port=3306,          # 端口
    user="root",        # 账户
    password="123456"   # 密码
)

print(conn.get_server_info())

'''执行非查询性质的SQL语句'''
# 获取游标对象

cursor = conn.cursor()          # 获取游标对象
conn.select_db("world")          # 选择数据库

'''执行SQL'''
# cursor.execute("create table test_pymysql(id int);")

cursor.execute("select * from student")

result: tuple = cursor.fetchall()

for r in result:
    print(r)

conn.close()