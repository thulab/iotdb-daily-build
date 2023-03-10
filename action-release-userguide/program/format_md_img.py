# coding=UTF-8
import os
import sys
import re
import subprocess
import shutil
import common


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


def match_include_img_label_file_from_md_list(tmp_md_path, file_re):  # 捕获包含 img 标签的文件从 md_list
    file_list = subprocess.getoutput('grep -rl \'%s\' --include=*.md %s' % (file_re, tmp_md_path)).split('\n')
    format_file_list = common.replace_space_add_backslash(file_list)
    return format_file_list


def match_line_from_md_file(file, file_re):  # 捕获包含 img 标签的文件从 md_file，返回 list
    return subprocess.getoutput('grep -n \'%s\' %s' % (file_re, file)).split('\n')


def match_link_from_line_list(match_line_list, url_re):
    parse_link_from_line_list = []
    for match_line in match_line_list:
        line_number = match_line.split(':')[0]
        line_content = match_line[len(line_number + ':'):]  # <img style="width:100%; max-width:800px; max-height:600px; margin-left:auto; margin-right:auto; display:block;" src="/img/github/69109512-f808bc80-0ab2-11ea-9e4d-b2b2f58fb474.png">
        line_url = re.search(url_re, str(line_content))  # src="/img/github/69109512-f808bc80-0ab2-11ea-9e4d-b2b2f58fb474.png"
        line_url = str(line_url.group()).rstrip('"')  # 去除末尾双引号
        line_url = line_url.lstrip('src="')  # 去除前置 src="
        parse_link_from_line_list.append(line_url)
    return parse_link_from_line_list


def format_md_img(md_tmp_path):
    # 拿到包含 <img.*> 标签的 md 文件列表
    file_re = '<img.*>$'
    # url_re = r'(http[s])://(.*)[.png|.jpg|.jpeg]'
    # url_re = r'(src=")(.*)(img)(.*)(github).*[.png|.jpg|.jpeg]'
    url_re = r'(src=")(.*)(.png|.jpg|.jpeg)(")'
    count_url = 0

    include_img_label_md_list = match_include_img_label_file_from_md_list(md_tmp_path, file_re)  # 文件中包含图片的列表
    # print(include_img_label_md_list)

    for file in include_img_label_md_list:
        match_line_list = match_line_from_md_file(file, file_re)  # 当前文件的有图片的行列表
        # print(match_line_list)
        parse_link_from_line_list = match_link_from_line_list(match_line_list, url_re)  # 有图片的行列表，拿到了url，要用这个 url 拼真实地址
        print(parse_link_from_line_list)
        exit()
    #
    #         url = line_url.group()
    #         for i in "jpg", "png", "jpeg":
    #             if i in url:
    #                 url = url[0:url.find(i) + len(i)]
    #
    #         # print('url是%s' % url)
    #
    #         # 替换内容
    #         new_line = '![](%s){ width=50%% }' % url
    #         print('替换%s的%s行 为%s' % (file_name, line_number, new_line))
    #         update_file_by_line(file_name, int(line_number), new_line)
    #     # 输出
    #     # print('在%s中修改了%s个链接' % (file_name, len(line_2)))
    #     count_url += len(line_2)
    # print('一共修改了%s个格式\n' % count_url)
    #
    # # 替换图片路径为本地路径
    # count_url = 0
    # new_file_re = '!\[.*[\)|\}]'  # 匹配![开头，)或者}结尾
    # file_list = subprocess.getoutput('grep -rl \'%s\' --include=*.md %s' % (new_file_re, paht))
    # file_list_2 = []
    # for k in file_list.split('\n'):
    #     file_list_2.append(k)
    # for file_name in file_list_2:
    #     file_name = file_name.replace(' ', '\ ')
    #     line = subprocess.getoutput('grep  -n \'%s\' %s' % (new_file_re, file_name))
    #     line_2 = []
    #     for m in line.split('\n'):
    #         line_2.append(m)
    #     for alone_line in line_2:
    #         line_number = alone_line.split(':')[0]
    #         line_url_2 = re.search(url_re, str(alone_line))
    #         # print('line_url_2=%s ' % line_url_2.group())
    #         url = line_url_2.group()
    #         relative_file_name = file_name[file_name.index(paht) + len(paht):].replace(' ', '_').replace('/', '-')[
    #                              1:].replace('\\', '').replace('.md', '') + '--' + line_number + os.path.splitext(url)[
    #                                  -1]
    #         img_download_path = os.path.join(os.getcwd(), 'img', relative_file_name)
    #         # a[a.find('zzm'):a.find('zzm') + len("zzm")]
    #         for i in "jpg", "png", "jpeg":
    #             if i in img_download_path:
    #                 img_download_path = img_download_path[0:img_download_path.find(i) + len(i)]
    #         # 下载图片
    #         try:
    #             # os.system('wget -O %s %s' % (img_download_path, url))
    #             print(('wget -O %s %s' % (img_download_path, url)))
    #             subprocess.getoutput('wget -O %s %s' % (img_download_path, url))
    #             # print('wget -O %s %s' % (img_download_path, url))
    #             print('download %s ok' % relative_file_name)
    #         except Exception as e:
    #             print('download failed,Exception:%s' % e)
    #             exit()
    #
    #         new_line = '![](%s){ width=50%% }' % img_download_path
    #         print('替换%s的%s行 为%s\n' % (file_name, line_number, new_line))
    #         update_file_by_line(file_name, int(line_number), new_line)
    #
    #     # 输出
    #     # print('在%s中修改了%s个链接' % (file_name, len(line_2)))
    #     count_url += len(line_2)
    # print('一共下载并替换了%s个url为本地图片\n' % count_url)


def get_cur_abs_path():
    return os.path.dirname(os.path.abspath(sys.argv[0]))


def copy_user_guide_folder_to_cur_folder(user_guide_abs_path, cur_dir):
    print('info: 准备复制 %s 到 %s' % (user_guide_abs_path, cur_dir))
    shutil.copytree(user_guide_abs_path, cur_dir)  # tmp下没有userguide文件夹了 cp userguide/* tmp/


def check_folder_is_exists(string):
    if os.path.isdir(string):
        print('info: %s 已经存在，执行删除操作' % string)
        shutil.rmtree(string)
    return string


def main(user_guide_abs_path, md_list):
    md_tmp_path = os.path.join(get_cur_abs_path(), 'tmp/md')
    img_tmp_paht = os.path.join(get_cur_abs_path(), 'tmp/img')
    copy_user_guide_folder_to_cur_folder(user_guide_abs_path, check_folder_is_exists(md_tmp_path))  # tmp下没有userguide文件夹了 cp userguide/* tmp/

    # print(md_list)
    format_md_img(md_tmp_path)

# 根据相对路径生成图片名称
# relative_file_name = file_name[file_path.index(paht) + len(paht):]  # 取file_name这个路径里面，在paht之后的内容，=相对路径
# relative_file_name = relative_file_name.replace(' ', '_')  # 空格换成_
# relative_file_name = relative_file_name.replace('/', '-')  # /换成-
# relative_file_name = relative_file_name[1:]  # 去掉第一个字符-
# relative_file_name = relative_file_name.replace('.md', '')  # 去掉扩展名
# relative_file_name = relative_file_name + line_number  # 拼接行号
# relative_file_name = relative_file_name + os.path.splitext(url)[-1]  # 加上扩展名
# relative_file_name = relative_file_name.replace('\\', '')  # 去掉
