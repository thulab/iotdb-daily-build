# 用户手册发布
将目录 iotdb/docs/zh/UserGuide 的md文件转换为doc文档

## 程序说明
```shell
.
├── Templates
│   ├── page.md  # 首页，目录页
│   ├── template_iotdb.docx  # iotdb 模版
│   └── template_timecho.docx  # timecho 模版
├── common.py  # 公共的函数，当前只有1个
├── format_md_img.py  # 格式化图像、下载图像
├── main.py  # 启动 pandoc
├── parse_json_generate_file_list.py  # 搜索 iotdb 的 site 目录，将 vue 的全部 ts文件解析，返回一个 version:md list 的字典
└── parse_vue_config_ts.py  # 解析 json，生成一个list
```
## 程序执行顺序：
> 程序入口： python3 main.py <iotdb_home> 
1. 从 iotdb 拿到 master 版本的 vue-list
   1. parse_json_generate_file_list.py 通过iotdb的目录，找到 vue 存储 master-md 的 ts 文件，发给下一步
      1. parse_vue_config_ts.py， 将 ts 转换成 json， 将 json 转换成list，返回上一步 
   2. parse_json_generate_file_list.py 将 list + vue 的标题，放入字典，传到下一个程序
2. 从 iotdb 的 docs/zh/userguide 拷贝到程序的tmp目录
   1. format_md_img.py
      1. 拷贝 md 文件
      2. 将 md 文件的图片相关的代码全部改为html类型 （当前 md 的图片标签，html 标签混用）
         ```
         ![](/root/a.png){witdh=50%}
         ```
      3. 统一全部图片为本地图片（包含在线图片、本地图片）
      4. 下载图片
3. main.py 开始 pandoc

## 剩下的问题
1. generate_md_list.py   
里面的判断行尾多出来的逗号和分号，可以在逐行读取的时候，判断当前行和上一行来做append
2. 转换成docx之后，图片显示不全  
这个是因为图片使用了默认的段落格式（固定行距20磅），当前尚未想到怎么改，可以考虑重新生成一份模版文件（Templates/template_xxx.docx）
