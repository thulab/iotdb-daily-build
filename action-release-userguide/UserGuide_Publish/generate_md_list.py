# coding=utf-8
import os
import sys
import time
import json
import typing
#


def get_site_zh_ts_list(iotdb_path):
    site_sidebar = 'site/src/main/.vuepress/sidebar'
    zh_userguide_file = 'zh.ts'
    config_path = os.path.join(iotdb_path, site_sidebar)
    config_file_list = []
    for i in os.listdir(config_path):
        abs_i = os.path.join(config_path, i)
        if os.path.isfile(abs_i):
            if i == zh_userguide_file:
                config_file_list.append(os.path.abspath(abs_i))
        else:
            for j in os.listdir(abs_i):
                abs_j = os.path.join(abs_i, j)
                if os.path.isfile(abs_j):
                    if j == zh_userguide_file:
                        config_file_list.append(os.path.abspath(abs_j))
    return config_file_list


def parse_config_file(config_str):
    dict_start = 'zhSidebar = '  # 这一行开始是 dict了
    dict_list = ''
    dict_second = config_str[config_str.index(dict_start)+len(dict_start):-2]
    for i in dict_second.split('\n'):  # 按\n拆分，\n就没了
        if not i:
            continue
        while True:
            if i[0] == ' ':
                i = i[1:]
            else:
                break
        if i[:2] == '//':
            continue
        dict_list += i
    return dict_list


#
def get_target_version_md_list():
    for config_file in get_site_zh_ts_list(iotdb_src):
        with open(config_file, 'r') as config:
            dict_config = parse_config_file(config.read())
        print(dict_config)
        exit()


if __name__ == '__main__':
    iotdb_src = '/Users/zhangzhengming/Src/Java/iotdb'
    get_target_version_md_list()
