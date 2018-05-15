# -*- coding:utf-8 -*-

import cx_Oracle
import CONFIG
import os


# env SIMPLIFIED CHINESE_CHINA.UTF8
#os.environ['NLS_ALNG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
#os.environ['NLS_ALNG'] = 'AMERICAN_AMERICA.UTF8'
#os.environ['NLS_ALNG'] = 'SIMPLIFIED CHINESE_CHINA.AL32UTF8'

class get_db():

    def __init__(self,user_name,passwd):
        self.user_name = user_name
        self.passwd = passwd
        print(self.user_name,self.passwd)

    # tns info
    def get_tns(self,env):
        if env=='PERP':
            return cx_Oracle.makedsn(CONFIG.DB_IP,CONFIG.DB_PORT,CONFIG.DB_INSTANCE_NAME)
        elif env == 'DERP':
            print('DERP..',CONFIG.DB_IP,CONFIG.DB_PORT,CONFIG.DB_INSTANCE_NAME)
            return cx_Oracle.makedsn(CONFIG.DB_IP,CONFIG.DB_PORT,CONFIG.DB_INSTANCE_NAME)
        elif env == 'TERP':
            return cx_Oracle.makedsn(CONFIG.DB_IP,CONFIG.DB_PORT,CONFIG.DB_INSTANCE_NAME)
        

    # db connection
    def get_db_conn(self,env):
        return cx_Oracle.connect(self.user_name,self.passwd,self.get_tns(env),encoding = 'UTF-8',nencoding = 'UTF-8') 

db = get_db('apps','debs1apps').get_db_conn('DERP')

print(db)
err_cur = db.cursor()

err_cur.execute(''' select * 
                      from apps.meserpprodsum m 
                     where process_flag = :flag ''',flag = 'E')

res_many = err_cur.fetchmany(3)

print(res_many)


db.close()