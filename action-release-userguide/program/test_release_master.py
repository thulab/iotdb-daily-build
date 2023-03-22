# coding=utf-8
import os.path
import subprocess
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
            print('info: 找到了master配置参数.')
            break
    if not key:
        print('error: 找不到 master 分支 ')
        exit()
    return key, common.replace_space_add_backslash(md_file_dict.get(key))


def generate_user_guide_abs_path(string):
    return os.path.join(string, 'docs/zh/UserGuide')


def main(iotdb_path):
    title, master_md_list = get_master_md_list(iotdb_path)  # 拿到master分支的标题，markdown文件列表
    user_guide_abs_path = generate_user_guide_abs_path(iotdb_path)  # 拼接出来userguide的绝对值路径
    format_md_img.main(user_guide_abs_path)  # 执行下一个文件的操作
    subprocess.getoutput('pandoc -f markdown -t docx -o result.docx --reference-doc Templates/template_iotdb.docx --log=log.txt %s' % ','.join(master_md_list))


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
