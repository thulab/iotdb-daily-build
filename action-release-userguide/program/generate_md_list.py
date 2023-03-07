# coding=utf-8
import json
import os


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


def add_quote_for_keyword(string):   # 给这些关键字增加引号，替换单引号为双引号
    json_keys = ['text', 'collapsible', 'prefix', 'children', 'link']
    for key in json_keys:
        string = string.replace(key + ':', f'"{key}":')
    return string.replace('\'', '"')


def replace_more_semicolon(string):
    string = string.replace('},],},', '}]},')  # 每个章节末尾
    string = string.replace('[],},', '[]},')  # key = children, 且为空的时候
    string = string.replace('},],};', '}]}')  # 完成前两次替换之后的json尾部
    string = string.replace('}]},],}', '}]}]}')

    return string


def parse_config_file(config_str):
    dict_start = 'zhSidebar ='  # 这一行开始是 dict了
    dict_list = ''
    dict_second = config_str[config_str.index(dict_start)+len(dict_start):]  # 就是从dict_start往后截取到文件尾
    for i in dict_second.split('\n'):  # 按\n拆分，\n就没了，等同于删除全部换行符
        if not i:
            continue
        i = i.strip()  # 删除首尾空格
        if i[:2] == '//':  # 删除注释行
            continue
        if i[:3] == '...':  # 删除第一个配置文件的引用行
            continue
        dict_list += i
    return dict_list


def replace_more_character(string):
    character_one = 'sidebar'  # 这个是siderbar文件夹下的zh.ts 多一个变量叫做sidebar，并且多一层括号，所以要替换掉
    if character_one in string:
        if string.index(character_one) == 0:
            string = string[0 + len(character_one):]
            string = string.strip()
            if string[0] == '(' and string[-2:] == ');':
                string = string[1:-2]
            return string
    return string


def format_json(config):
    config = parse_config_file(config)  # 截取json部分，删除首尾空格，删除注释行
    config = add_quote_for_keyword(config)  # 给关键字加双引号，替换单引号为双引号
    config = replace_more_semicolon(config)  # 删除多余的分号
    config = replace_more_character(config)  # 删除更多的非json部分的字符串
    return config


def get_json_config_list(iotdb_path):
    config_list = []
    for config_file in get_site_zh_ts_list(iotdb_path):
        with open(config_file, 'r') as config:
            json_config = format_json(config.read())
        try:
            config_list.append(json.loads(json_config))
            print('info: 文件 %s 已加载' % config_file)
        except Exception as abc:
            print('error: 文件 %s 有问题: %s\n' % (config_file, abc))
            print(json_config)
    return config_list


if __name__ == '__main__':
    iotdb_home = '/Users/zhangzhengming/Src/Java/iotdb'
    get_json_config_list(iotdb_home)
