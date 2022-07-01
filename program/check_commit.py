# coding=utf-8
import sys
from src import connect


# ----------拿到以下三个值的方式
# commit_id: git log  -n 1 | head -n 1  | cut -d ' ' -f 2
# commit_time: git log -n1 --pretty='format:%cd' --date=iso
# branch: git branch |grep ^*|cut -d ' ' -f 2
# ----------样例
# python3 check_commit.py '/Users/zhangzhengming/Src/Python/iotdb-daily-build-dependence/db/db.db' 'rel/0.12' '34b6a79913d7754f3f8397f9c26bdbef3a6393b5' '2022-06-30 10:57:40 +0800'


def check_commit(cur_branch, db_path):
    sql = 'select branch,commit_id,commit_time from commit_last where branch=\'%s\'' % cur_branch
    return connect.select_db(sql, db_path)


def update_commit(cur_branch, cur_commit_id, cur_commit_time, db_path):
    sql = 'update commit_last set commit_id=\'%s\',commit_time=\'%s\' where branch=\'%s\'' % (cur_commit_id, cur_commit_time, cur_branch)
    connect.insert_db(sql, db_path)


if __name__ == '__main__':
    if len(sys.argv[1:]) != 4:
        print('必须设置4个参数')
        exit()
    dbpath, branch, commit_id, commit_time = sys.argv[1:]
    # dbpath = '/Users/zhangzhengming/Src/Python/iotdb-daily-build-dependence/db/db.db'

    db_branch, db_commit_id, db_commit_time = check_commit(branch, dbpath)

    if branch == db_branch and commit_id == db_commit_id:
        print('stop')
        exit()
    elif commit_id != db_commit_id:
        update_commit(branch, commit_id, commit_time, dbpath)
        print('update')
        exit()
