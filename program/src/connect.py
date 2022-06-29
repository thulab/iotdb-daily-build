import sqlite3


def insert_db(sql, db_path):
    conn = sqlite3.connect(db_path)  # 打开或创建数据库文件
    c = conn.cursor()  # 获取游标
    c.execute(sql)
    conn.commit()  # 提交数据库操作
    conn.close()  # 关闭数据库连接


def select_db(sql, db_path):
    conn = sqlite3.connect(db_path)  # 打开或创建数据库文件
    c = conn.cursor()  # 获取游标
    row = c.execute(sql)
    res = row.fetchone()
    conn.commit()  # 提交数据库操作
    conn.close()  # 关闭数据库连接
    return res
