# coding=UTF-8
import os
import sys
import re
import subprocess
import shutil
import common


def return_re_list(re_type):
    if re_type == 'file':
        # 拿到两种格式的标签
        # <img style="width:100%; max-width:800px; max-height:600px; margin-left:auto; margin-right:auto; display:block;" src="/img/github/69109512-f808bc80-0ab2-11ea-9e4d-b2b2f58fb474.png">
        # ![avatar](/img/UserGuide/CLI/Command-Line-Interface/AdministrationConsole.png?raw=true)
        file_res_list = ['<img.*>$', '![.*[(.png)(.jpg)(.jpeg)(.svg)].*].*']
        return file_res_list
    elif re_type == 'url':
        # 三种格式
        # <img style="width:100%; max-width:800px; max-height:600px; margin-left:auto; margin-right:auto; display:block;" src="https://github.com/apache/iotdb-bin-resources/blob/main/integration-test/pic/step.svg">
        # ![iotdb_prometheus_grafana](https://raw.githubusercontent.com/apache/iotdb-bin-resources/main/docs/UserGuide/System%20Tools/Metrics/iotdb_prometheus_grafana.png)
        # ![architecture-design](/img/UserGuide/API/IoTDB-InfluxDB/architecture-design.png?raw=true)
        url_re_list = [r'(src=")(.*)(.png|.jpg|.jpeg|.svg)(.*)(")', r'(http[s])(://)(.*)(.png|.jpg|.jpeg|.svg)', r'(/.*)(/.*)(.png|.jpg|.jpeg|.svg)']
        return url_re_list
    else:
        print('fatal: 不知所谓')
        exit()


def match_include_img_label_file_from_md_list(tmp_md_path, file_res):  # 捕获包含 img 标签的文件从 md_list
    format_file_list = []
    for file_re in file_res:
        # print('grep -rl \'%s\' --include=*.md %s' % (file_re, tmp_md_path))
        file_list = subprocess.getoutput('grep -rl \'%s\' --include=*.md %s' % (file_re, tmp_md_path)).split('\n')  # -r 递归搜索文件夹，-l 只显示匹配到的文件名
        format_file_list += file_list
    return common.replace_space_add_backslash(format_file_list)


def match_line_from_md_file(file, file_res):  # 捕获包含 img 标签的文件从 md_file，返回 list
    url_list = []
    for file_re in file_res:
        # print('grep -no \'%s\' %s' % (file_re, file))
        file_list = subprocess.getoutput('grep -no \'%s\' %s' % (file_re, file)).split('\n')  # -n 显示行号， -o 只显示匹配到的内容
        url_list += file_list
    return common.replace_space_add_backslash(url_list)


def format_link_or_path(line_url):  # 把通过正则表达式匹配到的字符串再次格式化一下，因为不太准确
    line_url = str(line_url)
    line_url = line_url.rstrip('"')  # 去除末尾双引号，如果有
    line_url = line_url.lstrip('src="')  # 去除前置 src="，如果有

    if ' alt=' in line_url:  # 这个 re 容易把 后面的 alt 标签也带过来。。
        line_url = line_url.split(' alt=')[0]
    if '?raw' in line_url:  # 带有raw的link会自动跳转到 raw.githubusercontent.com 上，因为后面做了这一步，所以这个地方就不做了
        line_url = line_url.split('?raw')[0]
    return line_url


def replace_local_path_to_link(url):  # 将本地图片格式改为网络链接，也就是统一图片的地址为http链接，用于在下一步进行下载
    url = str(url)
    if url[0] == '/':  # 替换本地路径
        iotdb_img_raw_url = 'https://raw.githubusercontent.com/apache/iotdb/master/site/src/main/.vuepress/public'  # 加raw跳转之后的地址
        return os.path.join(iotdb_img_raw_url, url[1:])  # 拼接的第二个字符串的第一个字符是 / 时会跳过之前的内容，所以要把 / 去掉
    elif 'github.com' in url:
        return url.replace('github.com', 'raw.githubusercontent.com').replace('blob/', '')  # blob在raw这个链接下是没有的，所以要删除
    else:
        return url


def use_python_re_return_match_url(url_res, line_content):
    url_res = list(url_res)
    line_content = str(line_content)
    # print(line_content)
    for url_re in url_res:
        match_url = re.search(url_re, line_content)
        if not match_url:
            # print(f're {url_re} 没有匹配到')
            continue
        return match_url.group()  # group加到前面就会报错


def match_link_from_line_list(match_line_list):
    url_res = return_re_list('url')
    parse_link_from_line_list = []
    parse_link_from_line_list_raw = []
    for match_line in match_line_list:
        # print(match_line)
        line_number = match_line.split(':')[0]
        line_content = match_line[len(line_number + ':'):]  # <img style="width:100%; max-width:800px; max-height:600px; margin-left:auto; margin-right:auto; display:block;" src="/img/github/69109512-f808bc80-0ab2-11ea-9e4d-b2b2f58fb474.png">
        # print(f'line_content is {line_content}')
        parse_link_from_line_list_raw.append(line_content)  # 要整一个原始内容的列表用于替换

        match_content = use_python_re_return_match_url(url_res, line_content)  # 使用python的正则表达式去匹配
        # print(f'match_content is {match_content}')

        line_url = format_link_or_path(match_content)  # 将正则表达式匹配到的不规整的地方去掉
        line_url = replace_local_path_to_link(line_url)  # 如果是本地地址的话，将本地地址替换为github实际下载的地址

        parse_link_from_line_list.append(line_url)
    return parse_link_from_line_list_raw, parse_link_from_line_list


