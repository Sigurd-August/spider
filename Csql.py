import pymysql.cursors

connect = pymysql.connect(
    host='172.31.34.145',
    port=3306,
    user='15301148',
    passwd='15301148',
    db='db15301148',
    charset='utf8'
)

cursor = connect.cursor()

sql = "create table spider(Symbol varchar(255) not null)"
cursor.execute(sql)
for row in cursor.fetchall():
    print(row)

cursor.close()
connect.close()