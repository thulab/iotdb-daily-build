# title  
![daily-build](https://github.com/xiaoyekanren/iotdb-daily-build/actions/workflows/.github/workflows/main.yml/badge.svg)  
![check-status](https://github.com/xiaoyekanren/iotdb-daily-build/actions/workflows/.github/workflows/check_scripts.yml/badge.svg)  

## daily-build (main.yml)
build iotdb's and iot-benchmark's package every day. 
### iotdb

| iotdb             | 0.12.x | 0.13.x | 1.0.x | master|
|-------------------|--------|--------|-------|-------|
| all               |✓|✓|✓|✓|
| grafana-connector |✓|✓|-------|-------|
| grafana-plugin    |--------|✓|-------|-------|
| client-cpp        |✓|✓|✓|✓|
| python            |
| spark             |
| hadoop            |
| jdbc              |

### iot-benchmark

| iotdb-benchmark |
|-----------------|
| iotdb-0.12      |
| iotdb-0.13      |
| iotdb-1.0.x     |
| iotdb-master    |
| influxdb-2.0    |
| tdengine        |
| tdengine-3.0    |
| timescaledb     |
| timescaledb-cluster|

## start-stop-test (check_scripts.yml)
Execute the start-stop test case of the iotdb rel/1.0 branch every day.  

## release user-guide (release-userguide.yml)
one short to release user-guidy, need to 

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
