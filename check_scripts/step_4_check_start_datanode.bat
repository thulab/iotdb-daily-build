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

netstat -ano | findstr %dn_rpc_address%:%dn_rpc_port% | findstr LISTENING

for /f "tokens=5" %%a in ('netstat -ano | findstr %dn_rpc_address%:%dn_rpc_port% | findstr LISTENING') do (
echo "start datanode succeed. continue."
exit /B
)

echo "start datanode failed."
exit 1
