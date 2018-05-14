# -*- coding: utf-8 -*-

import cx_Oracle
import CONFIG
import os


# env SIMPLIFIED CHINESE_CHINA.UTF8
os.environ['NLS_ALNG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
#os.environ['NLS_ALNG'] = 'AMERICAN_AMERICA.AL32UTF8'
#os.environ['NLS_ALNG'] = 'SIMPLIFIED CHINESE_CHINA.AL32UTF8'
#os.environ['NLS_ALNG'] = 'AMERICAN_AMERICA.UTF8'
#os.environ['LANG'] = 'en_US.UTF-8'
#os.environ['LC_ALL'] = 'en_US.UTF-8'
os.environ['LANG'] = 'zh_CN.UTF-8'
os.environ['LC_ALL'] = 'zh_CN.UTF-8'

print(os.environ)

# tns info
def get_tns(env):
    if env=='PERP':
        return cx_Oracle.makedsn(CONFIG.DB_IP,CONFIG.DB_PORT,CONFIG.DB_INSTANCE_NAME)
    elif env == 'DERP':
        print('DERP..',CONFIG.DB_IP,CONFIG.DB_PORT,CONFIG.DB_INSTANCE_NAME)
        return cx_Oracle.makedsn(CONFIG.DB_IP,CONFIG.DB_PORT,CONFIG.DB_INSTANCE_NAME)
    elif env == 'TERP':
        return cx_Oracle.makedsn(CONFIG.DB_IP,CONFIG.DB_PORT,CONFIG.DB_INSTANCE_NAME)
    

# db connection
def get_db_conn(user_name,passwd,env):
    conn = cx_Oracle.connect(user_name,passwd,get_tns(env))
    return conn

db = get_db_conn('apps','debs1apps','DERP')

print(db)
err_cur = db.cursor()
fnd_cur = db.cursor()

err_cur.execute(''' select * 
                      from apps.meserpprodsum m 
                     where process_flag = :flag ''',flag = 'E')

fnd_cur.execute(''' select user_name,description
                      from apps.fnd_user fu 
                     where fu.user_name like :name 
                       and rownum <= 10''', name = 'B%')

res_err = err_cur.fetchmany(3)
res_fnd = fnd_cur.fetchmany(3)

print(res_err)
print(res_fnd)


db.close()