#/bin/bash

echo common para ...
current_path=$(pwd)
start_time=$(date +%Y_%m_%d_%H_%M_%S)
work_dict=${current_path}/performance_test-${start_time}

echo install depend packages
sudo apt-get update
sudo apt-get install unzip wget git -y

echo mkdir work directory ...
mkdir_test_folder() {
    if [ ! -d ${work_dict} ]; then
        mkdir -p ${work_dict}
    else
        rm -rf ${work_dict}
        mkdir -p ${work_dict}
    fi
}
mkdir_test_folder

echo install jdk and jre ...
install_jdk() {
    sudo apt-get install openjdk-8-jre openjdk-8-jdk -y
    java -version
}
install_jdk

echo install maven ...
install_mvn() {
    sudo apt-get install maven -y
    mvn -v
}
install_mvn

echo compile IoTDB ...
compile_server() {
    cd ${work_dict}
    git clone https://github.com/apache/iotdb.git
    iotdb_src_home=${work_dict}/iotdb
    cd ${iotdb_src_home}
    # checkout branch
    # git checkout [branch]
    mvn clean package -pl distribution -DskipTests
    iotdb_cur_branch=${work_dict}/iotdb_cur_branch
    cp -r ${iotdb_src_home}/distribution/target/apache-iotdb-*-server-bin/apache-iotdb-0*-server-bin ${iotdb_cur_branch}
}
compile_server

echo compile benchmark ...
compile_benchmark() {
    cd ${work_dict}
    git clone https://github.com/thulab/iotdb-benchmark.git
    benchmark_src_home=${work_dict}/iotdb-benchmark
    cd ${benchmark_src_home}
    mvn spotless:apply -q
    mvn clean package -pl core,iotdb-0.12 -Dmaven.test.skip=true
    benchmark_bin_home=${work_dict}/iotdb-benchmark-bin
    cp -r ${benchmark_src_home}/iotdb-0.12/target/iotdb-0.12-0.0.1 ${benchmark_bin_home}
}
compile_benchmark

echo modify benchmark config ...
modi_benchmark_config() {
    benchmark_conf=${benchmark_bin_home}/conf/config.properties
    sed -i 's/^LOOP.*/LOOP=100000/g' ${benchmark_conf}
}
modi_benchmark_config

echo start 1st IoTDB...
start_cur_iotdb() {
    cd ${iotdb_cur_branch}
    nohup sbin/start-server.sh >/dev/null 2>&1 &
    sleep 5
    iotdb_pid=$(jps -l | grep 'org.apache.iotdb.db.service.IoTDB' | awk '{print $1}')
    echo IoTDB\'s PID is ${iotdb_pid}
}
start_cur_iotdb

echo define benchmark output log file...
cur_bm_file=${work_dict}/benchmark_cur_branch.txt
pre_bm_file=${work_dict}/benchmark_previous_branch.txt

echo start benchmark 1st...
start_benchmark_one() {
    cd ${benchmark_bin_home}
    nohup ./benchmark.sh >${cur_bm_file} &
    sleep .5
    benchmark_pid=$(jps -l | grep 'cn.edu.tsinghua.iotdb.benchmark.App' | awk '{print $1}')
    echo Benchmark\'s PID is ${benchmark_pid}
}
start_benchmark_one

echo listen pid , until 1st benchmark over...
while true; do
    if test $(jps -l | grep 'cn.edu.tsinghua.iotdb.benchmark.App' | awk '{print $1}'); then
        echo benchmark not finish...
        tail -n 1 ${cur_bm_file}
        sleep 3
    else
        echo benchmark over...
        break
    fi
done

echo kill IoTDB...
kill -9 ${iotdb_pid}

echo compile previous IoTDB...
compile_previous_server() {
    cd ${iotdb_src_home}
    # checkout branch
    # git checkout [branch]
    mvn clean package -pl distribution -DskipTests
    iotdb_previous_branch=${work_dict}/iotdb_previous_branch
    cp -r ${iotdb_src_home}/distribution/target/apache-iotdb-*-server-bin/apache-iotdb-0*-server-bin ${iotdb_previous_branch}
}
compile_previous_server

echo start IoTDB...
start_previous_iotdb() {
    cd ${iotdb_previous_branch}
    nohup sbin/start-server.sh >/dev/null 2>&1 &
    sleep 5
    iotdb_pid=$(jps -l | grep 'org.apache.iotdb.db.service.IoTDB' | awk '{print $1}')
    echo IoTDB\'s PID is ${iotdb_pid}
}
start_previous_iotdb

echo start benchmark 2rd...
start_benchmark_two() {
    cd ${benchmark_bin_home}
    ./benchmark.sh >${pre_bm_file} &
    # sleep 3
    benchmark_pid=$(jps -l | grep 'cn.edu.tsinghua.iotdb.benchmark.App' | awk '{print $1}')
    echo Benchmark\'s PID is ${benchmark_pid}
}
start_benchmark_two

echo listen pid , until 2rd benchmark over...
while true; do
    if test $(jps -l | grep 'cn.edu.tsinghua.iotdb.benchmark.App' | awk '{print $1}'); then
        echo benchmark not finish...
        tail -n 1 ${pre_bm_file}
        sleep 3
    else
        echo Benchmark over...
        break
    fi
done

echo kill IoTDB...
kill -9 ${iotdb_pid}

echo check benchmark output file yes or no exist...
check_two_results() {
    if [ ! -f ${cur_bm_file} ] || [ ! -f ${pre_bm_file} ]; then
        echo output file not found or not 2 files...
        exit
    fi
}
check_two_results

echo
echo
echo
echo ----------
echo output results...
cur_time_elapsed=$(cat ${cur_bm_file} | grep 'Test elapsed' | awk '{print $8}')
pre_time_elapsed=$(cat ${pre_bm_file} | grep 'Test elapsed' | awk '{print $8}')
echo -e cur_time_elapsed ${cur_time_elapsed}'\t'pre_time_elapsed ${pre_time_elapsed}
echo
# create_schema
cur_create_schema=$(cat ${cur_bm_file} | grep 'Create schema' | awk '{print $4}')
pre_create_schema=$(cat ${pre_bm_file} | grep 'Create schema' | awk '{print $4}')
echo -e cur_create_schema ${cur_create_schema}'\t'pre_create_schema ${pre_create_schema}
echo
# throughput_points/s
cur_throughput=$(cat ${cur_bm_file} | grep -A2 '\---Result Matrix---' | grep 'INGESTION' | awk '{print $6}')
pre_throughput=$(cat ${pre_bm_file} | grep -A2 '\---Result Matrix---' | grep 'INGESTION' | awk '{print $6}')
echo -e cur_throughput:${cur_throughput}'\t'pre_throughput:${pre_throughput}
echo
# avg_in
cur_avg_latency=$(cat ${cur_bm_file} | grep -A2 '\---Latency (ms) Matrix---' | grep 'INGESTION' | awk '{print $2}')
pre_avg_latency=$(cat ${pre_bm_file} | grep -A2 '\---Latency (ms) Matrix---' | grep 'INGESTION' | awk '{print $2}')
echo -e cur_avg_latency:${cur_avg_latency}'\t'pre_avg_latency:${pre_avg_latency}
echo ----------
