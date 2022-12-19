# title  
![daily-build](https://github.com/xiaoyekanren/iotdb-daily-build/actions/workflows/.github/workflows/main.yml/badge.svg)  
![check-status](https://github.com/xiaoyekanren/iotdb-daily-build/actions/workflows/.github/workflows/check_scripts.yml/badge.svg)  


| 版本   | 打包项                                                                                   |
|------|---------------------------------------------------------------------------------------|
| 0.12 | all, server, cli, grafana-connector, client-cpp                                       |
| 0.13 | all, server, cli, grafana-connector, grafana-plugin, client-cpp                       |
| 0.14 | all, server, cli, grafana-connector, grafana-plugin, datanode, confignode, client-cpp |



| iotdb             | 0.11 | 0.12 | 0.13 | 0,14 |
|-------------------|------|------|------|------|
| all               |
| server            |
| cli               |
| grafana-connector |
| grafana-plugin    |
| client-cpp        |
| python            |
| spark             |
| hadoop            |

| iotdb-benchmark |
|-----------------|
| 0.11            |
| 0.12            |
| 0.13            |
| 0.14            |
| influxdb        |
| kairosdb        |
| timescaledb     |
| taosd           |

## 当前打包内容
当前计划，分成3个
1. 主
   1. 打包all，server，这些
2. windows打包client-cpp
   1. 只打包windwos相关内容，当前只有client-cpp-win
   2. 为了提速
      1. 把mvn缓存拿过来用
      2. 新建个仓库，寸一份打包完成的boost
3. benchmark
   1. 打包各个benchmark的包

## tips
### push到另外一个仓库
不太好弄



## test_upload
据说github action屏蔽掉了 scp ssh 诸如此类命令，测试也已失败告终，所以要使用 marketplace 上封装好的方法。   
use `appleboy/scp-action@master`, find more with https://github.com/appleboy/scp-action    
```shell
strip_components: 2  # 控制upload后的文件夹层级，${{ github.workspace }}往后每多一层加+1
# strip_components: 2  # remove the specified number of leading path elements.
timeout: 120s  # 超时时间
command_timeout: 60m  # scp超时时间
tar_tmp_path: "/tmp/${{ secrets.FILE_SERVER_IP_USER }}/"  # upload的临时文件存放位置
timeout  # timeout for ssh to remote host, default is 30s
command_timeout  # timeout for scp command, default is 10m
```
