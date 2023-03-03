# coding=utf-8
import os
import sys

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
    dict_start = 'zhSidebar = '
    return config_str[config_str.index(dict_start)+len(dict_start):-2]


#
def get_target_version_md_list():
    for config_file in get_site_zh_ts_list(iotdb_src):
        with open(config_file, 'r') as config:
            dict_config = parse_config_file(config.read())
        # print(dict_config)
        print(dict(dict_config))
        exit()



if __name__ == '__main__':
    iotdb_src = '/Users/zhangzhengming/Src/Java/iotdb'
    get_target_version_md_list()
