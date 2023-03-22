# coding=utf-8
import sys
import os
import subprocess
import format_md_img
import os.path
import parse_json_generate_file_list
import common


def get_master_md_list(iotdb_home):
    key = ''
    md_file_dict = dict(parse_json_generate_file_list.generate_different_version_md_dict(iotdb_home))
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


def get_md_list_to_str(iotdb_home, md_tmp_path):
    title, master_md_list = get_master_md_list(iotdb_home)  # 拿到master分支的标题，md 文件按顺序排列的 list
    new_md_list = [os.path.abspath('Templates/page.md')]  # 目录页
    for md in master_md_list:
        new_md_list.append(os.path.join(md_tmp_path, md))
    return ' '.join(new_md_list)


def main(iotdb_home):
    md_tmp_path = format_md_img.main(generate_user_guide_abs_path(iotdb_home))  # 拷贝 userguide 到当前目录的tmp下，下载图片，标准全部图片在md下的使用方式，返回 'tmp/md'
    md_list_str = get_md_list_to_str(iotdb_home, md_tmp_path)  # 将 iotdb/site 下拼出来的顺序md的list，和 tmp/md 拼一起
    template_file = os.path.abspath('Templates/template_iotdb.docx')  # 模版文件的绝对值路径
    output_file = 'result.docx'  # 输出文件

    print(f'pandoc -f markdown -t docx -o {output_file} --reference-doc {template_file} --log=log.txt {md_list_str}')
    exec_order = subprocess.getoutput(f'pandoc -f markdown -t docx -o {output_file} --reference-doc {template_file} --log=log.txt {md_list_str}')
    print(exec_order)


if __name__ == '__main__':
    iotdb_path = '/Users/zhangzhengming/Src/Java/iotdb'
    if len(sys.argv) == 1:
        main(iotdb_path)
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('error: 只可以提供一个参数或者不提供参数')
        exit()
