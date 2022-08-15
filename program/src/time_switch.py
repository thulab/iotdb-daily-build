# coding=utf-8
import sys
import time


if __name__ == '__main__':
    if len(sys.argv[1:]) != 1:
        print('只能设置1个参数')
        exit()
    input_value = sys.argv[1]
    input_value_split = time.strptime(input_value, "%Y-%m-%d %H:%M:%S %z")
    switch_timestamp = time.mktime(input_value_split)
    print(int(switch_timestamp))
