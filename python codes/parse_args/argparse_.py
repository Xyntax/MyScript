# !/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'xy'

import argparse

"""

### add_argument 说明
不带'--'的参数
    调用脚本时必须输入值
    参数输入的顺序与程序中定义的顺序一致
'-'的参数
    可不输入    add_argument("-a")
    类似有'--'的shortname，但程序中的变量名为定义的参数名
'--'参数
    参数别名: 只能是1个字符，区分大小写
        add_argument("-shortname","--name", help="params means")，但代码中不能使用shortname
    dest: 参数在程序中对应的变量名称 add_argument("a",dest='code_name')
    default: 参数默认值
    help: 参数作用解释  add_argument("a", help="params means")
    type : 默认string  add_argument("c", type=int)
    action:

        store：默认action模式，存储值到指定变量。
        store_const：存储值在参数的const部分指定，多用于实现非布尔的命令行flag。
        store_true / store_false：布尔开关。 store_true.默认为False，输入则为true。 store_flase 相反
        append：存储值到列表，该参数可以重复使用。
        append_const：存储值到列表，存储值在参数的const部分指定。
        count: 统计参数简写输入的个数  add_argument("-c", "--gc", action="count")
        version 输出版本信息然后退出。

    const:配合action="store_const|append_const"使用，默认值
    choices:输入值的范围 add_argument("--gb", choices=['A', 'B', 'C', 0])
    required : 默认False, 若为 True, 表示必须输入该参数"""


def parse_args():
    print('BHP Net Tool')
    print()
    print('Usage:Netcat.py -t target_host -p port')
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l",
        "--listen",
        help="listen on [host]:[port] for incoming connections",
        action='store_true'
    )
    parser.add_argument(
        "-e",
        "--execute",
        help="execute the given file upon receiving a connection"
    )
    parser.add_argument(
        "-c",
        "--command",
        help="initialize a command shell",
        action='store_true'
    )
    parser.add_argument(
        "-u",
        "--upload",
        help="upon receiving connection upload a file and write to [destination]"
    )
    parser.add_argument(
        "target"
    )
    parser.add_argument(
        "port"
    )
    return parser.parse_args()


args = parse_args()
print(args)
