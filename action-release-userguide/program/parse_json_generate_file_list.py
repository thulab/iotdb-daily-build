# coding=utf-8
import parse_vue_config_ts


def generate_json_file_list(iotdb_path):
    """
    给一个iotdb的路径，返回一个包含多个版本中文用户手册的list
    """
    return list(parse_vue_config_ts.get_json_config_list(iotdb_path))


def get_link_from_children(children_list):
    links = []
    for one in children_list:
        links.append(dict(one).get('link') + '.md')
    return links


def generate_md_list(content_list):  # content_list -> list
    """
    给一个json串，生成一个markdown list
    """
    markdown_list = []
    for chapter in content_list:
        chapter = dict(chapter)  # chapter -> dict
        if not chapter.get('children'):  # 第一个dict的childen是空的，所以要过滤掉
            continue
        prefix = chapter.get('prefix')  # IoTDB-Introduction/
        links = get_link_from_children(chapter.get('children'))  # ['What-is-IoTDB.md', 'Features.md', 'Architecture.md', 'Scenario.md', 'Publication.md']
        for link in links:
            markdown_list.append(prefix + link)
    return markdown_list


def generate_md_dict(json_file_list):  # json_file_list就是多个配置文件解析的json， json就一个配置文件
    """
    给一个包含多个版本中文用户手册的list，返回一个title -> md_list的 dict
    """
    md_dict = {}
    for json in json_file_list:  # json_list -> list, json -> dict
        json = dict(json)
        for title in json.keys():  # title -> str "/zh/UserGuide/V1.1.x/"
            content_list = list(json.get(title))  # list
            md_list = generate_md_list(content_list)  # 将一个json串传过去，返回一个md列表
            print('info: 生成%s的md文件列表完成.' % title)
            md_dict[title] = md_list
    return md_dict


def main(iotdb_path):
    json_file_list = generate_json_file_list(iotdb_path)
    md_dict = generate_md_dict(json_file_list)
    for i in md_dict.keys():
        print(i)
        print(md_dict.get(i))


if __name__ == '__main__':
    iotdb_home = 'D:\\Src\\Java\\iotdb'
    main(iotdb_home)
