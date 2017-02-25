import os

dir = raw_input('dir=')
arg = raw_input('arg=')
if len(arg) <= 2:
    print "arg too short!"
    exit(0)
file_list = []
for root, dirs, files in os.walk(dir):
    for file in files:
        file_list.append(os.path.join(root, file))

#print file_list

for filename in file_list:
    fobj = open(filename)

    line_num = 0
    for eachline in fobj.readlines():
        line_num += 1
        if arg in eachline:
            print "\n[*]-----arg Found!-----"
            print "[filename] " + filename
            print "[line] " + str(line_num)
            print "[code] " + eachline
