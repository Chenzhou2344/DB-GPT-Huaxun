import pymysql
 
# 建立数据库连接
conn = pymysql.Connect(
    host='127.0.0.1',  # 数据库主机名
    port=3307,  # 数据库端口号
    user='root',  # 数据库用户名
    password='123456',  # 数据库密码
    database='case_1_student_manager'  # 数据库名
)
 
# 执行SQL查询等操作
cursor = conn.cursor()
cursor.execute('SELECT * FROM students')
result = cursor.fetchall()
print(result)
# 关闭游标和连接
cursor.close()
conn.close()