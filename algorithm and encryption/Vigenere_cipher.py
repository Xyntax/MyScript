# -*- coding: utf-8 -*
__author__ = 'xy'
'''
密码学上机作业——维吉尼亚加解密算法

由于许久没碰c和java(@v@!) + 最近python使用较多 本次作业使用python3 编写
实现功能：加解密、检测用户输入

13281166 徐越

151012
'''
# get list a-z
alpha = [chr(i) for i in range(97, 123)]
# get list A-Z
xalpha = [chr(i) for i in range(65, 91)]

key = [2, 8, 15, 7, 4, 17]  # CIPHER
keylen = len(key)  # 考虑原文的长度是否比密钥长度大


# Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray
T = '\033[93m'  # tan


def encrypt(rawstring):
    """ENCRYPT FUNCTION"""
    rawlist = list(rawstring)  # 将原字符串分解为字母的列表，变量记为rawlist
    rawlistnum = [0 for i in range(len(rawstring))]  # 原字符串对应数字的列表，变量记为rawlistnum
    rawlen = len(rawlist)
    k = 0
    for item in rawlist:
        for j in range(len(alpha)):
            if item == alpha[j]:
                rawlistnum[k] = j
                k += 1
    resultnum = [0 for i in range(len(rawstring))]  # 加密后各字母所对应的数字的列表，变量记为resultnum
    for i in range(len(rawlistnum)):
        resultnum[i] = (rawlistnum[i] + key[i % keylen]) % 26
    resultchar = [0 for i in range(len(rawstring))]  # 加密后的各字母的列表，变量记为resultchar
    a = 0
    for index in resultnum:
        resultchar[a] = xalpha[index]
        a += 1
    result = ''.join(resultchar)
    return result


def decrypt(rawstring):
    """DECRYPT FUNCTION"""
    rawlist = list(rawstring)
    rawlistnum = [0 for i in range(len(rawstring))]
    rawlen = len(rawlist)
    k = 0
    for item in rawlist:
        for j in range(len(xalpha)):
            if item == xalpha[j]:
                rawlistnum[k] = j
                k = k + 1
    resultnum = [0 for i in range(len(rawstring))]
    for i in range(len(rawlistnum)):
        resultnum[i] = (rawlistnum[i] - key[i % keylen]) % 26  # 解密函数，此处为减法
    resultchar = [0 for i in range(len(rawstring))]
    a = 0
    for index in resultnum:
        resultchar[a] = alpha[index]  # 注意为alpha，非xalpha
        a = a + 1
    result = ''.join(resultchar)
    return result


def main():
    """MAIN FUNCTION"""
    print(B + '   [---]           Vigenere_cipher           [---]' + W)
    print(B + '   [---]       Created by: xuyue 13281166    [---]' + W)
    print(B + '   [---]   Github: http://github.com/Xyntax  [---]' + W)

    print('[' + G + '+' + W + ']' + 'Please Choose the Function:(E)ncrypt,(D)ecrypt')
    choice = input('>')
    if choice == 'E':
        print('[' + G + '+' + W + ']' + 'Please Input the Plaintext:')
        plainstring = input('>')
        if plainstring.isalpha():
            cipherresult = encrypt(plainstring)
            print('[' + G + '+' + W + ']' + 'Encrypt Result:', cipherresult)
        else:
            print('[' + R + '-' + W + ']' + 'Invalid Input')
    elif choice == 'D':
        print('[' + G + '+' + W + ']' + 'Please Input the Ciphertext:')
        cipherstring = input('>')
        if cipherstring.isalpha():
            plainresult = decrypt(cipherstring)
            print('[' + G + '+' + W + ']' + 'Decrypt Result:', plainresult)
        else:
            print('[' + R + '-' + W + ']' + 'Invalid Input')
    else:
        print('[' + R + '-' + W + ']' + 'Invalid Command')


if __name__ == "__main__":
    main()
