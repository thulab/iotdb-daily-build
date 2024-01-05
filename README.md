# iotdb-build  
iotdb的相关的一些文件生成脚本，依赖于github action
<!--
![daily-build](https://github.com/xiaoyekanren/iotdb-daily-build/actions/workflows/.github/workflows/main.yml/badge.svg)  
![check-status](https://github.com/xiaoyekanren/iotdb-daily-build/actions/workflows/.github/workflows/workflow-check-start_stop.yml/badge.svg)  
-->
## iotdb 启停测试
<img src="https://github.com/xiaoyekanren/iotdb-daily-build/actions/workflows/.github/workflows/workflow-check-start_stop.yml/badge.svg" width = "350" height = "50" />  
Execute the start-stop test case of the iotdb rel/1.0 branch every day.  

## iotdb 每日发布
<img src="https://github.com/xiaoyekanren/iotdb-daily-build/actions/workflows/.github/workflows/main.yml/badge.svg" width = "350" height = "50" />  

### 关于client-cpp  
windows使用的是windows-2022，Visual Studio Enterprise 2022，工具集版本是VC.v141  

linux使用的是ubuntu-22.04，gcc使用的是11.2.0，以下为ubuntu20+安装gcc11的方式：  
```shell
sudo add-apt-repository ppa:ubuntu-toolchain-r/test  # 通过该命令将 Ubuntu 官方的 toolchain-test 源添加到系统中
sudo apt update
sudo apt install build-essential
sudo apt install gcc-11 g++-11
```
  





----------
* iotdb 用户手册发布  
one short to release user-guidy, need to select pages by hand before relase.  
* test build rel/0.12  
* test self-hosted  
* test upload  
* tools 删除过早的tag  

