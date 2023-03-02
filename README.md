# title  
<!--
![daily-build](https://github.com/xiaoyekanren/iotdb-daily-build/actions/workflows/.github/workflows/main.yml/badge.svg)  
![check-status](https://github.com/xiaoyekanren/iotdb-daily-build/actions/workflows/.github/workflows/workflow-check-start_stop.yml/badge.svg)  
-->
<img src="https://github.com/xiaoyekanren/iotdb-daily-build/actions/workflows/.github/workflows/main.yml/badge.svg" width = "350" height = "50" />
<img src="https://github.com/xiaoyekanren/iotdb-daily-build/actions/workflows/.github/workflows/workflow-check-start_stop.yml/badge.svg" width = "350" height = "50" />



## daily-build (main.yml)
build iotdb's and iot-benchmark's package every day. 
### iotdb

| iotdb             | 0.12.x | 0.13.x | 1.0.x | master|
|-------------------|--------|--------|-------|-------|
| all               |✓|✓|✓|✓|
| grafana-connector |✓|✓|
| grafana-plugin    ||✓|
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
one short to release user-guidy, need to select pages by hand before relase. 
