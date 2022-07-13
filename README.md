# title  
![daily-build](https://github.com/xiaoyekanren/iotdb-daily-build/actions/workflows/.github/workflows/main.yml/badge.svg)


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
