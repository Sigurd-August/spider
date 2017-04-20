import pymysql.cursors
import urllib.request
import re

file_01 = open('1.html')
file_01_text = file_01.read()
#print(file_01_text)
pattern_symbol = re.compile(r'<th align="left" valign="top" class="colnorm" scope="row">(.*)</th>')
pattern_sname = re.compile(r'<td><a href="profile[?]symbol=.*" target="_top"><em>(.*?)</em> <em>(.*?)</em></a></td>')
pattern_cname = re.compile(r'<td>([\w\s]*?)</td>')
match_symbol = pattern_symbol.findall(file_01_text)
match_sname = pattern_sname.findall(file_01_text)
match_cname = pattern_cname.findall(file_01_text)

connect = pymysql.connect(
    host='172.31.34.145',
    port=3306,
    user='15301148',
    passwd='15301148',
    db='db15301148',
    charset='utf8'
)

cursor = connect.cursor()

for i in range(0,996):
    sql = "insert into usdaplant(Symbol,Scientific_Name,Common_Name)values( '%s', '%s', '%s')"
    data = (match_symbol[i],match_sname[i][0] +" "+ match_sname[i][1],match_cname[i])
    cursor.execute(sql % data)
    connect.commit()
    print('成功插入',i, '条数据')
for i in range(997,1046):
    sql = "insert into usdaplant(Symbol,Scientific_Name)values( '%s', '%s')"
    data = (match_symbol[i], match_sname[i][0] + " " + match_sname[i][1])
    cursor.execute(sql % data)
    connect.commit()
    print('成功插入', i, '条数据')
for i in range(1046,1053):
    sql = "insert into usdaplant(Symbol)values( '%s')"
    data = (match_symbol[i])
    cursor.execute(sql % data)
    connect.commit()
    print('成功插入', i, '条数据')
cursor.close()
connect.close()
file_01.close()