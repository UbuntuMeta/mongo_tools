# -*- coding: utf-8 -*-
import os, json

# os.system('cat /proc/cupinfo')

class MongoShell:
    """
       这是一个mongo操作工具类，封装了常用的mongo命令，如export/import/dump/store....
    """
    def __init__(self):
        self.getConf()
    # 用于切换集合，初始化条件
    def setParams(self, collection, condition):
        self.collection = collection
        self.condition = condition
    # 获取连接数据库等配置
    def getConf(self):
        config_fp = open('./config.json', 'r', encoding='utf-8')
        pure_content = config_fp.read()
        json_obj = json.loads(pure_content)
        self.db = json_obj['db']
        self.user = json_obj['user']
        self.pwd = json_obj['pwd']
        config_fp.close()
    # 导出数据 mongoexport
    def export(self):
        export_cmd = "mongoexport -u %s -p %s  -d %s -c %s -q '%s' -o %s.json --type json" \
                     % (self.user, self.pwd, self.db, self.collection, self.condition, self.collection + '_export')
        print("the cmd:" + export_cmd + "\r\n")
        os.system(export_cmd)
    def import_data(self, file_path):
        export_cmd = "mongoimport -u %s -p %s -d %s -c %s --file %s" % (self.user, self.pwd,  self.db, self.collection, file_path)
        os.system(export_cmd)

    def dump_single_table(self, file_path):
        export_cmd = "mongodump -u %s -p %s --authenticationDatabase %s -d %s -c %s -o %s" % (self.user, self.pwd, self.db, self.db, self.collection, file_path)
        os.system(export_cmd)
    def dump_single_db(self, file_path):
        export_cmd = "mongodump -u %s -p %s --authenticationDatabase %s -d %s -o %s" % (self.user, self.pwd, self.db, self.db, file_path)
        os.system(export_cmd)
    def store(self):
        pass
    def query(self):
        pass

collections = ['iflows', 'company_apps', 'group_users', 'groups', 'iflow_handle_histories']
condition = '{company_id: "561f72fbe419be013b8b468e"}'
shell_obj = MongoShell()
for collection in collections:
    shell_obj.setParams(collection, condition)
    shell_obj.export()
