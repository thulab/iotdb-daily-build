@echo off
echo "start" %ERRORLEVEL%
set superior_dir=%1
echo "check config" %ERRORLEVEL%
for /f  "eol=; tokens=2,2 delims==" %%i in ('findstr /i "^dn_rpc_port"
%superior_dir%\conf\iotdb-datanode.properties') do (
set dn_rpc_port=%%i
)
for /f  "eol=; tokens=2,2 delims==" %%i in ('findstr /i "dn_rpc_address"
%superior_dir%\conf\iotdb-datanode.properties') do (
set dn_rpc_address=%%i
)
echo "netstat" %ERRORLEVEL%
netstat /ano | findstr %dn_rpc_address%:%dn_rpc_port%  & set %ERRORLEVEL%=0
echo "check port" %ERRORLEVEL%
for /f "tokens=5" %%a in ('netstat /ano ^| findstr %dn_rpc_address%:%dn_rpc_port%') do (
echo "PID is %%a, stop datanode failed. exit."
exit 1
)
echo "finally" %ERRORLEVEL%
echo "stop datanode succeed. continue."
@REM exit /B
