#!/usr/bin/python
# -*- encoding:utf-8 -*-
#=========================================
# Filename : music.py
# Filetype : Python
# Author   : Colben
# Create   : 2015-08-04 20:50:17
#=========================================

import sys, os, time, subprocess, re, chardet, urllib, json, threading

def load_lrc(lrc_basename):
    try:
        lrc_contains = open(lrc_basename+'.lrc',  'rb').read()
    except:
        print('\033[4;0H\033[K\t Local lrc not found, checking internet ...')
        try:
            lrc_contains = urllib.urlopen(json.loads(urllib.urlopen('http://geci.me/api/lyric/'+os.path.split(lrc_basename)[1]).read())['result'][0]['lrc']).read()
        except:
            print('\033[4;0H\033[K\t Lrc not found ...')
            return
    # try:
    #     lrc_fp.close()
    # except:
    #     pass
    encoding = chardet.detect(lrc_contains)['encoding']
    if 'utf-8' != encoding:
        lrc_contains = lrc_contains.decode(encoding).encode('utf-8')
    for eachline in re.split(r'\n', lrc_contains):
        line = re.split(r']', eachline)
        if 1 < len(line):
            for tm in line[0:-1]:
                time = re.match(r'(\d\d)\s*:\s*(\d\d)',tm.strip(' [')).groups()
                pos = 60*int(time[0]) + int(time[1])
                lrc[pos] = line[-1]
    return

def main(song):
    global lrc
    lrc = {}
    print('\033[2J\033[2;0H\tPlaying %s ...'%song[:60])
    p = subprocess.Popen('mplayer %s 2>&1'%song, stdout = subprocess.PIPE, shell = True)

    while True:
        match = re.match(r'A:.*[\d:.()]* of (\d+)', p.stdout.read(30))
        if None != p.poll():
            print('\033[9;0H\tFailed to recognize file format .')
            return 1
        if not match:
            output = p.stdout.readline()
        else:
            tot_time = int(match.group(1)) - 1
            for jump in range(1, 10):
                if 70 >= tot_time/jump:
                    break
            #print '\033[15;0H\ttotal time: %d'%tot_time
            break
    print('\033[?25l')
    thread_load_lrc = threading.Thread(target = load_lrc, args = (os.path.splitext(song)[0], ))
    thread_load_lrc.start()
    while True:
        cur_char = p.stdout.read(1)
        if 'A' == cur_char:
            cur_time = int(p.stdout.read(5)[1:])
            print('\033[6;0H\033[K\tCurrent %d / Total %d'%(cur_time, tot_time))
            print('\033[1;0H', '-'*(tot_time/jump))
            print('\033[1;0H', '='*(cur_time/jump))
            print('\033[7;0H', '-'*(tot_time/jump))
            print('\033[7;0H', '='*(cur_time/jump))
            if tot_time <= cur_time:
                print('\033[8;0H\033[K\tquit')
                break
            print('\033[4;0H\033[K\t%s'%lrc[cur_time])
        elif 'E' == cur_char:
            print('\033[8;0H\033[K\tquit')
            break

    p.wait()
    print('\033[10;0H\033[?25h')
    return 0

if '__main__' == __name__:
    if 2 != len(sys.argv) or not os.path.isfile(sys.argv[1]):
        print('\nUsage:', sys.argv[0], '{exist music filename}\n')
    else:
        main(sys.argv[1])
