# -*- coding: utf-8 -*-


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

#以下是要执行的各种sql语句

def sumtable_sql():
    '''
    接收mes数据存放的erp端的中间表 待处理的账务数据
    '''
    str_sql = ''' select * 
                      from apps.meserpprodsum m 
                     where 
                     m.process_flag = :flag 
              '''
    return str_sql

def get_sumtable(workorder=None,status_code=None,process_flag='E'):
    '''
    接收mes数据存放的erp端的中间表 待处理的账务数据
    '''
    str_sql = ''' select * 
                      from apps.meserpprodsum m 
                     where 1=1
              '''
    if workorder:
        str_sql = str_sql+'and workorder = '+workorder
    if status_code:
        str_sql = str_sql+'and status_code = '+status_code
    if process_flag:
        str_sql = str_sql+'and process_flag = '+process_flag

    return str_sql

