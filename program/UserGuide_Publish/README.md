# pandoc
将iotdb/docs/zh/UserGuide/下的md文件根据需求转换为docx文档，作为中文交付物。
# 2022-08-16
参考文档`README_20220816.md`
## 一.执行方式
执行startup.py，根据提示向下执行

```shell
cd iotdb-private-tool/pandoc
python3 startup.py
```

## 二.安装说明
> * 安装python3
> * 安装pandoc,https://www.pandoc.org/  (当前为2.11.3.2)
## 三.IoTDB的中文目录
> iotdb/docs/zh/UserGuide  

## 四.pandoc使用方式 
```shell script
pandoc -f markdown -t docx --reference-doc template.docx -o output.docx -N [file_list]
-f [str] 输入文件格式
-t [str] 输出文件格式
--reference-doc [file] 模板文件
-o [file] 输出文件
-N 输出中的节标题进行编号
--log=[file] 输出log.json
```

## 五.文件说明  
### 1.scan_directory.md(可选)  
形成指定路径下所有文件路径的列表，保存在当前目录的include.txt  
(建议手动调整include.txt)  

### 2.format_file_list.py  
格式化include.txt,转译空格,写到一行  

### 3.format_md_img.py  
将markdown文件里面的图片链接从html调用方式修改为markdown的语法，并下载  
```markdown
![avator](path_or_url img_name){ width=50%% }
```

### 4.execute.md
输入包含一个或多个md文件的字符串,执行pandoc来生成docx  

### 5.startup.py
将1-4按顺序执行,将4个文件整合到了一起  

### 6.page.md
作为生成docx的首页和目录页  
### 7.template.docx
作为生成docx的模板  
### 8.include.txt
已经写好的列表，pandoc根据整个表的顺序来生成docx
## 六.仓库地址
### IoTDB-private-tool
> https://github.com/jixuan1989/iotdb-private-tool  
### pandoc
> https://www.pandoc.org

## 七.Tips
>* 1.word的分页符
```xml
<w:p>
<w:r>
    <w:br w:type="page"/>
  </w:r>
</w:p>
```

>* 2.docx详细内容

首先将docx扩展名改为zip，并打开
```
/.zip
│  [Content_Types].xml
├─docProps
├─word
│  │  document.xml(存放全部文本)
│  │  *.xml
│  ├─media(存放照片)
│  ├─theme
│  └─_rels
└─_rels
```

>* 3.docx里xml说明
```xml  
<w:document>
    <w:body>
        <w:p><!--段落-->
            <w:pPr>
                <w:pStyle><!--段落格式--></w:pStyle>
                <w:rPr><!--文本格式--></w:rPr>
            </w:pPr>
            <w:r>
                <w:rPr><!--文本格式--></w:rPr>
                <w:t><!--文本内容--></w:t>
            </w:r>
        </w:p></w:p>
    </w:body>
</w:document>
```

