@echo off

set superior_dir=%1

echo "get cn_internal_port"
for /f  "eol=; tokens=2,2 delims==" %%i in ('findstr /i "^cn_internal_port" %superior_dir%\conf\iotdb-confignode.properties') do (  set cn_internal_port=%%i )
echo "get cn_internal_address"
for /f  "eol=; tokens=2,2 delims==" %%i in ('findstr /i "^cn_internal_address" %superior_dir%\conf\iotdb-confignode.properties') do (  set cn_internal_address=%%i )
echo "get dn_rpc_port"
for /f  "eol=; tokens=2,2 delims==" %%i in ('findstr /i "^dn_rpc_port" %superior_dir%\conf\iotdb-datanode.properties') do (  set dn_rpc_port=%%i )
echo "get dn_rpc_address"
for /f  "eol=; tokens=2,2 delims==" %%i in ('findstr /i "^dn_rpc_address" %superior_dir%\conf\iotdb-datanode.properties') do (  set dn_rpc_address=%%i )
echo "get over"