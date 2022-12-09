@echo off
echo "start" %ERRORLEVEL%
set superior_dir=%1
echo "check config" %ERRORLEVEL%
for /f  "eol=; tokens=2,2 delims==" %%i in ('findstr /i "^cn_internal_port"
%superior_dir%\conf\iotdb-confignode.properties') do (
set cn_internal_port=%%i
)
for /f  "eol=; tokens=2,2 delims==" %%i in ('findstr /i "cn_internal_address"
%superior_dir%\conf\iotdb-confignode.properties') do (
set cn_internal_address=%%i
)
echo "netstat" %ERRORLEVEL%
netstat -ano | findstr %cn_internal_address%:%cn_internal_port% | findstr /V TIME_WAIT & set %ERRORLEVEL%=0
echo "check port" %ERRORLEVEL%
for /f "tokens=5" %%a in ('netstat -ano ^| findstr %cn_internal_address%:%cn_internal_port% ^| findstr /V TIME_WAIT') do (
echo "PID is %%a, stop confignode failed. exit."
exit 1
)
echo "finally" %ERRORLEVEL%
echo "start confignode succeed. continue."
@REM exit /B
