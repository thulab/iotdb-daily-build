@echo off

set superior_dir=%1

echo "get cn_internal_port"
for /f  "eol=; tokens=2,2 delims==" %%i in ('findstr /i "^cn_internal_port" %superior_dir%\conf\iotdb-confignode.properties') do (  set cn_internal_port=%%i )
echo %cn_internal_port%
echo "get cn_internal_address"
for /f  "eol=; tokens=2,2 delims==" %%i in ('findstr /i "^cn_internal_address" %superior_dir%\conf\iotdb-confignode.properties') do (  set cn_internal_address=%%i )
echo %cn_internal_address%
echo "get dn_rpc_port"
for /f  "eol=; tokens=2,2 delims==" %%i in ('findstr /i "^dn_rpc_port" %superior_dir%\conf\iotdb-datanode.properties') do (  set dn_rpc_port=%%i )
echo %dn_rpc_port%
echo "get dn_rpc_address"
for /f  "eol=; tokens=2,2 delims==" %%i in ('findstr /i "^dn_rpc_address" %superior_dir%\conf\iotdb-datanode.properties') do (  set dn_rpc_address=%%i )
echo %dn_rpc_address%

echo "Use netstat check port binding about confignode.."
netstat -ano | findstr ${{ steps.get-net-info.outputs.cn_internal_address }}:${{ steps.get-net-info.outputs.cn_internal_port }} | findstr LISTENING
echo "Use netstat check port binding about datanode.."
netstat -ano | findstr ${{ steps.get-net-info.outputs.dn_rpc_address }}:${{ steps.get-net-info.outputs.dn_rpc_port }} | findstr LISTENING
echo "Both confignode and datanode start suceessed."