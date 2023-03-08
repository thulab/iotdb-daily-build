# coding=utf-8
import parse_json_generate_file_list
import format_md_img
import sys


def format_md_path(md_list):
    format_md_list = []
    for md in md_list:
        format_md_list.append(md.replace(' ', '\ '))
    return format_md_list


def get_master_md_list(iotdb_path):
    key = ''
    md_file_dict = dict(parse_json_generate_file_list.generate_different_version_md_dict(iotdb_path))
    for key in md_file_dict.keys():
        if not 'master' in key:
            continue
        else:
            break
    if not key:
        print('error: zhaobudao ')
    print('info: 找到了master配置参数.')
    return key, format_md_path(md_file_dict.get(key))


def main(iotdb_path):
    title, master_md_list = get_master_md_list(iotdb_path)
    print(title)
    print(master_md_list)
    format_md_img.format_md_img(master_md_list)


if __name__ == '__main__':
    iotdb_home = 'D:\\Src\\Java\\iotdb'
    if len(sys.argv) == 1:
        main(iotdb_home)
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('error: 只可以提供一个参数或者不提供参数')
        exit()
