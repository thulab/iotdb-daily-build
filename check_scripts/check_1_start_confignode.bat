@echo off

set superior_dir=%1

for /f  "eol=; tokens=2,2 delims==" %%i in ('findstr /i "^cn_internal_port"
%superior_dir%\conf\iotdb-confignode.properties') do (
set cn_internal_port=%%i
)
for /f  "eol=; tokens=2,2 delims==" %%i in ('findstr /i "cn_internal_address"
%superior_dir%\conf\iotdb-confignode.properties') do (
set cn_internal_address=%%i
)

for /f "tokens=5" %%a in ('netstat /ano ^| findstr %cn_internal_address%:%cn_internal_port%') do (
if "%%a"=="" (
  echo "start confignode failed."
  exit
  ) else (
    echo "start confignode succeed. continue."
    )
)