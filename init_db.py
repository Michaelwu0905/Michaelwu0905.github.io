import sqlite3

conn=sqlite3.connect('database.db')

with open('db.sql') as f:
    conn.executescript(f.read())

# 创建句柄，执行后面的语句
cur=conn.cursor()

# 插入两条文章
cur.execute("INSERT INTO posts(title,content) VALUES(?,?)",
    ('学习Flask1','跟Leahcim学习第一部分')
)
cur.execute("INSERT INTO posts(title,content) VALUES(?,?)",
    ('学习Flask2','跟Leahcim学习第二部分')
)

conn.commit()
conn.close()