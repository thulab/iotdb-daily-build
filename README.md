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
master 分支与最新 release tag（v* 稳定版本）每天都会在 windows-2022（Visual Studio 2022 / MSVC v143）上打包  
c++ iotdb-session 客户端（`iotdb-session-cpp-<version>-windows-x86_64-msvc14.3.zip`，含 .sha512 校验文件）。  
构建使用 apache/iotdb 自带的 mvnw（maven 3.9.12）、JDK 17，依赖 boost-msvc-14.3、winflexbison3 与固定版本的 OpenSSL 3.x。  
linux 同样在 ubuntu-latest 上构建 `iotdb-session-cpp-<version>-linux-x86_64-glibc2.28.zip`。  





----------
* iotdb 用户手册发布  
one short to release user-guidy, need to select pages by hand before relase.  
* test build rel/0.12  
* test self-hosted  
* test upload  
* tools 删除过早的tag  

