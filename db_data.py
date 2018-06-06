# -*- coding:utf-8 -*-

import os
#import cx_Oracle


# env SIMPLIFIED CHINESE_CHINA.UTF8
#os.environ['NLS_ALNG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
#os.environ['NLS_ALNG'] = 'AMERICAN_AMERICA.UTF8'
#os.environ['NLS_ALNG'] = 'SIMPLIFIED CHINESE_CHINA.AL32UTF8'
# 获取oracle数据库数据

    
#db_conn,params
def ret_sql_res(db_conn,sql_str,sql_param,rows): 
    err_cur = db_conn.cursor()
    err_cur.execute(sql_str,sql_param)
    if rows:
        res_many = err_cur.fetchmany(rows)
    else:
        res_many = err_cur.fetchall()
    return res_many
