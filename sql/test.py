from pymysql import Connection

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True         # 设置自动提交
)

cursor = conn.cursor()
conn.select_db("py_sql")

cursor.execute("select * from orders")

result = cursor.fetchall()

orders_dict: dict = {}
for r in result:

    orders_dict['date'] = str(r[0])
    orders_dict['order_id'] = r[1]
    orders_dict['money'] = r[2]
    orders_dict['province'] = r[3]
    print(orders_dict)
    # print(r)

print(type(result[1986][0]))
conn.close()
