#!/bin/bash

# 利用死循环秒删指定路径的webshell
# 单线程的两次HTTP请求竞争不过本地shell脚本，也就是说webshell传上来也无法利用，个人感觉防御CTF的自动化上传脚本已足够。
# 进入环境后应尽快扫描www用户可以写入的路径，如/upload /image，然后使用该脚本保护。

suffix="_bak"

echo -e "Clean webshell from given path(s). \n2017/04/28 by <i@cdxy.me>\n"

if [ ! -n "$1" ]; then
    echo -e "Usage: \n $0 <path1> <path2> ...\nExample: \n $0 /var/www/html/upload /var/www/html/image ..."
    exit 2
fi

while true; do
    read -p "Blacklist Regex (e.g. *.php,[a-zA-Z0-9]*.php): " blacklist
    if [ -n "$blacklist" ];then
        break
    fi
done

read -p "Whitelist Regex (e.g. User.php|Admin.php|.htaccess): " whitelist

echo -e "\n\n===== SCANNING (Quit with [Ctrl-C]) =====\n\n"

while true; do
    for path in $@; do # 遍历输入的路径
        for file in `find $path -name "$blacklist"`; do # 递归遍历指定路径下所有符合正则的文件
            # 白名单保护
            if [ -n "$whitelist" ]; then
                result=$(echo "$file" | grep -E "$whitelist")
                if [[ "$result" != "" ]] ; then
                    continue
                fi
            fi
            # 将webshell备份为无害的后缀
            mv $file ${file}${suffix}
            echo "[!]MOVE: `readlink -f $file` -> ${file}${suffix}"
        done
    done
done