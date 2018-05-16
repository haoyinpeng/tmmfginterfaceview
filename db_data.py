# -*- coding:utf-8 -*-

import cx_Oracle
import CONFIG
import dbsession
import os

db_conn = dbsession.dbconnsingle('apps','debs1apps','DERP').db_conn()
# env SIMPLIFIED CHINESE_CHINA.UTF8
#os.environ['NLS_ALNG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
#os.environ['NLS_ALNG'] = 'AMERICAN_AMERICA.UTF8'
#os.environ['NLS_ALNG'] = 'SIMPLIFIED CHINESE_CHINA.AL32UTF8'
# 获取oracle数据库数据
class get_result():
    def __init__(self,what_res):
        self.what_res = what_res
    
    #db_conn,params
    def exec_sql(self): 
        err_cur = db_conn.cursor()
        err_cur.execute(''' select * 
                      from apps.meserpprodsum m 
                     where process_flag = :flag ''',flag = 'E')
        return err_cur
    
    def get_res_rows(self,cursor_01,rows):
        if rows:
            res_many = cursor_01.fetchmany(rows)
        else:
            res_many = cursor_01.fetchall()
        return res_many

