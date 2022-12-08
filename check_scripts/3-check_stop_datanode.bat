@echo off

set superior_dir=%1

for /f  "eol=; tokens=2,2 delims==" %%i in ('findstr /i "^dn_rpc_port"
%superior_dir%\conf\iotdb-datanode.properties') do (
set dn_rpc_port=%%i
)
for /f  "eol=; tokens=2,2 delims==" %%i in ('findstr /i "dn_rpc_address"
%superior_dir%\conf\iotdb-datanode.properties') do (
set dn_rpc_address=%%i
)

for /f "tokens=5" %%a in ('netstat /ano ^| findstr %dn_rpc_address%:%dn_rpc_port%') do (
if "%%a"=="" (
  echo "stop datanode succeed. continue."
  ) else (
    echo "PID is %%a"
    echo "stop datanode failed. exit."
    exit
    )
)
