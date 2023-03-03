# coding=utf-8
import os


def scan_directory(paht):
    g = os.walk(paht)
    abs_list = []

    for path, dir_list, file_list in g:
        for file_name in file_list:
            # print(os.path.abspath(os.path.join(path, file_name)))
            # abs_path = os.path.abspath(os.path.join(path, file_name))
            abs_path = os.path.join(path, file_name)
            if os.path.splitext(abs_path)[1] == '.md':
                abs_list.append(abs_path)
    print('一共找到了%s个md文件' % len(abs_list))

    # if input('是否写入include.txt？yes or 任意键取消：\n') == 'yes':
    if True:
        with open('include.txt', 'w', encoding='utf-8-sig') as hhh:
            for i in abs_list:
                hhh.write(i + '\n')
                print(i)
        print('\n已经将列表写入了include.txt，检查无误后执行下一步。\n')


if __name__ == '__main__':
    scan_directory(input('输入存放md文件的路径：\n'))
