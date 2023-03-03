#!/bin/bash
set -e

cd $1

# tag_list.txt --> 当前tag列表
git tag > tag_list.txt

# all_line --> 全部行数
all_line=$(cat tag_list.txt | wc -l)

# reserved_rows --> 要保留的tag数量
reserved_rows=20
# 如果tag太少就报错推出
if [ ${reserved_rows} -gt ${all_line} ]; then
     echo "tag共$all_line个，要删除$reserved_rows个，删除失败"
     exit 0
     exit 1
fi

# tag_delete.txt --> 要删除的tag
cat tag_list.txt | head -n $(expr $all_line - $reserved_rows) > tag_delete.txt

# 删除tag
while read line
do
    git tag -d ${line}
    git push origin :refs/tags/${line}
done < tag_delete.txt
