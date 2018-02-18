# -*- coding: utf-8 -*-
# 라이브러리 읽어 들이기
import MySQLdb
# MySQL 연결하기
conn = MySQLdb.connect(
    user='root',
    passwd='test-password',
    host='localhost',
    db='test')
# 커서 추출하기
cur = conn.cursor()
# 테이블 생성하기
cur.execute('DROP TABLE items')
cur.execute('''
    CREATE TABLE items (
        item_id INTEGER PRIMARY KEY AUTO_INCREMENT,
        name TEXT,
        price INTEGER
    )
    ''')
# 데이터 추가하기
data = [('Banana', 300),('Mango', 640), ('Kiwi', 280)]
for i in data:
    cur.execute("INSERT INTO items(name,price) VALUES(%s,%s)", i)
# 데이터 추출하기
cur.execute("SELECT * FROM items")
for row in cur.fetchall():
    print(row)
    
    