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


if __name__ == '__main__':
    dbpath = '/Users/zhangzhengming/Src/Python/iotdb-daily-build-dependence/db/commit.db'
    try:
        a, b = select_db('select id,time from last_commit limit 1', dbpath)
    except Exception as abc:
        a, b = 0, 1
    print(a,b)
    if a:
        print(123)
        print(type(a))
        print(len(str(a)))
    else:
        print(456)
    # insert_db('insert into last_commit (id,time) values (\'%s\', \'%s\')' % ('abcdef', '2008-12-26'), dbpath)


