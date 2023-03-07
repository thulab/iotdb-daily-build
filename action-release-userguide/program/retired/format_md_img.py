# coding=UTF-8
import os
import re
import subprocess


def update_file_by_line(file, line, new_line):
    """
    替代shell的sed
    """
    file = file.replace('\\', '')  # 这个地方不知道咋回事，转译空格就会报错
    with open(file, 'r') as f:
        all_neirong = f.readlines()
    all_neirong[line-1] = new_line + '\n'  # 不加/n的话，下一行就会上来，就会少一行
    with open(file, 'w') as f:
        f.writelines(all_neirong)


def format_md_img(paht):
    """
    file_list_2: 包含全部格式不对链接的md文件
    file_name: file_list_2中的一条
    line_2: 包含指定文件下全部有链接的行
    alone_line: line_2中的一条
    """
    file_re = '<img.*>$'
    # file_re2 = '\!\[.*[.png|.jpg|.jpeg]).*'

    url_re = r'(http[s])://(.*)[.png|.jpg|.jpeg]'
    count_url = 0

    # 匹配文件名列表=====>>>file_list_2
    file_list_2 = []
    # grep -rl '<img.*>$' --include=*.md /Users/zhangzhengming/Src/Python/test_iotdb_pandoc/pandoc/docs
    file_list = subprocess.getoutput('grep -rl \'%s\' --include=*.md %s' % (file_re, paht))
    for k in file_list.split('\n'):
        file_list_2.append(k.replace(' ', '\ '))
    # print('有以下文件有这个链接：\n' + str(file_list_2))

    # 匹配多行=====>>>line_2
    for file_name in file_list_2:
        line_2 = []
        # print('当前文件名是%s:\n' % file_name)
        line = subprocess.getoutput('grep  -n \'%s\' %s' % (file_re, file_name))
        for m in line.split('\n'):
            # print(m)
            line_2.append(m)
        # print('%s 文件里面有以下几个匹配项：\n%s' % (i, line_2))
        # for i in line_2:
        #     print(i)
        # 匹配单行=====>>>alone_line
        for alone_line in line_2:
            # 匹配行号
            line_number = alone_line.split(':')[0]
            # print('行号是%s' % line_number)

            # 匹配链接=====>>>url
            # print('alone_line is [%s]' % alone_line)
            line_url = re.search(url_re, str(alone_line))
            url = line_url.group()
            for i in "jpg", "png", "jpeg":
                if i in url:
                    url = url[0:url.find(i) + len(i)]

            # print('url是%s' % url)

            # 替换内容
            new_line = '![](%s){ width=50%% }' % url
            print('替换%s的%s行 为%s' % (file_name, line_number, new_line))
            update_file_by_line(file_name, int(line_number), new_line)
        # 输出
        # print('在%s中修改了%s个链接' % (file_name, len(line_2)))
        count_url += len(line_2)
    print('一共修改了%s个格式\n' % count_url)

    # 替换图片路径为本地路径
    count_url = 0
    new_file_re = '!\[.*[\)|\}]'  # 匹配![开头，)或者}结尾
    file_list = subprocess.getoutput('grep -rl \'%s\' --include=*.md %s' % (new_file_re, paht))
    file_list_2 = []
    for k in file_list.split('\n'):
        file_list_2.append(k)
    for file_name in file_list_2:
        file_name = file_name.replace(' ', '\ ')
        line = subprocess.getoutput('grep  -n \'%s\' %s' % (new_file_re, file_name))
        line_2 = []
        for m in line.split('\n'):
            line_2.append(m)
        for alone_line in line_2:
            line_number = alone_line.split(':')[0]
            line_url_2 = re.search(url_re, str(alone_line))
            # print('line_url_2=%s ' % line_url_2.group())
            url = line_url_2.group()
            relative_file_name = file_name[file_name.index(paht) + len(paht):].replace(' ', '_').replace('/', '-')[
                                 1:].replace('\\', '').replace('.md', '') + '--' + line_number + os.path.splitext(url)[
                                     -1]
            img_download_path = os.path.join(os.getcwd(), 'img', relative_file_name)
            # a[a.find('zzm'):a.find('zzm') + len("zzm")]
            for i in "jpg", "png", "jpeg":
                if i in img_download_path:
                    img_download_path = img_download_path[0:img_download_path.find(i) + len(i)]
            # 下载图片
            try:
                # os.system('wget -O %s %s' % (img_download_path, url))
                print(('wget -O %s %s' % (img_download_path, url)))
                subprocess.getoutput('wget -O %s %s' % (img_download_path, url))
                # print('wget -O %s %s' % (img_download_path, url))
                print('download %s ok' % relative_file_name)
            except Exception as e:
                print('download failed,Exception:%s' % e)
                exit()

            new_line = '![](%s){ width=50%% }' % img_download_path
            print('替换%s的%s行 为%s\n' % (file_name, line_number, new_line))
            update_file_by_line(file_name, int(line_number), new_line)

        # 输出
        # print('在%s中修改了%s个链接' % (file_name, len(line_2)))
        count_url += len(line_2)
    print('一共下载并替换了%s个url为本地图片\n' % count_url)


if __name__ == '__main__':
    format_md_img(input('输入存放md文件的路径：\n'))

# 根据相对路径生成图片名称
# relative_file_name = file_name[file_path.index(paht) + len(paht):]  # 取file_name这个路径里面，在paht之后的内容，=相对路径
# relative_file_name = relative_file_name.replace(' ', '_')  # 空格换成_
# relative_file_name = relative_file_name.replace('/', '-')  # /换成-
# relative_file_name = relative_file_name[1:]  # 去掉第一个字符-
# relative_file_name = relative_file_name.replace('.md', '')  # 去掉扩展名
# relative_file_name = relative_file_name + line_number  # 拼接行号
# relative_file_name = relative_file_name + os.path.splitext(url)[-1]  # 加上扩展名
# relative_file_name = relative_file_name.replace('\\', '')  # 去掉
