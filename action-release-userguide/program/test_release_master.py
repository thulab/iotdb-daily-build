# coding=utf-8
import os.path

import parse_json_generate_file_list
import format_md_img
import sys
import common


def get_master_md_list(iotdb_path):
    key = ''
    md_file_dict = dict(parse_json_generate_file_list.generate_different_version_md_dict(iotdb_path))
    for key in md_file_dict.keys():
        if 'master' not in key:
            continue
        else:
            break
    if not key:
        print('error: zhaobudao ')
    print('info: 找到了master配置参数.')
    return key, common.replace_space_add_backslash(md_file_dict.get(key))


def generate_user_guide_abs_path(string):
    return os.path.join(string, 'docs/zh/UserGuide')


def main(iotdb_path):
    title, master_md_list = get_master_md_list(iotdb_path)  # 拿到master分支的标题，markdown文件列表
    user_guide_abs_path = generate_user_guide_abs_path(iotdb_home)  # 拼接出来userguide的绝对值路径
    format_md_img.main(user_guide_abs_path)  # 执行下一个文件的操作


if __name__ == '__main__':
    # iotdb_home = 'D:\\Src\\Java\\iotdb'
    iotdb_home = '/Users/zhangzhengming/Src/Java/iotdb'
    if len(sys.argv) == 1:
        main(iotdb_home)
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('error: 只可以提供一个参数或者不提供参数')
        exit()
