# coding=utf-8
import sys

from format_md_img import format_md_img
from format_file_list import format_file_list
from scan_directory import scan_directory
from execute import execute

import os


def mkdir_tmp_folder(paht):  # 创建临时目录
    tmp_doc = os.path.join(os.getcwd(), 'iotdb')
    os.system('mkdir -p %s' % tmp_doc)
    os.system('cp -r %s/* %s/' % (paht, tmp_doc))
    os.system('mkdir -p img')
    return tmp_doc


def rm_tmp_folder(paht):  # 删除临时目录
    os.system('rm -rf %s' % paht)
    os.system('rm -rf %s' % os.path.join(os.getcwd(), 'img'))
    os.system('rm -rf %s' % os.path.join(os.getcwd(), 'include_format.txt'))


def check_inputpath(paht):  # 判断输入的路径是否正确
    while True:
        if paht[-1] == '/' or paht[-1] == ' ':
            paht = paht[:-1]
        else:
            break
    if os.path.isdir(paht):
        return paht
    else:
        print('\'%s\' not a dir,please restart' % paht)
        exit()


if __name__ == '__main__':
    # 1、输入文档绝对路径，拷贝
    file_path = mkdir_tmp_folder(check_inputpath(sys.argv[1]))
    # 2、将文件路径下文件列出来，写入include.txt里
    scan_directory(file_path)
    # 3、格式化列表，相对路径变为绝对路径，赋值字符串给format_list
    format_list = format_file_list('include.txt')
    # 4、修改文件路径下所有md文件的图片引用格式
    format_md_img(file_path)
    # 5、启动pandoc转格式
    produce_file = execute(format_list)
    # # 6、删除临时文件
    # rm_tmp_folder(file_path)
