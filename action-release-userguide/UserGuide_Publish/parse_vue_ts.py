# coding=utf-8
import json


# 去掉首尾空格,全部换行符
def remove_space_from_the_first_and_the_end(string):
    return string.strip()


# 去除首尾大括号
def remove_brackets_from_the_first_and_the_end(string):
    return string.rstrip('}').lstrip('{')


def replace_line_break(string):
    return string.replace('\n', '')


# other要去掉首尾的方括号
def remote_other_brackets_from_the_first_and_the_end(string):
    return remove_space_from_the_first_and_the_end(string).rstrip('],').lstrip('[')


# 拿到标题和其他
def get_title_and_other(string):
    string = str(string)
    part_one = string.split(':')[0]  # 取第一部分
    part_two = string[string.index(part_one)+len(part_one)+1:]  # 去掉第一部分才是第二部分，否则第二部分被去掉:了
    return part_one, part_two  # other要去掉首尾的方括号


def format_to_json(string):
    json_keys = ['text', 'collapsible', 'prefix', 'children', 'link']
    for key in json_keys:
        string = string.replace(key, f'"{key}"')
    return string


def main():
    pass


if __name__ == '__main__':
    with open('../abc.txt', 'r') as all_contents:
        all_string = all_contents.read()
        all_string = remove_space_from_the_first_and_the_end(all_string)  # 去掉首尾空格

        abc = format_to_json(all_string)
        print(abc)
        print(json.loads(abc))
        #
        # all_string = remove_brackets_from_the_first_and_the_end(all_string)  # 去掉首尾大括号
        # all_string = replace_line_break(all_string)  # 去掉全部换行符
        # title, contents = get_title_and_other(all_string)
        # json_contents = format_to_json(contents)
        # # print(json_contents)
        # abc = json.loads(json_contents)
        # print(abc)


        #
