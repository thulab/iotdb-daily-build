@echo off
echo "start"
set superior_dir=%1
echo "check config"
for /f  "eol=; tokens=2,2 delims==" %%i in ('findstr /i "^dn_rpc_port"
%superior_dir%\conf\iotdb-datanode.properties') do (
set dn_rpc_port=%%i
)
for /f  "eol=; tokens=2,2 delims==" %%i in ('findstr /i "dn_rpc_address"
%superior_dir%\conf\iotdb-datanode.properties') do (
set dn_rpc_address=%%i
)
echo "netstat"
netstat /ano | findstr %dn_rpc_address%:%dn_rpc_port%
echo "check port"
for /f "tokens=5" %%a in ('netstat /ano ^| findstr %dn_rpc_address%:%dn_rpc_port%') do (
echo "PID is %%a, stop datanode failed. exit."
exit 0
)
echo "finally"
echo "stop datanode succeed. continue."
exit /B
