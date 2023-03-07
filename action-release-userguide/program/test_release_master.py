# coding=utf-8
import parse_json_generate_file_list
import format_md_img
import sys


def format_md_path(string):
    return string.replace(' ', '\ ')


def get_master_md_list(iotdb_path):
    md_file_dict = dict(parse_json_generate_file_list.generate_different_version_md_dict(iotdb_path))
    for key in md_file_dict.keys():
        if not 'master' in key:
            continue
        else:
            break
    print(key)
    print(md_file_dict.get(key))
    return key, md_file_dict.get(key)


def main(iotdb_path):
    title, master_md_list = get_master_md_list(iotdb_path)
    format_md_img.(master_md_list)



if __name__ == '__main__':
    iotdb_home = 'D:\\Src\\Java\\iotdb'
    if len(sys.argv) == 1:
        main(iotdb_home)
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('error: 只可以提供一个参数或者不提供参数')
        exit()
