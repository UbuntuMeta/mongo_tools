# -*- coding: utf-8 -*-
import sys
sys.path.append(r'/home/rduser/bakmongo/mongo_tools')
from mongo_opt import MongoShell

# 先导出groups,users,group_users,company_users,groups,保存到备份文件夹

simple_collections = ['group_users', 'company_users', 'groups']
huaxi2_company_id = "561f72fbe419be013b8b468e"
condition = '{company_id: "%s"}' % huaxi2_company_id
# print(condition)
mongo = MongoShell()
print(mongo)
mongo.setStorePath('../savebak')
for collection in simple_collections:
    mongo.setParams(collection, condition)
    mongo.export()
#
# # 获取user_id文件
# script_file = "getUserIds.js"
# out_file = "./getUserID.txt"
# mongo.runScript(script_file, out_file)

# 获取满足条件的user_id结果的txt文档
def getUserIdInCondtion(mongo_shell):
    mongo_shell.runScript('/home/rduser/bakmongo/mongo_tools/js_scripts/get_user_id_from_users.js', './userids.txt')
    #{"_id":{$in:[ObjectId("5ae96286f871c94a74741562"),ObjectId("5c403985f871c95522681694")]}}
    file = open('./userids.txt', 'r', encoding='utf-8')
    file_new = open('./user_ids.txt', 'w+', encoding='utf-8')
    # 将前两行删除存入新文件
    line_no = 1
    for line in file.readlines():
        if line_no <=2 :
            line_no +=1
            continue        
        file_new.write(line)
        line_no+=1
    file.close()
    file_new.close()
    return ''

content = getUserIdInCondtion(mongo)
