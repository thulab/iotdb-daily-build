# 用户手册发布
将目录 iotdb/docs/zh/UserGuide 的md文件转换为doc文档

程序按顺序排列：
1. parse_vue_config_ts.py
   > 检测 iotdb/site/src/main/.vuepress/sidebar，找到用户手册的全部ts文件，修改格式后作为json导入，返回json list
2. parse_json_generate_file_list.py
   > 联合1使用  
   > 将上一步的json list 逐个读取，生成不同版本的 dict，version: markdown列表  
3. 

## generate_md_list.py
里面的判断行尾多出来的逗号和分号，可以在逐行读取的时候，判断当前行和上一行来做append

