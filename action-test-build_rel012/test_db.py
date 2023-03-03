# coding=utf-8
import sys

from src import connect


if __name__ == '__main__':
    # db_path = '/Users/zhangzhengming/Src/Python/iotdb-daily-build-dependence/db/db.db'
    db_path = sys.argv[1]
    # sql = 'select * from commit_last'
    sql = sys.argv[2]
    print(connect.select_db(sql, db_path))
