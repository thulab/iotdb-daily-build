# coding=utf-8
from src import connect


def check_commit():
    pass


if __name__ == '__main__':

    dbpath = '/Users/zhangzhengming/Src/Python/iotdb-daily-build-dependence/db/db.db'
    try:
        a, b = connect.select_db('select id,time from last_commit limit 1', dbpath)
    except:
        a, b = 0, 1
    print(a, b)
    if a:
        print(123)
        print(type(a))
        print(len(str(a)))
    else:
        print(456)
    # insert_db('insert into last_commit (id,time) values (\'%s\', \'%s\')' % ('abcdef', '2008-12-26'), dbpath)