def match_include_img_md_list(md_tmp_path):
    file_res = return_re_list('file')
    print('info: 开始匹配包含 img 的 md 文件列表')
    include_img_label_md_list = match_include_img_label_file_from_md_list(md_tmp_path, file_res)  # 文件中包含图片的列表
    print('info: 匹配完成')
    # print(include_img_label_md_list)
    return include_img_label_md_list


def generate_raw_and_new_url_dict(include_img_label_md_list):
    url_dict_raw = {}
    url_dict = {}
    file_res = return_re_list('file')
    for file in include_img_label_md_list:
        # print('info: 从文件 %s 里面匹配图片的 path or url' % file)
        match_line_list = match_line_from_md_file(file, file_res)  # 当前文件的有图片的行列表
        parse_link_from_line_list_raw, parse_link_from_line_list = match_link_from_line_list(match_line_list)  # 有图片的行列表，拿到了url，要用这个 url 拼真实地址
        # print(parse_link_from_line_list)
        url_dict_raw[file] = parse_link_from_line_list_raw
        url_dict[file] = parse_link_from_line_list
    return url_dict_raw, url_dict


def replace_str_a_to_str_b(file, raw_str, new_str):
    print('info: 将 %s 替换为 %s ' % (raw_str, new_str))
    with open(file, 'r') as f:
        file_content = f.readlines()
        for line in file_content:
            if not line.replace('\n', ''):  # 如果有空行就跳过
                continue
            if raw_str in line:
                file_content[file_content.index(line)] = line.replace(raw_str, new_str)
            else:
                continue
    with open(file, 'w') as f:
        f.writelines(file_content)


def replace_path_to_link_from_list(md, raw_link, dest_link):
    dest_link = list(dest_link)
    raw_link = list(raw_link)
    for index in range(len(raw_link)):
        format_link = '![](%s){ width=50%% }' % dest_link[index]
        replace_str_a_to_str_b(md, raw_link[index], format_link)    # 这里改range


def replace_path_to_link_from_dict(url_dict_raw, url_dict_dest):
    print('info: 将全部的非 url 地址统一为链接')
    for md in url_dict_raw.keys():
        print('info: 当前文件是 %s' % md)
        replace_path_to_link_from_list(md, url_dict_raw.get(md), url_dict_dest.get(md))
        print('\n')


def get_cur_abs_path():
    return os.path.dirname(os.path.abspath(sys.argv[0]))


def copy_user_guide_folder_to_cur_folder(user_guide_abs_path, cur_dir):
    print('info: 复制 %s 到 %s' % (user_guide_abs_path, cur_dir))
    shutil.copytree(user_guide_abs_path, cur_dir)  # tmp下没有userguide文件夹了 cp userguide/* tmp/


def check_folder_if_exists_then_rm(string):
    if os.path.isdir(string):
        print('info: %s 存在，删除' % string)
        shutil.rmtree(string)
    return string


def check_folder_if_not_exists_then_mkdir(string):
    if not os.path.isdir(string):
        print('info: %s 不存在，创建' % string)
        os.mkdir(string)
    return string


def download_img(url, dest_abs_path):
    print(('wget -O %s %s' % (dest_abs_path, url)))
    print(subprocess.getoutput('wget -O %s %s' % (dest_abs_path, url)))
    pass


def join_local_name(url, img_tmp_path):
    img_name = url.split('/')[-1]  # 图片的实际名称
    before_name_three_path = '_'.join(url.split('/')[-4:-1])  # 取url里面的最后三节路径拼一个name
    truth_name = os.path.join(img_tmp_path, (before_name_three_path + '_' + img_name).replace('-', '_'))
    return truth_name


def generate_local_name_lists_and_download_img(url_list, img_tmp_path):
    dict_list = []
    for url in url_list:
        local_abs_img_name = join_local_name(url, img_tmp_path)
        dict_list.append(local_abs_img_name)
        # 下载图片
        download_img(url, local_abs_img_name)
    return dict_list


def download_img_to_tmp_and_return_url_dict_local(url_md_dict, img_tmp_path):
    url_dict_local = {}

    check_folder_if_exists_then_rm(img_tmp_path)  # 删除再创建 img 的临时路径
    check_folder_if_not_exists_then_mkdir(img_tmp_path)

    for md in url_md_dict.keys():
        # 本地字典
        url_dict_local[md] = generate_local_name_lists_and_download_img(url_md_dict.get(md), img_tmp_path)
    # print(url_dict_local)
    return url_dict_local


def main(user_guide_abs_path):
    md_tmp_path = os.path.join(get_cur_abs_path(), 'tmp/md')
    img_tmp_path = os.path.join(get_cur_abs_path(), 'tmp/img')
    # 拷贝用户手册目录
    copy_user_guide_folder_to_cur_folder(user_guide_abs_path, check_folder_if_exists_then_rm(md_tmp_path))  # tmp下没有userguide文件夹了 cp userguide/* tmp/
    # 生成 新、旧 url的字典
    # print(md_list)
    include_img_label_md_list = match_include_img_md_list(md_tmp_path)
    url_dict_raw, url_dict = generate_raw_and_new_url_dict(include_img_label_md_list)
    # 下载图片到 img_tmp_paht
    url_dict_local = download_img_to_tmp_and_return_url_dict_local(url_dict, img_tmp_path)
    # 将文件夹内的全部的url统一成标准的url
    replace_path_to_link_from_dict(url_dict_raw, url_dict_local)
    return md_tmp_path
