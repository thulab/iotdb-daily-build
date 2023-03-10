# coding=utf-8

def replace_space_add_backslash(md_list):
    format_md_list = []
    for md in md_list:
        format_md_list.append(md.replace(' ', '\ '))
    return format_md_list
