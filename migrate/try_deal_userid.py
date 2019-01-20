# -*- coding: utf-8 -*-
file = open('./userids.txt', 'r', encoding='utf-8')
#content = file.read()
new_file = open('./newfile.txt', 'w+', encoding='utf-8')
# content = content.replace('MongoDB shell version: 3.2.13','')
# content = content.replace('connecting to: HuaXi','')
line_num = 1
try:
    for line in file.readlines():
        if line_num <= 2:
            line_num+= 1
            continue
        line_num+=1
        new_file.write(line) 
        # if 'MongoDB shell version: 3.2.13' in line:
        #     continue
        # if 'connecting to: HuaXi' in line:
        #     continue
        # else:
        #     new_file.write(line)
finally:
    new_file.close()
    file.close()