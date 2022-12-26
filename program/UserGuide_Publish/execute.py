# coding=utf-8
import os
import time
import sys


def execute(list_format):
    cur_time = str(time.strftime("%H%M%S"))
    if os.path.isfile(list_format):
        with open(list_format, 'r', encoding='utf-8-sig') as iii:
            for i in iii:
                list_format = i
                break
    os.system('pandoc -f markdown -t docx -o result.docx --reference-doc template.docx --log=log.txt %s' % list_format)
    print('生成文件是result.docx')


if __name__ == '__main__':
    execute(input('输入一个包含md文件的字符串，或者指定一个写好字符串的txt:\n'))
