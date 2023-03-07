# coding=utf-8
import os


def format_file_list(list_file):
    g = []
    with open(list_file, 'r', encoding='utf-8-sig') as iii:  # 编码必须一致，否则会出现一个<feff>(bom字符)
        for i in iii:
            # print(i)
            i = i.replace(' ', '\ ')
            i = i.replace('\n', '')
            # i = os.path.abspath(i)
            g.append(i)
    j = ''
    for k in g:
        j = j + k + ' '
    with open('include_format.txt', 'w', encoding='utf-8-sig') as hhh:
        hhh.write(j)
    print('已经将生成字符串存放到include_format.txt\n')
    return j


if __name__ == '__main__':
    format_file_list(input('输入存放列表的txt路径+名称：\n'))
