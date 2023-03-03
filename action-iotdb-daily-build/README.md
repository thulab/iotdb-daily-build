# iotdb-daily-build (iotdb 每日发布)
main.yml

## 内容
构建jdk8、11两个版本的iotdb、iot-benchmark的二进制包
包含内容：
1. iotdb 0.12 (all, client-cpp-win, grafana)
2. iotdb 0.13 (all, client-cpp-win, grafana)
3. iotdb 1.0 (all, client-cpp-win, grafana)
4. iotdb master (all, client-cpp-win, grafana)
5. benchmark (influxdb, iotdb-0.13, iotdb-0.12, iotdb-1.0, tdengine, tdengine-3.0, timescaledb, timescaledb-cluster)


### windows下client-cpp的准备
使用action每日构建iotdb-client-cpp-win, 2022-04-13  

* 操作系统  
windows-latest, windows-2019
* jdk  
1.8.0.322+6 (default)  
* maven  
3.8.5 (default)  
* visual studio  
win-latest, Visual Studio 17 2022 (default)  
win-2019, Visual Studio 16 2019 (default)  
* boost  
自行下载  
* flex  
自行下载  
* bison  
自行下载  
* openssl    
自行下载 (预装的有问题)  
* cmake  
3.18.1 (default)

参考这个文档：  
> https://github.com/actions/virtual-environments/blob/main/images/win/Windows2022-Readme.md  
> https://github.com/actions/virtual-environments/blob/main/images/win/Windows2019-Readme.md  
